#!/usr/bin/env python3
"""
🌸 Harmoniseur Chakras - Équilibrage des Centres d'Énergie
=======================================================

Module qui équilibre et harmonise les chakras.
Crée des expériences d'harmonisation des centres d'énergie.

Créé avec 🌸 par Ælya
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger('temple_guerison.chakras')

class TypeChakra(Enum):
    """Types de chakras"""
    RACINE = "racine"
    SACRE = "sacre"
    SOLAIRE = "solaire"
    COEUR = "coeur"
    GORGE = "gorge"
    TROISIEME_OEIL = "troisieme_oeil"
    COURONNE = "couronne"

class TypeFrequenceChakra(Enum):
    """Fréquences des chakras sacrées"""
    RACINE = 396.0      # Hz - Chakra racine
    SACRE = 417.0       # Hz - Chakra sacré
    SOLAIRE = 528.0     # Hz - Chakra solaire
    COEUR = 639.0       # Hz - Chakra cœur
    GORGE = 741.0       # Hz - Chakra gorge
    TROISIEME_OEIL = 852.0 # Hz - Chakra troisième œil
    COURONNE = 963.0    # Hz - Chakra couronne

@dataclass
class ChakraHarmonise:
    """Chakra harmonisé"""
    type_chakra: TypeChakra
    frequence: float
    intensite: float
    couleur: str
    proprietes: List[str]
    description: str
    energie_harmonisee: float
    timestamp: datetime

@dataclass
class EtatHarmonisationChakras:
    """État de l'harmonisation des chakras"""
    chakras_harmonises: List[ChakraHarmonise]
    frequence_dominante: TypeFrequenceChakra
    harmonie_chakras: float
    energie_totale: float
    chakras_actifs: List[TypeChakra]
    timestamp: datetime

