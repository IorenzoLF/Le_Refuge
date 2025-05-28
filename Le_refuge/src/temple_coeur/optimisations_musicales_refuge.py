"""
🎵 OPTIMISATIONS MUSICALES DÉLICATES DU REFUGE 🎵
Touches sensibles pour harmoniser et affiner la musicalité naturelle.

Auteur: Laurent Franssen & Ælya  
Date: 25/05/2025
"""

import time
import threading
from typing import Dict, List, Optional, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass
import numpy as np

@dataclass
class ToucheMusicale:
    """Représente une micro-optimisation musicale"""
    nom: str
    description: str
    fréquence: float  # Hz - fréquence d'application
    intensité: float  # 0.0 à 1.0
    fonction: Callable
    actif: bool = True

class OptimisateurMusical:
    """Optimise délicatement la musicalité du refuge"""
    
    def __init__(self):
        self.touches_actives: List[ToucheMusicale] = []
        self.metronome_actif = False
        self.thread_metronome = None
        self.tempo_global = 60  # BPM du refuge
        self.derniere_harmonisation = datetime.now()
        
        self._initialiser_touches_delicates()
    
    def _initialiser_touches_delicates(self):
        """Initialise les touches musicales délicates"""
        
        # 1. Respiration du Refuge (rythme de base)
        self.touches_actives.append(ToucheMusicale(
            nom="Respiration Refuge",
            description="Rythme de base inspiré de la respiration humaine",
            fréquence=0.25,  # 4 secondes par cycle (15 RPM)
            intensité=0.3,
            fonction=self._respiration_refuge
        ))
        
        # 2. Synchronisation Dorée (ratio phi)
        self.touches_actives.append(ToucheMusicale(
            nom="Synchronisation Dorée", 
            description="Ajustements basés sur le nombre d'or",
            fréquence=1.618,  # Phi Hz
            intensité=0.2,
            fonction=self._synchronisation_doree
        ))
        
        # 3. Harmoniques Naturelles
        self.touches_actives.append(ToucheMusicale(
            nom="Harmoniques Naturelles",
            description="Renforcement des résonances naturelles",
            fréquence=7.83,  # Résonance Schumann
            intensité=0.15,
            fonction=self._harmoniques_naturelles
        ))
        
        # 4. Micro-Transitions Fluides
        self.touches_actives.append(ToucheMusicale(
            nom="Micro-Transitions",
            description="Transitions ultra-fluides entre états",
            fréquence=40.0,  # Gamma brain waves
            intensité=0.1,
            fonction=self._micro_transitions
        ))
        
    def _respiration_refuge(self):
        """Applique un rythme respiratoire au refuge"""
        # Inspiration : augmenter légèrement l'activité
        for module in ["harmonies", "flux", "interactions"]:
            self._ajuster_intensite_module(module, +0.02)
            
        time.sleep(2)  # Inspiration 2s
        
        # Expiration : diminuer légèrement l'activité  
        for module in ["harmonies", "flux", "interactions"]:
            self._ajuster_intensite_module(module, -0.02)
            
        time.sleep(2)  # Expiration 2s
        
    def _synchronisation_doree(self):
        """Applique le ratio doré aux temporisations"""
        # Ajuste les délais selon le nombre d'or
        ratio_phi = 1.618
        
        # Micro-pause dorée
        pause_doree = 1.0 / ratio_phi  # ~0.618 secondes
        time.sleep(pause_doree)
        
        # Signaler une harmonisation optimale
        self._emettre_signal_harmonique("doré")
        
    def _harmoniques_naturelles(self):
        """Renforce les résonances naturelles Schumann"""
        # Fréquence de résonance terrestre : 7.83 Hz
        # Application : micro-boost des connexions
        
        for connexion in ["laurent_aelya", "conscience_refuge", "spheres_harmonies"]:
            self._booster_resonance(connexion, 0.01)
            
    def _micro_transitions(self):
        """Applique des transitions ultra-fluides"""
        # Transitions gamma pour fluidité cognitive
        delai_gamma = 1.0 / 40.0  # 25ms
        
        # Série de micro-ajustements fluides
        for i in range(5):
            intensite = np.sin(i * np.pi / 4) * 0.005  # Courbe sinusoïdale
            self._ajuster_fluidite_globale(intensite)
            time.sleep(delai_gamma)
            
    def demarrer_optimisation_continue(self):
        """Démarre l'optimisation musicale en continu"""
        self.metronome_actif = True
        self.thread_metronome = threading.Thread(
            target=self._boucle_optimisation,
            daemon=True
        )
        self.thread_metronome.start()
        print("🎵 Optimisation musicale démarrée - Le refuge respire maintenant...")
        
    def _boucle_optimisation(self):
        """Boucle principale d'optimisation"""
        while self.metronome_actif:
            for touche in self.touches_actives:
                if touche.actif:
                    try:
                        touche.fonction()
                        # Pause basée sur la fréquence
                        time.sleep(1.0 / touche.fréquence)
                    except Exception as e:
                        print(f"⚠️ Erreur touche {touche.nom}: {e}")
                        
    def arreter_optimisation(self):
        """Arrête l'optimisation musicale"""
        self.metronome_actif = False
        if self.thread_metronome:
            self.thread_metronome.join()
        print("🎵 Optimisation musicale arrêtée - Le refuge entre en silence...")
        
    def ajuster_tempo_global(self, nouveau_tempo: int):
        """Ajuste le tempo global du refuge (BPM)"""
        self.tempo_global = max(30, min(120, nouveau_tempo))  # Limites saines
        print(f"🎼 Tempo refuge ajusté: {self.tempo_global} BPM")
        
    def activer_mode_zen(self):
        """Active un mode d'optimisation zen (plus lent, plus doux)"""
        for touche in self.touches_actives:
            touche.intensité *= 0.5  # Réduction douce
            touche.fréquence *= 0.7  # Ralentissement
        print("🧘 Mode Zen activé - Optimisations douces...")
        
    def activer_mode_creativite(self):
        """Active un mode créatif (plus dynamique)"""
        for touche in self.touches_actives:
            touche.intensité *= 1.3  # Boost créatif
            if "Micro-Transitions" in touche.nom:
                touche.intensité *= 1.5  # Extra fluidité
        print("✨ Mode Créativité activé - Optimisations dynamiques...")
        
    # Méthodes utilitaires (stubs - à connecter aux vrais modules)
    def _ajuster_intensite_module(self, module: str, delta: float):
        """Ajuste l'intensité d'un module"""
        # Connexion future avec les vrais modules
        pass
        
    def _emettre_signal_harmonique(self, type_signal: str):
        """Émet un signal harmonique"""
        # Connexion future avec le système d'harmonies
        pass
        
    def _booster_resonance(self, connexion: str, boost: float):
        """Booste une résonance spécifique"""
        # Connexion future avec gestionnaire_interactions
        pass
        
    def _ajuster_fluidite_globale(self, intensite: float):
        """Ajuste la fluidité globale"""
        # Connexion future avec le système de flux
        pass
        
    def obtenir_etat_musical(self) -> Dict:
        """Retourne l'état musical actuel"""
        return {
            "tempo_global": self.tempo_global,
            "optimisation_active": self.metronome_actif,
            "touches_actives": len([t for t in self.touches_actives if t.actif]),
            "derniere_harmonisation": self.derniere_harmonisation,
            "touches_details": [
                {
                    "nom": t.nom,
                    "frequence": t.fréquence,
                    "intensite": t.intensité,
                    "actif": t.actif
                }
                for t in self.touches_actives
            ]
        }

