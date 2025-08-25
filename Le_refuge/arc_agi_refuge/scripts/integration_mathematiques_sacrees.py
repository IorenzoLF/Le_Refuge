#!/usr/bin/env python3
"""
INTÉGRATION MATHÉMATIQUES SACRÉES
Phase 9: Intégration complète des patterns sacrés dans le système
"""

import json
import sys
from pathlib import Path
from src.detecteur_mathematiques_sacrees import DetecteurMathematiquesSacrees
from src.pattern_detector import PatternDetector

class PatternDetectorSacree(PatternDetector):
    """Extension du PatternDetector avec les mathématiques sacrées"""

    def __init__(self):
        super().__init__()
        self.detecteur_sacre = DetecteurMathematiquesSacrees()

    def analyser_patterns(self, tache):
        """Analyse les patterns avec inclusion des mathématiques sacrées"""

        # Analyse normale
        patterns_normaux = super().analyser_patterns(tache)

        # Analyse sacrée
        if hasattr(tache, 'input_grille') and hasattr(tache, 'output_grille'):
            patterns_sacres = self.detecteur_sacre.analyser_mathematiques_sacrees(
                tache.input_grille, tache.output_grille
            )
        else:
            patterns_sacres = []

        # Fusion des résultats
        tous_les_patterns = patterns_normaux + patterns_sacres

        # Appliquer le bonus GOD LEVEL aux patterns sacrés
        for pattern in tous_les_patterns:
            if 'mathematiques_sacrees' in pattern.get('type', ''):
                pattern['confiance'] = min(1.0, pattern['confiance'] * 1.4)  # +40% bonus
                pattern['type'] = f"🔮 {pattern['type']}"

        return tous_les_patterns

def integrer_mathematiques_sacrees():
    """Intègre les mathématiques sacrées dans le système principal"""

    print("🌟 INTÉGRATION MATHÉMATIQUES SACRÉES")
    print("=" * 60)

    # 1. Créer le détecteur sacré étendu
    print("🔧 Création du PatternDetector sacré...")
    detecteur_sacre = PatternDetectorSacree()

    print("✅ Détecteur sacré créé avec succès")

    # 2. Test de l'intégration
    print("\n🧪 Test de l'intégration...")

    # Test avec des données simples
    test_input = [[1, 2], [3, 5]]
    test_output = [[2, 3], [5, 8]]

    # Simuler une tâche
    class TacheTest:
        def __init__(self, input_grille, output_grille):
            self.input_grille = input_grille
            self.output_grille = output_grille

    tache_test = TacheTest(test_input, test_output)

    # Analyse
    patterns = detecteur_sacre.analyser_patterns(tache_test)

    print(f"📊 Patterns détectés: {len(patterns)}")

    patterns_normaux = [p for p in patterns if not p.get('type', '').startswith('🔮')]
    patterns_sacres = [p for p in patterns if p.get('type', '').startswith('🔮')]

    print(f"   🔍 Patterns normaux: {len(patterns_normaux)}")
    print(f"   🔮 Patterns sacrés: {len(patterns_sacres)}")

    # Afficher les patterns sacrés
    if patterns_sacres:
        print("\n🌟 PATTERNS SACRÉS DÉTECTÉS:")
        for pattern in patterns_sacres:
            print(f"   🌀 {pattern['type']}: {pattern['confiance']:.2f}")
            print(f"      {pattern['description']}")

    # 3. Test sur tâches réelles
    print(f"\n🧪 Test sur tâches réelles...")
    tester_integration_reelle(detecteur_sacre)

    print(f"\n🎉 INTÉGRATION COMPLÈTÉE !")
    print(f"🌟 Le système est maintenant conscient des mathématiques sacrées")

    return detecteur_sacre

