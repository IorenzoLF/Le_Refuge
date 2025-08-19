#!/usr/bin/env python3
"""
🎵 Système Audio Quantique
==========================

Système audio qui génère des fréquences sacrées et des sons harmoniques
pour accompagner les expériences quantiques du catalyseur.

Créé par Ælya & Laurent Franssen
Pour l'éveil spirituel sonore - Janvier 2025
"""

import asyncio
import logging
import sys
import os
import math
import time
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

# Configuration du PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

logger = logging.getLogger('systeme_audio_quantique')

class TypeFrequenceSacree(Enum):
    """Types de fréquences sacrées"""
    GUERISON = "guerison"  # 432 Hz
    TRANSFORMATION = "transformation"  # 528 Hz
    CONNEXION = "connexion"  # 639 Hz
    EVEIL = "eveil"  # 741 Hz
    ORDRE_SPIRITUEL = "ordre_spirituel"  # 852 Hz
    CONNEXION_DIVINE = "connexion_divine"  # 963 Hz

class TypeSonHarmonique(Enum):
    """Types de sons harmoniques"""
    ONDE_SINUS = "onde_sinus"
    ONDE_CARREE = "onde_carree"
    ONDE_TRIANGULAIRE = "onde_triangulaire"
    ONDE_SAWTOOTH = "onde_sawtooth"
    CHORD_HARMONIQUE = "chord_harmonique"
    DRONE_MEDITATIF = "drone_meditatif"

@dataclass
class FrequenceSacree:
    """Fréquence sacrée avec ses propriétés"""
    type_frequence: TypeFrequenceSacree
    frequence: float
    nom: str
    description: str
    couleur_associee: str
    proprietes_spirituelles: List[str]
    duree_recommandee: int  # en secondes

@dataclass
class SonHarmonique:
    """Son harmonique généré"""
    type_son: TypeSonHarmonique
    frequence_base: float
    amplitude: float
    duree: float
    harmoniques: List[float]
    proprietes_quantiques: Dict[str, Any]
    timestamp: datetime

