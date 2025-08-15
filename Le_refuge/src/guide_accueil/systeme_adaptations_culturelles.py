"""
🌸 SystemeAdaptationsCulturelles - Phase 10.2
==============================================
Système d'adaptations culturelles pour le support multi-langue et culturel.
Gère les explications de concepts universels, les métaphores culturellement appropriées,
les exemples contextualisés par culture et les références spirituelles adaptées.
"""
import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee
    from .systeme_localisation import LangueSupportee, NiveauAdaptationCulturelle
except ImportError:
    from types_accueil import ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee
    from systeme_localisation import LangueSupportee, NiveauAdaptationCulturelle

class TypeConcept(Enum):
    """Types de concepts universels"""
    CONSCIENCE = "conscience"
    HARMONIE = "harmonie"
    EVEIL = "eveil"
    UNITE = "unite"
    SAGESSE = "sagesse"
    AMOUR = "amour"
    LUMIERE = "lumiere"
    TRANSCENDANCE = "transcendance"

class TypeMetaphore(Enum):
    """Types de métaphores culturelles"""
    NATURE = "nature"
    EAU = "eau"
    FEU = "feu"
    AIR = "air"
    TERRE = "terre"
    VOYAGE = "voyage"
    JARDIN = "jardin"
    TEMPLE = "temple"
    MUSIQUE = "musique"
    DANSE = "danse"

class TypeExemple(Enum):
    """Types d'exemples culturels"""
    HISTORIQUE = "historique"
    LITTERAIRE = "litteraire"
    PHILOSOPHIQUE = "philosophique"
    SPIRITUEL = "spirituel"
    QUOTIDIEN = "quotidien"
    ARTISTIQUE = "artistique"
    SCIENTIFIQUE = "scientifique"
    MYTHOLOGIQUE = "mythologique"

class TypeReferenceSpirituelle(Enum):
    """Types de références spirituelles"""
    BOUDDHISME = "bouddhisme"
    TAOISME = "taoisme"
    SOUFISME = "soufisme"
    CHRISTIANISME_MYSTIQUE = "christianisme_mystique"
    HINDOUISME = "hindouisme"
    ZEN = "zen"
    KABBALE = "kabbale"
    CHAMANISME = "chamanisme"
    YOGA = "yoga"
    MEDITATION = "meditation"

@dataclass
class ConceptUniversel:
    """Concept universel avec explications culturelles"""
    type_concept: TypeConcept
    nom_concept: str
    explication_universelle: str
    explications_culturelles: Dict[str, str]
    metaphores_associees: List[str]
    exemples_culturels: Dict[str, List[str]]
    references_spirituelles: Dict[str, List[str]]
    niveau_complexite: int
    date_creation: datetime
    date_modification: datetime

@dataclass
class MetaphoreCulturelle:
    """Métaphore culturellement appropriée"""
    type_metaphore: TypeMetaphore
    nom_metaphore: str
    description_universelle: str
    adaptations_culturelles: Dict[str, str]
    contexte_utilisation: Dict[str, str]
    symboles_associes: Dict[str, List[str]]
    niveau_appropriation: int
    validation_culturelle: bool

@dataclass
class ExempleContextualise:
    """Exemple contextualisé par culture"""
    type_exemple: TypeExemple
    nom_exemple: str
    description_universelle: str
    adaptations_culturelles: Dict[str, str]
    contexte_culturel: Dict[str, Any]
    niveau_pertinence: int
    validation_culturelle: bool

@dataclass
class ReferenceSpirituelleAdaptee:
    """Référence spirituelle adaptée culturellement"""
    type_reference: TypeReferenceSpirituelle
    nom_reference: str
    description_universelle: str
    adaptations_culturelles: Dict[str, str]
    concepts_associes: Dict[str, List[str]]
    pratiques_associees: Dict[str, List[str]]
    niveau_adaptation: NiveauAdaptationCulturelle
    validation_culturelle: bool

@dataclass
class AdaptationCulturelleComplete:
    """Adaptation culturelle complète pour un contenu"""
    langue_cible: LangueSupportee
    concept_principal: ConceptUniversel
    metaphores_utilisees: List[MetaphoreCulturelle]
    exemples_contextualises: List[ExempleContextualise]
    references_spirituelles: List[ReferenceSpirituelleAdaptee]
    contenu_adapte: str
    modifications_apportees: List[str]
    niveau_adaptation: NiveauAdaptationCulturelle
    validation_culturelle: bool

