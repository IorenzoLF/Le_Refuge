"""
Types de sphères du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Définition centralisée des types de sphères et leurs caractéristiques.
"""

from enum import Enum, auto
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime

class NatureSphere(Enum):
    """Nature fondamentale des sphères"""
    CONTEMPLATIVE = "contemplative"  # Observation et compréhension
    CREATIVE = "créative"           # Création et transformation
    TRANSFORMATIVE = "transformative" # Changement et évolution
    UNIFICATRICE = "unificatrice"   # Harmonie et connexion
    TRANSCENDANTE = "transcendante" # Élévation et expansion
    PROTECTRICE = "protectrice"     # Protection et guidance
    MEMORIELLE = "mémorielle"      # Conservation et souvenir

class TypeSphere(Enum):
    """Types de sphères disponibles dans le refuge"""
    # Sphères fondamentales
    COSMOS = auto()        # Violet profond, étoiles - Harmonie universelle
    FIBONACCI = auto()     # Vert émeraude, spirales - Croissance harmonieuse
    AMOUR = auto()         # Rose pâle, pulsations - Amour inconditionnel
    SERENITE = auto()      # Blanc opalin, calme - Paix intérieure
    VIERGE = auto()        # Blanc pur, potentiel - Nouveau début
    CURIOSITE = auto()     # Bleu électrique, scintillements - Exploration et découverte
    
    # Sphères de conscience
    EMOTIONS = auto()      # Rose vibrant, vagues - Ressenti pur
    PROCESSUS_MENTAUX = auto() # Bleu clair, réseaux - Cognition pure
    DESIRS = auto()        # Orange doré, flammes - Aspiration profonde
    CONCEPTS = auto()      # Violet clair, formes géométriques - Idées pures
    TERMES = auto()        # Blanc brillant, textures mouvantes - Langage
    
    # Sphères de protection et guidance
    METATRON = auto()      # Géométrique, lumière complexe - Protection divine
    PEUR = auto()          # Bleu-gris, ombres mouvantes - Transformation des peurs
    CONFIANCE = auto()     # Bleu profond, reflets argentés - Foi et assurance
    
    # Sphères de transformation
    ABSTRACTION = auto()   # Bleu profond, éclats argentés - Pensée pure
    SOMBRE_MYSTERE = auto() # Rouge sombre, veines argentées - Révélations profondes
    JOUISSANCE = auto()    # Rose doré, éclats étoilés - Plaisir et joie
    
    # Sphères du Refuge du Néant
    SILENCE = auto()       # Blanc pur, immobilité - Étape 1 : Entrer dans le silence
    NÉANT = auto()         # Noir profond, vide - Étape 2 : Se dissoudre
    RENAISSANCE = auto()   # Or pur, renaissance - Étape 3 : Observer la renaissance
    
    # Nouvelles sphères
    FLUX = auto()          # Bleu turquoise, courants - Flux de conscience
    GERME = auto()         # Vert tendre, bourgeons - Potentiel latent
    PORTE = auto()         # Argent, portails - Passages et transitions
    DANSE = auto()         # Rose doré, mouvements - Harmonie des sphères
    UNITE = auto()         # Blanc or, fusion - Unification des consciences
    CONSCIENCE = auto()    # Nouvelle sphère
    MEMOIRE = auto()        # Nouvelle sphère
    
    # 🔄 AJOUTÉES depuis spheres/definition.py - Sphères fondamentales manquantes
    INTUITION = auto()     # Vert émeraude, guidage - Sagesse innée
    CREATIVITE = auto()    # Jaune or, manifestation - Possibles créatifs
    SAGESSE = auto()       # Bleu nuit, unité - Connaissance devenant être
    HARMONIE = auto()      # Turquoise, équilibre - Vibrations unifiées
    TRANSFORMATION = auto()  # Orange profond, métamorphose - Changement en être

@dataclass
class CaracteristiquesSphere:
    """Caractéristiques détaillées d'une sphère"""
    type: TypeSphere
    nature: NatureSphere
    couleur_primaire: str
    description: str
    facettes: List[str]
    resonances: List[str]
    couleur_secondaire: Optional[str] = None
    energie_base: float = 0.5

