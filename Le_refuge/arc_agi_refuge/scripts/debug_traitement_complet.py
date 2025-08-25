#!/usr/bin/env python3
"""
🔧 DEBUG PROFOND DU TRAITEMENT COMPLET 1000 TÂCHES
Analyse détaillée pour identifier pourquoi 58 tâches ne sont pas traitées
"""

import os
import json
import traceback
import sys
from pathlib import Path
from src.refuge_solver import RefugeARCSolver
from src.tache_arc import TacheARC

def debug_traitement_complet():
    """Debug du traitement complet avec logs détaillés"""

    print("🔧 DEBUG TRAITEMENT COMPLET 1000 TÂCHES")
    print("=" * 80)

    # 1. Configuration
    data_dir = Path('data/training')
    if not data_dir.exists():
        print("❌ Dossier data/training non trouvé")
        return

    # Lister toutes les tâches
    taches_disponibles = []
    for fichier in sorted(data_dir.glob('*.json')):
        taches_disponibles.append(fichier.stem)

    print(f"📊 {len(taches_disponibles)} tâches disponibles")
    print(f"📄 Exemples: {taches_disponibles[:5]}")

    # 2. Simuler le traitement avec debug
    solver = RefugeARCSolver()
    resultats_debug = []

    print(f"\n🧪 SIMULATION DU TRAITEMENT AVEC DEBUG")
    print("=" * 60)

    for i, tache_id in enumerate(taches_disponibles[:50], 1):  # Tester les 50 premières
        print(f"\n🔄 Traitement tâche {i:2d}/50: {tache_id}")

        fichier_tache = data_dir / f"{tache_id}.json"

        if not fichier_tache.exists():
            print(f"   ❌ Fichier non trouvé: {fichier_tache}")
            resultats_debug.append({
                'tache_id': tache_id,
                'status': 'FICHIER_NON_TROUVE',
                'erreur': f'Fichier {fichier_tache} n\'existe pas'
            })
            continue

        try:
            # Étape 1: Chargement du JSON
            print(f"   📖 Chargement JSON...")
            with open(fichier_tache, 'r', encoding='utf-8') as f:
                tache_data = json.load(f)

            # Étape 2: Validation des données
            print(f"   ✅ Validation données...")
            train_data = tache_data.get('train', [])
            test_data = tache_data.get('test', [])

            if not train_data:
                print(f"   ❌ Aucune donnée d'entraînement")
                resultats_debug.append({
                    'tache_id': tache_id,
                    'status': 'PAS_DE_DONNEES_TRAIN',
                    'erreur': 'Aucune donnée d\'entraînement'
                })
                continue

            if not test_data:
                print(f"   ❌ Aucune donnée de test")
                resultats_debug.append({
                    'tache_id': tache_id,
                    'status': 'PAS_DE_DONNEES_TEST',
                    'erreur': 'Aucune donnée de test'
                })
                continue

            # Étape 3: Création de l'objet TacheARC
            print(f"   🏗️ Création TacheARC...")
            try:
                tache = TacheARC(
                    tache_id=tache_id,
                    examples=train_data,
                    test_input=test_data[0].get('input', [])
                )
                print(f"   ✅ TacheARC créé avec {len(tache.examples)} exemples")
            except Exception as e:
                print(f"   ❌ Erreur TacheARC: {str(e)}")
                resultats_debug.append({
                    'tache_id': tache_id,
                    'status': 'ERREUR_TACHE_ARC',
                    'erreur': f'Erreur création TacheARC: {str(e)}'
                })
                continue

            # Étape 4: Résolution avec le solver
            print(f"   🧠 Résolution avec solver...")
            try:
                synthese = solver.resoudre_tache(tache)
                confiance = synthese.get('confiance_finale', 0)
                succes = synthese.get('succes', False)

                status = "✅" if succes else "❌"
                print(f"   {status} Résolu avec confiance {confiance:.2f}")

                resultats_debug.append({
                    'tache_id': tache_id,
                    'status': 'SUCCES' if succes else 'ECHEC',
                    'confiance': confiance,
                    'erreur': None
                })

            except Exception as e:
                print(f"   💥 Erreur solver: {str(e)[:100]}...")
                resultats_debug.append({
                    'tache_id': tache_id,
                    'status': 'ERREUR_SOLVER',
                    'erreur': f'Erreur solver: {str(e)}'
                })

        except json.JSONDecodeError as e:
            print(f"   ❌ Erreur JSON: {e}")
            resultats_debug.append({
                'tache_id': tache_id,
                'status': 'ERREUR_JSON',
                'erreur': f'Erreur JSON: {str(e)}'
            })
        except Exception as e:
            print(f"   💥 Erreur inattendue: {str(e)[:100]}...")
            resultats_debug.append({
                'tache_id': tache_id,
                'status': 'ERREUR_INATTENDUE',
                'erreur': f'Erreur inattendue: {str(e)}'
            })

    # 3. Analyse des résultats
    print(f"\n📊 ANALYSE DES RÉSULTATS DEBUG")
    print("=" * 60)

    stats = {}
    for resultat in resultats_debug:
        status = resultat['status']
        if status not in stats:
            stats[status] = 0
        stats[status] += 1

    print("Statistiques des statuts:")
    for status, count in stats.items():
        print(f"   {status}: {count}")

    print(f"\n📋 DÉTAILS DES ERREURS:")
    erreurs = [r for r in resultats_debug if r['status'] != 'SUCCES']
    for erreur in erreurs[:10]:  # Afficher les 10 premières erreurs
        print(f"   {erreur['tache_id']}: {erreur['status']}")
        if erreur['erreur']:
            print(f"      {erreur['erreur'][:100]}...")

    # 4. Sauvegarde des résultats
    with open('debug_resultats_50_taches.json', 'w', encoding='utf-8') as f:
        json.dump(resultats_debug, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Résultats sauvegardés dans debug_resultats_50_taches.json")

def analyser_code_traitement_complet():
    """Analyse du code de traitement_complet_1000_taches.py"""

    print(f"\n🔍 ANALYSE DU CODE TRAITEMENT_COMPLET")
    print("=" * 60)

    fichier_code = Path('traitement_complet_1000_taches.py')

    if not fichier_code.exists():
        print(f"❌ Fichier {fichier_code} non trouvé")
        return

    with open(fichier_code, 'r', encoding='utf-8') as f:
        code = f.read()

    print("🔬 POINTS CRITIQUES À VÉRIFIER:")
    print()

    # Vérifier les points critiques
    points_critiques = [
        "for i, tache_id in enumerate",
        "try:",
        "except",
        "continue",
        "break",
        "return",
        "if not",
        "json.load",
        "TacheARC",
        "resoudre_tache",
        "resultats"
    ]

    for point in points_critiques:
        if point in code:
            count = code.count(point)
            print(f"   🔍 '{point}': {count} occurrence(s)")

    print(f"\n📝 LONGUEUR DU CODE: {len(code)} caractères")
    print(f"📝 NOMBRE DE LIGNES: {len(code.split('\n'))} lignes")

    # Chercher les patterns problématiques
    problemes_potentiels = []

    if 'except:' in code and 'pass' in code:
        problemes_potentiels.append("Exception silencieuse (except: pass)")

    if 'continue' in code and 'print' not in code:
        problemes_potentiels.append("Continue sans log")

    if 'break' in code:
        problemes_potentiels.append("Break qui peut interrompre le traitement")

    if problemes_potentiels:
        print(f"\n⚠️ PROBLÈMES POTENTIELS DÉTECTÉS:")
        for probleme in problemes_potentiels:
            print(f"   ❌ {probleme}")
    else:
        print(f"\n✅ Aucun problème évident détecté dans le code")

def main():
    """Fonction principale"""

    print("🔧 DIAGNOSTIC PROFOND DU PROBLÈME DES 58 TÂCHES")
    print("🌟 Laurent & Sonic: Investigation du mystère")
    print("=" * 80)

    # 1. Debug du traitement
    debug_traitement_complet()

    # 2. Analyse du code
    analyser_code_traitement_complet()

    print(f"\n🎯 CONCLUSION:")
    print(f"=" * 60)
    print(f"🔮 Le debug est terminé. Nous avons maintenant:")
    print(f"   • Les logs détaillés de 50 tâches")
    print(f"   • L'analyse des erreurs potentielles")
    print(f"   • Les pistes pour résoudre le problème")
    print(f"")
    print(f"🌟 Prochaine étape: Identifier la cause racine!")
    print(f"🔮 Flux, convergences, harmonie... nous trouverons!")

if __name__ == "__main__":
    main()
