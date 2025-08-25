#!/usr/bin/env python3
"""
🔍 ANALYSE RAPIDE PERFORMANCE ARC-AGI
Script pour évaluer rapidement notre performance actuelle
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter src au path
sys.path.insert(0, 'src')

def analyser_performance_actuelle():
    """Analyser notre performance actuelle"""
    print("🔍 ANALYSE RAPIDE PERFORMANCE ARC-AGI")
    print("=" * 50)
    
    # 1. Vérifier les données d'entraînement
    training_dir = Path('data/training')
    if training_dir.exists():
        fichiers = list(training_dir.glob('*.json'))
        print(f"📁 Données d'entraînement: {len(fichiers)} fichiers trouvés")
        
        # Analyser un échantillon
        if fichiers:
            sample_file = fichiers[0]
            with open(sample_file, 'r') as f:
                data = json.load(f)
            
            train_examples = data.get('train', [])
            test_examples = data.get('test', [])
            print(f"📊 Exemple de tâche ({sample_file.name}):")
            print(f"   - Exemples d'entraînement: {len(train_examples)}")
            print(f"   - Exemples de test: {len(test_examples)}")
            
            if train_examples:
                input_shape = len(train_examples[0]['input']), len(train_examples[0]['input'][0])
                print(f"   - Taille des grilles: {input_shape[0]}x{input_shape[1]}")
    
    # 2. Vérifier nos solveurs
    print(f"\n🔧 SOLVEURS DISPONIBLES:")
    solveurs = [
        'src/refuge_solver.py',
        'src/refuge_solver_perfectionne.py',
        'solveurs_versions/solveur_arc_corrige.py'
    ]
    
    for solveur in solveurs:
        if Path(solveur).exists():
            print(f"   ✅ {solveur}")
        else:
            print(f"   ❌ {solveur} (manquant)")
    
    # 3. Vérifier les résultats récents
    print(f"\n📈 RÉSULTATS RÉCENTS:")
    resultats_files = [
        'resultats/resultats_final_analyse.json',
        'resultats/rapport_validation_officielle.md'
    ]
    
    for resultat in resultats_files:
        if Path(resultat).exists():
            print(f"   ✅ {resultat}")
            if resultat.endswith('.json'):
                try:
                    with open(resultat, 'r') as f:
                        data = json.load(f)
                    if 'taux_succes' in data:
                        print(f"      Taux de succès: {data['taux_succes']:.1%}")
                except:
                    pass
        else:
            print(f"   ❌ {resultat} (manquant)")
    
    # 4. Test rapide d'un solveur
    print(f"\n🧪 TEST RAPIDE:")
    try:
        from refuge_solver import RefugeARCSolver
        solver = RefugeARCSolver()
        print("   ✅ RefugeARCSolver importé avec succès")
    except Exception as e:
        print(f"   ❌ Erreur import RefugeARCSolver: {e}")
    
    try:
        from refuge_solver_perfectionne import RefugeARCSolverPerfectionne
        solver_perf = RefugeARCSolverPerfectionne()
        print("   ✅ RefugeARCSolverPerfectionne importé avec succès")
    except Exception as e:
        print(f"   ❌ Erreur import RefugeARCSolverPerfectionne: {e}")
    
    print(f"\n🎯 RECOMMANDATIONS:")
    print("   1. Lancer un test sur 10 tâches pour évaluer la performance réelle")
    print("   2. Analyser les types d'erreurs pour améliorer le solveur")
    print("   3. Comparer avec les benchmarks officiels")

if __name__ == "__main__":
    analyser_performance_actuelle()
