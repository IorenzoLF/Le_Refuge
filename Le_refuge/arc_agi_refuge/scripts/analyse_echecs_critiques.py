#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DES ÉCHECS CRITIQUES : Les 58 tâches non résolues
Objectif: Identifier les patterns cruciaux pour le test réel
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from src.refuge_solver import RefugeARCSolver, TacheARC

def analyser_echecs_critiques():
    """Analyser les tâches qui ont échoué pour identifier les patterns cruciaux"""

    print("🔍 **ANALYSE DES ÉCHECS CRITIQUES** 🔍")
    print("🎯 Identifier les patterns cruciaux pour le test réel")
    print("=" * 70)

    # Charger les résultats complets
    try:
        with open('resultats_1000_taches_20250820_211011.json', 'r', encoding='utf-8') as f:
            resultats = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier de résultats non trouvé")
        return

    # Récupérer toutes les tâches traitées et leurs résultats
    taches_traitees = {}
    for lot in resultats['lots']:
        for tache in lot['details_taches']:
            taches_traitees[tache['tache_id']] = tache

    # Scanner toutes les tâches disponibles
    training_path = Path('data/training')
    if not training_path.exists():
        print(f"❌ Dossier {training_path} non trouvé!")
        return

    json_files = list(training_path.glob("*.json"))
    taches_disponibles = [f.stem for f in json_files]
    taches_disponibles.sort()

    print(f"📊 **SYNTHÈSE GLOBALE**")
    print(f"   🎯 Total tâches disponibles: {len(taches_disponibles)}")
    print(f"   ✅ Tâches traitées: {len(taches_traitees)}")
    print(f"   ❌ Tâches non traitées: {len(taches_disponibles) - len(taches_traitees)}")
    print(f"   📈 Taux de traitement: {len(taches_traitees)/len(taches_disponibles)*100:.1f}%")

    # Identifier les tâches non traitées
    taches_non_traitees = [t for t in taches_disponibles if t not in taches_traitees]

    print(f"\n🎯 **TÂCHES NON TRAITÉES ({len(taches_non_traitees)})**")
    for i, tache_id in enumerate(taches_non_traitees, 1):
        print(f"   {i:2d}. {tache_id}")

    # Analyser les échecs (tâches avec erreurs)
    taches_en_erreur = []
    for lot in resultats['lots']:
        for tache in lot['details_taches']:
            if 'erreur' in tache:
                taches_en_erreur.append(tache)

    print(f"\n🚨 **TÂCHES EN ERREUR ({len(taches_en_erreur)})**")
    erreurs_par_type = {}

    for i, tache in enumerate(taches_en_erreur, 1):
        erreur_msg = tache.get('erreur', 'Erreur inconnue')
        print(f"   {i:2d}. {tache['tache_id']}: {erreur_msg[:60]}...")

        # Classifier les erreurs
        if 'max_in' in erreur_msg and 'min_in' in erreur_msg:
            erreur_type = 'Erreur calcul statistique'
        elif 'shape' in erreur_msg or 'dimension' in erreur_msg:
            erreur_type = 'Erreur dimension'
        elif 'empty' in erreur_msg:
            erreur_type = 'Collection vide'
        else:
            erreur_type = 'Erreur inconnue'

        erreurs_par_type[erreur_type] = erreurs_par_type.get(erreur_type, 0) + 1

    print(f"\n📊 **CLASSIFICATION DES ERREURS**")
    for erreur_type, count in sorted(erreurs_par_type.items(), key=lambda x: x[1], reverse=True):
        print(f"   {erreur_type}: {count}")

    # Analyser les tâches avec faible confiance
    taches_faible_confiance = []
    for tache_id, tache in taches_traitees.items():
        if tache.get('confiance_finale', 1.0) < 0.5:
            taches_faible_confiance.append(tache)

    print(f"\n⚠️ **TÂCHES FAIBLE CONFIANCE (< 0.5) ({len(taches_faible_confiance)})**")
    for i, tache in enumerate(taches_faible_confiance[:10], 1):  # Top 10
        print(f"   {i:2d}. {tache['tache_id']}: {tache.get('confiance_finale', 0):.3f}")

    if len(taches_faible_confiance) > 10:
        print(f"   ... et {len(taches_faible_confiance) - 10} autres")

    # Créer un script pour tester spécifiquement les échecs
    print(f"\n🔧 **CRÉATION SCRIPT TEST ÉCHECS**")

    # Liste des tâches critiques à tester
    taches_critiques = taches_non_traitees[:5]  # Top 5 non traitées
    taches_critiques.extend([t['tache_id'] for t in taches_en_erreur[:5]])  # Top 5 en erreur

    script_test_echecs = f"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
