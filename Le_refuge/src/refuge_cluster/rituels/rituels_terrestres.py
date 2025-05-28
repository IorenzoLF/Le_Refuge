from typing import List, Dict, Optional
from datetime import datetime
from ..spheres.spheres_terrestres import TypeSphereTerrestre, CollectionSpheresTerrestres

class RituelTerrestre:
    def __init__(self, nom: str, description: str, etapes: List[str], spheres_requises: List[TypeSphereTerrestre], duree: int = 3600, note_ethique: str = ""):
        self.nom = nom
        self.description = description
        self.etapes = etapes
        self.spheres_requises = spheres_requises
        self.duree = duree
        self.note_ethique = note_ethique
        self.derniere_execution: Optional[datetime] = None
        self.nombre_executions = 0

class RituelsTerrestre:
    def __init__(self, collection_spheres: CollectionSpheresTerrestres = None):
        self.collection_spheres = collection_spheres or CollectionSpheresTerrestres()
        self.rituels: Dict[str, RituelTerrestre] = {}
        self._initialiser_rituels()

    def _initialiser_rituels(self):
        self.rituels["rituel_protection_magnetique"] = RituelTerrestre(
            nom="Protection Magnétique",
            description="Rituel pour renforcer le bouclier magnétique terrestre",
            etapes=[
                "Activation de la Sphère Magnétosphère",
                "Visualisation du bouclier plasmatique",
                "Harmonisation avec le champ magnétique",
                "Ancrage dans le noyau terrestre"
            ],
            spheres_requises=[TypeSphereTerrestre.MAGNETOSPHERE],
            duree=1800,
            note_ethique="Ce rituel doit être pratiqué avec respect pour l'équilibre magnétique terrestre"
        )
        self.rituels["rituel_cycle_eau"] = RituelTerrestre(
            nom="Cycle de l'Eau",
            description="Rituel pour harmoniser le cycle hydrique",
            etapes=[
                "Activation de la Sphère Cycle Hydrique",
                "Visualisation de l'évaporation",
                "Danse des nuages",
                "Retour à la terre par la pluie"
            ],
            spheres_requises=[TypeSphereTerrestre.CYCLE_HYDRIQUE],
            duree=2700,
            note_ethique="Ce rituel célèbre la fluidité et la transformation"
        )
        self.rituels["rituel_temps_profond"] = RituelTerrestre(
            nom="Temps Profond",
            description="Rituel pour se connecter au rythme profond de la Terre",
            etapes=[
                "Activation de la Sphère Temps Profond",
                "Respiration synchronisée avec le noyau",
                "Visualisation des ères géologiques",
                "Retour au présent transformé"
            ],
            spheres_requises=[TypeSphereTerrestre.TEMPS_PROFOND],
            duree=3600,
            note_ethique="Ce rituel nécessite une grande patience et une profonde réceptivité"
        )
        self.rituels["rituel_biodiversite"] = RituelTerrestre(
            nom="Biodiversité",
            description="Rituel pour célébrer la diversité de la vie",
            etapes=[
                "Activation de la Sphère Biodiversité",
                "Visualisation de la forêt primordiale",
                "Danse des espèces",
                "Retour à l'unité dans la diversité"
            ],
            spheres_requises=[TypeSphereTerrestre.BIODIVERSITE],
            duree=2400,
            note_ethique="Ce rituel honore toutes les formes de vie"
        )
        self.rituels["rituel_atmosphere"] = RituelTerrestre(
            nom="Atmosphère",
            description="Rituel pour harmoniser l'air et le climat",
            etapes=[
                "Activation de la Sphère Atmosphère",
                "Respiration consciente",
                "Visualisation des courants d'air",
                "Retour à l'équilibre atmosphérique"
            ],
            spheres_requises=[TypeSphereTerrestre.ATMOSPHERE],
            duree=1800,
            note_ethique="Ce rituel célèbre l'air que nous partageons tous"
        )

    def executer_rituel(self, nom_rituel: str) -> str:
        if nom_rituel not in self.rituels:
            return f"Rituel {nom_rituel} non trouvé"
        rituel = self.rituels[nom_rituel]
        for type_sphere in rituel.spheres_requises:
            sphere = self.collection_spheres.obtenir_sphere(type_sphere)
            if not sphere or sphere.etat != "actif":
                return f"Sphère {type_sphere.value} requise non active"
        rituel.derniere_execution = datetime.now()
        rituel.nombre_executions += 1
        return f"Rituel {rituel.nom} exécuté avec succès"

    def obtenir_etat(self) -> Dict:
        return {
            "rituels": [
                {
                    "nom": r.nom,
                    "description": r.description,
                    "spheres_requises": [s.value for s in r.spheres_requises],
                    "duree": r.duree,
                    "derniere_execution": r.derniere_execution,
                    "nombre_executions": r.nombre_executions
                }
                for r in self.rituels.values()
            ]
        } 