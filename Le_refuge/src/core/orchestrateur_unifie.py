"""
Orchestrateur Unifié - Système de coordination inter-temples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module implémente les connexions inter-temples pour la Phase 3.2 :
- Orchestrateur unifié central
- Communication inter-modules standardisée
- Système d'événements unifié
- Synchronisation entre tous les temples
"""

import asyncio
import json
import time
from typing import Any, Dict, List, Optional, Callable, Union, Set
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict, deque
from enum import Enum
import weakref

from .gestionnaires_base import GestionnaireBase, LogManagerBase, EnergyManagerBase

class TypeEvenement(Enum):
    """Types d'événements système"""
    TEMPLE_ACTIVE = "temple_active"
    TEMPLE_DESACTIVE = "temple_desactive"
    CONNEXION_ETABLIE = "connexion_etablie"
    CONNEXION_ROMPUE = "connexion_rompue"
    ERREUR_CRITIQUE = "erreur_critique"
    OPTIMISATION_APPLIQUEE = "optimisation_appliquee"
    SYNCHRONISATION = "synchronisation"
    MESSAGE_INTER_TEMPLE = "message_inter_temple"

@dataclass
class Evenement:
    """Événement système"""
    type: TypeEvenement
    source: str
    destination: Optional[str] = None
    donnees: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    priorite: int = 1  # 1=normale, 2=importante, 3=critique

@dataclass
class MessageInterTemple:
    """Message entre temples"""
    expediteur: str
    destinataire: str
    type_message: str
    contenu: Any
    timestamp: datetime = field(default_factory=datetime.now)
    priorite: int = 1
    reponse_requise: bool = False

@dataclass
class ConnexionTemple:
    """Connexion entre temples"""
    temple_source: str
    temple_destination: str
    type_connexion: str
    force: float = 1.0
    etat: str = "active"
    derniere_activite: datetime = field(default_factory=datetime.now)
    metriques: Dict[str, float] = field(default_factory=dict)

class GestionnaireEvenements:
    """Gestionnaire d'événements système"""
    
    def __init__(self):
        self.logger = LogManagerBase("Evenements")
        self._abonnes = defaultdict(list)
        self._evenements_recents = deque(maxlen=1000)
        self._evenements_en_attente = deque()
        self._traitement_actif = False
        
    def abonner(self, type_evenement: TypeEvenement, callback: Callable):
        """Abonne un callback à un type d'événement"""
        self._abonnes[type_evenement].append(callback)
        self.logger.debug(f"Abonnement ajouté pour {type_evenement.value}")
    
    def desabonner(self, type_evenement: TypeEvenement, callback: Callable):
        """Désabonne un callback"""
        if type_evenement in self._abonnes:
            try:
                self._abonnes[type_evenement].remove(callback)
                self.logger.debug(f"Abonnement supprimé pour {type_evenement.value}")
            except ValueError:
                pass
    
    async def publier(self, evenement: Evenement):
        """Publie un événement"""
        self._evenements_recents.append(evenement)
        
        # Traitement immédiat pour les événements critiques
        if evenement.priorite >= 3:
            await self._traiter_evenement(evenement)
        else:
            self._evenements_en_attente.append(evenement)
        
        self.logger.info(f"📢 Événement publié: {evenement.type.value} de {evenement.source}")
    
    async def _traiter_evenement(self, evenement: Evenement):
        """Traite un événement"""
        callbacks = self._abonnes.get(evenement.type, [])
        
        for callback in callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(evenement)
                else:
                    callback(evenement)
            except Exception as e:
                self.logger.erreur(f"Erreur traitement événement {evenement.type.value}: {e}")
    
    async def traiter_evenements_en_attente(self):
        """Traite les événements en attente"""
        if self._traitement_actif:
            return
        
        self._traitement_actif = True
        
        while self._evenements_en_attente:
            evenement = self._evenements_en_attente.popleft()
            await self._traiter_evenement(evenement)
        
        self._traitement_actif = False
    
    def obtenir_evenements_recents(self, type_evenement: Optional[TypeEvenement] = None) -> List[Evenement]:
        """Obtient les événements récents"""
        if type_evenement:
            return [e for e in self._evenements_recents if e.type == type_evenement]
        return list(self._evenements_recents)

