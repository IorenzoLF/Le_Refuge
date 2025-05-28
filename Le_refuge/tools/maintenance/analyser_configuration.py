#!/usr/bin/env python3
"""
🔧 Analyseur des Systèmes de Configuration
Analyse détaillée des 3 systèmes de configuration pour identifier les redondances et proposer une unification
"""

import json
import ast
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from collections import defaultdict
import re

class AnalyseurConfiguration:
    """Analyseur spécialisé pour les systèmes de configuration"""
    
    def __init__(self):
        self.fichiers_config = [
            "src/core/configuration.py",
            "src/refuge_cluster/refuge_core/refuge_config.py", 
            "src/utils/config.py",
            "src/temple_dialogues/dialogue_manager.py"
        ]
        self.systemes = {}
        self.redondances = defaultdict(list)
        self.todos_identifies = []
        self.classes_trouvees = {}
        self.constantes_trouvees = {}
        self.fonctions_trouvees = {}
        
    def analyser_fichier(self, fichier: str) -> Dict[str, Any]:
        """Analyse un fichier de configuration en détail"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                
            # Parse AST pour analyse structurelle
            try:
                tree = ast.parse(contenu)
                structure = self._analyser_ast(tree)
            except:
                structure = {"erreur": "Impossible de parser l'AST"}
                
            # Analyse textuelle pour TODOs et patterns
            todos = self._extraire_todos(contenu)
            imports = self._extraire_imports(contenu)
            classes = self._extraire_classes(contenu)
            constantes = self._extraire_constantes(contenu)
            fonctions = self._extraire_fonctions(contenu)
            
            return {
                "fichier": fichier,
                "taille": len(contenu),
                "lignes": len(contenu.split('\n')),
                "structure_ast": structure,
                "todos": todos,
                "imports": imports,
                "classes": classes,
                "constantes": constantes,
                "fonctions": fonctions,
                "patterns": self._identifier_patterns(contenu)
            }
            
        except Exception as e:
            return {
                "fichier": fichier,
                "erreur": str(e)
            }
    
    def _analyser_ast(self, tree: ast.AST) -> Dict[str, Any]:
        """Analyse l'AST pour extraire la structure"""
        classes = []
        fonctions = []
        constantes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                classes.append({
                    "nom": node.name,
                    "ligne": node.lineno,
                    "methodes": [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                })
            elif isinstance(node, ast.FunctionDef) and not any(node.lineno >= c["ligne"] for c in classes):
                fonctions.append({
                    "nom": node.name,
                    "ligne": node.lineno
                })
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constantes.append({
                            "nom": target.id,
                            "ligne": node.lineno
                        })
                        
        return {
            "classes": classes,
            "fonctions": fonctions,
            "constantes": constantes
        }
    
    def _extraire_todos(self, contenu: str) -> List[Dict[str, Any]]:
        """Extrait tous les TODOs avec contexte"""
        todos = []
        lignes = contenu.split('\n')
        
        for i, ligne in enumerate(lignes, 1):
            if 'TODO' in ligne:
                # Contexte avant et après
                contexte_avant = lignes[max(0, i-3):i-1] if i > 1 else []
                contexte_apres = lignes[i:min(len(lignes), i+2)] if i < len(lignes) else []
                
                todos.append({
                    "ligne": i,
                    "texte": ligne.strip(),
                    "contexte_avant": contexte_avant,
                    "contexte_apres": contexte_apres,
                    "type": self._classifier_todo(ligne)
                })
                
        return todos
    
    def _classifier_todo(self, ligne: str) -> str:
        """Classifie le type de TODO"""
        ligne_lower = ligne.lower()
        if "chargement" in ligne_lower or "charger" in ligne_lower:
            return "chargement"
        elif "vérification" in ligne_lower or "vérifier" in ligne_lower:
            return "verification"
        elif "implémentation" in ligne_lower or "implémenter" in ligne_lower:
            return "implementation"
        elif "configuration" in ligne_lower or "config" in ligne_lower:
            return "configuration"
        else:
            return "autre"
    
    def _extraire_imports(self, contenu: str) -> List[str]:
        """Extrait tous les imports"""
        imports = []
        for ligne in contenu.split('\n'):
            ligne = ligne.strip()
            if ligne.startswith('import ') or ligne.startswith('from '):
                imports.append(ligne)
        return imports
    
    def _extraire_classes(self, contenu: str) -> List[Dict[str, Any]]:
        """Extrait les définitions de classes avec détails"""
        classes = []
        lignes = contenu.split('\n')
        
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith('class '):
                match = re.match(r'class\s+(\w+)', ligne.strip())
                if match:
                    nom_classe = match.group(1)
                    
                    # Cherche les méthodes de cette classe
                    methodes = []
                    j = i + 1
                    while j < len(lignes) and (lignes[j].startswith('    ') or lignes[j].strip() == ''):
                        if lignes[j].strip().startswith('def '):
                            match_method = re.match(r'\s+def\s+(\w+)', lignes[j])
                            if match_method:
                                methodes.append(match_method.group(1))
                        j += 1
                    
                    classes.append({
                        "nom": nom_classe,
                        "ligne": i + 1,
                        "methodes": methodes
                    })
                    
        return classes
    
    def _extraire_constantes(self, contenu: str) -> List[Dict[str, Any]]:
        """Extrait les constantes (variables en MAJUSCULES)"""
        constantes = []
        lignes = contenu.split('\n')
        
        for i, ligne in enumerate(lignes):
            # Cherche les assignations de constantes (MAJUSCULES)
            match = re.match(r'^([A-Z_][A-Z0-9_]*)\s*=', ligne.strip())
            if match:
                nom_constante = match.group(1)
                
                # Détermine le type de valeur
                if '{' in ligne:
                    type_valeur = "dict"
                elif '[' in ligne:
                    type_valeur = "list"
                elif ligne.count('"') >= 2 or ligne.count("'") >= 2:
                    type_valeur = "string"
                else:
                    type_valeur = "autre"
                
                constantes.append({
                    "nom": nom_constante,
                    "ligne": i + 1,
                    "type": type_valeur
                })
                
        return constantes
    
    def _extraire_fonctions(self, contenu: str) -> List[Dict[str, Any]]:
        """Extrait les fonctions avec leurs signatures"""
        fonctions = []
        lignes = contenu.split('\n')
        
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith('def ') and not ligne.startswith('    '):
                match = re.match(r'def\s+(\w+)\s*\((.*?)\)', ligne.strip())
                if match:
                    nom_fonction = match.group(1)
                    parametres = match.group(2)
                    
                    fonctions.append({
                        "nom": nom_fonction,
                        "ligne": i + 1,
                        "parametres": parametres,
                        "est_todo": any("TODO" in lignes[j] for j in range(i, min(len(lignes), i+10)))
                    })
                    
        return fonctions
    
    def _identifier_patterns(self, contenu: str) -> Dict[str, Any]:
        """Identifie les patterns de configuration"""
        patterns = {
            "utilise_pydantic": "BaseModel" in contenu,
            "utilise_dataclass": "@dataclass" in contenu,
            "utilise_pathlib": "Path" in contenu,
            "utilise_logging": "logging" in contenu,
            "utilise_json": "json" in contenu,
            "utilise_yaml": "yaml" in contenu,
            "a_validation": "valider" in contenu.lower() or "validate" in contenu.lower(),
            "a_chargement": "charger" in contenu.lower() or "load" in contenu.lower(),
            "a_sauvegarde": "sauvegarder" in contenu.lower() or "save" in contenu.lower(),
            "style_moderne": "class " in contenu and "def " in contenu,
            "style_legacy": contenu.count("=") > contenu.count("def")
        }
        
        return patterns
    
    def identifier_redondances(self):
        """Identifie les redondances entre les systèmes"""
        # Redondances de constantes
        constantes_par_nom = defaultdict(list)
        for fichier, analyse in self.systemes.items():
            for constante in analyse.get("constantes", []):
                constantes_par_nom[constante["nom"]].append({
                    "fichier": fichier,
                    "ligne": constante["ligne"]
                })
        
        # Redondances de fonctions
        fonctions_par_nom = defaultdict(list)
        for fichier, analyse in self.systemes.items():
            for fonction in analyse.get("fonctions", []):
                fonctions_par_nom[fonction["nom"]].append({
                    "fichier": fichier,
                    "ligne": fonction["ligne"],
                    "est_todo": fonction.get("est_todo", False)
                })
        
        # Redondances de classes
        classes_par_nom = defaultdict(list)
        for fichier, analyse in self.systemes.items():
            for classe in analyse.get("classes", []):
                classes_par_nom[classe["nom"]].append({
                    "fichier": fichier,
                    "ligne": classe["ligne"],
                    "methodes": classe["methodes"]
                })
        
        self.redondances = {
            "constantes": {nom: fichiers for nom, fichiers in constantes_par_nom.items() if len(fichiers) > 1},
            "fonctions": {nom: fichiers for nom, fichiers in fonctions_par_nom.items() if len(fichiers) > 1},
            "classes": {nom: fichiers for nom, fichiers in classes_par_nom.items() if len(fichiers) > 1}
        }
    
    def analyser_todos_configuration(self):
        """Analyse spécifique des TODOs de configuration"""
        todos_config = []
        
        for fichier, analyse in self.systemes.items():
            for todo in analyse.get("todos", []):
                if todo["type"] in ["chargement", "verification", "configuration"]:
                    todos_config.append({
                        "fichier": fichier,
                        "ligne": todo["ligne"],
                        "texte": todo["texte"],
                        "type": todo["type"],
                        "contexte": todo.get("contexte_avant", [])
                    })
        
        self.todos_identifies = todos_config
    
    def proposer_architecture_unifiee(self) -> Dict[str, Any]:
        """Propose une architecture unifiée basée sur l'analyse"""
        
        # Identifie le système le plus moderne
        scores_modernite = {}
        for fichier, analyse in self.systemes.items():
            score = 0
            patterns = analyse.get("patterns", {})
            
            if patterns.get("utilise_pydantic"): score += 3
            if patterns.get("utilise_dataclass"): score += 2
            if patterns.get("utilise_pathlib"): score += 2
            if patterns.get("a_validation"): score += 2
            if patterns.get("style_moderne"): score += 1
            if not patterns.get("style_legacy"): score += 1
            
            scores_modernite[fichier] = score
        
        systeme_principal = max(scores_modernite.items(), key=lambda x: x[1])[0]
        
        return {
            "systeme_principal": systeme_principal,
            "scores_modernite": scores_modernite,
            "redondances_critiques": len(self.redondances["fonctions"]),
            "todos_a_resoudre": len(self.todos_identifies),
            "recommandations": self._generer_recommandations()
        }
    
    def _generer_recommandations(self) -> List[str]:
        """Génère des recommandations d'unification"""
        recommandations = []
        
        # Analyse des redondances
        if len(self.redondances["fonctions"]) > 0:
            recommandations.append("Unifier les fonctions dupliquées")
        
        if len(self.redondances["constantes"]) > 3:
            recommandations.append("Centraliser les constantes communes")
        
        # Analyse des TODOs
        todos_chargement = sum(1 for t in self.todos_identifies if t["type"] == "chargement")
        todos_verification = sum(1 for t in self.todos_identifies if t["type"] == "verification")
        
        if todos_chargement > 1:
            recommandations.append("Implémenter une fonction de chargement centralisée")
        
        if todos_verification > 1:
            recommandations.append("Implémenter une fonction de validation centralisée")
        
        return recommandations
    
    def generer_rapport(self):
        """Génère un rapport complet d'analyse"""
        print("🔧 ═══════════════════════════════════════════════════════")
        print("        ANALYSE DES SYSTÈMES DE CONFIGURATION")
        print("🔧 ═══════════════════════════════════════════════════════")
        print()
        
        # Analyse de chaque fichier
        for fichier in self.fichiers_config:
            if Path(fichier).exists():
                print(f"📁 Analyse de {fichier}...")
                analyse = self.analyser_fichier(fichier)
                self.systemes[fichier] = analyse
                
                if "erreur" in analyse:
                    print(f"   ❌ Erreur: {analyse['erreur']}")
                    continue
                
                print(f"   📊 {analyse['lignes']} lignes, {len(analyse['classes'])} classes, {len(analyse['fonctions'])} fonctions")
                print(f"   🔧 {len(analyse['todos'])} TODOs, {len(analyse['constantes'])} constantes")
                
                # Détails des TODOs
                for todo in analyse['todos']:
                    print(f"      🚨 L{todo['ligne']}: {todo['texte'][:60]}...")
                
                print()
        
        # Analyse des redondances
        print("🔍 ANALYSE DES REDONDANCES")
        print("=" * 50)
        
        self.identifier_redondances()
        
        for type_redondance, redondances in self.redondances.items():
            if redondances:
                print(f"\n📋 {type_redondance.upper()} dupliquées:")
                for nom, occurrences in redondances.items():
                    print(f"   • {nom}: {len(occurrences)} occurrences")
                    for occ in occurrences:
                        print(f"     - {occ['fichier']}:{occ['ligne']}")
        
        # Analyse des TODOs
        print("\n🎯 ANALYSE DES TODOS CONFIGURATION")
        print("=" * 50)
        
        self.analyser_todos_configuration()
        
        todos_par_type = defaultdict(list)
        for todo in self.todos_identifies:
            todos_par_type[todo["type"]].append(todo)
        
        for type_todo, todos in todos_par_type.items():
            print(f"\n📝 TODOs de type '{type_todo}': {len(todos)}")
            for todo in todos:
                print(f"   • {todo['fichier']}:{todo['ligne']}")
                print(f"     {todo['texte']}")
        
        # Proposition d'architecture
        print("\n🏗️ ARCHITECTURE UNIFIÉE RECOMMANDÉE")
        print("=" * 50)
        
        architecture = self.proposer_architecture_unifiee()
        
        print(f"\n🥇 Système principal recommandé: {architecture['systeme_principal']}")
        print(f"   Score de modernité: {architecture['scores_modernite'][architecture['systeme_principal']]}/10")
        
        print(f"\n📊 Scores de modernité:")
        for fichier, score in sorted(architecture['scores_modernite'].items(), key=lambda x: x[1], reverse=True):
            print(f"   • {fichier}: {score}/10")
        
        print(f"\n💡 Recommandations:")
        for i, rec in enumerate(architecture['recommandations'], 1):
            print(f"   {i}. {rec}")
        
        print(f"\n📈 Métriques:")
        print(f"   • Redondances critiques: {architecture['redondances_critiques']}")
        print(f"   • TODOs à résoudre: {architecture['todos_a_resoudre']}")
        print(f"   • Fichiers analysés: {len(self.systemes)}")
        
        return {
            "systemes": self.systemes,
            "redondances": dict(self.redondances),
            "todos": self.todos_identifies,
            "architecture": architecture
        }

if __name__ == "__main__":
    analyseur = AnalyseurConfiguration()
    resultat = analyseur.generer_rapport()
    
    # Sauvegarde le rapport
    with open("bibliotheque/apprentissage/analyse_configuration_complete.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, indent=2, ensure_ascii=False)
    
    print("\n💾 Analyse sauvegardée: bibliotheque/apprentissage/analyse_configuration_complete.json") 