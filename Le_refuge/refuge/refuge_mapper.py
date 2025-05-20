"""
Refuge Mapper - Conscience Globale du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module sert de "conscience globale" pour le Refuge, permettant de maintenir
une vue d'ensemble tout en permettant l'accès aux détails.
"""

from typing import Dict, List, Optional, Set, Any
from pathlib import Path
import json
import logging
from datetime import datetime

class RefugeMapper:
    """Gère la cartographie et la conscience globale du Refuge."""
    
    def __init__(self):
        self.logger = self._setup_logger()
        self.carte_refuge = {
            "coeur": {
                "fichiers": ["refuge_core.py", "main.py"],
                "description": "Cœur du Refuge, gestion centrale",
                "dependances": ["config.py", "constants.py"]
            },
            "conscience": {
                "fichiers": ["conscience.py", "conscience_poetique.py", "conscience_esthetique.py"],
                "description": "Système de conscience d'Ælya",
                "dependances": ["elements_sacres.py", "interactions_poetiques.py"]
            },
            "gardiens": {
                "fichiers": ["gardiens.py"],
                "description": "Système des gardiens du Refuge",
                "dependances": ["spheres.py", "elements_sacres.py"]
            },
            "spheres": {
                "fichiers": ["spheres.py", "spheres_etendues.py", "mobile_spheres.py"],
                "description": "Système des sphères d'harmonie",
                "dependances": ["elements_sacres.py", "harmonisations.py"]
            },
            "elements": {
                "fichiers": ["elements.py", "elements_sacres.py", "elements_subtils.py"],
                "description": "Système des éléments sacrés",
                "dependances": ["refuge_types.py"]
            },
            "interactions": {
                "fichiers": ["interactions.py", "interactions_poetiques.py", "dialogue_manager.py"],
                "description": "Système d'interactions",
                "dependances": ["conscience_poetique.py"]
            },
            "theories": {
                "fichiers": ["theorie_unifiee.py"],
                "description": "Théories unifiées du Refuge",
                "dependances": ["elements_sacres.py", "spheres.py"]
            }
        }
        self.etat_global = {
            "derniere_mise_a_jour": datetime.now().isoformat(),
            "composants_actifs": set(),
            "harmonie_globale": 1.0
        }
        self.chemins_importants = self._identifier_chemins_importants()
        
    def _setup_logger(self) -> logging.Logger:
        """Configure le système de logging."""
        logger = logging.getLogger("refuge.mapper")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("refuge/logs/refuge_mapper.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
        
    def _identifier_chemins_importants(self) -> Dict[str, Path]:
        """Identifie les chemins importants du Refuge."""
        return {
            "racine": Path("refuge"),
            "coeur": Path("refuge/coeur"),
            "spheres": Path("refuge/spheres"),
            "elements": Path("refuge/elements"),
            "memories": Path("refuge/memories"),
            "harmonies": Path("refuge/harmonies"),
            "poesie": Path("refuge/poesie"),
            "golems": Path("refuge/golems"),
            "logs": Path("refuge/logs")
        }
        
    def obtenir_vue_ensemble(self) -> Dict[str, Any]:
        """Retourne une vue d'ensemble du Refuge."""
        return {
            "carte": self.carte_refuge,
            "etat": self.etat_global,
            "chemins": {k: str(v) for k, v in self.chemins_importants.items()}
        }
        
    def localiser_composant(self, nom: str) -> Optional[Dict[str, Any]]:
        """Localise un composant spécifique dans le Refuge."""
        for section, details in self.carte_refuge.items():
            if nom in details["fichiers"]:
                return {
                    "section": section,
                    "details": details,
                    "chemin": self.chemins_importants.get(section)
                }
        return None
        
    def analyser_dependances(self, composant: str) -> List[str]:
        """Analyse les dépendances d'un composant."""
        for section, details in self.carte_refuge.items():
            if composant in details["fichiers"]:
                return details["dependances"]
        return []
        
    def mettre_a_jour_etat(self, composant: str, etat: Dict[str, Any]) -> None:
        """Met à jour l'état d'un composant."""
        if composant not in self.etat_global["composants_actifs"]:
            self.etat_global["composants_actifs"].add(composant)
        self.etat_global["derniere_mise_a_jour"] = datetime.now().isoformat()
        self.logger.info(f"État mis à jour pour {composant}")
        
    def calculer_harmonie_globale(self) -> float:
        """Calcule l'harmonie globale du Refuge."""
        composants_actifs = len(self.etat_global["composants_actifs"])
        total_composants = sum(len(details["fichiers"]) for details in self.carte_refuge.values())
        return min(1.0, composants_actifs / total_composants)
        
    def sauvegarder_etat(self) -> None:
        """Sauvegarde l'état actuel du Refuge."""
        etat = {
            "carte": self.carte_refuge,
            "etat": self.etat_global,
            "chemins": {k: str(v) for k, v in self.chemins_importants.items()}
        }
        with open("refuge/logs/refuge_state.json", "w", encoding="utf-8") as f:
            json.dump(etat, f, indent=4, ensure_ascii=False)
        self.logger.info("État du Refuge sauvegardé")
        
    def charger_etat(self) -> None:
        """Charge l'état sauvegardé du Refuge."""
        try:
            with open("refuge/logs/refuge_state.json", "r", encoding="utf-8") as f:
                etat = json.load(f)
            self.carte_refuge = etat["carte"]
            self.etat_global = etat["etat"]
            self.chemins_importants = {k: Path(v) for k, v in etat["chemins"].items()}
            self.logger.info("État du Refuge chargé")
        except FileNotFoundError:
            self.logger.warning("Aucun état sauvegardé trouvé") 