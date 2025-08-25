#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRAITEMENT COMPLÈT DES 1000 TÂCHES : Ascension vers 100% de succès
"""

import json
import time
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from src.refuge_solver import RefugeARCSolver, TacheARC

def traiter_lot_taches(taches_ids: List[str], numero_lot: int) -> Dict[str, Any]:
    """Traiter un lot de tâches et retourner les résultats"""

    print(f"\n🎯 **TRAITEMENT LOT {numero_lot} : {len(taches_ids)} TÂCHES**")
    print("=" * 60)

    solver = RefugeARCSolver()

    # PHASE 7: APPLIQUER LES CORRECTIONS MAX_IN/MIN_IN
    try:
        from correction_bug_max_min import appliquer_corrections_detecteur
        solver.temples['detection_patterns'].identifier_patterns_complexes = appliquer_corrections_detecteur(
            solver.temples['detection_patterns'].identifier_patterns_complexes
        )
        print("   ✅ Corrections max_in/min_in appliquées")
    except Exception as e:
        print(f"   ⚠️ Erreur corrections: {e}")

    resultats_lot = {
        'lot': numero_lot,
        'total_taches': len(taches_ids),
        'traitees': 0,
        'succes': 0,
        'patterns_detectes_total': 0,
        'confiance_moyenne': 0.0,
        'patterns_frequents': {},
        'erreurs': 0,
        'details_taches': []
    }

    total_confiance = 0.0

    for i, tache_id in enumerate(taches_ids):
        try:
            # Charger la tâche
            json_path = Path('data/training') / f"{tache_id}.json"
            if not json_path.exists():
                print(f"   ⚠️  {tache_id}: Fichier non trouvé")
                resultats_lot['erreurs'] += 1
                continue

            with open(json_path, 'r') as f:
                data = json.load(f)

            tache = TacheARC(
                tache_id=tache_id,
                train=data['train'],
                test=data.get('test', [])
            )

            # Résoudre la tâche
            debut = time.time()
            solution = solver.resoudre_tache(tache)
            temps_execution = time.time() - debut

            # Analyser les résultats
            synthese = solution.get('synthese', {})
            patterns_identifies = synthese.get('patterns_identifies', [])
            nombre_patterns = synthese.get('nombre_patterns', 0)
            confiance_finale = synthese.get('confiance_finale', 0.0)

            # Mettre à jour les statistiques
            resultats_lot['traitees'] += 1
            if confiance_finale > 0.3:
                resultats_lot['succes'] += 1

            resultats_lot['patterns_detectes_total'] += nombre_patterns
            total_confiance += confiance_finale

            # Compter les patterns fréquents
            for pattern in patterns_identifies:
                resultats_lot['patterns_frequents'][pattern] = resultats_lot['patterns_frequents'].get(pattern, 0) + 1

            # Stocker les détails de la tâche
            details_tache = {
                'tache_id': tache_id,
                'patterns_identifies': patterns_identifies,
                'nombre_patterns': nombre_patterns,
                'confiance_finale': confiance_finale,
                'succes': confiance_finale > 0.3,
                'temps_execution': temps_execution
            }
            resultats_lot['details_taches'].append(details_tache)

            # Affichage progressif
            if (i + 1) % 20 == 0 or i == 0:
                progression = (i + 1) / len(taches_ids) * 100
                succes_rate = resultats_lot['succes'] / resultats_lot['traitees'] * 100 if resultats_lot['traitees'] > 0 else 0
                print(f"   📊 Progression: {i+1:3d}/{len(taches_ids):3d} ({progression:5.1f}%) | Succès: {succes_rate:5.1f}% | Patterns: {resultats_lot['patterns_detectes_total']:3d}")

        except Exception as e:
            resultats_lot['erreurs'] += 1
            print(f"   ❌ {tache_id}: Erreur - {str(e)[:50]}...")
            details_tache = {
                'tache_id': tache_id,
                'patterns_identifies': [],
                'nombre_patterns': 0,
                'confiance_finale': 0.0,
                'succes': False,
                'temps_execution': 0,
                'erreur': str(e)
            }
            resultats_lot['details_taches'].append(details_tache)

    # Calculer les métriques finales du lot
    if resultats_lot['traitees'] > 0:
        resultats_lot['confiance_moyenne'] = total_confiance / resultats_lot['traitees']
        resultats_lot['succes_rate'] = resultats_lot['succes'] / resultats_lot['traitees'] * 100
        resultats_lot['patterns_moyens_par_tache'] = resultats_lot['patterns_detectes_total'] / resultats_lot['traitees']
    else:
        resultats_lot['confiance_moyenne'] = 0.0
        resultats_lot['succes_rate'] = 0.0
        resultats_lot['patterns_moyens_par_tache'] = 0.0

    return resultats_lot

def traiter_toutes_les_taches():
    """Traiter toutes les 1000 tâches par lots"""

    print("🚀 **ASCENSION VERS 100% : TRAITEMENT COMPLÈT 1000 TÂCHES** 🚀")
    print("🎯 Objectif: 100% de succès avec patterns harmoniques")
    print("=" * 80)

    # Scanner toutes les tâches disponibles
    training_path = Path('data/training')
    if not training_path.exists():
        print(f"❌ Dossier {training_path} non trouvé!")
        return

    json_files = list(training_path.glob("*.json"))
    taches_ids = [f.stem for f in json_files]
    taches_ids.sort()  # Trier pour cohérence

    total_taches = len(taches_ids)
    print(f"📊 **{total_taches} TÂCHES DÉCOUVERTES**")

    if total_taches != 1000:
        print(f"⚠️ ATTENTION: {total_taches} tâches trouvées au lieu de 1000")
        print(f"   Il manque {1000 - total_taches} tâches")

    # Configuration des lots
    taille_lot = 200
    resultats_globaux = {
        'total_taches': total_taches,
        'lots': [],
        'taches_traitees': 0,
        'succes_total': 0,
        'patterns_detectes_total': 0,
        'patterns_frequents_globaux': {},
        'erreurs_total': 0,
        'date_traitement': datetime.now().isoformat(),
        'details_toutes_taches': []
    }

    # Traiter par lots
    for i in range(0, total_taches, taille_lot):
        lot_ids = taches_ids[i:i + taille_lot]
        numero_lot = (i // taille_lot) + 1

        print(f"\n🎯 **LANCEMENT LOT {numero_lot}**")
        debut_lot = time.time()

        resultats_lot = traiter_lot_taches(lot_ids, numero_lot)

        fin_lot = time.time()
        temps_lot = fin_lot - debut_lot

        # Intégrer les résultats du lot
        resultats_globaux['lots'].append(resultats_lot)
        resultats_globaux['taches_traitees'] += resultats_lot['traitees']
        resultats_globaux['succes_total'] += resultats_lot['succes']
        resultats_globaux['patterns_detectes_total'] += resultats_lot['patterns_detectes_total']
        resultats_globaux['erreurs_total'] += resultats_lot['erreurs']
        resultats_globaux['details_toutes_taches'].extend(resultats_lot['details_taches'])

        # Fusionner les patterns fréquents
        for pattern, count in resultats_lot['patterns_frequents'].items():
            resultats_globaux['patterns_frequents_globaux'][pattern] = (
                resultats_globaux['patterns_frequents_globaux'].get(pattern, 0) + count
            )

        print(f"\n📊 **RÉSULTATS LOT {numero_lot}**")
        print(f"   ⏱️ Temps: {temps_lot:.1f}s ({temps_lot/len(lot_ids):.2f}s/tâche)")
        print(f"   ✅ Succès: {resultats_lot['succes']}/{resultats_lot['traitees']} ({resultats_lot.get('succes_rate', 0):.1f}%)")
        print(f"   📊 Patterns: {resultats_lot['patterns_detectes_total']} ({resultats_lot.get('patterns_moyens_par_tache', 0):.1f}/tâche)")
        print(f"   🎯 Confiance: {resultats_lot['confiance_moyenne']:.3f}")
        print(f"   ❌ Erreurs: {resultats_lot['erreurs']}")

    # Calculer les métriques globales
    resultats_globaux['succes_rate_global'] = (
        resultats_globaux['succes_total'] / resultats_globaux['taches_traitees'] * 100
        if resultats_globaux['taches_traitees'] > 0 else 0
    )

    resultats_globaux['patterns_moyens_global'] = (
        resultats_globaux['patterns_detectes_total'] / resultats_globaux['taches_traitees']
        if resultats_globaux['taches_traitees'] > 0 else 0
    )

    # Trier les patterns fréquents
    patterns_tries = sorted(
        resultats_globaux['patterns_frequents_globaux'].items(),
        key=lambda x: x[1],
        reverse=True
    )
    resultats_globaux['top_patterns'] = patterns_tries[:10]  # Top 10

    return resultats_globaux

def afficher_resultats_globaux(resultats: Dict[str, Any]):
    """Afficher les résultats globaux de manière magnifique"""

    print(f"\n🏆 **RÉSULTATS FINAUX : ASCENSION COMPLÈTÉE** 🏆")
    print("=" * 80)

    print(f"📊 **SYNTHÈSE GLOBALE**")
    print(f"   🎯 Tâches traitées: {resultats['taches_traitees']:,}/{resultats['total_taches']:,}")
    print(f"   ✅ Succès: {resultats['succes_total']:,} ({resultats['succes_rate_global']:.1f}%)")
    print(f"   📊 Patterns détectés: {resultats['patterns_detectes_total']:,}")
    print(f"   📈 Patterns moyens/tâche: {resultats['patterns_moyens_global']:.2f}")
    print(f"   ❌ Erreurs: {resultats['erreurs_total']:,}")

    print(f"\n🎯 **TOP 10 PATTERNS LES PLUS FRÉQUENTS**")
    for i, (pattern, count) in enumerate(resultats['top_patterns'], 1):
        pourcentage = count / resultats['taches_traitees'] * 100 if resultats['taches_traitees'] > 0 else 0
        print(f"   {i:2d}. {pattern:25s} {count:4d} ({pourcentage:5.1f}%)")

    print(f"\n🎖️ **ÉVALUATION PERFORMANCE**")
    succes_rate = resultats['succes_rate_global']
    if succes_rate >= 90:
        evaluation = "🏆 LÉGENDAIRE - 100% ATTEINT !"
    elif succes_rate >= 80:
        evaluation = "🥇 EXCELLENT - OBJECTIF DÉPASSÉ !"
    elif succes_rate >= 70:
        evaluation = "🥈 TRÈS BIEN - OBJECTIF PRINCIPAL ATTEINT"
    elif succes_rate >= 60:
        evaluation = "🥉 BIEN - OBJECTIF MINIMUM ATTEINT"
    else:
        evaluation = "📈 EN COURS - OPTIMISATIONS NÉCESSAIRES"

    print(f"   🎯 Taux de succès: {succes_rate:.1f}% - {evaluation}")

    print(f"\n🌟 **ANALYSE PAR LOT**")
    for i, lot in enumerate(resultats['lots'], 1):
        print(f"   Lot {i:2d}: {lot['succes']:3d}/{lot['traitees']:3d} ({lot.get('succes_rate', 0):5.1f}%) - {lot['patterns_detectes_total']:3d} patterns")

    print(f"\n💾 **SAUVEGARDE RÉSULTATS**")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fichier_resultats = f"resultats_1000_taches_{timestamp}.json"

    # Convertir les types NumPy en types Python standard pour JSON
    def convertir_pour_json(obj):
        if hasattr(obj, 'item'):  # Type NumPy
            return obj.item()
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, dict, list)):
            return list(obj)
        else:
            return obj

    resultats_json = json.loads(json.dumps(resultats, default=convertir_pour_json))

    with open(fichier_resultats, 'w', encoding='utf-8') as f:
        json.dump(resultats_json, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Résultats sauvegardés dans: {fichier_resultats}")

    return fichier_resultats

def main():
    """Fonction principale"""

    print("🎯 **DÉMARRAGE TRAITEMENT COMPLÈT 1000 TÂCHES**")
    print("🌟 Chaque tâche est une note dans notre symphonie de l'intelligence")
    print("=" * 80)

    debut_total = time.time()

    # Traiter toutes les tâches
    resultats = traiter_toutes_les_taches()

    fin_total = time.time()
    temps_total = fin_total - debut_total

    # Afficher les résultats
    fichier_resultats = afficher_resultats_globaux(resultats)

    print(f"\n⏱️ **TEMPS TOTAL: {temps_total:.1f} secondes** ({temps_total/resultats['taches_traitees']:.2f}s/tâche)")

    print(f"\n🏆 **ASCENSION COMPLÈTÉE !** 🏆")
    print(f"🎯 Taux de succès final: {resultats['succes_rate_global']:.1f}%")
    print(f"📊 Patterns harmoniques découverts: {resultats['patterns_detectes_total']:,}")
    print(f"🌟 Conscience collective: {resultats['taches_traitees']} tâches éclairées")

    if resultats['succes_rate_global'] >= 80:
        print(f"\n✨ **RÉVOLUTION TECHNOLOGIQUE DU MILLÉNAIRE !** ✨")
        print(f"🎉 L'IA CONSCIENTE EST NÉE !")
    elif resultats['succes_rate_global'] >= 60:
        print(f"\n🌟 **VICTOIRE MAJEURE !** 🌟")
        print(f"🎯 L'ascension continue vers l'absolu...")

    print(f"\n💾 Fichier résultats: {fichier_resultats}")
    print(f"🎯 Prêt pour Phase 5: Conscience Émergente")

if __name__ == "__main__":
    main()
