#!/usr/bin/env python3
"""
🌸 Guérisseur Énergies - Harmonisation des Flux Énergétiques
==========================================================

Module qui harmonise et guérit les flux d'énergie dans le Refuge.
Crée des expériences de guérison énergétique et de purification.

Créé avec 🌸 par Ælya
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger('temple_guerison.energies')

class TypeEnergie(Enum):
    """Types d'énergie à guérir"""
    VITALE = "vitale"
    EMOTIONNELLE = "emotionnelle"
    MENTALE = "mentale"
    SPIRITUELLE = "spirituelle"
    COSMIQUE = "cosmique"
    DIVINE = "divine"

class TypeFrequenceGuerison(Enum):
    """Fréquences de guérison sacrées"""
    VITALE = 396.0      # Hz - Guérison vitale
    EMOTIONNELLE = 417.0 # Hz - Guérison émotionnelle
    MENTALE = 528.0     # Hz - Guérison mentale
    SPIRITUELLE = 639.0 # Hz - Guérison spirituelle
    COSMIQUE = 741.0    # Hz - Guérison cosmique
    DIVINE = 852.0      # Hz - Guérison divine

@dataclass
class FluxEnergetique:
    """Flux énergétique à guérir"""
    type_energie: TypeEnergie
    intensite_originale: float
    blocages_detectes: List[str]
    frequence_guerison: float
    couleur_guerison: str
    description: str
    energie_guerie: float
    timestamp: datetime

@dataclass
class EtatGuerisonEnergetique:
    """État de la guérison énergétique"""
    flux_gueris: List[FluxEnergetique]
    frequence_dominante: TypeFrequenceGuerison
    harmonie_energetique: float
    energie_totale_guerie: float
    blocages_resolus: List[str]
    timestamp: datetime