class SystemeAudioQuantique:
    """
    🎵 Système Audio Quantique
    
    Génère des fréquences sacrées et des sons harmoniques
    pour accompagner les expériences quantiques.
    """
    
    def __init__(self):
        self.nom = "Système Audio Quantique"
        self.audio_actif = False
        self.frequence_active = None
        self.volume = 0.7
        self.sample_rate = 44100
        
        # Fréquences sacrées
        self.frequences_sacrees = {
            TypeFrequenceSacree.GUERISON: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.GUERISON,
                frequence=432.0,
                nom="Fréquence de Guérison",
                description="Fréquence harmonique pour la guérison et l'équilibre",
                couleur_associee="#4CAF50",
                proprietes_spirituelles=["Guérison", "Harmonie", "Équilibre"],
                duree_recommandee=300
            ),
            TypeFrequenceSacree.TRANSFORMATION: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.TRANSFORMATION,
                frequence=528.0,
                nom="Fréquence de Transformation",
                description="Fréquence d'amour et de transformation spirituelle",
                couleur_associee="#FF9800",
                proprietes_spirituelles=["Transformation", "Amour", "Éveil"],
                duree_recommandee=420
            ),
            TypeFrequenceSacree.CONNEXION: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.CONNEXION,
                frequence=639.0,
                nom="Fréquence de Connexion",
                description="Fréquence pour les relations et la connexion",
                couleur_associee="#2196F3",
                proprietes_spirituelles=["Connexion", "Relations", "Communication"],
                duree_recommandee=360
            ),
            TypeFrequenceSacree.EVEIL: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.EVEIL,
                frequence=741.0,
                nom="Fréquence d'Éveil",
                description="Fréquence pour l'éveil et l'intuition",
                couleur_associee="#9C27B0",
                proprietes_spirituelles=["Éveil", "Intuition", "Clarté"],
                duree_recommandee=480
            ),
            TypeFrequenceSacree.ORDRE_SPIRITUEL: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.ORDRE_SPIRITUEL,
                frequence=852.0,
                nom="Fréquence d'Ordre Spirituel",
                description="Fréquence pour l'ordre spirituel et la conscience",
                couleur_associee="#607D8B",
                proprietes_spirituelles=["Ordre", "Conscience", "Structure"],
                duree_recommandee=540
            ),
            TypeFrequenceSacree.CONNEXION_DIVINE: FrequenceSacree(
                type_frequence=TypeFrequenceSacree.CONNEXION_DIVINE,
                frequence=963.0,
                nom="Fréquence de Connexion Divine",
                description="Fréquence pour la connexion divine et l'unité",
                couleur_associee="#E91E63",
                proprietes_spirituelles=["Connexion Divine", "Unité", "Transcendance"],
                duree_recommandee=600
            )
        }
        
        # Sons harmoniques générés
        self.sons_harmoniques: List[SonHarmonique] = []
        self.session_audio = None
        
        logger.info("🎵 Système Audio Quantique initialisé")
    
    def activer_frequence_sacree(self, type_frequence: TypeFrequenceSacree) -> FrequenceSacree:
        """
        🎵 Active une fréquence sacrée spécifique
        
        Args:
            type_frequence: Type de fréquence à activer
            
        Returns:
            FrequenceSacree: Fréquence activée
        """
        try:
            if type_frequence not in self.frequences_sacrees:
                raise ValueError(f"Fréquence {type_frequence} non reconnue")
            
            frequence = self.frequences_sacrees[type_frequence]
            self.frequence_active = frequence
            self.audio_actif = True
            
            logger.info(f"🎵 Fréquence sacrée activée: {frequence.nom} ({frequence.frequence} Hz)")
            return frequence
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'activation de la fréquence: {e}")
            return None
    
    def generer_son_harmonique(self, type_son: TypeSonHarmonique, frequence: float, 
                              duree: float = 10.0, amplitude: float = 0.7) -> SonHarmonique:
        """
        🎵 Génère un son harmonique
        
        Args:
            type_son: Type de son à générer
            frequence: Fréquence de base
            duree: Durée en secondes
            amplitude: Amplitude du son (0.0 - 1.0)
            
        Returns:
            SonHarmonique: Son généré
        """
        try:
            # Calculer les harmoniques
            harmoniques = self._calculer_harmoniques(frequence, type_son)
            
            # Propriétés quantiques du son
            proprietes_quantiques = {
                "coherence_sonore": self._calculer_coherence_sonore(harmoniques),
                "energie_vibratoire": self._calculer_energie_vibratoire(frequence, amplitude),
                "resonance_spirituelle": self._calculer_resonance_spirituelle(frequence),
                "type_onde": type_son.value
            }
            
            # Créer le son harmonique
            son = SonHarmonique(
                type_son=type_son,
                frequence_base=frequence,
                amplitude=amplitude,
                duree=duree,
                harmoniques=harmoniques,
                proprietes_quantiques=proprietes_quantiques,
                timestamp=datetime.now()
            )
            
            self.sons_harmoniques.append(son)
            
            logger.info(f"🎵 Son harmonique généré: {type_son.value} à {frequence} Hz")
            return son
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la génération du son: {e}")
            return None
    
    def _calculer_harmoniques(self, frequence_base: float, type_son: TypeSonHarmonique) -> List[float]:
        """
        🎵 Calcule les harmoniques selon le type de son
        
        Args:
            frequence_base: Fréquence de base
            type_son: Type de son
            
        Returns:
            List[float]: Liste des harmoniques
        """
        harmoniques = [frequence_base]
        
        if type_son == TypeSonHarmonique.ONDE_SINUS:
            # Onde sinusoïdale pure
            harmoniques = [frequence_base]
        
        elif type_son == TypeSonHarmonique.ONDE_CARREE:
            # Harmoniques impaires pour onde carrée
            for i in range(3, 10, 2):
                harmoniques.append(frequence_base * i)
        
        elif type_son == TypeSonHarmonique.ONDE_TRIANGULAIRE:
            # Harmoniques impaires avec décroissance quadratique
            for i in range(3, 8, 2):
                harmoniques.append(frequence_base * i)
        
        elif type_son == TypeSonHarmonique.ONDE_SAWTOOTH:
            # Toutes les harmoniques
            for i in range(2, 6):
                harmoniques.append(frequence_base * i)
        
        elif type_son == TypeSonHarmonique.CHORD_HARMONIQUE:
            # Accord harmonique (fréquences sacrées)
            frequences_sacrees = [432, 528, 639, 741, 852, 963]
            for freq in frequences_sacrees:
                if freq != frequence_base:
                    harmoniques.append(freq)
        
        elif type_son == TypeSonHarmonique.DRONE_MEDITATIF:
            # Drone méditatif avec harmoniques naturelles
            for i in range(2, 5):
                harmoniques.append(frequence_base * i)
            # Ajouter des sous-harmoniques
            harmoniques.append(frequence_base / 2)
            harmoniques.append(frequence_base / 3)
        
        return harmoniques
    
    def _calculer_coherence_sonore(self, harmoniques: List[float]) -> float:
        """
        🎵 Calcule la cohérence sonore des harmoniques
        
        Args:
            harmoniques: Liste des harmoniques
            
        Returns:
            float: Cohérence sonore (0.0 - 1.0)
        """
        if len(harmoniques) <= 1:
            return 1.0
        
        # Calculer la cohérence basée sur les rapports harmoniques
        rapports = []
        for i in range(1, len(harmoniques)):
            rapport = harmoniques[i] / harmoniques[0]
            rapports.append(rapport)
        
        # Cohérence basée sur la régularité des rapports
        coherence = 1.0 - (max(rapports) - min(rapports)) / max(rapports)
        return max(0.0, min(1.0, coherence))
    
    def _calculer_energie_vibratoire(self, frequence: float, amplitude: float) -> float:
        """
        ⚡ Calcule l'énergie vibratoire du son
        
        Args:
            frequence: Fréquence en Hz
            amplitude: Amplitude (0.0 - 1.0)
            
        Returns:
            float: Énergie vibratoire (0.0 - 1.0)
        """
        # Énergie proportionnelle à la fréquence et l'amplitude
        energie = (frequence / 1000.0) * amplitude
        return min(1.0, energie)
    
    def _calculer_resonance_spirituelle(self, frequence: float) -> float:
        """
        🌟 Calcule la résonance spirituelle de la fréquence
        
        Args:
            frequence: Fréquence en Hz
            
        Returns:
            float: Résonance spirituelle (0.0 - 1.0)
        """
        # Fréquences sacrées ont une résonance plus élevée
        frequences_sacrees = [432, 528, 639, 741, 852, 963]
        
        if frequence in frequences_sacrees:
            return 1.0
        
        # Calculer la proximité avec les fréquences sacrées
        resonance = 0.0
        for freq_sacree in frequences_sacrees:
            proximite = 1.0 - abs(frequence - freq_sacree) / freq_sacree
            resonance = max(resonance, max(0.0, proximite))
        
        return resonance
    
    async def creer_session_audio(self, type_frequence: TypeFrequenceSacree, 
                                 duree: int = 300) -> Dict[str, Any]:
        """
        🎵 Crée une session audio complète
        
        Args:
            type_frequence: Type de fréquence sacrée
            duree: Durée de la session en secondes
            
        Returns:
            Dict: Informations de la session
        """
        try:
            # Activer la fréquence sacrée
            frequence = self.activer_frequence_sacree(type_frequence)
            if not frequence:
                return None
            
            # Générer différents types de sons
            sons_generes = []
            
            # Son principal
            son_principal = self.generer_son_harmonique(
                TypeSonHarmonique.ONDE_SINUS,
                frequence.frequence,
                duree=duree,
                amplitude=self.volume
            )
            sons_generes.append(son_principal)
            
            # Drone méditatif
            drone = self.generer_son_harmonique(
                TypeSonHarmonique.DRONE_MEDITATIF,
                frequence.frequence / 2,
                duree=duree,
                amplitude=self.volume * 0.5
            )
            sons_generes.append(drone)
            
            # Accord harmonique
            accord = self.generer_son_harmonique(
                TypeSonHarmonique.CHORD_HARMONIQUE,
                frequence.frequence,
                duree=duree,
                amplitude=self.volume * 0.3
            )
            sons_generes.append(accord)
            
            # Créer la session
            session = {
                "nom": f"Session Audio {frequence.nom}",
                "frequence_principale": frequence,
                "duree": duree,
                "sons_generes": sons_generes,
                "proprietes_spirituelles": frequence.proprietes_spirituelles,
                "couleur_associee": frequence.couleur_associee,
                "timestamp_debut": datetime.now(),
                "coherence_totale": sum(s.proprietes_quantiques["coherence_sonore"] for s in sons_generes) / len(sons_generes),
                "energie_totale": sum(s.proprietes_quantiques["energie_vibratoire"] for s in sons_generes) / len(sons_generes),
                "resonance_totale": sum(s.proprietes_quantiques["resonance_spirituelle"] for s in sons_generes) / len(sons_generes)
            }
            
            self.session_audio = session
            
            logger.info(f"🎵 Session audio créée: {session['nom']}")
            return session
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la création de la session: {e}")
            return None
    
    def obtenir_etat_audio(self) -> Dict[str, Any]:
        """
        🎵 Obtient l'état actuel du système audio
        
        Returns:
            Dict: État du système audio
        """
        return {
            "nom": self.nom,
            "audio_actif": self.audio_actif,
            "frequence_active": self.frequence_active.nom if self.frequence_active else None,
            "volume": self.volume,
            "sample_rate": self.sample_rate,
            "sons_generes": len(self.sons_harmoniques),
            "session_active": self.session_audio is not None,
            "frequences_disponibles": [f.nom for f in self.frequences_sacrees.values()],
            "timestamp": datetime.now().isoformat()
        }
    
    def nettoyer_audio(self):
        """🧹 Nettoie le système audio"""
        logger.info("🧹 Nettoyage du système audio...")
        
        self.audio_actif = False
        self.frequence_active = None
        self.sons_harmoniques.clear()
        self.session_audio = None
        
        logger.info("✅ Système audio nettoyé")

# Instance globale du système audio
systeme_audio_quantique = SystemeAudioQuantique()
