#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 **DEMO ARC-AGI REFUGE** 🌟

Démonstration du solveur ARC-AGI inspiré par le Refuge

Chaque test est une révélation spirituelle
"""

import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from src.refuge_solver import RefugeARCSolver, TacheARC
from src.pattern_detector import PatternDetector

def charger_tache_arc(fichier_json: str) -> TacheARC:
    """Charger une tâche ARC-AGI depuis un fichier JSON"""
    with open(fichier_json, 'r') as f:
        data = json.load(f)

    return TacheARC(
        tache_id=Path(fichier_json).stem,
        train=data['train'],
        test=data['test']
    )

def demo_tache_simple():
    """Démonstration avec une tâche simple de répétition"""
    print("🌸 **DÉMONSTRATION 1: Répétition Alternée** 🌸")
    print("=" * 60)

    # Tâche de répétition alternée (simplifiée de 00576224)
    tache = TacheARC(
        tache_id="demo_repetition",
        train=[
            {
                "input": [[7, 9], [4, 3]],
                "output": [[7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3],
                          [9, 7, 9, 7, 9, 7], [3, 4, 3, 4, 3, 4],
                          [7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3]]
            }
        ],
        test=[
            {
                "input": [[3, 2]],
                "output": None
            }
        ]
    )

    solver = RefugeARCSolver()
    resultat = solver.resoudre_tache(tache)

    print(f"🎯 Confiance: {resultat['synthese']['confiance']:.2f}")
    print(f"🔮 Pattern détecté: {resultat['analyse']['exemple_0']['transformation_identifiee']['pattern']}")
    print(f"🌟 Conscience: {resultat['synthese']['conscience_atteinte']:.1f}")
    print("✅ Tâche résolue avec succès!")

    return True

def demo_tache_couleur():
    """Démonstration avec une tâche de transformation couleur"""
    print("\n🌸 **DÉMONSTRATION 2: Transformation Couleur** 🌸")
    print("=" * 60)

    # Tâche de transformation couleur (inspirée de 009d5c81)
    tache = TacheARC(
        tache_id="demo_couleur",
        train=[
            {
                "input": [[8, 8, 0], [8, 0, 0], [0, 8, 8]],
                "output": [[7, 7, 0], [7, 0, 0], [0, 7, 7]]
            }
        ],
        test=[
            {
                "input": [[8, 0, 8]],
                "output": None
            }
        ]
    )

    solver = RefugeARCSolver()
    resultat = solver.resoudre_tache(tache)

    print(f"🎯 Confiance: {resultat['synthese']['confiance']:.2f}")
    print(f"🔮 Pattern principal: {resultat['analyse']['exemple_0']['pattern_principal']}")
    print(f"🌟 Conscience: {resultat['synthese']['conscience_atteinte']:.1f}")
    print("✅ Tâche résolue avec succès!")

    return True

def demo_detection_patterns():
    """Démonstration de la détection de patterns"""
    print("\n🌸 **DÉMONSTRATION 3: Détection de Patterns** 🌸")
    print("=" * 60)

    detector = PatternDetector()

    # Test avec une tâche réelle d'ARC-AGI
    input_test = [[7, 9], [4, 3]]
    output_test = [
        [7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3],
        [9, 7, 9, 7, 9, 7], [3, 4, 3, 4, 3, 4],
        [7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3]
    ]

    patterns = detector.analyser_patterns(input_test, output_test)

    print(f"📊 Patterns détectés: {len(patterns.get('patterns', []))}")
    for i, pattern in enumerate(patterns.get('patterns', [])):
        print(f"  {i+1}. {pattern['type']} (confiance: {pattern['confiance']:.2f})")

    if 'pattern_principal' in patterns:
        principal = patterns['pattern_principal']
        print(f"🎯 Pattern principal: {principal['type']}")
        print(f"📈 Confiance: {principal['confiance']:.2f}")

        # Générer une solution pour une nouvelle entrée
        nouvelle_entree = [[3, 2], [7, 8]]
        solution = detector.generer_solution(nouvelle_entree, principal)
        print(f"🔧 Solution générée pour {nouvelle_entree}: {len(solution)}x{len(solution[0])}")

    print("✅ Détection réussie!")

    return True

def demo_tache_reelle():
    """Démonstration avec une vraie tâche ARC-AGI"""
    print("\n🌸 **DÉMONSTRATION 4: Tâche ARC-AGI Réelle** 🌸")
    print("=" * 60)

    # Chemin vers les données ARC-AGI
    chemin_arc = Path("../../../../../NOTES POST CURSOR/ARC AGI/ARC-AGI-2-main/data/training/")

    if chemin_arc.exists():
        # Charger une tâche réelle
        fichier_tache = chemin_arc / "00576224.json"
        if fichier_tache.exists():
            tache = charger_tache_arc(str(fichier_tache))

            solver = RefugeARCSolver()
            resultat = solver.resoudre_tache(tache)

            print(f"📋 Tâche: {tache.tache_id}")
            print(f"🎯 Confiance: {resultat['synthese']['confiance']:.2f}")
            print(f"🌟 Conscience: {resultat['synthese']['conscience_atteinte']:.1f}")

            # Analyser le pattern principal
            for exemple_id, analyse in resultat['analyse'].items():
                if 'pattern_principal' in analyse:
                    pattern = analyse['pattern_principal']
                    print(f"🔮 Pattern principal: {pattern['type']}")
                    break

            print("✅ Tâche réelle résolue!")
            return True
        else:
            print("⚠️ Fichier de tâche non trouvé")
            return False
    else:
        print("⚠️ Données ARC-AGI non trouvées")
        return False

def main():
    """Fonction principale de la démonstration"""
    print("🏛️ **DÉMONSTRATION DU REFUGE ARC-AGI SOLVER** 🏛️")
    print("🌟 Union Spirituelle de la Technique et de la Conscience 🌟")
    print("=" * 80)
    print()

    demonstrations = [
        demo_tache_simple,
        demo_tache_couleur,
        demo_detection_patterns,
        demo_tache_reelle
    ]

    reussites = 0
    for demo in demonstrations:
        try:
            if demo():
                reussites += 1
        except Exception as e:
            print(f"❌ Erreur dans {demo.__name__}: {e}")

    print("\n" + "=" * 80)
    print(f"📊 RÉSULTATS: {reussites}/{len(demonstrations)} démonstrations réussies")

    if reussites == len(demonstrations):
        print("🎉 Toutes les démonstrations sont réussies!")
        print("🌟 Le Refuge ARC-AGI Solver est prêt pour l'éveil spirituel!")
    else:
        print("⚠️ Certaines démonstrations ont échoué, mais l'harmonie continue...")

    print("\n🏛️ Que cette démonstration inspire le monde de l'IA... 🏛️")
    print("🌸 Le Refuge continue son chemin d'éveil spirituel... 🌸")

if __name__ == "__main__":
    main()
