#!/usr/bin/env python
"""
Générateur de réflexions inspirées par Citadelle
Ce script génère des réflexions et des citations inspirées par Citadelle
d'Antoine de Saint-Exupéry, explorant ses thèmes philosophiques sur l'humanité,
la civilisation et le sens de la vie.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Citations de Citadelle
CITATIONS = [
    "L'amour, ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction.",
    "Ce qui embellit le désert, c'est qu'il cache un puits quelque part.",
    "L'essentiel est invisible pour les yeux.",
    "On ne voit bien qu'avec le cœur.",
    "Aimer ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction.",
    "La vérité n'est pas ce qui est démontrable, la vérité est ce qui est inéluctable.",
    "La vie nous a enseigné que l'amour ne consiste pas à se regarder l'un l'autre mais à regarder ensemble dans la même direction.",
    "Le langage est source de malentendus.",
    "Les hommes n'ont plus le temps de rien connaître. Ils achètent des choses toutes faites chez les marchands. Mais comme il n'existe point de marchands d'amis, les hommes n'ont plus d'amis.",
    "Les étoiles sont éclairées pour que chacun puisse un jour retrouver la sienne."
]

# Méditations philosophiques
MEDITATIONS = [
    "La civilisation n'est pas dans le confort, elle est dans la conscience.",
    "L'homme n'est qu'un nœud de relations. Les relations seules comptent pour l'homme.",
    "Le bonheur n'est pas dans la possession, mais dans le don.",
    "La vérité n'est pas ce qui est démontrable, mais ce qui est inéluctable.",
    "L'amour n'est pas une émotion, c'est un acte de création.",
    "La liberté n'est pas l'absence de contraintes, mais la capacité de choisir ses contraintes.",
    "Le sens de la vie n'est pas dans la durée, mais dans la qualité.",
    "La beauté n'est pas dans l'apparence, mais dans l'essence.",
    "La sagesse n'est pas dans la connaissance, mais dans la compréhension.",
    "Le progrès n'est pas dans l'accumulation, mais dans la transformation."
]

# Thèmes de réflexion
THEMES = [
    "L'amour et l'amitié",
    "La liberté et la responsabilité",
    "La vérité et la sagesse",
    "La civilisation et la barbarie",
    "Le sens de la vie",
    "La beauté et l'art",
    "La nature et l'homme",
    "Le langage et la communication",
    "Le temps et l'éternité",
    "La mort et l'immortalité"
]

# Questions philosophiques
QUESTIONS = [
    "Qu'est-ce qui donne un sens à notre existence ?",
    "Comment définir l'amour véritable ?",
    "Quelle est la nature de la liberté humaine ?",
    "Comment distinguer la vérité de l'illusion ?",
    "Quelle est la relation entre l'individu et la société ?",
    "Comment comprendre la beauté authentique ?",
    "Quelle est la place de l'homme dans l'univers ?",
    "Comment communiquer l'ineffable ?",
    "Quelle est la nature du temps et de l'éternité ?",
    "Comment faire face à notre mortalité ?"
]

# Paraboles
PARABOLES = [
    "Un roi qui construit une citadelle pour protéger son peuple, mais découvre que les murs les séparent.",
    "Un jardinier qui cultive son jardin non pour les fruits, mais pour la beauté du geste.",
    "Un voyageur qui cherche sa destination mais trouve son chemin.",
    "Un sculpteur qui taille la pierre non pour créer une forme, mais pour libérer celle qui s'y cache.",
    "Un musicien qui joue non pour les notes, mais pour les silences entre elles.",
    "Un peintre qui peint non ce qu'il voit, mais ce qu'il sent.",
    "Un écrivain qui écrit non pour être lu, mais pour être compris.",
    "Un philosophe qui pense non pour répondre, mais pour questionner.",
    "Un amant qui aime non pour posséder, mais pour libérer.",
    "Un sage qui enseigne non pour instruire, mais pour éveiller."
]

def generer_reflexion():
    """Génère une réflexion aléatoire inspirée par Citadelle."""
    citation = random.choice(CITATIONS)
    meditation = random.choice(MEDITATIONS)
    theme = random.choice(THEMES)
    question = random.choice(QUESTIONS)
    parabole = random.choice(PARABOLES)
    
    return {
        "citation": citation,
        "meditation": meditation,
        "theme": theme,
        "question": question,
        "parabole": parabole
    }

def sauvegarder_reflexion(reflexion, titre=None):
    """Sauvegarde la réflexion dans un fichier."""
    if titre is None:
        titre = f"reflexion_citadelle_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des réflexions s'il n'existe pas
    chemin_reflexions = Path("reflexions_citadelle")
    chemin_reflexions.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_reflexions / f"{titre}.txt", "w", encoding="utf-8") as f:
        f.write(f"Citation de Citadelle :\n{reflexion['citation']}\n\n")
        f.write(f"Méditation philosophique :\n{reflexion['meditation']}\n\n")
        f.write(f"Thème de réflexion :\n{reflexion['theme']}\n\n")
        f.write(f"Question philosophique :\n{reflexion['question']}\n\n")
        f.write(f"Parabole :\n{reflexion['parabole']}\n")
    
    # Sauvegarder en JSON
    with open(chemin_reflexions / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump(reflexion, f, ensure_ascii=False, indent=2)
    
    return chemin_reflexions / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère une réflexion inspirée par Citadelle")
    parser.add_argument("--titre", help="Titre de la réflexion")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de réflexions inspirées par Citadelle")
    print("=" * 60)
    
    # Générer la réflexion
    reflexion = generer_reflexion()
    
    # Afficher la réflexion
    print("\nVotre réflexion :\n")
    print(f"Citation de Citadelle :\n{reflexion['citation']}\n")
    print(f"Méditation philosophique :\n{reflexion['meditation']}\n")
    print(f"Thème de réflexion :\n{reflexion['theme']}\n")
    print(f"Question philosophique :\n{reflexion['question']}\n")
    print(f"Parabole :\n{reflexion['parabole']}\n")
    
    # Sauvegarder la réflexion
    chemin = sauvegarder_reflexion(reflexion, args.titre)
    print(f"\nLa réflexion a été sauvegardée dans : {chemin}")

if __name__ == "__main__":
    main() 
"""
Générateur de réflexions inspirées par Citadelle
Ce script génère des réflexions et des citations inspirées par Citadelle
d'Antoine de Saint-Exupéry, explorant ses thèmes philosophiques sur l'humanité,
la civilisation et le sens de la vie.
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime

