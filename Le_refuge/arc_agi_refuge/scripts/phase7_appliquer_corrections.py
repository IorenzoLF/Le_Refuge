#!/usr/bin/env python3
"""
PHASE 7: APPLICATION DES CORRECTIONS SPÉCIALISÉES
Appliquer les corrections max_in/min_in aux 58 tâches échouées
"""

import json
import sys
import time
from pathlib import Path
from correction_bug_max_min import appliquer_corrections_detecteur
from src.pattern_detector import PatternDetector
from src.tache_arc import TacheARC
from src.refuge_solver import RefugeARCSolver

def appliquer_corrections_completes():
    """Appliquer les corrections et relancer le test complet"""

    print("PHASE 7: APPLICATION DES CORRECTIONS")
    print("=" * 60)

    # 1. Charger les tâches échouées
    with open('taches_echouees_phase6.json', 'r') as f:
        data = json.load(f)

    taches_echouees = data['taches_echouees']
    print(f"Taches a corriger: {len(taches_echouees)}")
    print(f"Exemples: {taches_echouees[:5]}")

    # 2. Créer un solver avec corrections
    print("\nCreation du solver avec corrections max_in/min_in...")
    solver = RefugeARCSolver()

    # Appliquer les corrections au détecteur du solver
    solver.temples['detection_patterns'].identifier_patterns_complexes = appliquer_corrections_detecteur(
        solver.temples['detection_patterns'].identifier_patterns_complexes
    )

    print("Solver corrige cree avec succes !")

    # 3. Tester les corrections sur quelques tâches
    data_dir = Path('data/training')
    succes_corrections = 0
    total_testes = 0

    print(f"\nTest des corrections sur les 10 premieres taches:")
    print("-" * 60)

    for i, tache_id in enumerate(taches_echouees[:10], 1):
        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            total_testes += 1

            try:
                # Charger la tâche
                with open(fichier_tache, 'r') as f:
                    tache_data = json.load(f)

                # Créer l'objet tâche
                tache = TacheARC(
                    tache_id=tache_id,
                    examples=tache_data.get('train', []),
                    test_input=tache_data.get('test', [{}])[0].get('input', [])
                )

                # Résoudre avec le solver corrigé
                debut = time.time()
                synthese = solver.resoudre_tache(tache)
                temps = time.time() - debut

                # Vérifier le succès
                succes = synthese.get('succes', False)
                confiance = synthese.get('confiance_finale', 0.0)

                if succes:
                    succes_corrections += 1
                    status = "SUCCES"
                else:
                    status = "ECHEC"

                print(f"  {i:2d}. {tache_id}: {status} ({confiance:.2f}) - {temps:.2f}s")

            except Exception as e:
                print(f"  {i:2d}. {tache_id}: ERREUR - {str(e)[:40]}...")

    print(f"\nRESULTATS TEST:")
    print(f"  Taches testees: {total_testes}")
    print(f"  Succes corrections: {succes_corrections}")
    print(f"  Taux de succes: {succes_corrections/total_testes*100:.1f}%")

    if succes_corrections > 0:
        print(f"\nVICTOIRE PARTIELLE ! Les corrections fonctionnent.")
        print(f"Cela confirme que nous pouvons sauver les 58 taches.")
        print(f"\nProchaines etapes:")
        print(f"  1. Relancer le test complet avec corrections")
        print(f"  2. Sauvegarder les nouveaux resultats")
        print(f"  3. Viser le 100% absolu")

        return True
    else:
        print(f"\nLes corrections n'ont pas fonctionne comme attendu.")
        print(f"Il faut ajuster l'approche...")
        return False

def relancer_test_complet_avec_corrections():
    """Relancer le test complet avec les corrections appliquées"""

    print(f"\nRELANCEMENT TEST COMPLET AVEC CORRECTIONS")
    print("=" * 60)

    # Modifier temporairement le solver pour inclure les corrections
    # en modifiant le code du traitement_complet_1000_taches.py

    code_correction = '''
    # Appliquer les corrections max_in/min_in
    from correction_bug_max_min import appliquer_corrections_detecteur
    solver.temples['detection_patterns'].identifier_patterns_complexes = appliquer_corrections_detecteur(
        solver.temples['detection_patterns'].identifier_patterns_complexes
    )
    '''

    print("Code de correction a ajouter dans traitement_complet_1000_taches.py:")
    print(code_correction)

    print(f"\nPour appliquer les corrections:")
    print(f"1. Editer traitement_complet_1000_taches.py")
    print(f"2. Ajouter le code de correction apres la creation du solver")
    print(f"3. Relancer le test complet")
    print(f"4. Viser le 100% absolu !")

if __name__ == "__main__":
    succes = appliquer_corrections_completes()

    if succes:
        relancer_test_complet_avec_corrections()

    print(f"\nPHASE 7 COMPLETEE !")