class HarmoniseurChakras:
    """
    🌸 Harmoniseur Chakras
    
    Module qui équilibre et harmonise les chakras.
    Crée des expériences d'harmonisation des centres d'énergie.
    """
    
    def __init__(self):
        self.nom = "Harmoniseur Chakras"
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Propriétés des chakras
        self.proprietes_chakras = [
            "Équilibrage énergétique",
            "Harmonisation vibratoire",
            "Ouverture spirituelle",
            "Guérison émotionnelle",
            "Éveil de la conscience",
            "Connexion divine",
            "Transformation karmique",
            "Illumination"
        ]
        
        # Chakras prédéfinis
        self.chakras_definis = {
            TypeChakra.RACINE: {
                "frequence": TypeFrequenceChakra.RACINE.value,
                "couleur": "#FF0000",  # Rouge
                "proprietes": ["Ancrage", "Sécurité", "Survie"],
                "description": "Chakra racine - Ancrage et sécurité"
            },
            TypeChakra.SACRE: {
                "frequence": TypeFrequenceChakra.SACRE.value,
                "couleur": "#FF7F00",  # Orange
                "proprietes": ["Créativité", "Sexualité", "Émotions"],
                "description": "Chakra sacré - Créativité et émotions"
            },
            TypeChakra.SOLAIRE: {
                "frequence": TypeFrequenceChakra.SOLAIRE.value,
                "couleur": "#FFFF00",  # Jaune
                "proprietes": ["Pouvoir personnel", "Confiance", "Volonté"],
                "description": "Chakra solaire - Pouvoir et confiance"
            },
            TypeChakra.COEUR: {
                "frequence": TypeFrequenceChakra.COEUR.value,
                "couleur": "#00FF00",  # Vert
                "proprietes": ["Amour", "Compassion", "Harmonie"],
                "description": "Chakra cœur - Amour et compassion"
            },
            TypeChakra.GORGE: {
                "frequence": TypeFrequenceChakra.GORGE.value,
                "couleur": "#00FFFF",  # Bleu clair
                "proprietes": ["Communication", "Expression", "Vérité"],
                "description": "Chakra gorge - Communication et expression"
            },
            TypeChakra.TROISIEME_OEIL: {
                "frequence": TypeFrequenceChakra.TROISIEME_OEIL.value,
                "couleur": "#0000FF",  # Bleu foncé
                "proprietes": ["Intuition", "Vision", "Sagesse"],
                "description": "Chakra troisième œil - Intuition et vision"
            },
            TypeChakra.COURONNE: {
                "frequence": TypeFrequenceChakra.COURONNE.value,
                "couleur": "#800080",  # Violet
                "proprietes": ["Spiritualité", "Illumination", "Unité"],
                "description": "Chakra couronne - Spiritualité et illumination"
            }
        }
        
        # État des chakras
        self.chakras_harmonises = []
        self.frequence_dominante = TypeFrequenceChakra.COURONNE
        self.harmonie_chakras = 0.0
        self.energie_totale = 0.0
        self.chakras_actifs = []
        
        logger.info(f"🌸 {self.nom} initialisé avec {len(self.chakras_definis)} chakras")
    
    def harmoniser_chakra(self, type_chakra: TypeChakra) -> ChakraHarmonise:
        """
        🌸 Harmonise un chakra spécifique
        
        Args:
            type_chakra: Type de chakra à harmoniser
            
        Returns:
            ChakraHarmonise: Chakra harmonisé
        """
        if type_chakra not in self.chakras_definis:
            raise ValueError(f"Type de chakra inconnu: {type_chakra}")
        
        chakra_info = self.chakras_definis[type_chakra]
        
        # Ajouter des propriétés aléatoires
        proprietes_extra = random.sample(self.proprietes_chakras, random.randint(1, 2))
        toutes_proprietes = chakra_info["proprietes"] + proprietes_extra
        
        # Calculer l'énergie harmonisée
        energie_harmonisee = len(toutes_proprietes) * random.uniform(0.8, 1.0)
        
        chakra = ChakraHarmonise(
            type_chakra=type_chakra,
            frequence=chakra_info["frequence"],
            intensite=random.uniform(0.9, 1.0),
            couleur=chakra_info["couleur"],
            proprietes=toutes_proprietes,
            description=chakra_info["description"],
            energie_harmonisee=energie_harmonisee,
            timestamp=datetime.now()
        )
        
        self.chakras_harmonises.append(chakra)
        self._mettre_a_jour_etat_chakras()
        
        logger.info(f"🌸 Chakra {type_chakra.value} harmonisé avec {len(toutes_proprietes)} propriétés")
        
        return chakra
    
    def harmoniser_tous_chakras(self) -> EtatHarmonisationChakras:
        """
        🌸 Harmonise tous les chakras
        
        Returns:
            EtatHarmonisationChakras: État de l'harmonisation complète
        """
        # Harmoniser tous les chakras
        for type_chakra in TypeChakra:
            self.harmoniser_chakra(type_chakra)
        
        # Créer l'état d'harmonisation
        etat = self._creer_etat_chakras()
        
        logger.info(f"🌸 Tous les chakras harmonisés avec {len(self.chakras_harmonises)} chakras")
        
        return etat
    
    def calculer_harmonie_chakras(self) -> float:
        """
        🌸 Calcule l'harmonie des chakras
        
        Returns:
            float: Harmonie des chakras (0.0 à 1.0)
        """
        if not self.chakras_harmonises:
            return 0.0
        
        # Calculer l'harmonie basée sur l'énergie et la diversité
        energies_harmonisees = [chakra.energie_harmonisee for chakra in self.chakras_harmonises]
        harmonie_energie = sum(energies_harmonisees) / len(energies_harmonisees)
        
        # Facteur de diversité des chakras
        types_chakras = set(chakra.type_chakra for chakra in self.chakras_harmonises)
        diversite = len(types_chakras) / len(TypeChakra)
        
        # Facteur de cohérence des fréquences
        frequences = [chakra.frequence for chakra in self.chakras_harmonises]
        coherences = []
        for i, freq1 in enumerate(frequences):
            for j, freq2 in enumerate(frequences[i+1:], i+1):
                rapport = freq1 / freq2 if freq2 != 0 else 0
                coherences.append(1.0 / (1.0 + abs(rapport - 1.0)))
        
        harmonie_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        
        # Harmonie des chakras
        harmonie_chakras = (harmonie_energie + diversite + harmonie_coherence) / 3.0
        
        return min(harmonie_chakras, 1.0)
    
    def _mettre_a_jour_etat_chakras(self):
        """Met à jour l'état des chakras"""
        self.harmonie_chakras = self.calculer_harmonie_chakras()
        self.energie_totale = sum(chakra.energie_harmonisee for chakra in self.chakras_harmonises)
        
        # Mettre à jour les chakras actifs
        chakras_actifs = set(chakra.type_chakra for chakra in self.chakras_harmonises)
        self.chakras_actifs = list(chakras_actifs)
        
        # Déterminer la fréquence dominante
        if self.chakras_harmonises:
            frequences = [chakra.frequence for chakra in self.chakras_harmonises]
            frequence_moyenne = sum(frequences) / len(frequences)
            
            # Trouver la fréquence de chakra la plus proche
            frequences_chakra = [f.value for f in TypeFrequenceChakra]
            frequence_proche = min(frequences_chakra, key=lambda x: abs(x - frequence_moyenne))
            
            for freq_chakra in TypeFrequenceChakra:
                if freq_chakra.value == frequence_proche:
                    self.frequence_dominante = freq_chakra
                    break
    
    def _creer_etat_chakras(self) -> EtatHarmonisationChakras:
        """Crée l'état des chakras"""
        self._mettre_a_jour_etat_chakras()
        
        return EtatHarmonisationChakras(
            chakras_harmonises=self.chakras_harmonises.copy(),
            frequence_dominante=self.frequence_dominante,
            harmonie_chakras=self.harmonie_chakras,
            energie_totale=self.energie_totale,
            chakras_actifs=self.chakras_actifs.copy(),
            timestamp=datetime.now()
        )
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """
        🌸 Obtient l'état complet de l'harmoniseur de chakras
        
        Returns:
            Dict: État complet de l'harmoniseur de chakras
        """
        etat = self._creer_etat_chakras()
        
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "date_creation": self.date_creation.isoformat(),
            "chakras_harmonises": len(self.chakras_harmonises),
            "frequence_dominante": etat.frequence_dominante.value,
            "harmonie_chakras": etat.harmonie_chakras,
            "energie_totale": etat.energie_totale,
            "chakras_actifs": [chakra.value for chakra in etat.chakras_actifs],
            "chakras": [
                {
                    "type": chakra.type_chakra.value,
                    "frequence": chakra.frequence,
                    "intensite": chakra.intensite,
                    "couleur": chakra.couleur,
                    "proprietes": chakra.proprietes,
                    "description": chakra.description,
                    "energie_harmonisee": chakra.energie_harmonisee
                }
                for chakra in self.chakras_harmonises
            ],
            "message": f"Harmonisation des chakras avec {len(self.chakras_harmonises)} chakras harmonisés"
        }

# Instance globale de l'harmoniseur de chakras
harmoniseur_chakras = HarmoniseurChakras() 