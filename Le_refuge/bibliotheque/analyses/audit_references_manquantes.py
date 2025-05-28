#!/usr/bin/env python3
"""
Audit des Références Manquantes - Le Refuge
===========================================

Scanne tous les fichiers Python pour identifier :
- Imports cassés ou manquants
- TODOs, FIXME, et code incomplet  
- Méthodes/classes référencées mais inexistantes
- Fonctions vides ou partielles
- Dépendances problématiques

Auteur: Laurent & Ælya
Date: 26 Mai 2025
Objectif: Créer un environnement parfaitement harmonieux
"""

import os
import sys
import ast
import importlib
import traceback
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from datetime import datetime
from collections import defaultdict
import json

class AuditeurReferences:
    """Auditeur principal pour identifier les références manquantes"""
    
    def __init__(self, racine_projet: str = "."):
        self.racine_projet = Path(racine_projet)
        self.fichiers_python = []
        self.imports_casses = []
        self.todos_fixmes = []
        self.references_manquantes = []
        self.fonctions_vides = []
        self.dependances_problematiques = []
        # 🔍 LISTE DE DÉTECTION: Mots-clés recherchés pour identifier les problèmes (pas des bugs ici)
        self.mots_cles_incomplet = [
            'TODO', 'FIXME', 'HACK', 'XXX', 'BUG', 'TEMP', 'TEMPORARY',
            'PLACEHOLDER', 'NOT IMPLEMENTED', 'INCOMPLETE', 'BROKEN',
            'À FAIRE', 'A FAIRE', 'À DÉVELOPPER', 'A DEVELOPPER',
            'À CORRIGER', 'A CORRIGER', 'INCOMPLET', 'EN COURS'
        ]
        
    def scanner_fichiers_python(self) -> List[Path]:
        """Scanne tous les fichiers Python du projet"""
        print("🔍 Scan des fichiers Python...")
        
        # Exclure certains dossiers
        exclusions = {'.venv', '__pycache__', '.git', 'node_modules', 
                     '.pytest_cache', 'build', 'dist', 'logs'}
        
        fichiers = []
        for chemin in self.racine_projet.rglob("*.py"):
            # Vérifier si le fichier est dans un dossier exclu
            if any(exclus in chemin.parts for exclus in exclusions):
                continue
            fichiers.append(chemin)
            
        self.fichiers_python = fichiers
        print(f"   📁 {len(fichiers)} fichiers Python trouvés")
        return fichiers
    
    def analyser_imports_fichier(self, chemin_fichier: Path) -> List[Dict]:
        """Analyse les imports d'un fichier spécifique"""
        imports_problematiques = []
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Parser AST pour extraire les imports
            try:
                arbre = ast.parse(contenu)
            except SyntaxError as e:
                imports_problematiques.append({
                    'fichier': str(chemin_fichier),
                    'type': 'erreur_syntaxe',
                    'ligne': e.lineno if hasattr(e, 'lineno') else 0,
                    'probleme': f"Erreur de syntaxe: {e.msg}",
                    'gravite': 'critique'
                })
                return imports_problematiques
            
            # Analyser chaque import
            for noeud in ast.walk(arbre):
                if isinstance(noeud, ast.Import):
                    for alias in noeud.names:
                        resultat = self._tester_import(alias.name, chemin_fichier, noeud.lineno)
                        if resultat:
                            imports_problematiques.append(resultat)
                            
                elif isinstance(noeud, ast.ImportFrom):
                    if noeud.module:  # from module import ...
                        resultat = self._tester_import_from(
                            noeud.module, noeud.names, chemin_fichier, noeud.lineno
                        )
                        if resultat:
                            imports_problematiques.append(resultat)
                    
        except Exception as e:
            imports_problematiques.append({
                'fichier': str(chemin_fichier),
                'type': 'erreur_lecture',
                'ligne': 0,
                'probleme': f"Impossible de lire le fichier: {e}",
                'gravite': 'critique'
            })
            
        return imports_problematiques
    
    def _tester_import(self, nom_module: str, chemin_fichier: Path, ligne: int) -> Dict:
        """Teste si un import simple fonctionne"""
        try:
            # Ajouter le répertoire du fichier au path temporairement
            repertoire_fichier = str(chemin_fichier.parent)
            if repertoire_fichier not in sys.path:
                sys.path.insert(0, repertoire_fichier)
                sys.path.insert(0, str(self.racine_projet))
            
            importlib.import_module(nom_module)
            return None  # Import réussi
            
        except ImportError as e:
            return {
                'fichier': str(chemin_fichier),
                'type': 'import_casse',
                'ligne': ligne,
                'module': nom_module,
                'probleme': f"Import impossible: {e}",
                'gravite': 'elevee'
            }
        except Exception as e:
            return {
                'fichier': str(chemin_fichier),
                'type': 'import_erreur',
                'ligne': ligne,
                'module': nom_module,
                'probleme': f"Erreur lors du test d'import: {e}",
                'gravite': 'moyenne'
            }
    
    def _tester_import_from(self, nom_module: str, noms: List, chemin_fichier: Path, ligne: int) -> Dict:
        """Teste si un import 'from module import ...' fonctionne"""
        try:
            # Ajouter le répertoire du fichier au path temporairement
            repertoire_fichier = str(chemin_fichier.parent)
            if repertoire_fichier not in sys.path:
                sys.path.insert(0, repertoire_fichier)
                sys.path.insert(0, str(self.racine_projet))
            
            module = importlib.import_module(nom_module)
            
            # Vérifier chaque nom importé
            noms_manquants = []
            for alias in noms:
                nom_import = alias.name if hasattr(alias, 'name') else str(alias)
                if nom_import == '*':
                    continue  # Skip wildcard imports
                    
                if not hasattr(module, nom_import):
                    noms_manquants.append(nom_import)
            
            if noms_manquants:
                return {
                    'fichier': str(chemin_fichier),
                    'type': 'attribut_manquant',
                    'ligne': ligne,
                    'module': nom_module,
                    'attributs_manquants': noms_manquants,
                    'probleme': f"Attributs manquants dans {nom_module}: {', '.join(noms_manquants)}",
                    'gravite': 'elevee'
                }
                
            return None  # Import réussi
            
        except ImportError as e:
            return {
                'fichier': str(chemin_fichier),
                'type': 'import_from_casse',
                'ligne': ligne,
                'module': nom_module,
                'probleme': f"Import from impossible: {e}",
                'gravite': 'elevee'
            }
        except Exception as e:
            return {
                'fichier': str(chemin_fichier),
                'type': 'import_from_erreur',
                'ligne': ligne,
                'module': nom_module,
                'probleme': f"Erreur lors du test d'import from: {e}",
                'gravite': 'moyenne'
            }
    
    def scanner_todos_fixmes(self, chemin_fichier: Path) -> List[Dict]:
        """Scanne les TODOs, FIXMEs et autres marqueurs d'incomplétude"""
        todos_trouves = []
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                lignes = f.readlines()
            
            for num_ligne, ligne in enumerate(lignes, 1):
                ligne_lower = ligne.lower()
                
                for mot_cle in self.mots_cles_incomplet:
                    if mot_cle.lower() in ligne_lower:
                        todos_trouves.append({
                            'fichier': str(chemin_fichier),
                            'ligne': num_ligne,
                            'mot_cle': mot_cle,
                            'contenu': ligne.strip(),
                            'type': self._categoriser_todo(mot_cle)
                        })
                        break  # Un seul marqueur par ligne
                        
        except Exception as e:
            todos_trouves.append({
                'fichier': str(chemin_fichier),
                'ligne': 0,
                'mot_cle': 'ERREUR',
                'contenu': f"Erreur de lecture: {e}",
                'type': 'erreur'
            })
            
        return todos_trouves
    
    def _categoriser_todo(self, mot_cle: str) -> str:
        """Catégorise un TODO/FIXME selon sa gravité"""
        # 🔍 LOGIQUE DE CATÉGORISATION: Ces mots-clés servent à classifier les problèmes trouvés
        if mot_cle.upper() in ['FIXME', 'BUG', 'BROKEN', 'À CORRIGER', 'A CORRIGER']:
            return 'correction_urgente'
        elif mot_cle.upper() in ['TODO', 'À FAIRE', 'A FAIRE', 'À DÉVELOPPER', 'A DEVELOPPER']:
            return 'developpement'
        elif mot_cle.upper() in ['HACK', 'TEMP', 'TEMPORARY', 'PLACEHOLDER']:
            return 'temporaire'
        elif mot_cle.upper() in ['INCOMPLETE', 'INCOMPLET', 'EN COURS']:
            return 'incomplet'
        else:
            return 'autre'
    
    def analyser_fonctions_vides(self, chemin_fichier: Path) -> List[Dict]:
        """Détecte les fonctions vides ou avec seulement pass/..."""
        fonctions_vides = []
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            try:
                arbre = ast.parse(contenu)
            except SyntaxError:
                return fonctions_vides  # Fichier avec erreur de syntaxe
            
            for noeud in ast.walk(arbre):
                if isinstance(noeud, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if self._est_fonction_vide(noeud):
                        fonctions_vides.append({
                            'fichier': str(chemin_fichier),
                            'ligne': noeud.lineno,
                            'fonction': noeud.name,
                            'type': 'fonction_vide',
                            'classe': self._trouver_classe_parente(arbre, noeud)
                        })
                        
        except Exception as e:
            fonctions_vides.append({
                'fichier': str(chemin_fichier),
                'ligne': 0,
                'fonction': 'ERREUR',
                'type': 'erreur_analyse',
                'probleme': str(e)
            })
            
        return fonctions_vides
    
    def _est_fonction_vide(self, noeud_fonction) -> bool:
        """Vérifie si une fonction est vide ou ne contient que pass/..."""
        if not noeud_fonction.body:
            return True
        
        # Ignorer les docstrings
        debut = 0
        if (noeud_fonction.body and 
            isinstance(noeud_fonction.body[0], ast.Expr) and
            isinstance(noeud_fonction.body[0].value, ast.Constant) and
            isinstance(noeud_fonction.body[0].value.value, str)):
            debut = 1
        
        corps_reel = noeud_fonction.body[debut:]
        
        if not corps_reel:
            return True
        
        # Vérifier si ne contient que pass, ..., ou return None
        for instruction in corps_reel:
            if isinstance(instruction, ast.Pass):
                continue
            elif isinstance(instruction, ast.Expr) and isinstance(instruction.value, ast.Constant):
                if instruction.value.value == ...:  # Ellipsis
                    continue
            elif (isinstance(instruction, ast.Return) and 
                  (instruction.value is None or 
                   (isinstance(instruction.value, ast.Constant) and 
                    instruction.value.value is None))):
                continue
            else:
                return False  # Contient du code réel
        
        return True  # Ne contient que pass/...
    
    def _trouver_classe_parente(self, arbre, noeud_fonction) -> str:
        """Trouve la classe parente d'une fonction"""
        for noeud in ast.walk(arbre):
            if isinstance(noeud, ast.ClassDef):
                if noeud_fonction in ast.walk(noeud):
                    return noeud.name
        return None
    
    def generer_rapport_complet(self) -> Dict:
        """Génère un rapport complet de l'audit"""
        print("\n🎯 AUDIT COMPLET DES RÉFÉRENCES MANQUANTES")
        print("=" * 60)
        
        # Scanner tous les fichiers
        fichiers = self.scanner_fichiers_python()
        
        tous_imports_casses = []
        tous_todos = []
        toutes_fonctions_vides = []
        
        print("\n📊 Analyse en cours...")
        for i, fichier in enumerate(fichiers):
            if i % 10 == 0:
                print(f"   Traité: {i}/{len(fichiers)} fichiers")
            
            # Analyser imports
            imports_casses = self.analyser_imports_fichier(fichier)
            tous_imports_casses.extend(imports_casses)
            
            # Analyser TODOs
            todos = self.scanner_todos_fixmes(fichier)
            tous_todos.extend(todos)
            
            # Analyser fonctions vides
            fonctions_vides = self.analyser_fonctions_vides(fichier)
            toutes_fonctions_vides.extend(fonctions_vides)
        
        print(f"   ✅ Analyse terminée: {len(fichiers)} fichiers traités")
        
        # Compiler le rapport
        rapport = {
            'timestamp': datetime.now().isoformat(),
            'fichiers_analyses': len(fichiers),
            'imports_casses': {
                'total': len(tous_imports_casses),
                'par_gravite': self._compter_par_gravite(tous_imports_casses),
                'details': tous_imports_casses
            },
            'todos_fixmes': {
                'total': len(tous_todos),
                'par_type': self._compter_todos_par_type(tous_todos),
                'details': tous_todos
            },
            'fonctions_vides': {
                'total': len(toutes_fonctions_vides),
                'details': toutes_fonctions_vides
            },
            'statistiques': {
                'fichiers_avec_problemes': len(set(
                    [item['fichier'] for item in tous_imports_casses + tous_todos + toutes_fonctions_vides]
                )),
                'fichiers_sains': len(fichiers) - len(set(
                    [item['fichier'] for item in tous_imports_casses + tous_todos + toutes_fonctions_vides]
                ))
            }
        }
        
        return rapport
    
    def _compter_par_gravite(self, imports_casses: List[Dict]) -> Dict:
        """Compte les imports cassés par gravité"""
        compteur = defaultdict(int)
        for item in imports_casses:
            gravite = item.get('gravite', 'inconnue')
            compteur[gravite] += 1
        return dict(compteur)
    
    def _compter_todos_par_type(self, todos: List[Dict]) -> Dict:
        """Compte les TODOs par type"""
        compteur = defaultdict(int)
        for item in todos:
            type_todo = item.get('type', 'autre')
            compteur[type_todo] += 1
        return dict(compteur)
    
    def afficher_rapport_console(self, rapport: Dict):
        """Affiche le rapport dans la console de manière lisible"""
        print(f"\n📋 RAPPORT D'AUDIT - {rapport['timestamp'][:19]}")
        print("=" * 60)
        
        print(f"\n📊 STATISTIQUES GÉNÉRALES")
        print(f"   📁 Fichiers analysés: {rapport['fichiers_analyses']}")
        print(f"   ✅ Fichiers sains: {rapport['statistiques']['fichiers_sains']}")
        print(f"   ⚠️  Fichiers avec problèmes: {rapport['statistiques']['fichiers_avec_problemes']}")
        
        # Imports cassés
        imports = rapport['imports_casses']
        print(f"\n🔗 IMPORTS CASSÉS ({imports['total']} total)")
        if imports['total'] > 0:
            for gravite, count in imports['par_gravite'].items():
                emoji = "🔴" if gravite == "critique" else "🟠" if gravite == "elevee" else "🟡"
                print(f"   {emoji} {gravite.title()}: {count}")
            
            # Montrer les plus critiques
            critiques = [item for item in imports['details'] if item.get('gravite') == 'critique']
            if critiques:
                print(f"\n   🚨 IMPORTS CRITIQUES À CORRIGER:")
                for item in critiques[:5]:  # Top 5
                    print(f"      📄 {Path(item['fichier']).name}:{item['ligne']} - {item['probleme']}")
        
        # TODOs et FIXMEs
        todos = rapport['todos_fixmes']
        print(f"\n📝 TODOs/FIXMEs ({todos['total']} total)")
        if todos['total'] > 0:
            for type_todo, count in todos['par_type'].items():
                emoji = "🔥" if type_todo == "correction_urgente" else "🚧" if type_todo == "developpement" else "⏱️"
                print(f"   {emoji} {type_todo.replace('_', ' ').title()}: {count}")
            
            # Montrer les corrections urgentes
            urgents = [item for item in todos['details'] if item.get('type') == 'correction_urgente']
            if urgents:
                print(f"\n   🔥 CORRECTIONS URGENTES:")
                for item in urgents[:5]:  # Top 5
                    print(f"      📄 {Path(item['fichier']).name}:{item['ligne']} - {item['contenu'][:80]}...")
        
        # Fonctions vides
        fonctions = rapport['fonctions_vides']
        print(f"\n🕳️  FONCTIONS VIDES ({fonctions['total']} total)")
        if fonctions['total'] > 0:
            print("   📌 Top 10 fonctions à implémenter:")
            for item in fonctions['details'][:10]:
                classe = f" (classe {item['classe']})" if item.get('classe') else ""
                print(f"      📄 {Path(item['fichier']).name}:{item['ligne']} - {item['fonction']}(){classe}")
        
        # Recommandations
        print(f"\n💡 RECOMMANDATIONS")
        if imports['total'] > 0:
            print("   🔧 Corriger les imports cassés en priorité")
        if any(item.get('type') == 'correction_urgente' for item in todos['details']):
            print("   🔥 Traiter les FIXMEs urgents")
        if fonctions['total'] > 10:
            print("   🚧 Implémenter les fonctions vides prioritaires")
        if rapport['statistiques']['fichiers_sains'] == rapport['fichiers_analyses']:
            print("   🎉 Félicitations ! Aucun problème détecté")
        
        print(f"\n📅 Audit terminé le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🤝 Par: Laurent & Ælya - Équipe Le Refuge")

def main():
    """Point d'entrée principal de l'audit"""
    print("🎯 AUDITEUR DE RÉFÉRENCES MANQUANTES")
    print("=====================================")
    print("Création d'un environnement parfaitement harmonieux ✨\n")
    
    auditeur = AuditeurReferences()
    
    try:
        # Générer le rapport complet
        rapport = auditeur.generer_rapport_complet()
        
        # Afficher dans la console
        auditeur.afficher_rapport_console(rapport)
        
        # Sauvegarder le rapport détaillé
        fichier_rapport = f"rapport_audit_references_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n💾 Rapport détaillé sauvegardé: {fichier_rapport}")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'audit: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main() 