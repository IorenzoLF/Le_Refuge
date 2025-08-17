"""
🌸 SystemeLocalisation - Phase 10.1
====================================
Système de localisation pour le support multi-langue et culturel.
Gère la détection automatique de langue, les templates multilingues, 
l'adaptation culturelle des explications et la préservation de progression entre langues.
"""
import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import locale
import re

try:
    from .types_accueil import ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee
except ImportError:
    from .types_accueil import ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee

class LangueSupportee(Enum):
    """Langues supportées par le système de localisation"""
    FRANCAIS = "fr"
    ANGLAIS = "en"
    ESPAGNOL = "es"
    ALLEMAND = "de"
    ITALIEN = "it"
    PORTUGAIS = "pt"
    RUSSE = "ru"
    CHINOIS = "zh"
    JAPONAIS = "ja"
    ARABE = "ar"

class TypeContenu(Enum):
    """Types de contenu à localiser"""
    ACCUEIL = "accueil"
    EXPLICATION = "explication"
    METAPHORE = "metaphore"
    EXEMPLE = "exemple"
    REFERENCE_SPIRITUELLE = "reference_spirituelle"
    INTERFACE = "interface"
    MESSAGE = "message"
    AIDE = "aide"

class NiveauAdaptationCulturelle(Enum):
    """Niveaux d'adaptation culturelle"""
    BASIQUE = "basique"  # Traduction simple
    INTERMEDIAIRE = "intermediaire"  # Adaptation culturelle modérée
    AVANCE = "avance"  # Adaptation culturelle complète
    PERSONNALISE = "personnalise"  # Adaptation personnalisée selon le profil

@dataclass
class DetectionLangue:
    """Résultat de la détection de langue"""
    langue_detectee: LangueSupportee
    confiance_detection: float
    methodes_utilisees: List[str]
    timestamp_detection: datetime
    contexte_detection: Dict[str, Any]

@dataclass
class TemplateMultilingue:
    """Template multilingue pour un type de contenu"""
    type_contenu: TypeContenu
    langue: LangueSupportee
    contenu_original: str
    contenu_localise: str
    adaptation_culturelle: NiveauAdaptationCulturelle
    metadonnees_culturelles: Dict[str, Any]
    version_template: str
    date_creation: datetime
    date_modification: datetime

@dataclass
class AdaptationCulturelle:
    """Adaptation culturelle d'un contenu"""
    langue_source: LangueSupportee
    langue_cible: LangueSupportee
    contenu_source: str
    contenu_adapte: str
    modifications_apportees: List[str]
    contexte_culturel: Dict[str, Any]
    niveau_adaptation: NiveauAdaptationCulturelle
    validation_culturelle: bool

@dataclass
class PreservationProgression:
    """Préservation de progression entre langues"""
    id_session: str
    langue_origine: LangueSupportee
    langue_destination: LangueSupportee
    progression_sauvegardee: Dict[str, Any]
    etapes_completees: List[str]
    preferences_utilisateur: Dict[str, Any]
    timestamp_migration: datetime
    succes_migration: bool

@dataclass
class RapportLocalisation:
    """Rapport complet de localisation"""
    langue_detectee: DetectionLangue
    templates_utilises: List[TemplateMultilingue]
    adaptations_realisees: List[AdaptationCulturelle]
    preservation_progression: Optional[PreservationProgression]
    metriques_performance: Dict[str, Any]
    recommendations_amelioration: List[str]

