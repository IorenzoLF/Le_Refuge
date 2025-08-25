#!/usr/bin/env python3
"""
🔍 ANALYSE APPROFONDIE DES 58 TÂCHES MANQUANTES
Phase 6+ : Diagnostic complet du problème persistant
"""

import os
import json
import traceback
from pathlib import Path
from bibliotheque.developpement.arc_agi_refuge.src.refuge_solver import RefugeARCSolver, TacheARC

def analyser_toutes_les_taches():
    """Analyse complète de toutes les tâches disponibles vs traitées"""

    print("🔍 ANALYSE COMPLÈTE DES TÂCHES")
    print("=" * 80)

    # 1. Identifier toutes les tâches disponibles
    data_dir = Path('data/training')
    taches_totales = []

    if data_dir.exists():
        for fichier in sorted(data_dir.glob('*.json')):
            tache_id = fichier.stem
            taches_totales.append(tache_id)

        print(f"📊 Total de tâches disponibles: {len(taches_totales)}")
        print(f"📄 Exemples: {taches_totales[:5]}")
    else:
        print("❌ Dossier data/training non trouvé")
        return

    # 2. Identifier les tâches traitées dans les résultats
    taches_traitees = []

    # Chercher dans tous les fichiers de résultats
    fichiers_resultats = [f for f in os.listdir('.') if 'resultats' in f and f.endswith('.json')]

    for fichier in fichiers_resultats:
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Explorer différentes structures possibles
            if isinstance(data, dict):
                # Chercher récursivement tous les IDs de tâches
                def extraire_tache_ids(obj, ids_collectes):
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if isinstance(key, str) and len(key) == 8 and key.isalnum():
                                ids_collectes.add(key)
                            elif isinstance(value, str) and len(value) == 8 and value.isalnum():
                                ids_collectes.add(value)
                            else:
                                extraire_tache_ids(value, ids_collectes)
                    elif isinstance(obj, list):
                        for item in obj:
                            extraire_tache_ids(item, ids_collectes)

                ids_trouves = set()
                extraire_tache_ids(data, ids_trouves)
                taches_traitees.extend(ids_trouves)

        except Exception as e:
            print(f"⚠️ Erreur lecture {fichier}: {e}")

    taches_traitees = list(set(taches_traitees))  # Éliminer les doublons

    print(f"✅ Tâches traitées trouvées: {len(taches_traitees)}")
    print(f"📄 Exemples: {taches_traitees[:5]}")

    # 3. Identifier les tâches manquantes
    taches_manquantes = [t for t in taches_totales if t not in taches_traitees]

    print(f"\n🔍 RÉSULTATS:")
    print(f"   📊 Tâches totales: {len(taches_totales)}")
    print(f"   ✅ Tâches traitées: {len(taches_traitees)}")
    print(f"   ❌ Tâches manquantes: {len(taches_manquantes)}")
    print(f"   📈 Couverture: {len(taches_traitees)/len(taches_totales)*100:.1f}%")

    if taches_manquantes:
        print(f"\n📋 LISTE DES {len(taches_manquantes)} TÂCHES MANQUANTES:")
        for i, tache_id in enumerate(taches_manquantes, 1):
            print(f"   {i:2d}. {tache_id}")

        # Sauvegarder la liste complète
        with open('taches_manquantes_final.json', 'w', encoding='utf-8') as f:
            json.dump({
                'total_taches': len(taches_totales),
                'taches_traitees': len(taches_traitees),
                'taches_manquantes': taches_manquantes,
                'pourcentage_couverture': len(taches_traitees)/len(taches_totales)*100
            }, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Liste sauvegardée dans: taches_manquantes_final.json")

        # 4. Analyser quelques tâches manquantes en détail
        analyser_taches_manquantes_detail(taches_manquantes[:10])

        return taches_manquantes
    else:
        print("🎉 Aucune tâche manquante trouvée!")
        return []

def analyser_taches_manquantes_detail(taches_a_analyser):
    """Analyse détaillée de quelques tâches manquantes"""

    print(f"\n🔬 ANALYSE DÉTAILLÉE DES TÂCHES MANQUANTES")
    print("=" * 60)

    data_dir = Path('data/training')

    for tache_id in taches_a_analyser:
        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r') as f:
                    tache_data = json.load(f)

                print(f"\n📄 Tâche {tache_id}:")

                # Analyse de base
                nb_train = len(tache_data.get('train', []))
                nb_test = len(tache_data.get('test', []))
                print(f"   📊 {nb_train} exemples d'entraînement, {nb_test} tests")

                # Analyse des dimensions
                if nb_train > 0:
                    exemple = tache_data['train'][0]
                    input_grid = exemple.get('input', [])
                    output_grid = exemple.get('output', [])

                    if input_grid and output_grid:
                        h_in, w_in = len(input_grid), len(input_grid[0]) if input_grid else (0, 0)
                        h_out, w_out = len(output_grid), len(output_grid[0]) if output_grid else (0, 0)

                        print(f"   📐 Input: {h_in}x{w_in}, Output: {h_out}x{w_out}")

                        # Analyse des valeurs
                        valeurs_input = [val for row in input_grid for val in row]
                        valeurs_output = [val for row in output_grid for val in row]

                        val_min_in = min(valeurs_input) if valeurs_input else 0
                        val_max_in = max(valeurs_input) if valeurs_input else 0
                        val_min_out = min(valeurs_output) if valeurs_output else 0
                        val_max_out = max(valeurs_output) if valeurs_output else 0

                        print(f"   🎯 Input values: [{val_min_in}, {val_max_in}]")
                        print(f"   🎯 Output values: [{val_min_out}, {val_max_out}]")

                        # Test de chargement avec notre système
                        try:
                            tache = TacheARC(
                                tache_id=tache_id,
                                train=tache_data.get('train', []),
                                test=tache_data.get('test', [])
                            )
                            print(f"   ✅ Chargement TacheARC: OK")

                            # Test avec le solver
                            solver = RefugeARCSolver()
                            synthese = solver.resoudre_tache(tache)
                            print(f"   ✅ Résolution: OK - Confiance: {synthese.get('confiance_finale', 0):.2f}")

                        except Exception as e:
                            print(f"   ❌ Erreur système: {str(e)[:100]}...")

            except Exception as e:
                print(f"📄 Tâche {tache_id}: ❌ Erreur analyse - {str(e)[:80]}...")

def tester_batch_manquantes(taches_manquantes):
    """Test un batch des tâches manquantes"""

    print(f"\n🧪 TEST BATCH DES TÂCHES MANQUANTES")
    print("=" * 60)

    if not taches_manquantes:
        print("Aucune tâche manquante à tester")
        return

    solver = RefugeARCSolver()
    data_dir = Path('data/training')

    succes = 0
    total = min(20, len(taches_manquantes))  # Tester max 20 tâches

    print(f"Test des {total} premières tâches manquantes:")

    for i, tache_id in enumerate(taches_manquantes[:total], 1):
        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r') as f:
                    tache_data = json.load(f)

                # Créer et résoudre la tâche
                tache = TacheARC(
                    tache_id=tache_id,
                    train=tache_data.get('train', []),
                    test=tache_data.get('test', [])
                )

                synthese = solver.resoudre_tache(tache)
                confiance = synthese.get('confiance_finale', 0)
                reussi = synthese.get('succes', False)

                status = "✅" if reussi else "❌"
                print(f"   {i:2d}. {tache_id}: {status} ({confiance:.2f})")

                if reussi:
                    succes += 1

            except Exception as e:
                print(f"   {i:2d}. {tache_id}: 💥 ERREUR - {str(e)[:50]}...")

    print(f"\n📊 RÉSULTATS TEST BATCH:")
    print(f"   🎯 Testées: {total}")
    print(f"   ✅ Succès: {succes}")
    print(f"   📈 Taux de succès: {succes/total*100:.1f}%")

def main():
    """Fonction principale"""

    print("🔍 DIAGNOSTIC COMPLÈT DES 58 TÂCHES MANQUANTES")
    print("🌟 Laurent & Sonic: Résolution du mystère persistant")
    print("=" * 80)

    # 1. Analyse complète
    taches_manquantes = analyser_toutes_les_taches()

    # 2. Test batch si des tâches manquantes
    if taches_manquantes:
        tester_batch_manquantes(taches_manquantes)

    # 3. Diagnostic final
    print(f"\n🔬 DIAGNOSTIC FINAL:")
    print(f"=" * 60)

    if len(taches_manquantes) > 0:
        print(f"❌ PROBLÈME CONFIRMÉ:")
        print(f"   • {len(taches_manquantes)} tâches ne sont pas traitées")
        print(f"   • Ces tâches existent dans data/training/")
        print(f"   • Elles ne sont pas dans les fichiers de résultats")
        print(f"   • Le système semble les ignorer complètement")

        print(f"\n🔧 HYPOTHÈSES POSSIBLES:")
        print(f"   1. Erreur dans la boucle de traitement (index, exception silencieuse)")
        print(f"   2. Problème de format de données")
        print(f"   3. Erreur de parsing des fichiers JSON")
        print(f"   4. Exception non gérée qui interrompt le traitement")
        print(f"   5. Limitation de mémoire ou timeout")

        print(f"\n🎯 PROCHAINES ÉTAPES:")
        print(f"   1. Analyser le code de traitement_complet_1000_taches.py")
        print(f"   2. Ajouter des logs détaillés pour identifier où ça bloque")
        print(f"   3. Tester individuellement les tâches manquantes")
        print(f"   4. Vérifier les exceptions et erreurs cachées")

    else:
        print(f"🎉 AUCUN PROBLÈME DÉTECTÉ!")
        print(f"   • Toutes les tâches sont traitées")
        print(f"   • Le système fonctionne correctement")

    print(f"\n🌟 RÉSOLUTION EN COURS...")
    print(f"🔮 Nous trouverons la source du mystère!")

if __name__ == "__main__":
    main()
