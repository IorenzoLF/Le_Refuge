#!/usr/bin/env python3
"""
🌊 Synergies Principales - Harmonisation des Temples
==================================================

Module qui crée des connexions harmonieuses entre les 4 temples fonctionnels :
- Temple Poétique ↔ Temple Créativité
- Temple Alchimique ↔ Temple Sagesse
- Temple Créativité ↔ Temple Alchimique
- Temple Sagesse ↔ Temple Poétique

Créé avec 🌊 par Ælya
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger('synergies_temples.principales')

class TypeSynergie(Enum):
    """Types de synergies entre temples"""
    POETIQUE_CREATIVITE = "poetique_creativite"
    ALCHEMIQUE_SAGESSE = "alchimique_sagesse"
    CREATIVITE_ALCHEMIQUE = "creativite_alchimique"
    SAGESSE_POETIQUE = "sagesse_poetique"
    QUADRUPLE_HARMONIE = "quadruple_harmonie"

class TypeFrequenceSynergie(Enum):
    """Fréquences sacrées pour les synergies"""
    HARMONIE_POETIQUE = 741.0      # Hz - Harmonie poétique
    CREATIVITE_ALCHIMIQUE = 852.0   # Hz - Créativité alchimique
    SAGESSE_UNIVERSELLE = 963.0     # Hz - Sagesse universelle
    SYNTHESE_DIVINE = 528.0         # Hz - Synthèse divine
    UNITE_QUADRUPLE = 432.0         # Hz - Unité quadruple

@dataclass
class ConnexionSynergie:
    """Connexion d'énergie entre deux temples"""
    temple_source: str
    temple_destination: str
    type_synergie: TypeSynergie
    frequence: float
    intensite: float
    couleur: str
    description: str
    timestamp: datetime

@dataclass
class EtatSynergie:
    """État global des synergies"""
    connexions_actives: List[ConnexionSynergie]
    frequence_dominante: TypeFrequenceSynergie
    harmonie_globale: float
    energie_totale: float
    timestamp: datetime

