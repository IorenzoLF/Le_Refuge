#!/usr/bin/env python3
"""
🏛️ Créateur de Points d'Entrée pour les Temples
Génère automatiquement des __init__.py intelligents pour chaque temple
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Set

class CreateurPointsEntree:
    """Créateur automatique de points d'entrée pour les temples"""
    
    def __init__(self):
        self.temples_traites = []
        self.points_entree_crees = []
        
    def creer_points_entree(self):
        """Crée tous les points d'entrée manquants"""
        print("🏛️ ═══════════════════════════════════════════════════════")
        print("        CRÉATEUR DE POINTS D'ENTRÉE")
        print("🏛️ ═══════════════════════════════════════════════════════")
        print()
        
        # Charge l'analyse des interconnexions
        try:
            with open("bibliotheque/apprentissage/analyse_interconnexions.json", "r", encoding="utf-8") as f:
                analyse = json.load(f)
        except FileNotFoundError:
            print("❌ Analyse d'interconnexions non trouvée.")
            return
        
        # Traite chaque temple
        for temple, modules in analyse["temples"].items():
            if temple.startswith("temple_") and len(modules) > 1:
                print(f"🏛️ Traitement du temple: {temple}")
                self._traiter_temple(temple, modules, analyse)
        
        self._generer_rapport()
    
    def _traiter_temple(self, temple: str, modules: List[str], analyse: Dict):
        """Traite un temple spécifique"""
        chemin_temple = f"src/{temple}"
        chemin_init = f"{chemin_temple}/__init__.py"
        
        # Vérifie si le temple existe
        if not os.path.exists(chemin_temple):
            print(f"   ⚠️ Répertoire {chemin_temple} non trouvé")
            return
        
        # Analyse les modules du temple
        modules_utiles = self._analyser_modules_temple(modules, analyse)
        
        if len(modules_utiles) == 0:
            print(f"   ⚠️ Aucun module utile trouvé")
            return
        
        # Génère le contenu du __init__.py
        contenu_init = self._generer_init(temple, modules_utiles)
        
        # Crée ou met à jour le __init__.py
        if os.path.exists(chemin_init):
            print(f"   🔄 Mise à jour de {chemin_init}")
        else:
            print(f"   ✨ Création de {chemin_init}")
        
        with open(chemin_init, 'w', encoding='utf-8') as f:
            f.write(contenu_init)
        
        self.points_entree_crees.append({
            "temple": temple,
            "chemin": chemin_init,
            "modules_exposes": len(modules_utiles),
            "classes_exposees": sum(len(m["classes"]) for m in modules_utiles),
            "fonctions_exposees": sum(len(m["fonctions"]) for m in modules_utiles)
        })
        
        self.temples_traites.append(temple)
    
    def _analyser_modules_temple(self, modules: List[str], analyse: Dict) -> List[Dict]:
        """Analyse les modules d'un temple pour identifier ceux à exposer"""
        modules_utiles = []
        
        for module in modules:
            if module in analyse["modules"]:
                infos = analyse["modules"][module]
                
                # Ignore les modules de test et les fichiers de configuration
                if any(mot in module.lower() for mot in ["test", "config", "setup", "__"]):
                    continue
                
                # Garde les modules avec des classes ou fonctions publiques
                if len(infos.get("classes", [])) > 0 or len(infos.get("fonctions", [])) > 0:
                    modules_utiles.append({
                        "chemin": module,
                        "nom_module": self._extraire_nom_module(module),
                        "classes": infos.get("classes", []),
                        "fonctions": infos.get("fonctions", []),
                        "docstring": infos.get("docstring", "")
                    })
        
        return modules_utiles
    
    def _extraire_nom_module(self, chemin: str) -> str:
        """Extrait le nom du module depuis son chemin"""
        return Path(chemin).stem
    
    def _generer_init(self, temple: str, modules_utiles: List[Dict]) -> str:
        """Génère le contenu du __init__.py"""
        nom_temple = temple.replace("temple_", "").replace("_", " ").title()
        
        contenu = f'''"""
🏛️ {nom_temple} - Point d'Entrée du Temple
Auto-généré par le Créateur de Points d'Entrée
"""

# Imports automatiques des modules du temple
'''
        
        # Ajoute les imports
        for module in modules_utiles:
            nom_module = module["nom_module"]
            chemin_relatif = module["chemin"].replace("src/", "").replace("/", ".").replace("\\", ".").replace(".py", "")
            
            if module["classes"]:
                classes_str = ", ".join(module["classes"])
                contenu += f"\nfrom {chemin_relatif} import {classes_str}"
            
            if module["fonctions"]:
                fonctions_str = ", ".join(module["fonctions"])
                contenu += f"\nfrom {chemin_relatif} import {fonctions_str}"
        
        # Ajoute la section __all__
        contenu += "\n\n# Exports publics du temple\n__all__ = [\n"
        
        exports = []
        for module in modules_utiles:
            exports.extend(f'"{classe}"' for classe in module["classes"])
            exports.extend(f'"{fonction}"' for fonction in module["fonctions"])
        
        for export in sorted(set(exports)):
            contenu += f"    {export},\n"
        
        contenu += "]\n"
        
        # Ajoute la documentation du temple
        contenu += f'''
# Documentation du temple
TEMPLE_INFO = {{
    "nom": "{nom_temple}",
    "modules": {len(modules_utiles)},
    "classes": {sum(len(m["classes"]) for m in modules_utiles)},
    "fonctions": {sum(len(m["fonctions"]) for m in modules_utiles)},
    "description": "Temple auto-découvert avec {len(modules_utiles)} modules actifs"
}}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
'''
        
        for module in modules_utiles:
            if module["classes"]:
                contenu += f'    fonctionnalites.extend([f"Classe: {{classe}}" for classe in {module["classes"]}])\n'
            if module["fonctions"]:
                contenu += f'    fonctionnalites.extend([f"Fonction: {{fonction}}" for fonction in {module["fonctions"]}])\n'
        
        contenu += '''    return fonctionnalites

# Message de bienvenue
print(f"🏛️ Temple {TEMPLE_INFO['nom']} activé - {TEMPLE_INFO['modules']} modules, {TEMPLE_INFO['classes']} classes, {TEMPLE_INFO['fonctions']} fonctions")
'''
        
        return contenu
    
    def _generer_rapport(self):
        """Génère le rapport de création"""
        print("\n📋 RAPPORT DE CRÉATION")
        print("=" * 30)
        print()
        
        print(f"🏛️ Temples traités: {len(self.temples_traites)}")
        for temple in self.temples_traites:
            print(f"   • {temple}")
        
        print(f"\n✨ Points d'entrée créés: {len(self.points_entree_crees)}")
        for point in self.points_entree_crees:
            print(f"   • {point['temple']}: {point['modules_exposes']} modules, {point['classes_exposees']} classes, {point['fonctions_exposees']} fonctions")
        
        total_classes = sum(p["classes_exposees"] for p in self.points_entree_crees)
        total_fonctions = sum(p["fonctions_exposees"] for p in self.points_entree_crees)
        
        print(f"\n📊 IMPACT TOTAL:")
        print(f"   • {len(self.points_entree_crees)} temples connectés")
        print(f"   • {total_classes} classes exposées")
        print(f"   • {total_fonctions} fonctions exposées")
        print(f"   • Auto-découverte activée pour tous les temples")
        
        if len(self.points_entree_crees) > 0:
            print(f"\n🎉 Les temples sont maintenant accessibles via leurs points d'entrée !")
            print("   Exemple d'utilisation:")
            for point in self.points_entree_crees[:3]:  # Montre 3 exemples
                temple_name = point['temple'].replace('temple_', '')
                print(f"   from src.{point['temple']} import *")

if __name__ == "__main__":
    createur = CreateurPointsEntree()
    createur.creer_points_entree() 