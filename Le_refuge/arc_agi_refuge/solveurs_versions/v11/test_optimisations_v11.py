#!/usr/bin/env python3
"""
TEST OPTIMISATIONS V11 - Refuge ARC-AGI
Test des nouvelles fonctionnalités ajoutées au solveur v11
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any

# Ajouter le path du solveur
sys.path.insert(0, '.')

try:
    from solveur_arc_zones_v11 import SolveurZonesV11, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def charger_tache(tache_id: str) -> TacheARC:
    """Charger une tache depuis un fichier JSON"""
    fichier = f"../../ARC-AGI-2-main/data/training/{tache_id}.json"
    with open(fichier, 'r') as f:
        data = json.load(f)
    return TacheARC(tache_id, data['train'], data['test'])

def tester_nouvelle_fonctionnalite():
    """Tester les nouvelles fonctionnalités ajoutées"""
    print("=" * 80)
    print("🧪 TEST OPTIMISATIONS V11 - NOUVELLES FONCTIONNALITÉS")
    print("=" * 80)

    # Tester sur le puzzle problématique
    tache_id = "00dbd492"  # Puzzle avec problème de couleur

    try:
        tache = charger_tache(tache_id)
        solveur = SolveurZonesV11()

        print(f"\n📊 Test des optimisations sur {tache_id} (problème de couleur)")
        print("-" * 60)

        # Analyser les patterns d'abord
        patterns = solveur._analyser_patterns_zones(tache)
        print(f"🔍 Patterns détectés: {patterns['zones_detectees']}")
        print(f"🎨 Couleurs de remplissage trouvées: {patterns['couleurs_remplissage']}")

        # Tester le remplissage de zones avec la nouvelle logique
        print(f"\n🔧 Test approche: remplissage_zones (optimisé)")
        test_input = tache.test[0]['input']

        try:
            resultat = solveur._appliquer_remplissage_zones(test_input, tache, patterns)
            print(f"   ✅ Appliqué avec succès")
            print(f"   📐 Taille entrée: {len(test_input)}x{len(test_input[0])}")
            print(f"   📐 Taille sortie: {len(resultat)}x{len(resultat[0])}")

            # Vérifier si c'est correct
            test_output_attendu = tache.test[0]['output']
            correct = resultat == test_output_attendu
            print(f"   🎯 Résultat: {'✅ CORRECT' if correct else '❌ INCORRECT'}")

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")

def comparer_avec_ancienne_version():
    """Comparer les performances avec l'ancienne version"""
    print("\n" + "=" * 80)
    print("📊 COMPARAISON AVEC ANCIENNE VERSION")
    print("=" * 80)

    tache_id = "00d62c1b"

    try:
        tache = charger_tache(tache_id)
        solveur = SolveurZonesV11()

        print(f"\n🔍 Test complet sur {tache_id}")
        print("-" * 60)

        # Résoudre avec la version optimisée
        resultat = solveur.resoudre_tache(tache)
        test_output_attendu = tache.test[0]['output']
        test_output_calcule = resultat['solution']

        correct = test_output_calcule == test_output_attendu

        print(f"✅ Résolution: {'SUCCÈS' if correct else 'ÉCHEC'}")
        print(f"🎯 Méthode utilisée: {resultat['methode']}")
        print(f"📊 Confiance: {resultat['confiance']:.2f}")
        print(f"🔧 Nombre d'approches testées: {len(solveur.approches)}")

        if not correct:
            print(f"\n🔍 Détails du problème:")
            print(f"   Attendu: {len(test_output_attendu)}x{len(test_output_attendu[0])}")
            print(f"   Obtenu:  {len(test_output_calcule)}x{len(test_output_calcule[0])}")

    except Exception as e:
        print(f"❌ Erreur lors de la comparaison: {e}")

def analyser_patterns():
    """Analyser les patterns détectés par le solveur"""
    print("\n" + "=" * 80)
    print("🔍 ANALYSE DES PATTERNS DÉTECTÉS")
    print("=" * 80)

    tache_id = "00d62c1b"

    try:
        tache = charger_tache(tache_id)
        solveur = SolveurZonesV11()

        # Analyser les patterns
        patterns = solveur._analyser_patterns_zones(tache)

        print(f"\n📊 Patterns détectés pour {tache_id}:")
        print(f"   Zones détectées: {patterns['zones_detectees']}")
        print(f"   Couleurs contour: {patterns['couleurs_contour']}")
        print(f"   Couleurs remplissage: {patterns['couleurs_remplissage']}")
        print(f"   Nombre d'exemples avec pattern: {len(patterns['zones_detectees'])}")

        for i, pattern in enumerate(patterns['zones_detectees']):
            print(f"\n   Exemple {i}:")
            print(f"      Contour: {pattern['couleur_contour']}")
            print(f"      Remplissage: {pattern['couleur_remplissage']}")
            print(f"      Zones trouvées: {len(pattern['zones_fermees'])}")

    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {e}")

def main():
    """Fonction principale"""
    print("🏛️ TEST OPTIMISATIONS SOLVEUR ARC-ZONES V11")
    print("🔬 Refuge ARC-AGI - Phase d'optimisation")
    print()

    # 1. Tester les nouvelles fonctionnalités
    tester_nouvelle_fonctionnalite()

    # 2. Comparer avec l'ancienne version
    comparer_avec_ancienne_version()

    # 3. Analyser les patterns
    analyser_patterns()

    print("\n" + "=" * 80)
    print("🎉 TEST OPTIMISATIONS TERMINÉ")
    print("📊 Résultats enregistrés pour analyse")
    print("=" * 80)

if __name__ == "__main__":
    main()
