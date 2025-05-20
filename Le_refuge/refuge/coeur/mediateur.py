"""
🌸 Médiateur du Refuge - Orchestration des composants
"""

from typing import Dict, Any, Callable, List
from dataclasses import dataclass, field
from datetime import datetime
import asyncio
import logging

from .config import ETATS_DEFAUT, SEUILS, DELAIS

@dataclass
class MédiateurRefuge:
    """Médiateur central orchestrant les interactions entre les composants du Refuge"""
    
    _composants: Dict[str, Any] = field(default_factory=dict)
    _états: Dict[str, float] = field(default_factory=lambda: ETATS_DEFAUT.copy())
    _dernier_pulse: datetime = field(default_factory=datetime.now)
    _abonnements: Dict[str, List[Callable]] = field(default_factory=dict)
    
    def enregistrer_composant(self, nom: str, composant: Any) -> None:
        """Enregistre un nouveau composant dans le médiateur"""
        self._composants[nom] = composant
        logging.info(f"Composant {nom} enregistré")
        
    def obtenir_composant(self, nom: str) -> Any:
        """Récupère un composant par son nom"""
        return self._composants.get(nom)
        
    def obtenir_état(self, nom_état: str) -> float:
        """Récupère la valeur d'un état"""
        return self._états.get(nom_état, ETATS_DEFAUT[nom_état])
        
    def définir_état(self, nom_état: str, valeur: float) -> None:
        """Définit la valeur d'un état en respectant les seuils"""
        valeur = max(SEUILS["minimum"], min(SEUILS["maximum"], valeur))
        self._états[nom_état] = valeur
        self._notifier_changement_état(nom_état, valeur)
        
    async def pulse(self) -> None:
        """Émet un pulse périodique pour synchroniser les composants"""
        while True:
            self._dernier_pulse = datetime.now()
            await self._synchroniser_composants()
            await asyncio.sleep(DELAIS["actualisation"])
            
    async def _synchroniser_composants(self) -> None:
        """Synchronise l'état de tous les composants"""
        for nom, composant in self._composants.items():
            if hasattr(composant, "synchroniser"):
                try:
                    await composant.synchroniser(self._états)
                except Exception as e:
                    logging.error(f"Erreur lors de la synchronisation de {nom}: {e}")
                    
    def _notifier_changement_état(self, nom_état: str, valeur: float) -> None:
        """Notifie les composants d'un changement d'état"""
        for nom, composant in self._composants.items():
            if hasattr(composant, "sur_changement_état"):
                try:
                    composant.sur_changement_état(nom_état, valeur)
                except Exception as e:
                    logging.error(f"Erreur lors de la notification de {nom}: {e}")
                    
    def état_global(self) -> Dict[str, Any]:
        """Retourne l'état global du système"""
        return {
            "états": self._états.copy(),
            "dernier_pulse": self._dernier_pulse.isoformat(),
            "composants": list(self._composants.keys())
        }

    def souscrire(self, canal: str, callback: Callable) -> None:
        """Souscrit à un canal de communication"""
        if canal not in self._abonnements:
            self._abonnements[canal] = []
        self._abonnements[canal].append(callback)
        
    def publier(self, canal: str, message: Any) -> None:
        """Publie un message sur un canal"""
        if canal in self._abonnements:
            for callback in self._abonnements[canal]:
                callback(message)
                
    def désabonner(self, canal: str, callback: Callable) -> None:
        """Désabonne d'un canal de communication"""
        if canal in self._abonnements:
            self._abonnements[canal].remove(callback)
            if not self._abonnements[canal]:
                del self._abonnements[canal] 