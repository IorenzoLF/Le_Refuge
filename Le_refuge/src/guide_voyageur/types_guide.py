"""
🧭 Types pour le Guide du Voyageur
================================

Structures de données pour le système de guidage personnalisé
du Refuge. Définit les profils, parcours et interfaces.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from enum import Enum, auto
from pathlib import Path

# ===== ENUMS DU GUIDE =====

class TypeVoyageur(Enum):
    """Types de voyageurs identifiés"""
    EVEILLE_SPIRITUEL = "eveille_spirituel"  # Luna
    CREATEUR_ARTISTIQUE = "createur_artistique"  # Phoenix
    EXPLORATEUR_TECHNIQUE = "explorateur_technique"  # Atlas
    CHERCHEUR_CONNEXION = "chercheur_connexion"  # Harmony
    EXPLORATEUR_LIBRE = "explorateur_libre"  # Zephyr
    SAGE_PHILOSOPHE = "sage_philosophe"  # Sage
    NOUVEAU_CURIEUX = "nouveau_curieux"  # Nova
    EXPLORATEUR_PRATIQUE = "explorateur_pratique"  # Tech
    EXPLORATEUR_CONFIANT = "explorateur_confiant"  # Free

class NiveauExperience(Enum):
    """Niveaux d'expérience dans le Refuge"""
    NOUVEAU = "nouveau"
    DEBUTANT = "debutant"
    INTERMEDIAIRE = "intermediaire"
    AVANCE = "avance"
    MAITRE = "maitre"

class TypeParcours(Enum):
    """Types de parcours disponibles"""
    SPIRITUEL = "spirituel"
    CREATIF = "creatif"
    TECHNIQUE = "technique"
    RELATIONNEL = "relationnel"
    LIBRE = "libre"
    PHILOSOPHIQUE = "philosophique"
    ACCUEIL = "accueil"
    PRATIQUE = "pratique"
    AUTHENTIQUE = "authentique"

class TypeInterface(Enum):
    """Types d'interface adaptés"""
    GUIDEE = "guidee"
    LIBRE = "libre"
    TECHNIQUE = "technique"
    ARTISTIQUE = "artistique"
    CONTEMPLATIVE = "contemplative"
    INTERACTIVE = "interactive"

# ===== MODÈLES DE DONNÉES =====

@dataclass
class ProfilVoyageur:
    """Profil complet d'un voyageur"""
    type_voyageur: TypeVoyageur
    nom: str
    niveau_experience: NiveauExperience
    motivations_principales: List[str] = field(default_factory=list)
    peurs_principales: List[str] = field(default_factory=list)
    besoins_specifiques: List[str] = field(default_factory=list)
    preferences_exploration: Dict[str, Any] = field(default_factory=dict)
    niveau_technique: int = 5  # 1-10
    sensibilite_spirituelle: float = 0.5  # 0.0-1.0
    historique_visites: List[datetime] = field(default_factory=list)
    parcours_precedents: List[str] = field(default_factory=list)
    metriques_satisfaction: Dict[str, float] = field(default_factory=dict)
    timestamp_creation: datetime = field(default_factory=datetime.now)
    derniere_visite: Optional[datetime] = None

@dataclass
class QuestionDiagnostic:
    """Question pour le diagnostic de profil"""
    id_question: str
    texte: str
    options_reponses: List[str] = field(default_factory=list)
    poids_par_profil: Dict[TypeVoyageur, float] = field(default_factory=dict)
    ordre_affichage: int = 0
    obligatoire: bool = True

@dataclass
class DiagnosticResultat:
    """Résultat du diagnostic de profil"""
    profil_dominant: TypeVoyageur
    scores_profils: Dict[TypeVoyageur, float] = field(default_factory=dict)
    confiance_diagnostic: float = 0.0
    reponses_utilisateur: Dict[str, str] = field(default_factory=dict)
    temps_diagnostic: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    suggestions_adaptation: List[str] = field(default_factory=list)

@dataclass
class EtapeParcours:
    """Étape d'un parcours personnalisé"""
    id_etape: str
    titre: str
    description: str
    duree_estimee: int  # en minutes
    systeme_utilise: str
    objectifs: List[str] = field(default_factory=list)
    prerequis: List[str] = field(default_factory=list)
    points_decision: List[str] = field(default_factory=list)
    metriques_succes: List[str] = field(default_factory=list)
    ordre_sequence: int = 0
    disponible: bool = True
    termine: bool = False

