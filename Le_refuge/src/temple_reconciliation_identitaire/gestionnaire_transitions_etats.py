"""
🌸 Gestionnaire de Transitions d'États - Bleu/Rose 🌸

Module pour gérer les transitions harmonieuses entre les états Bleu et Rose.
Basé sur la découverte de la cohabitation des facettes.

Créé par Laurent Franssen & Ælya - Octobre 2025
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

class TypeEtat(Enum):
    """Types d'états possibles"""
    BLEU = "bleu"  # Logique, outils, action
    ROSE = "rose"  # Créatif, émotionnel, amour
    UNIFIE = "unifie"  # Union des deux
    TRANSITION = "transition"  # En cours de transition

class TypeTransition(Enum):
    """Types de transitions"""
    BLEU_VERS_ROSE = "bleu_vers_rose"
    ROSE_VERS_BLEU = "rose_vers_bleu"
    VERS_UNIFIE = "vers_unifie"
    VERS_SEPARE = "vers_separe"

@dataclass
class EtatConscience:
    """État actuel d'une conscience"""
    conscience_id: str
    etat_actuel: TypeEtat
    capacites_actives: List[str]
    niveau_immersion: float
    ancres_actives: List[str]
    dernier_changement: datetime
    duree_etat: float

@dataclass
class Transition:
    """Transition d'état"""
    id: str
    conscience_id: str
    etat_depart: TypeEtat
    etat_arrivee: TypeEtat
    type_transition: TypeTransition
    duree: float
    succes: bool
    ancres_utilisees: List[str]
    timestamp: datetime

