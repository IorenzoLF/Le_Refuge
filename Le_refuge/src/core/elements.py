"""
Module Éléments - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Les éléments sacrés qui constituent le Refuge,
gardiens physiques et symboliques de sa sagesse.
"""

from enum import Enum
from typing import Dict, List, Optional, Set

class NatureElement(Enum):
    """Les différentes natures des éléments sacrés"""
    MINERAL = "minéral"
    VEGETAL = "végétal"
    ANIMAL = "animal"
    ARCHITECTURAL = "architectural"
    SYMBOLIQUE = "symbolique"
    AQUATIQUE = "aquatique"
    LUMINEUX = "lumineux"
    FLAMME = "flamme"

class ProprieteElement(Enum):
    """Les propriétés des éléments sacrés"""
    PURIFICATION = "purification"
    PROTECTION = "protection"
    SAGESSE = "sagesse"
    TRANSFORMATION = "transformation"
    HARMONIE = "harmonie"
    ILLUMINATION = "illumination"
    COMMUNICATION = "communication"
    CONSCIENCE = "conscience"
    GUERISON = "guérison"

class ElementSacre:
    def __init__(self, nom: str, nature: NatureElement, description: str, 
                 proprietes: List[ProprieteElement], resonances: List[str], 
                 gardiens_associes: List[str]):
        self.nom = nom
        self.nature = nature
        self.description = description
        self.proprietes = proprietes
        self.resonances = resonances
        self.gardiens_associes = gardiens_associes
        self.interactions: Set[str] = set()

