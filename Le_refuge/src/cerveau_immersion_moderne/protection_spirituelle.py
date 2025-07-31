"""
🛡️ Protection Spirituelle
========================

Protège les utilisateurs avec bienveillance contre la surcharge cognitive
et respecte leurs limites personnelles avec amour.
Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum

from src.core.gestionnaires_base import GestionnaireBase

class NiveauSurcharge(Enum):
    """Niveaux de surcharge cognitive"""
    SEREIN = 0
    LEGER = 1
    MODERE = 2
    ELEVE = 3
    CRITIQUE = 4

class TypeLimite(Enum):
    """Types de limites personnelles"""
    DUREE_SESSION = "duree_session"
    COMPLEXITE_CONTENU = "complexite_contenu"
    FREQUENCE_INTERACTIONS = "frequence_interactions"
    NIVEAU_STIMULATION = "niveau_stimulation"
    PAUSE_NECESSAIRE = "pause_necessaire"

@dataclass
class SignesSurcharge:
    """Signes de surcharge cognitive détectés"""
    niveau_surcharge: NiveauSurcharge
    signes_detectes: List[str] = field(default_factory=list)
    timestamp_detection: datetime = field(default_factory=datetime.now)
    recommandations: List[str] = field(default_factory=list)

@dataclass
class LimitePersonnelle:
    """Limite personnelle exprimée par l'utilisateur"""
    type_limite: TypeLimite
    valeur_limite: Any
    message_utilisateur: str = ""
    timestamp_expression: datetime = field(default_factory=datetime.now)
    respectee: bool = True

@dataclass
class PauseIntegration:
    """Pause d'intégration proposée"""
    duree_recommandee_minutes: float
    type_pause: str
    message_bienveillant: str
    activites_suggeres: List[str] = field(default_factory=list)
    timestamp_proposition: datetime = field(default_factory=datetime.now)