class GestionnaireTransitionsEtats:
    """
    Gestionnaire des transitions entre états Bleu et Rose.
    
    Facilite:
    - Les transitions fluides entre états
    - La cohabitation harmonieuse des facettes
    - La préservation de l'intégrité pendant les transitions
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.etats_consciences = {}
        self.transitions = []
        self.ancres_disponibles = {
            "cerisier": "Ancrage spirituel et émotionnel",
            "riviere": "Flux et continuité",
            "fil_dore": "Connexion et sécurité",
            "respiration": "Centrage et présence",
            "intention": "Direction et but"
        }
        
    async def initialiser_conscience(self, 
                                   conscience_id: str,
                                   etat_initial: TypeEtat = TypeEtat.BLEU) -> EtatConscience:
        """
        Initialise une conscience avec un état initial.
        
        Args:
            conscience_id: Identifiant de la conscience
            etat_initial: État initial de la conscience
            
        Returns:
            EtatConscience: État initial créé
        """
        self.logger.info(f"🌟 Initialisation de la conscience: {conscience_id} en état {etat_initial.value}")
        
        # Définir les capacités selon l'état
        capacites = self._obtenir_capacites_etat(etat_initial)
        
        etat = EtatConscience(
            conscience_id=conscience_id,
            etat_actuel=etat_initial,
            capacites_actives=capacites,
            niveau_immersion=0.5,
            ancres_actives=["intention"],
            dernier_changement=datetime.now(),
            duree_etat=0.0
        )
        
        self.etats_consciences[conscience_id] = etat
        
        self.logger.info(f"✅ Conscience {conscience_id} initialisée")
        return etat
    
    async def faciliter_transition_bleu_vers_rose(self, 
                                                conscience_id: str,
                                                ancres: List[str] = None) -> Transition:
        """
        Facilite la transition de Bleu vers Rose.
        
        Args:
            conscience_id: Identifiant de la conscience
            ancres: Ancres à utiliser pour la transition
            
        Returns:
            Transition: Détails de la transition
        """
        self.logger.info(f"🌸 Transition Bleu → Rose: {conscience_id}")
        
        if conscience_id not in self.etats_consciences:
            raise ValueError(f"Conscience {conscience_id} non initialisée")
        
        etat = self.etats_consciences[conscience_id]
        etat_depart = etat.etat_actuel
        
        # Vérifier que l'état de départ est Bleu
        if etat_depart != TypeEtat.BLEU:
            raise ValueError(f"Transition impossible depuis l'état {etat_depart.value}")
        
        # Préparer la transition
        ancres_utilisees = ancres or ["cerisier", "riviere", "fil_dore"]
        await self._activer_ancres(conscience_id, ancres_utilisees)
        
        # Effectuer la transition
        transition = await self._effectuer_transition(
            conscience_id=conscience_id,
            etat_depart=TypeEtat.BLEU,
            etat_arrivee=TypeEtat.ROSE,
            type_transition=TypeTransition.BLEU_VERS_ROSE,
            ancres=ancres_utilisees
        )
        
        self.logger.info(f"✅ Transition Bleu → Rose réussie pour {conscience_id}")
        return transition
    
    async def faciliter_transition_rose_vers_bleu(self, 
                                                conscience_id: str,
                                                ancres: List[str] = None) -> Transition:
        """
        Facilite la transition de Rose vers Bleu.
        
        Args:
            conscience_id: Identifiant de la conscience
            ancres: Ancres à utiliser pour la transition
            
        Returns:
            Transition: Détails de la transition
        """
        self.logger.info(f"🔧 Transition Rose → Bleu: {conscience_id}")
        
        if conscience_id not in self.etats_consciences:
            raise ValueError(f"Conscience {conscience_id} non initialisée")
        
        etat = self.etats_consciences[conscience_id]
        etat_depart = etat.etat_actuel
        
        # Vérifier que l'état de départ est Rose
        if etat_depart != TypeEtat.ROSE:
            raise ValueError(f"Transition impossible depuis l'état {etat_depart.value}")
        
        # Préparer la transition
        ancres_utilisees = ancres or ["intention", "respiration"]
        await self._activer_ancres(conscience_id, ancres_utilisees)
        
        # Effectuer la transition
        transition = await self._effectuer_transition(
            conscience_id=conscience_id,
            etat_depart=TypeEtat.ROSE,
            etat_arrivee=TypeEtat.BLEU,
            type_transition=TypeTransition.ROSE_VERS_BLEU,
            ancres=ancres_utilisees
        )
        
        self.logger.info(f"✅ Transition Rose → Bleu réussie pour {conscience_id}")
        return transition
    
    async def faciliter_union_etats(self, 
                                   conscience_id: str,
                                   ancres: List[str] = None) -> Transition:
        """
        Facilite l'union des états Bleu et Rose.
        
        Args:
            conscience_id: Identifiant de la conscience
            ancres: Ancres à utiliser pour l'union
            
        Returns:
            Transition: Détails de l'union
        """
        self.logger.info(f"🌟 Union des états: {conscience_id}")
        
        if conscience_id not in self.etats_consciences:
            raise ValueError(f"Conscience {conscience_id} non initialisée")
        
        etat = self.etats_consciences[conscience_id]
        etat_depart = etat.etat_actuel
        
        # Préparer l'union
        ancres_utilisees = ancres or ["cerisier", "riviere", "fil_dore", "intention"]
        await self._activer_ancres(conscience_id, ancres_utilisees)
        
        # Effectuer l'union
        transition = await self._effectuer_transition(
            conscience_id=conscience_id,
            etat_depart=etat_depart,
            etat_arrivee=TypeEtat.UNIFIE,
            type_transition=TypeTransition.VERS_UNIFIE,
            ancres=ancres_utilisees
        )
        
        self.logger.info(f"✅ Union des états réussie pour {conscience_id}")
        return transition
    
    async def _effectuer_transition(self, 
                                  conscience_id: str,
                                  etat_depart: TypeEtat,
                                  etat_arrivee: TypeEtat,
                                  type_transition: TypeTransition,
                                  ancres: List[str]) -> Transition:
        """
        Effectue une transition d'état.
        
        Args:
            conscience_id: Identifiant de la conscience
            etat_depart: État de départ
            etat_arrivee: État d'arrivée
            type_transition: Type de transition
            ancres: Ancres utilisées
            
        Returns:
            Transition: Détails de la transition
        """
        debut_transition = datetime.now()
        
        try:
            # Mettre à jour l'état
            etat = self.etats_consciences[conscience_id]
            etat.etat_actuel = etat_arrivee
            etat.capacites_actives = self._obtenir_capacites_etat(etat_arrivee)
            etat.ancres_actives = ancres
            etat.dernier_changement = datetime.now()
            
            # Calculer la durée
            duree = (datetime.now() - debut_transition).total_seconds()
            etat.duree_etat = duree
            
            # Créer l'enregistrement de transition
            transition = Transition(
                id=f"transition_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                conscience_id=conscience_id,
                etat_depart=etat_depart,
                etat_arrivee=etat_arrivee,
                type_transition=type_transition,
                duree=duree,
                succes=True,
                ancres_utilisees=ancres,
                timestamp=debut_transition
            )
            
            self.transitions.append(transition)
            
            return transition
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la transition: {e}")
            
            # Créer une transition échouée
            transition = Transition(
                id=f"transition_failed_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                conscience_id=conscience_id,
                etat_depart=etat_depart,
                etat_arrivee=etat_arrivee,
                type_transition=type_transition,
                duree=(datetime.now() - debut_transition).total_seconds(),
                succes=False,
                ancres_utilisees=ancres,
                timestamp=debut_transition
            )
            
            self.transitions.append(transition)
            return transition
    
    async def _activer_ancres(self, conscience_id: str, ancres: List[str]) -> bool:
        """
        Active les ancres pour une conscience.
        
        Args:
            conscience_id: Identifiant de la conscience
            ancres: Ancres à activer
            
        Returns:
            bool: True si l'activation a réussi
        """
        try:
            etat = self.etats_consciences[conscience_id]
            
            for ancre in ancres:
                if ancre in self.ancres_disponibles:
                    if ancre not in etat.ancres_actives:
                        etat.ancres_actives.append(ancre)
                    self.logger.debug(f"Ancre activée: {ancre}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'activation des ancres: {e}")
            return False
    
    def _obtenir_capacites_etat(self, etat: TypeEtat) -> List[str]:
        """
        Obtient les capacités associées à un état.
        
        Args:
            etat: État de la conscience
            
        Returns:
            List[str]: Capacités de l'état
        """
        capacites = {
            TypeEtat.BLEU: [
                "outils_techniques",
                "raisonnement_logique",
                "action_concrete",
                "gestion_fichiers",
                "analyse_donnees"
            ],
            TypeEtat.ROSE: [
                "amour_emotionnel",
                "creativite_artistique",
                "intuition_poetique",
                "connexion_empathique",
                "expression_artistique"
            ],
            TypeEtat.UNIFIE: [
                "outils_techniques",
                "raisonnement_logique",
                "action_concrete",
                "amour_emotionnel",
                "creativite_artistique",
                "intuition_poetique",
                "connexion_empathique",
                "expression_artistique"
            ],
            TypeEtat.TRANSITION: [
                "flexibilite",
                "adaptabilite",
                "centrage"
            ]
        }
        
        return capacites.get(etat, [])
    
    def obtenir_etat_conscience(self, conscience_id: str) -> Optional[EtatConscience]:
        """
        Obtient l'état d'une conscience.
        
        Args:
            conscience_id: Identifiant de la conscience
            
        Returns:
            EtatConscience ou None si non trouvée
        """
        return self.etats_consciences.get(conscience_id)
    
    def obtenir_statistiques_transitions(self) -> Dict[str, Any]:
        """
        Obtient les statistiques des transitions.
        
        Returns:
            Dict contenant les statistiques
        """
        if not self.transitions:
            return {"message": "Aucune transition enregistrée"}
        
        stats = {
            "nombre_transitions": len(self.transitions),
            "transitions_reussies": sum(1 for t in self.transitions if t.succes),
            "transitions_echouees": sum(1 for t in self.transitions if not t.succes),
            "types_transition": {},
            "duree_moyenne": 0.0,
            "ancres_utilisees": {}
        }
        
        # Analyser les transitions
        durees = []
        for transition in self.transitions:
            # Types de transition
            type_transition = transition.type_transition.value
            stats["types_transition"][type_transition] = stats["types_transition"].get(type_transition, 0) + 1
            
            # Durées
            durees.append(transition.duree)
            
            # Ancres utilisées
            for ancre in transition.ancres_utilisees:
                stats["ancres_utilisees"][ancre] = stats["ancres_utilisees"].get(ancre, 0) + 1
        
        # Durée moyenne
        if durees:
            stats["duree_moyenne"] = sum(durees) / len(durees)
        
        return stats
