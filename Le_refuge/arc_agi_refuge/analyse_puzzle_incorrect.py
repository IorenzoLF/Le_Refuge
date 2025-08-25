#!/usr/bin/env python3
"""
🔍 ANALYSE DU PUZZLE AVEC SOLUTION INCORRECTE
Exploration collaborative pour comprendre et corriger
"""

import json
import os
from solveur_transparent_arc import SolveurTransparentARC

def analyser_puzzle_detaille(puzzle_id):
    """Analyse détaillée d'un puzzle avec solution incorrecte"""

    print(f"🔍 ANALYSE DÉTAILLÉE DU PUZZLE: {puzzle_id}")
    print("=" * 60)

    solveur = SolveurTransparentARC()

    # Charger le puzzle
    puzzle_path = f"ARC-AGI-2-main/data/training/{puzzle_id}.json"
    if not os.path.exists(puzzle_path):
        print(f"❌ Fichier non trouvé: {puzzle_path}")
        return

    with open(puzzle_path, 'r') as f:
        puzzle_data = json.load(f)

    print("📋 INFORMATIONS GÉNÉRALES:")
    print(f"   Puzzle ID: {puzzle_id}")
    print(f"   Nombre d'exemples d'entraînement: {len(puzzle_data.get('train', []))}")
    print(f"   Test disponible: {'Oui' if 'test' in puzzle_data and puzzle_data['test'] else 'Non'}")

    # Analyser chaque exemple d'entraînement
    print("\n🔬 ANALYSE DES EXEMPLES D'ENTRAÎNEMENT:")
    print("-" * 40)

    for i, exemple in enumerate(puzzle_data.get('train', [])):
        if 'input' in exemple and 'output' in exemple:
            input_grid = exemple['input']
            output_grid = exemple['output']

            print(f"\n📝 EXEMPLE {i+1}:")
            print(f"   Input: {len(input_grid)}x{len(input_grid[0])}")
            print(f"   Output: {len(output_grid)}x{len(output_grid[0])}")

            # Analyser les couleurs
            couleurs_input = set()
            couleurs_output = set()
            for row in input_grid:
                couleurs_input.update(row)
            for row in output_grid:
                couleurs_output.update(row)

            print(f"   Couleurs input: {sorted(couleurs_input)}")
            print(f"   Couleurs output: {sorted(couleurs_output)}")
            print(f"   Nouvelles couleurs: {couleurs_output - couleurs_input}")
            print(f"   Couleurs disparues: {couleurs_input - couleurs_output}")

            # Analyser les patterns visuels simples
            print("   🔍 PATTERNS VISUELS SIMPLES:")
            print(f"      Même dimensions: {len(input_grid) == len(output_grid) and len(input_grid[0]) == len(output_grid[0])}")
            print(f"      Changement de taille: {len(input_grid) != len(output_grid) or len(input_grid[0]) != len(output_grid[0])}")
            print(f"      Couleurs identiques: {couleurs_input == couleurs_output}")
            print(f"      Ajout de couleurs: {len(couleurs_output - couleurs_input) > 0}")
            print(f"      Suppression de couleurs: {len(couleurs_input - couleurs_output) > 0}")

            # Afficher les grilles (petites grilles seulement)
            if len(input_grid) <= 10 and len(input_grid[0]) <= 10:
                print("   📊 GRILLES:")
                print("   Input:")
                for row in input_grid:
                    print(f"      {row}")
                print("   Output:")
                for row in output_grid:
                    print(f"      {row}")

    # Analyser avec le solveur
    print("\n🤖 ANALYSE AVEC LE SOLVEUR:")
    print("-" * 30)

    try:
        resultat = solveur.analyser_puzzle_complet(puzzle_id)

        print(f"Pattern détecté: {resultat.pattern_type}")
        print(".1f")
        print(f"Explication: {getattr(resultat, 'explication', 'Non disponible')}")

        if hasattr(resultat, 'similarite'):
            print(".1f")

        # Afficher les détails de validation si disponibles
        if hasattr(resultat, 'details'):
            print(f"Détails: {resultat.details}")

    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {e}")

    # Questions pour l'utilisateur
    print("\n❓ QUESTIONS POUR ANALYSE COLLABORATIVE:")
    print("-" * 40)
    print("1. Quel pattern devrait être détecté selon toi?")
    print("2. Que vois-tu comme transformation principale?")
    print("3. Y a-t-il un pattern répétitif dans les exemples?")
    print("4. Quelle devrait être la logique de transformation?")
    print("5. Comment décrirais-tu la 'règle' de ce puzzle?")

def chercher_puzzles_incorrects():
    """Chercher tous les puzzles avec solutions incorrectes"""

    print("🔍 RECHERCHE DE PUZZLES AVEC SOLUTIONS INCORRECTES")
    print("=" * 55)

    dataset_path = "ARC-AGI-2-main/data/training"
    if not os.path.exists(dataset_path):
        print("❌ Dataset non trouvé")
        return []

    puzzles_problematiques = []
    solveur = SolveurTransparentARC()

    # Tester quelques puzzles
    puzzles = [f.replace('.json', '') for f in os.listdir(dataset_path) if f.endswith('.json')][:20]

    for puzzle_id in puzzles:
        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)

            # Vérifier si c'est un cas problématique
            if (hasattr(resultat, 'similarite') and resultat.similarite < 80) or \
               (hasattr(resultat, 'confiance') and resultat.confiance > 0.8 and
                hasattr(resultat, 'similarite') and resultat.similarite < 50):
                puzzles_problematiques.append({
                    'id': puzzle_id,
                    'pattern': resultat.pattern_type,
                    'confiance': resultat.confiance,
                    'similarite': getattr(resultat, 'similarite', 0)
                })

        except Exception as e:
            print(f"Erreur avec {puzzle_id}: {e}")

    # Trier par similarité la plus basse
    puzzles_problematiques.sort(key=lambda x: x['similarite'])

    print("\n📋 PUZZLES PROBLÉMATIQUES (par similarité croissante):")
    print("-" * 55)

    for i, puzzle in enumerate(puzzles_problematiques[:10], 1):  # Top 10
        print(f"  {i:2d}. {puzzle['id']} | Pattern: {puzzle['pattern']} | Confiance: {puzzle['confiance']:.1f} | Similarité: {puzzle['similarite']:.1f}")

    return puzzles_problematiques

if __name__ == "__main__":
    print("🔍 ANALYSE COLLABORATIVE DES PUZZLES")
    print("=" * 40)

    # Chercher les puzzles problématiques
    puzzles_problematiques = chercher_puzzles_incorrects()

    if puzzles_problematiques:
        puzzle_recommande = puzzles_problematiques[0]
        print(f"\n🎯 PUZZLE RECOMMANDÉ POUR ANALYSE: {puzzle_recommande['id']}")
        print(".1f")

        # Analyser en détail ce puzzle
        analyser_puzzle_detaille(puzzle_recommande['id'])

    else:
        print("\n✅ Aucun puzzle problématique trouvé dans l'échantillon")