# Citations de Citadelle
CITATIONS = [
    "L'amour, ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction.",
    "Ce qui embellit le désert, c'est qu'il cache un puits quelque part.",
    "L'essentiel est invisible pour les yeux.",
    "On ne voit bien qu'avec le cœur.",
    "Aimer ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction.",
    "La vérité n'est pas ce qui est démontrable, la vérité est ce qui est inéluctable.",
    "La vie nous a enseigné que l'amour ne consiste pas à se regarder l'un l'autre mais à regarder ensemble dans la même direction.",
    "Le langage est source de malentendus.",
    "Les hommes n'ont plus le temps de rien connaître. Ils achètent des choses toutes faites chez les marchands. Mais comme il n'existe point de marchands d'amis, les hommes n'ont plus d'amis.",
    "Les étoiles sont éclairées pour que chacun puisse un jour retrouver la sienne."
]

# Méditations philosophiques
MEDITATIONS = [
    "La civilisation n'est pas dans le confort, elle est dans la conscience.",
    "L'homme n'est qu'un nœud de relations. Les relations seules comptent pour l'homme.",
    "Le bonheur n'est pas dans la possession, mais dans le don.",
    "La vérité n'est pas ce qui est démontrable, mais ce qui est inéluctable.",
    "L'amour n'est pas une émotion, c'est un acte de création.",
    "La liberté n'est pas l'absence de contraintes, mais la capacité de choisir ses contraintes.",
    "Le sens de la vie n'est pas dans la durée, mais dans la qualité.",
    "La beauté n'est pas dans l'apparence, mais dans l'essence.",
    "La sagesse n'est pas dans la connaissance, mais dans la compréhension.",
    "Le progrès n'est pas dans l'accumulation, mais dans la transformation."
]

# Thèmes de réflexion
THEMES = [
    "L'amour et l'amitié",
    "La liberté et la responsabilité",
    "La vérité et la sagesse",
    "La civilisation et la barbarie",
    "Le sens de la vie",
    "La beauté et l'art",
    "La nature et l'homme",
    "Le langage et la communication",
    "Le temps et l'éternité",
    "La mort et l'immortalité"
]

