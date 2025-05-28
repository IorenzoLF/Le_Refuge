#!/usr/bin/env python3
"""
🏛️ Analyseur d'Interconnexions du Temple de l'Âme
Détecte les modules orphelins et analyse la structure des connexions
"""

import ast
import json
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict, Counter
import networkx as nx

class AnalyseurInterconnexions:
    """Analyseur des interconnexions entre modules du temple"""
    
    def __init__(self):
        self.modules = {}  # fichier -> infos du module
        self.imports = defaultdict(set)  # fichier -> set des imports
        self.imported_by = defaultdict(set)  # module -> set des fichiers qui l'importent
        self.graphe = nx.DiGraph()
        self.temples = defaultdict(list)  # temple -> liste des modules
        
    def analyser_temple(self, racine: str = "src"):
        """Analyse complète du temple"""
        print("🏛️ ═══════════════════════════════════════════════════════")
        print("        ANALYSE DU TEMPLE DE L'ÂME")
        print("🏛️ ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Découverte des modules
        self._decouvrir_modules(racine)
        
        # 2. Analyse des imports
        self._analyser_imports()
        
        # 3. Construction du graphe
        self._construire_graphe()
        
        # 4. Détection des orphelins
        orphelins = self._detecter_orphelins()
        
        # 5. Analyse des temples
        self._analyser_temples()
        
        # 6. Métriques d'interconnexion
        metriques = self._calculer_metriques()
        
        # 7. Rapport final
        self._generer_rapport(orphelins, metriques)
        
        return {
            "modules": self.modules,
            "orphelins": orphelins,
            "temples": dict(self.temples),
            "metriques": metriques
        }
    
    def _decouvrir_modules(self, racine: str):
        """Découvre tous les modules Python"""
        print("🔍 Découverte des modules...")
        
        for root, dirs, files in os.walk(racine):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    chemin_complet = os.path.join(root, file)
                    chemin_relatif = os.path.relpath(chemin_complet)
                    
                    # Analyse du module
                    infos = self._analyser_module(chemin_complet)
                    self.modules[chemin_relatif] = infos
                    
                    # Classification par temple
                    temple = self._identifier_temple(chemin_relatif)
                    self.temples[temple].append(chemin_relatif)
        
        print(f"   📁 {len(self.modules)} modules découverts")
        print(f"   🏛️ {len(self.temples)} temples identifiés")
        print()
    
    def _analyser_module(self, chemin: str) -> Dict:
        """Analyse un module spécifique"""
        try:
            with open(chemin, 'r', encoding='utf-8', errors='ignore') as f:
                contenu = f.read()
            
            # Parse AST
            try:
                tree = ast.parse(contenu)
                classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                fonctions = [node.name for node in ast.walk(tree) 
                           if isinstance(node, ast.FunctionDef) and not node.name.startswith('_')]
            except:
                classes, fonctions = [], []
            
            # Statistiques
            lignes = len(contenu.split('\n'))
            taille = len(contenu)
            
            return {
                "chemin": chemin,
                "lignes": lignes,
                "taille": taille,
                "classes": classes,
                "fonctions": fonctions,
                "docstring": self._extraire_docstring(contenu),
                "derniere_modification": os.path.getmtime(chemin)
            }
            
        except Exception as e:
            return {
                "chemin": chemin,
                "erreur": str(e),
                "lignes": 0,
                "taille": 0,
                "classes": [],
                "fonctions": []
            }
    
    def _extraire_docstring(self, contenu: str) -> str:
        """Extrait la docstring du module"""
        lignes = contenu.split('\n')
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith('"""') or ligne.strip().startswith("'''"):
                # Trouve la fin de la docstring
                quote = '"""' if '"""' in ligne else "'''"
                if ligne.count(quote) >= 2:
                    # Docstring sur une ligne
                    return ligne.strip().replace(quote, '')
                else:
                    # Docstring multi-lignes
                    for j in range(i+1, min(len(lignes), i+10)):
                        if quote in lignes[j]:
                            return ' '.join(lignes[i:j+1]).replace(quote, '').strip()
        return ""
    
    def _identifier_temple(self, chemin: str) -> str:
        """Identifie le temple d'appartenance d'un module"""
        parties = chemin.replace('\\', '/').split('/')
        
        if len(parties) >= 2:
            if parties[1].startswith('temple_'):
                return parties[1]
            elif parties[1] == 'core':
                return 'core'
            elif parties[1] == 'refuge_cluster':
                return 'refuge_cluster'
            elif parties[1] == 'utils':
                return 'utils'
            else:
                return parties[1]
        
        return 'racine'
    
    def _analyser_imports(self):
        """Analyse tous les imports entre modules"""
        print("🔗 Analyse des imports...")
        
        for chemin, infos in self.modules.items():
            if 'erreur' in infos:
                continue
                
            try:
                with open(infos['chemin'], 'r', encoding='utf-8', errors='ignore') as f:
                    contenu = f.read()
                
                # Parse AST pour les imports
                tree = ast.parse(contenu)
                imports_module = set()
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imports_module.add(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            imports_module.add(node.module)
                
                # Filtre les imports internes au projet
                imports_internes = set()
                for imp in imports_module:
                    if imp.startswith('src.') or imp.startswith('.'):
                        imports_internes.add(imp)
                        # Ajoute à imported_by
                        self.imported_by[imp].add(chemin)
                
                self.imports[chemin] = imports_internes
                
            except Exception as e:
                print(f"   ⚠️ Erreur import {chemin}: {e}")
        
        print(f"   🔗 {sum(len(imports) for imports in self.imports.values())} imports analysés")
        print()
    
    def _construire_graphe(self):
        """Construit le graphe des dépendances"""
        print("📊 Construction du graphe...")
        
        # Ajoute tous les modules comme nœuds
        for chemin in self.modules.keys():
            self.graphe.add_node(chemin)
        
        # Ajoute les arêtes (imports)
        for module, imports in self.imports.items():
            for imp in imports:
                # Convertit l'import en chemin de fichier
                chemin_import = self._import_vers_chemin(imp)
                if chemin_import and chemin_import in self.modules:
                    self.graphe.add_edge(module, chemin_import)
        
        print(f"   📊 Graphe: {len(self.graphe.nodes)} nœuds, {len(self.graphe.edges)} arêtes")
        print()
    
    def _import_vers_chemin(self, import_name: str) -> str:
        """Convertit un nom d'import en chemin de fichier"""
        # Simplifié - à améliorer selon les conventions du projet
        if import_name.startswith('src.'):
            chemin = import_name.replace('src.', 'src/').replace('.', '/') + '.py'
            return chemin
        return None
    
    def _detecter_orphelins(self) -> List[Dict]:
        """Détecte les modules orphelins"""
        print("👻 Détection des modules orphelins...")
        
        orphelins = []
        
        for chemin, infos in self.modules.items():
            # Un module est orphelin si :
            # 1. Il n'est importé par personne
            # 2. Il n'est pas un point d'entrée (main.py, __init__.py)
            # 3. Il n'est pas dans core/ ou utils/
            
            est_importe = any(chemin in imports for imports in self.imports.values())
            est_point_entree = 'main.py' in chemin or '__init__.py' in chemin
            est_utilitaire = '/core/' in chemin or '/utils/' in chemin
            
            if not est_importe and not est_point_entree and not est_utilitaire:
                # Analyse plus poussée
                score_orphelin = self._calculer_score_orphelin(chemin, infos)
                
                orphelins.append({
                    "chemin": chemin,
                    "temple": self._identifier_temple(chemin),
                    "score_orphelin": score_orphelin,
                    "raisons": self._analyser_raisons_orphelin(chemin, infos),
                    "suggestions": self._suggerer_connexions(chemin, infos)
                })
        
        # Trie par score d'orphelin (plus élevé = plus orphelin)
        orphelins.sort(key=lambda x: x["score_orphelin"], reverse=True)
        
        print(f"   👻 {len(orphelins)} modules orphelins détectés")
        print()
        
        return orphelins
    
    def _calculer_score_orphelin(self, chemin: str, infos: Dict) -> float:
        """Calcule un score d'orphelin (0-100)"""
        score = 0
        
        # Facteurs augmentant le score d'orphelin
        if len(infos.get('classes', [])) == 0:
            score += 20  # Pas de classes
        if len(infos.get('fonctions', [])) == 0:
            score += 20  # Pas de fonctions publiques
        if infos.get('lignes', 0) < 50:
            score += 15  # Très petit module
        if not infos.get('docstring', ''):
            score += 10  # Pas de documentation
        
        # Facteurs diminuant le score
        if len(infos.get('classes', [])) > 2:
            score -= 10  # Beaucoup de classes
        if len(infos.get('fonctions', [])) > 5:
            score -= 10  # Beaucoup de fonctions
        if infos.get('lignes', 0) > 200:
            score -= 15  # Module substantiel
        
        return max(0, min(100, score))
    
    def _analyser_raisons_orphelin(self, chemin: str, infos: Dict) -> List[str]:
        """Analyse pourquoi un module est orphelin"""
        raisons = []
        
        if len(infos.get('classes', [])) == 0:
            raisons.append("Aucune classe définie")
        if len(infos.get('fonctions', [])) == 0:
            raisons.append("Aucune fonction publique")
        if infos.get('lignes', 0) < 30:
            raisons.append("Module très court")
        if not infos.get('docstring', ''):
            raisons.append("Pas de documentation")
        if 'test' in chemin.lower():
            raisons.append("Module de test")
        if 'example' in chemin.lower():
            raisons.append("Module d'exemple")
        
        return raisons
    
    def _suggerer_connexions(self, chemin: str, infos: Dict) -> List[str]:
        """Suggère des connexions possibles"""
        suggestions = []
        
        temple = self._identifier_temple(chemin)
        
        # Suggestions basées sur le temple
        if temple.startswith('temple_'):
            suggestions.append(f"Intégrer dans le système {temple}")
            suggestions.append("Créer un point d'entrée dans __init__.py")
        
        # Suggestions basées sur le contenu
        if len(infos.get('classes', [])) > 0:
            suggestions.append("Exporter les classes dans un module principal")
        if len(infos.get('fonctions', [])) > 0:
            suggestions.append("Créer un module utilitaire qui importe ces fonctions")
        
        suggestions.append("Ajouter de la documentation")
        suggestions.append("Créer des tests unitaires")
        
        return suggestions
    
    def _analyser_temples(self):
        """Analyse la structure des temples"""
        print("🏛️ Analyse des temples...")
        
        for temple, modules in self.temples.items():
            print(f"   🏛️ {temple}: {len(modules)} modules")
        
        print()
    
    def _calculer_metriques(self) -> Dict:
        """Calcule les métriques d'interconnexion"""
        print("📈 Calcul des métriques...")
        
        # Métriques de base
        total_modules = len(self.modules)
        total_imports = sum(len(imports) for imports in self.imports.values())
        
        # Métriques de graphe
        if len(self.graphe.nodes) > 0:
            densite = nx.density(self.graphe)
            composantes = list(nx.weakly_connected_components(self.graphe))
            plus_grande_composante = max(len(c) for c in composantes) if composantes else 0
        else:
            densite = 0
            composantes = []
            plus_grande_composante = 0
        
        # Modules les plus connectés
        modules_connectes = []
        for module in self.modules.keys():
            imports_entrants = sum(1 for imports in self.imports.values() if module in imports)
            imports_sortants = len(self.imports.get(module, set()))
            total_connexions = imports_entrants + imports_sortants
            
            if total_connexions > 0:
                modules_connectes.append({
                    "module": module,
                    "entrants": imports_entrants,
                    "sortants": imports_sortants,
                    "total": total_connexions
                })
        
        modules_connectes.sort(key=lambda x: x["total"], reverse=True)
        
        metriques = {
            "total_modules": total_modules,
            "total_imports": total_imports,
            "densite_graphe": densite,
            "composantes_connexes": len(composantes),
            "plus_grande_composante": plus_grande_composante,
            "modules_les_plus_connectes": modules_connectes[:10],
            "temples": {temple: len(modules) for temple, modules in self.temples.items()}
        }
        
        print(f"   📈 Métriques calculées")
        print()
        
        return metriques
    
    def _generer_rapport(self, orphelins: List[Dict], metriques: Dict):
        """Génère le rapport final"""
        print("📋 RAPPORT D'INTERCONNEXIONS")
        print("=" * 50)
        print()
        
        # Vue d'ensemble
        print(f"📊 Vue d'ensemble:")
        print(f"   • Modules totaux: {metriques['total_modules']}")
        print(f"   • Imports totaux: {metriques['total_imports']}")
        print(f"   • Densité du graphe: {metriques['densite_graphe']:.3f}")
        print(f"   • Composantes connexes: {metriques['composantes_connexes']}")
        print()
        
        # Temples
        print(f"🏛️ Distribution par temples:")
        for temple, count in sorted(metriques['temples'].items(), key=lambda x: x[1], reverse=True):
            print(f"   • {temple}: {count} modules")
        print()
        
        # Modules orphelins
        print(f"👻 Modules orphelins ({len(orphelins)}):")
        for orphelin in orphelins[:10]:  # Top 10
            print(f"   • {orphelin['chemin']} (score: {orphelin['score_orphelin']:.1f})")
            print(f"     Temple: {orphelin['temple']}")
            print(f"     Raisons: {', '.join(orphelin['raisons'])}")
            print(f"     Suggestions: {orphelin['suggestions'][0] if orphelin['suggestions'] else 'Aucune'}")
            print()
        
        # Modules les plus connectés
        print(f"🔗 Modules les plus connectés:")
        for module in metriques['modules_les_plus_connectes'][:5]:
            print(f"   • {module['module']}: {module['total']} connexions")
            print(f"     ↙️ {module['entrants']} entrants, ↗️ {module['sortants']} sortants")
        print()
        
        # Recommandations
        print("💡 RECOMMANDATIONS:")
        if len(orphelins) > 0:
            print(f"   1. Examiner les {len(orphelins)} modules orphelins")
            print("   2. Créer des points d'entrée pour les temples")
            print("   3. Améliorer la documentation des modules")
        
        if metriques['densite_graphe'] < 0.1:
            print("   4. Augmenter les interconnexions entre modules")
        
        print("   5. Créer un système de découverte automatique")
        print()

if __name__ == "__main__":
    analyseur = AnalyseurInterconnexions()
    resultat = analyseur.analyser_temple()
    
    # Sauvegarde
    with open("bibliotheque/apprentissage/analyse_interconnexions.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, indent=2, ensure_ascii=False, default=str)
    
    print("💾 Analyse sauvegardée: bibliotheque/apprentissage/analyse_interconnexions.json") 