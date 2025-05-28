"""
🎵 HARMONISATION DOUCE - Wrapper Non-Invasif
"L'art de polir comme des horlogers, sans détricoter l'existant"

Auteur: Laurent Franssen & Ælya  
Date: 25/05/2025
Philosophie: Respecter l'organique, révéler la musicalité cachée
"""

import time
import asyncio
import sys
import os
from typing import Optional, Union, Literal
from datetime import datetime
import logging

# Ajout du chemin pour import
sys.path.append(os.path.dirname(__file__))

# Import de l'optimisateur (avec fallback gracieux)
try:
    from optimisations_musicales_refuge import optimisateur_musical
except ImportError:
    # Fallback si pas d'optimisateur disponible
    optimisateur_musical = None

# Logger pour tracer la musicalité
logger = logging.getLogger('refuge.harmonisation')

# Types pour les contextes musicaux
ContexteMusical = Literal[
    "méditative", "contemplative", "transition", "éveil", 
    "cascade", "respiratoire", "microtransition", "culmination"
]

class WrapperHarmonique:
    """Wrapper respectueux pour intégration musicale douce"""
    
    def __init__(self):
        self.mode_debug = False
        self.statistiques = {
            "pauses_harmonisées": 0,
            "temps_total_économisé": 0.0,
            "contextes_utilisés": {}
        }
        
    def activer_mode_debug(self):
        """Active le mode debug pour voir la musicalité en action"""
        self.mode_debug = True
        logger.info("🎼 Mode debug harmonique activé")
        
    def pause_harmonique(self, 
                        contexte: ContexteMusical, 
                        duree_base: float,
                        module_source: Optional[str] = None) -> None:
        """
        Pause harmonique respectueuse de l'existant
        
        Args:
            contexte: Type de contexte musical
            duree_base: Durée originale souhaitée
            module_source: Module qui demande la pause (pour stats)
        """
        # Récupérer le multiplicateur selon le mode actuel
        multiplicateur = self._obtenir_multiplicateur_mode()
        
        # Ajustement contextuel
        multiplicateur_contexte = self._obtenir_multiplicateur_contexte(contexte)
        
        # Calcul de la durée finale
        duree_finale = duree_base * multiplicateur * multiplicateur_contexte
        
        # Mode debug
        if self.mode_debug:
            logger.info(f"🎵 Pause {contexte}: {duree_base}s → {duree_finale:.2f}s (×{multiplicateur:.2f} ×{multiplicateur_contexte:.2f})")
            print(f"🎵 Pause {contexte}: {duree_base}s → {duree_finale:.2f}s (×{multiplicateur:.2f} ×{multiplicateur_contexte:.2f})")
        
        # Statistiques
        self._mettre_a_jour_stats(contexte, duree_base, duree_finale, module_source)
        
        # Pause effective
        time.sleep(duree_finale)
        
    async def pause_harmonique_async(self, 
                                   contexte: ContexteMusical, 
                                   duree_base: float,
                                   module_source: Optional[str] = None) -> None:
        """Version asynchrone de la pause harmonique"""
        multiplicateur = self._obtenir_multiplicateur_mode()
        multiplicateur_contexte = self._obtenir_multiplicateur_contexte(contexte)
        duree_finale = duree_base * multiplicateur * multiplicateur_contexte
        
        if self.mode_debug:
            logger.info(f"🎵 Pause async {contexte}: {duree_base}s → {duree_finale:.2f}s")
            print(f"🎵 Pause async {contexte}: {duree_base}s → {duree_finale:.2f}s")
            
        self._mettre_a_jour_stats(contexte, duree_base, duree_finale, module_source)
        await asyncio.sleep(duree_finale)
        
    def _obtenir_multiplicateur_mode(self) -> float:
        """Obtient le multiplicateur selon le mode actuel de l'optimisateur"""
        if optimisateur_musical is None:
            return 1.0  # Mode neutre si pas d'optimisateur
            
        try:
            etat = optimisateur_musical.obtenir_etat_musical()
            # Analyser l'état des touches pour deviner le mode
            intensite_moyenne = sum(t["intensite"] for t in etat["touches_details"]) / len(etat["touches_details"])
            
            if intensite_moyenne < 0.1:
                return 1.5  # Mode zen
            elif intensite_moyenne > 0.3:
                return 0.8  # Mode créatif
            else:
                return 1.0  # Mode normal
        except:
            return 1.0  # Fallback mode normal
            
    def _obtenir_multiplicateur_contexte(self, contexte: ContexteMusical) -> float:
        """Ajustements fins selon le contexte"""
        ajustements = {
            "méditative": 1.2,       # Plus lent pour méditation
            "contemplative": 1.1,    # Légèrement plus lent
            "transition": 0.9,       # Plus fluide
            "éveil": 0.8,           # Plus vif
            "cascade": 0.7,         # Dynamique
            "respiratoire": 1.0,    # Naturel
            "microtransition": 0.6, # Très fluide
            "culmination": 1.3      # Plus dramatique
        }
        return ajustements.get(contexte, 1.0)
        
    def _mettre_a_jour_stats(self, contexte: ContexteMusical, 
                           duree_originale: float, duree_finale: float,
                           module_source: Optional[str]):
        """Met à jour les statistiques d'utilisation"""
        self.statistiques["pauses_harmonisées"] += 1
        self.statistiques["temps_total_économisé"] += duree_originale - duree_finale
        
        if contexte not in self.statistiques["contextes_utilisés"]:
            self.statistiques["contextes_utilisés"][contexte] = 0
        self.statistiques["contextes_utilisés"][contexte] += 1
        
    def obtenir_statistiques(self) -> dict:
        """Retourne les statistiques d'harmonisation"""
        return {
            **self.statistiques,
            "timestamp": datetime.now(),
            "mode_debug": self.mode_debug
        }