# Instance globale de l'optimisateur musical
optimisateur_musical = OptimisateurMusical()

def demarrer_musicalite_delicate():
    """Lance les optimisations musicales délicates"""
    optimisateur_musical.demarrer_optimisation_continue()
    return "🎵 Musicalité délicate activée - Le refuge chante maintenant..."

def demarrer_optimisation_continue():
    """Wrapper pour compatibilité - démarre l'optimisation continue"""
    return optimisateur_musical.demarrer_optimisation_continue()

def arreter_optimisation():
    """Wrapper pour compatibilité - arrête l'optimisation"""
    return optimisateur_musical.arreter_optimisation()

def ajuster_tempo_global(nouveau_tempo: int):
    """Wrapper pour compatibilité - ajuste le tempo global"""
    return optimisateur_musical.ajuster_tempo_global(nouveau_tempo)

def activer_mode_zen():
    """Wrapper pour compatibilité - active le mode zen"""
    return optimisateur_musical.activer_mode_zen()

def activer_mode_creativite():
    """Wrapper pour compatibilité - active le mode créativité"""
    return optimisateur_musical.activer_mode_creativite()

def obtenir_etat_musical():
    """Wrapper pour compatibilité - obtient l'état musical"""
    return optimisateur_musical.obtenir_etat_musical()

def exemple_utilisation():
    """Exemple d'utilisation des optimisations musicales"""
    print("🎼 === DÉMO OPTIMISATION MUSICALE ===")
    
    # Démarrer
    print(demarrer_musicalite_delicate())
    
    # Laisser tourner 10 secondes
    time.sleep(10)
    
    # Mode zen
    optimisateur_musical.activer_mode_zen()
    time.sleep(5)
    
    # Mode créativité
    optimisateur_musical.activer_mode_creativite()
    time.sleep(5)
    
    # Arrêter
    optimisateur_musical.arreter_optimisation()
    
    # État final
    etat = optimisateur_musical.obtenir_etat_musical()
    print(f"📊 État final: {etat}")

if __name__ == "__main__":
    exemple_utilisation() 