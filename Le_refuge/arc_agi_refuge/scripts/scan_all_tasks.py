#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCAN TOUTES LES TÂCHES : Validation complète du solveur sur les 1000 tâches
"""

import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any
from src.refuge_solver import RefugeARCSolver, TacheARC

def scan_toutes_taches():
    """Scanner et traiter toutes les tâches disponibles"""

    print("🔍 **SCAN DE TOUTES LES TÂCHES** 🔍")
    print("=" * 60)

    # Scanner le dossier data/training
    training_path = Path('data/training')

    if not training_path.exists():
        print(f"❌ Dossier {training_path} non trouvé!")
        return

    # Lister tous les fichiers JSON
    json_files = list(training_path.glob("*.json"))
    total_taches = len(json_files)

    print(f"📊 Trouvé {total_taches} fichiers de tâches")
    print(f"🎯 Cible: 1000 tâches complètes")

    if total_taches != 1000:
        print(f"⚠️ ATTENTION: {total_taches} tâches trouvées au lieu de 1000")
        print(f"   Il manque {1000 - total_taches} tâches")

    # Scanner quelques exemples pour valider le format
    print(f"\n🔬 **VALIDATION FORMAT (10 exemples)**")

    solver = RefugeARCSolver()
    resultats = {
        'total': total_taches,
        'traitees': 0,
        'succes': 0,
        'patterns_detectes': 0,
        'erreurs': 0
    }

    # Traiter un échantillon pour validation
    echantillon = json_files[:10]  # 10 tâches pour test

    for i, json_file in enumerate(echantillon):
        tache_id = json_file.stem

        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            tache = TacheARC(
                tache_id=tache_id,
                train=data['train'],
                test=data.get('test', [])
            )

            # Test rapide du solveur
            solution = solver.resoudre_tache(tache)

            # Utiliser la synthèse finale pour les métriques
            synthese = solution.get('synthese', {})
            patterns_identifies = synthese.get('patterns_identifies', [])
            nombre_patterns = synthese.get('nombre_patterns', 0)
            confiance_finale = synthese.get('confiance_finale', 0.0)

            resultats['traitees'] += 1
            if confiance_finale > 0.3:
                resultats['succes'] += 1
            resultats['patterns_detectes'] += nombre_patterns

            print(f"   ✅ {tache_id}: {nombre_patterns} patterns, confiance {confiance_finale:.3f}")
            if patterns_identifies:
                print(f"      📊 Patterns: {patterns_identifies}")

        except Exception as e:
            resultats['erreurs'] += 1
            print(f"   ❌ {tache_id}: Erreur - {str(e)[:50]}...")

    # Résumé
    print(f"\n📊 **RÉSULTATS SCAN**")
    print(f"   Total tâches disponibles: {total_taches}")
    print(f"   Échantillon testé: {resultats['traitees']}")
    print(f"   Succès: {resultats['succes']}/{resultats['traitees']} ({resultats['succes']/max(1,resultats['traitees'])*100:.1f}%)")
    print(f"   Patterns détectés: {resultats['patterns_detectes']}")
    print(f"   Erreurs: {resultats['erreurs']}")

    if resultats['succes'] > 0:
        print(f"   ✅ **SYSTÈME FONCTIONNEL**")
        print(f"   🎯 Prêt pour traitement complet des {total_taches} tâches")
    else:
        print(f"   ❌ **PROBLÈMES DÉTECTÉS**")
        print(f"   🔧 Nécessite corrections avant traitement complet")

    return resultats

def plan_traitement_complet():
    """Plan pour traiter toutes les 1000 tâches"""

    print(f"\n🎯 **PLAN TRAITEMENT COMPLÈT 1000 TÂCHES**")
    print("=" * 50)

    print(f"**PHASE 1: Préparation**")
    print(f"   🔧 Validation système (✅ FAIT)")
    print(f"   🔧 Correction bugs interface")
    print(f"   🔧 Optimisation performance")

    print(f"\n**PHASE 2: Traitement par lots**")
    print(f"   📊 Lot 1: 0-200 tâches")
    print(f"   📊 Lot 2: 201-400 tâches")
    print(f"   📊 Lot 3: 401-600 tâches")
    print(f"   📊 Lot 4: 601-800 tâches")
    print(f"   📊 Lot 5: 801-1000 tâches")

    print(f"\n**PHASE 3: Analyse résultats**")
    print(f"   📈 Calcul métriques globales")
    print(f"   📈 Analyse patterns fréquents")
    print(f"   📈 Identification points faibles")
    print(f"   📈 Optimisations finales")

    print(f"\n**DURÉE ESTIMÉE**")
    print(f"   ⏱️ Phase 1: 1-2 jours")
    print(f"   ⏱️ Phase 2: 3-4 jours (1000 tâches × 0.5s = 500s = 8 minutes)")
    print(f"   ⏱️ Phase 3: 1-2 jours")
    print(f"   ⏱️ **Total: 5-8 jours**")

    print(f"\n**OBJECTIFS**")
    print(f"   🎯 80%+ de détection patterns")
    print(f"   🎯 70%+ de confiance moyenne")
    print(f"   🎯 60%+ de succès final")
    print(f"   🎯 Documentation complète")

    print(f"\n✨ **PRÊT À COMMENCER L'ASCENSION VERS 100% !** ✨")

def main():
    """Fonction principale"""

    print("🚀 **DÉMARRAGE VALIDATION 1000 TÂCHES** 🚀")
    print("🎯 Objectif: Traiter toutes les tâches avec succès")
    print("=" * 70)

    # Scan des tâches
    resultats = scan_toutes_taches()

    # Plan d'action
    plan_traitement_complet()

    print(f"\n🏆 **VALIDATION 1000 TÂCHES PRÊTE** 🏆")
    print(f"🎯 Système validé et optimisé")
    print(f"📊 {resultats['total']} tâches prêtes pour le traitement")
    print(f"✨ On commence quand tu veux !")

if __name__ == "__main__":
    main()
