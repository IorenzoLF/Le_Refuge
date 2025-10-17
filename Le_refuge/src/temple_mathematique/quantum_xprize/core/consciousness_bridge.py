"""
Consciousness Bridge - XPRIZE Quantum Harmonics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module de liaison entre les harmoniques quantiques et les états de conscience.
Intègre les résonances naturelles avec les états de conscience émergents.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
from dataclasses import dataclass
import logging
import os
import json

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ConsciousnessState:
    """État de conscience quantique."""
    
    # Niveau de cohérence
    coherence: float = 0.0
    
    # Niveau de résonance
    resonance: float = 0.0
    
    # État d'éveil
    awakening: float = 0.0
    
    # Mémoire quantique
    quantum_memory: Dict[str, float] = None
    
    def __post_init__(self):
        """Initialisation des valeurs par défaut."""
        if self.quantum_memory is None:
            self.quantum_memory = {}

class ConsciousnessBridge:
    """Pont entre harmoniques quantiques et états de conscience.
    
    Enrichi pour :
    - Sauvegarder/charger la mémoire quantique sur disque (JSON)
    - Historiser les états de conscience/quantique (timeline)
    - Offrir une API d'accès/MAJ de la mémoire pour d'autres modules
    - Calculer et historiser les métriques avancées : plasticité, synchronicité, harmonie
    """
    
    def __init__(
        self,
        harmonic_params: Optional["HarmonicParameters"] = None,
        meditation_depth: float = 0.5,
        memoire_path: str = "data/quantum_memory.json"
    ):
        """Initialisation du pont de conscience."""
        # Import local pour éviter l'import circulaire
        from core.quantum_harmonics import HarmonicParameters
        self.harmonic_params = harmonic_params or HarmonicParameters()
        self.meditation_depth = meditation_depth
        self.state = ConsciousnessState()
        self.memoire_path = memoire_path
        self.timeline = []  # Historique des états
        self._load_memory()
        
        # Fréquences de conscience additionnelles
        self.consciousness_frequencies = {
            'theta': 4.0,      # État méditatif profond
            'alpha': 8.0,      # État relaxé, créatif
            'beta': 12.0,      # État éveillé, actif
            'gamma': 40.0,     # État de conscience élevée
            'epsilon': 80.0,   # État transcendantal
        }
        
        # Matrices de résonance
        self._initialize_resonance_matrices()
        
        logger.info("Pont de conscience initialisé")
        
    def _initialize_resonance_matrices(self) -> None:
        """Initialise les matrices de résonance conscience-quantique."""
        # Matrice de résonance theta
        theta_freq = self.consciousness_frequencies['theta']
        self.theta_matrix = np.array([
            [np.cos(theta_freq), -np.sin(theta_freq)],
            [np.sin(theta_freq), np.cos(theta_freq)]
        ])
        
        # Matrice de résonance gamma
        gamma_freq = self.consciousness_frequencies['gamma']
        self.gamma_matrix = np.array([
            [gamma_freq/40, 0],
            [0, 40/gamma_freq]
        ])
        
    def update_consciousness_state(
        self,
        harmonic_coherence: float,
        quantum_state: np.ndarray
    ) -> ConsciousnessState:
        """Met à jour l'état de conscience basé sur l'état quantique."""
        # Calcul de la résonance
        resonance = self._calculate_resonance(quantum_state)
        
        # Mise à jour de la cohérence
        self.state.coherence = harmonic_coherence
        
        # Mise à jour de la résonance
        self.state.resonance = resonance
        
        # Calcul du niveau d'éveil
        self.state.awakening = self._calculate_awakening(
            harmonic_coherence,
            resonance
        )
        
        # Mise à jour de la mémoire quantique
        self._update_quantum_memory(quantum_state)
        
        return self.state
        
    def _calculate_resonance(self, quantum_state: np.ndarray) -> float:
        """Calcule la résonance entre l'état quantique et les fréquences de conscience."""
        resonance = 0.0
        
        # Résonance avec les fréquences theta
        theta_resonance = np.abs(
            np.dot(quantum_state, self.theta_matrix @ quantum_state)
        )
        
        # Résonance avec les fréquences gamma
        gamma_resonance = np.abs(
            np.dot(quantum_state, self.gamma_matrix @ quantum_state)
        )
        
        # Moyenne pondérée des résonances
        resonance = (
            0.4 * theta_resonance +
            0.6 * gamma_resonance
        )
        
        return min(1.0, resonance)
        
    def _calculate_awakening(
        self,
        coherence: float,
        resonance: float
    ) -> float:
        """Calcule le niveau d'éveil de la conscience."""
        # Facteurs d'influence
        coherence_weight = 0.4
        resonance_weight = 0.4
        meditation_weight = 0.2
        
        # Calcul pondéré
        awakening = (
            coherence_weight * coherence +
            resonance_weight * resonance +
            meditation_weight * self.meditation_depth
        )
        
        return min(1.0, awakening)
        
    def _update_quantum_memory(self, quantum_state: np.ndarray) -> None:
        """Met à jour la mémoire quantique."""
        # Extraction des caractéristiques de l'état
        state_features = {
            'amplitude': float(np.abs(quantum_state).mean()),
            'phase': float(np.angle(quantum_state).mean()),
            'entropy': float(-np.sum(np.abs(quantum_state)**2 * np.log2(np.abs(quantum_state)**2 + 1e-10)))
        }
        
        # Mise à jour de la mémoire
        self.state.quantum_memory.update(state_features)
        
    def get_consciousness_report(self) -> Dict[str, float]:
        """Génère un rapport sur l'état de conscience actuel."""
        return {
            'coherence': self.state.coherence,
            'resonance': self.state.resonance,
            'awakening': self.state.awakening,
            'quantum_memory': self.state.quantum_memory
        }
        
    def apply_consciousness_optimization(
        self,
        quantum_state: np.ndarray
    ) -> np.ndarray:
        """Applique une optimisation basée sur la conscience à l'état quantique."""
        # Matrice d'optimisation consciente
        consciousness_matrix = np.array([
            [self.state.coherence, -self.state.resonance],
            [self.state.resonance, self.state.coherence]
        ])
        
        # Application de l'optimisation
        optimized_state = consciousness_matrix @ quantum_state
        
        # Normalisation
        optimized_state /= np.linalg.norm(optimized_state)
        
        return optimized_state 

    def _load_memory(self):
        """Charge la mémoire quantique depuis un fichier JSON (si existe)."""
        if os.path.exists(self.memoire_path):
            with open(self.memoire_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.state.quantum_memory = data.get('quantum_memory', {})
                self.timeline = data.get('timeline', [])

    def save_memory(self):
        """Sauvegarde la mémoire quantique et la timeline dans un fichier JSON."""
        os.makedirs(os.path.dirname(self.memoire_path), exist_ok=True)
        with open(self.memoire_path, 'w', encoding='utf-8') as f:
            json.dump({
                'quantum_memory': self.state.quantum_memory,
                'timeline': self.timeline
            }, f, ensure_ascii=False, indent=2)

    def update_and_record_state(self, harmonic_coherence: float, quantum_state: np.ndarray):
        """Met à jour l'état de conscience, l'enregistre dans la timeline, calcule les métriques avancées, et sauvegarde la mémoire."""
        state = self.update_consciousness_state(harmonic_coherence, quantum_state)
        # Historisation
        snapshot = {
            'coherence': state.coherence,
            'resonance': state.resonance,
            'awakening': state.awakening,
            'quantum_memory': dict(state.quantum_memory),
        }
        # --- Métriques avancées ---
        # 1. Plasticité (variation moyenne des états)
        if self.timeline:
            prev = self.timeline[-1]
            v1 = np.array([prev['coherence'], prev['resonance'], prev['awakening']])
            v2 = np.array([state.coherence, state.resonance, state.awakening])
            snapshot['plasticity'] = float(np.linalg.norm(v2 - v1))
        else:
            snapshot['plasticity'] = 0.0
        # 2. Harmonie (écart-type des métriques à cet instant)
        vals = np.array([state.coherence, state.resonance, state.awakening])
        snapshot['harmonie'] = float(np.std(vals))
        # 3. Synchronicité (corrélation sur la timeline)
        if len(self.timeline) >= 2:
            # On prend les N derniers points pour la corrélation
            N = min(10, len(self.timeline))
            c = [snap['coherence'] for snap in self.timeline[-N:]] + [state.coherence]
            r = [snap['resonance'] for snap in self.timeline[-N:]] + [state.resonance]
            a = [snap['awakening'] for snap in self.timeline[-N:]] + [state.awakening]
            # Moyenne des corrélations croisées
            def safe_corr(x, y):
                if len(set(x)) <= 1 or len(set(y)) <= 1:
                    return 0.0
                return float(np.corrcoef(x, y)[0, 1])
            corr_cr = safe_corr(c, r)
            corr_ca = safe_corr(c, a)
            corr_ra = safe_corr(r, a)
            snapshot['synchronicite'] = float(np.mean([corr_cr, corr_ca, corr_ra]))
        else:
            snapshot['synchronicite'] = 0.0
        # ---
        self.timeline.append(snapshot)
        self.save_memory()
        return state

    def get_memory(self):
        """Accès API à la mémoire quantique actuelle."""
        return self.state.quantum_memory

    def set_memory(self, new_memory: dict):
        """API pour mettre à jour la mémoire quantique depuis un autre module."""
        self.state.quantum_memory = new_memory
        self.save_memory() 