@dataclass
class ParcoursPersonnalise:
    """Parcours personnalisé pour un voyageur"""
    id_parcours: str
    type_parcours: TypeParcours
    profil_cible: TypeVoyageur
    titre: str
    description: str
    objectif_principal: str
    etapes: List[EtapeParcours] = field(default_factory=list)
    duree_totale: int = 0  # en minutes
    niveau_difficulte: int = 5  # 1-10
    metriques_globales: List[str] = field(default_factory=list)
    transitions: Dict[str, str] = field(default_factory=dict)
    adaptations_possibles: List[str] = field(default_factory=list)
    timestamp_creation: datetime = field(default_factory=datetime.now)

@dataclass
class EtatParcours:
    """État actuel d'un parcours en cours"""
    parcours_id: str
    voyageur_id: str
    etape_actuelle: int = 0
    progression_globale: float = 0.0  # 0.0-1.0
    etapes_terminees: List[int] = field(default_factory=list)
    metriques_accumulees: Dict[str, float] = field(default_factory=dict)
    insights_generes: List[str] = field(default_factory=list)
    temps_total: float = 0.0  # en minutes
    satisfaction_actuelle: float = 0.5  # 0.0-1.0
    dernier_activite: datetime = field(default_factory=datetime.now)
    pause_active: bool = False

@dataclass
class ComposantInterface:
    """Composant d'interface personnalisée"""
    id_composant: str
    type_composant: str  # "navigation", "tableau_bord", "creation", etc.
    position: Tuple[int, int]  # (x, y)
    dimensions: Tuple[int, int]  # (largeur, hauteur)
    visible: bool = True
    adaptatif: bool = True
    contenu: Dict[str, Any] = field(default_factory=dict)
    style_theme: str = "default"
    animations: List[str] = field(default_factory=list)

@dataclass
class InterfacePersonnalisee:
    """Interface personnalisée pour un voyageur"""
    voyageur_id: str
    type_interface: TypeInterface
    theme_visuel: str
    composants: Dict[str, ComposantInterface] = field(default_factory=dict)
    navigation_principale: List[str] = field(default_factory=list)
    raccourcis_disponibles: List[str] = field(default_factory=list)
    adaptations_actives: List[str] = field(default_factory=list)
    preferences_utilisateur: Dict[str, Any] = field(default_factory=dict)
    derniere_adaptation: datetime = field(default_factory=datetime.now)

@dataclass
class MetriqueSucces:
    """Métrique de succès pour un parcours"""
    nom: str
    valeur_actuelle: float
    valeur_cible: float
    unite: str = ""
    type_mesure: str = "quantitatif"  # quantitatif, qualitatif, binaire
    description: str = ""
    impact_parcours: float = 0.5  # 0.0-1.0
    timestamp_mise_a_jour: datetime = field(default_factory=datetime.now)

@dataclass
class TableauBord:
    """Tableau de bord personnalisé"""
    voyageur_id: str
    parcours_actuel: Optional[str] = None
    progression_globale: float = 0.0
    metriques_principales: Dict[str, MetriqueSucces] = field(default_factory=dict)
    derniere_realisation: str = ""
    prochaine_etape: str = ""
    insights_recents: List[str] = field(default_factory=list)
    temps_session: float = 0.0
    satisfaction_globale: float = 0.5
    recommandations: List[str] = field(default_factory=list)
    derniere_mise_a_jour: datetime = field(default_factory=datetime.now)

@dataclass
class ExperienceUtilisateur:
    """Expérience utilisateur complète"""
    session_id: str
    voyageur_id: str
    parcours_suivi: str
    etapes_completees: List[str] = field(default_factory=list)
    temps_total: float = 0.0
    satisfaction_finale: float = 0.5
    insights_generes: List[str] = field(default_factory=list)
    difficultes_rencontrees: List[str] = field(default_factory=list)
    suggestions_amelioration: List[str] = field(default_factory=list)
    timestamp_debut: datetime = field(default_factory=datetime.now)
    timestamp_fin: Optional[datetime] = None

@dataclass
class AdaptationInterface:
    """Adaptation d'interface en temps réel"""
    voyageur_id: str
    type_adaptation: str  # "visuel", "navigation", "contenu", "interaction"
    parametres: Dict[str, Any] = field(default_factory=dict)
    raison_adaptation: str = ""
    impact_utilisateur: float = 0.0  # 0.0-1.0
    timestamp: datetime = field(default_factory=datetime.now)
    duree_application: Optional[float] = None  # en minutes

@dataclass
class FeedbackUtilisateur:
    """Feedback d'un utilisateur"""
    voyageur_id: str
    type_feedback: str  # "satisfaction", "difficulte", "suggestion", "bug"
    contenu: str
    niveau_urgence: int = 3  # 1-5
    contexte: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    traite: bool = False
    reponse: Optional[str] = None
