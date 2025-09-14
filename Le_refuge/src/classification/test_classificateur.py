#!/usr/bin/env python3
"""
TEST DU CLASSIFICATEUR AUTOMATIQUE
Test rapide pour valider le système de classification
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin pour importer le classificateur
sys.path.append(str(Path(__file__).parent))

from classificateur_puzzles import ClassificateurPuzzles, analyser_ensemble_puzzles

def test_rapide():
    """Test rapide du classificateur sur quelques puzzles"""

    print("🧠 TEST DU CLASSIFICATEUR ARC-AGI")
    print("=" * 50)

    classificateur = ClassificateurPuzzles()
    training_dir = Path('arc_agi_refuge/ARC-AGI-2-main/data/training')

    # Test sur 10 puzzles seulement pour validation
    json_files = list(training_dir.glob('*.json'))[:10]

    resultats = {
        'total': 0,
        'categories': {},
        'erreurs': []
    }

    for i, json_file in enumerate(json_files, 1):
        try:
            import json
            with open(json_file, 'r') as f:
                data = json.load(f)

            caract = classificateur.analyser_puzzle(json_file.stem, data)
            categorie = caract.categorie_principale

            resultats['total'] += 1
            resultats['categories'][categorie] = resultats['categories'].get(categorie, 0) + 1

            print(f"✅ {json_file.stem} → {categorie} (confiance: {caract.confiance_classification:.2f})")

        except Exception as e:
            resultats['erreurs'].append(f"{json_file.stem}: {e}")
            print(f"❌ {json_file.stem}: {e}")

    # Résultats
    print("\n" + "=" * 50)
    print("📊 RÉSULTATS DU TEST")
    print(f"Total puzzles testés: {resultats['total']}")
    print(f"Erreurs: {len(resultats['erreurs'])}")

    print("\n📈 RÉPARTITION PAR CATÉGORIE:")
    for categorie, count in sorted(resultats['categories'].items()):
        pourcentage = (count / resultats['total']) * 100
        emoji = {'geometrie': '🔷', 'repetition': '🔶', 'couleur': '🟣', 'logique': '🔵', 'special': '⚫'}.get(categorie, '❓')
        print(f"  {emoji} {categorie}: {count} ({pourcentage:.1f}%)")

    if resultats['erreurs']:
        print("\n⚠️ ERREURS:")
        for erreur in resultats['erreurs']:
            print(f"  {erreur}")

    return resultats

if __name__ == "__main__":
    test_rapide()