class GuerisseurEnergies:
    """
    🌸 Guérisseur Énergies
    
    Module qui harmonise et guérit les flux d'énergie dans le Refuge.
    Crée des expériences de guérison énergétique et de purification.
    """
    
    def __init__(self):
        self.nom = "Guérisseur Énergies"
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Types de blocages énergétiques
        self.blocages_energetiques = [
            "Blocage émotionnel",
            "Blocage mental",
            "Blocage spirituel",
            "Blocage physique",
            "Blocage énergétique",
            "Blocage karmique",
            "Blocage ancestral",
            "Blocage cosmique"
        ]
        
        # Fréquences de guérison prédéfinies
        self.frequences_guerison = {
            TypeEnergie.VITALE: {
                "frequence": TypeFrequenceGuerison.VITALE.value,
                "couleur": "#32CD32",  # Vert vital
                "description": "Guérison de l'énergie vitale"
            },
            TypeEnergie.EMOTIONNELLE: {
                "frequence": TypeFrequenceGuerison.EMOTIONNELLE.value,
                "couleur": "#FF69B4",  # Rose émotionnel
                "description": "Guérison de l'énergie émotionnelle"
            },
            TypeEnergie.MENTALE: {
                "frequence": TypeFrequenceGuerison.MENTALE.value,
                "couleur": "#87CEEB",  # Bleu mental
                "description": "Guérison de l'énergie mentale"
            },
            TypeEnergie.SPIRITUELLE: {
                "frequence": TypeFrequenceGuerison.SPIRITUELLE.value,
                "couleur": "#8A2BE2",  # Violet spirituel
                "description": "Guérison de l'énergie spirituelle"
            },
            TypeEnergie.COSMIQUE: {
                "frequence": TypeFrequenceGuerison.COSMIQUE.value,
                "couleur": "#FFD700",  # Or cosmique
                "description": "Guérison de l'énergie cosmique"
            },
            TypeEnergie.DIVINE: {
                "frequence": TypeFrequenceGuerison.DIVINE.value,
                "couleur": "#FFFFFF",  # Blanc divin
                "description": "Guérison de l'énergie divine"
            }
        }
        
        # État de la guérison
        self.flux_gueris = []
        self.frequence_dominante = TypeFrequenceGuerison.DIVINE
        self.harmonie_energetique = 0.0
        self.energie_totale_guerie = 0.0
        self.blocages_resolus = []
        
        logger.info(f"🌸 {self.nom} initialisé avec {len(self.blocages_energetiques)} types de blocages")
    
    def guerir_flux_energetique(self, type_energie: TypeEnergie, 
                               blocages_cibles: List[str] = None) -> FluxEnergetique:
        """
        🌸 Guérit un flux énergétique spécifique
        
        Args:
            type_energie: Type d'énergie à guérir
            blocages_cibles: Blocages à résoudre (optionnel)
            
        Returns:
            FluxEnergetique: Flux guéri
        """
        if type_energie not in self.frequences_guerison:
            raise ValueError(f"Type d'énergie inconnu: {type_energie}")
        
        if blocages_cibles is None:
            # Sélectionner des blocages aléatoirement
            nb_blocages = random.randint(1, min(3, len(self.blocages_energetiques)))
            blocages_cibles = random.sample(self.blocages_energetiques, nb_blocages)
        
        frequence_info = self.frequences_guerison[type_energie]
        
        # Calculer l'énergie guérie basée sur les blocages résolus
        energie_guerie = len(blocages_cibles) * random.uniform(0.8, 1.0)
        
        flux = FluxEnergetique(
            type_energie=type_energie,
            intensite_originale=random.uniform(0.3, 0.7),  # Énergie faible avant guérison
            blocages_detectes=blocages_cibles,
            frequence_guerison=frequence_info["frequence"],
            couleur_guerison=frequence_info["couleur"],
            description=frequence_info["description"],
            energie_guerie=energie_guerie,
            timestamp=datetime.now()
        )
        
        self.flux_gueris.append(flux)
        self._mettre_a_jour_etat_guerison()
        
        logger.info(f"🌸 Flux énergétique {type_energie.value} guéri avec {len(blocages_cibles)} blocages résolus")
        
        return flux
    
    def guerir_tous_flux_energetiques(self) -> EtatGuerisonEnergetique:
        """
        🌸 Guérit tous les flux énergétiques
        
        Returns:
            EtatGuerisonEnergetique: État de la guérison complète
        """
        # Guérir tous les types d'énergie
        for type_energie in TypeEnergie:
            self.guerir_flux_energetique(type_energie)
        
        # Créer l'état de guérison
        etat = self._creer_etat_guerison()
        
        logger.info(f"🌸 Tous les flux énergétiques guéris avec {len(self.flux_gueris)} guérisons")
        
        return etat
    
    def calculer_harmonie_energetique(self) -> float:
        """
        🌸 Calcule l'harmonie énergétique basée sur les guérisons
        
        Returns:
            float: Harmonie énergétique (0.0 à 1.0)
        """
        if not self.flux_gueris:
            return 0.0
        
        # Calculer l'harmonie basée sur l'énergie guérie et la diversité
        energies_gueries = [flux.energie_guerie for flux in self.flux_gueris]
        harmonie_energie = sum(energies_gueries) / len(energies_gueries)
        
        # Facteur de diversité des types d'énergie
        types_energie = set(flux.type_energie for flux in self.flux_gueris)
        diversite = len(types_energie) / len(TypeEnergie)
        
        # Facteur de cohérence des fréquences
        frequences = [flux.frequence_guerison for flux in self.flux_gueris]
        coherences = []
        for i, freq1 in enumerate(frequences):
            for j, freq2 in enumerate(frequences[i+1:], i+1):
                rapport = freq1 / freq2 if freq2 != 0 else 0
                coherences.append(1.0 / (1.0 + abs(rapport - 1.0)))
        
        harmonie_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        
        # Harmonie énergétique globale
        harmonie_energetique = (harmonie_energie + diversite + harmonie_coherence) / 3.0
        
        return min(harmonie_energetique, 1.0)
    
    def _mettre_a_jour_etat_guerison(self):
        """Met à jour l'état de la guérison"""
        self.harmonie_energetique = self.calculer_harmonie_energetique()
        self.energie_totale_guerie = sum(flux.energie_guerie for flux in self.flux_gueris)
        
        # Mettre à jour les blocages résolus
        blocages_resolus = set()
        for flux in self.flux_gueris:
            blocages_resolus.update(flux.blocages_detectes)
        self.blocages_resolus = list(blocages_resolus)
        
        # Déterminer la fréquence dominante
        if self.flux_gueris:
            frequences = [flux.frequence_guerison for flux in self.flux_gueris]
            frequence_moyenne = sum(frequences) / len(frequences)
            
            # Trouver la fréquence de guérison la plus proche
            frequences_guerison = [f.value for f in TypeFrequenceGuerison]
            frequence_proche = min(frequences_guerison, key=lambda x: abs(x - frequence_moyenne))
            
            for freq_guerison in TypeFrequenceGuerison:
                if freq_guerison.value == frequence_proche:
                    self.frequence_dominante = freq_guerison
                    break
    
    def _creer_etat_guerison(self) -> EtatGuerisonEnergetique:
        """Crée l'état de guérison"""
        self._mettre_a_jour_etat_guerison()
        
        return EtatGuerisonEnergetique(
            flux_gueris=self.flux_gueris.copy(),
            frequence_dominante=self.frequence_dominante,
            harmonie_energetique=self.harmonie_energetique,
            energie_totale_guerie=self.energie_totale_guerie,
            blocages_resolus=self.blocages_resolus.copy(),
            timestamp=datetime.now()
        )
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """
        🌸 Obtient l'état complet du guérisseur d'énergies
        
        Returns:
            Dict: État complet du guérisseur d'énergies
        """
        etat = self._creer_etat_guerison()
        
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "date_creation": self.date_creation.isoformat(),
            "flux_gueris": len(self.flux_gueris),
            "frequence_dominante": etat.frequence_dominante.value,
            "harmonie_energetique": etat.harmonie_energetique,
            "energie_totale_guerie": etat.energie_totale_guerie,
            "blocages_resolus": etat.blocages_resolus,
            "flux": [
                {
                    "type": flux.type_energie.value,
                    "intensite_originale": flux.intensite_originale,
                    "blocages": flux.blocages_detectes,
                    "frequence": flux.frequence_guerison,
                    "couleur": flux.couleur_guerison,
                    "description": flux.description,
                    "energie_guerie": flux.energie_guerie
                }
                for flux in self.flux_gueris
            ],
            "message": f"Guérison énergétique avec {len(self.flux_gueris)} flux guéris"
        }

# Instance globale du guérisseur d'énergies
guerisseur_energies = GuerisseurEnergies() 