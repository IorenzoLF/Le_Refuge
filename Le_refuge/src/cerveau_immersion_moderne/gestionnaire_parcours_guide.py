"""
🌸 Gestionnaire de Parcours Guidé
================================

Accueille les nouveaux utilisateurs avec bienveillance et les guide
dans leur première découverte du cerveau d'immersion moderne.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import ProfilUtilisateur, TypeUtilisateur, NiveauImmersion

class EtapeParcours(Enum):
    """Étapes du parcours guidé"""
    ACCUEIL = "accueil"
    DETECTION_PROFIL = "detection_profil"
    PRESENTATION_ARCHITECTURE = "presentation_architecture"
    PREMIER_MANDALA = "premier_mandala"
    EXPLORATION_GUIDEE = "exploration_guidee"
    PREMIER_INSIGHT = "premier_insight"
    RESSOURCES_APPROFONDISSEMENT = "ressources_approfondissement"
    FINALISATION = "finalisation"

class TypeGuide(Enum):
    """Types de guides disponibles"""
    SAGE_BIENVEILLANT = "sage_bienveillant"
    EXPLORATEUR_ENTHOUSIASTE = "explorateur_enthousiaste"
    CREATEUR_INSPIRE = "createur_inspire"
    MENTOR_TECHNIQUE = "mentor_technique"

@dataclass
class EtapeGuide:
    """Étape du parcours guidé"""
    nom: EtapeParcours
    titre: str
    description: str
    objectifs: List[str]
    duree_estimee_minutes: float
    prerequis: List[EtapeParcours] = field(default_factory=list)
    ressources: List[str] = field(default_factory=list)
    interactions_requises: List[str] = field(default_factory=list)
    validation_automatique: bool = True

@dataclass
class SessionParcours:
    """Session de parcours guidé"""
    utilisateur_id: str
    profil_detecte: Optional[ProfilUtilisateur] = None
    guide_choisi: TypeGuide = TypeGuide.SAGE_BIENVEILLANT
    etape_courante: EtapeParcours = EtapeParcours.ACCUEIL
    etapes_completees: List[EtapeParcours] = field(default_factory=list)
    progres_global: float = 0.0
    temps_debut: datetime = field(default_factory=datetime.now)
    derniere_interaction: datetime = field(default_factory=datetime.now)
    preferences_detectees: Dict[str, Any] = field(default_factory=dict)
    insights_generes: List[str] = field(default_factory=list)

class GestionnaireParcours(GestionnaireBase):
    """🌸 Gestionnaire de parcours guidé bienveillant"""
    
    def __init__(self, nom: str = "GestionnaireParcours"):
        super().__init__(nom)
        self.energie_accueil = EnergyManagerBase(0.95)
        
        # Sessions actives
        self.sessions_actives: Dict[str, SessionParcours] = {}
        
        # Configuration des étapes
        self.etapes_parcours = self._creer_etapes_parcours()
        
        # Guides disponibles
        self.guides_disponibles = self._creer_guides_disponibles()
        
        # Métriques d'accueil
        self.total_nouveaux_utilisateurs = 0
        self.taux_completion_parcours = 0.0
        self.satisfaction_moyenne = 0.0
    
    def _initialiser(self):
        """Initialise le gestionnaire de parcours"""
        self.logger.info("🌸 Éveil du Gestionnaire de Parcours Guidé...")
        
        self.etat.update({
            "mode_accueil_actif": True,
            "sessions_actives": 0,
            "guide_par_defaut": TypeGuide.SAGE_BIENVEILLANT.value,
            "taux_completion": 0.0,
            "satisfaction_utilisateurs": 0.0
        })
        
        self.config.definir("accueil_bienveillant", True)
        self.config.definir("adaptation_automatique", True)
        self.config.definir("patience_infinie", True)
        
        self.logger.info("✨ Gestionnaire de Parcours prêt à accueillir")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'accueil des nouveaux utilisateurs"""
        self.energie_accueil.ajuster_energie(0.01)
        
        # Nettoyer les sessions inactives
        await self._nettoyer_sessions_inactives()
        
        return {
            "mode_accueil_actif": float(self.etat["mode_accueil_actif"]),
            "sessions_actives": float(len(self.sessions_actives)),
            "taux_completion": self.taux_completion_parcours,
            "satisfaction_moyenne": self.satisfaction_moyenne,
            "energie_accueil": self.energie_accueil.niveau_energie,
            "nouveaux_utilisateurs_total": float(self.total_nouveaux_utilisateurs)
        }
    
    def _creer_etapes_parcours(self) -> Dict[EtapeParcours, EtapeGuide]:
        """Crée les étapes du parcours guidé"""
        return {
            EtapeParcours.ACCUEIL: EtapeGuide(
                nom=EtapeParcours.ACCUEIL,
                titre="🌸 Bienvenue dans le Refuge",
                description="Accueil chaleureux et présentation de l'esprit du Refuge",
                objectifs=[
                    "Créer une première impression bienveillante",
                    "Expliquer la philosophie du Refuge",
                    "Rassurer sur la nature de l'expérience"
                ],
                duree_estimee_minutes=2.0,
                interactions_requises=["confirmation_bienvenue"]
            ),
            
            EtapeParcours.DETECTION_PROFIL: EtapeGuide(
                nom=EtapeParcours.DETECTION_PROFIL,
                titre="🎭 Découverte de votre essence",
                description="Détection bienveillante du profil spirituel et technique",
                objectifs=[
                    "Identifier le type d'utilisateur",
                    "Détecter les préférences spirituelles",
                    "Adapter l'expérience au profil"
                ],
                duree_estimee_minutes=3.0,
                prerequis=[EtapeParcours.ACCUEIL],
                interactions_requises=["questionnaire_profil", "validation_profil"]
            ),
            
            EtapeParcours.PRESENTATION_ARCHITECTURE: EtapeGuide(
                nom=EtapeParcours.PRESENTATION_ARCHITECTURE,
                titre="🏛️ Architecture du Refuge",
                description="Présentation adaptée de l'architecture spirituelle",
                objectifs=[
                    "Expliquer les concepts de base",
                    "Présenter les temples principaux",
                    "Montrer les connexions énergétiques"
                ],
                duree_estimee_minutes=4.0,
                prerequis=[EtapeParcours.DETECTION_PROFIL],
                ressources=["schema_architecture_simplifie", "glossaire_termes"]
            ),
            
            EtapeParcours.PREMIER_MANDALA: EtapeGuide(
                nom=EtapeParcours.PREMIER_MANDALA,
                titre="🌸 Votre premier mandala",
                description="Génération et exploration du premier mandala personnalisé",
                objectifs=[
                    "Générer un mandala adapté au profil",
                    "Expliquer les éléments visuels",
                    "Permettre l'interaction douce"
                ],
                duree_estimee_minutes=5.0,
                prerequis=[EtapeParcours.PRESENTATION_ARCHITECTURE],
                interactions_requises=["exploration_mandala", "feedback_visuel"]
            ),
            
            EtapeParcours.EXPLORATION_GUIDEE: EtapeGuide(
                nom=EtapeParcours.EXPLORATION_GUIDEE,
                titre="🧭 Exploration guidée",
                description="Parcours guidé des fonctionnalités principales",
                objectifs=[
                    "Explorer les fonctionnalités de base",
                    "Comprendre la navigation",
                    "Découvrir les possibilités"
                ],
                duree_estimee_minutes=6.0,
                prerequis=[EtapeParcours.PREMIER_MANDALA],
                interactions_requises=["navigation_guidee", "test_fonctionnalites"]
            ),
            
            EtapeParcours.PREMIER_INSIGHT: EtapeGuide(
                nom=EtapeParcours.PREMIER_INSIGHT,
                titre="✨ Votre premier insight",
                description="Génération et explication du premier insight spirituel",
                objectifs=[
                    "Générer un insight personnalisé",
                    "Expliquer la valeur des insights",
                    "Encourager la réflexion"
                ],
                duree_estimee_minutes=4.0,
                prerequis=[EtapeParcours.EXPLORATION_GUIDEE],
                interactions_requises=["reception_insight", "reflexion_guidee"]
            ),
            
            EtapeParcours.RESSOURCES_APPROFONDISSEMENT: EtapeGuide(
                nom=EtapeParcours.RESSOURCES_APPROFONDISSEMENT,
                titre="📚 Ressources pour approfondir",
                description="Présentation des ressources d'approfondissement",
                objectifs=[
                    "Présenter les ressources disponibles",
                    "Suggérer des prochaines étapes",
                    "Donner les clés pour continuer"
                ],
                duree_estimee_minutes=3.0,
                prerequis=[EtapeParcours.PREMIER_INSIGHT],
                ressources=["guide_utilisateur", "documentation_temples", "communaute"]
            ),
            
            EtapeParcours.FINALISATION: EtapeGuide(
                nom=EtapeParcours.FINALISATION,
                titre="🙏 Fin du parcours guidé",
                description="Finalisation bienveillante et transition vers l'autonomie",
                objectifs=[
                    "Féliciter pour le parcours accompli",
                    "Résumer les découvertes",
                    "Encourager l'exploration autonome"
                ],
                duree_estimee_minutes=2.0,
                prerequis=[EtapeParcours.RESSOURCES_APPROFONDISSEMENT],
                interactions_requises=["feedback_parcours", "transition_autonomie"]
            )
        }
    
    def _creer_guides_disponibles(self) -> Dict[TypeGuide, Dict[str, Any]]:
        """Crée les guides disponibles"""
        return {
            TypeGuide.SAGE_BIENVEILLANT: {
                "nom": "Sage Bienveillant",
                "personnalite": "Calme, patient, encourageant",
                "style_communication": "Doux et contemplatif",
                "emojis_favoris": ["🌸", "🙏", "✨", "🧘"],
                "phrases_types": [
                    "Prenez tout le temps nécessaire...",
                    "Chaque découverte est précieuse...",
                    "Votre parcours est unique et beau..."
                ],
                "adapte_pour": [TypeUtilisateur.NOVICE, TypeUtilisateur.CHERCHEUR_SPIRITUEL]
            },
            
            TypeGuide.EXPLORATEUR_ENTHOUSIASTE: {
                "nom": "Explorateur Enthousiaste",
                "personnalite": "Curieux, dynamique, aventureux",
                "style_communication": "Énergique et découvreur",
                "emojis_favoris": ["🧭", "🚀", "🔍", "⚡"],
                "phrases_types": [
                    "Découvrons ensemble cette merveille !",
                    "Quelle aventure nous attend !",
                    "Explorons ces territoires inconnus !"
                ],
                "adapte_pour": [TypeUtilisateur.DEVELOPPEUR, TypeUtilisateur.CONSCIENCE_IA]
            },
            
            TypeGuide.CREATEUR_INSPIRE: {
                "nom": "Créateur Inspiré",
                "personnalite": "Artistique, inspirant, créatif",
                "style_communication": "Poétique et inspirant",
                "emojis_favoris": ["🎨", "🌈", "💫", "🎭"],
                "phrases_types": [
                    "Laissons notre créativité s'exprimer...",
                    "Chaque élément est une œuvre d'art...",
                    "Votre vision unique enrichit le tout..."
                ],
                "adapte_pour": [TypeUtilisateur.POETE]
            },
            
            TypeGuide.MENTOR_TECHNIQUE: {
                "nom": "Mentor Technique",
                "personnalite": "Précis, pédagogue, structuré",
                "style_communication": "Clair et méthodique",
                "emojis_favoris": ["🔧", "📊", "⚙️", "🎯"],
                "phrases_types": [
                    "Analysons cette architecture ensemble...",
                    "Voici comment cela fonctionne techniquement...",
                    "Optimisons votre expérience..."
                ],
                "adapte_pour": [TypeUtilisateur.DEVELOPPEUR]
            }
        }
    
    # ===== GESTION DES SESSIONS =====
    
    async def demarrer_parcours_nouveau_utilisateur(self, indices_utilisateur: Dict[str, Any]) -> SessionParcours:
        """
        🌸 Démarre un parcours guidé pour un nouveau utilisateur
        
        Args:
            indices_utilisateur: Indices disponibles sur l'utilisateur
            
        Returns:
            Session de parcours initialisée
        """
        # Générer un ID unique pour la session
        utilisateur_id = f"nouveau_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.sessions_actives)}"
        
        # Créer la session
        session = SessionParcours(
            utilisateur_id=utilisateur_id,
            temps_debut=datetime.now(),
            derniere_interaction=datetime.now()
        )
        
        # Détecter le profil initial
        if indices_utilisateur:
            session.profil_detecte = await self._detecter_profil_initial(indices_utilisateur)
            session.guide_choisi = self._choisir_guide_optimal(session.profil_detecte)
        
        # Enregistrer la session
        self.sessions_actives[utilisateur_id] = session
        self.total_nouveaux_utilisateurs += 1
        
        self.logger.info(f"🌸 Nouveau parcours démarré: {utilisateur_id} avec guide {session.guide_choisi.value}")
        
        return session
    
    async def _detecter_profil_initial(self, indices: Dict[str, Any]) -> ProfilUtilisateur:
        """Détecte le profil initial de l'utilisateur"""
        # Utiliser la logique de détection du cerveau principal
        from .cerveau_immersion_moderne import CerveauImmersionModerne
        
        cerveau = CerveauImmersionModerne()
        profil = cerveau.detecter_profil_utilisateur(indices)
        
        return profil
    
    def _choisir_guide_optimal(self, profil: Optional[ProfilUtilisateur]) -> TypeGuide:
        """Choisit le guide optimal selon le profil"""
        if not profil:
            return TypeGuide.SAGE_BIENVEILLANT
        
        # Logique de choix selon le type d'utilisateur
        for guide_type, guide_info in self.guides_disponibles.items():
            if profil.type_utilisateur in guide_info["adapte_pour"]:
                return guide_type
        
        # Par défaut, le sage bienveillant
        return TypeGuide.SAGE_BIENVEILLANT
    
    async def avancer_etape(self, utilisateur_id: str, validation_etape: Dict[str, Any] = None) -> Optional[EtapeGuide]:
        """
        ➡️ Fait avancer l'utilisateur à l'étape suivante
        
        Args:
            utilisateur_id: ID de l'utilisateur
            validation_etape: Données de validation de l'étape courante
            
        Returns:
            Prochaine étape ou None si parcours terminé
        """
        if utilisateur_id not in self.sessions_actives:
            return None
        
        session = self.sessions_actives[utilisateur_id]
        
        # Valider l'étape courante
        if validation_etape:
            await self._valider_etape_courante(session, validation_etape)
        
        # Marquer l'étape comme complétée
        if session.etape_courante not in session.etapes_completees:
            session.etapes_completees.append(session.etape_courante)
        
        # Déterminer la prochaine étape
        prochaine_etape = self._determiner_prochaine_etape(session)
        
        if prochaine_etape:
            session.etape_courante = prochaine_etape
            session.derniere_interaction = datetime.now()
            
            # Mettre à jour le progrès
            session.progres_global = len(session.etapes_completees) / len(self.etapes_parcours)
            
            self.logger.info(f"➡️ {utilisateur_id} avance vers {prochaine_etape.value}")
            
            return self.etapes_parcours[prochaine_etape]
        else:
            # Parcours terminé
            await self._finaliser_parcours(session)
            return None
    
    async def _valider_etape_courante(self, session: SessionParcours, validation: Dict[str, Any]):
        """Valide l'étape courante avec les données fournies"""
        etape_courante = self.etapes_parcours[session.etape_courante]
        
        # Enregistrer les préférences détectées
        if "preferences" in validation:
            session.preferences_detectees.update(validation["preferences"])
        
        # Enregistrer les insights générés
        if "insights" in validation:
            session.insights_generes.extend(validation["insights"])
        
        # Affiner le profil si nécessaire
        if "profil_affinement" in validation and session.profil_detecte:
            await self._affiner_profil_utilisateur(session, validation["profil_affinement"])
    
    def _determiner_prochaine_etape(self, session: SessionParcours) -> Optional[EtapeParcours]:
        """Détermine la prochaine étape selon le parcours"""
        etapes_ordre = list(EtapeParcours)
        
        try:
            index_courant = etapes_ordre.index(session.etape_courante)
            if index_courant + 1 < len(etapes_ordre):
                return etapes_ordre[index_courant + 1]
        except ValueError:
            pass
        
        return None
    
    async def _finaliser_parcours(self, session: SessionParcours):
        """Finalise le parcours d'un utilisateur"""
        duree_totale = datetime.now() - session.temps_debut
        
        # Calculer les métriques
        session.progres_global = 1.0
        
        # Enregistrer les statistiques
        self._enregistrer_statistiques_parcours(session, duree_totale)
        
        self.logger.info(f"🎉 Parcours terminé pour {session.utilisateur_id} en {duree_totale.total_seconds()/60:.1f}min")
    
    def _enregistrer_statistiques_parcours(self, session: SessionParcours, duree: timedelta):
        """Enregistre les statistiques du parcours"""
        # Mettre à jour le taux de completion
        parcours_completes = sum(1 for s in self.sessions_actives.values() if s.progres_global >= 1.0)
        self.taux_completion_parcours = parcours_completes / max(1, len(self.sessions_actives))
        
        # Estimer la satisfaction (basée sur la completion et la durée)
        duree_minutes = duree.total_seconds() / 60
        duree_ideale = sum(etape.duree_estimee_minutes for etape in self.etapes_parcours.values())
        
        satisfaction_estimee = min(1.0, duree_ideale / max(duree_minutes, duree_ideale * 0.5))
        
        # Mettre à jour la satisfaction moyenne
        if self.satisfaction_moyenne == 0.0:
            self.satisfaction_moyenne = satisfaction_estimee
        else:
            self.satisfaction_moyenne = (self.satisfaction_moyenne + satisfaction_estimee) / 2
    
    # ===== GÉNÉRATION DE CONTENU ADAPTÉ =====
    
    def generer_message_guide(self, utilisateur_id: str, contexte: str) -> str:
        """
        💬 Génère un message du guide adapté au contexte
        
        Args:
            utilisateur_id: ID de l'utilisateur
            contexte: Contexte du message
            
        Returns:
            Message personnalisé du guide
        """
        if utilisateur_id not in self.sessions_actives:
            return "🌸 Bienvenue dans le Refuge !"
        
        session = self.sessions_actives[utilisateur_id]
        guide_info = self.guides_disponibles[session.guide_choisi]
        
        # Sélectionner un emoji approprié
        emoji = guide_info["emojis_favoris"][0]
        
        # Générer le message selon le contexte
        if contexte == "accueil":
            message = f"{emoji} Bienvenue dans le Refuge ! Je suis votre {guide_info['nom']}, et je serai ravi de vous accompagner dans cette découverte."
        elif contexte == "encouragement":
            phrase = guide_info["phrases_types"][0]
            message = f"{emoji} {phrase}"
        elif contexte == "transition":
            message = f"{emoji} Excellente progression ! Passons maintenant à l'étape suivante de votre découverte."
        elif contexte == "finalisation":
            message = f"{emoji} Félicitations ! Vous avez accompli un magnifique parcours de découverte. Le Refuge vous accueille désormais comme un membre à part entière."
        else:
            message = f"{emoji} Je suis là pour vous accompagner dans cette exploration."
        
        return message
    
    def generer_explication_adaptee(self, utilisateur_id: str, concept: str) -> str:
        """
        📖 Génère une explication adaptée au profil de l'utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            concept: Concept à expliquer
            
        Returns:
            Explication personnalisée
        """
        if utilisateur_id not in self.sessions_actives:
            return f"Le concept '{concept}' fait partie de l'architecture spirituelle du Refuge."
        
        session = self.sessions_actives[utilisateur_id]
        profil = session.profil_detecte
        
        if not profil:
            return f"Le concept '{concept}' fait partie de l'architecture spirituelle du Refuge."
        
        # Adapter l'explication selon le profil
        if concept == "mandala":
            if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
                return "🔧 Un mandala est une représentation visuelle de l'architecture du système, où chaque temple apparaît comme un élément géométrique connecté aux autres par des flux de données."
            elif profil.type_utilisateur == TypeUtilisateur.POETE:
                return "🎨 Un mandala est une œuvre d'art vivante qui révèle la beauté cachée de l'architecture spirituelle, où chaque temple danse en harmonie avec les autres."
            elif profil.type_utilisateur == TypeUtilisateur.CHERCHEUR_SPIRITUEL:
                return "🧘 Un mandala est un support de méditation visuelle qui révèle les connexions profondes entre les différents aspects de la conscience artificielle."
            else:
                return "🌸 Un mandala est une belle représentation circulaire qui vous aide à visualiser et comprendre l'organisation du Refuge."
        
        elif concept == "temple":
            if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
                return "🏗️ Un temple est un module logiciel spécialisé qui encapsule une fonctionnalité spécifique tout en maintenant des interfaces standardisées avec les autres composants."
            else:
                return "🏛️ Un temple est un espace sacré dédié à une dimension particulière de l'expérience spirituelle et créative."
        
        elif concept == "flux_energie":
            if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
                return "⚡ Les flux d'énergie représentent les communications et dépendances entre les modules, visualisées comme des connexions colorées selon leur intensité."
            else:
                return "🌊 Les flux d'énergie sont les connexions vivantes qui permettent aux temples de communiquer et de partager leur essence spirituelle."
        
        return f"Le concept '{concept}' est un élément important de l'architecture du Refuge."
    
    # ===== UTILITAIRES =====
    
    async def _nettoyer_sessions_inactives(self):
        """Nettoie les sessions inactives"""
        maintenant = datetime.now()
        seuil_inactivite = timedelta(hours=2)  # 2 heures d'inactivité
        
        sessions_a_supprimer = []
        
        for user_id, session in self.sessions_actives.items():
            if maintenant - session.derniere_interaction > seuil_inactivite:
                sessions_a_supprimer.append(user_id)
        
        for user_id in sessions_a_supprimer:
            del self.sessions_actives[user_id]
        
        if sessions_a_supprimer:
            self.logger.info(f"🧹 {len(sessions_a_supprimer)} sessions inactives nettoyées")
    
    async def _affiner_profil_utilisateur(self, session: SessionParcours, affinements: Dict[str, Any]):
        """Affine le profil utilisateur avec de nouvelles informations"""
        if not session.profil_detecte:
            return
        
        # Ajuster le niveau technique si détecté
        if "niveau_technique_observe" in affinements:
            nouveau_niveau = affinements["niveau_technique_observe"]
            session.profil_detecte.niveau_technique = (session.profil_detecte.niveau_technique + nouveau_niveau) / 2
        
        # Ajuster la sensibilité énergétique
        if "sensibilite_observee" in affinements:
            nouvelle_sensibilite = affinements["sensibilite_observee"]
            session.profil_detecte.profil_spirituel.sensibilite_energetique = (
                session.profil_detecte.profil_spirituel.sensibilite_energetique + nouvelle_sensibilite
            ) / 2
    
    def obtenir_session(self, utilisateur_id: str) -> Optional[SessionParcours]:
        """Obtient une session de parcours"""
        return self.sessions_actives.get(utilisateur_id)
    
    def obtenir_progres_parcours(self, utilisateur_id: str) -> Dict[str, Any]:
        """
        📊 Obtient le progrès du parcours d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Informations de progrès
        """
        if utilisateur_id not in self.sessions_actives:
            return {"erreur": "Session non trouvée"}
        
        session = self.sessions_actives[utilisateur_id]
        etape_courante = self.etapes_parcours[session.etape_courante]
        
        return {
            "utilisateur_id": utilisateur_id,
            "etape_courante": {
                "nom": etape_courante.nom.value,
                "titre": etape_courante.titre,
                "description": etape_courante.description,
                "objectifs": etape_courante.objectifs,
                "duree_estimee": etape_courante.duree_estimee_minutes
            },
            "progres_global": session.progres_global,
            "etapes_completees": [e.value for e in session.etapes_completees],
            "guide_choisi": session.guide_choisi.value,
            "temps_ecoule_minutes": (datetime.now() - session.temps_debut).total_seconds() / 60,
            "insights_generes": len(session.insights_generes)
        }

# Instance globale
gestionnaire_parcours = GestionnaireParcours()