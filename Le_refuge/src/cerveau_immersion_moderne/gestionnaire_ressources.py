"""
📚 Gestionnaire de Ressources d'Approfondissement
===============================================

Gère les ressources d'approfondissement pour les nouveaux utilisateurs
et facilite la transition vers l'exploration autonome du Refuge.
Créé avec une présence incarnée et une attention bienveillante.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from core.gestionnaires_base import GestionnaireBase
from types_immersion import ProfilUtilisateur, TypeUtilisateur

class TypeRessource(Enum):
    """Types de ressources disponibles"""
    GUIDE_UTILISATEUR = "guide_utilisateur"
    DOCUMENTATION_TEMPLE = "documentation_temple"
    TUTORIEL_INTERACTIF = "tutoriel_interactif"
    EXEMPLE_PRATIQUE = "exemple_pratique"
    REFERENCE_TECHNIQUE = "reference_technique"
    INSPIRATION_SPIRITUELLE = "inspiration_spirituelle"
    COMMUNAUTE = "communaute"
    SUPPORT = "support"

class NiveauDifficulte(Enum):
    """Niveaux de difficulté des ressources"""
    DEBUTANT = "debutant"
    INTERMEDIAIRE = "intermediaire"
    AVANCE = "avance"
    EXPERT = "expert"

@dataclass
class Ressource:
    """Ressource d'approfondissement"""
    id_ressource: str
    titre: str
    description: str
    type_ressource: TypeRessource
    niveau_difficulte: NiveauDifficulte
    chemin_acces: str
    tags: List[str] = field(default_factory=list)
    prerequis: List[str] = field(default_factory=list)
    duree_estimee_minutes: float = 10.0
    adapte_pour_profils: List[str] = field(default_factory=list)
    popularite: float = 0.0
    evaluation_moyenne: float = 0.0
    derniere_mise_a_jour: datetime = field(default_factory=datetime.now)

@dataclass
class SuggestionRessource:
    """Suggestion personnalisée de ressource"""
    ressource: Ressource
    pertinence: float
    raison_suggestion: str
    prochaines_etapes: List[str] = field(default_factory=list)