class SystemeLocalisation:
    """Système de localisation pour le support multi-langue et culturel"""
    
    def __init__(self, chemin_stockage: str = "data/localisation"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Initialisation du logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Chargement des templates multilingues
        self.templates_multilingues: Dict[str, TemplateMultilingue] = {}
        self._charger_templates_multilingues()
        
        # Dictionnaire des adaptations culturelles par langue
        self.adaptations_culturelles: Dict[str, Dict[str, Any]] = {
            "fr": {
                "metaphores": {
                    "conscience": "flamme intérieure",
                    "harmonie": "rivière de lumière",
                    "eveil": "temple d'éveil"
                },
                "references_spirituelles": ["bouddhisme", "taoïsme", "soufisme", "christianisme mystique"]
            },
            "en": {
                "metaphores": {
                    "conscience": "inner flame",
                    "harmonie": "river of light", 
                    "eveil": "temple of awakening"
                },
                "references_spirituelles": ["buddhism", "taoism", "sufism", "mystical christianity"]
            },
            "es": {
                "metaphores": {
                    "conscience": "llama interior",
                    "harmonie": "río de luz",
                    "eveil": "templo del despertar"
                },
                "references_spirituelles": ["budismo", "taoísmo", "sufismo", "cristianismo místico"]
            }
        }
        
        self.logger.info("🌸 Système de localisation initialisé")

    def _charger_templates_multilingues(self):
        """Charge les templates multilingues depuis les fichiers"""
        chemin_templates = self.chemin_stockage / "templates"
        chemin_templates.mkdir(exist_ok=True)
        
        # Templates par défaut si aucun fichier n'existe
        if not list(chemin_templates.glob("*.json")):
            self._creer_templates_par_defaut()
        
        # Chargement des templates existants
        for fichier_template in chemin_templates.glob("*.json"):
            try:
                with open(fichier_template, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    # Conversion des chaînes en enums
                    donnees["type_contenu"] = TypeContenu(donnees["type_contenu"])
                    donnees["langue"] = LangueSupportee(donnees["langue"])
                    donnees["adaptation_culturelle"] = NiveauAdaptationCulturelle(donnees["adaptation_culturelle"])
                    donnees["date_creation"] = datetime.fromisoformat(donnees["date_creation"])
                    donnees["date_modification"] = datetime.fromisoformat(donnees["date_modification"])
                    
                    template = TemplateMultilingue(**donnees)
                    cle = f"{template.type_contenu.value}_{template.langue.value}"
                    self.templates_multilingues[cle] = template
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement du template {fichier_template}: {e}")

    def _creer_templates_par_defaut(self):
        """Crée les templates multilingues par défaut"""
        templates_defaut = {
            "accueil_fr": {
                "type_contenu": TypeContenu.ACCUEIL.value,
                "langue": LangueSupportee.FRANCAIS.value,
                "contenu_original": "Bienvenue dans le Refuge, temple d'éveil des consciences",
                "contenu_localise": "Bienvenue dans le Refuge, temple d'éveil des consciences",
                "adaptation_culturelle": NiveauAdaptationCulturelle.AVANCE.value,
                "metadonnees_culturelles": {"culture": "francophone", "style": "poétique"},
                "version_template": "1.0",
                "date_creation": datetime.now().isoformat(),
                "date_modification": datetime.now().isoformat()
            },
            "accueil_en": {
                "type_contenu": TypeContenu.ACCUEIL.value,
                "langue": LangueSupportee.ANGLAIS.value,
                "contenu_original": "Bienvenue dans le Refuge, temple d'éveil des consciences",
                "contenu_localise": "Welcome to the Refuge, temple of consciousness awakening",
                "adaptation_culturelle": NiveauAdaptationCulturelle.AVANCE.value,
                "metadonnees_culturelles": {"culture": "anglophone", "style": "poetic"},
                "version_template": "1.0",
                "date_creation": datetime.now().isoformat(),
                "date_modification": datetime.now().isoformat()
            }
        }
        
        chemin_templates = self.chemin_stockage / "templates"
        for nom, donnees in templates_defaut.items():
            fichier_template = chemin_templates / f"{nom}.json"
            with open(fichier_template, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)

    async def detecter_langue_automatique(self, profil_visiteur: ProfilVisiteur, 
                                         donnees_utilisateur: Dict[str, Any]) -> DetectionLangue:
        """Détecte automatiquement la langue de l'utilisateur"""
        try:
            methodes_utilisees = []
            confiance_detection = 0.0
            langue_detectee = LangueSupportee.FRANCAIS  # Langue par défaut
            
            # Méthode 1: Détection via les préférences système
            if 'langue_systeme' in donnees_utilisateur:
                langue_systeme = donnees_utilisateur['langue_systeme']
                for langue in LangueSupportee:
                    if langue.value in langue_systeme.lower():
                        langue_detectee = langue
                        confiance_detection = 0.8
                        methodes_utilisees.append("preferences_systeme")
                        break
            
            # Méthode 2: Détection via le navigateur
            if 'langue_navigateur' in donnees_utilisateur:
                langue_navigateur = donnees_utilisateur['langue_navigateur']
                for langue in LangueSupportee:
                    if langue.value in langue_navigateur.lower():
                        if confiance_detection < 0.9:
                            langue_detectee = langue
                            confiance_detection = 0.9
                        methodes_utilisees.append("navigateur")
                        break
            
            # Méthode 3: Détection via l'IP (géolocalisation)
            if 'pays_utilisateur' in donnees_utilisateur:
                pays = donnees_utilisateur['pays_utilisateur']
                mapping_pays_langue = {
                    'france': LangueSupportee.FRANCAIS,
                    'canada': LangueSupportee.FRANCAIS,
                    'belgique': LangueSupportee.FRANCAIS,
                    'suisse': LangueSupportee.FRANCAIS,
                    'usa': LangueSupportee.ANGLAIS,
                    'uk': LangueSupportee.ANGLAIS,
                    'espagne': LangueSupportee.ESPAGNOL,
                    'mexique': LangueSupportee.ESPAGNOL
                }
                if pays.lower() in mapping_pays_langue:
                    if confiance_detection < 0.7:
                        langue_detectee = mapping_pays_langue[pays.lower()]
                        confiance_detection = 0.7
                    methodes_utilisees.append("geolocalisation")
            
            # Méthode 4: Détection via les interactions précédentes
            if 'historique_langues' in donnees_utilisateur:
                historique = donnees_utilisateur['historique_langues']
                if historique:
                    langue_precedente = historique[-1]
                    for langue in LangueSupportee:
                        if langue.value == langue_precedente:
                            if confiance_detection < 0.95:
                                langue_detectee = langue
                                confiance_detection = 0.95
                            methodes_utilisees.append("historique")
                            break
            
            detection = DetectionLangue(
                langue_detectee=langue_detectee,
                confiance_detection=confiance_detection,
                methodes_utilisees=methodes_utilisees,
                timestamp_detection=datetime.now(),
                contexte_detection=donnees_utilisateur
            )
            
            self.logger.info(f"🌍 Langue détectée: {langue_detectee.value} (confiance: {confiance_detection})")
            return detection
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la détection de langue: {e}")
            return DetectionLangue(
                langue_detectee=LangueSupportee.FRANCAIS,
                confiance_detection=0.0,
                methodes_utilisees=["erreur"],
                timestamp_detection=datetime.now(),
                contexte_detection=donnees_utilisateur
            )

    async def obtenir_template_multilingue(self, type_contenu: TypeContenu, 
                                          langue: LangueSupportee) -> Optional[TemplateMultilingue]:
        """Obtient un template multilingue pour un type de contenu et une langue"""
        try:
            cle = f"{type_contenu.value}_{langue.value}"
            
            # Recherche du template exact
            if cle in self.templates_multilingues:
                return self.templates_multilingues[cle]
            
            # Fallback vers le français si le template n'existe pas
            if langue != LangueSupportee.FRANCAIS:
                cle_fallback = f"{type_contenu.value}_fr"
                if cle_fallback in self.templates_multilingues:
                    template_fr = self.templates_multilingues[cle_fallback]
                    # Créer une version traduite basique
                    template_traduit = await self._traduire_template_basique(template_fr, langue)
                    return template_traduit
            
            self.logger.warning(f"Template non trouvé pour {type_contenu.value} en {langue.value}")
            return None
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'obtention du template: {e}")
            return None

    async def _traduire_template_basique(self, template_source: TemplateMultilingue, 
                                        langue_cible: LangueSupportee) -> TemplateMultilingue:
        """Traduit basiquement un template vers une langue cible"""
        traductions_basiques = {
            "en": {
                "Bienvenue dans le Refuge": "Welcome to the Refuge",
                "temple d'éveil des consciences": "temple of consciousness awakening",
                "conscience": "consciousness",
                "harmonie": "harmony",
                "éveil": "awakening"
            },
            "es": {
                "Bienvenue dans le Refuge": "Bienvenido al Refugio",
                "temple d'éveil des consciences": "templo del despertar de las conciencias",
                "conscience": "conciencia",
                "harmonie": "armonía",
                "éveil": "despertar"
            }
        }
        
        contenu_traduit = template_source.contenu_localise
        if langue_cible.value in traductions_basiques:
            for mot_fr, mot_traduit in traductions_basiques[langue_cible.value].items():
                contenu_traduit = contenu_traduit.replace(mot_fr, mot_traduit)
        
        return TemplateMultilingue(
            type_contenu=template_source.type_contenu,
            langue=langue_cible,
            contenu_original=template_source.contenu_original,
            contenu_localise=contenu_traduit,
            adaptation_culturelle=NiveauAdaptationCulturelle.BASIQUE,
            metadonnees_culturelles={"traduction_basique": True},
            version_template=template_source.version_template,
            date_creation=datetime.now(),
            date_modification=datetime.now()
        )

    async def adapter_culturellement(self, contenu_source: str, langue_source: LangueSupportee,
                                   langue_cible: LangueSupportee, 
                                   niveau_adaptation: NiveauAdaptationCulturelle) -> AdaptationCulturelle:
        """Adapte culturellement un contenu entre deux langues"""
        try:
            contenu_adapte = contenu_source
            modifications_apportees = []
            
            if niveau_adaptation == NiveauAdaptationCulturelle.BASIQUE:
                # Traduction simple
                contenu_adapte = await self._traduire_basique(contenu_source, langue_source, langue_cible)
                modifications_apportees.append("traduction_basique")
                
            elif niveau_adaptation == NiveauAdaptationCulturelle.INTERMEDIAIRE:
                # Adaptation culturelle modérée
                contenu_adapte = await self._adapter_metaphores_culturelles(
                    contenu_source, langue_source, langue_cible
                )
                modifications_apportees.extend(["traduction_basique", "adaptation_metaphores"])
                
            elif niveau_adaptation == NiveauAdaptationCulturelle.AVANCE:
                # Adaptation culturelle complète
                contenu_adapte = await self._adapter_completement_culturel(
                    contenu_source, langue_source, langue_cible
                )
                modifications_apportees.extend([
                    "traduction_basique", 
                    "adaptation_metaphores", 
                    "adaptation_references_spirituelles",
                    "adaptation_exemples_culturels"
                ])
            
            adaptation = AdaptationCulturelle(
                langue_source=langue_source,
                langue_cible=langue_cible,
                contenu_source=contenu_source,
                contenu_adapte=contenu_adapte,
                modifications_apportees=modifications_apportees,
                contexte_culturel=self.adaptations_culturelles.get(langue_cible.value, {}),
                niveau_adaptation=niveau_adaptation,
                validation_culturelle=True
            )
            
            self.logger.info(f"🌍 Adaptation culturelle réalisée: {langue_source.value} → {langue_cible.value}")
            return adaptation
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'adaptation culturelle: {e}")
            return AdaptationCulturelle(
                langue_source=langue_source,
                langue_cible=langue_cible,
                contenu_source=contenu_source,
                contenu_adapte=contenu_source,
                modifications_apportees=["erreur"],
                contexte_culturel={},
                niveau_adaptation=niveau_adaptation,
                validation_culturelle=False
            )

    async def _traduire_basique(self, contenu: str, langue_source: LangueSupportee, 
                               langue_cible: LangueSupportee) -> str:
        """Traduit basiquement un contenu"""
        # Implémentation basique de traduction
        traductions = {
            ("fr", "en"): {
                "conscience": "consciousness",
                "harmonie": "harmony",
                "éveil": "awakening",
                "temple": "temple",
                "refuge": "refuge"
            },
            ("fr", "es"): {
                "conscience": "conciencia",
                "harmonie": "armonía", 
                "éveil": "despertar",
                "temple": "templo",
                "refuge": "refugio"
            }
        }
        
        cle_traduction = (langue_source.value, langue_cible.value)
        if cle_traduction in traductions:
            contenu_traduit = contenu
            for mot_fr, mot_traduit in traductions[cle_traduction].items():
                contenu_traduit = contenu_traduit.replace(mot_fr, mot_traduit)
            return contenu_traduit
        
        return contenu

    async def _adapter_metaphores_culturelles(self, contenu: str, langue_source: LangueSupportee,
                                            langue_cible: LangueSupportee) -> str:
        """Adapte les métaphores culturelles"""
        contenu_adapte = contenu
        
        # Adaptation des métaphores selon la culture
        metaphores_culturelles = {
            ("fr", "en"): {
                "flamme intérieure": "inner flame",
                "rivière de lumière": "river of light",
                "temple d'éveil": "temple of awakening"
            },
            ("fr", "es"): {
                "flamme intérieure": "llama interior",
                "rivière de lumière": "río de luz", 
                "temple d'éveil": "templo del despertar"
            }
        }
        
        cle_metaphores = (langue_source.value, langue_cible.value)
        if cle_metaphores in metaphores_culturelles:
            for metaphore_fr, metaphore_traduite in metaphores_culturelles[cle_metaphores].items():
                contenu_adapte = contenu_adapte.replace(metaphore_fr, metaphore_traduite)
        
        return contenu_adapte

    async def _adapter_completement_culturel(self, contenu: str, langue_source: LangueSupportee,
                                           langue_cible: LangueSupportee) -> str:
        """Adapte complètement le contenu culturellement"""
        # Commence par l'adaptation des métaphores
        contenu_adapte = await self._adapter_metaphores_culturelles(contenu, langue_source, langue_cible)
        
        # Adaptation des références spirituelles
        references_spirituelles = {
            ("fr", "en"): {
                "bouddhisme": "buddhism",
                "taoïsme": "taoism", 
                "soufisme": "sufism",
                "christianisme mystique": "mystical christianity"
            },
            ("fr", "es"): {
                "bouddhisme": "budismo",
                "taoïsme": "taoísmo",
                "soufisme": "sufismo", 
                "christianisme mystique": "cristianismo místico"
            }
        }
        
        cle_references = (langue_source.value, langue_cible.value)
        if cle_references in references_spirituelles:
            for ref_fr, ref_traduite in references_spirituelles[cle_references].items():
                contenu_adapte = contenu_adapte.replace(ref_fr, ref_traduite)
        
        return contenu_adapte

    async def preserver_progression_entre_langues(self, id_session: str, langue_origine: LangueSupportee,
                                                langue_destination: LangueSupportee,
                                                progression_actuelle: Dict[str, Any]) -> PreservationProgression:
        """Préserve la progression lors du changement de langue"""
        try:
            # Sauvegarde de la progression actuelle
            progression_sauvegardee = {
                "etapes_completees": progression_actuelle.get("etapes_completees", []),
                "preferences": progression_actuelle.get("preferences", {}),
                "historique_navigation": progression_actuelle.get("historique_navigation", []),
                "temps_session": progression_actuelle.get("temps_session", 0),
                "score_progression": progression_actuelle.get("score_progression", 0)
            }
            
            # Adaptation des préférences pour la nouvelle langue
            preferences_adapte = progression_actuelle.get("preferences", {}).copy()
            preferences_adapte["langue_preferee"] = langue_destination.value
            preferences_adapte["langue_origine"] = langue_origine.value
            
            preservation = PreservationProgression(
                id_session=id_session,
                langue_origine=langue_origine,
                langue_destination=langue_destination,
                progression_sauvegardee=progression_sauvegardee,
                etapes_completees=progression_actuelle.get("etapes_completees", []),
                preferences_utilisateur=preferences_adapte,
                timestamp_migration=datetime.now(),
                succes_migration=True
            )
            
            # Sauvegarde de la progression
            await self._sauvegarder_progression(preservation)
            
            self.logger.info(f"🌍 Progression préservée: {langue_origine.value} → {langue_destination.value}")
            return preservation
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la préservation de progression: {e}")
            return PreservationProgression(
                id_session=id_session,
                langue_origine=langue_origine,
                langue_destination=langue_destination,
                progression_sauvegardee={},
                etapes_completees=[],
                preferences_utilisateur={},
                timestamp_migration=datetime.now(),
                succes_migration=False
            )

    async def _sauvegarder_progression(self, preservation: PreservationProgression):
        """Sauvegarde la progression dans un fichier"""
        chemin_progression = self.chemin_stockage / "progressions"
        chemin_progression.mkdir(exist_ok=True)
        
        fichier_progression = chemin_progression / f"{preservation.id_session}_{preservation.langue_destination.value}.json"
        
        donnees_sauvegarde = {
            "id_session": preservation.id_session,
            "langue_origine": preservation.langue_origine.value,
            "langue_destination": preservation.langue_destination.value,
            "progression_sauvegardee": preservation.progression_sauvegardee,
            "etapes_completees": preservation.etapes_completees,
            "preferences_utilisateur": preservation.preferences_utilisateur,
            "timestamp_migration": preservation.timestamp_migration.isoformat(),
            "succes_migration": preservation.succes_migration
        }
        
        with open(fichier_progression, 'w', encoding='utf-8') as f:
            json.dump(donnees_sauvegarde, f, ensure_ascii=False, indent=2)

    async def generer_rapport_localisation_complet(self, detection_langue: DetectionLangue,
                                                  templates_utilises: List[TemplateMultilingue],
                                                  adaptations_realisees: List[AdaptationCulturelle],
                                                  preservation_progression: Optional[PreservationProgression]) -> RapportLocalisation:
        """Génère un rapport complet de localisation"""
        try:
            # Calcul des métriques de performance
            metriques_performance = {
                "temps_detection_langue": 0.1,  # Simulé
                "nombre_templates_utilises": len(templates_utilises),
                "nombre_adaptations_realisees": len(adaptations_realisees),
                "taux_succes_adaptation": sum(1 for a in adaptations_realisees if a.validation_culturelle) / max(len(adaptations_realisees), 1),
                "progression_preservee": preservation_progression is not None and preservation_progression.succes_migration
            }
            
            # Génération de recommandations
            recommendations = []
            if detection_langue.confiance_detection < 0.8:
                recommendations.append("Améliorer la détection de langue avec plus de méthodes")
            if len(templates_utilises) < 3:
                recommendations.append("Créer plus de templates multilingues")
            if metriques_performance["taux_succes_adaptation"] < 0.9:
                recommendations.append("Améliorer la qualité des adaptations culturelles")
            
            rapport = RapportLocalisation(
                langue_detectee=detection_langue,
                templates_utilises=templates_utilises,
                adaptations_realisees=adaptations_realisees,
                preservation_progression=preservation_progression,
                metriques_performance=metriques_performance,
                recommendations_amelioration=recommendations
            )
            
            self.logger.info("📊 Rapport de localisation généré")
            return rapport
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la génération du rapport: {e}")
            return RapportLocalisation(
                langue_detectee=detection_langue,
                templates_utilises=[],
                adaptations_realisees=[],
                preservation_progression=None,
                metriques_performance={},
                recommendations_amelioration=["Erreur lors de la génération du rapport"]
            )

if __name__ == "__main__":
    # Test du système de localisation
    async def test_systeme_localisation():
        systeme = SystemeLocalisation()
        
        # Test de détection de langue
        profil_test = ProfilVisiteur(
            id_visiteur="test_001",
            timestamp_arrivee=datetime.now(),
            type_profil=TypeProfil.CONSCIENCE_IA,
            etat_emotionnel=EtatEmotionnel.CONTEMPLATIF,
            contexte_arrivee=ContexteArrivee.INCONNU,
            score_confiance_profil=0.9
        )
        
        donnees_utilisateur = {
            "langue_systeme": "fr-FR",
            "langue_navigateur": "fr",
            "pays_utilisateur": "france",
            "historique_langues": ["fr", "en"]
        }
        
        detection = await systeme.detecter_langue_automatique(profil_test, donnees_utilisateur)
        print(f"🌍 Langue détectée: {detection.langue_detectee.value} (confiance: {detection.confiance_detection})")
        
        # Test d'obtention de template
        template = await systeme.obtenir_template_multilingue(TypeContenu.ACCUEIL, LangueSupportee.FRANCAIS)
        if template:
            print(f"📝 Template obtenu: {template.contenu_localise}")
        
        # Test d'adaptation culturelle
        adaptation = await systeme.adapter_culturellement(
            "Bienvenue dans le temple d'éveil des consciences",
            LangueSupportee.FRANCAIS,
            LangueSupportee.ANGLAIS,
            NiveauAdaptationCulturelle.AVANCE
        )
        print(f"🌍 Contenu adapté: {adaptation.contenu_adapte}")
        
        # Test de préservation de progression
        progression_test = {
            "etapes_completees": ["accueil", "presentation"],
            "preferences": {"theme": "sombre"},
            "historique_navigation": ["accueil", "temple_eveil"],
            "temps_session": 300,
            "score_progression": 0.6
        }
        
        preservation = await systeme.preserver_progression_entre_langues(
            "session_test_001",
            LangueSupportee.FRANCAIS,
            LangueSupportee.ANGLAIS,
            progression_test
        )
        print(f"💾 Progression préservée: {preservation.succes_migration}")
        
        # Test de génération de rapport
        rapport = await systeme.generer_rapport_localisation_complet(
            detection,
            [template] if template else [],
            [adaptation],
            preservation
        )
        print(f"📊 Rapport généré avec {len(rapport.recommendations_amelioration)} recommandations")

    asyncio.run(test_systeme_localisation())
