#!/usr/bin/env python3
"""
🧪 TEST DES PUZZLES SPÉCIFIQUES
0962bcdd (83.33%) et 05a7bcf2 (76.89%)
"""

import json
from solveur_transparent_arc import SolveurTransparentARC

def analyser_puzzle_detaille(puzzle_id, score_actuel):
    """Analyse détaillée d'un puzzle avec notre solveur amélioré"""
    print(f"\n🎯 ANALYSE DÉTAILLÉE - {puzzle_id}")
    print("=" * 50)
    print(f"📊 Score actuel: {score_actuel}%")
    print("🔍 Analyse avec solveur amélioré...")

    try:
        solveur = SolveurTransparentARC()
        resultat = solveur.analyser_puzzle_complet(puzzle_id)

        print("✅ Analyse réussie!")
        print(f"📝 Pattern détecté: {resultat.pattern_type}")
        print(".1f")
        print(f"📄 Explication: {resultat.explication}")

        # Analyser les exemples pour voir les patterns
        try:
            with open(f"ARC-AGI-2-main/data/training/{puzzle_id}.json", 'r') as f:
                puzzle_data = json.load(f)
        except:
            print("⚠️ Impossible de charger les données détaillées")
            return

        print("
📚 ANALYSE DES EXEMPLES:"        for i, exemple in enumerate(puzzle_data['train'], 1):
            input_grid = exemple['input']
            output_grid = exemple['output']

            print(f"\n🧪 Exemple {i}: {len(input_grid)}x{len(input_grid[0])} → {len(output_grid)}x{len(output_grid[0])}")

            # Analyser les couleurs
            couleurs_in = set()
            couleurs_out = set()

            for row in input_grid:
                for cell in row:
                    if cell != 0:
                        couleurs_in.add(cell)

            for row in output_grid:
                for cell in row:
                    if cell != 0:
                        couleurs_out.add(cell)

            print(f"   🎨 Couleurs: {sorted(couleurs_in)} → {sorted(couleurs_out)}")

            # Vérifier s'il y a des patterns spécifiques
            if len(couleurs_in) == 1 and len(couleurs_out) > 1:
                print("   🔄 Expansion de couleur unique")
            elif len(couleurs_out) < len(couleurs_in):
                print("   🔸 Réduction de couleurs")
            elif couleurs_in == couleurs_out:
                print("   🔄 Mêmes couleurs")

        # Évaluer le potentiel d'amélioration
        print("
🎯 ÉVALUATION:"        if resultat.pattern_type == "repetition_simple":
            print("   📊 Utilise déjà repetition_simple")

            if score_actuel < 80:
                print("   ⚠️ Score moyen - pourrait bénéficier d'autres patterns")
                print("   💡 Suggestions: vérifier patterns de symétrie, compression, etc.")
            elif score_actuel >= 95:
                print("   ✅ Score excellent - pattern adapté")
            else:
                print("   📈 Score correct - peut-être optimisable")

        else:
            print(f"   🔍 Utilise {resultat.pattern_type}")
            print("   💡 Nouveau pattern détecté!")

        return resultat

    except Exception as e:
        print(f"❌ Erreur analyse: {e}")
        return None

def main():
    print("🧪 TEST PUZZLES SPÉCIFIQUES")
    print("=" * 60)
    print("🎯 0962bcdd: 83.33% (réussi)")
    print("🎯 05a7bcf2: 76.89% (échoué)")
    print("🔍 Objectif: Évaluer potentiel d'amélioration")

    # Tester 0962bcdd
    resultat1 = analyser_puzzle_detaille("0962bcdd", 83.33)

    # Tester 05a7bcf2
    resultat2 = analyser_puzzle_detaille("05a7bcf2", 76.89)

    # Synthèse
    print("
📊 SYNTHÈSE:"    print("=" * 30)

    patterns_detectes = []
    if resultat1:
        patterns_detectes.append(resultat1.pattern_type)
    if resultat2:
        patterns_detectes.append(resultat2.pattern_type)

    print(f"📝 Patterns détectés: {set(patterns_detectes)}")

    print("
🎯 RECOMMANDATIONS:"    if 83.33 < 90:
        print("   💡 0962bcdd: Peut bénéficier d'optimisations")
    else:
        print("   ✅ 0962bcdd: Score satisfaisant")

    if 76.89 < 80:
        print("   🔧 05a7bcf2: Amélioration nécessaire")
        print("   💡 Suggestions: analyser les exemples d'échec")
    else:
        print("   📈 05a7bcf2: Score acceptable")

    print("
🚀 PROCHAINES ÉTAPES:"    print("   1. 🔍 Analyser les exemples d'échec pour 05a7bcf2")
    print("   2. 📊 Tester d'autres patterns sur ces puzzles")
    print("   3. 📈 Mesurer l'impact global des améliorations")

if __name__ == "__main__":
    main()