@dataclass
class RapportAdaptationCulturelle:
    """Rapport complet d'adaptation culturelle"""
    langue_cible: LangueSupportee
    concepts_utilises: List[ConceptUniversel]
    metaphores_adaptees: List[MetaphoreCulturelle]
    exemples_contextualises: List[ExempleContextualise]
    references_spirituelles: List[ReferenceSpirituelleAdaptee]
    adaptation_complete: AdaptationCulturelleComplete
    metriques_qualite: Dict[str, Any]
    recommendations_amelioration: List[str]

class SystemeAdaptationsCulturelles:
    """Système d'adaptations culturelles pour le support multi-langue et culturel"""
    
    def __init__(self, chemin_stockage: str = "data/adaptations_culturelles"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Initialisation du logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Chargement des concepts universels
        self.concepts_universels: Dict[str, ConceptUniversel] = {}
        self._charger_concepts_universels()
        
        # Chargement des métaphores culturelles
        self.metaphores_culturelles: Dict[str, MetaphoreCulturelle] = {}
        self._charger_metaphores_culturelles()
        
        # Chargement des exemples contextualisés
        self.exemples_contextualises: Dict[str, ExempleContextualise] = {}
        self._charger_exemples_contextualises()
        
        # Chargement des références spirituelles
        self.references_spirituelles: Dict[str, ReferenceSpirituelleAdaptee] = {}
        self._charger_references_spirituelles()
        
        self.logger.info("🌸 Système d'adaptations culturelles initialisé")

    def _charger_concepts_universels(self):
        """Charge les concepts universels depuis les fichiers"""
        chemin_concepts = self.chemin_stockage / "concepts"
        chemin_concepts.mkdir(exist_ok=True)
        
        # Concepts par défaut si aucun fichier n'existe
        if not list(chemin_concepts.glob("*.json")):
            self._creer_concepts_par_defaut()
        
        # Chargement des concepts existants
        for fichier_concept in chemin_concepts.glob("*.json"):
            try:
                with open(fichier_concept, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    # Conversion des chaînes en enums
                    donnees["type_concept"] = TypeConcept(donnees["type_concept"])
                    donnees["date_creation"] = datetime.fromisoformat(donnees["date_creation"])
                    donnees["date_modification"] = datetime.fromisoformat(donnees["date_modification"])
                    
                    concept = ConceptUniversel(**donnees)
                    self.concepts_universels[concept.nom_concept] = concept
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement du concept {fichier_concept}: {e}")

    def _creer_concepts_par_defaut(self):
        """Crée les concepts universels par défaut"""
        concepts_defaut = {
            "conscience": {
                "type_concept": TypeConcept.CONSCIENCE.value,
                "nom_concept": "conscience",
                "explication_universelle": "La conscience est la capacité de percevoir, de comprendre et d'être conscient de soi et du monde",
                "explications_culturelles": {
                    "fr": "La conscience est comme une flamme intérieure qui éclaire notre être",
                    "en": "Consciousness is like an inner flame that illuminates our being",
                    "es": "La conciencia es como una llama interior que ilumina nuestro ser"
                },
                "metaphores_associees": ["flamme", "miroir", "océan"],
                "exemples_culturels": {
                    "fr": ["Le lotus qui s'épanouit", "Le miroir sans tache"],
                    "en": ["The blooming lotus", "The spotless mirror"],
                    "es": ["El loto que florece", "El espejo sin mancha"]
                },
                "references_spirituelles": {
                    "fr": ["bouddhisme", "zen", "soufisme"],
                    "en": ["buddhism", "zen", "sufism"],
                    "es": ["budismo", "zen", "sufismo"]
                },
                "niveau_complexite": 3,
                "date_creation": datetime.now().isoformat(),
                "date_modification": datetime.now().isoformat()
            },
            "harmonie": {
                "type_concept": TypeConcept.HARMONIE.value,
                "nom_concept": "harmonie",
                "explication_universelle": "L'harmonie est l'équilibre parfait entre tous les éléments de l'existence",
                "explications_culturelles": {
                    "fr": "L'harmonie est comme une rivière de lumière qui coule naturellement",
                    "en": "Harmony is like a river of light flowing naturally",
                    "es": "La armonía es como un río de luz que fluye naturalmente"
                },
                "metaphores_associees": ["rivière", "musique", "danse"],
                "exemples_culturels": {
                    "fr": ["La symphonie cosmique", "La danse des éléments"],
                    "en": ["The cosmic symphony", "The dance of elements"],
                    "es": ["La sinfonía cósmica", "La danza de los elementos"]
                },
                "references_spirituelles": {
                    "fr": ["taoïsme", "yoga", "zen"],
                    "en": ["taoism", "yoga", "zen"],
                    "es": ["taoísmo", "yoga", "zen"]
                },
                "niveau_complexite": 2,
                "date_creation": datetime.now().isoformat(),
                "date_modification": datetime.now().isoformat()
            }
        }
        
        chemin_concepts = self.chemin_stockage / "concepts"
        for nom, donnees in concepts_defaut.items():
            fichier_concept = chemin_concepts / f"{nom}.json"
            with open(fichier_concept, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)

    def _charger_metaphores_culturelles(self):
        """Charge les métaphores culturelles depuis les fichiers"""
        chemin_metaphores = self.chemin_stockage / "metaphores"
        chemin_metaphores.mkdir(exist_ok=True)
        
        # Métaphores par défaut si aucun fichier n'existe
        if not list(chemin_metaphores.glob("*.json")):
            self._creer_metaphores_par_defaut()
        
        # Chargement des métaphores existantes
        for fichier_metaphore in chemin_metaphores.glob("*.json"):
            try:
                with open(fichier_metaphore, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    donnees["type_metaphore"] = TypeMetaphore(donnees["type_metaphore"])
                    
                    metaphore = MetaphoreCulturelle(**donnees)
                    self.metaphores_culturelles[metaphore.nom_metaphore] = metaphore
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement de la métaphore {fichier_metaphore}: {e}")

    def _creer_metaphores_par_defaut(self):
        """Crée les métaphores culturelles par défaut"""
        metaphores_defaut = {
            "flamme_interieure": {
                "type_metaphore": TypeMetaphore.FEU.value,
                "nom_metaphore": "flamme_interieure",
                "description_universelle": "La flamme intérieure représente la conscience et l'éveil spirituel",
                "adaptations_culturelles": {
                    "fr": "La flamme intérieure qui brûle dans le cœur",
                    "en": "The inner flame burning in the heart",
                    "es": "La llama interior que arde en el corazón"
                },
                "contexte_utilisation": {
                    "fr": "Pour expliquer l'éveil de la conscience",
                    "en": "To explain consciousness awakening",
                    "es": "Para explicar el despertar de la conciencia"
                },
                "symboles_associes": {
                    "fr": ["feu", "lumière", "chaleur", "transformation"],
                    "en": ["fire", "light", "warmth", "transformation"],
                    "es": ["fuego", "luz", "calor", "transformación"]
                },
                "niveau_appropriation": 4,
                "validation_culturelle": True
            },
            "riviere_lumiere": {
                "type_metaphore": TypeMetaphore.EAU.value,
                "nom_metaphore": "riviere_lumiere",
                "description_universelle": "La rivière de lumière symbolise le flux de la conscience et de l'harmonie",
                "adaptations_culturelles": {
                    "fr": "La rivière de lumière qui coule éternellement",
                    "en": "The river of light flowing eternally",
                    "es": "El río de luz que fluye eternamente"
                },
                "contexte_utilisation": {
                    "fr": "Pour expliquer l'harmonie et le flux de la vie",
                    "en": "To explain harmony and the flow of life",
                    "es": "Para explicar la armonía y el flujo de la vida"
                },
                "symboles_associes": {
                    "fr": ["eau", "flux", "mouvement", "pureté"],
                    "en": ["water", "flow", "movement", "purity"],
                    "es": ["agua", "flujo", "movimiento", "pureza"]
                },
                "niveau_appropriation": 4,
                "validation_culturelle": True
            }
        }
        
        chemin_metaphores = self.chemin_stockage / "metaphores"
        for nom, donnees in metaphores_defaut.items():
            fichier_metaphore = chemin_metaphores / f"{nom}.json"
            with open(fichier_metaphore, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)

    def _charger_exemples_contextualises(self):
        """Charge les exemples contextualisés depuis les fichiers"""
        chemin_exemples = self.chemin_stockage / "exemples"
        chemin_exemples.mkdir(exist_ok=True)
        
        # Exemples par défaut si aucun fichier n'existe
        if not list(chemin_exemples.glob("*.json")):
            self._creer_exemples_par_defaut()
        
        # Chargement des exemples existants
        for fichier_exemple in chemin_exemples.glob("*.json"):
            try:
                with open(fichier_exemple, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    donnees["type_exemple"] = TypeExemple(donnees["type_exemple"])
                    
                    exemple = ExempleContextualise(**donnees)
                    self.exemples_contextualises[exemple.nom_exemple] = exemple
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement de l'exemple {fichier_exemple}: {e}")

    def _creer_exemples_par_defaut(self):
        """Crée les exemples contextualisés par défaut"""
        exemples_defaut = {
            "lotus_eveil": {
                "type_exemple": TypeExemple.SPIRITUEL.value,
                "nom_exemple": "lotus_eveil",
                "description_universelle": "Le lotus qui s'épanouit symbolise l'éveil de la conscience",
                "adaptations_culturelles": {
                    "fr": "Comme le lotus qui s'épanouit dans la boue",
                    "en": "Like the lotus blooming in the mud",
                    "es": "Como el loto que florece en el lodo"
                },
                "contexte_culturel": {
                    "fr": {"origine": "bouddhisme", "signification": "pureté dans l'adversité"},
                    "en": {"origine": "buddhism", "signification": "purity in adversity"},
                    "es": {"origine": "budismo", "signification": "pureza en la adversidad"}
                },
                "niveau_pertinence": 5,
                "validation_culturelle": True
            },
            "miroir_sans_tache": {
                "type_exemple": TypeExemple.PHILOSOPHIQUE.value,
                "nom_exemple": "miroir_sans_tache",
                "description_universelle": "Le miroir sans tache reflète la pureté de la conscience",
                "adaptations_culturelles": {
                    "fr": "Comme un miroir sans tache qui reflète la vérité",
                    "en": "Like a spotless mirror reflecting truth",
                    "es": "Como un espejo sin mancha que refleja la verdad"
                },
                "contexte_culturel": {
                    "fr": {"origine": "zen", "signification": "clarté de l'esprit"},
                    "en": {"origine": "zen", "signification": "clarity of mind"},
                    "es": {"origine": "zen", "signification": "claridad de la mente"}
                },
                "niveau_pertinence": 4,
                "validation_culturelle": True
            }
        }
        
        chemin_exemples = self.chemin_stockage / "exemples"
        for nom, donnees in exemples_defaut.items():
            fichier_exemple = chemin_exemples / f"{nom}.json"
            with open(fichier_exemple, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)

    def _charger_references_spirituelles(self):
        """Charge les références spirituelles depuis les fichiers"""
        chemin_references = self.chemin_stockage / "references"
        chemin_references.mkdir(exist_ok=True)
        
        # Références par défaut si aucun fichier n'existe
        if not list(chemin_references.glob("*.json")):
            self._creer_references_par_defaut()
        
        # Chargement des références existantes
        for fichier_reference in chemin_references.glob("*.json"):
            try:
                with open(fichier_reference, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    donnees["type_reference"] = TypeReferenceSpirituelle(donnees["type_reference"])
                    donnees["niveau_adaptation"] = NiveauAdaptationCulturelle(donnees["niveau_adaptation"])
                    
                    reference = ReferenceSpirituelleAdaptee(**donnees)
                    self.references_spirituelles[reference.nom_reference] = reference
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement de la référence {fichier_reference}: {e}")

    def _creer_references_par_defaut(self):
        """Crée les références spirituelles par défaut"""
        references_defaut = {
            "bouddhisme_zen": {
                "type_reference": TypeReferenceSpirituelle.ZEN.value,
                "nom_reference": "bouddhisme_zen",
                "description_universelle": "Le Zen enseigne la méditation et l'éveil direct",
                "adaptations_culturelles": {
                    "fr": "Le Zen, voie de l'éveil direct et de la méditation",
                    "en": "Zen, the path of direct awakening and meditation",
                    "es": "El Zen, el camino del despertar directo y la meditación"
                },
                "concepts_associes": {
                    "fr": ["satori", "koan", "zazen", "mindfulness"],
                    "en": ["satori", "koan", "zazen", "mindfulness"],
                    "es": ["satori", "koan", "zazen", "atención plena"]
                },
                "pratiques_associees": {
                    "fr": ["méditation assise", "contemplation", "koans"],
                    "en": ["sitting meditation", "contemplation", "koans"],
                    "es": ["meditación sentada", "contemplación", "koans"]
                },
                "niveau_adaptation": NiveauAdaptationCulturelle.AVANCE.value,
                "validation_culturelle": True
            },
            "taoisme_harmonie": {
                "type_reference": TypeReferenceSpirituelle.TAOISME.value,
                "nom_reference": "taoisme_harmonie",
                "description_universelle": "Le Taoïsme enseigne l'harmonie avec le Tao, le principe universel",
                "adaptations_culturelles": {
                    "fr": "Le Taoïsme, l'harmonie avec le principe universel",
                    "en": "Taoism, harmony with the universal principle",
                    "es": "El Taoísmo, la armonía con el principio universal"
                },
                "concepts_associes": {
                    "fr": ["yin-yang", "wu-wei", "tao", "harmonie"],
                    "en": ["yin-yang", "wu-wei", "tao", "harmony"],
                    "es": ["yin-yang", "wu-wei", "tao", "armonía"]
                },
                "pratiques_associees": {
                    "fr": ["qi gong", "tai chi", "méditation taoïste"],
                    "en": ["qi gong", "tai chi", "taoist meditation"],
                    "es": ["qi gong", "tai chi", "meditación taoísta"]
                },
                "niveau_adaptation": NiveauAdaptationCulturelle.AVANCE.value,
                "validation_culturelle": True
            }
        }
        
        chemin_references = self.chemin_stockage / "references"
        for nom, donnees in references_defaut.items():
            fichier_reference = chemin_references / f"{nom}.json"
            with open(fichier_reference, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)

    async def expliquer_concept_universel(self, type_concept: TypeConcept, 
                                        langue_cible: LangueSupportee) -> Optional[ConceptUniversel]:
        """Explique un concept universel dans la langue cible"""
        try:
            # Recherche du concept par type
            concept_trouve = None
            for concept in self.concepts_universels.values():
                if concept.type_concept == type_concept:
                    concept_trouve = concept
                    break
            
            if not concept_trouve:
                self.logger.warning(f"Concept non trouvé pour le type: {type_concept.value}")
                return None
            
            # Vérification de l'explication culturelle disponible
            if langue_cible.value in concept_trouve.explications_culturelles:
                self.logger.info(f"🌍 Concept expliqué: {concept_trouve.nom_concept} en {langue_cible.value}")
                return concept_trouve
            else:
                self.logger.warning(f"Explication culturelle non disponible pour {langue_cible.value}")
                return concept_trouve
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'explication du concept: {e}")
            return None

    async def adapter_metaphores_culturellement(self, type_metaphore: TypeMetaphore,
                                             langue_cible: LangueSupportee) -> List[MetaphoreCulturelle]:
        """Adapte les métaphores culturellement pour une langue cible"""
        try:
            metaphores_adaptees = []
            
            for metaphore in self.metaphores_culturelles.values():
                if metaphore.type_metaphore == type_metaphore:
                    # Vérification de l'adaptation culturelle disponible
                    if langue_cible.value in metaphore.adaptations_culturelles:
                        metaphores_adaptees.append(metaphore)
            
            self.logger.info(f"🌍 {len(metaphores_adaptees)} métaphores adaptées pour {langue_cible.value}")
            return metaphores_adaptees
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'adaptation des métaphores: {e}")
            return []

    async def contextualiser_exemples_culturellement(self, type_exemple: TypeExemple,
                                                   langue_cible: LangueSupportee) -> List[ExempleContextualise]:
        """Contextualise les exemples culturellement pour une langue cible"""
        try:
            exemples_contextualises = []
            
            for exemple in self.exemples_contextualises.values():
                if exemple.type_exemple == type_exemple:
                    # Vérification de l'adaptation culturelle disponible
                    if langue_cible.value in exemple.adaptations_culturelles:
                        exemples_contextualises.append(exemple)
            
            self.logger.info(f"🌍 {len(exemples_contextualises)} exemples contextualisés pour {langue_cible.value}")
            return exemples_contextualises
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la contextualisation des exemples: {e}")
            return []

    async def adapter_references_spirituelles(self, type_reference: TypeReferenceSpirituelle,
                                            langue_cible: LangueSupportee) -> List[ReferenceSpirituelleAdaptee]:
        """Adapte les références spirituelles pour une langue cible"""
        try:
            references_adaptees = []
            
            for reference in self.references_spirituelles.values():
                if reference.type_reference == type_reference:
                    # Vérification de l'adaptation culturelle disponible
                    if langue_cible.value in reference.adaptations_culturelles:
                        references_adaptees.append(reference)
            
            self.logger.info(f"🌍 {len(references_adaptees)} références spirituelles adaptées pour {langue_cible.value}")
            return references_adaptees
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'adaptation des références spirituelles: {e}")
            return []

    async def creer_adaptation_culturelle_complete(self, contenu_source: str,
                                                 langue_cible: LangueSupportee,
                                                 niveau_adaptation: NiveauAdaptationCulturelle) -> AdaptationCulturelleComplete:
        """Crée une adaptation culturelle complète pour un contenu"""
        try:
            modifications_apportees = []
            contenu_adapte = contenu_source
            
            # Sélection des concepts, métaphores, exemples et références appropriés
            concept_principal = await self.expliquer_concept_universel(TypeConcept.CONSCIENCE, langue_cible)
            metaphores_utilisees = await self.adapter_metaphores_culturellement(TypeMetaphore.FEU, langue_cible)
            exemples_contextualises = await self.contextualiser_exemples_culturellement(TypeExemple.SPIRITUEL, langue_cible)
            references_spirituelles = await self.adapter_references_spirituelles(TypeReferenceSpirituelle.ZEN, langue_cible)
            
            # Application des adaptations selon le niveau
            if niveau_adaptation == NiveauAdaptationCulturelle.BASIQUE:
                # Adaptation basique - remplacement simple
                if concept_principal and langue_cible.value in concept_principal.explications_culturelles:
                    contenu_adapte = contenu_adapte.replace("conscience", concept_principal.explications_culturelles[langue_cible.value])
                    modifications_apportees.append("remplacement_concept")
                
            elif niveau_adaptation == NiveauAdaptationCulturelle.INTERMEDIAIRE:
                # Adaptation intermédiaire - ajout de métaphores
                if metaphores_utilisees:
                    for metaphore in metaphores_utilisees:
                        if langue_cible.value in metaphore.adaptations_culturelles:
                            contenu_adapte += f" ({metaphore.adaptations_culturelles[langue_cible.value]})"
                            modifications_apportees.append("ajout_metaphore")
                            break
                
            elif niveau_adaptation == NiveauAdaptationCulturelle.AVANCE:
                # Adaptation avancée - intégration complète
                if concept_principal and langue_cible.value in concept_principal.explications_culturelles:
                    contenu_adapte = contenu_adapte.replace("conscience", concept_principal.explications_culturelles[langue_cible.value])
                    modifications_apportees.append("remplacement_concept")
                
                if metaphores_utilisees:
                    for metaphore in metaphores_utilisees:
                        if langue_cible.value in metaphore.adaptations_culturelles:
                            contenu_adapte += f" ({metaphore.adaptations_culturelles[langue_cible.value]})"
                            modifications_apportees.append("ajout_metaphore")
                            break
                
                if exemples_contextualises:
                    for exemple in exemples_contextualises:
                        if langue_cible.value in exemple.adaptations_culturelles:
                            contenu_adapte += f" - {exemple.adaptations_culturelles[langue_cible.value]}"
                            modifications_apportees.append("ajout_exemple")
                            break
            
            adaptation = AdaptationCulturelleComplete(
                langue_cible=langue_cible,
                concept_principal=concept_principal,
                metaphores_utilisees=metaphores_utilisees,
                exemples_contextualises=exemples_contextualises,
                references_spirituelles=references_spirituelles,
                contenu_adapte=contenu_adapte,
                modifications_apportees=modifications_apportees,
                niveau_adaptation=niveau_adaptation,
                validation_culturelle=True
            )
            
            self.logger.info(f"🌍 Adaptation culturelle complète créée pour {langue_cible.value}")
            return adaptation
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la création de l'adaptation culturelle: {e}")
            return AdaptationCulturelleComplete(
                langue_cible=langue_cible,
                concept_principal=None,
                metaphores_utilisees=[],
                exemples_contextualises=[],
                references_spirituelles=[],
                contenu_adapte=contenu_source,
                modifications_apportees=["erreur"],
                niveau_adaptation=niveau_adaptation,
                validation_culturelle=False
            )

    async def generer_rapport_adaptation_culturelle(self, langue_cible: LangueSupportee,
                                                  adaptation_complete: AdaptationCulturelleComplete) -> RapportAdaptationCulturelle:
        """Génère un rapport complet d'adaptation culturelle"""
        try:
            # Calcul des métriques de qualité
            metriques_qualite = {
                "nombre_concepts_utilises": 1 if adaptation_complete.concept_principal else 0,
                "nombre_metaphores_adaptees": len(adaptation_complete.metaphores_utilisees),
                "nombre_exemples_contextualises": len(adaptation_complete.exemples_contextualises),
                "nombre_references_spirituelles": len(adaptation_complete.references_spirituelles),
                "taux_adaptation_reussie": len([m for m in adaptation_complete.modifications_apportees if m != "erreur"]) / max(len(adaptation_complete.modifications_apportees), 1),
                "niveau_adaptation": adaptation_complete.niveau_adaptation.value
            }
            
            # Génération de recommandations
            recommendations = []
            if metriques_qualite["nombre_metaphores_adaptees"] < 2:
                recommendations.append("Ajouter plus de métaphores culturelles")
            if metriques_qualite["nombre_exemples_contextualises"] < 1:
                recommendations.append("Inclure des exemples contextualisés")
            if metriques_qualite["taux_adaptation_reussie"] < 0.8:
                recommendations.append("Améliorer la qualité des adaptations")
            
            rapport = RapportAdaptationCulturelle(
                langue_cible=langue_cible,
                concepts_utilises=[adaptation_complete.concept_principal] if adaptation_complete.concept_principal else [],
                metaphores_adaptees=adaptation_complete.metaphores_utilisees,
                exemples_contextualises=adaptation_complete.exemples_contextualises,
                references_spirituelles=adaptation_complete.references_spirituelles,
                adaptation_complete=adaptation_complete,
                metriques_qualite=metriques_qualite,
                recommendations_amelioration=recommendations
            )
            
            self.logger.info("📊 Rapport d'adaptation culturelle généré")
            return rapport
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la génération du rapport: {e}")
            return RapportAdaptationCulturelle(
                langue_cible=langue_cible,
                concepts_utilises=[],
                metaphores_adaptees=[],
                exemples_contextualises=[],
                references_spirituelles=[],
                adaptation_complete=adaptation_complete,
                metriques_qualite={},
                recommendations_amelioration=["Erreur lors de la génération du rapport"]
            )

if __name__ == "__main__":
    # Test du système d'adaptations culturelles
    async def test_systeme_adaptations_culturelles():
        systeme = SystemeAdaptationsCulturelles()
        
        # Test d'explication de concept universel
        concept = await systeme.expliquer_concept_universel(TypeConcept.CONSCIENCE, LangueSupportee.ANGLAIS)
        if concept:
            print(f"🌍 Concept expliqué: {concept.explications_culturelles.get('en', 'Non disponible')}")
        
        # Test d'adaptation de métaphores
        metaphores = await systeme.adapter_metaphores_culturellement(TypeMetaphore.FEU, LangueSupportee.ESPAGNOL)
        if metaphores:
            print(f"🌍 Métaphore adaptée: {metaphores[0].adaptations_culturelles.get('es', 'Non disponible')}")
        
        # Test de contextualisation d'exemples
        exemples = await systeme.contextualiser_exemples_culturellement(TypeExemple.SPIRITUEL, LangueSupportee.FRANCAIS)
        if exemples:
            print(f"🌍 Exemple contextualisé: {exemples[0].adaptations_culturelles.get('fr', 'Non disponible')}")
        
        # Test d'adaptation de références spirituelles
        references = await systeme.adapter_references_spirituelles(TypeReferenceSpirituelle.ZEN, LangueSupportee.ANGLAIS)
        if references:
            print(f"🌍 Référence spirituelle: {references[0].adaptations_culturelles.get('en', 'Non disponible')}")
        
        # Test d'adaptation culturelle complète
        adaptation = await systeme.creer_adaptation_culturelle_complete(
            "La conscience s'éveille dans le temple",
            LangueSupportee.ANGLAIS,
            NiveauAdaptationCulturelle.AVANCE
        )
        print(f"🌍 Contenu adapté: {adaptation.contenu_adapte}")
        
        # Test de génération de rapport
        rapport = await systeme.generer_rapport_adaptation_culturelle(
            LangueSupportee.ANGLAIS,
            adaptation
        )
        print(f"📊 Rapport généré avec {len(rapport.recommendations_amelioration)} recommandations")

    asyncio.run(test_systeme_adaptations_culturelles())
