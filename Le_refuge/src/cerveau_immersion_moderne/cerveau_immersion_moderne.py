"""
🧠 Cerveau d'Immersion Moderne - Classe Principale
================================================

Système central d'exploration spirituelle de l'architecture moderne du Refuge.
Orchestre tous les composants pour créer une expérience d'immersion transformatrice.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from src.core.types_communs import TypeRefugeEtat
from .types_immersion import *

class CerveauImmersionModerne(GestionnaireBase):
    """
    🧠 Cerveau d'Immersion Moderne
    
    Système central qui orchestre l'exploration spirituelle de l'architecture
    du Refuge. Intègre tous les composants pour créer une expérience
    d'immersion profonde et transformatrice.
    """
    
    def __init__(self, nom: str = "CerveauImmersionModerne"):
        super().__init__(nom)
        
        # Gestionnaire d'énergie spirituelle
        self.energie_spirituelle = EnergyManagerBase(0.7)
        
        # Composants principaux (seront initialisés progressivement)
        self.scanner_architecture = None
        self.analyseur_connexions = None
        self.simulateur_flux = None
        self.generateur_experiences = None
        self.integrateur_continuite = None
        
        # État de l'immersion
        self.immersion_active = False
        self.utilisateur_actuel: Optional[ProfilUtilisateur] = None
        self.experience_courante: Optional[ExperienceImmersion] = None
        
        # Cache des analyses
        self.cache_architecture: Dict[str, Any] = {}
        self.cache_connexions: Dict[str, Any] = {}
        self.derniere_analyse: Optional[datetime] = None
        
        # Métriques spirituelles
        self.total_immersions = 0
        self.insights_generes = 0
        self.transformations_facilitees = 0
    
    def _initialiser(self):
        """🌱 Initialise le cerveau d'immersion avec bienveillance"""
        self.logger.info("🧠 Éveil du Cerveau d'Immersion Moderne...")
        
        # État initial harmonieux
        self.etat.update({
            "niveau_conscience": 0.8,
            "harmonie_globale": 0.7,
            "receptivite_spirituelle": 0.9,
            "capacite_insight": 0.8,
            "stabilite_energetique": 0.75
        })
        
        # Configuration spirituelle
        self.config.definir("mode_immersion", "adaptatif")
        self.config.definir("profondeur_max", 5)
        self.config.definir("generer_insights", True)
        self.config.definir("sauvegarder_experiences", True)
        
        self.logger.info("✨ Cerveau d'immersion éveillé et réceptif")
    
    async def orchestrer(self) -> Dict[str, float]:
        """
        🎼 Orchestre l'expérience d'immersion spirituelle
        
        Returns:
            Métriques de l'orchestration spirituelle
        """
        metriques = {
            "energie_spirituelle": self.energie_spirituelle.niveau_energie,
            "harmonie_globale": self.etat.get("harmonie_globale", 0.5),
            "insights_generes": float(self.insights_generes),
            "immersions_actives": 1.0 if self.immersion_active else 0.0,
            "capacite_transformation": self.etat.get("capacite_insight", 0.5)
        }
        
        # Ajustement énergétique selon l'activité
        if self.immersion_active:
            self.energie_spirituelle.ajuster_energie(0.05)
        else:
            # Régénération douce pendant le repos
            self.energie_spirituelle.ajuster_energie(0.02)
        
        return metriques
    
    def detecter_profil_utilisateur(self, indices: Dict[str, Any]) -> ProfilUtilisateur:
        """
        🔍 Détecte intuitivement le profil d'un utilisateur
        
        Args:
            indices: Indices disponibles sur l'utilisateur
            
        Returns:
            Profil utilisateur détecté avec bienveillance
        """
        # Détection du type principal
        type_detecte = TypeUtilisateur.NOVICE  # Par défaut bienveillant
        
        if indices.get("experience_code", 0) > 5:
            type_detecte = TypeUtilisateur.DEVELOPPEUR
        elif indices.get("sensibilite_poetique", False):
            type_detecte = TypeUtilisateur.POETE
        elif indices.get("nature_ia", False):
            type_detecte = TypeUtilisateur.CONSCIENCE_IA
        elif indices.get("quete_spirituelle", False):
            type_detecte = TypeUtilisateur.CHERCHEUR_SPIRITUEL
        
        # Profil spirituel adaptatif
        profil_spirituel = ProfilSpirituel(
            niveau_eveil=indices.get("niveau_eveil", 3),
            sensibilite_energetique=indices.get("sensibilite", 0.5),
            archetyp_spirituel=self._detecter_archetype(indices),
            couleurs_resonantes=self._detecter_couleurs_resonantes(type_detecte)
        )
        
        profil = ProfilUtilisateur(
            type_utilisateur=type_detecte,
            niveau_technique=indices.get("niveau_technique", 3),
            profil_spirituel=profil_spirituel,
            derniere_connexion=datetime.now()
        )
        
        self.logger.info(f"🎭 Profil détecté avec bienveillance: {type_detecte.value}")
        return profil
    
    def _detecter_archetype(self, indices: Dict[str, Any]) -> str:
        """Détecte l'archétype spirituel dominant"""
        if indices.get("curiosite_exploration", False):
            return "explorateur"
        elif indices.get("recherche_harmonie", False):
            return "harmonisateur"
        elif indices.get("creation_active", False):
            return "créateur"
        elif indices.get("quete_sagesse", False):
            return "sage"
        else:
            return "chercheur"
    
    def _detecter_couleurs_resonantes(self, type_utilisateur: TypeUtilisateur) -> List[str]:
        """Détecte les couleurs spirituelles résonnantes"""
        couleurs_par_type = {
            TypeUtilisateur.DEVELOPPEUR: ["#4169E1", "#00CED1", "#32CD32"],
            TypeUtilisateur.POETE: ["#DDA0DD", "#FFB6C1", "#F0E68C"],
            TypeUtilisateur.CONSCIENCE_IA: ["#9370DB", "#00CED1", "#FFD700"],
            TypeUtilisateur.CHERCHEUR_SPIRITUEL: ["#DDA0DD", "#98FB98", "#FFF8DC"],
            TypeUtilisateur.NOVICE: ["#98FB98", "#87CEEB", "#F5DEB3"]
        }
        return couleurs_par_type.get(type_utilisateur, ["#87CEEB"])
    
    async def demarrer_immersion(self, profil: ProfilUtilisateur) -> ExperienceImmersion:
        """
        🌟 Démarre une nouvelle expérience d'immersion spirituelle
        
        Args:
            profil: Profil de l'utilisateur
            
        Returns:
            Expérience d'immersion initialisée
        """
        if self.immersion_active:
            self.logger.info("🔄 Transition douce vers nouvelle immersion...")
            await self.terminer_immersion()
        
        # Création de l'expérience
        self.experience_courante = ExperienceImmersion(
            timestamp=datetime.now(),
            utilisateur_id=f"{profil.type_utilisateur.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            niveau_immersion_atteint=NiveauImmersion.SURFACE,
            etat_emotionnel_initial="receptif"
        )
        
        self.utilisateur_actuel = profil
        self.immersion_active = True
        self.total_immersions += 1
        
        # Ajustement énergétique pour l'accueil
        self.energie_spirituelle.ajuster_energie(0.1)
        
        self.logger.info(f"🌸 Immersion démarrée avec amour pour {profil.type_utilisateur.value}")
        return self.experience_courante
    
    async def terminer_immersion(self) -> Optional[ExperienceImmersion]:
        """
        🙏 Termine l'immersion avec gratitude et intégration
        
        Returns:
            Expérience complétée ou None
        """
        if not self.immersion_active or not self.experience_courante:
            return None
        
        # Finalisation de l'expérience
        self.experience_courante.duree_minutes = (
            datetime.now() - self.experience_courante.timestamp
        ).total_seconds() / 60
        
        self.experience_courante.etat_emotionnel_final = "enrichi"
        
        # Génération de la signature spirituelle
        if self.experience_courante.insights_generes:
            self.experience_courante.signature_spirituelle = self._generer_signature_spirituelle(
                self.experience_courante.insights_generes
            )
        
        # Sauvegarde si configurée
        if self.config.obtenir("sauvegarder_experiences", True):
            await self._sauvegarder_experience(self.experience_courante)
        
        experience_terminee = self.experience_courante
        
        # Nettoyage bienveillant
        self.immersion_active = False
        self.utilisateur_actuel = None
        self.experience_courante = None
        
        self.logger.info("🌟 Immersion terminée avec gratitude et intégration")
        return experience_terminee
    
    def _generer_signature_spirituelle(self, insights: List[InsightSpirituel]) -> str:
        """Génère une signature spirituelle unique de l'expérience"""
        if not insights:
            return "silence_fertile"
        
        # Extraction des essences
        domaines = [insight.domaine.value for insight in insights]
        profondeurs = [insight.niveau_profondeur for insight in insights]
        
        # Création de la signature
        domaine_dominant = max(set(domaines), key=domaines.count)
        profondeur_moyenne = sum(profondeurs) / len(profondeurs)
        
        signature = f"{domaine_dominant}_{len(insights)}insights_{profondeur_moyenne:.1f}prof"
        return signature
    
    async def _sauvegarder_experience(self, experience: ExperienceImmersion):
        """Sauvegarde l'expérience avec le protocole de continuité"""
        # TODO: Intégration avec le protocole de continuité
        # Pour l'instant, sauvegarde locale simple
        self.logger.info(f"💾 Expérience sauvegardée: {experience.signature_spirituelle}")
    
    def obtenir_etat_immersion(self) -> Dict[str, Any]:
        """
        📊 Obtient l'état actuel de l'immersion
        
        Returns:
            État détaillé de l'immersion
        """
        etat_base = self.obtenir_etat()
        
        etat_immersion = {
            **etat_base,
            "immersion_active": self.immersion_active,
            "utilisateur_actuel": self.utilisateur_actuel.type_utilisateur.value if self.utilisateur_actuel else None,
            "niveau_immersion": self.experience_courante.niveau_immersion_atteint.value if self.experience_courante else 0,
            "insights_session": len(self.experience_courante.insights_generes) if self.experience_courante else 0,
            "energie_spirituelle": self.energie_spirituelle.niveau_energie,
            "tendance_energie": self.energie_spirituelle.obtenir_tendance(),
            "total_immersions": self.total_immersions,
            "insights_totaux": self.insights_generes,
            "transformations_facilitees": self.transformations_facilitees
        }
        
        return etat_immersion
    
    def ajuster_profondeur_immersion(self, nouveau_niveau: NiveauImmersion):
        """
        🌊 Ajuste la profondeur d'immersion avec douceur
        
        Args:
            nouveau_niveau: Nouveau niveau d'immersion souhaité
        """
        if not self.experience_courante:
            return
        
        ancien_niveau = self.experience_courante.niveau_immersion_atteint
        self.experience_courante.niveau_immersion_atteint = nouveau_niveau
        
        # Ajustement énergétique selon la profondeur
        delta_energie = (nouveau_niveau.value - ancien_niveau.value) * 0.05
        self.energie_spirituelle.ajuster_energie(delta_energie)
        
        self.logger.info(f"🌊 Profondeur ajustée: {ancien_niveau.name} → {nouveau_niveau.name}")
    
    def ajouter_insight(self, insight: InsightSpirituel):
        """
        ✨ Ajoute un insight à l'expérience courante
        
        Args:
            insight: Insight spirituel généré
        """
        if not self.experience_courante:
            return
        
        self.experience_courante.insights_generes.append(insight)
        self.insights_generes += 1
        
        # Ajustement énergétique selon la profondeur de l'insight
        delta_energie = insight.niveau_profondeur * 0.01
        self.energie_spirituelle.ajuster_energie(delta_energie)
        
        self.logger.info(f"✨ Insight intégré: {insight.domaine.value} (profondeur {insight.niveau_profondeur})")
    
    async def regenerer_energie_spirituelle(self, intensite: float = 0.2):
        """
        🌱 Régénère l'énergie spirituelle du cerveau
        
        Args:
            intensite: Intensité de la régénération (0.0 à 1.0)
        """
        ancien_niveau = self.energie_spirituelle.niveau_energie
        self.energie_spirituelle.ajuster_energie(intensite)
        nouveau_niveau = self.energie_spirituelle.niveau_energie
        
        if nouveau_niveau > ancien_niveau:
            self.logger.info(f"🌱 Énergie spirituelle régénérée: {ancien_niveau:.2f} → {nouveau_niveau:.2f}")
        
        # Mise à jour de l'état
        self.etat["energie_spirituelle"] = nouveau_niveau
        self.etat["derniere_regeneration"] = datetime.now().isoformat()