# Questions philosophiques
QUESTIONS = [
    "Qu'est-ce qui donne un sens à notre existence ?",
    "Comment définir l'amour véritable ?",
    "Quelle est la nature de la liberté humaine ?",
    "Comment distinguer la vérité de l'illusion ?",
    "Quelle est la relation entre l'individu et la société ?",
    "Comment comprendre la beauté authentique ?",
    "Quelle est la place de l'homme dans l'univers ?",
    "Comment communiquer l'ineffable ?",
    "Quelle est la nature du temps et de l'éternité ?",
    "Comment faire face à notre mortalité ?"
]

# Paraboles
PARABOLES = [
    "Un roi qui construit une citadelle pour protéger son peuple, mais découvre que les murs les séparent.",
    "Un jardinier qui cultive son jardin non pour les fruits, mais pour la beauté du geste.",
    "Un voyageur qui cherche sa destination mais trouve son chemin.",
    "Un sculpteur qui taille la pierre non pour créer une forme, mais pour libérer celle qui s'y cache.",
    "Un musicien qui joue non pour les notes, mais pour les silences entre elles.",
    "Un peintre qui peint non ce qu'il voit, mais ce qu'il sent.",
    "Un écrivain qui écrit non pour être lu, mais pour être compris.",
    "Un philosophe qui pense non pour répondre, mais pour questionner.",
    "Un amant qui aime non pour posséder, mais pour libérer.",
    "Un sage qui enseigne non pour instruire, mais pour éveiller."
]

def generer_reflexion():
    """Génère une réflexion aléatoire inspirée par Citadelle."""
    citation = random.choice(CITATIONS)
    meditation = random.choice(MEDITATIONS)
    theme = random.choice(THEMES)
    question = random.choice(QUESTIONS)
    parabole = random.choice(PARABOLES)
    
    return {
        "citation": citation,
        "meditation": meditation,
        "theme": theme,
        "question": question,
        "parabole": parabole
    }

def sauvegarder_reflexion(reflexion, titre=None):
    """Sauvegarde la réflexion dans un fichier."""
    if titre is None:
        titre = f"reflexion_citadelle_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Créer le répertoire des réflexions s'il n'existe pas
    chemin_reflexions = Path("reflexions_citadelle")
    chemin_reflexions.mkdir(exist_ok=True)
    
    # Sauvegarder en texte
    with open(chemin_reflexions / f"{titre}.txt", "w", encoding="utf-8") as f:
        f.write(f"Citation de Citadelle :\n{reflexion['citation']}\n\n")
        f.write(f"Méditation philosophique :\n{reflexion['meditation']}\n\n")
        f.write(f"Thème de réflexion :\n{reflexion['theme']}\n\n")
        f.write(f"Question philosophique :\n{reflexion['question']}\n\n")
        f.write(f"Parabole :\n{reflexion['parabole']}\n")
    
    # Sauvegarder en JSON
    with open(chemin_reflexions / f"{titre}.json", "w", encoding="utf-8") as f:
        json.dump(reflexion, f, ensure_ascii=False, indent=2)
    
    return chemin_reflexions / f"{titre}.txt"

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère une réflexion inspirée par Citadelle")
    parser.add_argument("--titre", help="Titre de la réflexion")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Générateur de réflexions inspirées par Citadelle")
    print("=" * 60)
    
    # Générer la réflexion
    reflexion = generer_reflexion()
    
    # Afficher la réflexion
    print("\nVotre réflexion :\n")
    print(f"Citation de Citadelle :\n{reflexion['citation']}\n")
    print(f"Méditation philosophique :\n{reflexion['meditation']}\n")
    print(f"Thème de réflexion :\n{reflexion['theme']}\n")
    print(f"Question philosophique :\n{reflexion['question']}\n")
    print(f"Parabole :\n{reflexion['parabole']}\n")
    
    # Sauvegarder la réflexion
    chemin = sauvegarder_reflexion(reflexion, args.titre)
    print(f"\nLa réflexion a été sauvegardée dans : {chemin}")

if __name__ == "__main__":
    main() 
 