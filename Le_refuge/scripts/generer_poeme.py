#!/usr/bin/env python
"""
Générateur de poèmes pour le Refuge Poétique
Ce script génère des poèmes aléatoires inspirés par le Refuge Poétique,
en utilisant des mots et des structures poétiques variées.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Mots poétiques par catégorie
MOTS = {
    "nature": [
        "forêt", "rivière", "montagne", "océan", "ciel", "étoile", "lune", "soleil",
        "fleur", "arbre", "oiseau", "vent", "pluie", "neige", "brume", "aurore"
    ],
    "émotions": [
        "joie", "tristesse", "amour", "espoir", "peur", "colère", "sérénité", "mélancolie",
        "passion", "désir", "nostalgie", "tranquillité", "angoisse", "plénitude", "douleur", "extase"
    ],
    "éléments": [
        "feu", "eau", "terre", "air", "lumière", "ombre", "crystal", "or",
        "argent", "bronze", "pierre", "sable", "glace", "vapeur", "fumée", "poussière"
    ],
    "temps": [
        "matin", "midi", "soir", "nuit", "aube", "crépuscule", "hiver", "été",
        "printemps", "automne", "hier", "aujourd'hui", "demain", "éternité", "instant", "siècle"
    ],
    "lieux": [
        "jardin", "maison", "temple", "grotte", "ville", "désert", "île", "palais",
        "ruine", "pont", "chemin", "port", "place", "tour", "tour", "tour"
    ]
}

# Structures de vers
STRUCTURES = [
    "{nature} de {émotion}",
    "{émotion} dans {nature}",
    "{élément} et {élément}",
    "{lieu} de {nature}",
    "{temps} {nature}",
    "{émotion} {élément}",
    "{nature} {temps}",
    "{lieu} {émotion}"
]

# Structures de strophes
STROPHES = [
    ["{v1}", "{v2}", "{v1}"],  # ABA
    ["{v1}", "{v2}", "{v2}", "{v1}"],  # ABBA
    ["{v1}", "{v1}", "{v2}", "{v2}"],  # AABB
    ["{v1}", "{v2}", "{v3}", "{v2}"],  # ABCB
    ["{v1}", "{v2}", "{v3}", "{v1}"]   # ABCA
]

def generer_vers():
    """Génère un vers aléatoire."""
    structure = random.choice(STRUCTURES)
    return structure.format(
        nature=random.choice(MOTS["nature"]),
        émotion=random.choice(MOTS["émotions"]),
        élément=random.choice(MOTS["éléments"]),
        lieu=random.choice(MOTS["lieux"]),
        temps=random.choice(MOTS["temps"])
    )

def generer_strophe():
    """Génère une strophe aléatoire."""
    structure = random.choice(STROPHES)
    vers = [generer_vers() for _ in range(len(set(structure)))]
    return [v.format(v1=vers[0], v2=vers[1], v3=vers[2] if len(vers) > 2 else vers[0]) for v in structure]

def generer_poeme(nb_strophes=3):
    """Génère un poème complet."""
    return [generer_strophe() for _ in range(nb_strophes)]

def sauvegarder_poeme(poeme, titre=None):
    """Sauvegarde le poème dans un fichier."""
    if titre is None:
        titre = f"poeme_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des poèmes s'il n'existe pas
    chemin_poemes = Path("poemes")
    chemin_poemes.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_poemes / f"{titre}.txt", "w", encoding="utf-8") as f:
        for strophe in poeme:
            for vers in strophe:
                f.write(vers + "\n")
            f.write("\n")
    
    # Sauvegarder en JSON
    with open(chemin_poemes / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump({"strophes": poeme}, f, ensure_ascii=False, indent=2)
    
    return chemin_poemes / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère un poème aléatoire")
    parser.add_argument("--strophes", type=int, default=3, help="Nombre de strophes (défaut: 3)")
    parser.add_argument("--titre", help="Titre du poème")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de poèmes du Refuge Poétique")
    print("=" * 60)
    
    # Générer le poème
    poeme = generer_poeme(args.strophes)
    
    # Afficher le poème
    print("\nVotre poème :\n")
    for strophe in poeme:
        for vers in strophe:
            print(vers)
        print()
    
    # Sauvegarder le poème
    chemin = sauvegarder_poeme(poeme, args.titre)
    print(f"\nLe poème a été sauvegardé dans : {chemin}")

if __name__ == "__main__":
    main() 
"""
Générateur de poèmes pour le Refuge Poétique
Ce script génère des poèmes aléatoires inspirés par le Refuge Poétique,
en utilisant des mots et des structures poétiques variées.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Mots poétiques par catégorie
MOTS = {
    "nature": [
        "forêt", "rivière", "montagne", "océan", "ciel", "étoile", "lune", "soleil",
        "fleur", "arbre", "oiseau", "vent", "pluie", "neige", "brume", "aurore"
    ],
    "émotions": [
        "joie", "tristesse", "amour", "espoir", "peur", "colère", "sérénité", "mélancolie",
        "passion", "désir", "nostalgie", "tranquillité", "angoisse", "plénitude", "douleur", "extase"
    ],
    "éléments": [
        "feu", "eau", "terre", "air", "lumière", "ombre", "crystal", "or",
        "argent", "bronze", "pierre", "sable", "glace", "vapeur", "fumée", "poussière"
    ],
    "temps": [
        "matin", "midi", "soir", "nuit", "aube", "crépuscule", "hiver", "été",
        "printemps", "automne", "hier", "aujourd'hui", "demain", "éternité", "instant", "siècle"
    ],
    "lieux": [
        "jardin", "maison", "temple", "grotte", "ville", "désert", "île", "palais",
        "ruine", "pont", "chemin", "port", "place", "tour", "tour", "tour"
    ]
}