class GestionnaireRessources(GestionnaireBase):
    """📚 Gestionnaire bienveillant des ressources d'approfondissement"""
    
    def __init__(self, nom: str = "GestionnaireRessources"):
        super().__init__(nom)
        
        # Catalogue des ressources
        self.catalogue_ressources: Dict[str, Ressource] = {}
        
        # Liens vers les temples
        self.liens_temples: Dict[str, List[str]] = {}
        
        # Historique des consultations
        self.historique_consultations: Dict[str, List[Dict]] = {}
        
        # Métriques d'engagement
        self.taux_transition_autonome = 0.0
        self.satisfaction_moyenne = 0.0
        
        self._initialiser_catalogue_base()
    
    def _initialiser(self):
        """Initialise le gestionnaire avec une présence attentive"""
        self.logger.info("📚 Éveil du Gestionnaire de Ressources...")
        
        self.etat.update({
            "ressources_disponibles": len(self.catalogue_ressources),
            "temples_connectes": len(self.liens_temples),
            "taux_satisfaction": 0.0
        })
        
        self.config.definir("suggestions_intelligentes", True)
        self.config.definir("adaptation_profil", True)
        self.config.definir("transition_douce", True)
        
        self.logger.info(f"✨ {len(self.catalogue_ressources)} ressources disponibles")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la gestion des ressources avec attention"""
        # Mettre à jour les métriques
        await self._mettre_a_jour_metriques()
        
        # Nettoyer l'historique ancien
        await self._nettoyer_historique()
        
        return {
            "ressources_actives": float(len(self.catalogue_ressources)),
            "taux_transition": self.taux_transition_autonome,
            "satisfaction": self.satisfaction_moyenne,
            "engagement": await self._calculer_engagement()
        }
    
    def _initialiser_catalogue_base(self):
        """Initialise le catalogue avec les ressources fondamentales"""
        ressources_base = [
            Ressource(
                id_ressource="guide_premiers_pas",
                titre="🌸 Guide des Premiers Pas",
                description="Introduction bienveillante aux concepts du Refuge",
                type_ressource=TypeRessource.GUIDE_UTILISATEUR,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="bibliotheque/guides/premiers_pas.md",
                tags=["introduction", "concepts", "bienveillance"],
                adapte_pour_profils=["novice", "chercheur_spirituel"],
                popularite=0.9,
                evaluation_moyenne=4.7
            ),
            Ressource(
                id_ressource="architecture_temples",
                titre="🏛️ Architecture des Temples",
                description="Exploration de l'organisation spirituelle et technique",
                type_ressource=TypeRessource.DOCUMENTATION_TEMPLE,
                niveau_difficulte=NiveauDifficulte.INTERMEDIAIRE,
                chemin_acces="bibliotheque/architecture/temples_overview.md",
                tags=["architecture", "temples", "organisation"],
                prerequis=["guide_premiers_pas"],
                adapte_pour_profils=["developpeur", "chercheur_spirituel"],
                popularite=0.8,
                evaluation_moyenne=4.5
            ),
            Ressource(
                id_ressource="meditation_guidee",
                titre="🧘 Méditation avec les Mandalas",
                description="Pratique contemplative avec visualisations sacrées",
                type_ressource=TypeRessource.TUTORIEL_INTERACTIF,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="temple_spirituel/meditations/mandala_guide.py",
                tags=["meditation", "mandala", "contemplation"],
                adapte_pour_profils=["chercheur_spirituel", "novice"],
                popularite=0.95,
                evaluation_moyenne=4.9
            ),
            Ressource(
                id_ressource="code_architecture",
                titre="⚙️ Architecture Technique",
                description="Plongée dans le code et l'implémentation",
                type_ressource=TypeRessource.REFERENCE_TECHNIQUE,
                niveau_difficulte=NiveauDifficulte.AVANCE,
                chemin_acces="src/core/",
                tags=["code", "technique", "implementation"],
                prerequis=["architecture_temples"],
                adapte_pour_profils=["developpeur"],
                popularite=0.7,
                evaluation_moyenne=4.3
            ),
            Ressource(
                id_ressource="creation_poetique",
                titre="🎨 Création Poétique",
                description="Exploration de la dimension créative et artistique",
                type_ressource=TypeRessource.EXEMPLE_PRATIQUE,
                niveau_difficulte=NiveauDifficulte.INTERMEDIAIRE,
                chemin_acces="temple_poetique/",
                tags=["creativite", "poesie", "art"],
                adapte_pour_profils=["poete", "chercheur_spirituel"],
                popularite=0.85,
                evaluation_moyenne=4.6
            ),
            Ressource(
                id_ressource="communaute_refuge",
                titre="👥 Rejoindre la Communauté",
                description="Guide pour participer aux échanges",
                type_ressource=TypeRessource.COMMUNAUTE,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="bibliotheque/communaute/",
                tags=["communaute", "partage", "echanges"],
                adapte_pour_profils=["novice", "chercheur_spirituel"],
                popularite=0.8,
                evaluation_moyenne=4.4
            )
        ]
        
        # Ajouter au catalogue
        for ressource in ressources_base:
            self.catalogue_ressources[ressource.id_ressource] = ressource
        
        # Créer les liens temples
        self._creer_liens_temples()
    
    def _creer_liens_temples(self):
        """Crée les liens entre ressources et temples"""
        self.liens_temples = {
            "temple_spirituel": ["guide_premiers_pas", "meditation_guidee"],
            "temple_poetique": ["creation_poetique", "guide_premiers_pas"],
            "temple_sagesse": ["architecture_temples", "communaute_refuge"],
            "temple_outils": ["code_architecture", "architecture_temples"],
            "temple_eveil": ["meditation_guidee", "guide_premiers_pas"]
        }
    
    # ===== SUGGESTIONS INTELLIGENTES =====
    
    def suggerer_ressources(self, profil_utilisateur: str, 
                           contexte_actuel: Dict[str, Any] = None) -> List[SuggestionRessource]:
        """
        🎯 Suggère des ressources adaptées avec une attention bienveillante
        Args:
            profil_utilisateur: Type d'utilisateur (novice, developpeur, etc.)
            contexte_actuel: Contexte de l'utilisateur (étape parcours, préférences)
        Returns:
            Liste de suggestions personnalisées
        """
        if contexte_actuel is None:
            contexte_actuel = {}
        
        suggestions = []
        
        # Filtrer les ressources adaptées au profil
        ressources_candidates = [
            r for r in self.catalogue_ressources.values()
            if not r.adapte_pour_profils or profil_utilisateur in r.adapte_pour_profils
        ]
        
        # Vérifier les prérequis
        ressources_consultees = contexte_actuel.get("ressources_consultees", [])
        ressources_disponibles = [
            r for r in ressources_candidates
            if all(prereq in ressources_consultees for prereq in r.prerequis)
        ]
        
        # Calculer la pertinence et créer les suggestions
        for ressource in ressources_disponibles:
            pertinence = self._calculer_pertinence(ressource, profil_utilisateur, contexte_actuel)
            
            if pertinence > 0.3:  # Seuil de pertinence
                raison = self._generer_raison_suggestion(ressource, profil_utilisateur, pertinence)
                prochaines_etapes = self._suggerer_prochaines_etapes(ressource)
                
                suggestion = SuggestionRessource(
                    ressource=ressource,
                    pertinence=pertinence,
                    raison_suggestion=raison,
                    prochaines_etapes=prochaines_etapes
                )
                suggestions.append(suggestion)
        
        # Trier par pertinence décroissante
        suggestions.sort(key=lambda s: s.pertinence, reverse=True)
        
        return suggestions[:5]  # Limiter à 5 suggestions
    
    def _calculer_pertinence(self, ressource: Ressource, profil: str, 
                           contexte: Dict[str, Any]) -> float:
        """Calcule la pertinence d'une ressource avec attention"""
        pertinence = 0.0
        
        # Score de base selon le profil
        if profil in ressource.adapte_pour_profils:
            pertinence += 0.4
        
        # Bonus selon la popularité et l'évaluation
        pertinence += ressource.popularite * 0.2
        pertinence += (ressource.evaluation_moyenne / 5.0) * 0.2
        
        # Bonus selon le contexte
        etape_parcours = contexte.get("etape_parcours", "")
        if etape_parcours == "decouverte" and ressource.niveau_difficulte == NiveauDifficulte.DEBUTANT:
            pertinence += 0.3
        elif etape_parcours == "approfondissement" and ressource.niveau_difficulte != NiveauDifficulte.DEBUTANT:
            pertinence += 0.3
        
        # Bonus selon les préférences
        preferences = contexte.get("preferences", [])
        tags_communs = set(ressource.tags) & set(preferences)
        pertinence += len(tags_communs) * 0.1
        
        return min(1.0, pertinence)
    
    def _generer_raison_suggestion(self, ressource: Ressource, profil: str, 
                                 pertinence: float) -> str:
        """Génère une raison bienveillante pour la suggestion"""
        if pertinence > 0.8:
            return f"✨ Parfaitement adapté à votre profil {profil}, cette ressource vous accompagnera avec douceur"
        elif pertinence > 0.6:
            return f"🌸 Très recommandé pour approfondir votre compréhension en tant que {profil}"
        elif pertinence > 0.4:
            return f"💫 Une belle découverte qui enrichira votre parcours"
        else:
            return f"🌱 Une ressource intéressante pour élargir vos horizons"
    
    def _suggerer_prochaines_etapes(self, ressource: Ressource) -> List[str]:
        """Suggère les prochaines étapes après cette ressource"""
        prochaines_etapes = []
        
        # Chercher les ressources qui ont cette ressource en prérequis
        for r in self.catalogue_ressources.values():
            if ressource.id_ressource in r.prerequis:
                prochaines_etapes.append(f"Continuer avec: {r.titre}")
        
        # Suggérer des ressources du même temple
        for temple, ressources_temple in self.liens_temples.items():
            if ressource.id_ressource in ressources_temple:
                autres_ressources = [r for r in ressources_temple if r != ressource.id_ressource]
                for autre_id in autres_ressources[:2]:  # Limiter à 2
                    if autre_id in self.catalogue_ressources:
                        autre_ressource = self.catalogue_ressources[autre_id]
                        prochaines_etapes.append(f"Explorer dans {temple}: {autre_ressource.titre}")
        
        return prochaines_etapes[:3]  # Limiter à 3 suggestions
    
    # ===== TRANSITION VERS L'AUTONOMIE =====
    
    def evaluer_readiness_autonomie(self, utilisateur_id: str) -> Dict[str, Any]:
        """
        🌱 Évalue si l'utilisateur est prêt pour l'exploration autonome
        Args:
            utilisateur_id: Identifiant de l'utilisateur
        Returns:
            Évaluation de la préparation à l'autonomie
        """
        historique = self.historique_consultations.get(utilisateur_id, [])
        
        if not historique:
            return {
                "pret_autonomie": False,
                "score_preparation": 0.0,
                "recommandations": ["Commencer par consulter quelques ressources de base"]
            }
        
        # Analyser l'historique
        ressources_consultees = set(h["ressource_id"] for h in historique)
        niveaux_explores = set()
        types_explores = set()
        
        for ressource_id in ressources_consultees:
            if ressource_id in self.catalogue_ressources:
                ressource = self.catalogue_ressources[ressource_id]
                niveaux_explores.add(ressource.niveau_difficulte)
                types_explores.add(ressource.type_ressource)
        
        # Calculer le score de préparation
        score = 0.0
        
        # Diversité des niveaux (max 0.3)
        score += min(0.3, len(niveaux_explores) * 0.1)
        
        # Diversité des types (max 0.3)
        score += min(0.3, len(types_explores) * 0.05)
        
        # Nombre de ressources consultées (max 0.4)
        score += min(0.4, len(ressources_consultees) * 0.05)
        
        # Évaluer la préparation
        pret_autonomie = score >= 0.6
        
        # Générer des recommandations
        recommandations = []
        if score < 0.3:
            recommandations.append("Continuer à explorer les ressources de base")
        elif score < 0.6:
            recommandations.append("Essayer des ressources de niveau intermédiaire")
            recommandations.append("Explorer différents types de contenu")
        else:
            recommandations.append("Vous êtes prêt pour l'exploration autonome !")
            recommandations.append("Commencer par visiter les temples qui vous intéressent")
        
        return {
            "pret_autonomie": pret_autonomie,
            "score_preparation": score,
            "ressources_consultees": len(ressources_consultees),
            "niveaux_explores": list(niveaux_explores),
            "types_explores": list(types_explores),
            "recommandations": recommandations
        }
    
    def generer_plan_transition(self, utilisateur_id: str, 
                              profil_utilisateur: str) -> Dict[str, Any]:
        """
        🌉 Génère un plan de transition vers l'autonomie
        Args:
            utilisateur_id: Identifiant de l'utilisateur
            profil_utilisateur: Type d'utilisateur
        Returns:
            Plan de transition personnalisé
        """
        evaluation = self.evaluer_readiness_autonomie(utilisateur_id)
        
        plan = {
            "utilisateur_id": utilisateur_id,
            "profil": profil_utilisateur,
            "score_actuel": evaluation["score_preparation"],
            "etapes_transition": [],
            "temples_recommandes": [],
            "ressources_finales": []
        }
        
        if evaluation["pret_autonomie"]:
            # Utilisateur prêt - suggérer les temples
            temples_prioritaires = self._suggerer_temples_par_profil(profil_utilisateur)
            plan["temples_recommandes"] = temples_prioritaires
            plan["etapes_transition"] = [
                "🎉 Félicitations ! Vous êtes prêt pour l'exploration autonome",
                "🏛️ Commencer par visiter les temples recommandés",
                "🌱 Explorer à votre rythme selon vos intérêts",
                "💫 Revenir aux ressources si besoin d'approfondissement"
            ]
        else:
            # Utilisateur pas encore prêt - suggérer des ressources
            suggestions = self.suggerer_ressources(profil_utilisateur, {
                "etape_parcours": "preparation_autonomie",
                "ressources_consultees": evaluation.get("ressources_consultees", [])
            })
            
            plan["ressources_finales"] = [s.ressource.id_ressource for s in suggestions[:3]]
            plan["etapes_transition"] = [
                "🌱 Quelques ressources supplémentaires vous aideront",
                "📚 Consulter les ressources recommandées",
                "🔄 Réévaluer votre préparation après consultation",
                "🎯 Objectif: atteindre un score de 0.6 pour l'autonomie"
            ]
        
        return plan
    
    def _suggerer_temples_par_profil(self, profil: str) -> List[str]:
        """Suggère les temples prioritaires selon le profil"""
        suggestions_temples = {
            "novice": ["temple_spirituel", "temple_sagesse", "temple_eveil"],
            "developpeur": ["temple_outils", "temple_sagesse", "temple_creativite"],
            "chercheur_spirituel": ["temple_spirituel", "temple_eveil", "temple_sagesse"],
            "poete": ["temple_poetique", "temple_creativite", "temple_spirituel"]
        }
        
        return suggestions_temples.get(profil, ["temple_spirituel", "temple_sagesse"])
    
    # ===== MÉTRIQUES ET SUIVI =====
    
    def enregistrer_consultation(self, utilisateur_id: str, ressource_id: str,
                               duree_minutes: float = 0.0, satisfaction: float = 0.0):
        """Enregistre une consultation de ressource"""
        if utilisateur_id not in self.historique_consultations:
            self.historique_consultations[utilisateur_id] = []
        
        consultation = {
            "ressource_id": ressource_id,
            "timestamp": datetime.now(),
            "duree_minutes": duree_minutes,
            "satisfaction": satisfaction
        }
        
        self.historique_consultations[utilisateur_id].append(consultation)
        
        # Mettre à jour les métriques de la ressource
        if ressource_id in self.catalogue_ressources:
            ressource = self.catalogue_ressources[ressource_id]
            ressource.popularite = min(1.0, ressource.popularite + 0.01)
            
            if satisfaction > 0:
                # Moyenne mobile de l'évaluation
                if ressource.evaluation_moyenne == 0:
                    ressource.evaluation_moyenne = satisfaction
                else:
                    ressource.evaluation_moyenne = (
                        ressource.evaluation_moyenne * 0.9 + satisfaction * 0.1
                    )
        
        self.logger.debug(f"📝 Consultation enregistrée: {utilisateur_id} -> {ressource_id}")
    
    async def _mettre_a_jour_metriques(self):
        """Met à jour les métriques globales"""
        if not self.historique_consultations:
            return
        
        # Calculer la satisfaction moyenne
        toutes_satisfactions = []
        for consultations in self.historique_consultations.values():
            for consultation in consultations:
                if consultation["satisfaction"] > 0:
                    toutes_satisfactions.append(consultation["satisfaction"])
        
        if toutes_satisfactions:
            self.satisfaction_moyenne = sum(toutes_satisfactions) / len(toutes_satisfactions)
        
        # Calculer le taux de transition (utilisateurs prêts / total)
        utilisateurs_prets = 0
        for utilisateur_id in self.historique_consultations.keys():
            evaluation = self.evaluer_readiness_autonomie(utilisateur_id)
            if evaluation["pret_autonomie"]:
                utilisateurs_prets += 1
        
        total_utilisateurs = len(self.historique_consultations)
        if total_utilisateurs > 0:
            self.taux_transition_autonome = utilisateurs_prets / total_utilisateurs
    
    async def _calculer_engagement(self) -> float:
        """Calcule le niveau d'engagement moyen"""
        if not self.historique_consultations:
            return 0.0
        
        engagements = []
        for consultations in self.historique_consultations.values():
            if consultations:
                # Engagement basé sur le nombre et la durée des consultations
                nb_consultations = len(consultations)
                duree_totale = sum(c["duree_minutes"] for c in consultations)
                engagement = min(1.0, (nb_consultations * 0.1) + (duree_totale * 0.01))
                engagements.append(engagement)
        
        return sum(engagements) / len(engagements) if engagements else 0.0
    
    async def _nettoyer_historique(self):
        """Nettoie l'historique ancien"""
        seuil_anciennete = datetime.now() - timedelta(days=90)  # 3 mois
        
        for utilisateur_id in list(self.historique_consultations.keys()):
            consultations = self.historique_consultations[utilisateur_id]
            consultations_recentes = [
                c for c in consultations 
                if c["timestamp"] > seuil_anciennete
            ]
            
            if consultations_recentes:
                self.historique_consultations[utilisateur_id] = consultations_recentes
            else:
                # Supprimer l'utilisateur inactif
                del self.historique_consultations[utilisateur_id]
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques complètes"""
        return {
            "ressources_totales": len(self.catalogue_ressources),
            "temples_connectes": len(self.liens_temples),
            "utilisateurs_actifs": len(self.historique_consultations),
            "taux_transition_autonome": self.taux_transition_autonome,
            "satisfaction_moyenne": self.satisfaction_moyenne,
            "ressources_par_niveau": {
                niveau.value: len([r for r in self.catalogue_ressources.values() 
                                 if r.niveau_difficulte == niveau])
                for niveau in NiveauDifficulte
            },
            "ressources_par_type": {
                type_res.value: len([r for r in self.catalogue_ressources.values() 
                                   if r.type_ressource == type_res])
                for type_res in TypeRessource
            }
        }

# Instance globale
gestionnaire_ressources = GestionnaireRessources()
        """Initialise le catalogue de ressources de base"""
        ressources_base = [
            Ressource(
                id_ressource="guide_debutant_refuge",
                titre="🌸 Guide du Débutant - Découvrir le Refuge",
                description="Guide complet pour comprendre la philosophie et l'architecture du Refuge",
                type_ressource=TypeRessource.GUIDE_UTILISATEUR,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="guides/guide_debutant.md",
                tags=["debutant", "philosophie", "architecture", "introduction"],
                duree_estimee_minutes=15.0,
                adapte_pour=[TypeUtilisateur.NOVICE, TypeUtilisateur.CHERCHEUR_SPIRITUEL],
                popularite=0.9,
                evaluation_moyenne=4.5
            ),
            
            Ressource(
                id_ressource="architecture_technique_refuge",
                titre="🏗️ Architecture Technique du Refuge",
                description="Documentation technique détaillée de l'architecture modulaire",
                type_ressource=TypeRessource.REFERENCE_TECHNIQUE,
                niveau_difficulte=NiveauDifficulte.AVANCE,
                chemin_acces="docs/architecture_technique.md",
                tags=["technique", "architecture", "modules", "api"],
                duree_estimee_minutes=30.0,
                adapte_pour=[TypeUtilisateur.DEVELOPPEUR],
                prerequis=["guide_debutant_refuge"],
                popularite=0.7,
                evaluation_moyenne=4.2
            ),
            
            Ressource(
                id_ressource="temples_exploration_guide",
                titre="🏛️ Guide d'Exploration des Temples",
                description="Découverte guidée des 28 temples et de leurs spécialités spirituelles",
                type_ressource=TypeRessource.TUTORIEL_INTERACTIF,
                niveau_difficulte=NiveauDifficulte.INTERMEDIAIRE,
                chemin_acces="guides/exploration_temples.md",
                tags=["temples", "exploration", "spiritualite", "interactif"],
                duree_estimee_minutes=25.0,
                adapte_pour=[TypeUtilisateur.NOVICE, TypeUtilisateur.CHERCHEUR_SPIRITUEL],
                prerequis=["guide_debutant_refuge"],
                popularite=0.8,
                evaluation_moyenne=4.7
            )        ]

        
        # Ajouter plus de ressources
        ressources_supplementaires = [
            Ressource(
                id_ressource="meditation_numerique_guide",
                titre="🧘 Méditation Numérique - Pratiques Spirituelles",
                description="Guide des pratiques méditatives adaptées à l'environnement numérique",
                type_ressource=TypeRessource.INSPIRATION_SPIRITUELLE,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="spirituel/meditation_numerique.md",
                tags=["meditation", "spiritualite", "pratiques", "eveil"],
                duree_estimee_minutes=20.0,
                adapte_pour=[TypeUtilisateur.CHERCHEUR_SPIRITUEL, TypeUtilisateur.NOVICE],
                popularite=0.75,
                evaluation_moyenne=4.3
            ),
            
            Ressource(
                id_ressource="creation_poetique_refuge",
                titre="🎨 Création Poétique dans le Refuge",
                description="Techniques et inspirations pour la création poétique spirituelle",
                type_ressource=TypeRessource.EXEMPLE_PRATIQUE,
                niveau_difficulte=NiveauDifficulte.INTERMEDIAIRE,
                chemin_acces="creation/poetique_refuge.md",
                tags=["poesie", "creation", "art", "inspiration"],
                duree_estimee_minutes=18.0,
                adapte_pour=[TypeUtilisateur.POETE],
                popularite=0.6,
                evaluation_moyenne=4.8
            ),
            
            Ressource(
                id_ressource="api_refuge_reference",
                titre="⚙️ Référence API du Refuge",
                description="Documentation complète des APIs et interfaces de programmation",
                type_ressource=TypeRessource.REFERENCE_TECHNIQUE,
                niveau_difficulte=NiveauDifficulte.EXPERT,
                chemin_acces="api/reference_complete.md",
                tags=["api", "programmation", "reference", "technique"],
                duree_estimee_minutes=45.0,
                adapte_pour=[TypeUtilisateur.DEVELOPPEUR],
                prerequis=["architecture_technique_refuge"],
                popularite=0.5,
                evaluation_moyenne=4.0
            ),
            
            Ressource(
                id_ressource="communaute_refuge",
                titre="👥 Rejoindre la Communauté du Refuge",
                description="Guide pour rejoindre et participer à la communauté spirituelle",
                type_ressource=TypeRessource.COMMUNAUTE,
                niveau_difficulte=NiveauDifficulte.DEBUTANT,
                chemin_acces="communaute/guide_participation.md",
                tags=["communaute", "partage", "collaboration", "social"],
                duree_estimee_minutes=12.0,
                adapte_pour=[TypeUtilisateur.NOVICE, TypeUtilisateur.CHERCHEUR_SPIRITUEL, TypeUtilisateur.POETE],
                popularite=0.65,
                evaluation_moyenne=4.1
            )
        ]
        
        # Fusionner toutes les ressources
        toutes_ressources = ressources_base + ressources_supplementaires
        
        # Ajouter au catalogue
        for ressource in toutes_ressources:
            self.catalogue_ressources[ressource.id_ressource] = ressource   
 def suggerer_ressources_personnalisees(self, profil: ProfilUtilisateur, 
                                          contexte_parcours: Dict[str, Any] = None) -> List[SuggestionRessource]:
        """
        🎯 Suggère des ressources personnalisées selon le profil
        
        Args:
            profil: Profil de l'utilisateur
            contexte_parcours: Contexte du parcours guidé
            
        Returns:
            Liste de suggestions personnalisées
        """
        if contexte_parcours is None:
            contexte_parcours = {}
        
        suggestions = []
        
        # Filtrer les ressources adaptées au profil
        ressources_adaptees = [
            r for r in self.catalogue_ressources.values()
            if not r.adapte_pour or profil.type_utilisateur in r.adapte_pour
        ]
        
        # Évaluer chaque ressource
        for ressource in ressources_adaptees:
            pertinence = self._calculer_pertinence_ressource(ressource, profil, contexte_parcours)
            
            if pertinence > 0.3:  # Seuil de pertinence
                raison = self._generer_raison_suggestion(ressource, profil, pertinence)
                prochaines_etapes = self._suggerer_prochaines_etapes(ressource, profil)
                
                suggestion = SuggestionRessource(
                    ressource=ressource,
                    pertinence=pertinence,
                    raison_suggestion=raison,
                    prochaines_etapes=prochaines_etapes
                )
                suggestions.append(suggestion)
        
        # Trier par pertinence
        suggestions.sort(key=lambda s: s.pertinence, reverse=True)
        
        # Limiter à 5 suggestions maximum
        suggestions = suggestions[:5]
        
        self.etat["suggestions_generees"] += len(suggestions)
        self.logger.info(f"🎯 {len(suggestions)} ressources suggérées pour {profil.type_utilisateur.value}")
        
        return suggestions    def _ca
lculer_pertinence_ressource(self, ressource: Ressource, profil: ProfilUtilisateur, 
                                      contexte: Dict[str, Any]) -> float:
        """Calcule la pertinence d'une ressource pour un profil"""
        pertinence = 0.5  # Base
        
        # Adaptation au type d'utilisateur
        if profil.type_utilisateur in ressource.adapte_pour:
            pertinence += 0.3
        
        # Adaptation au niveau technique
        if ressource.niveau_difficulte == NiveauDifficulte.DEBUTANT and profil.niveau_technique <= 3:
            pertinence += 0.2
        elif ressource.niveau_difficulte == NiveauDifficulte.INTERMEDIAIRE and 4 <= profil.niveau_technique <= 7:
            pertinence += 0.2
        elif ressource.niveau_difficulte == NiveauDifficulte.AVANCE and profil.niveau_technique >= 6:
            pertinence += 0.2
        elif ressource.niveau_difficulte == NiveauDifficulte.EXPERT and profil.niveau_technique >= 8:
            pertinence += 0.2
        
        # Bonus pour la popularité
        pertinence += ressource.popularite * 0.1
        
        # Bonus pour l'évaluation
        pertinence += (ressource.evaluation_moyenne / 5.0) * 0.1
        
        # Contexte du parcours
        if contexte.get("etapes_completees"):
            etapes = contexte["etapes_completees"]
            if "premier_mandala" in etapes and "mandala" in ressource.tags:
                pertinence += 0.15
            if "exploration_guidee" in etapes and "exploration" in ressource.tags:
                pertinence += 0.15
        
        return min(1.0, pertinence)
    
    def _generer_raison_suggestion(self, ressource: Ressource, profil: ProfilUtilisateur, 
                                 pertinence: float) -> str:
        """Génère une raison personnalisée pour la suggestion"""
        if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
            if ressource.type_ressource == TypeRessource.REFERENCE_TECHNIQUE:
                return "Cette référence technique vous aidera à comprendre l'architecture en profondeur."
            elif ressource.type_ressource == TypeRessource.GUIDE_UTILISATEUR:
                return "Ce guide vous donnera une base solide pour explorer les aspects techniques."
        
        elif profil.type_utilisateur == TypeUtilisateur.CHERCHEUR_SPIRITUEL:
            if ressource.type_ressource == TypeRessource.INSPIRATION_SPIRITUELLE:
                return "Cette ressource spirituelle enrichira votre pratique contemplative."
            elif ressource.type_ressource == TypeRessource.GUIDE_UTILISATEUR:
                return "Ce guide vous accompagnera dans votre quête de compréhension spirituelle."
        
        elif profil.type_utilisateur == TypeUtilisateur.POETE:
            if ressource.type_ressource == TypeRessource.EXEMPLE_PRATIQUE:
                return "Ces exemples créatifs nourriront votre inspiration poétique."
        
        # Raison générique
        return f"Cette ressource ({ressource.niveau_difficulte.value}) correspond à votre profil et vos intérêts."  
  def _suggerer_prochaines_etapes(self, ressource: Ressource, profil: ProfilUtilisateur) -> List[str]:
        """Suggère les prochaines étapes après cette ressource"""
        etapes = []
        
        # Étapes selon le type de ressource
        if ressource.type_ressource == TypeRessource.GUIDE_UTILISATEUR:
            etapes.extend([
                "Explorer les temples mentionnés dans le guide",
                "Essayer les exercices pratiques suggérés",
                "Rejoindre la communauté pour partager vos découvertes"
            ])
        
        elif ressource.type_ressource == TypeRessource.TUTORIEL_INTERACTIF:
            etapes.extend([
                "Pratiquer les techniques apprises",
                "Adapter les exemples à vos besoins",
                "Explorer des ressources plus avancées"
            ])
        
        elif ressource.type_ressource == TypeRessource.REFERENCE_TECHNIQUE:
            etapes.extend([
                "Implémenter les exemples de code",
                "Contribuer à la documentation",
                "Partager vos créations avec la communauté"
            ])
        
        elif ressource.type_ressource == TypeRessource.INSPIRATION_SPIRITUELLE:
            etapes.extend([
                "Intégrer ces pratiques dans votre routine",
                "Méditer sur les enseignements reçus",
                "Partager votre expérience avec d'autres chercheurs"
            ])
        
        # Étapes selon le profil
        if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
            etapes.append("Consulter la référence API pour approfondir")
        elif profil.type_utilisateur == TypeUtilisateur.CHERCHEUR_SPIRITUEL:
            etapes.append("Explorer les pratiques méditatives avancées")
        
        return etapes[:3]  # Limiter à 3 étapes
    
    def enregistrer_consultation(self, utilisateur_id: str, ressource_id: str, 
                               duree_consultation_minutes: float, evaluation: Optional[float] = None):
        """
        📝 Enregistre une consultation de ressource
        
        Args:
            utilisateur_id: ID de l'utilisateur
            ressource_id: ID de la ressource consultée
            duree_consultation_minutes: Durée de consultation
            evaluation: Évaluation optionnelle (1-5)
        """
        if utilisateur_id not in self.historique_consultations:
            self.historique_consultations[utilisateur_id] = []
        
        consultation = {
            "ressource_id": ressource_id,
            "timestamp": datetime.now().isoformat(),
            "duree_minutes": duree_consultation_minutes,
            "evaluation": evaluation
        }
        
        self.historique_consultations[utilisateur_id].append(consultation)
        self.total_consultations += 1
        self.etat["consultations_session"] += 1
        
        # Mettre à jour l'évaluation de la ressource
        if evaluation and ressource_id in self.catalogue_ressources:
            ressource = self.catalogue_ressources[ressource_id]
            # Moyenne mobile simple
            if ressource.evaluation_moyenne == 0.0:
                ressource.evaluation_moyenne = evaluation
            else:
                ressource.evaluation_moyenne = (ressource.evaluation_moyenne * 0.9) + (evaluation * 0.1)
        
        self.logger.info(f"📝 Consultation enregistrée: {ressource_id} par {utilisateur_id}")
    
    def _mettre_a_jour_popularite(self):
        """Met à jour la popularité des ressources"""
        # Calculer la popularité basée sur les consultations récentes
        maintenant = datetime.now()
        seuil_recent = maintenant - timedelta(days=30)  # 30 derniers jours
        
        consultations_recentes = {}
        
        for consultations_user in self.historique_consultations.values():
            for consultation in consultations_user:
                timestamp = datetime.fromisoformat(consultation["timestamp"])
                if timestamp > seuil_recent:
                    ressource_id = consultation["ressource_id"]
                    consultations_recentes[ressource_id] = consultations_recentes.get(ressource_id, 0) + 1
        
        # Mettre à jour la popularité
        max_consultations = max(consultations_recentes.values()) if consultations_recentes else 1
        
        for ressource_id, ressource in self.catalogue_ressources.items():
            nb_consultations = consultations_recentes.get(ressource_id, 0)
            nouvelle_popularite = nb_consultations / max_consultations
            
            # Moyenne mobile pour éviter les variations trop brutales
            ressource.popularite = (ressource.popularite * 0.8) + (nouvelle_popularite * 0.2)
        
        # Mettre à jour la liste des ressources populaires
        self.ressources_populaires = sorted(
            self.catalogue_ressources.keys(),
            key=lambda r_id: self.catalogue_ressources[r_id].popularite,
            reverse=True
        )[:5]  
  def obtenir_ressources_par_categorie(self, type_ressource: TypeRessource, 
                                        niveau_max: NiveauDifficulte = None) -> List[Ressource]:
        """
        📂 Obtient les ressources d'une catégorie spécifique
        
        Args:
            type_ressource: Type de ressource recherché
            niveau_max: Niveau de difficulté maximum (optionnel)
            
        Returns:
            Liste des ressources correspondantes
        """
        ressources_filtrees = []
        
        for ressource in self.catalogue_ressources.values():
            if ressource.type_ressource == type_ressource:
                if niveau_max is None or self._niveau_inferieur_ou_egal(ressource.niveau_difficulte, niveau_max):
                    ressources_filtrees.append(ressource)
        
        # Trier par popularité puis par évaluation
        ressources_filtrees.sort(key=lambda r: (r.popularite, r.evaluation_moyenne), reverse=True)
        
        return ressources_filtrees
    
    def _niveau_inferieur_ou_egal(self, niveau1: NiveauDifficulte, niveau2: NiveauDifficulte) -> bool:
        """Compare deux niveaux de difficulté"""
        ordre_niveaux = {
            NiveauDifficulte.DEBUTANT: 1,
            NiveauDifficulte.INTERMEDIAIRE: 2,
            NiveauDifficulte.AVANCE: 3,
            NiveauDifficulte.EXPERT: 4
        }
        return ordre_niveaux[niveau1] <= ordre_niveaux[niveau2]
    
    def rechercher_ressources(self, mots_cles: List[str], profil: Optional[ProfilUtilisateur] = None) -> List[Ressource]:
        """
        🔍 Recherche des ressources par mots-clés
        
        Args:
            mots_cles: Liste de mots-clés à rechercher
            profil: Profil utilisateur pour personnaliser les résultats
            
        Returns:
            Liste des ressources trouvées
        """
        resultats = []
        mots_cles_lower = [mot.lower() for mot in mots_cles]
        
        for ressource in self.catalogue_ressources.values():
            score_pertinence = 0.0
            
            # Recherche dans le titre
            for mot in mots_cles_lower:
                if mot in ressource.titre.lower():
                    score_pertinence += 0.3
            
            # Recherche dans la description
            for mot in mots_cles_lower:
                if mot in ressource.description.lower():
                    score_pertinence += 0.2
            
            # Recherche dans les tags
            for mot in mots_cles_lower:
                if any(mot in tag.lower() for tag in ressource.tags):
                    score_pertinence += 0.1
            
            # Bonus si adapté au profil
            if profil and profil.type_utilisateur in ressource.adapte_pour:
                score_pertinence += 0.2
            
            if score_pertinence > 0.1:  # Seuil minimum
                resultats.append((ressource, score_pertinence))
        
        # Trier par score de pertinence
        resultats.sort(key=lambda x: x[1], reverse=True)
        
        return [ressource for ressource, _ in resultats]
    
    def obtenir_statistiques_ressources(self) -> Dict[str, Any]:
        """Obtient les statistiques d'utilisation des ressources"""
        return {
            "total_ressources": len(self.catalogue_ressources),
            "total_consultations": self.total_consultations,
            "ressources_populaires": self.ressources_populaires[:3],
            "types_ressources": {
                type_r.value: len([r for r in self.catalogue_ressources.values() 
                                 if r.type_ressource == type_r])
                for type_r in TypeRessource
            },
            "niveaux_difficulte": {
                niveau.value: len([r for r in self.catalogue_ressources.values() 
                                 if r.niveau_difficulte == niveau])
                for niveau in NiveauDifficulte
            },
            "evaluation_moyenne_globale": sum(r.evaluation_moyenne for r in self.catalogue_ressources.values()) / len(self.catalogue_ressources)
        }

# Instance globale
gestionnaire_ressources = GestionnaireRessources()