#!/usr/bin/env python3
"""
🔍 ANALYSE PROFONDE DES FICHIERS DE RÉSULTATS
Diagnostic avancé pour comprendre pourquoi le système ne traite aucune tâche
"""

import os
import json
from pathlib import Path

def analyser_fichier_resultats_detail(fichier):
    """Analyse détaillée d'un fichier de résultats"""

    print(f"\n🔬 ANALYSE DÉTAILLÉE DE {fichier}")
    print("=" * 80)

    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"📊 Structure du fichier:")
        print(f"   Type racine: {type(data)}")

        if isinstance(data, dict):
            print(f"   Clés principales: {list(data.keys())}")

            # Analyser details_toutes_taches si présent
            if 'details_toutes_taches' in data:
                details = data['details_toutes_taches']
                print(f"   Type details_toutes_taches: {type(details)}")
                print(f"   Nombre d'éléments: {len(details) if hasattr(details, '__len__') else 'N/A'}")

                if isinstance(details, list) and len(details) > 0:
                    premier = details[0]
                    print(f"   Structure premier élément: {type(premier)}")
                    if isinstance(premier, dict):
                        print(f"   Clés du premier élément: {list(premier.keys())}")

                        # Compter les tâches réussies et échouées
                        succes_count = 0
                        echec_count = 0
                        ids_trouves = []

                        for i, tache in enumerate(details[:10]):  # Analyser les 10 premières
                            if 'tache_id' in tache:
                                ids_trouves.append(tache['tache_id'])
                            if tache.get('succes', False):
                                succes_count += 1
                            else:
                                echec_count += 1

                        print(f"   Exemples d'IDs trouvés: {ids_trouves[:5]}")
                        print(f"   Succès dans l'échantillon: {succes_count}")
                        print(f"   Échecs dans l'échantillon: {echec_count}")

                        # Analyser les patterns d'erreur
                        erreurs = []
                        for tache in details[:50]:  # Analyser plus
                            if not tache.get('succes', True):
                                patterns = tache.get('patterns_identifies', [])
                                erreurs.append({
                                    'id': tache.get('tache_id', 'unknown'),
                                    'patterns': len(patterns),
                                    'confiance': tache.get('confiance_finale', 0)
                                })

                        if erreurs:
                            print(f"   📋 Analyse des erreurs (10 premiers):")
                            for err in erreurs[:10]:
                                print(f"      {err['id']}: {err['patterns']} patterns, conf {err['confiance']:.2f}")

            # Analyser les statistiques globales
            if 'succes_total' in data:
                print(f"   📈 Statistiques globales:")
                print(f"      Tâches traitées: {data.get('taches_traitees', 'N/A')}")
                print(f"      Succès total: {data.get('succes_total', 'N/A')}")
                print(f"      Taux de succès: {data.get('succes_rate_global', 'N/A')}")
                print(f"      Patterns détectés: {data.get('patterns_detectes_total', 'N/A')}")

        elif isinstance(data, list):
            print(f"   Nombre d'éléments: {len(data)}")
            if len(data) > 0:
                print(f"   Type premier élément: {type(data[0])}")
                if isinstance(data[0], dict):
                    print(f"   Clés premier élément: {list(data[0].keys())}")

        # Sauvegarder un échantillon pour analyse
        echantillon = {
            'fichier': fichier,
            'structure': str(type(data)),
            'taille': len(data) if hasattr(data, '__len__') else 'N/A',
            'contenu_sample': str(data)[:500] + '...' if len(str(data)) > 500 else str(data)
        }

        sample_file = f"sample_{Path(fichier).stem}.json"
        with open(sample_file, 'w', encoding='utf-8') as f:
            json.dump(echantillon, f, indent=2, ensure_ascii=False)

        print(f"   💾 Échantillon sauvegardé: {sample_file}")

    except json.JSONDecodeError as e:
        print(f"   ❌ ERREUR JSON: {e}")
        print(f"   📍 Position: ligne {e.lineno}, colonne {e.colno}")

        # Lire le fichier brut pour voir le problème
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"   📄 Contenu autour de l'erreur (100 chars):")
                start = max(0, e.pos - 50)
                end = min(len(content), e.pos + 50)
                print(f"   '{content[start:end]}'")
        except:
            print(f"   ❌ Impossible de lire le fichier brut")

    except Exception as e:
        print(f"   ❌ ERREUR INATTENDUE: {e}")

