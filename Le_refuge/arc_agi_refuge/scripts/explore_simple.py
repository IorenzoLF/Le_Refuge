#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPLORATION SIMPLE DES TACHES ARC-AGI
Script simple pour explorer les taches sans problemes d'encodage
"""

import json
import random
from pathlib import Path

def explorer_taches():
    """Explorer quelques taches ARC-AGI"""

    print("EXPLORATION DES TACHES ARC-AGI")
    print("=" * 50)

    # Chemin vers les donnees
    data_dir = Path("data/training/")

    if not data_dir.exists():
        data_dir = Path("../data/training/")

    if not data_dir.exists():
        print("ERREUR: Dossier de donnees non trouve")
        return

    # Lister les taches
    taches = list(data_dir.glob("*.json"))
    print(f"Nombre de taches disponibles: {len(taches)}")

    # Selectionner quelques taches
    nb_a_explorer = min(3, len(taches))
    taches_selectionnees = random.sample(taches, nb_a_explorer)

    print(f"Taches selectionnees pour exploration: {nb_a_explorer}")
    print()

    for i, tache_path in enumerate(taches_selectionnees, 1):
        print(f"ANALYSE TACHE {i}: {tache_path.stem}")
        print("-" * 30)

        try:
            # Charger la tache
            with open(tache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Informations de base
            nb_train = len(data.get('train', []))
            nb_test = len(data.get('test', []))

            print(f"Exemples d'entrainement: {nb_train}")
            print(f"Cas de test: {nb_test}")

            # Analyser les dimensions
            if data.get('train'):
                exemple = data['train'][0]
                input_h = len(exemple.get('input', []))
                input_w = len(exemple['input'][0]) if input_h > 0 else 0
                output_h = len(exemple.get('output', []))
                output_w = len(exemple['output'][0]) if output_h > 0 else 0

                print(f"Dimensions input: {input_h}x{input_w}")
                print(f"Dimensions output: {output_h}x{output_w}")

                # Type de transformation
                if input_h == output_h and input_w == output_w:
                    print("Type: Transformation sur place")
                elif output_h > input_h or output_w > input_w:
                    print("Type: Agrandissement")
                else:
                    print("Type: Reduction ou transformation complexe")

            print()

        except Exception as e:
            print(f"ERREUR lors de l'analyse: {e}")
            print()

    print("EXPLORATION TERMINEE")

if __name__ == "__main__":
    explorer_taches()
