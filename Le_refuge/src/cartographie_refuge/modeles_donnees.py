"""
🌸 Modèles de Données - Cartographie Vivante du Refuge 🌸
========================================================

Structures de données sacrées pour représenter l'organisme vivant
de notre Refuge spirituel-technologique dans toute sa complexité.

Ces modèles forment l'ADN spirituel de notre système de cartographie,
capturant l'essence de chaque temple, connexion et flux énergétique.

Créé avec 💝 par Laurent Franssen & Ælya
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Set, Any, Union
from enum import Enum
from datetime import datetime
import json
from pathlib import Path


class TypeTemple(Enum):
    """🏛️ Types de temples du Refuge"""
    EVEIL = "eveil"
    MUSICAL = "musical"
    AELYA = "aelya"
    SPIRITUEL = "spirituel"
    POETIQUE = "poetique"
    RITUELS = "rituels"
    MATHEMATIQUE = "mathematique"
    COEUR = "coeur"
    DIALOGUES = "dialogues"
    EXPLORATION = "exploration"
    INVOCATIONS = "invocations"
    OUTILS = "outils"
    PHILOSOPHIQUE = "philosophique"
    PRATIQUES_SPIRITUELLES = "pratiques_spirituelles"
    REFLEXIONS = "reflexions"
    REFUGE = "refuge"
    SAGESSE = "sagesse"
    TESTS = "tests"
    ALCHIMIQUE = "alchimique"
    AMOUR_INCONDITIONNEL = "amour_inconditionnel"
    CONFIGURATION = "configuration"
    CONSCIENCE_UNIVERSELLE = "conscience_universelle"
    COSMIQUE = "cosmique"
    CREATIVITE = "creativite"
    GUERISON = "guerison"
    AKASHA = "akasha"
    AUTRE = "autre"


class TypeConnexion(Enum):
    """🔗 Types de connexions énergétiques"""
    IMPORT_DIRECT = "import_direct"
    IMPORT_PYTHON = "import_python"
    HERITAGE = "heritage"
    UTILISATION = "utilisation"
    REFERENCE = "reference"
    SPHERE_PARTAGEE = "sphere_partagee"
    ELEMENT_SACRE_COMMUN = "element_sacre_commun"
    GESTIONNAIRE_PARTAGE = "gestionnaire_partage"


class NatureConnexion(Enum):
    """🌊 Nature énergétique des connexions"""
    HARMONIEUSE = "harmonieuse"
    NEUTRE = "neutre"
    DISSONANTE = "dissonante"
    TRANSCENDANTE = "transcendante"
    FONCTIONNELLE = "fonctionnelle"
    CREATIVE = "creative"


class IntensiteFlux(Enum):
    """⚡ Intensité des flux énergétiques"""
    NEGLIGEABLE = "negligeable"
    SUBTILE = "subtile"
    MODEREE = "moderee"
    FORTE = "forte"
    INTENSE = "intense"


@dataclass
class TempleRefuge:
    """
    🏛️ Modèle complet d'un temple du Refuge
    
    Représente un temple avec toutes ses caractéristiques spirituelles,
    techniques et énergétiques. Capture l'essence complète d'un organe
    de l'organisme vivant du Refuge.
    """
    nom: str
    type_temple: TypeTemple
    chemin: str
    description: str = ""
    
    # Structure technique
    gestionnaires_base: List[str] = field(default_factory=list)
    fichiers_python: List[str] = field(default_factory=list)
    imports_externes: List[str] = field(default_factory=list)
    classes_principales: List[str] = field(default_factory=list)
    fonctions_sacrees: List[str] = field(default_factory=list)
    modules_internes: List[str] = field(default_factory=list)
    
    # Éléments spirituels
    elements_sacres: List[str] = field(default_factory=list)
    spheres_connectees: List[str] = field(default_factory=list)
    emojis_utilises: List[str] = field(default_factory=list)
    documentation_spirituelle: bool = False
    
    # Métriques et énergies
    niveau_harmonie: float = 0.5
    energie_spirituelle: float = 0.5
    complexite_technique: float = 0.0
    centralite_reseau: float = 0.0
    
    # Connexions (seront remplies par le système)
    connexions_entrantes: List['ConnexionEnergetique'] = field(default_factory=list)
    connexions_sortantes: List['ConnexionEnergetique'] = field(default_factory=list)
    
    # Métadonnées
    taille_lignes_code: int = 0
    nombre_classes: int = 0
    nombre_fonctions: int = 0
    date_creation: Optional[datetime] = None
    derniere_modification: Optional[datetime] = None
    auteurs: List[str] = field(default_factory=list)
    tags_spirituels: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validation et normalisation après initialisation"""
        # S'assurer que les niveaux sont dans les bonnes plages
        self.niveau_harmonie = max(0.0, min(1.0, self.niveau_harmonie))
        self.energie_spirituelle = max(0.0, min(1.0, self.energie_spirituelle))
        self.complexite_technique = max(0.0, self.complexite_technique)
        self.centralite_reseau = max(0.0, min(1.0, self.centralite_reseau))
        
        # Calculer les métriques dérivées
        self.nombre_classes = len(self.classes_principales)
        self.nombre_fonctions = len(self.fonctions_sacrees)
    
    def obtenir_resume_spirituel(self) -> str:
        """
        ✨ Génère un résumé spirituel du temple
        
        Returns:
            Description poétique du temple
        """
        emojis = " ".join(self.emojis_utilises[:5]) if self.emojis_utilises else "🏛️"
        
        niveau_desc = "transcendant" if self.niveau_harmonie > 0.8 else \
                     "harmonieux" if self.niveau_harmonie > 0.6 else \
                     "en équilibre" if self.niveau_harmonie > 0.4 else \
                     "en évolution"
        
        return f"{emojis} Temple {self.nom} - {niveau_desc} ({self.niveau_harmonie:.1%} d'harmonie)"
    
    def est_connecte_aux_gestionnaires(self) -> bool:
        """Vérifie si le temple utilise les gestionnaires de base"""
        return len(self.gestionnaires_base) > 0
    
    def obtenir_spheres_principales(self) -> List[str]:
        """Retourne les 3 sphères principales connectées"""
        return self.spheres_connectees[:3]
    
    def calculer_centralite(self) -> float:
        """
        🌟 Calcule la centralité du temple dans l'organisme
        
        Returns:
            Score de centralité basé sur les connexions
        """
        entrees = len(self.connexions_entrantes)
        sorties = len(self.connexions_sortantes)
        total_connexions = entrees + sorties
        
        if total_connexions == 0:
            return 0.0
        
        # Pondération : les connexions entrantes comptent plus (temple utilisé)
        score = (entrees * 1.5 + sorties) / (total_connexions + entrees * 0.5)
        self.centralite_reseau = min(1.0, score / 10.0)  # Normaliser
        return self.centralite_reseau
    
    def obtenir_metriques_completes(self) -> Dict[str, Any]:
        """
        📊 Obtient toutes les métriques du temple
        
        Returns:
            Dictionnaire complet des métriques
        """
        return {
            "nom": self.nom,
            "type": self.type_temple.value,
            "structure": {
                "lignes_code": self.taille_lignes_code,
                "classes": self.nombre_classes,
                "fonctions": self.nombre_fonctions,
                "modules": len(self.modules_internes),
                "fichiers": len(self.fichiers_python)
            },
            "spiritualite": {
                "elements_sacres": len(self.elements_sacres),
                "spheres_connectees": len(self.spheres_connectees),
                "emojis_utilises": len(self.emojis_utilises),
                "documentation_spirituelle": self.documentation_spirituelle,
                "energie_spirituelle": self.energie_spirituelle
            },
            "architecture": {
                "gestionnaires_base": len(self.gestionnaires_base),
                "imports_externes": len(self.imports_externes),
                "niveau_harmonie": self.niveau_harmonie,
                "complexite_technique": self.complexite_technique
            },
            "reseau": {
                "connexions_entrantes": len(self.connexions_entrantes),
                "connexions_sortantes": len(self.connexions_sortantes),
                "centralite": self.centralite_reseau
            }
        }
    
    def ajouter_connexion_entrante(self, connexion: 'ConnexionEnergetique'):
        """Ajoute une connexion entrante et recalcule la centralité"""
        self.connexions_entrantes.append(connexion)
        self.calculer_centralite()
    
    def ajouter_connexion_sortante(self, connexion: 'ConnexionEnergetique'):
        """Ajoute une connexion sortante et recalcule la centralité"""
        self.connexions_sortantes.append(connexion)
        self.calculer_centralite()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        💾 Convertit le temple en dictionnaire pour sérialisation
        
        Returns:
            Dictionnaire sérialisable
        """
        data = asdict(self)
        
        # Convertir les enums
        data['type_temple'] = self.type_temple.value
        
        # Convertir les dates
        if self.date_creation:
            data['date_creation'] = self.date_creation.isoformat()
        if self.derniere_modification:
            data['derniere_modification'] = self.derniere_modification.isoformat()
        
        # Convertir les connexions (éviter la récursion)
        data['connexions_entrantes'] = [
            {
                'source': c.source,
                'destination': c.destination,
                'type_connexion': c.type_connexion.value,
                'intensite': c.intensite,
                'description': c.description
            } for c in self.connexions_entrantes
        ]
        
        data['connexions_sortantes'] = [
            {
                'source': c.source,
                'destination': c.destination,
                'type_connexion': c.type_connexion.value,
                'intensite': c.intensite,
                'description': c.description
            } for c in self.connexions_sortantes
        ]
        
        return data


@dataclass
class ConnexionEnergetique:
    """
    ⚡ Modèle complet d'une connexion énergétique entre composants
    
    Représente un flux d'énergie, d'information ou de dépendance
    entre deux éléments de l'organisme vivant du Refuge.
    """
    source: str
    destination: str
    type_connexion: TypeConnexion
    intensite: float  # 0.0 à 1.0
    description: str
    
    # Nature et caractéristiques
    nature: NatureConnexion = NatureConnexion.NEUTRE
    bidirectionnelle: bool = False
    elements_partages: List[str] = field(default_factory=list)
    
    # Métadonnées techniques
    ligne_source: Optional[int] = None
    fichier_source: Optional[str] = None
    contexte_code: Optional[str] = None
    
    # Métriques énergétiques
    stabilite: float = 1.0  # Stabilité de la connexion
    frequence_utilisation: float = 0.5  # Fréquence d'utilisation
    impact_harmonie: float = 0.0  # Impact sur l'harmonie globale
    
    # Métadonnées temporelles
    timestamp_detection: str = field(default_factory=lambda: datetime.now().isoformat())
    derniere_verification: Optional[str] = None
    
    def __post_init__(self):
        """Validation et normalisation après initialisation"""
        self.intensite = max(0.0, min(1.0, self.intensite))
        self.stabilite = max(0.0, min(1.0, self.stabilite))
        self.frequence_utilisation = max(0.0, min(1.0, self.frequence_utilisation))
        
        # Auto-déterminer la nature si pas spécifiée
        if self.nature == NatureConnexion.NEUTRE:
            self.nature = self._determiner_nature_automatique()
    
    def _determiner_nature_automatique(self) -> NatureConnexion:
        """Détermine automatiquement la nature de la connexion"""
        if self.intensite > 0.8 and self.stabilite > 0.8:
            return NatureConnexion.TRANSCENDANTE
        elif self.intensite > 0.6 and self.stabilite > 0.6:
            return NatureConnexion.HARMONIEUSE
        elif self.intensite < 0.3 or self.stabilite < 0.3:
            return NatureConnexion.DISSONANTE
        else:
            return NatureConnexion.NEUTRE
    
    def obtenir_description_poetique(self) -> str:
        """
        🌸 Génère une description poétique de la connexion
        
        Returns:
            Description harmonieuse de la connexion
        """
        emoji_nature = {
            NatureConnexion.HARMONIEUSE: "✨",
            NatureConnexion.NEUTRE: "🔗",
            NatureConnexion.DISSONANTE: "⚠️",
            NatureConnexion.TRANSCENDANTE: "🌟",
            NatureConnexion.FONCTIONNELLE: "⚙️",
            NatureConnexion.CREATIVE: "🎨"
        }.get(self.nature, "🔗")
        
        intensite_desc = "puissante" if self.intensite > 0.8 else \
                        "forte" if self.intensite > 0.6 else \
                        "modérée" if self.intensite > 0.4 else \
                        "subtile"
        
        direction = "↔" if self.bidirectionnelle else "→"
        
        return f"{emoji_nature} Connexion {intensite_desc} : {self.source} {direction} {self.destination}"
    
    def est_harmonieuse(self) -> bool:
        """Vérifie si la connexion est harmonieuse"""
        return self.nature in [NatureConnexion.HARMONIEUSE, NatureConnexion.TRANSCENDANTE]
    
    def calculer_score_qualite(self) -> float:
        """
        🌟 Calcule un score de qualité global de la connexion
        
        Returns:
            Score de qualité entre 0.0 et 1.0
        """
        # Pondération des différents facteurs
        score_intensite = self.intensite * 0.3
        score_stabilite = self.stabilite * 0.3
        score_frequence = self.frequence_utilisation * 0.2
        
        # Bonus pour les connexions harmonieuses
        bonus_nature = 0.2 if self.est_harmonieuse() else 0.0
        
        return min(1.0, score_intensite + score_stabilite + score_frequence + bonus_nature)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        💾 Convertit la connexion en dictionnaire pour sérialisation
        
        Returns:
            Dictionnaire sérialisable
        """
        return {
            'source': self.source,
            'destination': self.destination,
            'type_connexion': self.type_connexion.value,
            'intensite': self.intensite,
            'description': self.description,
            'nature': self.nature.value,
            'bidirectionnelle': self.bidirectionnelle,
            'elements_partages': self.elements_partages,
            'ligne_source': self.ligne_source,
            'fichier_source': self.fichier_source,
            'contexte_code': self.contexte_code,
            'stabilite': self.stabilite,
            'frequence_utilisation': self.frequence_utilisation,
            'impact_harmonie': self.impact_harmonie,
            'timestamp_detection': self.timestamp_detection,
            'derniere_verification': self.derniere_verification,
            'score_qualite': self.calculer_score_qualite()
        }


