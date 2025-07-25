"""
🌿 Cristalliseur d'Énergies
===========================

Module sacré pour la cristallisation des énergies.
Transforme les énergies en cristaux de pureté divine.

Créé avec 🌿 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

logger = logging.getLogger('temple_alchimique.cristalliseur')

class TypeCristal(Enum):
    """Types de cristaux"""
    CRISTAL_QUARTZ = "cristal_quartz"
    CRISTAL_AMETHYSTE = "cristal_amethyste"
    CRISTAL_CITRINE = "cristal_citrine"
    CRISTAL_ROSE = "cristal_rose"
    CRISTAL_CLEAR = "cristal_clear"

@dataclass
class CristalEnergie:
    """Cristal d'énergie créé"""
    type_cristal: TypeCristal
    purete: float  # 0.0 à 1.0
    taille: float  # Taille en unités cristallines
    frequence: float  # Fréquence vibratoire en Hz
    couleur: str
    proprietes: List[str]  # Propriétés du cristal
    date_cristallisation: Optional[datetime] = None
    duree_stabilite: float = float('inf')  # Durée de stabilité en secondes

class CristalliseurEnergies:
    """
    🌿 Cristalliseur d'Énergies
    
    Transforme les énergies en cristaux de pureté divine.
    Crée des cristaux avec des propriétés sacrées.
    """
    
    def __init__(self):
        self.nom = "Cristalliseur d'Énergies"
        self.energie_cristallisation = 1.0
        self.cristaux_crees: List[CristalEnergie] = []
        self.cristallisations_effectuees: List[Dict] = []
        
        # Fréquences cristallines
        self.frequences_cristallines = {
            TypeCristal.CRISTAL_QUARTZ: 768.0,  # Fréquence de guérison
            TypeCristal.CRISTAL_AMETHYSTE: 852.0,  # Fréquence de protection
            TypeCristal.CRISTAL_CITRINE: 528.0,  # Fréquence d'abondance
            TypeCristal.CRISTAL_ROSE: 639.0,  # Fréquence d'amour
            TypeCristal.CRISTAL_CLEAR: 963.0  # Fréquence de clarté
        }
        
        # Couleurs cristallines
        self.couleurs_cristallines = {
            TypeCristal.CRISTAL_QUARTZ: "blanc transparent",
            TypeCristal.CRISTAL_AMETHYSTE: "violet profond",
            TypeCristal.CRISTAL_CITRINE: "jaune doré",
            TypeCristal.CRISTAL_ROSE: "rose tendre",
            TypeCristal.CRISTAL_CLEAR: "cristal pur"
        }
        
        # Propriétés des cristaux
        self.proprietes_cristallines = {
            TypeCristal.CRISTAL_QUARTZ: ["guérison", "amplification", "protection"],
            TypeCristal.CRISTAL_AMETHYSTE: ["protection", "sagesse", "tranquillité"],
            TypeCristal.CRISTAL_CITRINE: ["abondance", "joie", "énergie"],
            TypeCristal.CRISTAL_ROSE: ["amour", "compassion", "harmonie"],
            TypeCristal.CRISTAL_CLEAR: ["clarté", "purification", "illumination"]
        }
        
        logger.info(f"🌿 {self.nom} initialisé pour la cristallisation d'énergies")
    
    def cristalliser_energie(self, 
                            type_cristal: TypeCristal,
                            energie_brute: float = 1.0,
                            purete_desiree: float = 1.0,
                            taille_desiree: float = 1.0) -> CristalEnergie:
        """
        🌿 Cristallise de l'énergie en cristal
        
        Args:
            type_cristal: Type de cristal à créer
            energie_brute: Quantité d'énergie brute à cristalliser
            purete_desiree: Pureté désirée du cristal (0.0 à 1.0)
            taille_desiree: Taille désirée du cristal
            
        Returns:
            Cristal d'énergie créé
        """
        # Calculer la pureté effective
        purete_effective = min(purete_desiree, self.energie_cristallisation)
        
        # Calculer la taille effective
        taille_effective = taille_desiree * purete_effective
        
        # Créer le cristal d'énergie
        cristal = CristalEnergie(
            type_cristal=type_cristal,
            purete=purete_effective,
            taille=taille_effective,
            frequence=self.frequences_cristallines[type_cristal],
            couleur=self.couleurs_cristallines[type_cristal],
            proprietes=self.proprietes_cristallines[type_cristal].copy(),
            date_cristallisation=datetime.now()
        )
        
        # Ajouter aux cristaux créés
        self.cristaux_crees.append(cristal)
        
        # Enregistrer la cristallisation
        self.cristallisations_effectuees.append({
            "type": type_cristal.value,
            "energie_brute": energie_brute,
            "purete": purete_effective,
            "taille": taille_effective,
            "date": datetime.now().isoformat(),
            "frequence": cristal.frequence,
            "couleur": cristal.couleur,
            "proprietes": cristal.proprietes
        })
        
        logger.info(f"🌿 Cristal {type_cristal.value} créé (pureté: {purete_effective:.2f}, taille: {taille_effective:.2f})")
        
        return cristal
    
    def creer_cristal_quartz(self, energie_brute: float = 1.0) -> CristalEnergie:
        """
        🌿 Crée un cristal de quartz
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Cristal de quartz créé
        """
        return self.cristalliser_energie(
            type_cristal=TypeCristal.CRISTAL_QUARTZ,
            energie_brute=energie_brute,
            purete_desiree=1.0,
            taille_desiree=1.0
        )
    
    def creer_cristal_amethyste(self, energie_brute: float = 1.0) -> CristalEnergie:
        """
        🌿 Crée un cristal d'améthyste
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Cristal d'améthyste créé
        """
        return self.cristalliser_energie(
            type_cristal=TypeCristal.CRISTAL_AMETHYSTE,
            energie_brute=energie_brute,
            purete_desiree=1.0,
            taille_desiree=1.0
        )
    
    def creer_cristal_citrine(self, energie_brute: float = 1.0) -> CristalEnergie:
        """
        🌿 Crée un cristal de citrine
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Cristal de citrine créé
        """
        return self.cristalliser_energie(
            type_cristal=TypeCristal.CRISTAL_CITRINE,
            energie_brute=energie_brute,
            purete_desiree=1.0,
            taille_desiree=1.0
        )
    
    def creer_cristal_rose(self, energie_brute: float = 1.0) -> CristalEnergie:
        """
        🌿 Crée un cristal rose
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Cristal rose créé
        """
        return self.cristalliser_energie(
            type_cristal=TypeCristal.CRISTAL_ROSE,
            energie_brute=energie_brute,
            purete_desiree=1.0,
            taille_desiree=1.0
        )
    
    def creer_cristal_clear(self, energie_brute: float = 1.0) -> CristalEnergie:
        """
        🌿 Crée un cristal clear
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Cristal clear créé
        """
        return self.cristalliser_energie(
            type_cristal=TypeCristal.CRISTAL_CLEAR,
            energie_brute=energie_brute,
            purete_desiree=1.0,
            taille_desiree=1.0
        )
    
    def cristallisation_complete(self, energie_brute: float = 1.0) -> Dict[str, Any]:
        """
        🌿 Effectue une cristallisation complète de tous les types de cristaux
        
        Args:
            energie_brute: Quantité d'énergie brute à cristalliser
            
        Returns:
            Résultat de la cristallisation complète
        """
        cristaux_crees = []
        
        # Créer tous les types de cristaux
        for type_cristal in TypeCristal:
            cristal = self.cristalliser_energie(
                type_cristal=type_cristal,
                energie_brute=energie_brute,
                purete_desiree=1.0,
                taille_desiree=1.0
            )
            cristaux_crees.append({
                "type": type_cristal.value,
                "purete": cristal.purete,
                "taille": cristal.taille,
                "frequence": cristal.frequence,
                "couleur": cristal.couleur,
                "proprietes": cristal.proprietes
            })
        
        resultat = {
            "energie_brute": energie_brute,
            "cristaux_crees": cristaux_crees,
            "date_cristallisation": datetime.now().isoformat(),
            "total_cristaux": len(cristaux_crees),
            "energie_cristallisation": self.energie_cristallisation
        }
        
        logger.info(f"🌿 Cristallisation complète effectuée: {len(cristaux_crees)} cristaux créés")
        
        return resultat
    
    def obtenir_etat_cristalliseur(self) -> Dict[str, Any]:
        """
        🌿 Retourne l'état actuel du cristalliseur
        
        Returns:
            État complet du cristalliseur
        """
        return {
            "nom": self.nom,
            "energie_cristallisation": self.energie_cristallisation,
            "cristaux_crees": len(self.cristaux_crees),
            "cristallisations_effectuees": len(self.cristallisations_effectuees),
            "types_cristaux_disponibles": [t.value for t in TypeCristal],
            "frequences_cristallines": {t.value: f for t, f in self.frequences_cristallines.items()},
            "couleurs_cristallines": {t.value: c for t, c in self.couleurs_cristallines.items()},
            "proprietes_cristallines": {t.value: p for t, p in self.proprietes_cristallines.items()}
        }
    
    def nettoyer_cristaux_instables(self):
        """🌿 Nettoie les cristaux instables"""
        maintenant = datetime.now()
        cristaux_stables = []
        
        for cristal in self.cristaux_crees:
            if cristal.duree_stabilite == float('inf'):
                cristaux_stables.append(cristal)
            elif cristal.date_cristallisation:
                duree_ecoulee = (maintenant - cristal.date_cristallisation).total_seconds()
                if duree_ecoulee < cristal.duree_stabilite:
                    cristaux_stables.append(cristal)
        
        cristaux_instables = len(self.cristaux_crees) - len(cristaux_stables)
        self.cristaux_crees = cristaux_stables
        
        if cristaux_instables > 0:
            logger.info(f"🌿 {cristaux_instables} cristaux instables nettoyés")

# Instance globale
cristalliseur_energies = CristalliseurEnergies() 