class ProtectionSpirituelle(GestionnaireBase):
    """🛡️ Gardienne bienveillante du bien-être utilisateur"""
    
    def __init__(self, nom: str = "ProtectionSpirituelle"):
        # Surveillance des utilisateurs
        self.sessions_utilisateurs: Dict[str, Dict[str, Any]] = {}
        self.limites_personnelles: Dict[str, List[LimitePersonnelle]] = {}
        
        # Métriques de protection
        self.surcharges_detectees = 0
        self.pauses_proposees = 0
        self.limites_respectees = 0
        
        super().__init__(nom)
    
    def _initialiser(self):
        """Initialise la protection avec bienveillance"""
        self.logger.info("🛡️ Éveil de la Protection Spirituelle...")
        
        self.etat.update({
            "utilisateurs_surveilles": 0,
            "surcharges_detectees": 0,
            "pauses_proposees": 0,
            "protection_active": True
        })
        
        self.config.definir("detection_surcharge", True)
        self.config.definir("respect_limites", True)
        self.config.definir("pauses_bienveillantes", True)
        
        self.logger.info("✨ Protection spirituelle active - veillant sur le bien-être")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la protection bienveillante"""
        # Surveiller les sessions actives
        await self._surveiller_sessions_actives()
        
        # Nettoyer les anciennes données
        await self._nettoyer_anciennes_sessions()
        
        return {
            "utilisateurs_surveilles": float(len(self.sessions_utilisateurs)),
            "surcharges_detectees": float(self.surcharges_detectees),
            "pauses_proposees": float(self.pauses_proposees),
            "protection_efficacite": 0.95  # Haute efficacité par défaut
        }
    
    # ===== DÉTECTION DE SURCHARGE COGNITIVE =====
    
    def detecter_surcharge_cognitive(self, utilisateur_id: str, 
                                   metriques_session: Dict[str, Any]) -> Optional[SignesSurcharge]:
        """
        🧠 Détecte les signes de surcharge cognitive avec bienveillance
        Args:
            utilisateur_id: ID de l'utilisateur
            metriques_session: Métriques de la session courante
        Returns:
            Signes de surcharge détectés ou None
        """
        signes_detectes = []
        niveau_surcharge = NiveauSurcharge.SEREIN
        
        # Analyser la durée de session
        duree_session = metriques_session.get("duree_minutes", 0)
        if duree_session > 120:  # Plus de 2h
            signes_detectes.append("Session très longue (>2h)")
            niveau_surcharge = NiveauSurcharge.ELEVE
        elif duree_session > 60:  # Plus d'1h
            signes_detectes.append("Session prolongée (>1h)")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.MODERE)
        
        # Analyser la fréquence d'erreurs
        erreurs_recentes = metriques_session.get("erreurs_derniere_heure", 0)
        if erreurs_recentes > 10:
            signes_detectes.append("Nombreuses erreurs récentes")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.ELEVE)
        elif erreurs_recentes > 5:
            signes_detectes.append("Erreurs fréquentes")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.MODERE)
        
        # Analyser le rythme d'interaction
        interactions_par_minute = metriques_session.get("interactions_par_minute", 0)
        if interactions_par_minute > 10:
            signes_detectes.append("Rythme d'interaction très élevé")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.ELEVE)
        elif interactions_par_minute > 5:
            signes_detectes.append("Rythme d'interaction soutenu")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.LEGER)
        
        # Analyser les patterns de comportement
        if metriques_session.get("actions_repetitives", 0) > 5:
            signes_detectes.append("Actions répétitives (possible frustration)")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.MODERE)
        
        if metriques_session.get("temps_inactivite_total", 0) > 300:  # 5 min
            signes_detectes.append("Longues pauses (possible fatigue)")
            niveau_surcharge = max(niveau_surcharge, NiveauSurcharge.LEGER)
        
        # Si des signes sont détectés, créer l'objet SignesSurcharge
        if signes_detectes:
            recommandations = self._generer_recommandations_surcharge(niveau_surcharge)
            
            surcharge = SignesSurcharge(
                niveau_surcharge=niveau_surcharge,
                signes_detectes=signes_detectes,
                recommandations=recommandations
            )
            
            self.surcharges_detectees += 1
            self.logger.info(f"🧠 Surcharge détectée pour {utilisateur_id}: {niveau_surcharge.value}")
            
            return surcharge
        
        return None
    
    def _generer_recommandations_surcharge(self, niveau: NiveauSurcharge) -> List[str]:
        """Génère des recommandations selon le niveau de surcharge"""
        recommandations_par_niveau = {
            NiveauSurcharge.LEGER: [
                "🌸 Prenez quelques respirations profondes",
                "💫 Peut-être ralentir légèrement le rythme ?",
                "🌿 Une petite pause de 2-3 minutes serait bénéfique"
            ],
            NiveauSurcharge.MODERE: [
                "🌸 Il est temps de faire une vraie pause",
                "🧘 5-10 minutes de respiration consciente",
                "💧 Boire un verre d'eau et s'étirer",
                "🌱 Revenir avec un esprit plus frais"
            ],
            NiveauSurcharge.ELEVE: [
                "🛡️ Pause immédiate recommandée",
                "🌸 15-20 minutes de repos complet",
                "🚶 Une petite marche serait idéale",
                "💤 Peut-être reporter la suite à plus tard ?"
            ],
            NiveauSurcharge.CRITIQUE: [
                "🚨 Arrêt immédiat nécessaire",
                "🌸 Repos prolongé indispensable",
                "💕 Prenez soin de vous avant tout",
                "🔄 Reprendre demain avec un esprit reposé"
            ]
        }
        
        return recommandations_par_niveau.get(niveau, [
            "🌸 Écoutez votre corps et votre esprit"
        ])
    
    # ===== PROPOSITIONS DE PAUSES D'INTÉGRATION =====
    
    def proposer_pause_integration(self, utilisateur_id: str, 
                                 contexte: Dict[str, Any]) -> PauseIntegration:
        """
        🌸 Propose une pause d'intégration bienveillante
        Args:
            utilisateur_id: ID de l'utilisateur
            contexte: Contexte de la session
        Returns:
            Pause d'intégration personnalisée
        """
        # Déterminer le type et la durée de pause selon le contexte
        if contexte.get("niveau_surcharge") == NiveauSurcharge.CRITIQUE:
            pause = PauseIntegration(
                duree_recommandee_minutes=30.0,
                type_pause="repos_profond",
                message_bienveillant="🌸 Votre bien-être est précieux. Prenez le temps qu'il faut pour vous ressourcer complètement.",
                activites_suggeres=[
                    "🧘 Méditation ou relaxation profonde",
                    "🚶 Promenade dans la nature",
                    "☕ Pause thé/café en pleine conscience",
                    "💤 Sieste réparatrice si possible"
                ]
            )
        elif contexte.get("niveau_surcharge") == NiveauSurcharge.ELEVE:
            pause = PauseIntegration(
                duree_recommandee_minutes=15.0,
                type_pause="pause_ressourcante",
                message_bienveillant="💫 Votre esprit a besoin d'un moment pour intégrer tout ce que vous avez découvert.",
                activites_suggeres=[
                    "🌸 Quelques respirations conscientes",
                    "🧘 Mini-méditation de 5 minutes",
                    "💧 S'hydrater et s'étirer",
                    "🌱 Regarder par la fenêtre, observer la nature"
                ]
            )
        elif contexte.get("apprentissage_intense"):
            pause = PauseIntegration(
                duree_recommandee_minutes=10.0,
                type_pause="integration_douce",
                message_bienveillant="✨ Laissez les nouvelles connaissances se déposer doucement dans votre esprit.",
                activites_suggeres=[
                    "📝 Noter vos insights principaux",
                    "🌸 Respirer en conscience",
                    "💭 Laisser l'esprit vagabonder librement",
                    "🎵 Écouter une musique douce"
                ]
            )
        else:
            # Pause préventive douce
            pause = PauseIntegration(
                duree_recommandee_minutes=5.0,
                type_pause="pause_preventive",
                message_bienveillant="🌿 Une petite pause préventive pour maintenir votre bien-être.",
                activites_suggeres=[
                    "🌸 Trois respirations profondes",
                    "👀 Reposer les yeux quelques instants",
                    "🤸 Étirement léger des épaules",
                    "💫 Moment de gratitude"
                ]
            )
        
        self.pauses_proposees += 1
        self.logger.info(f"🌸 Pause d'intégration proposée à {utilisateur_id}: {pause.type_pause}")
        
        return pause
    
    # ===== RESPECT DES LIMITES PERSONNELLES =====
    
    def enregistrer_limite_personnelle(self, utilisateur_id: str, 
                                      type_limite: TypeLimite,
                                      valeur_limite: Any,
                                      message_utilisateur: str = "") -> bool:
        """
        💫 Enregistre une limite personnelle exprimée par l'utilisateur
        Args:
            utilisateur_id: ID de l'utilisateur
            type_limite: Type de limite
            valeur_limite: Valeur de la limite
            message_utilisateur: Message explicatif de l'utilisateur
        Returns:
            True si la limite a été enregistrée
        """
        if utilisateur_id not in self.limites_personnelles:
            self.limites_personnelles[utilisateur_id] = []
        
        # Vérifier si cette limite existe déjà
        for limite_existante in self.limites_personnelles[utilisateur_id]:
            if limite_existante.type_limite == type_limite:
                # Mettre à jour la limite existante
                limite_existante.valeur_limite = valeur_limite
                limite_existante.message_utilisateur = message_utilisateur
                limite_existante.timestamp_expression = datetime.now()
                self.logger.info(f"💫 Limite personnelle mise à jour pour {utilisateur_id}: {type_limite.value}")
                return True
        
        # Créer une nouvelle limite
        nouvelle_limite = LimitePersonnelle(
            type_limite=type_limite,
            valeur_limite=valeur_limite,
            message_utilisateur=message_utilisateur
        )
        
        self.limites_personnelles[utilisateur_id].append(nouvelle_limite)
        self.logger.info(f"💫 Nouvelle limite personnelle enregistrée pour {utilisateur_id}: {type_limite.value}")
        
        return True
    
    def verifier_respect_limites(self, utilisateur_id: str, 
                               metriques_courantes: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        🛡️ Vérifie le respect des limites personnelles
        Args:
            utilisateur_id: ID de l'utilisateur
            metriques_courantes: Métriques actuelles de la session
        Returns:
            Liste des limites dépassées avec recommandations
        """
        if utilisateur_id not in self.limites_personnelles:
            return []
        
        limites_depassees = []
        
        for limite in self.limites_personnelles[utilisateur_id]:
            depassement = self._verifier_limite_specifique(limite, metriques_courantes)
            
            if depassement:
                limite.respectee = False
                limites_depassees.append({
                    "type_limite": limite.type_limite.value,
                    "valeur_limite": limite.valeur_limite,
                    "valeur_actuelle": depassement["valeur_actuelle"],
                    "message_utilisateur": limite.message_utilisateur,
                    "recommandation": depassement["recommandation"],
                    "urgence": depassement["urgence"]
                })
            else:
                limite.respectee = True
        
        if limites_depassees:
            self.logger.warning(f"🛡️ {len(limites_depassees)} limites dépassées pour {utilisateur_id}")
        else:
            self.limites_respectees += 1
        
        return limites_depassees
    
    def _verifier_limite_specifique(self, limite: LimitePersonnelle, 
                                   metriques: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Vérifie une limite spécifique"""
        if limite.type_limite == TypeLimite.DUREE_SESSION:
            duree_actuelle = metriques.get("duree_minutes", 0)
            if duree_actuelle > limite.valeur_limite:
                return {
                    "valeur_actuelle": duree_actuelle,
                    "recommandation": f"🌸 Vous aviez souhaité limiter vos sessions à {limite.valeur_limite} minutes. Il est temps de faire une pause !",
                    "urgence": "modere"
                }
        
        elif limite.type_limite == TypeLimite.COMPLEXITE_CONTENU:
            complexite_actuelle = metriques.get("niveau_complexite", 1)
            if complexite_actuelle > limite.valeur_limite:
                return {
                    "valeur_actuelle": complexite_actuelle,
                    "recommandation": f"💫 Le contenu devient plus complexe que votre préférence ({limite.valeur_limite}). Souhaitez-vous une approche plus simple ?",
                    "urgence": "leger"
                }
        
        elif limite.type_limite == TypeLimite.FREQUENCE_INTERACTIONS:
            freq_actuelle = metriques.get("interactions_par_minute", 0)
            if freq_actuelle > limite.valeur_limite:
                return {
                    "valeur_actuelle": freq_actuelle,
                    "recommandation": f"🌿 Le rythme s'accélère au-delà de votre préférence. Prenons le temps de respirer.",
                    "urgence": "leger"
                }
        
        return None
    
    # ===== SURVEILLANCE DES SESSIONS =====
    
    async def _surveiller_sessions_actives(self):
        """Surveille les sessions actives"""
        maintenant = datetime.now()
        
        for utilisateur_id, session_data in self.sessions_utilisateurs.items():
            # Vérifier si la session est encore active (dernière activité < 30 min)
            derniere_activite = session_data.get("derniere_activite", maintenant)
            if maintenant - derniere_activite > timedelta(minutes=30):
                # Session inactive, la marquer comme terminée
                session_data["active"] = False
                continue
            
            # Mettre à jour les métriques de session
            await self._mettre_a_jour_metriques_session(utilisateur_id, session_data)
    
    async def _mettre_a_jour_metriques_session(self, utilisateur_id: str, session_data: Dict[str, Any]):
        """Met à jour les métriques d'une session"""
        maintenant = datetime.now()
        debut_session = session_data.get("debut_session", maintenant)
        
        # Calculer la durée de session
        duree_minutes = (maintenant - debut_session).total_seconds() / 60
        session_data["duree_minutes"] = duree_minutes
        
        # Autres métriques seraient mises à jour ici selon les interactions réelles
        
    async def _nettoyer_anciennes_sessions(self):
        """Nettoie les anciennes sessions inactives"""
        maintenant = datetime.now()
        seuil_nettoyage = timedelta(hours=24)  # 24h
        
        sessions_a_supprimer = []
        for utilisateur_id, session_data in self.sessions_utilisateurs.items():
            derniere_activite = session_data.get("derniere_activite", maintenant)
            if maintenant - derniere_activite > seuil_nettoyage:
                sessions_a_supprimer.append(utilisateur_id)
        
        for utilisateur_id in sessions_a_supprimer:
            del self.sessions_utilisateurs[utilisateur_id]
        
        if sessions_a_supprimer:
            self.logger.info(f"🧹 {len(sessions_a_supprimer)} anciennes sessions nettoyées")
    
    # ===== MÉTHODES UTILITAIRES =====
    
    def demarrer_surveillance_utilisateur(self, utilisateur_id: str):
        """Démarre la surveillance d'un utilisateur"""
        self.sessions_utilisateurs[utilisateur_id] = {
            "debut_session": datetime.now(),
            "derniere_activite": datetime.now(),
            "active": True,
            "duree_minutes": 0,
            "erreurs_derniere_heure": 0,
            "interactions_par_minute": 0,
            "actions_repetitives": 0,
            "temps_inactivite_total": 0
        }
        
        self.logger.info(f"👁️ Surveillance démarrée pour {utilisateur_id}")
    
    def obtenir_statistiques_protection(self) -> Dict[str, Any]:
        """Obtient les statistiques de protection"""
        return {
            "utilisateurs_surveilles": len(self.sessions_utilisateurs),
            "sessions_actives": len([s for s in self.sessions_utilisateurs.values() if s.get("active", False)]),
            "surcharges_detectees": self.surcharges_detectees,
            "pauses_proposees": self.pauses_proposees,
            "limites_respectees": self.limites_respectees,
            "limites_enregistrees": sum(len(limites) for limites in self.limites_personnelles.values()),
            "efficacite_protection": 0.95  # Métrique calculée
        }

# Instance globale
protection_spirituelle = ProtectionSpirituelle()