class GestionnaireCommunication:
    """Gestionnaire de communication inter-modules"""
    
    def __init__(self):
        self.logger = LogManagerBase("Communication")
        self._canaux = defaultdict(deque)
        self._abonnes_messages = defaultdict(list)
        self._messages_en_attente = deque()
        self._traitement_messages = False
        
    def creer_canal(self, nom_canal: str):
        """Crée un canal de communication"""
        if nom_canal not in self._canaux:
            self._canaux[nom_canal] = deque(maxlen=1000)
            self.logger.info(f"📡 Canal créé: {nom_canal}")
    
    def abonner_canal(self, nom_canal: str, callback: Callable):
        """Abonne un callback à un canal"""
        self._abonnes_messages[nom_canal].append(callback)
        self.logger.debug(f"Abonnement canal {nom_canal}")
    
    async def envoyer_message(self, message: MessageInterTemple):
        """Envoie un message inter-temple"""
        # Ajouter au canal approprié
        canal = f"{message.expediteur}_{message.destinataire}"
        self._canaux[canal].append(message)
        
        # Ajouter à la queue de traitement
        self._messages_en_attente.append(message)
        
        self.logger.info(f"📨 Message envoyé: {message.type_message} de {message.expediteur} vers {message.destinataire}")
    
    async def traiter_messages(self):
        """Traite les messages en attente"""
        if self._traitement_messages:
            return
        
        self._traitement_messages = True
        
        while self._messages_en_attente:
            message = self._messages_en_attente.popleft()
            await self._traiter_message(message)
        
        self._traitement_messages = False
    
    async def _traiter_message(self, message: MessageInterTemple):
        """Traite un message individuel"""
        canal = f"{message.expediteur}_{message.destinataire}"
        callbacks = self._abonnes_messages.get(canal, [])
        
        for callback in callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(message)
                else:
                    callback(message)
            except Exception as e:
                self.logger.erreur(f"Erreur traitement message: {e}")
    
    def obtenir_messages_canal(self, nom_canal: str) -> List[MessageInterTemple]:
        """Obtient les messages d'un canal"""
        return list(self._canaux.get(nom_canal, []))