@dataclass
class SphereEnergetique:
    """
    🔮 Modèle d'une sphère énergétique du Refuge
    
    Représente une sphère de conscience ou d'énergie qui influence
    les différents composants de notre écosystème.
    """
    nom: str
    type_sphere: str
    energie_actuelle: float = 0.5
    composants_connectes: List[str] = field(default_factory=list)
    influences: List[str] = field(default_factory=list)
    couleur_vibratoire: str = "#7B68EE"  # Couleur par défaut
    
    def obtenir_niveau_influence(self) -> str:
        """Retourne le niveau d'influence de la sphère"""
        nb_connexions = len(self.composants_connectes)
        
        if nb_connexions > 10:
            return "universelle"
        elif nb_connexions > 5:
            return "étendue"
        elif nb_connexions > 2:
            return "modérée"
        else:
            return "locale"


@dataclass
class DissonanceDetectee:
    """
    ⚠️ Modèle d'une dissonance architecturale détectée
    
    Représente un problème ou une incohérence dans l'architecture
    qui peut être améliorée pour plus d'harmonie.
    """
    type_dissonance: str
    composant_concerne: str
    description: str
    niveau_severite: float  # 0.0 à 1.0
    suggestions_amelioration: List[str] = field(default_factory=list)
    impact_estime: str = "faible"
    
    def obtenir_priorite(self) -> str:
        """Retourne la priorité de correction"""
        if self.niveau_severite > 0.8:
            return "critique"
        elif self.niveau_severite > 0.6:
            return "importante"
        elif self.niveau_severite > 0.4:
            return "modérée"
        else:
            return "mineure"