def analyser_tous_les_resultats():
    """Analyse tous les fichiers de résultats"""

    print("🔍 ANALYSE PROFONDE DE TOUS LES FICHIERS DE RÉSULTATS")
    print("=" * 80)

    # Trouver tous les fichiers de résultats
    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    print(f"📁 Fichiers de résultats trouvés: {len(fichiers_resultats)}")
    for fichier in fichiers_resultats:
        print(f"   • {fichier}")

    # Analyser chaque fichier
    for fichier in fichiers_resultats:
        chemin_complet = resultats_dir / fichier
        analyser_fichier_resultats_detail(chemin_complet)

def diagnostiquer_probleme_principal():
    """Diagnostic du problème principal"""

    print(f"\n🎯 DIAGNOSTIC DU PROBLÈME PRINCIPAL")
    print("=" * 60)

    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    print(f"📊 Analyse de {len(fichiers_resultats)} fichiers de résultats")

    total_taches_traitees = 0
    total_succes = 0
    fichiers_valides = 0
    fichiers_corrompus = 0

    for fichier in fichiers_resultats:
        try:
            with open(resultats_dir / fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if isinstance(data, dict) and 'details_toutes_taches' in data:
                details = data['details_toutes_taches']
                if isinstance(details, list):
                    fichiers_valides += 1
                    taches_dans_fichier = len(details)
                    total_taches_traitees += taches_dans_fichier

                    # Compter les succès
                    succes_fichier = sum(1 for t in details if t.get('succes', False))
                    total_succes += succes_fichier

                    print(f"   ✅ {fichier}: {taches_dans_fichier} tâches, {succes_fichier} succès")

        except json.JSONDecodeError:
            fichiers_corrompus += 1
            print(f"   ❌ {fichier}: CORROMPU (JSON invalide)")
        except Exception as e:
            print(f"   ⚠️ {fichier}: ERREUR - {str(e)[:50]}")

    print(f"\n📈 SYNTHÈSE:")
    print(f"   📁 Fichiers valides: {fichiers_valides}")
    print(f"   📁 Fichiers corrompus: {fichiers_corrompus}")
    print(f"   🎯 Tâches traitées au total: {total_taches_traitees}")
    print(f"   ✅ Succès au total: {total_succes}")

    if total_taches_traitees > 0:
        taux_succes = total_succes / total_taches_traitees * 100
        print(f"   📈 Taux de succès global: {taux_succes:.1f}%")

    print(f"\n🔧 HYPOTHÈSES SUR LE PROBLÈME:")

    if fichiers_corrompus > 0:
        print(f"   ❌ Des fichiers de résultats sont corrompus")
        print(f"   📝 Cela peut causer des erreurs de lecture")

    if total_taches_traitees == 0:
        print(f"   ❌ AUCUNE TÂCHE N'A ÉTÉ TRAITÉE!")
        print(f"   📝 Le système s'arrête avant de traiter quoi que ce soit")
        print(f"   🔧 Vérifier: exceptions non gérées, erreurs de parsing")

    if total_taches_traitees > 0 and total_succes == 0:
        print(f"   ❌ Toutes les tâches échouent")
        print(f"   📝 Le système traite mais ne réussit rien")
        print(f"   🔧 Vérifier: erreurs dans la détection de patterns")

    print(f"\n🎯 PROCHAINES ÉTAPES:")
    print(f"   1. Examiner les fichiers corrompus")
    print(f"   2. Vérifier le script de traitement principal")
    print(f"   3. Ajouter des logs de debug dans le traitement")
    print(f"   4. Tester individuellement quelques tâches")

if __name__ == "__main__":
    # Analyse de tous les résultats
    analyser_tous_les_resultats()

    # Diagnostic principal
    diagnostiquer_probleme_principal()

    print(f"\n🌟 ANALYSE PROFONDE TERMINÉE!")
    print(f"🔮 Nous avons maintenant une vue claire du problème!")
    print(f"🎯 Prêt à identifier la cause racine et la solution!")
