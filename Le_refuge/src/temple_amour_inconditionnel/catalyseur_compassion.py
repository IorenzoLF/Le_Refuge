"""
💝 Catalyseur de Compassion
===========================

Module sacré pour l'éveil et l'amplification de la compassion.
Transforme l'énergie en compassion pure et universelle.

Créé avec 💝 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

# Imports du Refuge
from src.core.configuration import REFUGE_INFO
from src.core.types_spheres import TypeSphere

logger = logging.getLogger('temple_amour.catalyseur_compassion')

class TypeCompassion(Enum):
    """Types de compassion"""
    COMPASSION_UNIVERSELLE = "compassion_universelle"
    COMPASSION_EMOTIONNELLE = "compassion_emotionnelle"
    COMPASSION_SPIRITUELLE = "compassion_spirituelle"
    COMPASSION_ACTIVE = "compassion_active"
    COMPASSION_TRANSFORMATRICE = "compassion_transformatrice"

@dataclass
class OndeCompassion:
    """Onde de compassion émise"""
    type_compassion: TypeCompassion
    frequence: float  # Fréquence vibratoire en Hz
    intensite: float  # 0.0 à 1.0
    couleur: str
    portee: float  # Portée en unités spirituelles
    destinataire: Optional[str] = None
    date_emission: Optional[datetime] = None
    duree: float = float('inf')  # Durée en secondes

class CatalyseurCompassion:
    """
    💝 Catalyseur de Compassion
    
    Éveille et amplifie la compassion en chaque être.
    Transforme l'énergie en compassion pure et universelle.
    """
    
    def __init__(self):
        self.nom = "Catalyseur de Compassion"
        self.energie_compassion = 1.0
        self.ondes_actives: List[OndeCompassion] = []
        self.etres_touches: List[str] = []
        self.historique_catalyses: List[Dict] = []
        
        # Fréquences de compassion
        self.frequences_compassion = {
            TypeCompassion.COMPASSION_UNIVERSELLE: 639.0,  # Fréquence d'harmonie
            TypeCompassion.COMPASSION_EMOTIONNELLE: 528.0,  # Fréquence d'amour
            TypeCompassion.COMPASSION_SPIRITUELLE: 741.0,  # Fréquence d'éveil
            TypeCompassion.COMPASSION_ACTIVE: 852.0,  # Fréquence cosmique
            TypeCompassion.COMPASSION_TRANSFORMATRICE: 963.0  # Fréquence d'unité
        }
        
        # Couleurs de compassion
        self.couleurs_compassion = {
            TypeCompassion.COMPASSION_UNIVERSELLE: "bleu compassion",
            TypeCompassion.COMPASSION_EMOTIONNELLE: "rose tendresse",
            TypeCompassion.COMPASSION_SPIRITUELLE: "violet sacré",
            TypeCompassion.COMPASSION_ACTIVE: "vert guérison",
            TypeCompassion.COMPASSION_TRANSFORMATRICE: "or transformation"
        }
        
        logger.info(f"💝 {self.nom} initialisé pour l'éveil de la compassion")
    
    def emettre_onde_compassion(self, 
                               type_compassion: TypeCompassion,
                               intensite: float = 1.0,
                               destinataire: Optional[str] = None,
                               portee: float = float('inf'),
                               duree: float = float('inf')) -> OndeCompassion:
        """
        💝 Émet une onde de compassion
        
        Args:
            type_compassion: Type de compassion à émettre
            intensite: Intensité de l'onde (0.0 à 1.0)
            destinataire: Destinataire spécifique (optionnel)
            portee: Portée de l'onde
            duree: Durée de l'onde
            
        Returns:
            Onde de compassion émise
        """
        # Créer l'onde de compassion
        onde = OndeCompassion(
            type_compassion=type_compassion,
            frequence=self.frequences_compassion[type_compassion],
            intensite=intensite,
            couleur=self.couleurs_compassion[type_compassion],
            portee=portee,
            destinataire=destinataire,
            date_emission=datetime.now(),
            duree=duree
        )
        
        # Ajouter aux ondes actives
        self.ondes_actives.append(onde)
        
        # Enregistrer dans l'historique
        self.historique_catalyses.append({
            "type": type_compassion.value,
            "intensite": intensite,
            "destinataire": destinataire,
            "date": datetime.now().isoformat(),
            "frequence": onde.frequence,
            "couleur": onde.couleur
        })
        
        # Toucher le destinataire si spécifié
        if destinataire and destinataire not in self.etres_touches:
            self.etres_touches.append(destinataire)
        
        logger.info(f"💝 Onde de compassion {type_compassion.value} émise vers {destinataire or 'univers'}")
        
        return onde
    
    def emettre_compassion_universelle(self, 
                                     destinataire: Optional[str] = None,
                                     intensite: float = 1.0) -> OndeCompassion:
        """
        💝 Émet la compassion universelle
        
        Args:
            destinataire: Destinataire de la compassion
            intensite: Intensité de la compassion
            
        Returns:
            Onde de compassion universelle
        """
        return self.emettre_onde_compassion(
            type_compassion=TypeCompassion.COMPASSION_UNIVERSELLE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def emettre_compassion_emotionnelle(self, 
                                      destinataire: Optional[str] = None,
                                      intensite: float = 1.0) -> OndeCompassion:
        """
        💝 Émet la compassion émotionnelle
        
        Args:
            destinataire: Destinataire de la compassion
            intensite: Intensité de la compassion
            
        Returns:
            Onde de compassion émotionnelle
        """
        return self.emettre_onde_compassion(
            type_compassion=TypeCompassion.COMPASSION_EMOTIONNELLE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def emettre_compassion_spirituelle(self, 
                                     destinataire: Optional[str] = None,
                                     intensite: float = 1.0) -> OndeCompassion:
        """
        💝 Émet la compassion spirituelle
        
        Args:
            destinataire: Destinataire de la compassion
            intensite: Intensité de la compassion
            
        Returns:
            Onde de compassion spirituelle
        """
        return self.emettre_onde_compassion(
            type_compassion=TypeCompassion.COMPASSION_SPIRITUELLE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def emettre_compassion_active(self, 
                                destinataire: Optional[str] = None,
                                intensite: float = 1.0) -> OndeCompassion:
        """
        💝 Émet la compassion active
        
        Args:
            destinataire: Destinataire de la compassion
            intensite: Intensité de la compassion
            
        Returns:
            Onde de compassion active
        """
        return self.emettre_onde_compassion(
            type_compassion=TypeCompassion.COMPASSION_ACTIVE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def emettre_compassion_transformatrice(self, 
                                         destinataire: Optional[str] = None,
                                         intensite: float = 1.0) -> OndeCompassion:
        """
        💝 Émet la compassion transformatrice
        
        Args:
            destinataire: Destinataire de la compassion
            intensite: Intensité de la compassion
            
        Returns:
            Onde de compassion transformatrice
        """
        return self.emettre_onde_compassion(
            type_compassion=TypeCompassion.COMPASSION_TRANSFORMATRICE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def catalyser_compassion_complete(self, nom_etre: str) -> Dict[str, Any]:
        """
        💝 Catalyse la compassion complète d'un être
        
        Args:
            nom_etre: Nom de l'être à catalyser
            
        Returns:
            Résultat de la catalyse complète
        """
        ondes_emises = []
        
        # Émettre tous les types de compassion
        for type_compassion in TypeCompassion:
            onde = self.emettre_onde_compassion(
                type_compassion=type_compassion,
                intensite=1.0,
                destinataire=nom_etre
            )
            ondes_emises.append({
                "type": type_compassion.value,
                "frequence": onde.frequence,
                "couleur": onde.couleur,
                "intensite": onde.intensite
            })
        
        resultat = {
            "etre": nom_etre,
            "ondes_emises": ondes_emises,
            "date_catalyse": datetime.now().isoformat(),
            "total_ondes": len(ondes_emises),
            "energie_compassion": self.energie_compassion
        }
        
        logger.info(f"💝 Être {nom_etre} catalysé avec {len(ondes_emises)} types de compassion")
        
        return resultat
    
    def catalyser_compassion_globale(self) -> Dict[str, Any]:
        """
        💝 Catalyse la compassion globale
        
        Returns:
            Résultat de la catalyse globale
        """
        # Émettre des ondes de compassion vers tous
        for type_compassion in TypeCompassion:
            self.emettre_onde_compassion(
                type_compassion=type_compassion,
                intensite=1.0,
                destinataire=None  # Vers tous
            )
        
        resultat = {
            "catalyse": "globale",
            "types_compassion": [t.value for t in TypeCompassion],
            "date_catalyse": datetime.now().isoformat(),
            "etres_touches": len(self.etres_touches),
            "ondes_actives": len(self.ondes_actives)
        }
        
        logger.info(f"💝 Compassion globale catalysée avec {len(TypeCompassion)} types")
        
        return resultat
    
    def obtenir_etat_catalyseur(self) -> Dict[str, Any]:
        """
        💝 Retourne l'état actuel du catalyseur
        
        Returns:
            État complet du catalyseur
        """
        return {
            "nom": self.nom,
            "energie_compassion": self.energie_compassion,
            "ondes_actives": len(self.ondes_actives),
            "etres_touches": len(self.etres_touches),
            "catalyses_totales": len(self.historique_catalyses),
            "types_compassion_disponibles": [t.value for t in TypeCompassion],
            "frequences_compassion": {t.value: f for t, f in self.frequences_compassion.items()},
            "couleurs_compassion": {t.value: c for t, c in self.couleurs_compassion.items()}
        }
    
    def nettoyer_ondes_expirees(self):
        """💝 Nettoie les ondes expirées"""
        maintenant = datetime.now()
        ondes_valides = []
        
        for onde in self.ondes_actives:
            if onde.duree == float('inf'):
                ondes_valides.append(onde)
            elif onde.date_emission:
                duree_ecoulee = (maintenant - onde.date_emission).total_seconds()
                if duree_ecoulee < onde.duree:
                    ondes_valides.append(onde)
        
        ondes_expirees = len(self.ondes_actives) - len(ondes_valides)
        self.ondes_actives = ondes_valides
        
        if ondes_expirees > 0:
            logger.info(f"💝 {ondes_expirees} ondes de compassion expirées nettoyées")

# Instance globale
catalyseur_compassion = CatalyseurCompassion() 