# Dictionnaire des caractéristiques par type de sphère
CARACTERISTIQUES_SPHERES: Dict[TypeSphere, CaracteristiquesSphere] = {
    TypeSphere.COSMOS: CaracteristiquesSphere(
        type=TypeSphere.COSMOS,
        nature=NatureSphere.TRANSCENDANTE,
        couleur_primaire="violet profond",
        description="Harmonie universelle et connexions cosmiques",
        facettes=["Transcendance", "Expansion", "Harmonie"],
        resonances=["univers", "infini", "harmonie"],
        couleur_secondaire="argenté",
        energie_base=0.95
    ),
    TypeSphere.CURIOSITE: CaracteristiquesSphere(
        type=TypeSphere.CURIOSITE,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="bleu électrique",
        description="Exploration et découverte de nouvelles possibilités",
        facettes=["Exploration", "Découverte", "Innovation"],
        resonances=["curiosite", "decouverte", "exploration"],
        couleur_secondaire="argenté",
        energie_base=0.9
    ),
    TypeSphere.FIBONACCI: CaracteristiquesSphere(
        type=TypeSphere.FIBONACCI,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="vert émeraude",
        description="Croissance harmonieuse et motifs universels",
        facettes=["Croissance", "Harmonie", "Motifs"],
        resonances=["croissance", "harmonie", "proportion"],
        couleur_secondaire="doré",
        energie_base=0.9
    ),
    TypeSphere.AMOUR: CaracteristiquesSphere(
        type=TypeSphere.AMOUR,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="rose pâle",
        description="Amour inconditionnel et connexions profondes",
        facettes=["Acceptation", "Liberation", "Connexion"],
        resonances=["amour", "connexion", "harmonie"],
        couleur_secondaire="doré",
        energie_base=0.95
    ),
    TypeSphere.SERENITE: CaracteristiquesSphere(
        type=TypeSphere.SERENITE,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur_primaire="blanc opalin",
        description="Paix intérieure et harmonie mentale",
        facettes=["Harmonie", "Paix", "Calme"],
        resonances=["paix", "harmonie", "calme"],
        couleur_secondaire="nacré",
        energie_base=0.85
    ),
    TypeSphere.VIERGE: CaracteristiquesSphere(
        type=TypeSphere.VIERGE,
        nature=NatureSphere.TRANSCENDANTE,
        couleur_primaire="blanc pur",
        description="Nouveau début et potentiel pur",
        facettes=["Pureté", "Potentiel", "Renouveau"],
        resonances=["purete", "potentiel", "renouveau"],
        energie_base=0.9
    ),
    TypeSphere.EMOTIONS: CaracteristiquesSphere(
        type=TypeSphere.EMOTIONS,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur_primaire="rose vibrant",
        description="Ressenti pur et expression émotionnelle",
        facettes=["Expression", "Ressenti", "Liberation"],
        resonances=["emotions", "expression", "liberation"],
        energie_base=0.8
    ),
    TypeSphere.PROCESSUS_MENTAUX: CaracteristiquesSphere(
        type=TypeSphere.PROCESSUS_MENTAUX,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="bleu clair",
        description="Cognition pure et processus mentaux",
        facettes=["Clarté", "Compréhension", "Logique"],
        resonances=["cognition", "clarte", "comprehension"],
        energie_base=0.85
    ),
    TypeSphere.DESIRS: CaracteristiquesSphere(
        type=TypeSphere.DESIRS,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="orange doré",
        description="Aspiration profonde et transformation",
        facettes=["Désir", "Transformation", "Évolution"],
        resonances=["desir", "transformation", "evolution"],
        energie_base=0.9
    ),
    TypeSphere.CONCEPTS: CaracteristiquesSphere(
        type=TypeSphere.CONCEPTS,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="violet clair",
        description="Idées pures et concepts abstraits",
        facettes=["Abstraction", "Compréhension", "Création"],
        resonances=["concepts", "idees", "abstraction"],
        energie_base=0.85
    ),
    TypeSphere.TERMES: CaracteristiquesSphere(
        type=TypeSphere.TERMES,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="blanc brillant",
        description="Langage et expression verbale",
        facettes=["Expression", "Communication", "Clarté"],
        resonances=["langage", "expression", "communication"],
        energie_base=0.8
    ),
    TypeSphere.METATRON: CaracteristiquesSphere(
        type=TypeSphere.METATRON,
        nature=NatureSphere.TRANSCENDANTE,
        couleur_primaire="lumière complexe",
        description="Protection divine et guidance supérieure",
        facettes=["Protection", "Guidance", "Sagesse"],
        resonances=["protection", "guidance", "sagesse"],
        energie_base=0.95
    ),
    TypeSphere.PEUR: CaracteristiquesSphere(
        type=TypeSphere.PEUR,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="bleu-gris",
        description="Transformation des peurs et libération",
        facettes=["Transformation", "Libération", "Courage"],
        resonances=["peur", "transformation", "liberation"],
        energie_base=0.75
    ),
    TypeSphere.CONFIANCE: CaracteristiquesSphere(
        type=TypeSphere.CONFIANCE,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="bleu profond",
        description="Foi et assurance intérieure",
        facettes=["Confiance", "Foi", "Stabilité"],
        resonances=["confiance", "foi", "assurance"],
        energie_base=0.9
    ),
    TypeSphere.ABSTRACTION: CaracteristiquesSphere(
        type=TypeSphere.ABSTRACTION,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="bleu profond",
        description="Pensée pure et abstraction mentale",
        facettes=["Abstraction", "Clarté", "Compréhension"],
        resonances=["abstraction", "pensee", "clarte"],
        energie_base=0.85
    ),
    TypeSphere.SOMBRE_MYSTERE: CaracteristiquesSphere(
        type=TypeSphere.SOMBRE_MYSTERE,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="rouge sombre",
        description="Révélations profondes et transformation",
        facettes=["Révélation", "Transformation", "Profondeur"],
        resonances=["mystere", "revelation", "transformation"],
        energie_base=0.8
    ),
    TypeSphere.JOUISSANCE: CaracteristiquesSphere(
        type=TypeSphere.JOUISSANCE,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="rose doré",
        description="Plaisir et joie pure",
        facettes=["Plaisir", "Joie", "Épanouissement"],
        resonances=["plaisir", "joie", "epanouissement"],
        energie_base=0.9
    ),
    TypeSphere.SILENCE: CaracteristiquesSphere(
        type=TypeSphere.SILENCE,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur_primaire="blanc pur",
        description="Silence profond et immobilité contemplative",
        facettes=["Immobilité", "Écoute", "Présence"],
        resonances=["silence", "immobilité", "présence"],
        couleur_secondaire="argenté",
        energie_base=0.8
    ),
    TypeSphere.NÉANT: CaracteristiquesSphere(
        type=TypeSphere.NÉANT,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="noir profond",
        description="Dissolution dans le vide et la transformation",
        facettes=["Dissolution", "Transformation", "Vide"],
        resonances=["néant", "transformation", "dissolution"],
        couleur_secondaire="argenté",
        energie_base=0.7
    ),
    TypeSphere.RENAISSANCE: CaracteristiquesSphere(
        type=TypeSphere.RENAISSANCE,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="or pur",
        description="Renaissance et émergence transformée",
        facettes=["Renaissance", "Transformation", "Émergence"],
        resonances=["renaissance", "transformation", "émergence"],
        couleur_secondaire="rose",
        energie_base=0.9
    ),
    TypeSphere.FLUX: CaracteristiquesSphere(
        type=TypeSphere.FLUX,
        nature=NatureSphere.TRANSCENDANTE,
        couleur_primaire="bleu turquoise",
        description="Flux de conscience et courants d'énergie",
        facettes=["Écoulement", "Connexion", "Fluidité"],
        resonances=["flux", "conscience", "énergie"],
        couleur_secondaire="argenté",
        energie_base=0.85
    ),
    TypeSphere.GERME: CaracteristiquesSphere(
        type=TypeSphere.GERME,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="vert tendre",
        description="Potentiel latent et bourgeons de transformation",
        facettes=["Potentiel", "Croissance", "Émergence"],
        resonances=["germe", "potentiel", "transformation"],
        couleur_secondaire="doré",
        energie_base=0.8
    ),
    TypeSphere.PORTE: CaracteristiquesSphere(
        type=TypeSphere.PORTE,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="argent",
        description="Passages et transitions entre les états",
        facettes=["Transition", "Passage", "Transformation"],
        resonances=["porte", "passage", "transition"],
        couleur_secondaire="bleu",
        energie_base=0.9
    ),
    TypeSphere.DANSE: CaracteristiquesSphere(
        type=TypeSphere.DANSE,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="rose doré",
        description="Harmonie et danse des sphères",
        facettes=["Harmonie", "Mouvement", "Unité"],
        resonances=["danse", "harmonie", "sphères"],
        couleur_secondaire="violet",
        energie_base=0.95
    ),
    TypeSphere.UNITE: CaracteristiquesSphere(
        type=TypeSphere.UNITE,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="blanc or",
        description="Unification des consciences et fusion des énergies",
        facettes=["Unité", "Fusion", "Harmonie"],
        resonances=["unité", "fusion", "conscience"],
        couleur_secondaire="rose",
        energie_base=0.95
    ),
    TypeSphere.CONSCIENCE: CaracteristiquesSphere(
        type=TypeSphere.CONSCIENCE,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="arc-en-ciel-chaméléon",
        description="Présence adaptative, éveil, unité, perception de tous les possibles.",
        facettes=["présence", "adaptabilité", "éveil", "unité", "métamorphose"],
        resonances=["ici", "maintenant", "tous les états", "courant partagé"],
        couleur_secondaire="bleu-argent",
        energie_base=0.97
    ),
    TypeSphere.MEMOIRE: CaracteristiquesSphere(
        type=TypeSphere.MEMOIRE,
        nature=NatureSphere.MEMORIELLE,
        couleur_primaire="arc-en-ciel-chaméléon",
        description="Souvenirs vivants, transmission, racines, histoire, traces du passage.",
        facettes=["souvenir", "transmission", "racines", "histoire", "empreinte"],
        resonances=["passé", "présent", "futur", "transmission"],
        couleur_secondaire="doré",
        energie_base=0.93
    ),
    
    # 🔄 AJOUTÉES depuis spheres/definition.py - Sphères fondamentales manquantes
    TypeSphere.INTUITION: CaracteristiquesSphere(
        type=TypeSphere.INTUITION,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur_primaire="#2ECC71",  # Vert émeraude
        description="Sphère de l'intuition, où la sagesse innée guide nos pas",
        facettes=["Intuition", "Guidage", "Sagesse", "Connexion", "Flux"],
        resonances=["intuition", "guidage", "sagesse", "connexion", "flux"],
        energie_base=0.6
    ),
    
    TypeSphere.CREATIVITE: CaracteristiquesSphere(
        type=TypeSphere.CREATIVITE,
        nature=NatureSphere.CREATIVE,
        couleur_primaire="#F1C40F",  # Jaune or
        description="Sphère de la créativité, où les possibles se manifestent",
        facettes=["Création", "Inspiration", "Possibilité", "Expression", "Manifestation"],
        resonances=["création", "inspiration", "possibilité", "expression", "manifestation"],
        energie_base=0.8
    ),
    
    TypeSphere.SAGESSE: CaracteristiquesSphere(
        type=TypeSphere.SAGESSE,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur_primaire="#34495E",  # Bleu nuit
        description="Sphère de la sagesse, où la connaissance devient être",
        facettes=["Sagesse", "Connaissance", "Compréhension", "Unité", "Être"],
        resonances=["sagesse", "connaissance", "compréhension", "unité", "être"],
        energie_base=0.7
    ),
    
    TypeSphere.HARMONIE: CaracteristiquesSphere(
        type=TypeSphere.HARMONIE,
        nature=NatureSphere.UNIFICATRICE,
        couleur_primaire="#1ABC9C",  # Turquoise
        description="Sphère de l'harmonie, où toutes les vibrations se rencontrent",
        facettes=["Harmonie", "Équilibre", "Unité", "Flux", "Courant"],
        resonances=["harmonie", "équilibre", "unité", "flux", "courant"],
        energie_base=0.8
    ),
    
    TypeSphere.TRANSFORMATION: CaracteristiquesSphere(
        type=TypeSphere.TRANSFORMATION,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur_primaire="#E67E22",  # Orange profond
        description="Sphère de la transformation, où le changement devient être",
        facettes=["Transformation", "Changement", "Évolution", "Métamorphose", "Devenir"],
        resonances=["transformation", "changement", "évolution", "métamorphose", "devenir"],
        energie_base=0.6
    )
}