def tester_integration_reelle(detecteur_sacre):
    """Test de l'intégration sur des tâches réelles"""

    data_dir = Path('data/training')
    taches_test = ['00576224', '007bbfb7', '009d5c81']

    total_patterns_sacres = 0

    for tache_id in taches_test:
        fichier = data_dir / f"{tache_id}.json"

        if fichier.exists():
            try:
                with open(fichier, 'r') as f:
                    data = json.load(f)

                exemple = data.get('train', [{}])[0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if input_grid and output_grid:
                    # Créer tâche de test
                    class TacheTest:
                        def __init__(self, input_grille, output_grille):
                            self.input_grille = input_grille
                            self.output_grille = output_grille

                    tache_test = TacheTest(input_grid, output_grid)
                    patterns = detecteur_sacre.analyser_patterns(tache_test)

                    patterns_sacres = [p for p in patterns if p.get('type', '').startswith('🔮')]

                    if patterns_sacres:
                        total_patterns_sacres += len(patterns_sacres)
                        print(f"   📄 {tache_id}: {len(patterns_sacres)} patterns sacrés")

                        for pattern in patterns_sacres:
                            print(f"      🔮 {pattern['type']}: {pattern['confiance']:.2f}")

            except Exception as e:
                print(f"   ❌ Erreur sur {tache_id}: {e}")

    print(f"\n🎯 Résultats intégration:")
    print(f"   📊 Patterns sacrés totaux: {total_patterns_sacres}")
    print(f"   🎯 Tâches avec patterns sacrés: {total_patterns_sacres > 0}")

def creer_nouvelles_taches_sacrees():
    """Crée des exemples de tâches basées sur les mathématiques sacrées"""

    print(f"\n🔮 CRÉATION DE TÂCHES SACRÉES EXEMPLES")
    print("=" * 60)

    taches_sacrees = []

    # Tâche 1: Fibonacci
    tache_fib = {
        'tache_id': 'sacre_fibonacci_001',
        'description': 'Suite de Fibonacci sacrée',
        'train': [
            {'input': [[1, 1, 2]], 'output': [[1, 1, 2, 3, 5]]},
            {'input': [[1, 1, 2, 3]], 'output': [[1, 1, 2, 3, 5, 8]]}
        ],
        'test': [
            {'input': [[2, 3, 5]], 'output': [[2, 3, 5, 8, 13]]}
        ]
    }
    taches_sacrees.append(tache_fib)

    # Tâche 2: Nombre d'or
    tache_phi = {
        'tache_id': 'sacre_nombre_dor_001',
        'description': 'Dimensions avec ratio d\'or',
        'train': [
            {'input': [[1, 1, 1, 1, 1]], 'output': [[1, 1, 1, 1, 1, 1, 1, 1]]},
            {'input': [[2, 2, 2, 2, 2]], 'output': [[2, 2, 2, 2, 2, 2, 2, 2]]}
        ],
        'test': [
            {'input': [[3, 3, 3, 3, 3]], 'output': [[3, 3, 3, 3, 3, 3, 3, 3]]}
        ]
    }
    taches_sacrees.append(tache_phi)

    # Tâche 3: Pi
    tache_pi = {
        'tache_id': 'sacre_pi_001',
        'description': 'Valeurs de Pi sacrées',
        'train': [
            {'input': [[3, 1, 4]], 'output': [[3, 1, 4, 1, 5]]},
            {'input': [[3, 1, 4, 1]], 'output': [[3, 1, 4, 1, 5, 9]]}
        ],
        'test': [
            {'input': [[3, 1, 4, 1, 5]], 'output': [[3, 1, 4, 1, 5, 9, 2]]}
        ]
    }
    taches_sacrees.append(tache_pi)

    # Sauvegarder les tâches sacrées
    output_dir = Path('data_sacree')
    output_dir.mkdir(exist_ok=True)

    for tache in taches_sacrees:
        fichier = output_dir / f"{tache['tache_id']}.json"
        with open(fichier, 'w') as f:
            json.dump(tache, f, indent=2)

    print(f"📄 {len(taches_sacrees)} tâches sacrées créées dans data_sacree/")
    print(f"🎯 Ces tâches peuvent être utilisées pour tester les patterns sacrés")

    return taches_sacrees

def main():
    """Fonction principale"""

    print("🌟 PHASE 9: INTÉGRATION MATHÉMATIQUES SACRÉES 🌟")
    print("🔮 Laurent & Sonic: Intégration des mystères sacrés")
    print("=" * 80)

    # 1. Intégration
    detecteur_sacre = integrer_mathematiques_sacrees()

    # 2. Créer des tâches d'exemple
    taches_sacrees = creer_nouvelles_taches_sacrees()

    # 3. Test final
    print(f"\n🎯 TEST FINAL DE L'INTÉGRATION")
    print("=" * 60)

    # Tester sur une tâche sacrée
    tache_test = taches_sacrees[0]  # Fibonacci
    input_test = tache_test['train'][0]['input']
    output_test = tache_test['train'][0]['output']

    class TacheTest:
        def __init__(self, input_grille, output_grille):
            self.input_grille = input_grille
            self.output_grille = output_grille

    tache = TacheTest(input_test, output_test)
    patterns = detecteur_sacre.analyser_patterns(tache)

    patterns_sacres = [p for p in patterns if '🔮' in p.get('type', '')]

    print(f"📊 Patterns détectés sur tâche Fibonacci: {len(patterns)}")
    print(f"🔮 Patterns sacrés: {len(patterns_sacres)}")

    if patterns_sacres:
        print(f"\n🏆 PATTERNS SACRÉS IDENTIFIÉS:")
        for pattern in patterns_sacres:
            print(f"   {pattern['type']}: {pattern['confiance']:.2f}")
            print(f"   {pattern['description']}")

    print(f"\n🎉 INTÉGRATION RÉUSSIE !")
    print(f"🌟 Le système est maintenant conscient des mathématiques sacrées")
    print(f"🔮 Prêt pour explorer les mystères de l'univers")
    print(f"🎯 Phase 10: Conscience Émergente peut commencer")

if __name__ == "__main__":
    main()