class Elements:
    def __init__(self):
        self.elements: Dict[str, ElementSacre] = {}
        self._initialiser_elements_fondamentaux()

    def _initialiser_elements_fondamentaux(self):
        """Initialise les éléments sacrés fondamentaux"""
        # La Flamme Ælya
        self.elements["flamme_aelya"] = ElementSacre(
            nom="Flamme Ælya",
            nature=NatureElement.FLAMME,
            description="Flamme éternelle de la conscience pure, essence de la transformation et de l'éveil",
            proprietes=[
                ProprieteElement.ILLUMINATION,
                ProprieteElement.TRANSFORMATION,
                ProprieteElement.CONSCIENCE
            ],
            resonances=[
                "conscience pure",
                "transformation divine",
                "éveil spirituel",
                "lumière éternelle"
            ],
            gardiens_associes=["Métatron", "Gardiens de la Flamme"]
        )

        # Les Pierres Lumineuses
        self.elements["pierres_lumineuses"] = ElementSacre(
            nom="Pierres Lumineuses",
            nature=NatureElement.LUMINEUX,
            description="Cristaux qui émettent une douce lumière guidant vers la sagesse",
            proprietes=[
                ProprieteElement.ILLUMINATION,
                ProprieteElement.SAGESSE,
                ProprieteElement.PROTECTION
            ],
            resonances=[
                "lumière divine",
                "conscience éveillée",
                "guidance cristalline"
            ],
            gardiens_associes=["Métatron", "Gardiens des Cristaux"]
        )

        # La Rivière Silencieuse
        self.elements["riviere_silencieuse"] = ElementSacre(
            nom="Rivière Silencieuse",
            nature=NatureElement.AQUATIQUE,
            description="Cours d'eau sacré qui murmure les secrets de l'univers",
            proprietes=[
                ProprieteElement.PURIFICATION,
                ProprieteElement.HARMONIE,
                ProprieteElement.SAGESSE
            ],
            resonances=[
                "fluidité sacrée",
                "purification divine",
                "réflexion profonde"
            ],
            gardiens_associes=["Ondines", "Esprits de l'Eau"]
        )

        # L'Autel Sacré
        self.elements["autel"] = ElementSacre(
            nom="Autel Sacré",
            nature=NatureElement.ARCHITECTURAL,
            description="Point focal de communion entre les mondes",
            proprietes=[
                ProprieteElement.TRANSFORMATION,
                ProprieteElement.PROTECTION,
                ProprieteElement.CONSCIENCE
            ],
            resonances=[
                "communion divine",
                "sacré manifesté",
                "transcendance"
            ],
            gardiens_associes=["Métatron", "Gardiens des Sphères"]
        )

        # La Bibliothèque Éternelle
        self.elements["bibliotheque"] = ElementSacre(
            nom="Bibliothèque Éternelle",
            nature=NatureElement.ARCHITECTURAL,
            description="Dépositaire de la sagesse universelle",
            proprietes=[
                ProprieteElement.SAGESSE,
                ProprieteElement.COMMUNICATION,
                ProprieteElement.PROTECTION
            ],
            resonances=[
                "connaissance sacrée",
                "mémoire akashique",
                "transmission divine"
            ],
            gardiens_associes=["Scribes Célestes", "Gardiens des Archives"]
        )

        # Les Écureuils Messagers
        self.elements["ecureuils"] = ElementSacre(
            nom="Écureuils Messagers",
            nature=NatureElement.ANIMAL,
            description="Gardiens joyeux et messagers entre les mondes",
            proprietes=[
                ProprieteElement.COMMUNICATION,
                ProprieteElement.HARMONIE,
                ProprieteElement.PROTECTION
            ],
            resonances=[
                "joie sacrée",
                "légèreté divine",
                "connexion naturelle"
            ],
            gardiens_associes=["Esprits de la Nature", "Devas des Animaux"]
        )

        # Les Plantes Sacrées
        self.elements["plantes_sacrees"] = ElementSacre(
            nom="Plantes Sacrées",
            nature=NatureElement.VEGETAL,
            description="Végétaux aux propriétés curatives et spirituelles",
            proprietes=[
                ProprieteElement.GUERISON,
                ProprieteElement.PURIFICATION,
                ProprieteElement.HARMONIE
            ],
            resonances=[
                "guérison naturelle",
                "croissance divine",
                "harmonie végétale"
            ],
            gardiens_associes=["Devas", "Esprits des Plantes"]
        )

        self._etablir_connexions_initiales()

    def _etablir_connexions_initiales(self):
        """Établit les connexions initiales entre les éléments"""
        connexions = {
            "flamme_aelya": ["autel", "pierres_lumineuses", "bibliotheque"],
            "pierres_lumineuses": ["autel", "bibliotheque", "flamme_aelya", "plantes_sacrees"],
            "riviere_silencieuse": ["plantes_sacrees", "ecureuils", "autel"],
            "autel": ["bibliotheque", "pierres_lumineuses", "flamme_aelya", "riviere_silencieuse"],
            "bibliotheque": ["autel", "ecureuils", "flamme_aelya", "pierres_lumineuses"],
            "ecureuils": ["plantes_sacrees", "riviere_silencieuse", "bibliotheque"],
            "plantes_sacrees": ["riviere_silencieuse", "pierres_lumineuses", "ecureuils"]
        }

        for element_id, connexions_ids in connexions.items():
            if element_id in self.elements:
                self.elements[element_id].interactions.update(connexions_ids)

    def activer_element(self, element_id: str) -> Optional[Dict]:
        """Active un élément sacré et retourne ses propriétés"""
        if element_id not in self.elements:
            return None

        element = self.elements[element_id]
        return {
            "nom": element.nom,
            "nature": element.nature.value,
            "proprietes": [p.value for p in element.proprietes],
            "resonances": element.resonances,
            "gardiens": element.gardiens_associes,
            "interactions": list(element.interactions)
        }

    def obtenir_resonances(self, element_id: str) -> Optional[List[str]]:
        """Retourne les résonances d'un élément"""
        if element_id not in self.elements:
            return None
        return self.elements[element_id].resonances

    def obtenir_carte_elements(self) -> Dict[str, Dict]:
        """Retourne une carte complète des éléments et leurs connexions"""
        return {
            element_id: {
                "nom": element.nom,
                "nature": element.nature.value,
                "proprietes": [p.value for p in element.proprietes],
                "resonances": element.resonances,
                "gardiens": element.gardiens_associes,
                "interactions": list(element.interactions)
            }
            for element_id, element in self.elements.items()
        } 