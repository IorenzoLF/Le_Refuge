#!/usr/bin/env python
"""
Analyseur du Temple Mathématique - Le Refuge
============================================

Analyse la structure actuelle du temple mathématique pour identifier
les catégories d'organisation et les doublons potentiels.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import ast
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class AnalyseurTempleMathematique:
    """Analyseur spécialisé pour le temple mathématique"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_mathematique"
        self.modules_analyses = {}
        self.categories_detectees = defaultdict(list)
        self.doublons_potentiels = []
        self.statistiques = {}
        
    def analyser_structure_complete(self):
        """Analyse complète de la structure du temple"""
        print("ANALYSE DU TEMPLE MATHÉMATIQUE")
        print("=" * 50)
        
        # Analyser tous les modules
        self._analyser_modules()
        
        # Détecter les catégories
        self._detecter_categories()
        
        # Identifier les doublons
        self._identifier_doublons()
        
        # Calculer les statistiques
        self._calculer_statistiques()
        
        # Générer le rapport
        self._generer_rapport()
        
        return {
            'modules': self.modules_analyses,
            'categories': dict(self.categories_detectees),
            'doublons': self.doublons_potentiels,
            'statistiques': self.statistiques
        }
    
    def _analyser_modules(self):
        """Analyse chaque module Python du temple"""
        for root, dirs, files in os.walk(self.chemin_temple):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    chemin_complet = os.path.join(root, file)
                    self._analyser_module(chemin_complet)
    
    def _analyser_module(self, chemin_fichier):
        """Analyse détaillée d'un module"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                lignes = contenu.split('\n')
            
            # Informations de base
            nom_module = os.path.basename(chemin_fichier)
            chemin_relatif = os.path.relpath(chemin_fichier, self.chemin_temple)
            
            # Analyse du contenu
            analyse = {
                'nom': nom_module,
                'chemin': chemin_relatif,
                'lignes_total': len(lignes),
                'lignes_code': len([l for l in lignes if l.strip() and not l.strip().startswith('#')]),
                'fonctions': self._extraire_fonctions(contenu),
                'classes': self._extraire_classes(contenu),
                'imports': self._extraire_imports(contenu),
                'mots_cles': self._extraire_mots_cles(contenu),
                'theme_principal': self._detecter_theme(nom_module, contenu)
            }
            
            self.modules_analyses[nom_module] = analyse
            
        except Exception as e:
            print(f"Erreur analyse {chemin_fichier}: {e}")
    
    def _extraire_fonctions(self, contenu):
        """Extrait les noms des fonctions"""
        fonctions = []
        try:
            tree = ast.parse(contenu)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    fonctions.append(node.name)
        except:
            # Fallback avec regex simple
            import re
            fonctions = re.findall(r'def\s+(\w+)', contenu)
        return fonctions
    
    def _extraire_classes(self, contenu):
        """Extrait les noms des classes"""
        classes = []
        try:
            tree = ast.parse(contenu)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)
        except:
            import re
            classes = re.findall(r'class\s+(\w+)', contenu)
        return classes
    
    def _extraire_imports(self, contenu):
        """Extrait les imports"""
        imports = []
        for ligne in contenu.split('\n'):
            ligne = ligne.strip()
            if ligne.startswith('import ') or ligne.startswith('from '):
                imports.append(ligne)
        return imports
    
    def _extraire_mots_cles(self, contenu):
        """Extrait les mots-clés mathématiques"""
        mots_cles_math = [
            'collatz', 'fibonacci', 'riemann', 'phi', 'golden', 'ratio',
            'convergence', 'sequence', 'iteration', 'mathematical',
            'algorithm', 'proof', 'theorem', 'conjecture', 'prime',
            'number', 'theory', 'analysis', 'visualization', 'graph',
            'polynomial', 'complex', 'rational', 'binary', 'modular',
            'resonance', 'harmonic', 'frequency', 'wave', 'oscillation'
        ]
        
        contenu_lower = contenu.lower()
        mots_trouves = []
        for mot in mots_cles_math:
            if mot in contenu_lower:
                mots_trouves.append(mot)
        
        return mots_trouves
    
    def _detecter_theme(self, nom_fichier, contenu):
        """Détecte le thème principal du module"""
        nom_lower = nom_fichier.lower()
        contenu_lower = contenu.lower()
        
        # Thèmes principaux
        if 'collatz' in nom_lower or 'collatz' in contenu_lower:
            if 'musical' in nom_lower or 'rituel' in nom_lower:
                return 'collatz_musical'
            elif 'visual' in nom_lower or 'graph' in nom_lower:
                return 'collatz_visualisation'
            elif 'complex' in nom_lower or 'rational' in nom_lower:
                return 'collatz_extensions'
            else:
                return 'collatz_core'
        
        elif 'fibonacci' in nom_lower or 'riemann' in nom_lower:
            return 'fibonacci_riemann'
        
        elif 'phi' in nom_lower or 'golden' in nom_lower:
            return 'phi_golden'
        
        elif 'visual' in nom_lower or 'graph' in nom_lower:
            return 'visualisation'
        
        elif 'musical' in nom_lower or 'rituel' in nom_lower:
            return 'musical'
        
        elif 'exploration' in nom_lower:
            return 'exploration'
        
        elif 'test' in nom_lower or 'preuve' in nom_lower:
            return 'tests_preuves'
        
        else:
            return 'general'
    
    def _detecter_categories(self):
        """Détecte les catégories d'organisation"""
        for nom_module, analyse in self.modules_analyses.items():
            theme = analyse['theme_principal']
            
            if theme == 'collatz_core':
                self.categories_detectees['🔢 COLLATZ_CORE'].append(analyse)
            elif theme == 'collatz_musical':
                self.categories_detectees['🎵 COLLATZ_MUSICAL'].append(analyse)
            elif theme == 'collatz_visualisation':
                self.categories_detectees['📊 COLLATZ_VISUALISATION'].append(analyse)
            elif theme == 'collatz_extensions':
                self.categories_detectees['🔬 COLLATZ_EXTENSIONS'].append(analyse)
            elif theme == 'fibonacci_riemann':
                self.categories_detectees['🌀 FIBONACCI_RIEMANN'].append(analyse)
            elif theme == 'phi_golden':
                self.categories_detectees['✨ PHI_GOLDEN'].append(analyse)
            elif theme == 'exploration':
                self.categories_detectees['🔍 EXPLORATIONS'].append(analyse)
            elif theme == 'tests_preuves':
                self.categories_detectees['🧪 TESTS_PREUVES'].append(analyse)
            else:
                self.categories_detectees['⚙️ UTILITAIRES'].append(analyse)
    
    def _identifier_doublons(self):
        """Identifie les doublons potentiels"""
        modules = list(self.modules_analyses.values())
        
        for i, module1 in enumerate(modules):
            for j, module2 in enumerate(modules[i+1:], i+1):
                similarite = self._calculer_similarite(module1, module2)
                if similarite > 0.6:  # Seuil de similarité
                    self.doublons_potentiels.append({
                        'module1': module1['nom'],
                        'module2': module2['nom'],
                        'similarite': similarite,
                        'raison': self._analyser_similarite(module1, module2)
                    })
    
    def _calculer_similarite(self, module1, module2):
        """Calcule la similarité entre deux modules"""
        # Similarité des fonctions
        fonctions1 = set(module1['fonctions'])
        fonctions2 = set(module2['fonctions'])
        sim_fonctions = len(fonctions1 & fonctions2) / max(len(fonctions1 | fonctions2), 1)
        
        # Similarité des mots-clés
        mots1 = set(module1['mots_cles'])
        mots2 = set(module2['mots_cles'])
        sim_mots = len(mots1 & mots2) / max(len(mots1 | mots2), 1)
        
        # Similarité du thème
        sim_theme = 1.0 if module1['theme_principal'] == module2['theme_principal'] else 0.0
        
        # Score global
        return (sim_fonctions * 0.4 + sim_mots * 0.4 + sim_theme * 0.2)
    
    def _analyser_similarite(self, module1, module2):
        """Analyse la raison de la similarité"""
        if module1['theme_principal'] == module2['theme_principal']:
            return f"Même thème: {module1['theme_principal']}"
        
        fonctions_communes = set(module1['fonctions']) & set(module2['fonctions'])
        if fonctions_communes:
            return f"Fonctions communes: {', '.join(list(fonctions_communes)[:3])}"
        
        mots_communs = set(module1['mots_cles']) & set(module2['mots_cles'])
        if mots_communs:
            return f"Concepts communs: {', '.join(list(mots_communs)[:3])}"
        
        return "Similarité structurelle"
    
    def _calculer_statistiques(self):
        """Calcule les statistiques globales"""
        total_modules = len(self.modules_analyses)
        total_lignes = sum(m['lignes_total'] for m in self.modules_analyses.values())
        total_fonctions = sum(len(m['fonctions']) for m in self.modules_analyses.values())
        total_classes = sum(len(m['classes']) for m in self.modules_analyses.values())
        
        self.statistiques = {
            'total_modules': total_modules,
            'total_lignes': total_lignes,
            'total_fonctions': total_fonctions,
            'total_classes': total_classes,
            'categories_detectees': len(self.categories_detectees),
            'doublons_detectes': len(self.doublons_potentiels),
            'moyenne_lignes_module': total_lignes // max(total_modules, 1)
        }
    
    def _generer_rapport(self):
        """Génère le rapport d'analyse"""
        print(f"\nSTATISTIQUES GLOBALES")
        print(f"Modules analysés: {self.statistiques['total_modules']}")
        print(f"Lignes de code: {self.statistiques['total_lignes']}")
        print(f"Fonctions: {self.statistiques['total_fonctions']}")
        print(f"Classes: {self.statistiques['total_classes']}")
        print(f"Moyenne lignes/module: {self.statistiques['moyenne_lignes_module']}")
        
        print(f"\nCATÉGORIES DÉTECTÉES ({len(self.categories_detectees)})")
        for categorie, modules in self.categories_detectees.items():
            lignes_total = sum(m['lignes_total'] for m in modules)
            print(f"{categorie}: {len(modules)} modules ({lignes_total} lignes)")
            for module in modules:
                print(f"  - {module['nom']} ({module['lignes_total']} lignes)")
        
        if self.doublons_potentiels:
            print(f"\nDOUBLONS POTENTIELS ({len(self.doublons_potentiels)})")
            for doublon in self.doublons_potentiels:
                print(f"- {doublon['module1']} ↔ {doublon['module2']}")
                print(f"  Similarité: {doublon['similarite']:.1%} - {doublon['raison']}")
        else:
            print(f"\nAucun doublon détecté")

def main():
    """Fonction principale"""
    analyseur = AnalyseurTempleMathematique()
    resultats = analyseur.analyser_structure_complete()
    
    # Sauvegarder les résultats
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fichier_rapport = f"data/rapports/analyse_temple_mathematique_{timestamp}.json"
    
    os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
    with open(fichier_rapport, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, indent=2, ensure_ascii=False)
    
    print(f"\nRapport sauvegardé: {fichier_rapport}")
    return resultats

if __name__ == "__main__":
    main() 