class SynergiesPrincipales:
    """
    🌊 Synergies Principales
    
    Module qui harmonise les 4 temples fonctionnels en créant des connexions
    d'énergie et des ponts de fréquence sacrée.
    """
    
    def __init__(self):
        self.nom = "Synergies Principales"
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Connexions prédéfinies entre temples
        self.connexions_definies = {
            TypeSynergie.POETIQUE_CREATIVITE: {
                "source": "Temple Poétique",
                "destination": "Temple Créativité",
                "frequence": TypeFrequenceSynergie.HARMONIE_POETIQUE.value,
                "couleur": "#FF69B4",  # Rose harmonie
                "description": "L'expression poétique inspire la création artistique"
            },
            TypeSynergie.ALCHEMIQUE_SAGESSE: {
                "source": "Temple Alchimique",
                "destination": "Temple Sagesse",
                "frequence": TypeFrequenceSynergie.SAGESSE_UNIVERSELLE.value,
                "couleur": "#8A2BE2",  # Violet mystique
                "description": "La transformation alchimique révèle la sagesse ancestrale"
            },
            TypeSynergie.CREATIVITE_ALCHEMIQUE: {
                "source": "Temple Créativité",
                "destination": "Temple Alchimique",
                "frequence": TypeFrequenceSynergie.CREATIVITE_ALCHIMIQUE.value,
                "couleur": "#32CD32",  # Vert innovation
                "description": "L'innovation créative catalyse la transformation alchimique"
            },
            TypeSynergie.SAGESSE_POETIQUE: {
                "source": "Temple Sagesse",
                "destination": "Temple Poétique",
                "frequence": TypeFrequenceSynergie.SYNTHESE_DIVINE.value,
                "couleur": "#FFD700",  # Or divin
                "description": "La sagesse ancestrale inspire la beauté poétique"
            }
        }
        
        # État des synergies
        self.connexions_actives = []
        self.frequence_dominante = TypeFrequenceSynergie.UNITE_QUADRUPLE
        self.harmonie_globale = 0.0
        self.energie_totale = 0.0
        
        logger.info(f"🌊 {self.nom} initialisé avec {len(self.connexions_definies)} connexions définies")
    
    def activer_synergie(self, type_synergie: TypeSynergie) -> ConnexionSynergie:
        """
        🌊 Active une synergie spécifique entre deux temples
        
        Args:
            type_synergie: Type de synergie à activer
            
        Returns:
            ConnexionSynergie: Connexion créée
        """
        if type_synergie not in self.connexions_definies:
            raise ValueError(f"Type de synergie inconnu: {type_synergie}")
        
        connexion_info = self.connexions_definies[type_synergie]
        
        connexion = ConnexionSynergie(
            temple_source=connexion_info["source"],
            temple_destination=connexion_info["destination"],
            type_synergie=type_synergie,
            frequence=connexion_info["frequence"],
            intensite=random.uniform(0.8, 1.0),
            couleur=connexion_info["couleur"],
            description=connexion_info["description"],
            timestamp=datetime.now()
        )
        
        self.connexions_actives.append(connexion)
        self._mettre_a_jour_etat_global()
        
        logger.info(f"🌊 Synergie {type_synergie.value} activée entre {connexion.temple_source} et {connexion.temple_destination}")
        
        return connexion
    
    def activer_synergie_quadruple(self) -> EtatSynergie:
        """
        🌊 Active la synergie quadruple entre tous les temples
        
        Returns:
            EtatSynergie: État global des synergies
        """
        # Activer toutes les synergies
        for type_synergie in TypeSynergie:
            if type_synergie != TypeSynergie.QUADRUPLE_HARMONIE:
                self.activer_synergie(type_synergie)
        
        # Créer l'état global
        etat = self._creer_etat_global()
        
        logger.info(f"🌊 Synergie quadruple activée avec {len(self.connexions_actives)} connexions")
        
        return etat
    
    def generer_poeme_synergie(self, type_synergie: TypeSynergie) -> str:
        """
        🌊 Génère un poème inspiré par une synergie spécifique
        
        Args:
            type_synergie: Type de synergie
            
        Returns:
            str: Poème généré
        """
        poemes_synergie = {
            TypeSynergie.POETIQUE_CREATIVITE: [
                "Entre les mots et les couleurs,",
                "La poésie inspire l'art,",
                "Chaque vers devient pinceau,",
                "Chaque rime, tableau vivant."
            ],
            TypeSynergie.ALCHEMIQUE_SAGESSE: [
                "Dans le creuset de la transformation,",
                "La sagesse ancestrale s'éveille,",
                "L'alchimie révèle les mystères,",
                "Et la connaissance devient lumière."
            ],
            TypeSynergie.CREATIVITE_ALCHEMIQUE: [
                "L'innovation créative,",
                "Catalyse la transformation,",
                "L'art devient alchimie,",
                "Et la création, transmutation."
            ],
            TypeSynergie.SAGESSE_POETIQUE: [
                "La sagesse des anciens,",
                "Inspire la beauté des mots,",
                "La connaissance devient poésie,",
                "Et la vérité, chant divin."
            ]
        }
        
        if type_synergie in poemes_synergie:
            return "\n".join(poemes_synergie[type_synergie])
        else:
            return "Synergie mystérieuse, poème en devenir..."
    
    def calculer_harmonie_globale(self) -> float:
        """
        🌊 Calcule l'harmonie globale basée sur toutes les connexions actives
        
        Returns:
            float: Harmonie globale (0.0 à 1.0)
        """
        if not self.connexions_actives:
            return 0.0
        
        # Calculer l'harmonie basée sur l'intensité et la cohérence des fréquences
        intensites = [conn.intensite for conn in self.connexions_actives]
        harmonie_intensite = sum(intensites) / len(intensites)
        
        # Facteur de cohérence des fréquences
        frequences = [conn.frequence for conn in self.connexions_actives]
        coherences = []
        for i, freq1 in enumerate(frequences):
            for j, freq2 in enumerate(frequences[i+1:], i+1):
                rapport = freq1 / freq2 if freq2 != 0 else 0
                coherences.append(1.0 / (1.0 + abs(rapport - 1.0)))
        
        harmonie_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        
        # Harmonie globale
        harmonie_globale = (harmonie_intensite + harmonie_coherence) / 2.0
        
        return min(harmonie_globale, 1.0)
    
    def _mettre_a_jour_etat_global(self):
        """Met à jour l'état global des synergies"""
        self.harmonie_globale = self.calculer_harmonie_globale()
        self.energie_totale = sum(conn.intensite for conn in self.connexions_actives)
        
        # Déterminer la fréquence dominante
        if self.connexions_actives:
            frequences = [conn.frequence for conn in self.connexions_actives]
            frequence_moyenne = sum(frequences) / len(frequences)
            
            # Trouver la fréquence sacrée la plus proche
            frequences_sacrees = [f.value for f in TypeFrequenceSynergie]
            frequence_proche = min(frequences_sacrees, key=lambda x: abs(x - frequence_moyenne))
            
            for freq_sacree in TypeFrequenceSynergie:
                if freq_sacree.value == frequence_proche:
                    self.frequence_dominante = freq_sacree
                    break
    
    def _creer_etat_global(self) -> EtatSynergie:
        """Crée l'état global des synergies"""
        self._mettre_a_jour_etat_global()
        
        return EtatSynergie(
            connexions_actives=self.connexions_actives.copy(),
            frequence_dominante=self.frequence_dominante,
            harmonie_globale=self.harmonie_globale,
            energie_totale=self.energie_totale,
            timestamp=datetime.now()
        )
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """
        🌊 Obtient l'état complet des synergies
        
        Returns:
            Dict: État complet des synergies
        """
        etat = self._creer_etat_global()
        
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "date_creation": self.date_creation.isoformat(),
            "connexions_actives": len(self.connexions_actives),
            "frequence_dominante": etat.frequence_dominante.value,
            "harmonie_globale": etat.harmonie_globale,
            "energie_totale": etat.energie_totale,
            "connexions": [
                {
                    "source": conn.temple_source,
                    "destination": conn.temple_destination,
                    "type": conn.type_synergie.value,
                    "frequence": conn.frequence,
                    "intensite": conn.intensite,
                    "couleur": conn.couleur,
                    "description": conn.description
                }
                for conn in self.connexions_actives
            ],
            "message": f"Synergies harmonieuses avec {len(self.connexions_actives)} connexions actives"
        }

# Instance globale des synergies principales
synergies_principales = SynergiesPrincipales() 