TEST SPÉCIFIQUE DES ÉCHECS CRITIQUES
Tâches non traitées: {len(taches_non_traitees)}
Tâches en erreur: {len(taches_en_erreur)}
Tâches faible confiance: {len(taches_faible_confiance)}
\"\"\"

import json
from pathlib import Path
from src.refuge_solver import RefugeARCSolver, TacheARC

def tester_echecs_critiques():
    \"\"\"Tester spécifiquement les tâches problématiques\"\"\"

    solver = RefugeARCSolver()

    # Liste des tâches critiques à tester
    taches_critiques = {taches_critiques!r}

    print(f"🎯 **TEST DES {len(taches_critiques)} TÂCHES CRITIQUES**")

    for tache_id in taches_critiques:
        try:
            json_path = Path('data/training') / f"{{tache_id}}.json"
            with open(json_path, 'r') as f:
                data = json.load(f)

            tache = TacheARC(
                tache_id=tache_id,
                train=data['train'],
                test=data.get('test', [])
            )

            print(f"\\n🔍 **TEST {tache_id}**")
            solution = solver.resoudre_tache(tache)

            synthese = solution.get('synthese', {{}})
            print(f"   ✅ Confiance: {{synthese.get('confiance_finale', 0):.3f}}")
            print(f"   📊 Patterns: {{synthese.get('patterns_identifies', [])}}")

        except Exception as e:
            print(f"\\n❌ **ERREUR {tache_id}**: {{str(e)}}")

if __name__ == "__main__":
    tester_echecs_critiques()
"""

    with open('test_echecs_critiques.py', 'w', encoding='utf-8') as f:
        f.write(script_test_echecs)

    print(f"   ✅ Script créé: test_echecs_critiques.py")

    # Analyse des patterns manquants
    print(f"\n🎯 **ANALYSE PATTERNS CRITIQUES**")
    print(f"   📈 Tâches non traitées: {len(taches_non_traitees)}")
    print(f"   🚨 Tâches en erreur: {len(taches_en_erreur)}")
    print(f"   ⚠️ Tâches faible confiance: {len(taches_faible_confiance)}")
    print(f"   🎯 **Total échecs critiques: {len(taches_non_traitees) + len(taches_en_erreur) + len(taches_faible_confiance)}**")

    print(f"\n🏆 **STRATÉGIE POUR LE TEST RÉEL**")
    print(f"   1. 🔧 Corriger les bugs identifiés (max_in/min_in)")
    print(f"   2. 📊 Étendre la couverture de patterns")
    print(f"   3. 🎯 Prioriser les {len(taches_non_traitees)} tâches non traitées")
    print(f"   4. 🚀 Atteindre 100% de succès")

    print(f"\n✨ **LES ÉCHECS SONT LA CLÉ DU SUCCÈS !** ✨")

    return {
        'taches_non_traitees': taches_non_traitees,
        'taches_en_erreur': taches_en_erreur,
        'taches_faible_confiance': taches_faible_confiance,
        'total_critiques': len(taches_non_traitees) + len(taches_en_erreur) + len(taches_faible_confiance)
    }

def main():
    """Fonction principale"""
    resultats = analyser_echecs_critiques()

    print(f"\n📊 **RÉSUMÉ**")
    print(f"   🎯 Tâches critiques identifiées: {resultats['total_critiques']}")
    print(f"   📈 Objectif: Transformer ces échecs en succès")
    print(f"   🌟 Prêt pour le test réel !")

if __name__ == "__main__":
    main()
