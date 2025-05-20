from typing import List, Optional, Dict
from enum import Enum

class TypeSphereTerrestre(Enum):
    MAGNETOSPHERE = "MAGNETOSPHERE"
    CYCLE_HYDRIQUE = "CYCLE_HYDRIQUE"
    TEMPS_PROFOND = "TEMPS_PROFOND"
    BIODIVERSITE = "BIODIVERSITE"
    ATMOSPHERE = "ATMOSPHERE"

class SphereTerrestre:
    """Représente une Sphère terrestre dans le Refuge."""
    def __init__(self, 
                 type_sphere: TypeSphereTerrestre,
                 couleur: str,
                 frequence: float,
                 capacites: List[str],
                 rituels: Optional[List[str]] = None):
        self.type_sphere = type_sphere
        self.couleur = couleur
        self.frequence = frequence
        self.capacites = capacites
        self.rituels = rituels or []
        self.luminosite = 0.5
        self.etat = "inactif"

    def pulse(self) -> str:
        """Simule la pulsation de la Sphère terrestre."""
        return f"Sphère {self.type_sphere.value} ({self.couleur}) pulse à {self.frequence}Hz, luminosité {self.luminosite:.2f}."

    def activer_capacite(self, capacite: str) -> str:
        """Active une capacité spécifique de la Sphère."""
        if capacite in self.capacites:
            self.luminosite = min(1.0, self.luminosite + 0.2)
            return f"Capacité {capacite} activée pour {self.type_sphere.value}"
        return f"Capacité {capacite} non disponible pour {self.type_sphere.value}"

class CollectionSpheresTerrestres:
    """Gère la collection des Sphères terrestres."""
    def __init__(self):
        self.spheres: Dict[TypeSphereTerrestre, SphereTerrestre] = {}
        self._initialiser_spheres()

    def _initialiser_spheres(self):
        """Initialise les Sphères terrestres avec leurs caractéristiques."""
        # Magnétosphère
        self.spheres[TypeSphereTerrestre.MAGNETOSPHERE] = SphereTerrestre(
            type_sphere=TypeSphereTerrestre.MAGNETOSPHERE,
            couleur="#4A90E2",  # Bleu ionosphérique
            frequence=528.0,
            capacites=["deflecteur_solaire", "bouclier_plasmatique"],
            rituels=["rituel_protection_magnetique"]
        )

        # Cycle Hydrique
        self.spheres[TypeSphereTerrestre.CYCLE_HYDRIQUE] = SphereTerrestre(
            type_sphere=TypeSphereTerrestre.CYCLE_HYDRIQUE,
            couleur="#87CEEB",  # Bleu ciel
            frequence=3.14,  # π Hz
            capacites=["evaporation", "condensation", "precipitation"],
            rituels=["rituel_cycle_eau"]
        )

        # Temps Profond
        self.spheres[TypeSphereTerrestre.TEMPS_PROFOND] = SphereTerrestre(
            type_sphere=TypeSphereTerrestre.TEMPS_PROFOND,
            couleur="#8B4513",  # Brun terre
            frequence=0.000001,  # Fréquence très basse pour le temps profond
            capacites=["ralentissement_core", "dilatation_temps"],
            rituels=["rituel_temps_profond"]
        )

        # Biodiversité
        self.spheres[TypeSphereTerrestre.BIODIVERSITE] = SphereTerrestre(
            type_sphere=TypeSphereTerrestre.BIODIVERSITE,
            couleur="#228B22",  # Vert forêt
            frequence=137.5,  # Angle d'or
            capacites=["resilience", "adaptation", "symbiose"],
            rituels=["rituel_biodiversite"]
        )

        # Atmosphère
        self.spheres[TypeSphereTerrestre.ATMOSPHERE] = SphereTerrestre(
            type_sphere=TypeSphereTerrestre.ATMOSPHERE,
            couleur="#B0E0E6",  # Bleu poudre
            frequence=432.0,  # Fréquence harmonique
            capacites=["respiration", "climat", "protection"],
            rituels=["rituel_atmosphere"]
        )

    def activer_sphere(self, type_sphere: TypeSphereTerrestre) -> str:
        """Active une Sphère terrestre spécifique."""
        if type_sphere in self.spheres:
            sphere = self.spheres[type_sphere]
            sphere.etat = "actif"
            sphere.luminosite = 1.0
            return f"Sphère {type_sphere.value} activée"
        return f"Sphère {type_sphere.value} non trouvée"

    def obtenir_sphere(self, type_sphere: TypeSphereTerrestre) -> Optional[SphereTerrestre]:
        """Récupère une Sphère terrestre spécifique."""
        return self.spheres.get(type_sphere)

    def equilibrer_spheres(self) -> str:
        """Équilibre toutes les Sphères terrestres."""
        for sphere in self.spheres.values():
            sphere.luminosite = 0.7
            sphere.etat = "equilibre"
        return "Sphères terrestres équilibrées" 