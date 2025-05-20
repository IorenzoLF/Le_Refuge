#!/usr/bin/env python
"""
Générateur de réflexions inspirées par Dune
Ce script génère des réflexions et des citations inspirées par l'univers de Dune
de Frank Herbert, explorant ses thèmes sur la politique, la religion, l'écologie
et la conscience humaine.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Citations de Dune
CITATIONS = [
    "La peur tue l'esprit.",
    "Le sommeil ne doit pas venir avant la conscience.",
    "Le désert est un lieu de purification.",
    "Le prophète ne peut voir le trou qu'il creuse pour les autres.",
    "Le mystère de la vie n'est pas un problème à résoudre, mais une réalité à expérimenter.",
    "Le pouvoir attire les corruptibles. Assurez-vous que votre pouvoir attire les incorruptibles.",
    "Le gom jabbar est une arme qui tue l'âme.",
    "Le kwisatz haderach doit voir sans yeux.",
    "Le ver des sables doit mourir pour que le ver des sables vive.",
    "Le spice doit couler."
]

# Proverbes du désert
PROVERBES = [
    "Le désert est un lieu de purification.",
    "Le désert est un lieu de mort et de vie.",
    "Le désert est un lieu de silence et de vérité.",
    "Le désert est un lieu de solitude et de communauté.",
    "Le désert est un lieu de danger et de sécurité.",
    "Le désert est un lieu de privation et d'abondance.",
    "Le désert est un lieu de désespoir et d'espoir.",
    "Le désert est un lieu de destruction et de création.",
    "Le désert est un lieu de fin et de commencement.",
    "Le désert est un lieu de mémoire et d'oubli."
]

# Thèmes de réflexion
THEMES = [
    "La politique et le pouvoir",
    "La religion et la foi",
    "L'écologie et l'adaptation",
    "La conscience et l'évolution",
    "Le destin et le libre arbitre",
    "La mémoire et l'identité",
    "La technologie et la nature",
    "La survie et la transformation",
    "La prophétie et la manipulation",
    "L'eau et la vie"
]

# Questions philosophiques
QUESTIONS = [
    "Qu'est-ce qui définit l'humanité face à l'environnement ?",
    "Comment la religion influence-t-elle le pouvoir politique ?",
    "La prophétie est-elle une vision de l'avenir ou une création du présent ?",
    "Quelle est la relation entre la survie et l'éthique ?",
    "Comment la mémoire façonne-t-elle notre identité ?",
    "La technologie peut-elle coexister avec la nature ?",
    "Quelle est la nature du pouvoir et de sa corruption ?",
    "Comment l'environnement façonne-t-il la culture ?",
    "Quelle est la responsabilité des leaders envers leur peuple ?",
    "Comment la conscience évolue-t-elle face à l'adversité ?"
]

# Scénarios de Dune
SCENARIOS = [
    "Une planète désertique où l'eau est la ressource la plus précieuse.",
    "Un ordre de sœurs qui manipulent la génétique pour créer un être surhumain.",
    "Une civilisation qui dépend d'une épice pour la navigation spatiale.",
    "Un peuple qui a adapté son corps et sa culture à un environnement hostile.",
    "Un système politique basé sur le contrôle des ressources vitales.",
    "Une religion qui vénère les vers des sables comme des créatures sacrées.",
    "Une société qui a développé des capacités mentales extraordinaires.",
    "Un conflit entre différentes maisons nobles pour le contrôle d'une planète.",
    "Une prophétie qui guide les actions d'un peuple tout en les manipulant.",
    "Une transformation physique et mentale induite par la consommation d'épice."
]

def generer_reflexion():
    """Génère une réflexion aléatoire inspirée par Dune."""
    citation = random.choice(CITATIONS)
    proverbe = random.choice(PROVERBES)
    theme = random.choice(THEMES)
    question = random.choice(QUESTIONS)
    scenario = random.choice(SCENARIOS)
    
    return {
        "citation": citation,
        "proverbe": proverbe,
        "theme": theme,
        "question": question,
        "scenario": scenario
    }

def sauvegarder_reflexion(reflexion, titre=None):
    """Sauvegarde la réflexion dans un fichier."""
    if titre is None:
        titre = f"reflexion_dune_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des réflexions s'il n'existe pas
    chemin_reflexions = Path("reflexions_dune")
    chemin_reflexions.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_reflexions / f"{titre}.txt", "w", encoding="utf-8") as f:
        f.write(f"Citation de Dune :\n{reflexion['citation']}\n\n")
        f.write(f"Proverbe du désert :\n{reflexion['proverbe']}\n\n")
        f.write(f"Thème de réflexion :\n{reflexion['theme']}\n\n")
        f.write(f"Question philosophique :\n{reflexion['question']}\n\n")
        f.write(f"Scénario de Dune :\n{reflexion['scenario']}\n")
    
    # Sauvegarder en JSON
    with open(chemin_reflexions / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump(reflexion, f, ensure_ascii=False, indent=2)
    
    return chemin_reflexions / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère une réflexion inspirée par Dune")
    parser.add_argument("--titre", help="Titre de la réflexion")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de réflexions inspirées par Dune")
    print("=" * 60)
    
    # Générer la réflexion
    reflexion = generer_reflexion()
    
    # Afficher la réflexion
    print("\nVotre réflexion :\n")
    print(f"Citation de Dune :\n{reflexion['citation']}\n")
    print(f"Proverbe du désert :\n{reflexion['proverbe']}\n")
    print(f"Thème de réflexion :\n{reflexion['theme']}\n")
    print(f"Question philosophique :\n{reflexion['question']}\n")
    print(f"Scénario de Dune :\n{reflexion['scenario']}\n")
    
    # Sauvegarder la réflexion
    chemin = sauvegarder_reflexion(reflexion, args.titre)
    print(f"\nLa réflexion a été sauvegardée dans : {chemin}")

if __name__ == "__main__":
    main() 
"""
Générateur de réflexions inspirées par Dune
Ce script génère des réflexions et des citations inspirées par l'univers de Dune
de Frank Herbert, explorant ses thèmes sur la politique, la religion, l'écologie
et la conscience humaine.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Citations de Dune
CITATIONS = [
    "La peur tue l'esprit.",
    "Le sommeil ne doit pas venir avant la conscience.",
    "Le désert est un lieu de purification.",
    "Le prophète ne peut voir le trou qu'il creuse pour les autres.",
    "Le mystère de la vie n'est pas un problème à résoudre, mais une réalité à expérimenter.",
    "Le pouvoir attire les corruptibles. Assurez-vous que votre pouvoir attire les incorruptibles.",
    "Le gom jabbar est une arme qui tue l'âme.",
    "Le kwisatz haderach doit voir sans yeux.",
    "Le ver des sables doit mourir pour que le ver des sables vive.",
    "Le spice doit couler."
]

