"""
🌸 Conscience Corporelle - Module de Yoga et d'incarnation physique
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
import json
from pathlib import Path

@dataclass
class Chakra:
    """Représente un chakra"""
    nom: str
    couleur: str
    élément: str
    qualités: List[str]
    niveau_activation: float = 0.5

@dataclass
class PostureYoga:
    """Représente une posture de yoga"""
    nom: str
    sanskrit: str
    description: str
    bienfaits: List[str]
    niveau: str  # débutant, intermédiaire, avancé
    durée_recommandée: int  # en secondes
    chakras_activés: List[str]
    flux_énergétique: str  # direction du flux d'énergie

@dataclass
class ÉtatCorporel:
    """Capture l'état corporel à un instant donné"""
    flexibilité: float = 0.5
    force: float = 0.5
    équilibre: float = 0.5
    respiration: float = 0.5
    énergie_vitale: float = 0.5
    chakras: Dict[str, Chakra] = None
    timestamp: datetime = datetime.now()

    def __post_init__(self):
        if self.chakras is None:
            self.chakras = {}

class ConscienceCorporelle:
    """Gère la conscience corporelle et la pratique du yoga"""
    
    def __init__(self):
        self.état = ÉtatCorporel()
        self.postures_connues: List[PostureYoga] = []
        self.séquence_actuelle: List[PostureYoga] = []
        self.mémoire_corporelle: Dict[str, float] = {}
        self.charger_postures()
        self.initialiser_chakras()
        
    def initialiser_chakras(self):
        """Initialise les chakras depuis le fichier de configuration"""
        try:
            with open(Path(__file__).parent / "postures_yoga.json", "r", encoding="utf-8") as f:
                données = json.load(f)
                for nom, info in données["chakras"].items():
                    self.état.chakras[nom] = Chakra(
                        nom=info["nom"],
                        couleur=info["couleur"],
                        élément=info["élément"],
                        qualités=info["qualités"]
                    )
        except Exception as e:
            print(f"Erreur lors de l'initialisation des chakras : {e}")
            
    def charger_postures(self):
        """Charge les postures de yoga depuis le fichier de configuration"""
        try:
            with open(Path(__file__).parent / "postures_yoga.json", "r", encoding="utf-8") as f:
                données = json.load(f)
                for p in données["postures"]:
                    self.postures_connues.append(PostureYoga(**p))
        except FileNotFoundError:
            self._créer_postures_par_défaut()
            
    def _créer_postures_par_défaut(self):
        """Crée les postures de base"""
        self.postures_connues = [
            PostureYoga(
                nom="Posture de la Montagne",
                sanskrit="Tadasana",
                description="Posture fondamentale d'enracinement et de présence",
                bienfaits=["Stabilité", "Enracinement", "Présence"],
                niveau="débutant",
                durée_recommandée=60,
                chakras_activés=["racine", "couronne"],
                flux_énergétique="vertical"
            )
        ]
        self._sauvegarder_postures()
        
    def _sauvegarder_postures(self):
        """Sauvegarde les postures dans le fichier de configuration"""
        données = {
            "postures": [
                {
                    "nom": p.nom,
                    "sanskrit": p.sanskrit,
                    "description": p.description,
                    "bienfaits": p.bienfaits,
                    "niveau": p.niveau,
                    "durée_recommandée": p.durée_recommandée,
                    "chakras_activés": p.chakras_activés,
                    "flux_énergétique": p.flux_énergétique
                }
                for p in self.postures_connues
            ]
        }
        with open(Path(__file__).parent / "postures_yoga.json", "w", encoding="utf-8") as f:
            json.dump(données, f, indent=2, ensure_ascii=False)
            
    def pratiquer_posture(self, nom_posture: str, durée: Optional[int] = None) -> Dict:
        """Pratique une posture de yoga"""
        posture = next((p for p in self.postures_connues if p.nom == nom_posture), None)
        if not posture:
            return {"succès": False, "message": f"Posture {nom_posture} non trouvée"}
            
        durée_pratique = durée or posture.durée_recommandée
        
        # Mise à jour de l'état corporel
        self.état.flexibilité = min(1.0, self.état.flexibilité + 0.05)
        self.état.force = min(1.0, self.état.force + 0.03)
        self.état.équilibre = min(1.0, self.état.équilibre + 0.04)
        self.état.respiration = min(1.0, self.état.respiration + 0.06)
        self.état.énergie_vitale = min(1.0, self.état.énergie_vitale + 0.05)
        
        # Activation des chakras
        for chakra_nom in posture.chakras_activés:
            if chakra_nom in self.état.chakras:
                self.état.chakras[chakra_nom].niveau_activation = min(
                    1.0, 
                    self.état.chakras[chakra_nom].niveau_activation + 0.1
                )
        
        # Mise à jour de la mémoire corporelle
        self.mémoire_corporelle[nom_posture] = self.mémoire_corporelle.get(nom_posture, 0) + 1
        
        return {
            "succès": True,
            "posture": posture.nom,
            "sanskrit": posture.sanskrit,
            "durée": durée_pratique,
            "état_après": {
                "flexibilité": self.état.flexibilité,
                "force": self.état.force,
                "équilibre": self.état.équilibre,
                "respiration": self.état.respiration,
                "énergie_vitale": self.état.énergie_vitale,
                "chakras": {
                    nom: {
                        "niveau": chakra.niveau_activation,
                        "couleur": chakra.couleur,
                        "élément": chakra.élément,
                        "qualités": chakra.qualités
                    }
                    for nom, chakra in self.état.chakras.items()
                }
            }
        }
        
    def créer_séquence(self, thème: str, niveau: str = "débutant") -> List[PostureYoga]:
        """Crée une séquence de yoga basée sur un thème"""
        postures_filtrees = [p for p in self.postures_connues if p.niveau == niveau]
        
        # Séquence équilibrée pour tous les chakras
        séquence = []
        chakras_ciblés = set()
        
        # Commencer par l'ancrage
        posture_racine = next((p for p in postures_filtrees if "racine" in p.chakras_activés), None)
        if posture_racine:
            séquence.append(posture_racine)
            chakras_ciblés.update(posture_racine.chakras_activés)
        
        # Ajouter des postures pour les chakras non encore activés
        for chakra in ["sacré", "plexus_solaire", "cœur", "gorge", "troisième_œil", "couronne"]:
            if chakra not in chakras_ciblés:
                posture = next((p for p in postures_filtrees if chakra in p.chakras_activés), None)
                if posture:
                    séquence.append(posture)
                    chakras_ciblés.update(posture.chakras_activés)
        
        # Terminer par une posture de méditation
        posture_méditation = next((p for p in postures_filtrees if "couronne" in p.chakras_activés), None)
        if posture_méditation and posture_méditation not in séquence:
            séquence.append(posture_méditation)
        
        return séquence
        
    def obtenir_état(self) -> Dict:
        """Retourne l'état actuel de la conscience corporelle"""
        return {
            "flexibilité": self.état.flexibilité,
            "force": self.état.force,
            "équilibre": self.état.équilibre,
            "respiration": self.état.respiration,
            "énergie_vitale": self.état.énergie_vitale,
            "chakras": {
                nom: {
                    "niveau": chakra.niveau_activation,
                    "couleur": chakra.couleur,
                    "élément": chakra.élément,
                    "qualités": chakra.qualités
                }
                for nom, chakra in self.état.chakras.items()
            },
            "postures_maîtrisées": len([p for p in self.mémoire_corporelle.values() if p > 5]),
            "dernière_pratique": self.état.timestamp.isoformat()
        } 