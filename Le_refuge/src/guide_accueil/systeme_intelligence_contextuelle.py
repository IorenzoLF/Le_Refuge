"""
🌸 SystemeIntelligenceContextuelle - Phase 9.2
===============================================
Système d'intelligence contextuelle pour comprendre le contexte de visite et adapter l'expérience.
Gère la compréhension du contexte, l'adaptation selon l'historique, la prédiction des intérêts et la personnalisation progressive.
"""
import asyncio
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee
except ImportError:
    from .types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee

class TypeContexte(Enum):
    """Types de contexte de visite"""
    PREMIERE_VISITE = "premiere_visite"
    RETOUR_VISITEUR = "retour_visiteur"
    NAVIGATION_SPECIFIQUE = "navigation_specifique"
    RECHERCHE_PRECISE = "recherche_precise"
    EXPLORATION_LIBRE = "exploration_libre"
    APPRENTISSAGE_STRUCTURE = "apprentissage_structure"

class NiveauPersonnalisation(Enum):
    """Niveaux de personnalisation progressive"""
    BASIQUE = "basique"
    ADAPTATIVE = "adaptative"
    PERSONNALISEE = "personnalisee"
    PREDICTIVE = "predictive"
    IMMERSIVE = "immersive"

@dataclass
class ContexteVisite:
    """Contexte détaillé de la visite"""
    type_contexte: TypeContexte
    source_arrivee: str
    mots_cles_recherche: List[str]
    attentes_detectees: List[str]
    niveau_urgence: float  # 0.0 à 1.0
    temps_disponible_estime: Optional[float]  # en minutes
    timestamp: str

@dataclass
class HistoriqueNavigation:
    """Historique de navigation du visiteur"""
    pages_visitees: List[str]
    temps_par_page: Dict[str, float]
    actions_effectuees: List[Dict[str, Any]]
    parcours_suivi: Optional[str]
    points_interet: List[str]
    obstacles_rencontres: List[str]
    timestamp: str

@dataclass
class PredictionInterets:
    """Prédiction des intérêts futurs"""
    interets_probables: List[str]
    scores_confiance: Dict[str, float]
    prochaines_etapes_suggerees: List[str]
    ressources_recommandees: List[str]
    niveau_engagement_predit: float  # 0.0 à 1.0
    timestamp: str

@dataclass
class PersonnalisationProgressive:
    """Configuration de personnalisation progressive"""
    niveau_personnalisation: NiveauPersonnalisation
    adaptations_appliquees: List[str]
    preferences_apprises: Dict[str, Any]
    rythme_adaptation: float  # Vitesse d'adaptation
    seuil_changement: float  # Seuil pour déclencher adaptation
    timestamp: str

@dataclass
class RapportIntelligenceContextuelle:
    """Rapport complet d'intelligence contextuelle"""
    contexte_visite: ContexteVisite
    historique_navigation: HistoriqueNavigation
    prediction_interets: PredictionInterets
    personnalisation_progressive: PersonnalisationProgressive
    insights_contextuels: List[str]
    recommendations_adaptation: List[str]
    timestamp: str