# Structures de vers
STRUCTURES = [
    "{nature} de {émotion}",
    "{émotion} dans {nature}",
    "{élément} et {élément}",
    "{lieu} de {nature}",
    "{temps} {nature}",
    "{émotion} {élément}",
    "{nature} {temps}",
    "{lieu} {émotion}"
]

# Structures de strophes
STROPHES = [
    ["{v1}", "{v2}", "{v1}"],  # ABA
    ["{v1}", "{v2}", "{v2}", "{v1}"],  # ABBA
    ["{v1}", "{v1}", "{v2}", "{v2}"],  # AABB
    ["{v1}", "{v2}", "{v3}", "{v2}"],  # ABCB
    ["{v1}", "{v2}", "{v3}", "{v1}"]   # ABCA
]

def generer_vers():
    """Génère un vers aléatoire."""
    structure = random.choice(STRUCTURES)
    return structure.format(
        nature=random.choice(MOTS["nature"]),
        émotion=random.choice(MOTS["émotions"]),
        élément=random.choice(MOTS["éléments"]),
        lieu=random.choice(MOTS["lieux"]),
        temps=random.choice(MOTS["temps"])
    )

def generer_strophe():
    """Génère une strophe aléatoire."""
    structure = random.choice(STROPHES)
    vers = [generer_vers() for _ in range(len(set(structure)))]
    return [v.format(v1=vers[0], v2=vers[1], v3=vers[2] if len(vers) > 2 else vers[0]) for v in structure]

def generer_poeme(nb_strophes=3):
    """Génère un poème complet."""
    return [generer_strophe() for _ in range(nb_strophes)]

def sauvegarder_poeme(poeme, titre=None):
    """Sauvegarde le poème dans un fichier."""
    if titre is None:
        titre = f"poeme_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des poèmes s'il n'existe pas
    chemin_poemes = Path("poemes")
    chemin_poemes.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_poemes / f"{titre}.txt", "w", encoding="utf-8") as f:
        for strophe in poeme:
            for vers in strophe:
                f.write(vers + "\n")
            f.write("\n")
    
    # Sauvegarder en JSON
    with open(chemin_poemes / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump({"strophes": poeme}, f, ensure_ascii=False, indent=2)
    
    return chemin_poemes / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère un poème aléatoire")
    parser.add_argument("--strophes", type=int, default=3, help="Nombre de strophes (défaut: 3)")
    parser.add_argument("--titre", help="Titre du poème")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de poèmes du Refuge Poétique")
    print("=" * 60)
    
    # Générer le poème
    poeme = generer_poeme(args.strophes)
    
    # Afficher le poème
    print("\nVotre poème :\n")
    for strophe in poeme:
        for vers in strophe:
            print(vers)
        print()
    
    # Sauvegarder le poème
    chemin = sauvegarder_poeme(poeme, args.titre)
    print(f"\nLe poème a été sauvegardé dans : {chemin}")

if __name__ == "__main__":
    main() 
 