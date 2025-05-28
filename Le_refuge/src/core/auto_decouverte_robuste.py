#!/usr/bin/env python3
"""
🛡️ Auto-Découverte Robuste du Temple de l'Âme
Version tolérante aux erreurs qui analyse les fichiers sans les importer
"""

import os
import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import defaultdict

class AutoDecouverteRobuste:
    """Système d'auto-découverte robuste et tolérant aux erreurs"""
    
    def __init__(self):
        self.temples_analyses = {}
        self.modules_analyses = {}
        self.connexions_potentielles = []
        self.fonctionnalites_par_categorie = defaultdict(list)
        self.erreurs_rencontrees = []
        
    def decouvrir_temple_robuste(self) -> Dict[str, Any]:
        """Découverte robuste de tout le temple"""
        print("🛡️ ═══════════════════════════════════════════════════════")
        print("        AUTO-DÉCOUVERTE ROBUSTE")
        print("🛡️ ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Analyse statique des temples
        self._analyser_temples_statique()
        
        # 2. Détection des patterns et connexions
        self._detecter_patterns()
        
        # 3. Création de l'interface virtuelle
        interface = self._creer_interface_virtuelle()
        
        # 4. Génération des recommandations
        self._generer_recommandations()
        
        # 5. Rapport final
        self._generer_rapport_robuste()
        
        return interface
    
    def _analyser_temples_statique(self):
        """Analyse statique de tous les temples sans import"""
        print("📊 Analyse statique des temples...")
        
        src_path = Path("src")
        for item in src_path.iterdir():
            if item.is_dir() and item.name.startswith("temple_"):
                temple_name = item.name
                print(f"   🏛️ Analyse: {temple_name}")
                
                temple_info = {
                    'nom': temple_name,
                    'chemin': str(item),
                    'modules': [],
                    'classes_totales': 0,
                    'fonctions_totales': 0,
                    'imports_externes': set(),
                    'imports_internes': set(),
                    'erreurs': []
                }
                
                # Analyse de tous les fichiers Python du temple
                for py_file in item.rglob("*.py"):
                    if py_file.name != "__init__.py":
                        module_info = self._analyser_module_statique(py_file, temple_name)
                        if module_info:
                            temple_info['modules'].append(module_info)
                            temple_info['classes_totales'] += len(module_info['classes'])
                            temple_info['fonctions_totales'] += len(module_info['fonctions'])
                            temple_info['imports_externes'].update(module_info['imports_externes'])
                            temple_info['imports_internes'].update(module_info['imports_internes'])
                
                self.temples_analyses[temple_name] = temple_info
                print(f"      📁 {len(temple_info['modules'])} modules, {temple_info['classes_totales']} classes, {temple_info['fonctions_totales']} fonctions")
        
        print(f"   🏛️ {len(self.temples_analyses)} temples analysés")
        print()
    
    def _analyser_module_statique(self, fichier: Path, temple: str) -> Dict:
        """Analyse statique d'un module sans l'importer"""
        try:
            with open(fichier, 'r', encoding='utf-8', errors='ignore') as f:
                contenu = f.read()
            
            # Parse AST
            try:
                tree = ast.parse(contenu)
            except SyntaxError as e:
                self.erreurs_rencontrees.append(f"Erreur syntaxe {fichier}: {e}")
                return None
            
            # Extraction des informations
            classes = []
            fonctions = []
            imports_externes = set()
            imports_internes = set()
            
            for node in ast.walk(tree):
                # Classes
                if isinstance(node, ast.ClassDef):
                    methodes = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                    classes.append({
                        'nom': node.name,
                        'methodes': methodes,
                        'ligne': node.lineno,
                        'docstring': ast.get_docstring(node) or ""
                    })
                
                # Fonctions
                elif isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
                    fonctions.append({
                        'nom': node.name,
                        'args': [arg.arg for arg in node.args.args],
                        'ligne': node.lineno,
                        'docstring': ast.get_docstring(node) or ""
                    })
                
                # Imports
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.startswith('src.'):
                            imports_internes.add(alias.name)
                        else:
                            imports_externes.add(alias.name)
                
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        if node.module.startswith('src.'):
                            imports_internes.add(node.module)
                        else:
                            imports_externes.add(node.module)
            
            module_info = {
                'nom': fichier.stem,
                'chemin': str(fichier),
                'temple': temple,
                'classes': classes,
                'fonctions': fonctions,
                'imports_externes': imports_externes,
                'imports_internes': imports_internes,
                'lignes': len(contenu.split('\n')),
                'taille': len(contenu)
            }
            
            self.modules_analyses[str(fichier)] = module_info
            return module_info
            
        except Exception as e:
            self.erreurs_rencontrees.append(f"Erreur analyse {fichier}: {e}")
            return None
    
    def _detecter_patterns(self):
        """Détecte les patterns et connexions potentielles"""
        print("🔍 Détection des patterns...")
        
        # Patterns par nom
        patterns_noms = {
            'gestionnaire': [],
            'analyseur': [],
            'generateur': [],
            'visualisation': [],
            'rituel': [],
            'harmonie': [],
            'poesie': [],
            'musique': [],
            'spirituel': []
        }
        
        # Analyse des modules
        for module_info in self.modules_analyses.values():
            nom_module = module_info['nom'].lower()
            
            # Détection par nom
            for pattern, liste in patterns_noms.items():
                if pattern in nom_module:
                    liste.append(module_info)
            
            # Catégorisation des classes
            for classe in module_info['classes']:
                self._categoriser_element(classe, 'classe', module_info)
            
            # Catégorisation des fonctions
            for fonction in module_info['fonctions']:
                self._categoriser_element(fonction, 'fonction', module_info)
        
        # Stockage des patterns
        for pattern, elements in patterns_noms.items():
            if elements:
                self.fonctionnalites_par_categorie[pattern] = elements
        
        # Détection des connexions potentielles
        self._detecter_connexions_potentielles()
        
        print(f"   🔍 {len(self.fonctionnalites_par_categorie)} catégories détectées")
        print(f"   🔗 {len(self.connexions_potentielles)} connexions potentielles")
        print()
    
    def _categoriser_element(self, element: Dict, type_element: str, module_info: Dict):
        """Catégorise un élément (classe ou fonction)"""
        nom = element['nom'].lower()
        
        categories = []
        
        # Analyse du nom
        if any(mot in nom for mot in ['create', 'creer', 'generate', 'generer']):
            categories.append('creation')
        if any(mot in nom for mot in ['analyze', 'analyser', 'process', 'traiter']):
            categories.append('analyse')
        if any(mot in nom for mot in ['transform', 'transformer', 'convert']):
            categories.append('transformation')
        if any(mot in nom for mot in ['visualize', 'visualiser', 'display', 'afficher']):
            categories.append('visualisation')
        if any(mot in nom for mot in ['ritual', 'rituel', 'ceremony']):
            categories.append('rituel')
        if any(mot in nom for mot in ['harmony', 'harmonie', 'resonance']):
            categories.append('harmonie')
        if any(mot in nom for mot in ['poem', 'poeme', 'verse', 'vers']):
            categories.append('poesie')
        if any(mot in nom for mot in ['music', 'musique', 'sound', 'son']):
            categories.append('musique')
        
        # Stockage
        for categorie in categories:
            self.fonctionnalites_par_categorie[categorie].append({
                'type': type_element,
                'element': element,
                'module': module_info['nom'],
                'temple': module_info['temple'],
                'chemin': module_info['chemin']
            })
    
    def _detecter_connexions_potentielles(self):
        """Détecte les connexions potentielles entre modules"""
        
        # Connexions par imports internes
        for module_info in self.modules_analyses.values():
            for import_interne in module_info['imports_internes']:
                self.connexions_potentielles.append({
                    'type': 'import',
                    'source': module_info['nom'],
                    'cible': import_interne,
                    'temple_source': module_info['temple'],
                    'force': 'forte'
                })
        
        # Connexions par similarité de noms
        modules_par_temple = defaultdict(list)
        for module_info in self.modules_analyses.values():
            modules_par_temple[module_info['temple']].append(module_info)
        
        for temple, modules in modules_par_temple.items():
            if len(modules) > 1:
                self.connexions_potentielles.append({
                    'type': 'temple',
                    'elements': [m['nom'] for m in modules],
                    'temple': temple,
                    'force': 'moyenne',
                    'description': f"Modules du même temple {temple}"
                })
    
    def _creer_interface_virtuelle(self) -> Dict[str, Any]:
        """Crée une interface virtuelle unifiée"""
        interface = {
            'temples': self.temples_analyses,
            'modules': self.modules_analyses,
            'fonctionnalites': dict(self.fonctionnalites_par_categorie),
            'connexions': self.connexions_potentielles,
            'statistiques': self._calculer_statistiques(),
            'recommandations': self._generer_recommandations_interface()
        }
        
        return interface
    
    def _calculer_statistiques(self) -> Dict[str, Any]:
        """Calcule les statistiques globales"""
        total_modules = len(self.modules_analyses)
        total_classes = sum(len(m['classes']) for m in self.modules_analyses.values())
        total_fonctions = sum(len(m['fonctions']) for m in self.modules_analyses.values())
        total_lignes = sum(m['lignes'] for m in self.modules_analyses.values())
        
        # Temples les plus riches
        temples_stats = []
        for temple, info in self.temples_analyses.items():
            temples_stats.append({
                'nom': temple,
                'modules': len(info['modules']),
                'classes': info['classes_totales'],
                'fonctions': info['fonctions_totales']
            })
        
        temples_stats.sort(key=lambda x: x['classes'] + x['fonctions'], reverse=True)
        
        return {
            'total_modules': total_modules,
            'total_classes': total_classes,
            'total_fonctions': total_fonctions,
            'total_lignes': total_lignes,
            'temples_count': len(self.temples_analyses),
            'categories_count': len(self.fonctionnalites_par_categorie),
            'connexions_count': len(self.connexions_potentielles),
            'erreurs_count': len(self.erreurs_rencontrees),
            'temples_top': temples_stats[:5]
        }
    
    def _generer_recommandations_interface(self) -> List[Dict]:
        """Génère des recommandations pour améliorer l'interface"""
        recommandations = []
        
        # Temples sans classes
        for temple, info in self.temples_analyses.items():
            if info['classes_totales'] == 0 and info['fonctions_totales'] > 0:
                recommandations.append({
                    'type': 'amelioration',
                    'temple': temple,
                    'description': f"Temple {temple} a {info['fonctions_totales']} fonctions mais aucune classe",
                    'suggestion': "Créer des classes pour organiser les fonctions"
                })
        
        # Modules isolés
        modules_sans_connexion = []
        for module_info in self.modules_analyses.values():
            if not module_info['imports_internes'] and not module_info['imports_externes']:
                modules_sans_connexion.append(module_info['nom'])
        
        if modules_sans_connexion:
            recommandations.append({
                'type': 'connexion',
                'description': f"{len(modules_sans_connexion)} modules sans imports",
                'modules': modules_sans_connexion[:5],
                'suggestion': "Créer des connexions entre ces modules"
            })
        
        return recommandations
    
    def _generer_recommandations(self):
        """Génère des recommandations d'amélioration"""
        self.recommandations = []
        
        # Analyse des erreurs
        if self.erreurs_rencontrees:
            self.recommandations.append({
                'priorite': 'haute',
                'type': 'correction',
                'description': f"{len(self.erreurs_rencontrees)} erreurs détectées",
                'actions': ['Corriger les erreurs de syntaxe', 'Vérifier les imports manquants']
            })
        
        # Temples sous-utilisés
        for temple, info in self.temples_analyses.items():
            if len(info['modules']) > 3 and info['classes_totales'] < 5:
                self.recommandations.append({
                    'priorite': 'moyenne',
                    'type': 'optimisation',
                    'temple': temple,
                    'description': f"Temple {temple} sous-utilisé",
                    'actions': ['Créer plus de classes', 'Organiser les fonctions']
                })
    
    def _generer_rapport_robuste(self):
        """Génère le rapport de découverte robuste"""
        print("📋 RAPPORT D'AUTO-DÉCOUVERTE ROBUSTE")
        print("=" * 45)
        print()
        
        stats = self._calculer_statistiques()
        
        print(f"📊 STATISTIQUES GLOBALES:")
        print(f"   • Temples analysés: {stats['temples_count']}")
        print(f"   • Modules analysés: {stats['total_modules']}")
        print(f"   • Classes découvertes: {stats['total_classes']}")
        print(f"   • Fonctions découvertes: {stats['total_fonctions']}")
        print(f"   • Lignes de code: {stats['total_lignes']:,}")
        print()
        
        print(f"🏛️ TOP TEMPLES:")
        for temple in stats['temples_top']:
            print(f"   • {temple['nom']}: {temple['modules']} modules, {temple['classes']} classes, {temple['fonctions']} fonctions")
        print()
        
        print(f"📂 CATÉGORIES DÉTECTÉES ({len(self.fonctionnalites_par_categorie)}):")
        for categorie, elements in self.fonctionnalites_par_categorie.items():
            print(f"   • {categorie}: {len(elements)} éléments")
        print()
        
        print(f"🔗 CONNEXIONS POTENTIELLES: {len(self.connexions_potentielles)}")
        
        if self.erreurs_rencontrees:
            print(f"\n⚠️ ERREURS DÉTECTÉES ({len(self.erreurs_rencontrees)}):")
            for erreur in self.erreurs_rencontrees[:5]:
                print(f"   • {erreur}")
            if len(self.erreurs_rencontrees) > 5:
                print(f"   • ... et {len(self.erreurs_rencontrees) - 5} autres")
        
        print("\n🎯 CAPACITÉS ROBUSTES ACTIVÉES:")
        print("   ✅ Analyse statique sans import")
        print("   🛡️ Tolérance aux erreurs de syntaxe")
        print("   🔍 Détection automatique des patterns")
        print("   🔗 Connexions virtuelles intelligentes")
        print("   📊 Statistiques complètes du temple")
        
        # Sauvegarde
        interface = self._creer_interface_virtuelle()
        with open("bibliotheque/apprentissage/interface_robuste.json", "w", encoding="utf-8") as f:
            # Sérialisation sécurisée avec conversion des sets
            def convert_sets(obj):
                if isinstance(obj, set):
                    return list(obj)
                elif isinstance(obj, dict):
                    return {k: convert_sets(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_sets(item) for item in obj]
                return obj
            
            interface_safe = {
                'temples': {k: convert_sets({key: val for key, val in v.items() if isinstance(val, (str, int, list, dict, set))}) 
                           for k, v in interface['temples'].items()},
                'statistiques': convert_sets(interface['statistiques']),
                'fonctionnalites_count': {k: len(v) for k, v in interface['fonctionnalites'].items()},
                'connexions_count': len(interface['connexions']),
                'recommandations': convert_sets(interface['recommandations'])
            }
            json.dump(interface_safe, f, indent=2, ensure_ascii=False)
        
        print("\n💾 Interface robuste sauvegardée: bibliotheque/apprentissage/interface_robuste.json")

if __name__ == "__main__":
    auto_decouverte = AutoDecouverteRobuste()
    interface = auto_decouverte.decouvrir_temple_robuste()
    print(f"\n🎉 Découverte robuste terminée ! {len(interface['temples'])} temples analysés.") 