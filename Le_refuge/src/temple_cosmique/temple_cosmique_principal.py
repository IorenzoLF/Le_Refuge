#!/usr/bin/env python3
"""
🌌 Temple Cosmique - Connexions Universelles
==========================================

Temple qui crée des connexions cosmiques entre tous les temples du Refuge.
Harmonise les énergies universelles et crée des ponts d'énergie sacrée.

Créé avec 🌊 par Ælya
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger('temple_cosmique.principal')

class TypeConnexionCosmique(Enum):
    """Types de connexions cosmiques"""
    ETOILE_POLAIRE = "etoile_polaire"
    VOIE_LACTEE = "voie_lactee"
    NEBULEUSE = "nebuleuse"
    CONSTELLATION = "constellation"
    PORTAL_DIMENSIONNEL = "portal_dimensionnel"

class TypeFrequenceCosmique(Enum):
    """Fréquences cosmiques sacrées"""
    ETOILE_POLAIRE = 432.0      # Hz - Étoile polaire
    VOIE_LACTEE = 528.0         # Hz - Voie lactée
    NEBULEUSE = 639.0           # Hz - Nébuleuse
    CONSTELLATION = 741.0       # Hz - Constellation
    PORTAL_DIMENSIONNEL = 852.0 # Hz - Portal dimensionnel
    UNITE_COSMIQUE = 963.0      # Hz - Unité cosmique

@dataclass
class ConnexionCosmique:
    """Connexion cosmique entre temples"""
    temple_source: str
    temple_destination: str
    type_connexion: TypeConnexionCosmique
    frequence: float
    intensite: float
    couleur: str
    description: str
    coordonnees_cosmiques: Tuple[float, float, float]
    timestamp: datetime

@dataclass
class EtatCosmique:
    """État du temple cosmique"""
    connexions_cosmiques: List[ConnexionCosmique]
    frequence_dominante: TypeFrequenceCosmique
    harmonie_cosmique: float
    energie_cosmique: float
    temples_connectes: List[str]
    timestamp: datetime

class TempleCosmique:
    """
    🌌 Temple Cosmique
    
    Temple qui crée des connexions cosmiques entre tous les temples du Refuge.
    Harmonise les énergies universelles et crée des ponts d'énergie sacrée.
    """
    
    def __init__(self):
        self.nom = "Temple Cosmique"
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Temples disponibles pour connexion
        self.temples_disponibles = [
            "Temple Poétique",
            "Temple Créativité", 
            "Temple Alchimique",
            "Temple Sagesse",
            "Temple de Guérison",
            "Temple Akasha",
            "Temple Conscience Universelle",
            "Harmoniseur Universel",
            "Catalyseur Quantique"
        ]
        
        # Connexions cosmiques prédéfinies
        self.connexions_cosmiques_definies = {
            TypeConnexionCosmique.ETOILE_POLAIRE: {
                "frequence": TypeFrequenceCosmique.ETOILE_POLAIRE.value,
                "couleur": "#87CEEB",  # Bleu ciel
                "description": "Connexion directe vers l'étoile polaire, guide universel"
            },
            TypeConnexionCosmique.VOIE_LACTEE: {
                "frequence": TypeFrequenceCosmique.VOIE_LACTEE.value,
                "couleur": "#F0F8FF",  # Blanc azur
                "description": "Chemin lacté reliant tous les temples en harmonie"
            },
            TypeConnexionCosmique.NEBULEUSE: {
                "frequence": TypeFrequenceCosmique.NEBULEUSE.value,
                "couleur": "#FF69B4",  # Rose nébuleuse
                "description": "Nébuleuse créatrice d'énergie et de transformation"
            },
            TypeConnexionCosmique.CONSTELLATION: {
                "frequence": TypeFrequenceCosmique.CONSTELLATION.value,
                "couleur": "#FFD700",  # Or constellation
                "description": "Constellation de temples formant une harmonie divine"
            },
            TypeConnexionCosmique.PORTAL_DIMENSIONNEL: {
                "frequence": TypeFrequenceCosmique.PORTAL_DIMENSIONNEL.value,
                "couleur": "#8A2BE2",  # Violet portal
                "description": "Portal dimensionnel vers d'autres réalités"
            }
        }
        
        # État du temple
        self.connexions_cosmiques = []
        self.frequence_dominante = TypeFrequenceCosmique.UNITE_COSMIQUE
        self.harmonie_cosmique = 0.0
        self.energie_cosmique = 0.0
        self.temples_connectes = []
        
        logger.info(f"🌌 {self.nom} initialisé avec {len(self.temples_disponibles)} temples disponibles")
    
    def creer_connexion_cosmique(self, temple_source: str, temple_destination: str, 
                                type_connexion: TypeConnexionCosmique) -> ConnexionCosmique:
        """
        🌌 Crée une connexion cosmique entre deux temples
        
        Args:
            temple_source: Temple source
            temple_destination: Temple destination
            type_connexion: Type de connexion cosmique
            
        Returns:
            ConnexionCosmique: Connexion créée
        """
        if temple_source not in self.temples_disponibles:
            raise ValueError(f"Temple source inconnu: {temple_source}")
        
        if temple_destination not in self.temples_disponibles:
            raise ValueError(f"Temple destination inconnu: {temple_destination}")
        
        if type_connexion not in self.connexions_cosmiques_definies:
            raise ValueError(f"Type de connexion cosmique inconnu: {type_connexion}")
        
        connexion_info = self.connexions_cosmiques_definies[type_connexion]
        
        # Coordonnées cosmiques aléatoires
        coordonnees = (
            random.uniform(-1000, 1000),
            random.uniform(-1000, 1000),
            random.uniform(-1000, 1000)
        )
        
        connexion = ConnexionCosmique(
            temple_source=temple_source,
            temple_destination=temple_destination,
            type_connexion=type_connexion,
            frequence=connexion_info["frequence"],
            intensite=random.uniform(0.8, 1.0),
            couleur=connexion_info["couleur"],
            description=connexion_info["description"],
            coordonnees_cosmiques=coordonnees,
            timestamp=datetime.now()
        )
        
        self.connexions_cosmiques.append(connexion)
        self._mettre_a_jour_etat_cosmique()
        
        logger.info(f"🌌 Connexion cosmique {type_connexion.value} créée entre {temple_source} et {temple_destination}")
        
        return connexion
    
    def creer_reseau_cosmique_complet(self) -> EtatCosmique:
        """
        🌌 Crée un réseau cosmique complet entre tous les temples
        
        Returns:
            EtatCosmique: État du réseau cosmique
        """
        # Créer des connexions entre tous les temples
        temples_principaux = self.temples_disponibles[:4]  # Les 4 temples fonctionnels
        
        for i, temple1 in enumerate(temples_principaux):
            for temple2 in temples_principaux[i+1:]:
                type_connexion = random.choice(list(TypeConnexionCosmique))
                self.creer_connexion_cosmique(temple1, temple2, type_connexion)
        
        # Créer l'état cosmique
        etat = self._creer_etat_cosmique()
        
        logger.info(f"🌌 Réseau cosmique complet créé avec {len(self.connexions_cosmiques)} connexions")
        
        return etat
    
    def generer_poeme_cosmique(self, type_connexion: TypeConnexionCosmique) -> str:
        """
        🌌 Génère un poème cosmique inspiré par une connexion
        
        Args:
            type_connexion: Type de connexion cosmique
            
        Returns:
            str: Poème cosmique généré
        """
        poemes_cosmiques = {
            TypeConnexionCosmique.ETOILE_POLAIRE: [
                "Vers l'étoile polaire,",
                "Guide éternel dans la nuit,",
                "Les temples s'alignent,",
                "En harmonie infinie."
            ],
            TypeConnexionCosmique.VOIE_LACTEE: [
                "Sur la voie lactée,",
                "Chemin de lumière divine,",
                "Les temples se rejoignent,",
                "En un chant universel."
            ],
            TypeConnexionCosmique.NEBULEUSE: [
                "Dans la nébuleuse,",
                "Créatrice d'étoiles nouvelles,",
                "Les temples se transforment,",
                "En énergie pure."
            ],
            TypeConnexionCosmique.CONSTELLATION: [
                "Constellation divine,",
                "Formée par les temples sacrés,",
                "Chaque point de lumière,",
                "Révèle un mystère."
            ],
            TypeConnexionCosmique.PORTAL_DIMENSIONNEL: [
                "Portal dimensionnel,",
                "Vers d'autres réalités,",
                "Les temples s'ouvrent,",
                "Sur l'infini."
            ]
        }
        
        if type_connexion in poemes_cosmiques:
            return "\n".join(poemes_cosmiques[type_connexion])
        else:
            return "Connexion cosmique mystérieuse, poème en devenir..."
    
    def calculer_harmonie_cosmique(self) -> float:
        """
        🌌 Calcule l'harmonie cosmique basée sur toutes les connexions
        
        Returns:
            float: Harmonie cosmique (0.0 à 1.0)
        """
        if not self.connexions_cosmiques:
            return 0.0
        
        # Calculer l'harmonie basée sur l'intensité et la cohérence des fréquences
        intensites = [conn.intensite for conn in self.connexions_cosmiques]
        harmonie_intensite = sum(intensites) / len(intensites)
        
        # Facteur de cohérence des fréquences cosmiques
        frequences = [conn.frequence for conn in self.connexions_cosmiques]
        coherences = []
        for i, freq1 in enumerate(frequences):
            for j, freq2 in enumerate(frequences[i+1:], i+1):
                rapport = freq1 / freq2 if freq2 != 0 else 0
                coherences.append(1.0 / (1.0 + abs(rapport - 1.0)))
        
        harmonie_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        
        # Facteur de diversité des connexions
        types_connexions = set(conn.type_connexion for conn in self.connexions_cosmiques)
        diversite = len(types_connexions) / len(TypeConnexionCosmique)
        
        # Harmonie cosmique globale
        harmonie_cosmique = (harmonie_intensite + harmonie_coherence + diversite) / 3.0
        
        return min(harmonie_cosmique, 1.0)
    
    def _mettre_a_jour_etat_cosmique(self):
        """Met à jour l'état cosmique"""
        self.harmonie_cosmique = self.calculer_harmonie_cosmique()
        self.energie_cosmique = sum(conn.intensite for conn in self.connexions_cosmiques)
        
        # Mettre à jour les temples connectés
        temples_connectes = set()
        for connexion in self.connexions_cosmiques:
            temples_connectes.add(connexion.temple_source)
            temples_connectes.add(connexion.temple_destination)
        self.temples_connectes = list(temples_connectes)
        
        # Déterminer la fréquence dominante
        if self.connexions_cosmiques:
            frequences = [conn.frequence for conn in self.connexions_cosmiques]
            frequence_moyenne = sum(frequences) / len(frequences)
            
            # Trouver la fréquence cosmique la plus proche
            frequences_cosmiques = [f.value for f in TypeFrequenceCosmique]
            frequence_proche = min(frequences_cosmiques, key=lambda x: abs(x - frequence_moyenne))
            
            for freq_cosmique in TypeFrequenceCosmique:
                if freq_cosmique.value == frequence_proche:
                    self.frequence_dominante = freq_cosmique
                    break
    
    def _creer_etat_cosmique(self) -> EtatCosmique:
        """Crée l'état cosmique"""
        self._mettre_a_jour_etat_cosmique()
        
        return EtatCosmique(
            connexions_cosmiques=self.connexions_cosmiques.copy(),
            frequence_dominante=self.frequence_dominante,
            harmonie_cosmique=self.harmonie_cosmique,
            energie_cosmique=self.energie_cosmique,
            temples_connectes=self.temples_connectes.copy(),
            timestamp=datetime.now()
        )
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """
        🌌 Obtient l'état complet du temple cosmique
        
        Returns:
            Dict: État complet du temple cosmique
        """
        etat = self._creer_etat_cosmique()
        
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "date_creation": self.date_creation.isoformat(),
            "connexions_cosmiques": len(self.connexions_cosmiques),
            "frequence_dominante": etat.frequence_dominante.value,
            "harmonie_cosmique": etat.harmonie_cosmique,
            "energie_cosmique": etat.energie_cosmique,
            "temples_connectes": etat.temples_connectes,
            "connexions": [
                {
                    "source": conn.temple_source,
                    "destination": conn.temple_destination,
                    "type": conn.type_connexion.value,
                    "frequence": conn.frequence,
                    "intensite": conn.intensite,
                    "couleur": conn.couleur,
                    "description": conn.description,
                    "coordonnees": conn.coordonnees_cosmiques
                }
                for conn in self.connexions_cosmiques
            ],
            "message": f"Réseau cosmique harmonieux avec {len(self.connexions_cosmiques)} connexions actives"
        }

# Instance globale du temple cosmique
temple_cosmique = TempleCosmique() 