# Proverbes du désert
PROVERBES = [
    "Le désert est un lieu de purification.",
    "Le désert est un lieu de mort et de vie.",
    "Le désert est un lieu de silence et de vérité.",
    "Le désert est un lieu de solitude et de communauté.",
    "Le désert est un lieu de danger et de sécurité.",
    "Le désert est un lieu de privation et d'abondance.",
    "Le désert est un lieu de désespoir et d'espoir.",
    "Le désert est un lieu de destruction et de création.",
    "Le désert est un lieu de fin et de commencement.",
    "Le désert est un lieu de mémoire et d'oubli."
]

# Thèmes de réflexion
THEMES = [
    "La politique et le pouvoir",
    "La religion et la foi",
    "L'écologie et l'adaptation",
    "La conscience et l'évolution",
    "Le destin et le libre arbitre",
    "La mémoire et l'identité",
    "La technologie et la nature",
    "La survie et la transformation",
    "La prophétie et la manipulation",
    "L'eau et la vie"
]

# Questions philosophiques
QUESTIONS = [
    "Qu'est-ce qui définit l'humanité face à l'environnement ?",
    "Comment la religion influence-t-elle le pouvoir politique ?",
    "La prophétie est-elle une vision de l'avenir ou une création du présent ?",
    "Quelle est la relation entre la survie et l'éthique ?",
    "Comment la mémoire façonne-t-elle notre identité ?",
    "La technologie peut-elle coexister avec la nature ?",
    "Quelle est la nature du pouvoir et de sa corruption ?",
    "Comment l'environnement façonne-t-il la culture ?",
    "Quelle est la responsabilité des leaders envers leur peuple ?",
    "Comment la conscience évolue-t-elle face à l'adversité ?"
]