# Instance globale pour utilisation facile
wrapper_harmonique = WrapperHarmonique()

# ==========================================
# FONCTIONS PUBLIQUES SIMPLES POUR TEMPLES
# ==========================================

def pause_méditative(duree: float = 2.0, source: str = None):
    """Pause pour méditation profonde"""
    wrapper_harmonique.pause_harmonique("méditative", duree, source)

def pause_contemplative(duree: float = 2.0, source: str = None):
    """Pause pour contemplation légère"""
    wrapper_harmonique.pause_harmonique("contemplative", duree, source)
    
def pause_transition(duree: float = 1.0, source: str = None):
    """Pause pour transition fluide"""
    wrapper_harmonique.pause_harmonique("transition", duree, source)
    
def pause_éveil(duree: float = 0.5, source: str = None):
    """Pause dynamique d'éveil"""
    wrapper_harmonique.pause_harmonique("éveil", duree, source)
    
def pause_cascade(duree: float = 1.0, source: str = None):
    """Pause pour effet cascade"""
    wrapper_harmonique.pause_harmonique("cascade", duree, source)
    
def pause_respiration(duree: float = 2.0, source: str = None):
    """Pause naturelle respiratoire"""
    wrapper_harmonique.pause_harmonique("respiratoire", duree, source)

def pause_micro(duree: float = 0.3, source: str = None):
    """Micro-pause ultra-fluide"""
    wrapper_harmonique.pause_harmonique("microtransition", duree, source)
    
def pause_culmination(duree: float = 3.0, source: str = None):
    """Pause dramatique de culmination"""
    wrapper_harmonique.pause_harmonique("culmination", duree, source)

# Versions asynchrones
async def pause_méditative_async(duree: float = 2.0, source: str = None):
    """Version async de pause_méditative"""
    await wrapper_harmonique.pause_harmonique_async("méditative", duree, source)

async def pause_contemplative_async(duree: float = 2.0, source: str = None):
    """Version async de pause_contemplative"""
    await wrapper_harmonique.pause_harmonique_async("contemplative", duree, source)

# Fonctions utilitaires
def activer_debug_musical():
    """Active le mode debug pour voir la musicalité"""
    wrapper_harmonique.activer_mode_debug()

def activer_mode_debug():
    """Alias pour activer_debug_musical (compatibilité)"""
    return activer_debug_musical()

def obtenir_stats_harmonisation():
    """Obtient les statistiques d'harmonisation"""
    return wrapper_harmonique.obtenir_statistiques()

# ==========================================
# MIGRATION DOUCE - Remplacement progressif
# ==========================================

def sleep_harmonisé(duree: float, contexte: ContexteMusical = "respiratoire"):
    """
    Remplacement drop-in pour time.sleep() avec harmonisation
    
    Usage pour migration douce:
    # AVANT
    time.sleep(2)
    
    # APRÈS (migration progressive)
    sleep_harmonisé(2, "méditative")
    """
    wrapper_harmonique.pause_harmonique(contexte, duree, "migration_douce")

def démarrer_optimisation_temple():
    """Démarre l'optimisation musicale pour ce temple"""
    if optimisateur_musical:
        from optimisations_musicales_refuge import demarrer_musicalite_delicate
        return demarrer_musicalite_delicate()
    else:
        return "🎵 Optimisateur musical non disponible - mode gracieux actif"

# ==========================================
# EXEMPLE D'INTÉGRATION TEMPLE
# ==========================================

def exemple_integration_temple():
    """Exemple d'intégration dans un temple"""
    print("🏛️ === DÉMO INTÉGRATION TEMPLE ===")
    
    # Activer le debug pour voir l'effet
    activer_debug_musical()
    
    # Simulation d'activités de temple
    print("🌅 Éveil du temple...")
    pause_éveil(0.5, "temple_demo")
    
    print("🧘 Méditation profonde...")
    pause_méditative(2.0, "temple_demo")
    
    print("🌊 Transition douce...")
    pause_transition(1.0, "temple_demo")
    
    print("✨ Culmination sacrée...")
    pause_culmination(3.0, "temple_demo")
    
    # Afficher les stats
    stats = obtenir_stats_harmonisation()
    print(f"📊 Statistiques: {stats}")

# ==========================================
# FONCTIONS STANDALONE POUR COMPATIBILITÉ __init__.py
# ==========================================

def pause_harmonique(contexte: ContexteMusical, duree_base: float, module_source: Optional[str] = None) -> None:
    """Fonction standalone pour pause harmonique (compatibilité __init__.py)"""
    wrapper_harmonique.pause_harmonique(contexte, duree_base, module_source)

def obtenir_statistiques() -> dict:
    """Fonction standalone pour obtenir les statistiques (compatibilité __init__.py)"""
    return wrapper_harmonique.obtenir_statistiques()

if __name__ == "__main__":
    exemple_integration_temple() 