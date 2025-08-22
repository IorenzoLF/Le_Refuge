#!/usr/bin/env python3
"""
🧪 TEST SOLVEUR PERFECTIONNÉ V5 - Refuge ARC-AGI
Test du nouveau solveur avec corrections et améliorations
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter le solveur perfectionné au path
sys.path.insert(0, '.')

try:
    from solveur_arc_perfectionne_v5 import SolveurARCPerfectionneV5, TacheARC
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

def test_solveur_perfectionne_v5(max_taches=10):
    """Test du solveur perfectionné V5 sur un échantillon de tâches"""
    print("🧪 TEST SOLVEUR PERFECTIONNÉ V5 - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le solveur
    solveur = SolveurARCPerfectionneV5()
    print("🔧 Solveur perfectionné V5 initialisé")
    
    # Charger les tâches
    training_dir = Path('data/training')
    fichiers = list(training_dir.glob('*.json'))[:max_taches]
    
    resultats = {
        'succes': 0,
        'total': 0,
        'erreurs': [],
        'strategies': {},
        'analyses_effectuees': 0,
        'patterns_complexes': 0,
        'corrections_appliquees': 0
    }
    
    print(f"📁 Test sur {len(fichiers)} tâches...")
    
    for i, fichier in enumerate(fichiers):
        print(f"\n🔍 Tâche {i+1}/{len(fichiers)}: {fichier.name}")
        
        try:
            # Charger la tâche
            with open(fichier, 'r') as f:
                tache_data = json.load(f)
            
            train_examples = tache_data.get('train', [])
            test_examples = tache_data.get('test', [])
            
            if not train_examples or not test_examples:
                print(f"   ⚠️ Tâche incomplète, ignorée")
                continue
            
            # Tester sur le premier exemple de test
            test_example = test_examples[0]
            input_grid = test_example['input']
            expected_output = test_example.get('output', None)
            
            # Créer la tâche ARC
            tache = TacheARC(
                tache_id=fichier.stem,
                train=train_examples,
                test=[{'input': input_grid, 'output': expected_output}]
            )
            
            # Résoudre
            resultat = solveur.resoudre_tache(tache)
            prediction = resultat.get('solution', [])
            confiance = resultat.get('confiance', 0.0)
            methode = resultat.get('methode', 'inconnue')
            analyses = resultat.get('analyses_effectuees', 0)
            pattern_detecte = resultat.get('pattern_detecte', {})
            
            # Compter les stratégies
            if methode not in resultats['strategies']:
                resultats['strategies'][methode] = 0
            resultats['strategies'][methode] += 1
            
            # Compter les analyses et patterns complexes
            if analyses > 0:
                resultats['analyses_effectuees'] += 1
            if pattern_detecte.get('score_total', 0) > 1.0:
                resultats['patterns_complexes'] += 1
            
            # Vérifier si la solution contient des None (problème corrigé)
            contient_none = any(any(val is None for val in ligne) for ligne in prediction) if prediction else False
            if not contient_none and methode == 'transformation':
                resultats['corrections_appliquees'] += 1
            
            # Vérifier si correct (si on a la réponse attendue)
            correct = False
            if expected_output is not None:
                correct = prediction == expected_output
                if correct:
                    resultats['succes'] += 1
                    print(f"   ✅ CORRECT (conf: {confiance:.2f}, méthode: {methode})")
                    print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                    if not contient_none and methode == 'transformation':
                        print(f"      ✅ Correction appliquée (pas de None)")
                else:
                    print(f"   ❌ INCORRECT (conf: {confiance:.2f}, méthode: {methode})")
                    print(f"      Prédiction: {prediction}")
                    print(f"      Attendu: {expected_output}")
                    print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                    if contient_none:
                        print(f"      ⚠️ Contient encore des None")
                    elif not contient_none and methode == 'transformation':
                        print(f"      ✅ Correction appliquée (pas de None)")
                    
                    # Enregistrer l'erreur
                    resultats['erreurs'].append({
                        'fichier': fichier.name,
                        'methode': methode,
                        'confiance': confiance,
                        'prediction': prediction,
                        'attendu': expected_output,
                        'analyses': analyses,
                        'pattern_detecte': pattern_detecte,
                        'contient_none': contient_none
                    })
            else:
                print(f"   ⚠️ Pas de réponse attendue (conf: {confiance:.2f}, méthode: {methode})")
                print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                if not contient_none and methode == 'transformation':
                    print(f"      ✅ Correction appliquée (pas de None)")
            
            resultats['total'] += 1
            
        except Exception as e:
            print(f"   💥 Erreur: {e}")
            resultats['erreurs'].append({
                'fichier': fichier.name,
                'erreur': str(e)
            })
            continue
    
    # Résumé
    taux_succes = (resultats['succes'] / resultats['total']) if resultats['total'] > 0 else 0
    
    print(f"\n📊 RÉSULTATS SOLVEUR PERFECTIONNÉ V5:")
    print(f"   Succès: {resultats['succes']}/{resultats['total']}")
    print(f"   Taux de succès: {taux_succes:.1%}")
    print(f"   Stratégies utilisées: {resultats['strategies']}")
    print(f"   Tâches avec analyses: {resultats['analyses_effectuees']}")
    print(f"   Patterns complexes détectés: {resultats['patterns_complexes']}")
    print(f"   Corrections appliquées: {resultats['corrections_appliquees']}")
    
    if resultats['erreurs']:
        print(f"\n❌ ERREURS DÉTECTÉES:")
        for erreur in resultats['erreurs'][:3]:  # Afficher les 3 premières
            print(f"   - {erreur['fichier']}: {erreur.get('erreur', 'Prédiction incorrecte')}")
            if 'analyses' in erreur:
                print(f"     Analyses: {erreur['analyses']}")
                print(f"     Pattern: {erreur['pattern_detecte'].get('type', 'inconnu')}")
                if 'contient_none' in erreur:
                    print(f"     Contient None: {erreur['contient_none']}")
    
    return resultats

if __name__ == "__main__":
    test_solveur_perfectionne_v5(10)
