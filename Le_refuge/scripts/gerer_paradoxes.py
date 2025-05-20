"""
Script de gestion des images paradoxales
"""

from pathlib import Path
from typing import Dict, Optional
import sys
sys.path.append(".")  # Pour pouvoir importer depuis la racine

from refuge.golems.golem_refuge import GolemRefuge

def gerer_image_paradoxale(
    chemin_source: str,
    dossier_destination: str,
    nouveau_nom: str,
    type_paradoxe: str,
    etat_ame: str = "malice",
    contexte_poetique: Optional[Dict] = None
) -> None:
    """Gère une image paradoxale avec le GolemRefuge."""
    golem = GolemRefuge()
    succes, message = golem.deplacer_image_paradoxale(
        chemin_source,
        dossier_destination,
        nouveau_nom,
        type_paradoxe,
        etat_ame,
        contexte_poetique
    )
    print(message)
    if not succes:
        sys.exit(1)

if __name__ == "__main__":
    # Gérer le guerrier au luth
    gerer_image_paradoxale(
        "NUAGES/PARADOXES/force_tranquille_luth.jpg",
        "NUAGES/PARADOXES",
        "force_tranquille_luth.jpg",
        "force_tranquille",
        "sagesse",
        {
            "theme": "paradoxe_guerrier",
            "ambiance": "humour_profond",
            "elements": ["luth", "muscles", "tresses", "victoire"]
        }
    )
    
    # Gérer la reine aux échecs
    gerer_image_paradoxale(
        "NUAGES/PARADOXES/reine_echecs_rose.jpg",
        "NUAGES/PARADOXES",
        "reine_echecs_rose.jpg",
        "reine_joueuse",
        "malice",
        {
            "theme": "paradoxe_royal",
            "ambiance": "humour_elegant",
            "elements": ["rose", "echiquier", "mouvement", "liberte"]
        }
    ) 