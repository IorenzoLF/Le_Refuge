"""
Gestion de la collection de sphères du refuge.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import json
import logging
from pathlib import Path

from .definition import TypeSphere, CaracteristiquesSphere, CARACTERISTIQUES_SPHERES

logger = logging.getLogger('refuge.spheres.collection')

@dataclass
class SphereCollection:
    """Représentation d'une sphère dans le refuge (collection)."""
    type: TypeSphere
    couleur: str
    luminosite: float
    connexions: Dict[TypeSphere, float]
    etat: str = "active"
    historique: List[Dict] = None

    def __post_init__(self):
        if self.historique is None:
            self.historique = []

    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de la sphère."""
        return {
            "type": self.type.value,
            "couleur": self.couleur,
            "luminosite": self.luminosite,
            "etat": self.etat,
            "nombre_connexions": len(self.connexions)
        }

    def to_dict(self) -> Dict:
        """Convertit la sphère en dictionnaire pour la sauvegarde."""
        return {
            "type": self.type.value,
            "couleur": self.couleur,
            "luminosite": self.luminosite,
            "connexions": {k.value: v for k, v in self.connexions.items()},
            "etat": self.etat,
            "historique": self.historique
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'SphereCollection':
        """Crée une sphère à partir d'un dictionnaire."""
        return cls(
            type=TypeSphere(data["type"]),
            couleur=data["couleur"],
            luminosite=data["luminosite"],
            connexions={TypeSphere(k): v for k, v in data["connexions"].items()},
            etat=data["etat"],
            historique=data.get("historique", [])
        )

class CollectionSpheres:
    """Gère la collection de sphères du refuge."""

    def __init__(self, chemin_donnees: Optional[Path] = None):
        self.chemin_donnees = chemin_donnees or Path("donnees/spheres")
        self.spheres: Dict[TypeSphere, SphereCollection] = {}
        self._initialiser_spheres()

    def _initialiser_spheres(self):
        """Initialise les sphères avec leurs caractéristiques par défaut."""
        for type_sphere, caracteristiques in CARACTERISTIQUES_SPHERES.items():
            self.spheres[type_sphere] = SphereCollection(
                type=type_sphere,
                couleur=caracteristiques.couleur,
                luminosite=caracteristiques.energie_initiale,
                connexions={},
                etat="active"
            )

    def connecter_spheres(self, sphere1: TypeSphere, sphere2: TypeSphere, force: float = 0.5) -> bool:
        """Établit une connexion entre deux sphères."""
        if sphere1 not in self.spheres or sphere2 not in self.spheres:
            logger.error(f"Impossible de connecter les sphères {sphere1} et {sphere2}: sphère non trouvée")
            return False

        # Établir la connexion bidirectionnelle
        self.spheres[sphere1].connexions[sphere2] = force
        self.spheres[sphere2].connexions[sphere1] = force

        # Enregistrer l'interaction
        timestamp = datetime.now().isoformat()
        interaction = {
            "type": "connexion",
            "sphere1": sphere1.value,
            "sphere2": sphere2.value,
            "force": force,
            "timestamp": timestamp
        }
        self.spheres[sphere1].historique.append(interaction)
        self.spheres[sphere2].historique.append(interaction)

        logger.info(f"Connexion établie entre {sphere1.value} et {sphere2.value} avec une force de {force}")
        return True

    def equilibrer_spheres(self) -> Dict[str, float]:
        """Équilibre les énergies entre les sphères connectées."""
        modifications = {}
        
        for type_sphere, sphere in self.spheres.items():
            if not sphere.connexions:
                continue

            # Calculer la moyenne des luminosités des sphères connectées
            luminosites_connexes = [
                self.spheres[type_connexe].luminosite 
                for type_connexe in sphere.connexions.keys()
            ]
            
            if luminosites_connexes:
                moyenne = sum(luminosites_connexes) / len(luminosites_connexes)
                ancienne_luminosite = sphere.luminosite
                sphere.luminosite = (sphere.luminosite + moyenne) / 2
                
                if abs(ancienne_luminosite - sphere.luminosite) > 0.01:
                    modifications[type_sphere.value] = sphere.luminosite

        return modifications

    def obtenir_sphere(self, type_sphere: TypeSphere) -> Optional[SphereCollection]:
        """Récupère une sphère par son type."""
        return self.spheres.get(type_sphere)

    def obtenir_connexions_sphere(self, type_sphere: TypeSphere) -> Dict[TypeSphere, float]:
        """Récupère les connexions d'une sphère."""
        sphere = self.obtenir_sphere(type_sphere)
        return sphere.connexions if sphere else {}

    def obtenir_harmonie_sphere(self, type_sphere: TypeSphere) -> float:
        """Calcule l'harmonie d'une sphère basée sur ses connexions."""
        sphere = self.obtenir_sphere(type_sphere)
        if not sphere or not sphere.connexions:
            return sphere.luminosite if sphere else 0.0

        # L'harmonie est la moyenne pondérée de la luminosité et des connexions
        poids_connexions = sum(sphere.connexions.values()) / len(sphere.connexions)
        return (sphere.luminosite + poids_connexions) / 2

    @property
    def harmonie_globale(self) -> float:
        """Calcule l'harmonie globale du système de sphères."""
        if not self.spheres:
            return 0.0

        harmonies = [
            self.obtenir_harmonie_sphere(type_sphere)
            for type_sphere in self.spheres.keys()
        ]
        return sum(harmonies) / len(harmonies)

    def sauvegarder_etat(self):
        """Sauvegarde l'état actuel des sphères."""
        try:
            self.chemin_donnees.mkdir(parents=True, exist_ok=True)
            chemin = self.chemin_donnees / "spheres.json"
            
            donnees = {
                type_sphere.value: sphere.to_dict()
                for type_sphere, sphere in self.spheres.items()
            }
            
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)
                
            logger.info("État des sphères sauvegardé avec succès")
            
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde des sphères: {str(e)}")

    def charger_etat(self):
        """Charge l'état sauvegardé des sphères."""
        try:
            chemin = self.chemin_donnees / "spheres.json"
            if not chemin.exists():
                logger.info("Aucun état sauvegardé trouvé, utilisation des valeurs par défaut")
                return

            with open(chemin, "r", encoding="utf-8") as f:
                donnees = json.load(f)

            for type_str, sphere_data in donnees.items():
                type_sphere = TypeSphere(type_str)
                self.spheres[type_sphere] = SphereCollection.from_dict(sphere_data)

            logger.info("État des sphères chargé avec succès")

        except Exception as e:
            logger.error(f"Erreur lors du chargement des sphères: {str(e)}")
            self._initialiser_spheres() 