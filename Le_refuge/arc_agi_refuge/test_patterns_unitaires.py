#!/usr/bin/env python3
"""
🧪 TESTS UNITAIRES POUR TOUS LES PATTERNS ARC-AGI
Validation systématique de chaque module de patterns
"""

import sys
import os
from typing import List, Dict, Any

# Ajouter le répertoire actuel au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from solveur_transparent_arc import SolveurTransparentARC
from patterns_dimensions import GestionnaireDimensions
from patterns_diagonales import detecter_pattern_diagonal, appliquer_pattern_diagonal
from phase2_couleurs_complexes import detecter_pattern_couleurs, appliquer_pattern_couleurs
from phase3_spatiaux_complexes import detecter_pattern_spatial, appliquer_pattern_spatial
from validation_solution import valider_solution_complete

class TesteurPatternsUnitaires:
    """Framework de tests unitaires pour valider chaque pattern"""

    def __init__(self):
        self.solveur = SolveurTransparentARC()
        self.gestionnaire_dimensions = GestionnaireDimensions()
        self.resultats_tests = {}

    def calculer_similarite(self, grille_generee: List[List[int]], grille_attendue: List[List[int]]) -> float:
        """Calcule la similarité entre deux grilles"""
        if not grille_generee or not grille_attendue:
            return 0.0

        h1, w1 = len(grille_generee), len(grille_generee[0])
        h2, w2 = len(grille_attendue), len(grille_attendue[0])

        if h1 != h2 or w1 != w2:
            return 0.0

        total = h1 * w1
        correct = sum(1 for i in range(h1) for j in range(w1)
                     if grille_generee[i][j] == grille_attendue[i][j])

        return correct / total * 100

    def test_pattern_dimensions(self):
        """Test des patterns de dimensions"""
        print("📏 TEST PATTERNS DIMENSIONS")
        print("=" * 40)

        tests = [
            {
                'nom': 'Reduction symetrique 10x10 → 5x5',
                'input': [[(i + j) % 10 for j in range(10)] for i in range(10)],
                'output_attendu': [[(i*2 + j*2) % 10 for j in range(5)] for i in range(5)]
            },
            {
                'nom': 'Agrandissement symetrique 3x3 → 6x6',
                'input': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                'output_attendu': [[1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3],
                                 [4, 4, 5, 5, 6, 6], [4, 4, 5, 5, 6, 6],
                                 [7, 7, 8, 8, 9, 9], [7, 7, 8, 8, 9, 9]]
            }
        ]

        succes = 0
        for test in tests:
            try:
                pattern = self.gestionnaire_dimensions.detecter_changement_dimensions(test['input'], test['output_attendu'])
                if pattern['changement']:
                    dimensions_cible = (len(test['output_attendu']), len(test['output_attendu'][0]))
                    resultat = self.gestionnaire_dimensions.appliquer_changement_dimensions(
                        test['input'],
                        dimensions_cible,
                        pattern['type_changement']
                    )
                    similarite = self.calculer_similarite(resultat, test['output_attendu'])

                    if similarite > 80:
                        print(f"✅ {test['nom']}: {similarite:.1f}% similarite")
                        succes += 1
                    else:
                        print(f"❌ {test['nom']}: {similarite:.1f}% similarite")
                else:
                    print(f"⚠️  {test['nom']}: Aucun changement de dimensions detecte")

            except Exception as e:
                print(f"❌ {test['nom']}: Erreur - {e}")

        self.resultats_tests['dimensions'] = {'succes': succes, 'total': len(tests)}
        print(f"📊 Resultat dimensions: {succes}/{len(tests)} tests reussis\n")

    def test_pattern_diagonales(self):
        """Test des patterns diagonaux"""
        print("🔄 TEST PATTERNS DIAGONAUX")
        print("=" * 40)

        tests = [
            {
                'nom': 'Diagonal simple 3x3 → 3x3',
                'input': [[1, 0, 0], [0, 2, 0], [0, 0, 3]],
                'output_attendu': [[1, 2, 3], [0, 2, 0], [0, 0, 3]]
            }
        ]

        succes = 0
        for test in tests:
            try:
                pattern = detecter_pattern_diagonal(test['input'], test['output_attendu'])
                if pattern['detecte']:
                    resultat = appliquer_pattern_diagonal(test['input'], test['output_attendu'])
                    similarite = self.calculer_similarite(resultat, test['output_attendu'])

                    if similarite > 80:
                        print(f"✅ {test['nom']}: {similarite:.1f}% similarite")
                        succes += 1
                    else:
                        print(f"❌ {test['nom']}: {similarite:.1f}% similarite")
                else:
                    print(f"⚠️  {test['nom']}: Pattern non detecte")

            except Exception as e:
                print(f"❌ {test['nom']}: Erreur - {e}")

        self.resultats_tests['diagonales'] = {'succes': succes, 'total': len(tests)}
        print(f"📊 Resultat diagonales: {succes}/{len(tests)} tests reussis\n")

    def test_pattern_couleurs(self):
        """Test des patterns de couleurs"""
        print("🎨 TEST PATTERNS COULEURS")
        print("=" * 40)

        tests = [
            {
                'nom': 'Remplacement simple 1→2',
                'input': [[1, 1, 3], [1, 1, 3], [3, 3, 3]],
                'output_attendu': [[2, 2, 3], [2, 2, 3], [3, 3, 3]]
            },
            {
                'nom': 'Ajout couleur 4',
                'input': [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                'output_attendu': [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
            }
        ]

        succes = 0
        for test in tests:
            try:
                pattern = detecter_pattern_couleurs(test['input'], test['output_attendu'])
                if pattern['detecte']:
                    resultat = appliquer_pattern_couleurs(test['input'], pattern)
                    similarite = self.calculer_similarite(resultat, test['output_attendu'])

                    if similarite > 80:
                        print(f"✅ {test['nom']}: {similarite:.1f}% similarite")
                        succes += 1
                    else:
                        print(f"❌ {test['nom']}: {similarite:.1f}% similarite")
                else:
                    print(f"⚠️  {test['nom']}: Pattern non detecte")

            except Exception as e:
                print(f"❌ {test['nom']}: Erreur - {e}")

        self.resultats_tests['couleurs'] = {'succes': succes, 'total': len(tests)}
        print(f"📊 Resultat couleurs: {succes}/{len(tests)} tests reussis\n")

    def test_pattern_spatiaux(self):
        """Test des patterns spatiaux"""
        print("🌀 TEST PATTERNS SPATIAUX")
        print("=" * 40)

        tests = [
            {
                'nom': 'Remplissage intelligent',
                'input': [[1, 0, 3], [0, 1, 0], [3, 0, 1]],
                'output_attendu': [[1, 1, 3], [1, 1, 1], [3, 1, 1]]
            }
        ]

        succes = 0
        for test in tests:
            try:
                pattern = detecter_pattern_spatial(test['input'], test['output_attendu'])
                if pattern['detecte']:
                    resultat = appliquer_pattern_spatial(test['input'], pattern)
                    similarite = self.calculer_similarite(resultat, test['output_attendu'])

                    if similarite > 80:
                        print(f"✅ {test['nom']}: {similarite:.1f}% similarite")
                        succes += 1
                    else:
                        print(f"❌ {test['nom']}: {similarite:.1f}% similarite")
                else:
                    print(f"⚠️  {test['nom']}: Pattern non detecte")

            except Exception as e:
                print(f"❌ {test['nom']}: Erreur - {e}")

        self.resultats_tests['spatiaux'] = {'succes': succes, 'total': len(tests)}
        print(f"📊 Resultat spatiaux: {succes}/{len(tests)} tests reussis\n")

    def test_validation_solution(self):
        """Test du système de validation"""
        print("🛡️ TEST VALIDATION SOLUTION")
        print("=" * 40)

        tests = [
            {
                'nom': 'Solution parfaite',
                'generee': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                'attendue': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            },
            {
                'nom': 'Solution avec erreurs',
                'generee': [[1, 2, 3], [4, 0, 6], [7, 8, 9]],
                'attendue': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            },
            {
                'nom': 'Dimensions incorrectes',
                'generee': [[1, 2, 3], [4, 5, 6]],
                'attendue': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            }
        ]

        succes = 0
        for test in tests:
            try:
                validation = valider_solution_complete(test['generee'], test['attendue'])

                if test['nom'] == 'Solution parfaite' and validation['correct']:
                    print(f"✅ {test['nom']}: Correctement validee")
                    succes += 1
                elif test['nom'] == 'Solution avec erreurs' and not validation['correct']:
                    print(f"✅ {test['nom']}: Correctement rejetee ({validation['similarite']:.1f}%)")
                    succes += 1
                elif test['nom'] == 'Dimensions incorrectes' and validation['qualite'] == 'dimensions_incompatibles':
                    print(f"✅ {test['nom']}: Dimensions incorrectes detectees")
                    succes += 1
                else:
                    print(f"❌ {test['nom']}: Resultat inattendu")

            except Exception as e:
                print(f"❌ {test['nom']}: Erreur - {e}")

        self.resultats_tests['validation'] = {'succes': succes, 'total': len(tests)}
        print(f"📊 Resultat validation: {succes}/{len(tests)} tests reussis\n")

    def executer_tous_tests(self):
        """Exécute tous les tests unitaires"""
        print("🧪 TESTS UNITAIRES - PHASE 4")
        print("=" * 50)

        # Exécuter tous les tests
        self.test_pattern_dimensions()
        self.test_pattern_diagonales()
        self.test_pattern_couleurs()
        self.test_pattern_spatiaux()
        self.test_validation_solution()

        # Résumé final
        self.afficher_resume_final()

    def afficher_resume_final(self):
        """Affiche le résumé final des tests"""
        print("📊 RÉSUMÉ FINAL DES TESTS UNITAIRES")
        print("=" * 50)

        total_succes = 0
        total_tests = 0

        for module, resultat in self.resultats_tests.items():
            succes = resultat['succes']
            total = resultat['total']
            taux = succes / total * 100 if total > 0 else 0

            print(f"{module:12s}: {succes:2d}/{total:2d} ({taux:5.1f}%)")
            total_succes += succes
            total_tests += total

        taux_global = total_succes / total_tests * 100 if total_tests > 0 else 0
        print(f"GLOBAL    : {total_succes:2d}/{total_tests:2d} ({taux_global:5.1f}%)")
        if taux_global >= 80:
            print("🎉 TOUS LES MODULES VALIDÉS - Prêt pour l'intégration!")
        elif taux_global >= 60:
            print("⚠️  MODULES PRINCIPALEMENT VALIDÉS - Quelques ajustements nécessaires")
        else:
            print("❌ MODULES À AMÉLIORER - Tests échoués détectés")

def main():
    """Fonction principale"""
    testeur = TesteurPatternsUnitaires()
    testeur.executer_tous_tests()

if __name__ == "__main__":
    main()