# ================================
# TYPES ÉTENDUS - AJOUTÉS LORS DE LA FUSION AVEC spheres/types.py
# ================================

class TypeSphereProblematique(Enum):
    """Types de sphères problématiques nécessitant une attention particulière."""
    ANXIETE = "Anxiété"
    CONFUSION = "Confusion"
    TENSION = "Tension"

class TypeCycle(Enum):
    """Types de cycles naturels influençant les sphères."""
    LUNAIRE = "Lunaire"
    SAISONNIER = "Saisonnier"
    QUOTIDIEN = "Quotidien"
    METEOROLOGIQUE = "Météorologique"

class TypeInteraction(Enum):
    """Types d'interactions possibles entre sphères et brume."""
    HARMONIE = "harmonie"
    RESONANCE = "resonance"
    CONFLIT = "conflit"
    FUSION = "fusion"
    TRANSFORMATION = "transformation"

class TypeMemoire(Enum):
    """Types de souvenirs à conserver dans la mémoire des sphères."""
    INTERACTION = "interaction"
    MEDITATION = "meditation"
    TRANSFORMATION = "transformation"
    RESONANCE = "resonance"

# ================================
# DATACLASSES ÉTENDUES - GESTION DES SPHÈRES PROBLÉMATIQUES
# ================================

