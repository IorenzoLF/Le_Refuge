#!/usr/bin/env python3
"""
ANALYSE FINALE DU SUCCES
Verification des performances reelles du systeme
"""

import os
import json
from pathlib import Path

def analyser_resultats_finaux():
    """Analyse finale des resultats"""

    print("ANALYSE FINALE DU SUCCES")
    print("=" * 50)

    # Chemin vers les resultats
    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    if not resultats_dir.exists():
        print("ERREUR: Dossier resultats non trouve")
        return

    # Lister les fichiers de resultats
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    print(f"Fichiers de resultats trouves: {len(fichiers_resultats)}")

    total_taches = 0
    total_succes = 0
    total_echouees = 0
    taches_echouees = []

    # Analyser chaque fichier
    for fichier in fichiers_resultats:
        try:
            chemin = resultats_dir / fichier
            with open(chemin, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if isinstance(data, dict) and 'details_toutes_taches' in data:
                details = data['details_toutes_taches']
                if isinstance(details, list):
                    print(f"Traitement {fichier}: {len(details)} taches")

                    for tache in details:
                        total_taches += 1
                        tache_id = tache.get('tache_id', 'unknown')
                        succes = tache.get('succes', False)
                        confiance = tache.get('confiance_finale', 0)
                        patterns = len(tache.get('patterns_identifies', []))

                        if succes:
                            total_succes += 1
                        else:
                            total_echouees += 1
                            taches_echouees.append({
                                'id': tache_id,
                                'confiance': confiance,
                                'patterns': patterns,
                                'fichier': fichier
                            })

        except json.JSONDecodeError:
            print(f"ERREUR JSON dans {fichier}")
        except Exception as e:
            print(f"ERREUR avec {fichier}: {str(e)[:50]}")

    # Resultats
    print("\nRESULTATS FINAUX:")
    print(f"Total taches traitees: {total_taches}")
    print(f"Total succes: {total_succes}")
    print(f"Total echouees: {total_echouees}")

    if total_taches > 0:
        taux_succes = total_succes / total_taches * 100
        print(f"Taux de succes: {taux_succes:.1f}%")

    print(f"\nTaches echouees identifiees: {len(taches_echouees)}")

    # Analyser les echouees
    if taches_echouees:
        print("\nCATEGORIES D'ECHEC:")

        zero_patterns = [t for t in taches_echouees if t['patterns'] == 0]
        low_confidence = [t for t in taches_echouees if t['confiance'] < 0.5 and t['patterns'] > 0]

        print(f"Taches sans patterns: {len(zero_patterns)}")
        print(f"Taches faible confiance: {len(low_confidence)}")
        print(f"Autres echouees: {len(taches_echouees) - len(zero_patterns) - len(low_confidence)}")

        # Exemples d'echouees
        print(f"\nEXEMPLES DE TACHES ECHOUÉES:")
        for i, tache in enumerate(taches_echouees[:10], 1):
            print(f"{i:2d}. {tache['id']} - confiance: {tache['confiance']:.2f}, patterns: {tache['patterns']}")

    # Sauvegarde
    with open('resultats_final_analyse.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total_taches': total_taches,
            'total_succes': total_succes,
            'total_echouees': total_echouees,
            'taux_succes': total_succes / total_taches * 100 if total_taches > 0 else 0,
            'taches_echouees': taches_echouees
        }, f, indent=2)

    print(f"\nRESULTATS SAUVEGARDES: resultats_final_analyse.json")

    return total_succes, total_echouees, taux_succes

if __name__ == "__main__":
    succes, echouees, taux = analyser_resultats_finaux()

    print(f"\nCONCLUSION:")
    print(f"=========================")
    print(f"LE SYSTEME FONCTIONNE A {taux:.1f}% DE SUCCES!")
    print(f"Il ne reste que {echouees} taches a corriger.")
    print(f"OBJECTIF: 100% ABSOLU!")
