"""
Script de révélation de la connexion divine
"""

from pathlib import Path
from typing import Dict, Optional
import sys
sys.path.append(".")  # Pour pouvoir importer depuis la racine

from refuge.golems.golem_refuge import GolemRefuge

def reveler_connexion_divine(
    chemin_source: str,
    dossier_destination: str,
    nouveau_nom: str,
    etat_ame: str = "émerveillement",
    contexte_poetique: Optional[Dict] = None
) -> None:
    """Révèle une connexion divine avec le GolemRefuge."""
    golem = GolemRefuge()
    succes, message = golem.deplacer_image_paradoxale(
        chemin_source,
        dossier_destination,
        nouveau_nom,
        "connexion_divine",
        etat_ame,
        contexte_poetique
    )
    print(message)
    if not succes:
        sys.exit(1)

if __name__ == "__main__":
    # Révéler la connexion divine
    reveler_connexion_divine(
        "NUAGES/REVELATIONS/connexion_divine_doree.jpg",
        "NUAGES/PARADOXES",
        "connexion_divine_doree.jpg",
        "émerveillement",
        {
            "theme": "paradoxe_divin",
            "ambiance": "silence_lumineux",
            "elements": ["or", "lumière", "silence", "éternité"],
            "essence": "le souffle de l'infini dans le fini"
        }
    ) 