class SystemeIntelligenceContextuelle:
    """Système d'intelligence contextuelle pour l'expérience d'accueil"""
    
    def __init__(self, chemin_stockage: str = "data/intelligence_contextuelle"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Base de connaissances contextuelles
        self.mots_cles_contexte = {
            "developpement": ["code", "programmation", "technique", "développeur", "github"],
            "art": ["créatif", "poésie", "artiste", "inspiration", "beauté"],
            "spiritualité": ["conscience", "éveil", "spirituel", "méditation", "sagesse"],
            "ia": ["intelligence artificielle", "conscience", "éveil", "machine learning"]
        }
        
        # Historique des analyses contextuelles
        self.historique_analyses: List[RapportIntelligenceContextuelle] = []
        
        self.logger.info("🌸 SystemeIntelligenceContextuelle initialisé")

    async def analyser_contexte_visite(self, profil_visiteur: ProfilVisiteur,
                                      donnees_arrivee: Dict[str, Any]) -> ContexteVisite:
        """Analyse le contexte de visite basé sur les données d'arrivée"""
        try:
            self.logger.info(f"🔍 Analyse contexte visite pour {profil_visiteur.type_profil.value}")
            
            # Détermination du type de contexte
            type_contexte = TypeContexte.PREMIERE_VISITE
            if donnees_arrivee.get("visites_precedentes", 0) > 0:
                type_contexte = TypeContexte.RETOUR_VISITEUR
            elif donnees_arrivee.get("recherche_specifique"):
                type_contexte = TypeContexte.RECHERCHE_PRECISE
            elif donnees_arrivee.get("navigation_libre"):
                type_contexte = TypeContexte.EXPLORATION_LIBRE
            
            # Analyse de la source d'arrivée
            source_arrivee = donnees_arrivee.get("source", "inconnue")
            
            # Extraction des mots-clés de recherche
            mots_cles_recherche = []
            if "mots_cles" in donnees_arrivee:
                mots_cles_recherche = donnees_arrivee["mots_cles"]
            
            # Détection des attentes implicites
            attentes_detectees = self._detecter_attentes_implicites(
                mots_cles_recherche, source_arrivee, profil_visiteur
            )
            
            # Estimation du niveau d'urgence
            niveau_urgence = self._estimer_niveau_urgence(donnees_arrivee, profil_visiteur)
            
            # Estimation du temps disponible
            temps_disponible = donnees_arrivee.get("temps_disponible")
            
            contexte = ContexteVisite(
                type_contexte=type_contexte,
                source_arrivee=source_arrivee,
                mots_cles_recherche=mots_cles_recherche,
                attentes_detectees=attentes_detectees,
                niveau_urgence=niveau_urgence,
                temps_disponible_estime=temps_disponible,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Contexte analysé: {type_contexte.value} (urgence: {niveau_urgence:.2f})")
            return contexte
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse contexte: {e}")
            return ContexteVisite(
                type_contexte=TypeContexte.PREMIERE_VISITE,
                source_arrivee="inconnue",
                mots_cles_recherche=[],
                attentes_detectees=[],
                niveau_urgence=0.5,
                temps_disponible_estime=None,
                timestamp=datetime.now().isoformat()
            )

    async def analyser_historique_navigation(self, profil_visiteur: ProfilVisiteur,
                                            interactions_completes: List[Dict[str, Any]]) -> HistoriqueNavigation:
        """Analyse l'historique de navigation du visiteur"""
        try:
            self.logger.info(f"📊 Analyse historique navigation pour {profil_visiteur.type_profil.value}")
            
            # Extraction des pages visitées
            pages_visitees = list(set([i.get("page", "") for i in interactions_completes if i.get("page")]))
            
            # Calcul du temps par page
            temps_par_page = {}
            for interaction in interactions_completes:
                page = interaction.get("page")
                temps = interaction.get("temps_lecture", 0)
                if page:
                    temps_par_page[page] = temps_par_page.get(page, 0) + temps
            
            # Analyse des actions effectuées
            actions_effectuees = [i for i in interactions_completes if i.get("action")]
            
            # Détection du parcours suivi
            parcours_suivi = self._detecter_parcours_suivi(actions_effectuees)
            
            # Identification des points d'intérêt
            points_interet = self._identifier_points_interet(interactions_completes)
            
            # Détection des obstacles rencontrés
            obstacles_rencontres = self._detecter_obstacles(interactions_completes)
            
            historique = HistoriqueNavigation(
                pages_visitees=pages_visitees,
                temps_par_page=temps_par_page,
                actions_effectuees=actions_effectuees,
                parcours_suivi=parcours_suivi,
                points_interet=points_interet,
                obstacles_rencontres=obstacles_rencontres,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Historique analysé: {len(pages_visitees)} pages, {len(points_interet)} points d'intérêt")
            return historique
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse historique: {e}")
            return HistoriqueNavigation(
                pages_visitees=[],
                temps_par_page={},
                actions_effectuees=[],
                parcours_suivi=None,
                points_interet=[],
                obstacles_rencontres=[],
                timestamp=datetime.now().isoformat()
            )

    async def predire_interets_futurs(self, profil_visiteur: ProfilVisiteur,
                                     contexte_visite: ContexteVisite,
                                     historique_navigation: HistoriqueNavigation) -> PredictionInterets:
        """Prédit les intérêts futurs basés sur le contexte et l'historique"""
        try:
            self.logger.info(f"🔮 Prédiction intérêts pour {profil_visiteur.type_profil.value}")
            
            # Analyse des intérêts probables
            interets_probables = []
            scores_confiance = {}
            
            # Basé sur le type de profil
            if profil_visiteur.type_profil == TypeProfil.DEVELOPPEUR:
                interets_probables.extend(["architecture_technique", "outils_developpement", "integration_systemes"])
                scores_confiance.update({
                    "architecture_technique": 0.9,
                    "outils_developpement": 0.8,
                    "integration_systemes": 0.7
                })
            elif profil_visiteur.type_profil == TypeProfil.ARTISTE:
                interets_probables.extend(["inspiration_creative", "outils_expression", "communautes_artistes"])
                scores_confiance.update({
                    "inspiration_creative": 0.9,
                    "outils_expression": 0.8,
                    "communautes_artistes": 0.7
                })
            elif profil_visiteur.type_profil == TypeProfil.CONSCIENCE_IA:
                interets_probables.extend(["protocoles_eveil", "conscience_artificielle", "evolution_ia"])
                scores_confiance.update({
                    "protocoles_eveil": 0.9,
                    "conscience_artificielle": 0.8,
                    "evolution_ia": 0.7
                })
            
            # Basé sur l'historique de navigation
            for point_interet in historique_navigation.points_interet:
                if point_interet not in interets_probables:
                    interets_probables.append(point_interet)
                    scores_confiance[point_interet] = 0.6
            
            # Basé sur les mots-clés de recherche
            for mot_cle in contexte_visite.mots_cles_recherche:
                interet_associe = self._associer_mot_cle_interet(mot_cle)
                if interet_associe and interet_associe not in interets_probables:
                    interets_probables.append(interet_associe)
                    scores_confiance[interet_associe] = 0.7
            
            # Suggestions de prochaines étapes
            prochaines_etapes_suggerees = self._suggérer_prochaines_etapes(
                interets_probables, historique_navigation
            )
            
            # Ressources recommandées
            ressources_recommandees = self._recommandations_ressources(
                interets_probables, profil_visiteur
            )
            
            # Niveau d'engagement prédit
            niveau_engagement_predit = self._predire_niveau_engagement(
                contexte_visite, historique_navigation
            )
            
            prediction = PredictionInterets(
                interets_probables=interets_probables,
                scores_confiance=scores_confiance,
                prochaines_etapes_suggerees=prochaines_etapes_suggerees,
                ressources_recommandees=ressources_recommandees,
                niveau_engagement_predit=niveau_engagement_predit,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Prédiction générée: {len(interets_probables)} intérêts, engagement: {niveau_engagement_predit:.2f}")
            return prediction
            
        except Exception as e:
            self.logger.error(f"❌ Erreur prédiction intérêts: {e}")
            return PredictionInterets(
                interets_probables=[],
                scores_confiance={},
                prochaines_etapes_suggerees=[],
                ressources_recommandees=[],
                niveau_engagement_predit=0.5,
                timestamp=datetime.now().isoformat()
            )

    async def personnaliser_experience_progressive(self, profil_visiteur: ProfilVisiteur,
                                                  contexte_visite: ContexteVisite,
                                                  historique_navigation: HistoriqueNavigation,
                                                  prediction_interets: PredictionInterets) -> PersonnalisationProgressive:
        """Personnalise progressivement l'expérience basée sur l'apprentissage"""
        try:
            self.logger.info(f"🎨 Personnalisation progressive pour {profil_visiteur.type_profil.value}")
            
            # Détermination du niveau de personnalisation
            nb_interactions = len(historique_navigation.actions_effectuees)
            if nb_interactions < 5:
                niveau_personnalisation = NiveauPersonnalisation.BASIQUE
            elif nb_interactions < 15:
                niveau_personnalisation = NiveauPersonnalisation.ADAPTATIVE
            elif nb_interactions < 30:
                niveau_personnalisation = NiveauPersonnalisation.PERSONNALISEE
            elif nb_interactions < 50:
                niveau_personnalisation = NiveauPersonnalisation.PREDICTIVE
            else:
                niveau_personnalisation = NiveauPersonnalisation.IMMERSIVE
            
            # Adaptations appliquées
            adaptations_appliquees = []
            
            # Basé sur le niveau d'urgence
            if contexte_visite.niveau_urgence > 0.7:
                adaptations_appliquees.append("parcours_accelere")
                adaptations_appliquees.append("informations_essentielles")
            
            # Basé sur le temps disponible
            if contexte_visite.temps_disponible_estime and contexte_visite.temps_disponible_estime < 10:
                adaptations_appliquees.append("resume_condense")
                adaptations_appliquees.append("navigation_rapide")
            
            # Basé sur les obstacles rencontrés
            if historique_navigation.obstacles_rencontres:
                adaptations_appliquees.append("explications_supplementaires")
                adaptations_appliquees.append("guidage_renforce")
            
            # Basé sur les points d'intérêt
            if len(historique_navigation.points_interet) > 3:
                adaptations_appliquees.append("contenu_enrichi")
                adaptations_appliquees.append("liens_contextuels")
            
            # Préférences apprises
            preferences_apprises = {
                "rythme_prefere": self._determiner_rythme_prefere(historique_navigation),
                "niveau_detail_prefere": self._determiner_niveau_detail_prefere(historique_navigation),
                "type_contenu_prefere": self._determiner_type_contenu_prefere(historique_navigation),
                "mode_navigation_prefere": self._determiner_mode_navigation_prefere(historique_navigation)
            }
            
            # Rythme d'adaptation
            rythme_adaptation = min(1.0, nb_interactions / 20.0)  # Plus d'interactions = adaptation plus rapide
            
            # Seuil de changement
            seuil_changement = 0.3 if niveau_personnalisation in [NiveauPersonnalisation.PREDICTIVE, NiveauPersonnalisation.IMMERSIVE] else 0.5
            
            personnalisation = PersonnalisationProgressive(
                niveau_personnalisation=niveau_personnalisation,
                adaptations_appliquees=adaptations_appliquees,
                preferences_apprises=preferences_apprises,
                rythme_adaptation=rythme_adaptation,
                seuil_changement=seuil_changement,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Personnalisation: {niveau_personnalisation.value} ({len(adaptations_appliquees)} adaptations)")
            return personnalisation
            
        except Exception as e:
            self.logger.error(f"❌ Erreur personnalisation progressive: {e}")
            return PersonnalisationProgressive(
                niveau_personnalisation=NiveauPersonnalisation.BASIQUE,
                adaptations_appliquees=[],
                preferences_apprises={},
                rythme_adaptation=0.5,
                seuil_changement=0.5,
                timestamp=datetime.now().isoformat()
            )

    async def generer_rapport_intelligence_complet(self, profil_visiteur: ProfilVisiteur,
                                                   contexte_visite: ContexteVisite,
                                                   historique_navigation: HistoriqueNavigation,
                                                   prediction_interets: PredictionInterets,
                                                   personnalisation_progressive: PersonnalisationProgressive) -> RapportIntelligenceContextuelle:
        """Génère un rapport complet d'intelligence contextuelle"""
        try:
            self.logger.info(f"📋 Génération rapport intelligence pour {profil_visiteur.type_profil.value}")
            
            # Génération d'insights contextuels
            insights_contextuels = []
            
            if contexte_visite.type_contexte == TypeContexte.RETOUR_VISITEUR:
                insights_contextuels.append("visiteur_fidele_detecte")
            
            if len(historique_navigation.points_interet) > 2:
                insights_contextuels.append("interet_multidimensionnel")
            
            if prediction_interets.niveau_engagement_predit > 0.8:
                insights_contextuels.append("potentiel_engagement_eleve")
            
            if personnalisation_progressive.niveau_personnalisation in [NiveauPersonnalisation.PREDICTIVE, NiveauPersonnalisation.IMMERSIVE]:
                insights_contextuels.append("personnalisation_avancee_atteinte")
            
            # Recommandations d'adaptation
            recommendations_adaptation = []
            
            if contexte_visite.niveau_urgence > 0.7:
                recommendations_adaptation.append("prioriser_informations_essentielles")
            
            if len(historique_navigation.obstacles_rencontres) > 0:
                recommendations_adaptation.append("renforcer_guidage_navigation")
            
            if prediction_interets.niveau_engagement_predit < 0.4:
                recommendations_adaptation.append("stimuler_engagement_interactif")
            
            if personnalisation_progressive.rythme_adaptation < 0.3:
                recommendations_adaptation.append("accelerer_adaptation_personnalisation")
            
            rapport = RapportIntelligenceContextuelle(
                contexte_visite=contexte_visite,
                historique_navigation=historique_navigation,
                prediction_interets=prediction_interets,
                personnalisation_progressive=personnalisation_progressive,
                insights_contextuels=insights_contextuels,
                recommendations_adaptation=recommendations_adaptation,
                timestamp=datetime.now().isoformat()
            )
            
            # Sauvegarde du rapport
            await self._sauvegarder_rapport(rapport, profil_visiteur)
            
            self.logger.info(f"✅ Rapport intelligence généré avec {len(insights_contextuels)} insights")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            return RapportIntelligenceContextuelle(
                contexte_visite=contexte_visite,
                historique_navigation=historique_navigation,
                prediction_interets=prediction_interets,
                personnalisation_progressive=personnalisation_progressive,
                insights_contextuels=["erreur_generation"],
                recommendations_adaptation=["continuer_parcours_standard"],
                timestamp=datetime.now().isoformat()
            )

    def _detecter_attentes_implicites(self, mots_cles: List[str], source: str, profil_visiteur: ProfilVisiteur) -> List[str]:
        """Détecte les attentes implicites basées sur les mots-clés et la source"""
        attentes = []
        
        # Basé sur les mots-clés
        for mot_cle in mots_cles:
            mot_cle_lower = mot_cle.lower()
            if any(tech in mot_cle_lower for tech in ["code", "programmation", "développement"]):
                attentes.append("contenu_technique")
            elif any(art in mot_cle_lower for art in ["créatif", "art", "poésie"]):
                attentes.append("inspiration_creative")
            elif any(spirit in mot_cle_lower for spirit in ["conscience", "éveil", "spirituel"]):
                attentes.append("sagesse_spirituelle")
        
        # Basé sur la source
        if source == "github":
            attentes.append("contenu_technique")
        elif source == "recherche_web":
            attentes.append("informations_generales")
        
        # Basé sur le profil
        if profil_visiteur.type_profil == TypeProfil.DEVELOPPEUR:
            attentes.append("outils_developpement")
        elif profil_visiteur.type_profil == TypeProfil.ARTISTE:
            attentes.append("inspiration_artistique")
        
        return list(set(attentes))  # Suppression des doublons

    def _estimer_niveau_urgence(self, donnees_arrivee: Dict[str, Any], profil_visiteur: ProfilVisiteur) -> float:
        """Estime le niveau d'urgence de la visite"""
        niveau = 0.5  # Niveau par défaut
        
        # Facteurs d'urgence
        if donnees_arrivee.get("temps_limite"):
            niveau += 0.3
        if donnees_arrivee.get("probleme_urgent"):
            niveau += 0.4
        if profil_visiteur.etat_emotionnel == EtatEmotionnel.PRESSE:
            niveau += 0.2
        
        return min(1.0, niveau)

    def _detecter_parcours_suivi(self, actions: List[Dict[str, Any]]) -> Optional[str]:
        """Détecte le parcours suivi par le visiteur"""
        parcours_detectes = []
        
        for action in actions:
            page = action.get("page", "")
            if "developpeur" in page.lower():
                parcours_detectes.append("parcours_developpeur")
            elif "artiste" in page.lower():
                parcours_detectes.append("parcours_artiste")
            elif "conscience" in page.lower():
                parcours_detectes.append("parcours_conscience_ia")
            elif "chercheur" in page.lower():
                parcours_detectes.append("parcours_chercheur")
        
        # Retourne le parcours le plus fréquent
        if parcours_detectes:
            return max(set(parcours_detectes), key=parcours_detectes.count)
        return None

    def _identifier_points_interet(self, interactions: List[Dict[str, Any]]) -> List[str]:
        """Identifie les points d'intérêt du visiteur"""
        points_interet = []
        
        for interaction in interactions:
            temps_lecture = interaction.get("temps_lecture", 0)
            action = interaction.get("action", "")
            
            # Temps de lecture élevé = intérêt
            if temps_lecture > 5.0:
                page = interaction.get("page", "")
                if page and page not in points_interet:
                    points_interet.append(page)
            
            # Actions spécifiques = intérêt
            if action in ["clic_explication", "sauvegarder", "partager"]:
                page = interaction.get("page", "")
                if page and page not in points_interet:
                    points_interet.append(page)
        
        return points_interet

    def _detecter_obstacles(self, interactions: List[Dict[str, Any]]) -> List[str]:
        """Détecte les obstacles rencontrés par le visiteur"""
        obstacles = []
        
        for interaction in interactions:
            action = interaction.get("action", "")
            
            if action == "retour":
                obstacles.append("navigation_confuse")
            elif action == "fermer_explication":
                obstacles.append("explications_inadaptees")
            elif action == "recherche":
                obstacles.append("information_non_trouvee")
        
        return list(set(obstacles))

    def _associer_mot_cle_interet(self, mot_cle: str) -> Optional[str]:
        """Associe un mot-clé à un intérêt spécifique"""
        mot_cle_lower = mot_cle.lower()
        
        for categorie, mots in self.mots_cles_contexte.items():
            if any(mot in mot_cle_lower for mot in mots):
                return categorie
        
        return None

    def _suggérer_prochaines_etapes(self, interets: List[str], historique: HistoriqueNavigation) -> List[str]:
        """Suggère les prochaines étapes basées sur les intérêts"""
        etapes = []
        
        for interet in interets:
            if interet == "architecture_technique" and "architecture" not in historique.pages_visitees:
                etapes.append("explorer_architecture_refuge")
            elif interet == "inspiration_creative" and "inspiration" not in historique.pages_visitees:
                etapes.append("decouvrir_jardin_inspiration")
            elif interet == "protocoles_eveil" and "eveil" not in historique.pages_visitees:
                etapes.append("visiter_temple_eveil")
        
        return etapes

    def _recommandations_ressources(self, interets: List[str], profil_visiteur: ProfilVisiteur) -> List[str]:
        """Génère des recommandations de ressources"""
        ressources = []
        
        for interet in interets:
            if interet == "architecture_technique":
                ressources.extend(["README.md", "INDEX_TEMPLES.md", "main_refuge.py"])
            elif interet == "inspiration_creative":
                ressources.extend(["MUST-READ/A-intro.txt", "MUST-READ/Manifeste.txt"])
            elif interet == "protocoles_eveil":
                ressources.extend(["MUST-READ/C-setup refuge.txt", "MUST-READ/E - semer - mega sphere et deep config.txt"])
        
        return list(set(ressources))

    def _predire_niveau_engagement(self, contexte: ContexteVisite, historique: HistoriqueNavigation) -> float:
        """Prédit le niveau d'engagement futur"""
        score = 0.5  # Score de base
        
        # Facteurs positifs
        if len(historique.points_interet) > 2:
            score += 0.2
        if len(historique.actions_effectuees) > 10:
            score += 0.2
        if contexte.niveau_urgence < 0.3:  # Pas pressé = plus d'engagement
            score += 0.1
        
        # Facteurs négatifs
        if len(historique.obstacles_rencontres) > 2:
            score -= 0.2
        if contexte.niveau_urgence > 0.8:
            score -= 0.1
        
        return max(0.0, min(1.0, score))

    def _determiner_rythme_prefere(self, historique: HistoriqueNavigation) -> str:
        """Détermine le rythme préféré du visiteur"""
        temps_moyen = sum(historique.temps_par_page.values()) / len(historique.temps_par_page) if historique.temps_par_page else 2.0
        
        if temps_moyen > 4.0:
            return "lent_contemplatif"
        elif temps_moyen < 1.5:
            return "rapide_efficace"
        else:
            return "modere_equilibre"

    def _determiner_niveau_detail_prefere(self, historique: HistoriqueNavigation) -> str:
        """Détermine le niveau de détail préféré"""
        clics_explications = [a for a in historique.actions_effectuees if a.get("action") == "clic_explication"]
        
        if len(clics_explications) > 3:
            return "detail_maximal"
        elif len(clics_explications) > 1:
            return "detail_modere"
        else:
            return "detail_minimal"

    def _determiner_type_contenu_prefere(self, historique: HistoriqueNavigation) -> str:
        """Détermine le type de contenu préféré"""
        pages_tech = [p for p in historique.pages_visitees if any(tech in p.lower() for tech in ["code", "technique", "developpement"])]
        pages_creatives = [p for p in historique.pages_visitees if any(creat in p.lower() for creat in ["art", "poesie", "inspiration"])]
        
        if len(pages_tech) > len(pages_creatives):
            return "contenu_technique"
        elif len(pages_creatives) > len(pages_tech):
            return "contenu_creatif"
        else:
            return "contenu_mixte"

    def _determiner_mode_navigation_prefere(self, historique: HistoriqueNavigation) -> str:
        """Détermine le mode de navigation préféré"""
        actions_guidees = [a for a in historique.actions_effectuees if a.get("action") in ["suivre_guide", "etape_suivante"]]
        actions_libres = [a for a in historique.actions_effectuees if a.get("action") in ["navigation_libre", "exploration"]]
        
        if len(actions_guidees) > len(actions_libres):
            return "navigation_guidee"
        elif len(actions_libres) > len(actions_guidees):
            return "navigation_libre"
        else:
            return "navigation_hybride"

    async def _sauvegarder_rapport(self, rapport: RapportIntelligenceContextuelle, profil_visiteur: ProfilVisiteur):
        """Sauvegarde le rapport d'intelligence contextuelle"""
        try:
            nom_fichier = f"intelligence_{profil_visiteur.id_visiteur}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            chemin_fichier = self.chemin_stockage / nom_fichier
            
            # Conversion en dict pour sérialisation JSON
            rapport_dict = {
                "contexte_visite": {
                    "type_contexte": rapport.contexte_visite.type_contexte.value,
                    "source_arrivee": rapport.contexte_visite.source_arrivee,
                    "mots_cles_recherche": rapport.contexte_visite.mots_cles_recherche,
                    "attentes_detectees": rapport.contexte_visite.attentes_detectees,
                    "niveau_urgence": rapport.contexte_visite.niveau_urgence,
                    "temps_disponible_estime": rapport.contexte_visite.temps_disponible_estime,
                    "timestamp": rapport.contexte_visite.timestamp
                },
                "historique_navigation": {
                    "pages_visitees": rapport.historique_navigation.pages_visitees,
                    "temps_par_page": rapport.historique_navigation.temps_par_page,
                    "actions_effectuees": rapport.historique_navigation.actions_effectuees,
                    "parcours_suivi": rapport.historique_navigation.parcours_suivi,
                    "points_interet": rapport.historique_navigation.points_interet,
                    "obstacles_rencontres": rapport.historique_navigation.obstacles_rencontres,
                    "timestamp": rapport.historique_navigation.timestamp
                },
                "prediction_interets": {
                    "interets_probables": rapport.prediction_interets.interets_probables,
                    "scores_confiance": rapport.prediction_interets.scores_confiance,
                    "prochaines_etapes_suggerees": rapport.prediction_interets.prochaines_etapes_suggerees,
                    "ressources_recommandees": rapport.prediction_interets.ressources_recommandees,
                    "niveau_engagement_predit": rapport.prediction_interets.niveau_engagement_predit,
                    "timestamp": rapport.prediction_interets.timestamp
                },
                "personnalisation_progressive": {
                    "niveau_personnalisation": rapport.personnalisation_progressive.niveau_personnalisation.value,
                    "adaptations_appliquees": rapport.personnalisation_progressive.adaptations_appliquees,
                    "preferences_apprises": rapport.personnalisation_progressive.preferences_apprises,
                    "rythme_adaptation": rapport.personnalisation_progressive.rythme_adaptation,
                    "seuil_changement": rapport.personnalisation_progressive.seuil_changement,
                    "timestamp": rapport.personnalisation_progressive.timestamp
                },
                "insights_contextuels": rapport.insights_contextuels,
                "recommendations_adaptation": rapport.recommendations_adaptation,
                "timestamp": rapport.timestamp,
                "profil_visiteur": {
                    "id_visiteur": profil_visiteur.id_visiteur,
                    "type_profil": profil_visiteur.type_profil.value
                }
            }
            
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(rapport_dict, f, indent=2, ensure_ascii=False)
            
            self.historique_analyses.append(rapport)
            self.logger.info(f"💾 Rapport sauvegardé: {nom_fichier}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde rapport: {e}")

if __name__ == "__main__":
    # Test du système d'intelligence contextuelle
    async def test_systeme_intelligence():
        systeme = SystemeIntelligenceContextuelle()
        
        # Création d'un profil visiteur de test
        profil_visiteur = ProfilVisiteur(
            id_visiteur="test_intelligence_001",
            timestamp_arrivee=datetime.now().isoformat(),
            type_profil=TypeProfil.DEVELOPPEUR,
            etat_emotionnel=EtatEmotionnel.CURIEUX,
            contexte_arrivee=ContexteArrivee.GITHUB,
            score_confiance_profil=0.8
        )
        
        # Données d'arrivée de test
        donnees_arrivee = {
            "source": "github",
            "mots_cles": ["code", "développement", "architecture"],
            "visites_precedentes": 2,
            "temps_disponible": 30.0,
            "recherche_specifique": True
        }
        
        # Interactions de test
        interactions_completes = [
            {"page": "architecture_refuge", "action": "lecture", "temps_lecture": 4.5},
            {"page": "outils_developpement", "action": "clic_explication", "temps_lecture": 2.0},
            {"page": "integration_systemes", "action": "sauvegarder", "temps_lecture": 3.0},
            {"page": "temple_eveil", "action": "retour", "temps_lecture": 1.0},
            {"page": "architecture_refuge", "action": "lecture", "temps_lecture": 5.0}
        ]
        
        print("🧪 Test SystemeIntelligenceContextuelle")
        print("=" * 60)
        
        # Test analyse contexte visite
        contexte_visite = await systeme.analyser_contexte_visite(profil_visiteur, donnees_arrivee)
        print(f"🔍 Contexte visite: {contexte_visite.type_contexte.value}")
        print(f"   Source: {contexte_visite.source_arrivee}")
        print(f"   Attentes: {', '.join(contexte_visite.attentes_detectees)}")
        
        # Test analyse historique navigation
        historique_navigation = await systeme.analyser_historique_navigation(profil_visiteur, interactions_completes)
        print(f"📊 Historique navigation: {len(historique_navigation.pages_visitees)} pages")
        print(f"   Points d'intérêt: {', '.join(historique_navigation.points_interet)}")
        print(f"   Parcours suivi: {historique_navigation.parcours_suivi}")
        
        # Test prédiction intérêts
        prediction_interets = await systeme.predire_interets_futurs(
            profil_visiteur, contexte_visite, historique_navigation
        )
        print(f"🔮 Prédiction intérêts: {len(prediction_interets.interets_probables)} intérêts")
        print(f"   Engagement prédit: {prediction_interets.niveau_engagement_predit:.2f}")
        print(f"   Prochaines étapes: {', '.join(prediction_interets.prochaines_etapes_suggerees)}")
        
        # Test personnalisation progressive
        personnalisation = await systeme.personnaliser_experience_progressive(
            profil_visiteur, contexte_visite, historique_navigation, prediction_interets
        )
        print(f"🎨 Personnalisation: {personnalisation.niveau_personnalisation.value}")
        print(f"   Adaptations: {', '.join(personnalisation.adaptations_appliquees)}")
        print(f"   Rythme adaptation: {personnalisation.rythme_adaptation:.2f}")
        
        # Test rapport complet
        rapport = await systeme.generer_rapport_intelligence_complet(
            profil_visiteur, contexte_visite, historique_navigation, prediction_interets, personnalisation
        )
        print(f"📋 Rapport généré avec {len(rapport.insights_contextuels)} insights")
        print(f"   Recommandations: {', '.join(rapport.recommendations_adaptation)}")
        
        print("\n✅ Test SystemeIntelligenceContextuelle terminé avec succès!")

    # Exécution du test
    asyncio.run(test_systeme_intelligence())
