#!/usr/bin/env python3
"""
Diagnostic du surapprentissage systémique
Analyse des vraies causes des échecs de généralisation
"""

import json
import os

def diagnostiquer_surapprentissage():
    print("🔬 DIAGNOSTIC DU SURAPPRENTISSAGE SYSTEMIQUE")
    print("=" * 55)
    print("🎯 Objectif: Identifier les causes profondes des échecs de généralisation")
    print()

    # Analyser quelques puzzles échoués
    puzzles_a_analyser = ["007bbfb7", "00d62c1b", "03560426"]

    for puzzle_id in puzzles_a_analyser:
        print(f"📋 ANALYSE DU PUZZLE {puzzle_id}")
        print("-" * 40)

        try:
            with open(f"ARC-AGI-2-main/data/training/{puzzle_id}.json", 'r') as f:
                data = json.load(f)

            print("🔍 COMPARAISON TRAINING vs TEST:")

            # Analyser les couleurs
            train_couleurs = set()
            test_couleurs = set()

            for exemple in data['train']:
                for row in exemple['input']:
                    train_couleurs.update(row)
                for row in exemple['output']:
                    train_couleurs.update(row)

            for exemple in data['test']:
                for row in exemple['input']:
                    test_couleurs.update(row)
                if 'output' in exemple:
                    for row in exemple['output']:
                        test_couleurs.update(row)

            print(f"  Couleurs training: {sorted(train_couleurs)}")
            print(f"  Couleurs test: {sorted(test_couleurs)}")
            print(f"  Nouvelles couleurs en test: {test_couleurs - train_couleurs}")

            # Analyser les dimensions
            train_dims = set()
            test_dims = set()

            for exemple in data['train']:
                inp = exemple['input']
                out = exemple['output']
                train_dims.add((len(inp), len(inp[0]), len(out), len(out[0])))

            for exemple in data['test']:
                inp = exemple['input']
                test_dims.add((len(inp), len(inp[0])))
                if 'output' in exemple:
                    out = exemple['output']
                    test_dims.add((len(inp), len(inp[0]), len(out), len(out[0])))

            print(f"  Dimensions training: {train_dims}")
            print(f"  Dimensions test: {test_dims}")
            print(f"  Nouvelles dimensions: {test_dims - train_dims}")

            # Analyser les patterns spatiaux
            print("  🔍 PATTERNS SPATIAUX:")

            # Training
            for i, exemple in enumerate(data['train'][:2], 1):
                inp = exemple['input']
                out = exemple['output']
                print(f"    Training {i}: {analyser_pattern_spatial(inp, out)}")

            # Test
            for i, exemple in enumerate(data['test'][:2], 1):
                inp = exemple['input']
                out = exemple['output'] if 'output' in exemple else None
                if out:
                    print(f"    Test {i}: {analyser_pattern_spatial(inp, out)}")
                else:
                    print(f"    Test {i}: Output masqué")

        except Exception as e:
            print(f"  ❌ Erreur: {e}")

        print()

def analyser_pattern_spatial(input_grid, output_grid):
    """Analyse basique des patterns spatiaux"""
    try:
        # Compter les pixels non-zéro
        input_count = sum(1 for row in input_grid for cell in row if cell != 0)
        output_count = sum(1 for row in output_grid for cell in row if cell != 0)

        # Rapport de pixels
        ratio = output_count / input_count if input_count > 0 else 0

        # Analyse de symétrie
        sym_h = est_symetrique_horizontale(output_grid)
        sym_v = est_symetrique_verticale(output_grid)

        return ".2f"
    except:
        return "Erreur d'analyse"

def est_symetrique_horizontale(grid):
    """Vérifie si la grille est symétrique horizontalement"""
    if not grid:
        return False
    n = len(grid)
    for i in range(n):
        if grid[i] != grid[n-1-i]:
            return False
    return True

def est_symetrique_verticale(grid):
    """Vérifie si la grille est symétrique verticalement"""
    if not grid or not grid[0]:
        return False
    n = len(grid[0])
    for i in range(n):
        col1 = [row[i] for row in grid]
        col2 = [row[n-1-i] for row in grid]
        if col1 != col2:
            return False
    return True

def analyser_causes_systemiques():
    print("🏗️ ANALYSE DES CAUSES SYSTEMIQUES")
    print("=" * 40)

    causes = [
        {
            "cause": "🎯 Approche bottom-up sans vision globale",
            "description": "Résoudre puzzle par puzzle sans architecture cohérente",
            "impact": "Chaque solveur est une solution ad hoc non réutilisable"
        },
        {
            "cause": "📊 Métriques locales sans validation globale",
            "description": "Tester seulement sur données d'entraînement du puzzle",
            "impact": "Aucun feedback sur l'impact global du système"
        },
        {
            "cause": "🔧 Sur-optimisation pour les cas vus",
            "description": "Ajustements excessifs pour matcher les exemples d'entraînement",
            "impact": "Perte de capacité de généralisation"
        },
        {
            "cause": "🏗️ Architecture non modulaire",
            "description": "Solveurs spécialisés au lieu de patterns réutilisables",
            "impact": "Impossible de composer et réutiliser les patterns"
        },
        {
            "cause": "🎨 Patterns visuels vs règles abstraites",
            "description": "Description de patterns apparents sans extraction des règles",
            "impact": "Manque de compréhension des mécanismes sous-jacents"
        }
    ]

    for i, cause in enumerate(causes, 1):
        print(f"{i}. {cause['cause']}")
        print(f"   📝 {cause['description']}")
        print(f"   💥 Impact: {cause['impact']}")
        print()

if __name__ == "__main__":
    diagnostiquer_surapprentissage()
    analyser_causes_systemiques()
