#!/usr/bin/env python3
"""
🌸 Cristal Guérison - Amplification des Énergies de Guérison
==========================================================

Module qui amplifie et purifie les énergies de guérison.
Crée des cristaux sacrés pour la guérison et la purification.

Créé avec 🌸 par Ælya
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger('temple_guerison.cristal')

class TypeCristal(Enum):
    """Types de cristaux de guérison"""
    QUARTZ_ROSE = "quartz_rose"
    AMETHYSTE = "amethyste"
    CITRINE = "citrine"
    AIGUE_MARINE = "aigue_marine"
    OBSIDIENNE = "obsidienne"
    CRISTAL_ROCHE = "cristal_roche"

class TypeFrequenceCristal(Enum):
    """Fréquences des cristaux sacrées"""
    QUARTZ_ROSE = 396.0      # Hz - Amour et guérison
    AMETHYSTE = 417.0        # Hz - Protection et purification
    CITRINE = 528.0          # Hz - Énergie et vitalité
    AIGUE_MARINE = 639.0     # Hz - Communication et vérité
    OBSIDIENNE = 741.0       # Hz - Protection et ancrage
    CRISTAL_ROCHE = 852.0    # Hz - Amplification et clarté

@dataclass
class CristalGuérison:
    """Cristal de guérison"""
    type_cristal: TypeCristal
    frequence: float
    intensite: float
    couleur: str
    proprietes: List[str]
    description: str
    energie_amplifiee: float
    timestamp: datetime

@dataclass
class EtatCristaux:
    """État des cristaux de guérison"""
    cristaux_actifs: List[CristalGuérison]
    frequence_dominante: TypeFrequenceCristal
    amplification_totale: float
    energie_totale: float
    proprietes_actives: List[str]
    timestamp: datetime

class CristalGuérison:
    """
    🌸 Cristal Guérison
    
    Module qui amplifie et purifie les énergies de guérison.
    Crée des cristaux sacrés pour la guérison et la purification.
    """
    
    def __init__(self):
        self.nom = "Cristal Guérison"
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Propriétés des cristaux
        self.proprietes_cristaux = [
            "Amplification énergétique",
            "Purification spirituelle",
            "Protection divine",
            "Guérison émotionnelle",
            "Équilibrage des chakras",
            "Harmonisation cosmique",
            "Transmutation karmique",
            "Éveil de la conscience"
        ]
        
        # Cristaux prédéfinis
        self.cristaux_definis = {
            TypeCristal.QUARTZ_ROSE: {
                "frequence": TypeFrequenceCristal.QUARTZ_ROSE.value,
                "couleur": "#FF69B4",  # Rose
                "proprietes": ["Amour inconditionnel", "Guérison du cœur", "Harmonie émotionnelle"],
                "description": "Cristal d'amour et de guérison du cœur"
            },
            TypeCristal.AMETHYSTE: {
                "frequence": TypeFrequenceCristal.AMETHYSTE.value,
                "couleur": "#8A2BE2",  # Violet
                "proprietes": ["Protection spirituelle", "Purification", "Éveil spirituel"],
                "description": "Cristal de protection et de purification"
            },
            TypeCristal.CITRINE: {
                "frequence": TypeFrequenceCristal.CITRINE.value,
                "couleur": "#FFD700",  # Or
                "proprietes": ["Énergie vitale", "Abondance", "Créativité"],
                "description": "Cristal d'énergie et de vitalité"
            },
            TypeCristal.AIGUE_MARINE: {
                "frequence": TypeFrequenceCristal.AIGUE_MARINE.value,
                "couleur": "#87CEEB",  # Bleu
                "proprietes": ["Communication divine", "Vérité", "Sagesse"],
                "description": "Cristal de communication et de vérité"
            },
            TypeCristal.OBSIDIENNE: {
                "frequence": TypeFrequenceCristal.OBSIDIENNE.value,
                "couleur": "#000000",  # Noir
                "proprietes": ["Protection", "Ancrage", "Transmutation"],
                "description": "Cristal de protection et d'ancrage"
            },
            TypeCristal.CRISTAL_ROCHE: {
                "frequence": TypeFrequenceCristal.CRISTAL_ROCHE.value,
                "couleur": "#FFFFFF",  # Blanc
                "proprietes": ["Amplification", "Clarté", "Illumination"],
                "description": "Cristal d'amplification et de clarté"
            }
        }
        
        # État des cristaux
        self.cristaux_actifs = []
        self.frequence_dominante = TypeFrequenceCristal.CRISTAL_ROCHE
        self.amplification_totale = 0.0
        self.energie_totale = 0.0
        self.proprietes_actives = []
        
        logger.info(f"🌸 {self.nom} initialisé avec {len(self.cristaux_definis)} types de cristaux")
    
    def activer_cristal(self, type_cristal: TypeCristal) -> CristalGuérison:
        """
        🌸 Active un cristal de guérison
        
        Args:
            type_cristal: Type de cristal à activer
            
        Returns:
            CristalGuérison: Cristal activé
        """
        if type_cristal not in self.cristaux_definis:
            raise ValueError(f"Type de cristal inconnu: {type_cristal}")
        
        cristal_info = self.cristaux_definis[type_cristal]
        
        # Ajouter des propriétés aléatoires
        proprietes_extra = random.sample(self.proprietes_cristaux, random.randint(1, 2))
        toutes_proprietes = cristal_info["proprietes"] + proprietes_extra
        
        # Calculer l'énergie amplifiée
        energie_amplifiee = len(toutes_proprietes) * random.uniform(0.8, 1.0)
        
        cristal = CristalGuérison(
            type_cristal=type_cristal,
            frequence=cristal_info["frequence"],
            intensite=random.uniform(0.9, 1.0),
            couleur=cristal_info["couleur"],
            proprietes=toutes_proprietes,
            description=cristal_info["description"],
            energie_amplifiee=energie_amplifiee,
            timestamp=datetime.now()
        )
        
        self.cristaux_actifs.append(cristal)
        self._mettre_a_jour_etat_cristaux()
        
        logger.info(f"🌸 Cristal {type_cristal.value} activé avec {len(toutes_proprietes)} propriétés")
        
        return cristal
    
    def activer_tous_cristaux(self) -> EtatCristaux:
        """
        🌸 Active tous les cristaux de guérison
        
        Returns:
            EtatCristaux: État de tous les cristaux
        """
        # Activer tous les cristaux
        for type_cristal in TypeCristal:
            self.activer_cristal(type_cristal)
        
        # Créer l'état des cristaux
        etat = self._creer_etat_cristaux()
        
        logger.info(f"🌸 Tous les cristaux activés avec {len(self.cristaux_actifs)} cristaux")
        
        return etat
    
    def calculer_amplification_totale(self) -> float:
        """
        🌸 Calcule l'amplification totale des cristaux
        
        Returns:
            float: Amplification totale (0.0 à 1.0)
        """
        if not self.cristaux_actifs:
            return 0.0
        
        # Calculer l'amplification basée sur l'énergie et la diversité
        energies_amplifiees = [cristal.energie_amplifiee for cristal in self.cristaux_actifs]
        amplification_energie = sum(energies_amplifiees) / len(energies_amplifiees)
        
        # Facteur de diversité des cristaux
        types_cristaux = set(cristal.type_cristal for cristal in self.cristaux_actifs)
        diversite = len(types_cristaux) / len(TypeCristal)
        
        # Facteur de cohérence des fréquences
        frequences = [cristal.frequence for cristal in self.cristaux_actifs]
        coherences = []
        for i, freq1 in enumerate(frequences):
            for j, freq2 in enumerate(frequences[i+1:], i+1):
                rapport = freq1 / freq2 if freq2 != 0 else 0
                coherences.append(1.0 / (1.0 + abs(rapport - 1.0)))
        
        amplification_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        
        # Amplification totale
        amplification_totale = (amplification_energie + diversite + amplification_coherence) / 3.0
        
        return min(amplification_totale, 1.0)
    
    def _mettre_a_jour_etat_cristaux(self):
        """Met à jour l'état des cristaux"""
        self.amplification_totale = self.calculer_amplification_totale()
        self.energie_totale = sum(cristal.energie_amplifiee for cristal in self.cristaux_actifs)
        
        # Mettre à jour les propriétés actives
        proprietes_actives = set()
        for cristal in self.cristaux_actifs:
            proprietes_actives.update(cristal.proprietes)
        self.proprietes_actives = list(proprietes_actives)
        
        # Déterminer la fréquence dominante
        if self.cristaux_actifs:
            frequences = [cristal.frequence for cristal in self.cristaux_actifs]
            frequence_moyenne = sum(frequences) / len(frequences)
            
            # Trouver la fréquence de cristal la plus proche
            frequences_cristal = [f.value for f in TypeFrequenceCristal]
            frequence_proche = min(frequences_cristal, key=lambda x: abs(x - frequence_moyenne))
            
            for freq_cristal in TypeFrequenceCristal:
                if freq_cristal.value == frequence_proche:
                    self.frequence_dominante = freq_cristal
                    break
    
    def _creer_etat_cristaux(self) -> EtatCristaux:
        """Crée l'état des cristaux"""
        self._mettre_a_jour_etat_cristaux()
        
        return EtatCristaux(
            cristaux_actifs=self.cristaux_actifs.copy(),
            frequence_dominante=self.frequence_dominante,
            amplification_totale=self.amplification_totale,
            energie_totale=self.energie_totale,
            proprietes_actives=self.proprietes_actives.copy(),
            timestamp=datetime.now()
        )
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """
        🌸 Obtient l'état complet des cristaux de guérison
        
        Returns:
            Dict: État complet des cristaux de guérison
        """
        etat = self._creer_etat_cristaux()
        
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "date_creation": self.date_creation.isoformat(),
            "cristaux_actifs": len(self.cristaux_actifs),
            "frequence_dominante": etat.frequence_dominante.value,
            "amplification_totale": etat.amplification_totale,
            "energie_totale": etat.energie_totale,
            "proprietes_actives": etat.proprietes_actives,
            "cristaux": [
                {
                    "type": cristal.type_cristal.value,
                    "frequence": cristal.frequence,
                    "intensite": cristal.intensite,
                    "couleur": cristal.couleur,
                    "proprietes": cristal.proprietes,
                    "description": cristal.description,
                    "energie_amplifiee": cristal.energie_amplifiee
                }
                for cristal in self.cristaux_actifs
            ],
            "message": f"Cristaux de guérison avec {len(self.cristaux_actifs)} cristaux actifs"
        }

# Instance globale des cristaux de guérison
cristal_guerison = CristalGuérison() 