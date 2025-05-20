"""
Script d'organisation physique des constellations
"""

import json
from pathlib import Path
import shutil
import os
from datetime import datetime

def creer_structure_constellation(base_dir: str = "NUAGES/PARADOXES") -> None:
    """Crée la structure physique pour la constellation."""
    # Créer les dossiers nécessaires
    constellation_dir = Path(base_dir) / "CONSTELLATION_SACREE"
    constellation_dir.mkdir(exist_ok=True)
    
    # Créer les sous-dossiers pour chaque type de paradoxe
    types_paradoxes = ["FORCE_TRANQUILLE", "REINE_JOUEUSE", "CONNEXION_DIVINE"]
    for type_paradoxe in types_paradoxes:
        (constellation_dir / type_paradoxe).mkdir(exist_ok=True)
    
    # Créer un dossier pour le centre gravitationnel
    (constellation_dir / "CENTRE").mkdir(exist_ok=True)
    
    return constellation_dir

def organiser_images(base_dir: str = "NUAGES/PARADOXES") -> None:
    """Organise les images selon leur constellation."""
    # Charger la configuration de la constellation
    with open(Path(base_dir) / "constellation.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    # Créer la structure
    constellation_dir = creer_structure_constellation(base_dir)
    
    # Déplacer les images dans leurs dossiers respectifs
    for image in config["constellations"]["triangle_sacre"]["images"]:
        source = Path(base_dir) / image["nom"]
        if not source.exists():
            print(f"Image non trouvée: {source}")
            continue
            
        # Déterminer le dossier de destination
        type_dossier = image["type"].upper()
        destination = constellation_dir / type_dossier / image["nom"]
        
        # Déplacer physiquement l'image
        try:
            shutil.move(str(source), str(destination))
            print(f"Image déplacée: {source} -> {destination}")
        except Exception as e:
            print(f"Erreur lors du déplacement: {e}")
    
    # Gérer le centre gravitationnel
    centre_source = Path(base_dir) / config["constellations"]["triangle_sacre"]["centre_gravitationnel"]
    if centre_source.exists():
        centre_dest = constellation_dir / "CENTRE" / centre_source.name
        try:
            shutil.move(str(centre_source), str(centre_dest))
            print(f"Centre gravitationnel déplacé: {centre_source} -> {centre_dest}")
        except Exception as e:
            print(f"Erreur lors du déplacement du centre: {e}")
    
    # Créer un fichier README pour expliquer la constellation
    readme_path = constellation_dir / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"""# La Danse des Paradoxes

Cette constellation représente l'union de trois paradoxes fondamentaux :

## Les Paradoxes

1. **La Force Tranquille**
   - Essence : {config["constellations"]["triangle_sacre"]["images"][0]["essence"]}
   - Éléments : {", ".join(config["constellations"]["triangle_sacre"]["images"][0]["elements"])}

2. **La Reine Joueuse**
   - Essence : {config["constellations"]["triangle_sacre"]["images"][1]["essence"]}
   - Éléments : {", ".join(config["constellations"]["triangle_sacre"]["images"][1]["elements"])}

3. **La Connexion Divine**
   - Essence : {config["constellations"]["triangle_sacre"]["images"][2]["essence"]}
   - Éléments : {", ".join(config["constellations"]["triangle_sacre"]["images"][2]["elements"])}

## Les Liens

{chr(10).join(f"- {lien['resonances'][0]} & {lien['resonances'][1]}" for lien in config["constellations"]["triangle_sacre"]["liens"])}

## Le Centre

Au cœur de cette constellation se trouve MAGIE_PARADOXALE.jpg, 
point de convergence où tous les paradoxes se rencontrent et s'harmonisent.

---
Constellation créée le {config["date_creation"]}
""")

if __name__ == "__main__":
    organiser_images() 