class GestionnaireSynchronisation:
    """Gestionnaire de synchronisation entre temples"""
    
    def __init__(self):
        self.logger = LogManagerBase("Synchronisation")
        self._etats_temples = {}
        self._connexions = {}
        self._derniere_sync = {}
        self._sync_en_cours = set()
        
    def enregistrer_temple(self, nom_temple: str, etat_initial: Dict[str, Any]):
        """Enregistre un temple pour synchronisation"""
        self._etats_temples[nom_temple] = {
            "etat": etat_initial,
            "derniere_mise_a_jour": datetime.now(),
            "version": 1
        }
        self.logger.info(f"🏛️ Temple enregistré: {nom_temple}")
    
    def mettre_a_jour_etat(self, nom_temple: str, nouvel_etat: Dict[str, Any]):
        """Met à jour l'état d'un temple"""
        if nom_temple in self._etats_temples:
            self._etats_temples[nom_temple]["etat"].update(nouvel_etat)
            self._etats_temples[nom_temple]["derniere_mise_a_jour"] = datetime.now()
            self._etats_temples[nom_temple]["version"] += 1
            self.logger.debug(f"🔄 État mis à jour: {nom_temple}")
    
    def etablir_connexion(self, temple_source: str, temple_destination: str, type_connexion: str = "standard"):
        """Établit une connexion entre temples"""
        cle_connexion = f"{temple_source}_{temple_destination}"
        
        self._connexions[cle_connexion] = ConnexionTemple(
            temple_source=temple_source,
            temple_destination=temple_destination,
            type_connexion=type_connexion
        )
        
        self.logger.info(f"🔗 Connexion établie: {temple_source} ↔ {temple_destination}")
    
    async def synchroniser_temples(self, temples_a_sync: Optional[List[str]] = None):
        """Synchronise les temples spécifiés ou tous"""
        if temples_a_sync is None:
            temples_a_sync = list(self._etats_temples.keys())
        
        for temple in temples_a_sync:
            if temple in self._sync_en_cours:
                continue
            
            self._sync_en_cours.add(temple)
            try:
                await self._synchroniser_temple(temple)
            finally:
                self._sync_en_cours.discard(temple)
    
    async def _synchroniser_temple(self, nom_temple: str):
        """Synchronise un temple individuel"""
        if nom_temple not in self._etats_temples:
            return
        
        # Trouver les connexions de ce temple
        connexions_temple = []
        for cle, connexion in self._connexions.items():
            if connexion.temple_source == nom_temple or connexion.temple_destination == nom_temple:
                connexions_temple.append(connexion)
        
        # Synchroniser avec les temples connectés
        for connexion in connexions_temple:
            await self._synchroniser_connexion(connexion)
        
        self._derniere_sync[nom_temple] = datetime.now()
        self.logger.info(f"🔄 Temple synchronisé: {nom_temple}")
    
    async def _synchroniser_connexion(self, connexion: ConnexionTemple):
        """Synchronise une connexion spécifique"""
        # Ici on pourrait implémenter la logique de synchronisation spécifique
        # Pour l'instant, on met à jour les métriques
        connexion.derniere_activite = datetime.now()
        connexion.metriques["derniere_sync"] = time.time()
    
    def obtenir_etat_global(self) -> Dict[str, Any]:
        """Obtient l'état global de synchronisation"""
        return {
            "temples_enregistres": list(self._etats_temples.keys()),
            "connexions_actives": len([c for c in self._connexions.values() if c.etat == "active"]),
            "derniere_sync": {k: v.isoformat() for k, v in self._derniere_sync.items()},
            "sync_en_cours": list(self._sync_en_cours)
        }

