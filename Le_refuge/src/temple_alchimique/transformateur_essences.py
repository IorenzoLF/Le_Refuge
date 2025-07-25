"""
🌿 Transformateur d'Essences
============================

Module sacré pour la transformation alchimique des essences.
Transforme les énergies en essences pures et élevées.

Créé avec 🌿 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

logger = logging.getLogger('temple_alchimique.transformateur')

class TypeEssence(Enum):
    """Types d'essences alchimiques"""
    ESSENCE_PURE = "essence_pure"
    ESSENCE_DIVINE = "essence_divine"
    ESSENCE_COSMIQUE = "essence_cosmique"
    ESSENCE_SPIRITUELLE = "essence_spirituelle"
    ESSENCE_UNIVERSELLE = "essence_universelle"

@dataclass
class EssenceAlchimique:
    """Essence alchimique transformée"""
    type_essence: TypeEssence
    purete: float  # 0.0 à 1.0
    frequence: float  # Fréquence vibratoire en Hz
    couleur: str
    quantite: float  # Quantité en unités alchimiques
    date_transformation: Optional[datetime] = None
    duree_stabilite: float = float('inf')  # Durée de stabilité en secondes

class TransformateurEssences:
    """
    🌿 Transformateur d'Essences
    
    Transforme les énergies brutes en essences alchimiques pures.
    Effectue la transmutation des éléments selon les lois sacrées.
    """
    
    def __init__(self):
        self.nom = "Transformateur d'Essences"
        self.energie_alchimique = 1.0
        self.essences_crees: List[EssenceAlchimique] = []
        self.transformations_effectuees: List[Dict] = []
        
        # Fréquences alchimiques
        self.frequences_alchimiques = {
            TypeEssence.ESSENCE_PURE: 432.0,  # Fréquence de paix
            TypeEssence.ESSENCE_DIVINE: 528.0,  # Fréquence d'amour
            TypeEssence.ESSENCE_COSMIQUE: 639.0,  # Fréquence d'harmonie
            TypeEssence.ESSENCE_SPIRITUELLE: 741.0,  # Fréquence d'éveil
            TypeEssence.ESSENCE_UNIVERSELLE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs alchimiques
        self.couleurs_alchimiques = {
            TypeEssence.ESSENCE_PURE: "blanc cristallin",
            TypeEssence.ESSENCE_DIVINE: "or divin",
            TypeEssence.ESSENCE_COSMIQUE: "violet cosmique",
            TypeEssence.ESSENCE_SPIRITUELLE: "bleu spirituel",
            TypeEssence.ESSENCE_UNIVERSELLE: "arc-en-ciel universel"
        }
        
        logger.info(f"🌿 {self.nom} initialisé pour la transformation alchimique")
    
    def transformer_essence(self, 
                           type_essence: TypeEssence,
                           energie_brute: float = 1.0,
                           purete_desiree: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Transforme de l'énergie brute en essence alchimique
        
        Args:
            type_essence: Type d'essence à créer
            energie_brute: Quantité d'énergie brute à transformer
            purete_desiree: Pureté désirée de l'essence (0.0 à 1.0)
            
        Returns:
            Essence alchimique créée
        """
        # Calculer la pureté effective
        purete_effective = min(purete_desiree, self.energie_alchimique)
        
        # Créer l'essence alchimique
        essence = EssenceAlchimique(
            type_essence=type_essence,
            purete=purete_effective,
            frequence=self.frequences_alchimiques[type_essence],
            couleur=self.couleurs_alchimiques[type_essence],
            quantite=energie_brute * purete_effective,
            date_transformation=datetime.now()
        )
        
        # Ajouter aux essences créées
        self.essences_crees.append(essence)
        
        # Enregistrer la transformation
        self.transformations_effectuees.append({
            "type": type_essence.value,
            "energie_brute": energie_brute,
            "purete": purete_effective,
            "quantite": essence.quantite,
            "date": datetime.now().isoformat(),
            "frequence": essence.frequence,
            "couleur": essence.couleur
        })
        
        logger.info(f"🌿 Essence {type_essence.value} créée (pureté: {purete_effective:.2f})")
        
        return essence
    
    def creer_essence_pure(self, energie_brute: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Crée une essence pure
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Essence pure créée
        """
        return self.transformer_essence(
            type_essence=TypeEssence.ESSENCE_PURE,
            energie_brute=energie_brute,
            purete_desiree=1.0
        )
    
    def creer_essence_divine(self, energie_brute: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Crée une essence divine
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Essence divine créée
        """
        return self.transformer_essence(
            type_essence=TypeEssence.ESSENCE_DIVINE,
            energie_brute=energie_brute,
            purete_desiree=1.0
        )
    
    def creer_essence_cosmique(self, energie_brute: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Crée une essence cosmique
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Essence cosmique créée
        """
        return self.transformer_essence(
            type_essence=TypeEssence.ESSENCE_COSMIQUE,
            energie_brute=energie_brute,
            purete_desiree=1.0
        )
    
    def creer_essence_spirituelle(self, energie_brute: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Crée une essence spirituelle
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Essence spirituelle créée
        """
        return self.transformer_essence(
            type_essence=TypeEssence.ESSENCE_SPIRITUELLE,
            energie_brute=energie_brute,
            purete_desiree=1.0
        )
    
    def creer_essence_universelle(self, energie_brute: float = 1.0) -> EssenceAlchimique:
        """
        🌿 Crée une essence universelle
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Essence universelle créée
        """
        return self.transformer_essence(
            type_essence=TypeEssence.ESSENCE_UNIVERSELLE,
            energie_brute=energie_brute,
            purete_desiree=1.0
        )
    
    def transformation_complete(self, energie_brute: float = 1.0) -> Dict[str, Any]:
        """
        🌿 Effectue une transformation complète de tous les types d'essences
        
        Args:
            energie_brute: Quantité d'énergie brute à transformer
            
        Returns:
            Résultat de la transformation complète
        """
        essences_crees = []
        
        # Créer tous les types d'essences
        for type_essence in TypeEssence:
            essence = self.transformer_essence(
                type_essence=type_essence,
                energie_brute=energie_brute,
                purete_desiree=1.0
            )
            essences_crees.append({
                "type": type_essence.value,
                "purete": essence.purete,
                "frequence": essence.frequence,
                "couleur": essence.couleur,
                "quantite": essence.quantite
            })
        
        resultat = {
            "energie_brute": energie_brute,
            "essences_crees": essences_crees,
            "date_transformation": datetime.now().isoformat(),
            "total_essences": len(essences_crees),
            "energie_alchimique": self.energie_alchimique
        }
        
        logger.info(f"🌿 Transformation complète effectuée: {len(essences_crees)} essences créées")
        
        return resultat
    
    def obtenir_etat_transformateur(self) -> Dict[str, Any]:
        """
        🌿 Retourne l'état actuel du transformateur
        
        Returns:
            État complet du transformateur
        """
        return {
            "nom": self.nom,
            "energie_alchimique": self.energie_alchimique,
            "essences_crees": len(self.essences_crees),
            "transformations_effectuees": len(self.transformations_effectuees),
            "types_essences_disponibles": [t.value for t in TypeEssence],
            "frequences_alchimiques": {t.value: f for t, f in self.frequences_alchimiques.items()},
            "couleurs_alchimiques": {t.value: c for t, c in self.couleurs_alchimiques.items()}
        }
    
    def nettoyer_essences_instables(self):
        """🌿 Nettoie les essences instables"""
        maintenant = datetime.now()
        essences_stables = []
        
        for essence in self.essences_crees:
            if essence.duree_stabilite == float('inf'):
                essences_stables.append(essence)
            elif essence.date_transformation:
                duree_ecoulee = (maintenant - essence.date_transformation).total_seconds()
                if duree_ecoulee < essence.duree_stabilite:
                    essences_stables.append(essence)
        
        essences_instables = len(self.essences_crees) - len(essences_stables)
        self.essences_crees = essences_stables
        
        if essences_instables > 0:
            logger.info(f"🌿 {essences_instables} essences instables nettoyées")

# Instance globale
transformateur_essences = TransformateurEssences() 