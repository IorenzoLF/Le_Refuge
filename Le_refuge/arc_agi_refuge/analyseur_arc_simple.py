#!/usr/bin/env python3
"""
🔍 ANALYSEUR ARC SIMPLE - Pour vous aider à améliorer votre solveur
Aide non-technique pour comprendre et améliorer votre système ARC-AGI

Auteur: Sonic AI Assistant - Créé pour vous aider malgré les limitations techniques
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
import matplotlib.pyplot as plt
import numpy as np

class AnalyseurARCSimple:
    """Analyseur simple pour comprendre les puzzles ARC"""

    def __init__(self):
        self.couleurs_arc = {
            0: "🔵 NOIR",
            1: "🔴 ROUGE",
            2: "🟢 VERT",
            3: "🟡 JAUNE",
            4: "🔵 BLEU",
            5: "🟣 VIOLET",
            6: "🟠 ORANGE",
            7: "⚪ GRIS",
            8: "⚫ NOIR FONCÉ",
            9: "🔵 CYAN"
        }

    def analyser_puzzle_simple(self, tache_id: str) -> Dict[str, Any]:
        """Analyse simple d'un puzzle pour comprendre sa structure"""

        try:
            # Charger le puzzle
            fichier = f"ARC-AGI-2-main/data/training/{tache_id}.json"
            with open(fichier, 'r') as f:
                data = json.load(f)

            print(f"\n🧩 ANALYSE DU PUZZLE: {tache_id}")
            print("=" * 50)

            # Analyser les exemples d'entraînement
            print("📚 EXEMPLES D'ENTRAÎNEMENT:")
            for i, exemple in enumerate(data['train']):
                print(f"\n  Exemple {i+1}:")
                input_grid = exemple['input']
                output_grid = exemple['output']

                print(f"    Entrée: {len(input_grid)}x{len(input_grid[0])}")
                print(f"    Sortie: {len(output_grid)}x{len(output_grid[0])}")
                print(f"    Couleurs entrée: {set().union(*input_grid) if input_grid else 'vide'}")
                print(f"    Couleurs sortie: {set().union(*output_grid) if output_grid else 'vide'}")

                # Détection simple de patterns
                pattern = self.detecter_pattern_simple(input_grid, output_grid)
                print(f"    Pattern détecté: {pattern}")

            # Analyser les tests
            print(f"\n🧪 TESTS À RÉSOUDRE:")
            for i, test in enumerate(data['test']):
                input_grid = test['input']
                print(f"  Test {i+1}: {len(input_grid)}x{len(input_grid[0])}")
                print(f"    Couleurs: {set().union(*input_grid) if input_grid else 'vide'}")

            return {
                'id': tache_id,
                'nb_exemples': len(data['train']),
                'nb_tests': len(data['test']),
                'patterns_detectes': [self.detecter_pattern_simple(ex['input'], ex['output']) for ex in data['train']]
            }

        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de {tache_id}: {e}")
            return {}

    def detecter_pattern_simple(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> str:
        """Détection simple de patterns"""

        if not input_grid or not output_grid:
            return "Données vides"

        # Même taille ?
        meme_taille = (len(input_grid) == len(output_grid) and
                      len(input_grid[0]) == len(output_grid[0]) if input_grid and output_grid else False)

        # Compter les couleurs
        couleurs_in = set().union(*input_grid) if input_grid else set()
        couleurs_out = set().union(*output_grid) if output_grid else set()

        # Patterns simples
        if meme_taille and couleurs_in == couleurs_out:
            return "Même taille, mêmes couleurs"

        elif not meme_taille and couleurs_in.issubset(couleurs_out):
            return "Changement de taille avec couleurs conservées"

        elif couleurs_in != couleurs_out:
            return "Changement de couleurs"

        else:
            return "Pattern complexe"

    def comparer_solutions(self, tache_id: str, solution_predite: List[List[int]], solution_attendue: List[List[int]]) -> Dict[str, Any]:
        """Compare une solution prédite avec la solution attendue"""

        print(f"\n⚖️ COMPARAISON POUR {tache_id}")
        print("=" * 40)

        if solution_predite == solution_attendue:
            print("✅ SOLUTION CORRECTE !")
            return {'correct': True, 'score': 100}

        # Analyse des différences
        try:
            pred_array = np.array(solution_predite)
            attendu_array = np.array(solution_attendue)

            print(f"Dimensions prédites: {pred_array.shape}")
            print(f"Dimensions attendues: {attendu_array.shape}")
            print(f"Égalité parfaite: {np.array_equal(pred_array, attendu_array)}")

            if pred_array.shape != attendu_array.shape:
                print("❌ Dimensions différentes")
                return {'correct': False, 'score': 0, 'probleme': 'dimensions_differentes'}

            # Calculer la similarité
            differences = np.sum(pred_array != attendu_array)
            total_elements = pred_array.size
            similarite = (total_elements - differences) / total_elements * 100

            print(f"Similarité: {similarite:.1f}% ({total_elements - differences}/{total_elements} pixels corrects)")

            return {
                'correct': False,
                'score': similarite,
                'probleme': 'contenu_different',
                'differences': differences,
                'total_elements': total_elements
            }

        except Exception as e:
            print(f"❌ Erreur lors de la comparaison: {e}")
            return {'correct': False, 'score': 0, 'probleme': 'erreur_comparaison'}

    def generer_rapport_simple(self, resultats_tests: List[Dict[str, Any]]) -> str:
        """Génère un rapport simple des résultats"""

        if not resultats_tests:
            return "Aucun résultat à analyser"

        total = len(resultats_tests)
        corrects = sum(1 for r in resultats_tests if r.get('correct', False))

        rapport = f"""
📊 RAPPORT D'ANALYSE ARC SIMPLE
{'='*40}

🎯 PERFORMANCE GLOBALE:
   • Total de tests: {total}
   • Tests réussis: {corrects}
   • Taux de succès: {corrects/total*100:.1f}%

🔍 ANALYSE DES ERREURS:
"""

        erreurs_par_type = {}
        for r in resultats_tests:
            if not r.get('correct', False):
                prob = r.get('probleme', 'inconnu')
                erreurs_par_type[prob] = erreurs_par_type.get(prob, 0) + 1

        for erreur, count in erreurs_par_type.items():
            rapport += f"   • {erreur}: {count} fois\n"

        rapport += f"\n💡 RECOMMANDATIONS:\n"
        if corrects == 0:
            rapport += "   • Concentrez-vous sur le pattern de base détecté\n"
            rapport += "   • Vérifiez les dimensions de sortie\n"
            rapport += "   • Testez sur un puzzle plus simple d'abord\n"
        elif corrects/total < 0.5:
            rapport += "   • Bon début ! Améliorez la détection de couleurs\n"
            rapport += "   • Ajoutez plus de patterns de transformation\n"
            rapport += "   • Testez votre solveur sur plus d'exemples\n"
        else:
            rapport += "   • Excellent progrès !\n"
            rapport += "   • Peaufinez les détails\n"
            rapport += "   • Préparez-vous pour plus de puzzles complexes\n"

        return rapport

def main():
    """Fonction principale pour analyse simple"""

    print("🔍 ANALYSEUR ARC SIMPLE")
    print("======================")
    print("Cet outil vous aide à comprendre vos puzzles ARC sans coder!")

    analyseur = AnalyseurARCSimple()

    # Analyser quelques puzzles
    puzzles_test = ['00d62c1b', '00dbd492', '00576224']  # Le premier que vous avez résolu + d'autres

    resultats = []
    for puzzle_id in puzzles_test:
        try:
            analyse = analyseur.analyser_puzzle_simple(puzzle_id)
            resultats.append(analyse)
        except Exception as e:
            print(f"❌ Impossible d'analyser {puzzle_id}: {e}")

    # Générer rapport
    if resultats:
        rapport = analyseur.generer_rapport_simple(resultats)
        print(rapport)

        # Sauvegarder le rapport
        with open('rapport_analyse_arc_simple.txt', 'w', encoding='utf-8') as f:
            f.write(rapport)
        print("💾 Rapport sauvegardé dans 'rapport_analyse_arc_simple.txt'")

if __name__ == "__main__":
    main()
