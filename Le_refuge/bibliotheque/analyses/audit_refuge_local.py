#!/usr/bin/env python3
"""
Audit Refuge Local - Références Manquantes
==========================================

Version ciblée pour auditer uniquement le projet Le Refuge,
en excluant les bibliothèques externes comme ParlAI, PyTorch-BigGraph, etc.

Auteur: Laurent & Ælya
Date: 26 Mai 2025
"""

import os
import sys
import ast
import importlib
import traceback
from pathlib import Path
from typing import Dict, List
from datetime import datetime
from collections import defaultdict
import json

class AuditeurRefugeLocal:
    """Auditeur ciblé pour Le Refuge uniquement"""
    
    def __init__(self):
        self.racine_projet = Path(".")
        self.exclusions_principales = {
            'ParlAI', 'PyTorch-BigGraph', 'AI-Scientist', 'AI-Scientist-v2',
            'SURPRISES', '.venv', '__pycache__', '.git', 'node_modules',
            '.pytest_cache', 'build', 'dist', 'logs', 'backup_cluster_test',
            'backup_cluster_sacred_20250525_181950', 'backup_coeur_migration',
            'ARCHIVES', 'BROL-DOC', 'NOTES POST CURSOR', 'examples/templates',
            'tools/.venv', 'SOURCE_ORIENTALE'
        }
        
        # 🔍 LISTE DE DÉTECTION: Mots-clés recherchés pour identifier les problèmes (pas des bugs ici)
        self.mots_cles_incomplet = [
            'TODO', 'FIXME', 'HACK', 'XXX', 'BUG', 'TEMP', 'TEMPORARY',
            'PLACEHOLDER', 'NOT IMPLEMENTED', 'INCOMPLETE', 'BROKEN',
            'À FAIRE', 'A FAIRE', 'À DÉVELOPPER', 'A DEVELOPPER',
            'À CORRIGER', 'A CORRIGER', 'INCOMPLET', 'EN COURS'
        ]
    
    def scanner_fichiers_refuge(self) -> List[Path]:
        """Scanne seulement les fichiers Python du refuge principal"""
        print("🔍 Scan des fichiers Python du Refuge...")
        
        fichiers = []
        for chemin in self.racine_projet.rglob("*.py"):
            # Vérifier si le fichier est dans un dossier exclu
            if any(exclus in str(chemin) for exclus in self.exclusions_principales):
                continue
            
            # Inclure seulement les fichiers pertinents
            if (chemin.is_relative_to(self.racine_projet) and 
                not any(part.startswith('.') for part in chemin.parts[1:])):
                fichiers.append(chemin)
        
        print(f"   📁 {len(fichiers)} fichiers Python du Refuge trouvés")
        return fichiers
    
    def analyser_imports_leger(self, chemin_fichier: Path) -> List[Dict]:
        """Analyse légère des imports (sans exécution)"""
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
            
            # Collecter les imports pour analyse statique
            for noeud in ast.walk(arbre):
                if isinstance(noeud, ast.Import):
                    for alias in noeud.names:
                        if self._est_import_refuge_suspect(alias.name):
                            imports_problematiques.append({
                                'fichier': str(chemin_fichier),
                                'type': 'import_suspect',
                                'ligne': noeud.lineno,
                                'module': alias.name,
                                'probleme': f"Import potentiellement problématique: {alias.name}",
                                'gravite': 'moyenne'
                            })
                            
                elif isinstance(noeud, ast.ImportFrom):
                    if noeud.module and self._est_import_refuge_suspect(noeud.module):
                        imports_problematiques.append({
                            'fichier': str(chemin_fichier),
                            'type': 'import_from_suspect',
                            'ligne': noeud.lineno,
                            'module': noeud.module,
                            'probleme': f"Import from potentiellement problématique: {noeud.module}",
                            'gravite': 'moyenne'
                        })
                    
        except Exception as e:
            imports_problematiques.append({
                'fichier': str(chemin_fichier),
                'type': 'erreur_lecture',
                'ligne': 0,
                'probleme': f"Impossible de lire le fichier: {e}",
                'gravite': 'critique'
            })
            
        return imports_problematiques
    
    def _est_import_refuge_suspect(self, nom_module: str) -> bool:
        """Vérifie si un import est suspect (référence interne potentiellement cassée)"""
        # Imports internes suspects
        suspects = [
            'refuge_core', 'base', 'gardiens', 'elements_sacres', 
            'elements_subtils', 'spheres_etendues', 'flux', 'emergences',
            'transformations', 'equilibre', 'evolution', 'integration_spheres'
        ]
        
        # Vérifier si c'est un import relatif du refuge
        if any(suspect in nom_module for suspect in suspects):
            return True
        
        # Vérifier si c'est un import vers un fichier qui n'existe plus
        if nom_module.startswith('.') or 'refuge' in nom_module.lower():
            return True
            
        return False
    
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
    
    def generer_rapport_refuge(self) -> Dict:
        """Génère un rapport ciblé pour Le Refuge"""
        print("\n🎯 AUDIT REFUGE LOCAL - RÉFÉRENCES MANQUANTES")
        print("=" * 50)
        
        # Scanner les fichiers du refuge
        fichiers = self.scanner_fichiers_refuge()
        
        tous_imports_suspects = []
        tous_todos = []
        toutes_fonctions_vides = []
        
        print("\n📊 Analyse en cours...")
        for i, fichier in enumerate(fichiers):
            if i % 5 == 0:
                print(f"   Traité: {i}/{len(fichiers)} fichiers")
            
            # Analyser imports suspects
            imports_suspects = self.analyser_imports_leger(fichier)
            tous_imports_suspects.extend(imports_suspects)
            
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
            'imports_suspects': {
                'total': len(tous_imports_suspects),
                'details': tous_imports_suspects
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
            'fichiers_analyses_liste': [str(f) for f in fichiers]
        }
        
        return rapport
    
    def _compter_todos_par_type(self, todos: List[Dict]) -> Dict:
        """Compte les TODOs par type"""
        compteur = defaultdict(int)
        for item in todos:
            type_todo = item.get('type', 'autre')
            compteur[type_todo] += 1
        return dict(compteur)
    
    def afficher_rapport_console(self, rapport: Dict):
        """Affiche le rapport dans la console de manière lisible"""
        print(f"\n📋 RAPPORT AUDIT REFUGE LOCAL - {rapport['timestamp'][:19]}")
        print("=" * 60)
        
        print(f"\n📊 STATISTIQUES REFUGE")
        print(f"   📁 Fichiers analysés: {rapport['fichiers_analyses']}")
        
        # Imports suspects
        imports = rapport['imports_suspects']
        print(f"\n🔗 IMPORTS SUSPECTS ({imports['total']} total)")
        if imports['total'] > 0:
            print("   📌 Imports à vérifier:")
            for item in imports['details'][:10]:  # Top 10
                print(f"      📄 {Path(item['fichier']).name}:{item['ligne']} - {item['module']}")
                print(f"          {item['probleme']}")
        else:
            print("   ✅ Aucun import suspect détecté!")
        
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
                    print(f"      📄 {Path(item['fichier']).name}:{item['ligne']}")
                    print(f"          {item['contenu'][:100]}...")
        else:
            print("   ✅ Aucun TODO/FIXME trouvé!")
        
        # Fonctions vides
        fonctions = rapport['fonctions_vides']
        print(f"\n🕳️  FONCTIONS VIDES ({fonctions['total']} total)")
        if fonctions['total'] > 0:
            print("   📌 Fonctions à implémenter:")
            for item in fonctions['details'][:10]:  # Top 10
                classe = f" (classe {item['classe']})" if item.get('classe') else ""
                print(f"      📄 {Path(item['fichier']).name}:{item['ligne']} - {item['fonction']}(){classe}")
        else:
            print("   ✅ Aucune fonction vide détectée!")
        
        # Recommandations
        print(f"\n💡 RECOMMANDATIONS POUR LE REFUGE")
        total_problemes = imports['total'] + len([t for t in todos['details'] if t.get('type') == 'correction_urgente']) + fonctions['total']
        
        if total_problemes == 0:
            print("   🎉 FÉLICITATIONS ! Le Refuge est parfaitement harmonieux !")
            print("   ✨ Aucun problème détecté - environnement idéal pour Ælya")
        else:
            if imports['total'] > 0:
                print("   🔧 Vérifier et corriger les imports suspects")
            if any(item.get('type') == 'correction_urgente' for item in todos['details']):
                print("   🔥 Traiter les FIXMEs urgents en priorité")
            if fonctions['total'] > 5:
                print("   🚧 Implémenter les fonctions vides importantes")
        
        print(f"\n📅 Audit Refuge terminé le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🤝 Par: Laurent & Ælya - Équipe Le Refuge")

def main():
    """Point d'entrée principal de l'audit refuge"""
    print("🏛️  AUDITEUR REFUGE LOCAL")
    print("=========================")
    print("Audit ciblé du projet Le Refuge uniquement ✨\n")
    
    auditeur = AuditeurRefugeLocal()
    
    try:
        # Générer le rapport refuge
        rapport = auditeur.generer_rapport_refuge()
        
        # Afficher dans la console
        auditeur.afficher_rapport_console(rapport)
        
        # Sauvegarder le rapport
        fichier_rapport = f"rapport_audit_refuge_local_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n💾 Rapport refuge sauvegardé: {fichier_rapport}")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'audit refuge: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main() 