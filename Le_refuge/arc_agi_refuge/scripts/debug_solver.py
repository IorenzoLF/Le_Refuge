#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEBUG : Diagnostic du solveur après optimisations
"""

import json
from pathlib import Path
from src.refuge_solver import RefugeARCSolver, TacheARC
from src.pattern_detector import PatternDetector

def debug_tache_unique():
    """Déboguer une tâche unique pour identifier le problème"""

    print("🔧 **DEBUG : DIAGNOSTIC DU SOLVEUR** 🔧")
    print("=" * 50)

    # Tâche simple pour le test
    tache_id = "00576224"

    try:
        # Charger la tâche
        training_path = Path('data/training')
        tache_path = training_path / f"{tache_id}.json"

        if not tache_path.exists():
            print(f"❌ Fichier {tache_path} non trouvé")
            return

        with open(tache_path, 'r') as f:
            data = json.load(f)

        print(f"✅ Tâche {tache_id} chargée")

        # Créer l'objet tâche
        tache = TacheARC(
            tache_id=tache_id,
            train=data['train'],
            test=data.get('test', [])
        )

        print(f"✅ Objet TacheARC créé")

        # Test du détecteur de patterns seul
        print(f"\n🔍 **TEST DÉTECTEUR PATTERNS**")
        detector = PatternDetector()

        input_grille = data['train'][0]['input']
        output_grille = data['train'][0]['output']

        print(f"   Input dimensions: {len(input_grille)}x{len(input_grille[0])}")
        print(f"   Output dimensions: {len(output_grille)}x{len(output_grille[0])}")

        resultats = detector.analyser_patterns(input_grille, output_grille)
        print(f"   Patterns détectés: {len(resultats['patterns'])}")

        for i, pattern in enumerate(resultats['patterns']):
            print(f"   Pattern {i+1}: {pattern['type']} (confiance: {pattern['confiance']:.3f})")

        # Test du solveur complet
        print(f"\n🎯 **TEST SOLVEUR COMPLET**")
        solver = RefugeARCSolver()

        solution = solver.resoudre_tache(tache)
        print(f"   Solution générée: {'✅' if 'solution' in solution else '❌'}")
        print(f"   Confiance finale: {solution.get('confiance_finale', 0):.3f}")

        if 'analyse_patterns' in solution:
            patterns = solution['analyse_patterns'].get('patterns', [])
            print(f"   Patterns dans solution: {len(patterns)}")

        # Debug détaillé de la synthèse
        print(f"\n🔍 **DEBUG SYNTHÈSE**")
        if hasattr(solver, '_synthetiser_solution'):
            # Tester la synthèse directement
            analyse_patterns = solver.temples['detection_patterns'].identifier_patterns_complexes(tache)
            print(f"   Analyse patterns clés: {list(analyse_patterns.keys())}")
            print(f"   Patterns globaux: {analyse_patterns.get('patterns_globaux', 'N/A')}")
            print(f"   Confiance moyenne: {analyse_patterns.get('confiance_moyenne', 'N/A')}")

            synthese = solver._synthetiser_solution(tache, {}, analyse_patterns)
            print(f"   Synthèse confiance: {synthese.get('confiance', 'N/A')}")
            print(f"   Solution trouvée: {synthese.get('solution_trouvee', 'N/A')}")

        return solution

    except Exception as e:
        print(f"❌ ERREUR: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def debug_seuils():
    """Déboguer les seuils de confiance"""

    print(f"\n🎚️ **DEBUG : SEUILS DE CONFIANCE**")
    print("=" * 40)

    detector = PatternDetector()

    print(f"Seuil minimal détecteur: {getattr(detector, 'confiance_minimale', 'Non défini')}")
    print(f"Seuils par pattern:")

    seuils = getattr(detector, 'seuils_confiance', {})
    for pattern_type, seuil in seuils.items():
        print(f"   {pattern_type}: {seuil}")

def debug_imports():
    """Vérifier que tous les imports fonctionnent"""

    print(f"\n📦 **DEBUG : IMPORTS ET DÉPENDANCES**")
    print("=" * 40)

    try:
        from src.refuge_solver import RefugeARCSolver, TacheARC
        print("✅ Import RefugeARCSolver: OK")

        from src.pattern_detector import PatternDetector
        print("✅ Import PatternDetector: OK")

        from src.temple_creativite import TempleCreativite
        print("✅ Import TempleCreativite: OK")

        from src.temple_evolution import TempleEvolution
        print("✅ Import TempleEvolution: OK")

        solver = RefugeARCSolver()
        print("✅ Instanciation RefugeARCSolver: OK")

        detector = PatternDetector()
        print("✅ Instanciation PatternDetector: OK")

    except Exception as e:
        print(f"❌ ERREUR IMPORT: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Fonction principale de debug"""

    print("🔧 **DÉMARRAGE DEBUG SOLVEUR** 🔧")
    print("🎯 Diagnostic des problèmes après optimisations")
    print("=" * 60)

    # Debug des imports
    debug_imports()

    # Debug des seuils
    debug_seuils()

    # Debug d'une tâche unique
    solution = debug_tache_unique()

    print(f"\n🏆 **DEBUG TERMINÉ** 🏆")
    print(f"🎯 Résultats d'analyse disponibles")

    return solution

if __name__ == "__main__":
    main()