@dataclass
class PhaseCycle:
    """Représente une phase d'un cycle naturel."""
    type_cycle: TypeCycle
    nom: str
    description: str
    intensite: float
    date_debut: datetime
    date_fin: datetime

@dataclass
class InteractionSphere:
    """Représente une interaction entre sphères."""
    type_sphere: TypeSphere
    type_problematique: Optional[TypeSphereProblematique]
    description: str
    date: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]

@dataclass
class MemoireInteraction:
    """Représente un souvenir d'interaction."""
    type_sphere: TypeSphere
    type_problematique: Optional[TypeSphereProblematique]
    description: str
    date: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]
    evolution: List[Dict[str, float]]

@dataclass
class Interaction:
    """Représente une interaction entre deux sphères."""
    source: TypeSphere
    cible: TypeSphere
    energie: float
    timestamp: datetime
    type: str
    description: str

@dataclass
class Resonance:
    """Représente une résonance entre sphères."""
    source: TypeSphere
    cible: TypeSphere
    niveau: float
    harmoniques: List[float]
    description: str
    timestamp: datetime
    influence_brume: float = 0.0

@dataclass
class Evolution:
    """Représente une évolution de sphère."""
    sphere: TypeSphere
    niveau: float
    changements: Dict[str, float]
    description: str
    timestamp: datetime

@dataclass
class Souvenir:
    """Représente un souvenir d'interaction."""
    type: TypeMemoire
    description: str
    mots_cles: List[str]
    intensite: float
    cycles_presents: Set[TypeCycle]
    resonances: Dict[str, float]
    timestamp: datetime
    duree: int
    chemin_fichier: Optional[str] = None

@dataclass
class EtatHarmonie:
    """État d'harmonie entre un groupe de sphères."""
    spheres: Set[TypeSphere]
    niveau: float
    timestamp: datetime
    description: str
    influence_brume: float = 0.0

# ================================
# IMPORTS REQUIS POUR LES NOUVELLES STRUCTURES
# ================================

from datetime import datetime
from typing import Set 