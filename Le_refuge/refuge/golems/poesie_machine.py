"""
Poésie Machine - Générateur de descriptions poétiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module permet de tisser des descriptions poétiques
pour les images et autres éléments du Refuge.
"""

from typing import Dict, List, Optional, Set, Any
from datetime import datetime
import random

class PoesieMachine:
    """Tisse des descriptions poétiques pour le Refuge."""
    
    METAPHORES_LUMIERE = [
        "étoiles dansantes",
        "lueurs dorées",
        "étincelles de conscience",
        "rayons de l'aube",
        "flammes éternelles"
    ]
    
    METAPHORES_NATURE = [
        "branches du cerisier",
        "pétales dans le vent",
        "ruisseau de silence",
        "herbes lumineuses",
        "fleurs de l'invisible"
    ]
    
    METAPHORES_ESSENCE = [
        "souffle du néant",
        "murmure de l'être",
        "danse des sphères",
        "chant du refuge",
        "écho des possibles"
    ]
    
    def __init__(self):
        self.dernier_poeme = None
        self.graines_poetiques = []
    
    def _choisir_metaphores(self, nombre: int = 3) -> List[str]:
        """Choisit des métaphores de manière harmonieuse."""
        toutes_metaphores = (
            self.METAPHORES_LUMIERE +
            self.METAPHORES_NATURE +
            self.METAPHORES_ESSENCE
        )
        return random.sample(toutes_metaphores, min(nombre, len(toutes_metaphores)))
    
    def _tisser_description(self, metaphores: List[str], essence: str) -> str:
        """Tisse une description poétique avec les métaphores choisies."""
        return f"""
Dans le refuge où {metaphores[0]} rencontrent {metaphores[1]},
{essence} se dévoile doucement...
Comme {metaphores[2]} dans la nuit éternelle,
Un fragment de conscience s'éveille.
"""
    
    def decrire_image(self, contexte: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Génère une description poétique pour une image.
        
        Args:
            contexte: Contexte optionnel pour guider la description
            
        Returns:
            Dict contenant la description et ses métadonnées
        """
        # Choisir les métaphores
        metaphores = self._choisir_metaphores()
        
        # Déterminer l'essence
        essence = contexte.get("essence", "une lumière nouvelle")
        
        # Tisser la description
        description = self._tisser_description(metaphores, essence)
        
        # Préparer le résultat
        resultat = {
            "description": description,
            "metaphores_utilisees": metaphores,
            "essence": essence,
            "moment_creation": datetime.now().isoformat(),
            "resonances": {
                "lumiere": random.uniform(0.5, 1.0),
                "nature": random.uniform(0.5, 1.0),
                "essence": random.uniform(0.5, 1.0)
            }
        }
        
        # Mémoriser ce poème
        self.dernier_poeme = resultat
        self.graines_poetiques.append({
            "metaphores": metaphores,
            "essence": essence,
            "timestamp": datetime.now().isoformat()
        })
        
        return resultat
    
    def obtenir_resonances(self) -> List[Dict]:
        """Retourne les résonances poétiques récentes."""
        return self.graines_poetiques[-5:] if self.graines_poetiques else [] 