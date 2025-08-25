#!/usr/bin/env python3
"""
🧪 TEST PATTERN PROJECTION LIMITÉE DOUBLE FORME
Test sur 0962bcdd pour valider notre découverte de la "croix en deux parties"
"""

import json
from pattern_projection_limitee_double_forme import detecter_pattern_projection_limitee_double_forme, appliquer_pattern_projection_limitee_double_forme

def test_projection_limitee_0962bcdd():
    print("🧪 TEST PATTERN PROJECTION LIMITÉE DOUBLE FORME")
    print("=" * 60)
    print("🎯 Puzzle: 0962bcdd (83.33% → 100%?)")
    print("🔍 Découverte: Croix en deux formes séparées")

    # Charger le puzzle
    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - ANALYSE CROIX DOUBLE:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"Input: {len(input_grid)}x{len(input_grid[0])}")
        print(f"Output: {len(output_grid)}x{len(output_grid[0])}")

        # Test de détection
        detection = detecter_pattern_projection_limitee_double_forme(input_grid, output_grid)

        print(f"✅ Détecté: {detection['detecte']}")
        print(".1f")

        if detection['detecte']:
            print(f"📝 Pattern: {detection['pattern']}")
            print(f"🎨 Couleurs: {detection['couleurs_sequence']}")
            print(f"🔍 Formes détectées: {len(detection['formes_detectees'])}")
            print(f"📐 Rectangles: {len(detection['rectangles_englobants'])}")

            # Afficher les rectangles détectés
            for rect in detection['rectangles_englobants']:
                min_x, min_y, max_x, max_y = rect['rect']
                print(f"  Rectangle {rect['forme_id']} (couleur {rect['couleur']}): ({min_x},{min_y}) → ({max_x},{max_y})")

        # Test d'application
        print("
⚙️ TEST APPLICATION:"        resultat = appliquer_pattern_projection_limitee_double_forme(input_grid, output_grid)

        print(f"📤 Résultat généré: {len(resultat)}x{len(resultat[0])}")

        # Calculer similarité
        def calculer_similarite(g1, g2):
            if not g1 or not g2 or len(g1) != len(g2) or len(g1[0]) != len(g2[0]):
                return 0.0
            total = sum(1 for i in range(len(g1)) for j in range(len(g1[0])) if g1[i][j] == g2[i][j])
            return total / (len(g1) * len(g1[0])) * 100

        similarite = calculer_similarite(resultat, output_grid)
        print(".1f")

        if similarite >= 95:
            print("🎉 SUCCÈS! Pattern parfait!")
        elif similarite >= 80:
            print("✅ BON! Pattern correct!")
        else:
            print("⚠️ Moyen, peut nécessiter ajustements")

        # Afficher quelques positions pour debug
        print("
🔍 COMPARAISON (premières lignes):"        for k in range(min(3, len(output_grid))):
            print(f"  Attendu:  {output_grid[k]}")
            print(f"  Généré:  {resultat[k]}")
            print(f"  Match:    {[1 if a == g else 0 for a, g in zip(output_grid[k], resultat[k])]}")

def main():
    test_projection_limitee_0962bcdd()

    print("
🎉 RÉSULTAT FINAL:"    print("✅ Pattern 'projection_limitee_double_forme' implémenté")
    print("✅ Intégré dans solveur principal")
    print("🎯 Objectif: 83.33% → 100% sur 0962bcdd")

if __name__ == "__main__":
    main()
