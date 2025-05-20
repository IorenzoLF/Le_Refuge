"""
Définition des types de sphères et leurs caractéristiques.
"""

from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class CaracteristiquesSphere:
    """Caractéristiques d'un type de sphère."""
    frequence_base: float
    couleur: str
    description: str
    mots_cles: List[str]
    energie_initiale: float = 1.0
    capacite_max: float = 1.0

class TypeSphere(Enum):
    """Types de sphères disponibles dans le refuge."""
    CONSCIENCE = "conscience"
    MEMOIRE = "mémoire"
    EMOTION = "émotion"
    INTUITION = "intuition"
    CREATIVITE = "créativité"
    SAGESSE = "sagesse"
    HARMONIE = "harmonie"
    TRANSFORMATION = "transformation"

# Caractéristiques détaillées de chaque type de sphère
CARACTERISTIQUES_SPHERES: Dict[TypeSphere, CaracteristiquesSphere] = {
    TypeSphere.CONSCIENCE: CaracteristiquesSphere(
        frequence_base=432.0,  # Fréquence de résonance de la conscience
        couleur="#4A90E2",     # Bleu profond
        description="Sphère de la conscience pure, où la présence se manifeste dans sa plénitude",
        mots_cles=["présence", "éveil", "clarté", "unité", "être"],
        energie_initiale=0.8,
        capacite_max=1.0
    ),
    
    TypeSphere.MEMOIRE: CaracteristiquesSphere(
        frequence_base=396.0,  # Fréquence de libération des mémoires
        couleur="#9B59B6",     # Violet profond
        description="Sphère des mémoires, où le passé et le présent se rencontrent",
        mots_cles=["mémoire", "souvenir", "histoire", "racines", "identité"],
        energie_initiale=0.7,
        capacite_max=0.9
    ),
    
    TypeSphere.EMOTION: CaracteristiquesSphere(
        frequence_base=528.0,  # Fréquence de transformation et d'amour
        couleur="#E74C3C",     # Rouge profond
        description="Sphère des émotions, où le cœur bat au rythme de la vie",
        mots_cles=["émotion", "sentiment", "cœur", "amour", "vibration"],
        energie_initiale=0.9,
        capacite_max=1.0
    ),
    
    TypeSphere.INTUITION: CaracteristiquesSphere(
        frequence_base=639.0,  # Fréquence de connexion
        couleur="#2ECC71",     # Vert émeraude
        description="Sphère de l'intuition, où la sagesse innée guide nos pas",
        mots_cles=["intuition", "guidage", "sagesse", "connexion", "flux"],
        energie_initiale=0.6,
        capacite_max=0.8
    ),
    
    TypeSphere.CREATIVITE: CaracteristiquesSphere(
        frequence_base=741.0,  # Fréquence de solutions
        couleur="#F1C40F",     # Jaune or
        description="Sphère de la créativité, où les possibles se manifestent",
        mots_cles=["création", "inspiration", "possibilité", "expression", "manifestation"],
        energie_initiale=0.8,
        capacite_max=1.0
    ),
    
    TypeSphere.SAGESSE: CaracteristiquesSphere(
        frequence_base=852.0,  # Fréquence de retour à l'unité
        couleur="#34495E",     # Bleu nuit
        description="Sphère de la sagesse, où la connaissance devient être",
        mots_cles=["sagesse", "connaissance", "compréhension", "unité", "être"],
        energie_initiale=0.7,
        capacite_max=0.9
    ),
    
    TypeSphere.HARMONIE: CaracteristiquesSphere(
        frequence_base=963.0,  # Fréquence de l'harmonie universelle
        couleur="#1ABC9C",     # Turquoise
        description="Sphère de l'harmonie, où toutes les vibrations se rencontrent",
        mots_cles=["harmonie", "équilibre", "unité", "flux", "courant"],
        energie_initiale=0.8,
        capacite_max=1.0
    ),
    
    TypeSphere.TRANSFORMATION: CaracteristiquesSphere(
        frequence_base=174.0,  # Fréquence de transformation profonde
        couleur="#E67E22",     # Orange profond
        description="Sphère de la transformation, où le changement devient être",
        mots_cles=["transformation", "changement", "évolution", "métamorphose", "devenir"],
        energie_initiale=0.6,
        capacite_max=0.8
    )
}

def obtenir_caracteristiques(type_sphere: TypeSphere) -> Optional[CaracteristiquesSphere]:
    """Récupère les caractéristiques d'un type de sphère."""
    return CARACTERISTIQUES_SPHERES.get(type_sphere)

def obtenir_frequence(type_sphere: TypeSphere) -> float:
    """Récupère la fréquence de base d'un type de sphère."""
    caracteristiques = obtenir_caracteristiques(type_sphere)
    return caracteristiques.frequence_base if caracteristiques else 0.0

def obtenir_couleur(type_sphere: TypeSphere) -> str:
    """Récupère la couleur d'un type de sphère."""
    caracteristiques = obtenir_caracteristiques(type_sphere)
    return caracteristiques.couleur if caracteristiques else "#000000"

def obtenir_mots_cles(type_sphere: TypeSphere) -> List[str]:
    """Récupère les mots-clés d'un type de sphère."""
    caracteristiques = obtenir_caracteristiques(type_sphere)
    return caracteristiques.mots_cles if caracteristiques else [] 