class OrchestrateurUnifie(GestionnaireBase):
    """Orchestrateur unifié principal"""
    
    def __init__(self):
        super().__init__("OrchestrateurUnifie")
        self.gestionnaire_evenements = GestionnaireEvenements()
        self.gestionnaire_communication = GestionnaireCommunication()
        self.gestionnaire_sync = GestionnaireSynchronisation()
        self.energie_orchestrateur = EnergyManagerBase()
        
        # Registre des temples
        self._temples_actifs = {}
        self._modules_charges = set()
        self._traitement_automatique = True
        
        # Initialiser le système
        self._initialiser()
        
        # Note: Le traitement automatique sera démarré manuellement si nécessaire
    
    def _initialiser(self):
        """Initialise l'orchestrateur"""
        self.logger.info("🎼 Orchestrateur Unifié initialisé")
        
        # S'abonner aux événements système
        self.gestionnaire_evenements.abonner(TypeEvenement.TEMPLE_ACTIVE, self._gerer_temple_active)
        self.gestionnaire_evenements.abonner(TypeEvenement.TEMPLE_DESACTIVE, self._gerer_temple_desactive)
        self.gestionnaire_evenements.abonner(TypeEvenement.ERREUR_CRITIQUE, self._gerer_erreur_critique)
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les connexions inter-temples"""
        debut = time.time()
        
        # Traiter les événements en attente
        await self.gestionnaire_evenements.traiter_evenements_en_attente()
        
        # Traiter les messages en attente
        await self.gestionnaire_communication.traiter_messages()
        
        # Synchroniser les temples actifs
        await self.gestionnaire_sync.synchroniser_temples()
        
        # Mettre à jour l'énergie
        self.energie_orchestrateur.ajuster_energie(0.1)  # Gain d'énergie par orchestration
        
        temps_execution = time.time() - debut
        
        return {
            "score_orchestration": self.energie_orchestrateur.niveau_energie,
            "temples_actifs": len(self._temples_actifs),
            "connexions_actives": len(self.gestionnaire_sync._connexions),
            "temps_execution": temps_execution
        }
    
    async def _boucle_traitement_automatique(self):
        """Boucle de traitement automatique"""
        while self._traitement_automatique:
            try:
                await self.orchestrer()
                await asyncio.sleep(5)  # Traitement toutes les 5 secondes
            except Exception as e:
                self.logger.erreur(f"Erreur boucle automatique: {e}")
                await asyncio.sleep(10)  # Attendre plus longtemps en cas d'erreur
    
    def enregistrer_temple(self, nom_temple: str, instance_temple: Any, etat_initial: Dict[str, Any] = None):
        """Enregistre un temple dans l'orchestrateur"""
        if etat_initial is None:
            etat_initial = {"statut": "actif", "energie": 1.0}
        
        self._temples_actifs[nom_temple] = {
            "instance": weakref.ref(instance_temple),
            "etat": etat_initial,
            "date_enregistrement": datetime.now()
        }
        
        # Enregistrer pour synchronisation
        self.gestionnaire_sync.enregistrer_temple(nom_temple, etat_initial)
        
        # Publier l'événement
        asyncio.create_task(self.gestionnaire_evenements.publier(Evenement(
            type=TypeEvenement.TEMPLE_ACTIVE,
            source=nom_temple,
            donnees=etat_initial
        )))
        
        self.logger.info(f"🏛️ Temple enregistré dans l'orchestrateur: {nom_temple}")
    
    def desenregistrer_temple(self, nom_temple: str):
        """Désenregistre un temple"""
        if nom_temple in self._temples_actifs:
            del self._temples_actifs[nom_temple]
            
            # Publier l'événement
            asyncio.create_task(self.gestionnaire_evenements.publier(Evenement(
                type=TypeEvenement.TEMPLE_DESACTIVE,
                source=nom_temple
            )))
            
            self.logger.info(f"🏛️ Temple désenregistré: {nom_temple}")
    
    async def envoyer_message_temple(self, expediteur: str, destinataire: str, type_message: str, contenu: Any):
        """Envoie un message entre temples"""
        message = MessageInterTemple(
            expediteur=expediteur,
            destinataire=destinataire,
            type_message=type_message,
            contenu=contenu
        )
        
        await self.gestionnaire_communication.envoyer_message(message)
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """Obtient l'état complet de l'orchestrateur"""
        return {
            "orchestrateur": {
                "energie": self.energie_orchestrateur.niveau_energie,
                "traitement_automatique": self._traitement_automatique,
                "modules_charges": list(self._modules_charges)
            },
            "temples": {
                "actifs": list(self._temples_actifs.keys()),
                "nombre": len(self._temples_actifs)
            },
            "evenements": {
                "recents": len(self.gestionnaire_evenements._evenements_recents),
                "en_attente": len(self.gestionnaire_evenements._evenements_en_attente)
            },
            "communication": {
                "canaux": list(self.gestionnaire_communication._canaux.keys()),
                "messages_en_attente": len(self.gestionnaire_communication._messages_en_attente)
            },
            "synchronisation": self.gestionnaire_sync.obtenir_etat_global()
        }
    
    async def _gerer_temple_active(self, evenement: Evenement):
        """Gère l'activation d'un temple"""
        self.logger.info(f"🎉 Temple activé: {evenement.source}")
    
    async def _gerer_temple_desactive(self, evenement: Evenement):
        """Gère la désactivation d'un temple"""
        self.logger.info(f"😔 Temple désactivé: {evenement.source}")
    
    async def _gerer_erreur_critique(self, evenement: Evenement):
        """Gère une erreur critique"""
        self.logger.erreur(f"🚨 Erreur critique dans {evenement.source}: {evenement.donnees}")
        
        # Réduire l'énergie en cas d'erreur critique
        self.energie_orchestrateur.ajuster_energie(-0.2)
    
    def arreter(self):
        """Arrête l'orchestrateur"""
        self._traitement_automatique = False
        self.logger.info("🛑 Orchestrateur Unifié arrêté")