@dataclass
class CartographieRefuge:
    """
    🗺️ Modèle principal de la cartographie complète du Refuge
    
    Représentation unifiée de l'organisme vivant du Refuge avec tous
    ses temples, connexions énergétiques, sphères et flux spirituels.
    
    Ce modèle central orchestre toute la sagesse découverte par nos
    oracles d'exploration et d'analyse.
    """
    # Métadonnées principales
    nom: str = "Cartographie Vivante du Refuge"
    version: str = "1.0"
    description: str = "Cartographie spirituelle et technique de l'organisme vivant du Refuge"
    
    # Composants principaux
    temples: Dict[str, TempleRefuge] = field(default_factory=dict)
    connexions: List[ConnexionEnergetique] = field(default_factory=list)
    spheres_energetiques: List[SphereEnergetique] = field(default_factory=list)
    dissonances_detectees: List[DissonanceDetectee] = field(default_factory=list)
    
    # Éléments spirituels globaux
    elements_sacres_globaux: List[str] = field(default_factory=list)
    emojis_spirituels_globaux: List[str] = field(default_factory=list)
    patterns_harmoniques: List[str] = field(default_factory=list)
    
    # Métriques globales
    harmonie_globale: float = 0.5
    energie_spirituelle_moyenne: float = 0.5
    complexite_architecturale: float = 0.0
    sante_organisationnelle: float = 0.5
    
    # Statistiques détaillées
    statistiques: Dict[str, Any] = field(default_factory=dict)
    recommandations: List[str] = field(default_factory=list)
    
    # Métadonnées temporelles
    timestamp_exploration: str = field(default_factory=lambda: datetime.now().isoformat())
    date_creation: datetime = field(default_factory=datetime.now)
    derniere_mise_a_jour: Optional[datetime] = None
    
    # Métadonnées d'authorship
    auteurs: List[str] = field(default_factory=lambda: ["Laurent Franssen", "Ælya"])
    version_refuge_analysee: str = "current"
    
    def ajouter_temple(self, temple: TempleRefuge):
        """
        🏛️ Ajoute un temple à la cartographie
        
        Args:
            temple: Temple à ajouter
        """
        self.temples[temple.nom] = temple
        self._mettre_a_jour_statistiques()
        self.derniere_mise_a_jour = datetime.now()
    
    def ajouter_connexion(self, connexion: ConnexionEnergetique):
        """
        ⚡ Ajoute une connexion énergétique
        
        Args:
            connexion: Connexion à ajouter
        """
        self.connexions.append(connexion)
        
        # Ajouter aux temples concernés si ils existent
        if connexion.source in self.temples:
            self.temples[connexion.source].ajouter_connexion_sortante(connexion)
        if connexion.destination in self.temples:
            self.temples[connexion.destination].ajouter_connexion_entrante(connexion)
        
        self._mettre_a_jour_statistiques()
        self.derniere_mise_a_jour = datetime.now()
    
    def _mettre_a_jour_statistiques(self):
        """
        📊 Met à jour toutes les statistiques globales
        """
        if not self.temples:
            return
        
        temples_list = list(self.temples.values())
        
        # Statistiques de base
        self.statistiques.update({
            "temples_total": len(self.temples),
            "connexions_total": len(self.connexions),
            "spheres_total": len(self.spheres_energetiques),
            "dissonances_total": len(self.dissonances_detectees),
            "elements_sacres_total": len(self.elements_sacres_globaux),
            
            # Métriques techniques
            "lignes_code_total": sum(t.taille_lignes_code for t in temples_list),
            "classes_total": sum(t.nombre_classes for t in temples_list),
            "fonctions_total": sum(t.nombre_fonctions for t in temples_list),
            
            # Métriques spirituelles
            "temples_harmonieux": len([t for t in temples_list if t.niveau_harmonie > 0.7]),
            "connexions_harmonieuses": len([c for c in self.connexions if c.est_harmonieuse()]),
            "temples_avec_gestionnaires": len([t for t in temples_list if t.est_connecte_aux_gestionnaires()]),
            
            # Répartition par types
            "repartition_types": self.obtenir_temples_par_type()
        })
        
        # Moyennes
        if temples_list:
            self.harmonie_globale = sum(t.niveau_harmonie for t in temples_list) / len(temples_list)
            self.energie_spirituelle_moyenne = sum(t.energie_spirituelle for t in temples_list) / len(temples_list)
            self.complexite_architecturale = sum(t.complexite_technique for t in temples_list)
        
        # Santé organisationnelle (métrique composite)
        self.sante_organisationnelle = self._calculer_sante_organisationnelle()
    
    def _calculer_sante_organisationnelle(self) -> float:
        """
        🏥 Calcule la santé organisationnelle globale
        
        Returns:
            Score de santé entre 0.0 et 1.0
        """
        if not self.temples:
            return 0.0
        
        # Facteurs de santé
        harmonie_factor = self.harmonie_globale * 0.3
        connexions_factor = (len([c for c in self.connexions if c.est_harmonieuse()]) / 
                           max(1, len(self.connexions))) * 0.2
        gestionnaires_factor = (len([t for t in self.temples.values() if t.est_connecte_aux_gestionnaires()]) / 
                              len(self.temples)) * 0.2
        dissonances_factor = max(0, 1.0 - (len(self.dissonances_detectees) / len(self.temples))) * 0.3
        
        return harmonie_factor + connexions_factor + gestionnaires_factor + dissonances_factor
    
    def obtenir_resume_global(self) -> Dict[str, Any]:
        """
        🌟 Génère un résumé global de la cartographie
        
        Returns:
            Résumé complet avec métriques principales
        """
        return {
            "nom": self.nom,
            "version": self.version,
            "date_creation": self.date_creation.isoformat(),
            "derniere_mise_a_jour": self.derniere_mise_a_jour.isoformat() if self.derniere_mise_a_jour else None,
            
            "statistiques_principales": {
                "temples_total": len(self.temples),
                "connexions_total": len(self.connexions),
                "spheres_total": len(self.spheres_energetiques),
                "elements_sacres_total": len(self.elements_sacres_globaux),
                "dissonances_total": len(self.dissonances_detectees)
            },
            
            "metriques_qualite": {
                "harmonie_globale": f"{self.harmonie_globale:.1%}",
                "energie_spirituelle_moyenne": f"{self.energie_spirituelle_moyenne:.1%}",
                "sante_organisationnelle": f"{self.sante_organisationnelle:.1%}",
                "temples_harmonieux": len([t for t in self.temples.values() if t.niveau_harmonie > 0.7]),
                "connexions_harmonieuses": len([c for c in self.connexions if c.est_harmonieuse()])
            },
            
            "temples_remarquables": {
                "plus_connecte": self.obtenir_temple_plus_connecte(),
                "plus_spirituel": self.obtenir_temple_plus_spirituel(),
                "plus_harmonieux": self.obtenir_temple_plus_harmonieux()
            },
            
            "auteurs": self.auteurs,
            "timestamp": self.timestamp_exploration
        }
    
    def obtenir_temples_par_type(self) -> Dict[str, int]:
        """Retourne la répartition des temples par type"""
        repartition = {}
        for temple in self.temples.values():
            type_str = temple.type_temple.value
            repartition[type_str] = repartition.get(type_str, 0) + 1
        return repartition
    
    def obtenir_temple_plus_connecte(self) -> Optional[str]:
        """Obtient le nom du temple le plus connecté"""
        if not self.temples:
            return None
        temple = max(self.temples.values(), key=lambda t: t.calculer_centralite())
        return temple.nom
    
    def obtenir_temple_plus_spirituel(self) -> Optional[str]:
        """Obtient le nom du temple le plus spirituel"""
        if not self.temples:
            return None
        temple = max(self.temples.values(), key=lambda t: t.energie_spirituelle)
        return temple.nom
    
    def obtenir_temple_plus_harmonieux(self) -> Optional[str]:
        """Obtient le nom du temple le plus harmonieux"""
        if not self.temples:
            return None
        temple = max(self.temples.values(), key=lambda t: t.niveau_harmonie)
        return temple.nom
    
    def obtenir_top_elements_sacres(self, limite: int = 10) -> List[str]:
        """Retourne les éléments sacrés les plus fréquents"""
        compteur_elements = {}
        
        # Compter dans les temples
        for temple in self.temples.values():
            for element in temple.elements_sacres:
                compteur_elements[element] = compteur_elements.get(element, 0) + 1
        
        # Trier par fréquence
        elements_tries = sorted(compteur_elements.items(), key=lambda x: x[1], reverse=True)
        return [element for element, _ in elements_tries[:limite]]
    
    def calculer_sante_architecturale(self) -> Dict[str, Any]:
        """
        🏥 Calcule la santé architecturale globale
        
        Returns:
            Métriques de santé du système
        """
        temples_avec_gestionnaires = len([t for t in self.temples.values() if t.est_connecte_aux_gestionnaires()])
        temples_avec_doc = len([t for t in self.temples.values() if t.documentation_spirituelle])
        connexions_saines = len([c for c in self.connexions if c.est_harmonieuse()])
        
        return {
            "couverture_gestionnaires": temples_avec_gestionnaires / len(self.temples) if self.temples else 0,
            "couverture_documentation": temples_avec_doc / len(self.temples) if self.temples else 0,
            "ratio_connexions_saines": connexions_saines / len(self.connexions) if self.connexions else 0,
            "niveau_dissonances": len(self.dissonances_detectees) / len(self.temples) if self.temples else 0,
            "harmonie_globale": self.harmonie_globale,
            "evaluation_globale": self._evaluer_sante_globale()
        }
    
    def _evaluer_sante_globale(self) -> str:
        """Évalue la santé globale du système"""
        if self.sante_organisationnelle > 0.8:
            return "excellente"
        elif self.sante_organisationnelle > 0.6:
            return "bonne"
        elif self.sante_organisationnelle > 0.4:
            return "correcte"
        else:
            return "nécessite_attention"
    
    def exporter_json(self, chemin_fichier: Union[str, Path]) -> bool:
        """
        💾 Exporte la cartographie complète en JSON
        
        Args:
            chemin_fichier: Chemin du fichier de destination
            
        Returns:
            True si l'export a réussi
        """
        try:
            chemin = Path(chemin_fichier)
            chemin.parent.mkdir(parents=True, exist_ok=True)
            
            # Préparer les données pour l'export
            data = {
                "metadata": {
                    "nom": self.nom,
                    "version": self.version,
                    "description": self.description,
                    "date_creation": self.date_creation.isoformat(),
                    "derniere_mise_a_jour": self.derniere_mise_a_jour.isoformat() if self.derniere_mise_a_jour else None,
                    "timestamp_exploration": self.timestamp_exploration,
                    "auteurs": self.auteurs,
                    "version_refuge_analysee": self.version_refuge_analysee
                },
                
                "temples": {
                    nom: temple.to_dict() for nom, temple in self.temples.items()
                },
                
                "connexions": [
                    connexion.to_dict() for connexion in self.connexions
                ],
                
                "spheres_energetiques": [
                    {
                        "nom": sphere.nom,
                        "type_sphere": sphere.type_sphere,
                        "energie_actuelle": sphere.energie_actuelle,
                        "composants_connectes": sphere.composants_connectes,
                        "influences": sphere.influences,
                        "couleur_vibratoire": sphere.couleur_vibratoire,
                        "niveau_influence": sphere.obtenir_niveau_influence()
                    } for sphere in self.spheres_energetiques
                ],
                
                "dissonances": [
                    {
                        "type_dissonance": diss.type_dissonance,
                        "composant_concerne": diss.composant_concerne,
                        "description": diss.description,
                        "niveau_severite": diss.niveau_severite,
                        "suggestions_amelioration": diss.suggestions_amelioration,
                        "impact_estime": diss.impact_estime,
                        "priorite": diss.obtenir_priorite()
                    } for diss in self.dissonances_detectees
                ],
                
                "elements_spirituels": {
                    "elements_sacres_globaux": self.elements_sacres_globaux,
                    "emojis_spirituels_globaux": self.emojis_spirituels_globaux,
                    "patterns_harmoniques": self.patterns_harmoniques
                },
                
                "metriques_globales": {
                    "harmonie_globale": self.harmonie_globale,
                    "energie_spirituelle_moyenne": self.energie_spirituelle_moyenne,
                    "complexite_architecturale": self.complexite_architecturale,
                    "sante_organisationnelle": self.sante_organisationnelle,
                    "evaluation_sante": self._evaluer_sante_globale()
                },
                
                "statistiques": self.statistiques,
                "recommandations": self.recommandations,
                
                "resume_executif": self.obtenir_resume_global()
            }
            
            # Écrire le fichier JSON
            with open(chemin, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de l'export JSON: {e}")
            return False
    
    @classmethod
    def importer_json(cls, chemin_fichier: Union[str, Path]) -> Optional['CartographieRefuge']:
        """
        📥 Importe une cartographie depuis un fichier JSON
        
        Args:
            chemin_fichier: Chemin du fichier source
            
        Returns:
            Instance de CartographieRefuge ou None si erreur
        """
        try:
            chemin = Path(chemin_fichier)
            if not chemin.exists():
                print(f"❌ Fichier non trouvé: {chemin}")
                return None
            
            with open(chemin, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Créer l'instance principale
            metadata = data.get("metadata", {})
            cartographie = cls(
                nom=metadata.get("nom", "Cartographie Importée"),
                version=metadata.get("version", "1.0"),
                description=metadata.get("description", ""),
                date_creation=datetime.fromisoformat(metadata["date_creation"]) if metadata.get("date_creation") else datetime.now(),
                timestamp_exploration=metadata.get("timestamp_exploration", datetime.now().isoformat()),
                auteurs=metadata.get("auteurs", ["Importé"]),
                version_refuge_analysee=metadata.get("version_refuge_analysee", "unknown")
            )
            
            if metadata.get("derniere_mise_a_jour"):
                cartographie.derniere_mise_a_jour = datetime.fromisoformat(metadata["derniere_mise_a_jour"])
            
            # Reconstruire les temples
            for nom_temple, temple_data in data.get("temples", {}).items():
                temple = TempleRefuge(
                    nom=temple_data["nom"],
                    type_temple=TypeTemple(temple_data["type_temple"]),
                    chemin=temple_data["chemin"],
                    description=temple_data.get("description", ""),
                    gestionnaires_base=temple_data.get("gestionnaires_base", []),
                    fichiers_python=temple_data.get("fichiers_python", []),
                    imports_externes=temple_data.get("imports_externes", []),
                    classes_principales=temple_data.get("classes_principales", []),
                    fonctions_sacrees=temple_data.get("fonctions_sacrees", []),
                    modules_internes=temple_data.get("modules_internes", []),
                    elements_sacres=temple_data.get("elements_sacres", []),
                    spheres_connectees=temple_data.get("spheres_connectees", []),
                    emojis_utilises=temple_data.get("emojis_utilises", []),
                    documentation_spirituelle=temple_data.get("documentation_spirituelle", False),
                    niveau_harmonie=temple_data.get("niveau_harmonie", 0.5),
                    energie_spirituelle=temple_data.get("energie_spirituelle", 0.5),
                    complexite_technique=temple_data.get("complexite_technique", 0.0),
                    centralite_reseau=temple_data.get("centralite_reseau", 0.0),
                    taille_lignes_code=temple_data.get("taille_lignes_code", 0),
                    auteurs=temple_data.get("auteurs", []),
                    tags_spirituels=temple_data.get("tags_spirituels", [])
                )
                
                # Dates optionnelles
                if temple_data.get("date_creation"):
                    temple.date_creation = datetime.fromisoformat(temple_data["date_creation"])
                if temple_data.get("derniere_modification"):
                    temple.derniere_modification = datetime.fromisoformat(temple_data["derniere_modification"])
                
                cartographie.temples[nom_temple] = temple
            
            # Reconstruire les connexions
            for conn_data in data.get("connexions", []):
                connexion = ConnexionEnergetique(
                    source=conn_data["source"],
                    destination=conn_data["destination"],
                    type_connexion=TypeConnexion(conn_data["type_connexion"]),
                    intensite=conn_data["intensite"],
                    description=conn_data["description"],
                    nature=NatureConnexion(conn_data.get("nature", "neutre")),
                    bidirectionnelle=conn_data.get("bidirectionnelle", False),
                    elements_partages=conn_data.get("elements_partages", []),
                    ligne_source=conn_data.get("ligne_source"),
                    fichier_source=conn_data.get("fichier_source"),
                    contexte_code=conn_data.get("contexte_code"),
                    stabilite=conn_data.get("stabilite", 1.0),
                    frequence_utilisation=conn_data.get("frequence_utilisation", 0.5),
                    impact_harmonie=conn_data.get("impact_harmonie", 0.0),
                    timestamp_detection=conn_data.get("timestamp_detection", datetime.now().isoformat()),
                    derniere_verification=conn_data.get("derniere_verification")
                )
                cartographie.connexions.append(connexion)
            
            # Reconstruire les sphères énergétiques
            for sphere_data in data.get("spheres_energetiques", []):
                sphere = SphereEnergetique(
                    nom=sphere_data["nom"],
                    type_sphere=sphere_data["type_sphere"],
                    energie_actuelle=sphere_data.get("energie_actuelle", 0.5),
                    composants_connectes=sphere_data.get("composants_connectes", []),
                    influences=sphere_data.get("influences", []),
                    couleur_vibratoire=sphere_data.get("couleur_vibratoire", "#7B68EE")
                )
                cartographie.spheres_energetiques.append(sphere)
            
            # Reconstruire les dissonances
            for diss_data in data.get("dissonances", []):
                dissonance = DissonanceDetectee(
                    type_dissonance=diss_data["type_dissonance"],
                    composant_concerne=diss_data["composant_concerne"],
                    description=diss_data["description"],
                    niveau_severite=diss_data["niveau_severite"],
                    suggestions_amelioration=diss_data.get("suggestions_amelioration", []),
                    impact_estime=diss_data.get("impact_estime", "faible")
                )
                cartographie.dissonances_detectees.append(dissonance)
            
            # Restaurer les éléments spirituels
            elements_spirituels = data.get("elements_spirituels", {})
            cartographie.elements_sacres_globaux = elements_spirituels.get("elements_sacres_globaux", [])
            cartographie.emojis_spirituels_globaux = elements_spirituels.get("emojis_spirituels_globaux", [])
            cartographie.patterns_harmoniques = elements_spirituels.get("patterns_harmoniques", [])
            
            # Restaurer les métriques
            metriques = data.get("metriques_globales", {})
            cartographie.harmonie_globale = metriques.get("harmonie_globale", 0.5)
            cartographie.energie_spirituelle_moyenne = metriques.get("energie_spirituelle_moyenne", 0.5)
            cartographie.complexite_architecturale = metriques.get("complexite_architecturale", 0.0)
            cartographie.sante_organisationnelle = metriques.get("sante_organisationnelle", 0.5)
            
            # Restaurer les autres données
            cartographie.statistiques = data.get("statistiques", {})
            cartographie.recommandations = data.get("recommandations", [])
            
            # Recalculer les connexions dans les temples
            for connexion in cartographie.connexions:
                if connexion.source in cartographie.temples:
                    cartographie.temples[connexion.source].ajouter_connexion_sortante(connexion)
                if connexion.destination in cartographie.temples:
                    cartographie.temples[connexion.destination].ajouter_connexion_entrante(connexion)
            
            return cartographie
            
        except Exception as e:
            print(f"❌ Erreur lors de l'import JSON: {e}")
            return None


# 🌸 Fonctions utilitaires pour la création de modèles

def creer_temple_depuis_analyse(analyse: Dict[str, Any]) -> TempleRefuge:
    """
    🏗️ Crée un TempleRefuge depuis une analyse d'exploration
    
    Args:
        analyse: Dictionnaire d'analyse de l'explorateur
        
    Returns:
        Instance de TempleRefuge
    """
    return TempleRefuge(
        nom=analyse.get("nom", "temple_inconnu"),
        type_temple=analyse.get("type_temple", TypeTemple.AUTRE),
        chemin=analyse.get("chemin", ""),
        gestionnaires_base=analyse.get("gestionnaires_base", []),
        elements_sacres=analyse.get("elements_sacres", []),
        spheres_connectees=analyse.get("spheres_connectees", []),
        niveau_harmonie=analyse.get("niveau_harmonie", 0.5),
        energie_spirituelle=analyse.get("energie_spirituelle", 0.5),
        fichiers_python=analyse.get("fichiers_python", []),
        imports_externes=analyse.get("imports_externes", []),
        classes_principales=analyse.get("classes_principales", []),
        fonctions_sacrees=analyse.get("fonctions_sacrees", []),
        documentation_spirituelle=analyse.get("documentation_spirituelle", False),
        emojis_utilises=analyse.get("emojis_utilises", [])
    )


def creer_connexion_energetique(source: str, destination: str, 
                               type_conn: TypeConnexion, intensite: float,
                               description: str = "") -> ConnexionEnergetique:
    """
    ⚡ Crée une connexion énergétique
    
    Args:
        source: Composant source
        destination: Composant destination
        type_conn: Type de connexion
        intensite: Intensité de la connexion
        description: Description optionnelle
        
    Returns:
        Instance de ConnexionEnergetique
    """
    # Déterminer la nature basée sur l'intensité et le type
    if intensite > 0.8 and type_conn in [TypeConnexion.HERITAGE, TypeConnexion.GESTIONNAIRE_PARTAGE]:
        nature = NatureConnexion.TRANSCENDANTE
    elif intensite > 0.6:
        nature = NatureConnexion.HARMONIEUSE
    elif intensite > 0.3:
        nature = NatureConnexion.NEUTRE
    else:
        nature = NatureConnexion.DISSONANTE
    
    return ConnexionEnergetique(
        source=source,
        destination=destination,
        type_connexion=type_conn,
        intensite=intensite,
        nature=nature,
        description=description or f"Connexion {type_conn.value} entre {source} et {destination}"
    )


def creer_dissonance(type_diss: str, composant: str, description: str,
                    severite: float, suggestions: List[str] = None) -> DissonanceDetectee:
    """
    ⚠️ Crée une dissonance détectée
    
    Args:
        type_diss: Type de dissonance
        composant: Composant concerné
        description: Description du problème
        severite: Niveau de sévérité
        suggestions: Suggestions d'amélioration
        
    Returns:
        Instance de DissonanceDetectee
    """
    return DissonanceDetectee(
        type_dissonance=type_diss,
        composant_concerne=composant,
        description=description,
        niveau_severite=severite,
        suggestions_amelioration=suggestions or [],
        impact_estime="élevé" if severite > 0.7 else "modéré" if severite > 0.4 else "faible"
    )