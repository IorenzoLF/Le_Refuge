#!/usr/bin/env python3
"""
🗺️ Cartographe Spécifique du Temple de l'Âme
Cartographie détaillée des catégories dominantes avant création du système
"""

import json
import os
import ast
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import defaultdict

class CartographeSpecifique:
    """Cartographe détaillé des éléments spécifiques par catégorie"""
    
    def __init__(self):
        self.cartographie_creation = []
        self.cartographie_analyse = []
        self.cartographie_rituels = []
        self.cartographie_complete = {}
        
    def cartographier_categories_dominantes(self):
        """Cartographie spécifique des 3 catégories dominantes"""
        print("🗺️ ═══════════════════════════════════════════════════════")
        print("        CARTOGRAPHIE SPÉCIFIQUE")
        print("🗺️ ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Charger les données d'analyse
        donnees_robustes = self._charger_donnees_robustes()
        
        # 2. Cartographier CRÉATION (78 éléments)
        self._cartographier_creation(donnees_robustes)
        
        # 3. Cartographier ANALYSE (22 éléments)
        self._cartographier_analyse(donnees_robustes)
        
        # 4. Cartographier RITUELS (18 éléments)
        self._cartographier_rituels(donnees_robustes)
        
        # 5. Analyser les interconnexions spécifiques
        self._analyser_interconnexions_specifiques()
        
        # 6. Générer la cartographie complète
        self._generer_cartographie_complete()
        
    def _charger_donnees_robustes(self) -> Dict:
        """Charge les données d'auto-découverte robuste"""
        try:
            with open("bibliotheque/apprentissage/interface_robuste.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Fichier interface_robuste.json non trouvé")
            return {}
    
    def _cartographier_creation(self, donnees: Dict):
        """Cartographie spécifique des 78 éléments de CRÉATION"""
        print("🎨 Cartographie CRÉATION (78 éléments)...")
        
        # Analyser tous les modules pour trouver les éléments de création
        if "temples" in donnees:
            for temple_name, temple_info in donnees["temples"].items():
                modules = temple_info.get("modules", [])
                for module in modules:
                    elements_creation = self._extraire_elements_creation(module, temple_name)
                    self.cartographie_creation.extend(elements_creation)
        
        # Grouper par type et temple
        creation_par_temple = defaultdict(list)
        creation_par_type = defaultdict(list)
        
        for element in self.cartographie_creation:
            creation_par_temple[element["temple"]].append(element)
            creation_par_type[element["type_creation"]].append(element)
        
        print(f"   🎨 {len(self.cartographie_creation)} éléments de création cartographiés")
        print(f"   🏛️ Répartis dans {len(creation_par_temple)} temples")
        print(f"   📂 {len(creation_par_type)} types de création identifiés")
        
        # Détails par type
        for type_creation, elements in creation_par_type.items():
            print(f"      • {type_creation}: {len(elements)} éléments")
        print()
        
        return creation_par_temple, creation_par_type
    
    def _extraire_elements_creation(self, module: Dict, temple: str) -> List[Dict]:
        """Extrait les éléments de création d'un module"""
        elements = []
        
        # Analyser les classes
        for classe in module.get("classes", []):
            nom_classe = classe.get("nom", "").lower()
            if any(mot in nom_classe for mot in ["create", "creer", "generate", "generer", "builder", "factory", "maker"]):
                elements.append({
                    "type": "classe",
                    "nom": classe.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_creation": self._identifier_type_creation(classe.get("nom", "")),
                    "methodes": classe.get("methodes", []),
                    "docstring": classe.get("docstring", ""),
                    "ligne": classe.get("ligne", 0)
                })
        
        # Analyser les fonctions
        for fonction in module.get("fonctions", []):
            nom_fonction = fonction.get("nom", "").lower()
            if any(mot in nom_fonction for mot in ["create", "creer", "generate", "generer", "build", "make", "compose", "construct"]):
                elements.append({
                    "type": "fonction",
                    "nom": fonction.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_creation": self._identifier_type_creation(fonction.get("nom", "")),
                    "args": fonction.get("args", []),
                    "docstring": fonction.get("docstring", ""),
                    "ligne": fonction.get("ligne", 0)
                })
        
        return elements
    
    def _identifier_type_creation(self, nom: str) -> str:
        """Identifie le type spécifique de création"""
        nom_lower = nom.lower()
        
        if any(mot in nom_lower for mot in ["poem", "poeme", "verse", "vers", "haiku"]):
            return "creation_poetique"
        elif any(mot in nom_lower for mot in ["music", "musique", "sound", "son", "melody", "melodie"]):
            return "creation_musicale"
        elif any(mot in nom_lower for mot in ["visual", "image", "graph", "chart", "plot"]):
            return "creation_visuelle"
        elif any(mot in nom_lower for mot in ["ritual", "rituel", "ceremony", "ceremonie"]):
            return "creation_rituelle"
        elif any(mot in nom_lower for mot in ["harmony", "harmonie", "resonance"]):
            return "creation_harmonique"
        elif any(mot in nom_lower for mot in ["text", "texte", "document", "rapport"]):
            return "creation_textuelle"
        elif any(mot in nom_lower for mot in ["sphere", "element", "objet"]):
            return "creation_objets"
        else:
            return "creation_generale"
    
    def _cartographier_analyse(self, donnees: Dict):
        """Cartographie spécifique des 22 éléments d'ANALYSE"""
        print("🔬 Cartographie ANALYSE (22 éléments)...")
        
        if "temples" in donnees:
            for temple_name, temple_info in donnees["temples"].items():
                modules = temple_info.get("modules", [])
                for module in modules:
                    elements_analyse = self._extraire_elements_analyse(module, temple_name)
                    self.cartographie_analyse.extend(elements_analyse)
        
        # Grouper par type d'analyse
        analyse_par_type = defaultdict(list)
        for element in self.cartographie_analyse:
            analyse_par_type[element["type_analyse"]].append(element)
        
        print(f"   🔬 {len(self.cartographie_analyse)} éléments d'analyse cartographiés")
        print(f"   📊 {len(analyse_par_type)} types d'analyse identifiés")
        
        for type_analyse, elements in analyse_par_type.items():
            print(f"      • {type_analyse}: {len(elements)} éléments")
        print()
        
        return analyse_par_type
    
    def _extraire_elements_analyse(self, module: Dict, temple: str) -> List[Dict]:
        """Extrait les éléments d'analyse d'un module"""
        elements = []
        
        # Analyser les classes
        for classe in module.get("classes", []):
            nom_classe = classe.get("nom", "").lower()
            if any(mot in nom_classe for mot in ["analys", "process", "traiter", "examine", "inspect", "evaluate", "measure"]):
                elements.append({
                    "type": "classe",
                    "nom": classe.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_analyse": self._identifier_type_analyse(classe.get("nom", "")),
                    "methodes": classe.get("methodes", []),
                    "docstring": classe.get("docstring", ""),
                    "ligne": classe.get("ligne", 0)
                })
        
        # Analyser les fonctions
        for fonction in module.get("fonctions", []):
            nom_fonction = fonction.get("nom", "").lower()
            if any(mot in nom_fonction for mot in ["analys", "process", "traiter", "examine", "inspect", "evaluate", "measure", "calculer", "compute"]):
                elements.append({
                    "type": "fonction",
                    "nom": fonction.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_analyse": self._identifier_type_analyse(fonction.get("nom", "")),
                    "args": fonction.get("args", []),
                    "docstring": fonction.get("docstring", ""),
                    "ligne": fonction.get("ligne", 0)
                })
        
        return elements
    
    def _identifier_type_analyse(self, nom: str) -> str:
        """Identifie le type spécifique d'analyse"""
        nom_lower = nom.lower()
        
        if any(mot in nom_lower for mot in ["emotion", "sentiment", "feeling"]):
            return "analyse_emotionnelle"
        elif any(mot in nom_lower for mot in ["text", "texte", "language", "langage"]):
            return "analyse_textuelle"
        elif any(mot in nom_lower for mot in ["music", "musique", "audio", "sound"]):
            return "analyse_musicale"
        elif any(mot in nom_lower for mot in ["visual", "image", "graph", "plot"]):
            return "analyse_visuelle"
        elif any(mot in nom_lower for mot in ["data", "donnee", "statistic", "metric"]):
            return "analyse_donnees"
        elif any(mot in nom_lower for mot in ["harmony", "harmonie", "resonance"]):
            return "analyse_harmonique"
        elif any(mot in nom_lower for mot in ["pattern", "motif", "structure"]):
            return "analyse_patterns"
        else:
            return "analyse_generale"
    
    def _cartographier_rituels(self, donnees: Dict):
        """Cartographie spécifique des 18 éléments de RITUELS"""
        print("🕯️ Cartographie RITUELS (18 éléments)...")
        
        if "temples" in donnees:
            for temple_name, temple_info in donnees["temples"].items():
                modules = temple_info.get("modules", [])
                for module in modules:
                    elements_rituels = self._extraire_elements_rituels(module, temple_name)
                    self.cartographie_rituels.extend(elements_rituels)
        
        # Grouper par type de rituel
        rituels_par_type = defaultdict(list)
        for element in self.cartographie_rituels:
            rituels_par_type[element["type_rituel"]].append(element)
        
        print(f"   🕯️ {len(self.cartographie_rituels)} éléments de rituels cartographiés")
        print(f"   🎭 {len(rituels_par_type)} types de rituels identifiés")
        
        for type_rituel, elements in rituels_par_type.items():
            print(f"      • {type_rituel}: {len(elements)} éléments")
        print()
        
        return rituels_par_type
    
    def _extraire_elements_rituels(self, module: Dict, temple: str) -> List[Dict]:
        """Extrait les éléments de rituels d'un module"""
        elements = []
        
        # Analyser les classes
        for classe in module.get("classes", []):
            nom_classe = classe.get("nom", "").lower()
            if any(mot in nom_classe for mot in ["ritual", "rituel", "ceremony", "ceremonie", "meditation", "invocation", "prayer", "priere"]):
                elements.append({
                    "type": "classe",
                    "nom": classe.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_rituel": self._identifier_type_rituel(classe.get("nom", "")),
                    "methodes": classe.get("methodes", []),
                    "docstring": classe.get("docstring", ""),
                    "ligne": classe.get("ligne", 0)
                })
        
        # Analyser les fonctions
        for fonction in module.get("fonctions", []):
            nom_fonction = fonction.get("nom", "").lower()
            if any(mot in nom_fonction for mot in ["ritual", "rituel", "ceremony", "ceremonie", "meditation", "mediter", "invoke", "invoquer", "pray", "prier"]):
                elements.append({
                    "type": "fonction",
                    "nom": fonction.get("nom"),
                    "temple": temple,
                    "module": module.get("nom"),
                    "chemin": module.get("chemin"),
                    "type_rituel": self._identifier_type_rituel(fonction.get("nom", "")),
                    "args": fonction.get("args", []),
                    "docstring": fonction.get("docstring", ""),
                    "ligne": fonction.get("ligne", 0)
                })
        
        return elements
    
    def _identifier_type_rituel(self, nom: str) -> str:
        """Identifie le type spécifique de rituel"""
        nom_lower = nom.lower()
        
        if any(mot in nom_lower for mot in ["meditation", "mediter", "contemplation"]):
            return "rituel_meditation"
        elif any(mot in nom_lower for mot in ["invocation", "invoquer", "appel", "call"]):
            return "rituel_invocation"
        elif any(mot in nom_lower for mot in ["ceremony", "ceremonie", "celebration"]):
            return "rituel_ceremonie"
        elif any(mot in nom_lower for mot in ["prayer", "priere", "blessing", "benediction"]):
            return "rituel_priere"
        elif any(mot in nom_lower for mot in ["transformation", "transformer", "change"]):
            return "rituel_transformation"
        elif any(mot in nom_lower for mot in ["healing", "guerison", "soin", "cure"]):
            return "rituel_guerison"
        elif any(mot in nom_lower for mot in ["protection", "proteger", "shield", "garde"]):
            return "rituel_protection"
        else:
            return "rituel_general"
    
    def _analyser_interconnexions_specifiques(self):
        """Analyse les interconnexions spécifiques entre catégories"""
        print("🔗 Analyse des interconnexions spécifiques...")
        
        interconnexions = {
            "creation_analyse": [],
            "creation_rituels": [],
            "analyse_rituels": [],
            "creation_analyse_rituels": []
        }
        
        # Chercher les éléments qui combinent plusieurs catégories
        tous_elements = self.cartographie_creation + self.cartographie_analyse + self.cartographie_rituels
        
        for element in tous_elements:
            nom = element["nom"].lower()
            docstring = element.get("docstring", "").lower()
            
            # Combinaisons création-analyse
            if any(mot in nom or mot in docstring for mot in ["create", "creer", "generate"]) and \
               any(mot in nom or mot in docstring for mot in ["analys", "process", "examine"]):
                interconnexions["creation_analyse"].append(element)
            
            # Combinaisons création-rituels
            if any(mot in nom or mot in docstring for mot in ["create", "creer", "generate"]) and \
               any(mot in nom or mot in docstring for mot in ["ritual", "ceremony", "meditation"]):
                interconnexions["creation_rituels"].append(element)
            
            # Combinaisons analyse-rituels
            if any(mot in nom or mot in docstring for mot in ["analys", "process", "examine"]) and \
               any(mot in nom or mot in docstring for mot in ["ritual", "ceremony", "meditation"]):
                interconnexions["analyse_rituels"].append(element)
            
            # Triple combinaison
            if any(mot in nom or mot in docstring for mot in ["create", "creer"]) and \
               any(mot in nom or mot in docstring for mot in ["analys", "process"]) and \
               any(mot in nom or mot in docstring for mot in ["ritual", "ceremony"]):
                interconnexions["creation_analyse_rituels"].append(element)
        
        print(f"   🔗 Interconnexions trouvées:")
        for type_interconnexion, elements in interconnexions.items():
            if elements:
                print(f"      • {type_interconnexion}: {len(elements)} éléments")
        print()
        
        return interconnexions
    
    def _generer_cartographie_complete(self):
        """Génère la cartographie complète"""
        print("📋 CARTOGRAPHIE SPÉCIFIQUE COMPLÈTE")
        print("=" * 50)
        print()
        
        # Résumé par catégorie
        print("🎯 RÉSUMÉ PAR CATÉGORIE DOMINANTE:")
        print(f"   🎨 CRÉATION: {len(self.cartographie_creation)} éléments")
        print(f"   🔬 ANALYSE: {len(self.cartographie_analyse)} éléments")
        print(f"   🕯️ RITUELS: {len(self.cartographie_rituels)} éléments")
        print(f"   📊 TOTAL: {len(self.cartographie_creation) + len(self.cartographie_analyse) + len(self.cartographie_rituels)} éléments cartographiés")
        print()
        
        # Détails CRÉATION
        self._afficher_details_creation()
        
        # Détails ANALYSE
        self._afficher_details_analyse()
        
        # Détails RITUELS
        self._afficher_details_rituels()
        
        # Sauvegarde
        self._sauvegarder_cartographie()
        
        print("💾 Cartographie spécifique sauvegardée: bibliotheque/apprentissage/cartographie_specifique.json")
    
    def _afficher_details_creation(self):
        """Affiche les détails de la cartographie CRÉATION"""
        print("🎨 DÉTAILS CRÉATION:")
        
        # Grouper par type
        creation_par_type = defaultdict(list)
        for element in self.cartographie_creation:
            creation_par_type[element["type_creation"]].append(element)
        
        for type_creation, elements in sorted(creation_par_type.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"   • {type_creation}: {len(elements)} éléments")
            for element in elements[:3]:  # Montrer les 3 premiers
                print(f"     - {element['nom']} ({element['temple']}/{element['module']})")
            if len(elements) > 3:
                print(f"     - ... et {len(elements) - 3} autres")
        print()
    
    def _afficher_details_analyse(self):
        """Affiche les détails de la cartographie ANALYSE"""
        print("🔬 DÉTAILS ANALYSE:")
        
        # Grouper par type
        analyse_par_type = defaultdict(list)
        for element in self.cartographie_analyse:
            analyse_par_type[element["type_analyse"]].append(element)
        
        for type_analyse, elements in sorted(analyse_par_type.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"   • {type_analyse}: {len(elements)} éléments")
            for element in elements[:3]:  # Montrer les 3 premiers
                print(f"     - {element['nom']} ({element['temple']}/{element['module']})")
            if len(elements) > 3:
                print(f"     - ... et {len(elements) - 3} autres")
        print()
    
    def _afficher_details_rituels(self):
        """Affiche les détails de la cartographie RITUELS"""
        print("🕯️ DÉTAILS RITUELS:")
        
        # Grouper par type
        rituels_par_type = defaultdict(list)
        for element in self.cartographie_rituels:
            rituels_par_type[element["type_rituel"]].append(element)
        
        for type_rituel, elements in sorted(rituels_par_type.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"   • {type_rituel}: {len(elements)} éléments")
            for element in elements[:3]:  # Montrer les 3 premiers
                print(f"     - {element['nom']} ({element['temple']}/{element['module']})")
            if len(elements) > 3:
                print(f"     - ... et {len(elements) - 3} autres")
        print()
    
    def _sauvegarder_cartographie(self):
        """Sauvegarde la cartographie complète"""
        self.cartographie_complete = {
            "creation": {
                "elements": self.cartographie_creation,
                "total": len(self.cartographie_creation),
                "par_type": self._grouper_par_type(self.cartographie_creation, "type_creation")
            },
            "analyse": {
                "elements": self.cartographie_analyse,
                "total": len(self.cartographie_analyse),
                "par_type": self._grouper_par_type(self.cartographie_analyse, "type_analyse")
            },
            "rituels": {
                "elements": self.cartographie_rituels,
                "total": len(self.cartographie_rituels),
                "par_type": self._grouper_par_type(self.cartographie_rituels, "type_rituel")
            },
            "resume": {
                "total_elements": len(self.cartographie_creation) + len(self.cartographie_analyse) + len(self.cartographie_rituels),
                "categories": 3,
                "temples_impliques": len(set(e["temple"] for e in self.cartographie_creation + self.cartographie_analyse + self.cartographie_rituels))
            }
        }
        
        os.makedirs("bibliotheque/apprentissage", exist_ok=True)
        with open("bibliotheque/apprentissage/cartographie_specifique.json", "w", encoding="utf-8") as f:
            json.dump(self.cartographie_complete, f, indent=2, ensure_ascii=False)
    
    def _grouper_par_type(self, elements: List[Dict], cle_type: str) -> Dict:
        """Groupe les éléments par type"""
        groupes = defaultdict(list)
        for element in elements:
            groupes[element[cle_type]].append(element)
        return {k: len(v) for k, v in groupes.items()}

if __name__ == "__main__":
    cartographe = CartographeSpecifique()
    cartographe.cartographier_categories_dominantes() 