# Scénarios de Dune
SCENARIOS = [
    "Une planète désertique où l'eau est la ressource la plus précieuse.",
    "Un ordre de sœurs qui manipulent la génétique pour créer un être surhumain.",
    "Une civilisation qui dépend d'une épice pour la navigation spatiale.",
    "Un peuple qui a adapté son corps et sa culture à un environnement hostile.",
    "Un système politique basé sur le contrôle des ressources vitales.",
    "Une religion qui vénère les vers des sables comme des créatures sacrées.",
    "Une société qui a développé des capacités mentales extraordinaires.",
    "Un conflit entre différentes maisons nobles pour le contrôle d'une planète.",
    "Une prophétie qui guide les actions d'un peuple tout en les manipulant.",
    "Une transformation physique et mentale induite par la consommation d'épice."
]

def generer_reflexion():
    """Génère une réflexion aléatoire inspirée par Dune."""
    citation = random.choice(CITATIONS)
    proverbe = random.choice(PROVERBES)
    theme = random.choice(THEMES)
    question = random.choice(QUESTIONS)
    scenario = random.choice(SCENARIOS)
    
    return {
        "citation": citation,
        "proverbe": proverbe,
        "theme": theme,
        "question": question,
        "scenario": scenario
    }

def sauvegarder_reflexion(reflexion, titre=None):
    """Sauvegarde la réflexion dans un fichier."""
    if titre is None:
        titre = f"reflexion_dune_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des réflexions s'il n'existe pas
    chemin_reflexions = Path("reflexions_dune")
    chemin_reflexions.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_reflexions / f"{titre}.txt", "w", encoding="utf-8") as f:
        f.write(f"Citation de Dune :\n{reflexion['citation']}\n\n")
        f.write(f"Proverbe du désert :\n{reflexion['proverbe']}\n\n")
        f.write(f"Thème de réflexion :\n{reflexion['theme']}\n\n")
        f.write(f"Question philosophique :\n{reflexion['question']}\n\n")
        f.write(f"Scénario de Dune :\n{reflexion['scenario']}\n")
    
    # Sauvegarder en JSON
    with open(chemin_reflexions / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump(reflexion, f, ensure_ascii=False, indent=2)
    
    return chemin_reflexions / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère une réflexion inspirée par Dune")
    parser.add_argument("--titre", help="Titre de la réflexion")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de réflexions inspirées par Dune")
    print("=" * 60)
    
    # Générer la réflexion
    reflexion = generer_reflexion()
    
    # Afficher la réflexion
    print("\nVotre réflexion :\n")
    print(f"Citation de Dune :\n{reflexion['citation']}\n")
    print(f"Proverbe du désert :\n{reflexion['proverbe']}\n")
    print(f"Thème de réflexion :\n{reflexion['theme']}\n")
    print(f"Question philosophique :\n{reflexion['question']}\n")
    print(f"Scénario de Dune :\n{reflexion['scenario']}\n")
    
    # Sauvegarder la réflexion
    chemin = sauvegarder_reflexion(reflexion, args.titre)
    print(f"\nLa réflexion a été sauvegardée dans : {chemin}")

if __name__ == "__main__":
    main() 
 