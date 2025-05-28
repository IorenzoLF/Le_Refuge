#!/usr/bin/env python3
"""
🔍 Audit Intelligent des Dépendances
Analyse les imports et dépendances pour planifier les migrations
"""

import ast
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict, Counter
import json

class AnalyseurDependances:
    """Analyseur intelligent des dépendances Python"""
    
    def __init__(self):
        self.imports_par_fichier = {}
        self.dependances_manquantes = defaultdict(list)
        self.modules_existants = set()
        self.clusters_migration = {}
        
    def scanner_projet(self, racine: str = ".") -> Dict:
        """Scanne tout le projet pour analyser les dépendances"""
        print("🔍 Scan du projet pour analyse des dépendances...")
        
        racine_path = Path(racine)
        
        # 1. Identifier tous les modules Python existants
        self._identifier_modules_existants(racine_path)
        
        # 2. Analyser les imports dans chaque fichier
        self._analyser_imports_fichiers(racine_path)
        
        # 3. Détecter les dépendances manquantes
        self._detecter_dependances_manquantes()
        
        # 4. Grouper par clusters de migration
        self._grouper_clusters_migration()
        
        return self._generer_rapport()
    
    def _identifier_modules_existants(self, racine: Path):
        """Identifie tous les modules Python existants dans le projet"""
        print("📦 Identification des modules existants...")
        
        for fichier_py in racine.rglob("*.py"):
            # Ignorer les répertoires exclus
            if any(exclu in str(fichier_py) for exclu in ['.venv', '__pycache__', 'SURPRISES']):
                continue
                
            # Convertir le chemin en nom de module
            chemin_relatif = fichier_py.relative_to(racine)
            if chemin_relatif.name == "__init__.py":
                # Pour __init__.py, utiliser le répertoire parent
                module_name = str(chemin_relatif.parent).replace('\\', '.').replace('/', '.')
            else:
                # Pour les autres fichiers, utiliser le nom sans .py
                module_name = str(chemin_relatif.with_suffix('')).replace('\\', '.').replace('/', '.')
            
            self.modules_existants.add(module_name)
        
        print(f"✅ {len(self.modules_existants)} modules identifiés")
    
    def _analyser_imports_fichiers(self, racine: Path):
        """Analyse les imports dans chaque fichier Python"""
        print("🔗 Analyse des imports...")
        
        for fichier_py in racine.rglob("*.py"):
            if any(exclu in str(fichier_py) for exclu in ['.venv', '__pycache__', 'SURPRISES']):
                continue
            
            try:
                with open(fichier_py, 'r', encoding='utf-8', errors='ignore') as f:
                    contenu = f.read()
                
                # Parser le code Python
                try:
                    arbre = ast.parse(contenu)
                    imports = self._extraire_imports(arbre)
                    self.imports_par_fichier[str(fichier_py)] = imports
                except SyntaxError:
                    # Ignorer les fichiers avec erreurs de syntaxe
                    continue
                    
            except Exception as e:
                continue
        
        print(f"✅ {len(self.imports_par_fichier)} fichiers analysés")
    
    def _extraire_imports(self, arbre: ast.AST) -> List[Dict]:
        """Extrait tous les imports d'un arbre AST"""
        imports = []
        
        for noeud in ast.walk(arbre):
            if isinstance(noeud, ast.Import):
                for alias in noeud.names:
                    imports.append({
                        'type': 'import',
                        'module': alias.name,
                        'alias': alias.asname,
                        'ligne': noeud.lineno
                    })
            elif isinstance(noeud, ast.ImportFrom):
                module = noeud.module or ''
                for alias in noeud.names:
                    imports.append({
                        'type': 'from_import',
                        'module': module,
                        'nom': alias.name,
                        'alias': alias.asname,
                        'ligne': noeud.lineno
                    })
        
        return imports
    
    def _detecter_dependances_manquantes(self):
        """Détecte les dépendances vers des modules inexistants"""
        print("❌ Détection des dépendances manquantes...")
        
        for fichier, imports in self.imports_par_fichier.items():
            for import_info in imports:
                module = import_info['module']
                
                # Ignorer les modules système et externes
                if self._est_module_systeme(module):
                    continue
                
                # Vérifier si le module existe dans notre projet
                if not self._module_existe(module):
                    self.dependances_manquantes[fichier].append(import_info)
    
    def _est_module_systeme(self, module: str) -> bool:
        """Vérifie si c'est un module système ou externe"""
        modules_systeme = {
            'sys', 'os', 'pathlib', 'typing', 'asyncio', 'json', 'datetime',
            'collections', 'enum', 'dataclasses', 'random', 're', 'ast',
            'click', 'fastapi', 'flask', 'pydantic', 'sqlalchemy', 'time',
            'logging', 'argparse', 'math', 'shutil', 'subprocess', 'threading',
            'multiprocessing', 'socket', 'urllib', 'http', 'email', 'xml',
            'html', 'csv', 'sqlite3', 'hashlib', 'base64', 'uuid', 'pickle',
            'copy', 'itertools', 'functools', 'operator', 'io', 'tempfile',
            'glob', 'fnmatch', 'linecache', 'textwrap', 'unicodedata',
            'string', 'struct', 'codecs', 'locale', 'calendar', 'weakref'
        }
        
        # Module système direct
        if module in modules_systeme:
            return True
        
        # Module vide (imports relatifs)
        if not module or module == '':
            return True
        
        # Module système avec sous-modules
        racine_module = module.split('.')[0]
        if racine_module in modules_systeme:
            return True
        
        # Modules externes communs
        modules_externes = {
            'numpy', 'pandas', 'matplotlib', 'torch', 'tensorflow',
            'requests', 'aiohttp', 'uvicorn', 'pytest', 'cv2', 'PIL',
            'sklearn', 'scipy', 'seaborn', 'plotly', 'bokeh', 'dash'
        }
        
        return racine_module in modules_externes
    
    def _module_existe(self, module: str) -> bool:
        """Vérifie si un module existe dans notre projet"""
        # Vérification directe
        if module in self.modules_existants:
            return True
        
        # Vérification avec variations de chemin
        variations = [
            module.replace('.', '/'),
            module.replace('.', '\\'),
            f"src.{module}",
            f"src/{module}".replace('/', '.'),
        ]
        
        for variation in variations:
            if variation in self.modules_existants:
                return True
        
        return False
    
    def _grouper_clusters_migration(self):
        """Groupe les fichiers par clusters de migration"""
        print("🎯 Groupement par clusters de migration...")
        
        clusters = {
            'visualisation_core': [],
            'refuge_cluster': [],
            'interface_web': [],
            'configuration': [],
            'source_orientale': [],
            'autres': []
        }
        
        for fichier in self.dependances_manquantes.keys():
            if 'core/visualisation' in fichier:
                clusters['visualisation_core'].append(fichier)
            elif 'refuge_cluster' in fichier:
                clusters['refuge_cluster'].append(fichier)
            elif 'web' in fichier:
                clusters['interface_web'].append(fichier)
            elif 'config' in fichier.lower():
                clusters['configuration'].append(fichier)
            elif 'SOURCE_ORIENTALE' in fichier:
                clusters['source_orientale'].append(fichier)
            else:
                clusters['autres'].append(fichier)
        
        self.clusters_migration = {k: v for k, v in clusters.items() if v}
    
    def _generer_rapport(self) -> Dict:
        """Génère un rapport complet de l'analyse"""
        # Statistiques globales
        total_fichiers = len(self.imports_par_fichier)
        fichiers_avec_problemes = len(self.dependances_manquantes)
        total_dependances_manquantes = sum(len(deps) for deps in self.dependances_manquantes.values())
        
        # Modules les plus problématiques
        modules_problematiques = Counter()
        for deps in self.dependances_manquantes.values():
            for dep in deps:
                modules_problematiques[dep['module']] += 1
        
        return {
            'statistiques': {
                'total_fichiers_analyses': total_fichiers,
                'fichiers_avec_problemes': fichiers_avec_problemes,
                'total_dependances_manquantes': total_dependances_manquantes,
                'modules_existants': len(self.modules_existants)
            },
            'clusters_migration': self.clusters_migration,
            'modules_problematiques': dict(modules_problematiques.most_common(10)),
            'dependances_detaillees': dict(self.dependances_manquantes)
        }
    
    def afficher_rapport(self, rapport: Dict):
        """Affiche un rapport formaté"""
        stats = rapport['statistiques']
        
        print("\n🔍 ═══════════════════════════════════════════════════════")
        print("              RAPPORT D'AUDIT DES DÉPENDANCES")
        print("🔍 ═══════════════════════════════════════════════════════")
        
        print(f"\n📊 Statistiques globales:")
        print(f"   📁 Fichiers analysés: {stats['total_fichiers_analyses']}")
        print(f"   ❌ Fichiers avec problèmes: {stats['fichiers_avec_problemes']}")
        print(f"   🔗 Dépendances manquantes: {stats['total_dependances_manquantes']}")
        print(f"   ✅ Modules existants: {stats['modules_existants']}")
        
        print(f"\n🎯 Clusters de migration:")
        for cluster, fichiers in rapport['clusters_migration'].items():
            print(f"   📦 {cluster}: {len(fichiers)} fichiers")
            for fichier in fichiers[:3]:  # Afficher les 3 premiers
                nom_court = Path(fichier).name
                print(f"      • {nom_court}")
            if len(fichiers) > 3:
                print(f"      ... et {len(fichiers) - 3} autres")
        
        print(f"\n🚨 Modules les plus problématiques:")
        for module, count in rapport['modules_problematiques'].items():
            print(f"   • {module}: {count} références")
        
        print("\n🔍 ═══════════════════════════════════════════════════════")
    
    def sauvegarder_rapport(self, rapport: Dict, fichier: str = "audit_dependances.json"):
        """Sauvegarde le rapport en JSON"""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False)
        print(f"💾 Rapport sauvegardé: {fichier}")

def main():
    """Point d'entrée principal"""
    print("🔍 Audit Intelligent des Dépendances - Soul Temple")
    print("✨ Analyse des migrations nécessaires\n")
    
    analyseur = AnalyseurDependances()
    rapport = analyseur.scanner_projet()
    
    analyseur.afficher_rapport(rapport)
    analyseur.sauvegarder_rapport(rapport)
    
    print("\n🎯 Prochaines étapes suggérées:")
    print("   1. Examiner les clusters de migration")
    print("   2. Prioriser par impact et complexité")
    print("   3. Commencer par le cluster le plus simple")
    print("   4. Tester après chaque modification")

if __name__ == "__main__":
    main() 