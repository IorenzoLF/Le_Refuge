#!/usr/bin/env python3
"""
🔄 ANALYSE DÉCALAGE PROGRESSIF - 05269061
Le vrai pattern: décalage diagonal progressif, pas alternance simple
"""

import json
from collections import Counter

def analyser_decalage_progressif():
    print("🔄 ANALYSE DÉCALAGE PROGRESSIF - 05269061")
    print("=" * 60)
    print("🎯 Découverte: Pas d'alternance simple")
    print("✅ Pattern: Décalage progressif diagonal")
    print("📝 Chaque ligne = décalage de la précédente")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - DÉCALAGE PROGRESSIF:")
        output_grid = exemple['output']

        print("LIGNES SUCCESSIVES:")
        h, w = len(output_grid), len(output_grid[0])
        for j in range(h):
            print(f"  Ligne {j}: {output_grid[j]}")

        # Analyser les décalages entre lignes successives
        print("
🔍 ANALYSE DÉCALAGES:"        decalages = []

        for j in range(h-1):
            ligne1 = output_grid[j]
            ligne2 = output_grid[j+1]

            # Trouver le décalage
            decalage_trouve = None
            for decalage in range(-w, w+1):
                match = True
                for k in range(w):
                    pos = k + decalage
                    if 0 <= pos < w:
                        if ligne1[k] != ligne2[pos]:
                            match = False
                            break
                    else:
                        match = False
                        break

                if match:
                    decalage_trouve = decalage
                    break

            if decalage_trouve is not None:
                decalages.append(decalage_trouve)
                print(f"  Ligne {j} → Ligne {j+1}: décalage {decalage_trouve} ✅")
            else:
                decalages.append(None)
                print(f"  Ligne {j} → Ligne {j+1}: pas de décalage simple ❌")

        print(f"\nDécalages trouvés: {decalages}")

        # Analyser la séquence de couleurs
        couleurs_sequence = []
        for row in output_grid:
            for cell in row:
                if cell != 0 and cell not in couleurs_sequence:
                    couleurs_sequence.append(cell)

        print(f"Séquence couleurs: {couleurs_sequence}")

        # Vérifier pattern diagonal progressif
        print("
🔍 VÉRIFICATION PATTERN DIAGONAL PROGRESSIF:"        pattern_diagonal = True
        explications = []

        for j in range(h):
            for k in range(w):
                if output_grid[j][k] != 0:
                    # Position diagonale attendue
                    position_diagonale = (j + k) % len(couleurs_sequence)
                    couleur_attendue = couleurs_sequence[position_diagonale]

                    if output_grid[j][k] == couleur_attendue:
                        explications.append(f"  ({j},{k}): {output_grid[j][k]} = {couleur_attendue} ✅")
                    else:
                        explications.append(f"  ({j},{k}): {output_grid[j][k]} ≠ {couleur_attendue} ❌")
                        pattern_diagonal = False

        print("Pattern diagonal progressif:", "✅" if pattern_diagonal else "❌")
        if not pattern_diagonal:
            print("Quelques exemples:")
            for exp in explications[:6]:  # 6 premiers
                print(exp)

        # Conclusion
        print("
🎯 CONCLUSION:"        if pattern_diagonal:
            print("   ✅ PATERN DIAGONAL PROGRESSIF CONFIRMÉ")
            print("   📝 Formule: couleur = sequence[(i+j) % longueur]")
            print("   🎨 Fonctionne pour cet exemple")
        else:
            print("   ❌ Pas un pattern diagonal simple")
            print("   🔍 Pattern plus complexe à identifier")
            print("   💡 Peut-être pattern de décalage différent")

def analyser_vrai_pattern():
    """Analyser le vrai pattern derrière les décalages"""

    print("
🧠 ANALYSE DU VRAI PATTERN:"    print("=" * 40)

    print("\n📊 OBSERVATIONS:")
    print("   1. Chaque ligne est un décalage de la précédente")
    print("   2. Le décalage n'est pas constant")
    print("   3. Il y a une logique de propagation")

    print("\n🔍 HYPOTHÈSES:")
    print("   1. Décalage = (i+1) % longueur_séquence")
    print("   2. Décalage = i % 3 (cyclique)")
    print("   3. Décalage basé sur position diagonale")

    print("\n💡 PROCHAINE ÉTAPE:")
    print("   🔧 Adapter le pattern 'ondulation_diagonale'")
    print("   📝 Changer logique de détection")
    print("   🎯 Reconnaître décalage progressif")

def main():
    analyser_decalage_progressif()
    analyser_vrai_pattern()

if __name__ == "__main__":
    main()
