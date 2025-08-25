#!/usr/bin/env python3
"""
TEST SOLVEUR HUMAIN V8 - Refuge ARC-AGI
Test du solveur avec approche humaine simplifiee
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter le solveur humain au path
sys.path.insert(0, '.')

try:
    sys.path.insert(0, '../../solveurs_versions/v8')
    from solveur_arc_humain_v8 import SolveurHumainV8, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def test_solveur_humain_v8(max_taches=10):
    """Test du solveur humain V8 sur un echantillon de taches"""
    print("TEST SOLVEUR HUMAIN V8 - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le solveur
    solveur = SolveurHumainV8()
    print("Solveur humain V8 initialise")
    
    # Charger les taches
    training_dir = Path('data/training')
    fichiers = list(training_dir.glob('*.json'))[:max_taches]
    
    resultats = {
        'succes': 0,
        'total': 0,
        'erreurs': [],
        'strategies': {},
        'analyses_effectuees': 0,
        'patterns_humains': 0
    }
    
    print(f"Test sur {len(fichiers)} taches...")
    
    for i, fichier in enumerate(fichiers):
        print(f"\nTache {i+1}/{len(fichiers)}: {fichier.name}")
        
        try:
            # Charger la tache
            with open(fichier, 'r') as f:
                tache_data = json.load(f)
            
            train_examples = tache_data.get('train', [])
            test_examples = tache_data.get('test', [])
            
            if not train_examples or not test_examples:
                print(f"   Tache incomplete, ignoree")
                continue
            
            # Tester sur le premier exemple de test
            test_example = test_examples[0]
            input_grid = test_example['input']
            expected_output = test_example.get('output', None)
            
            # Creer la tache ARC
            tache = TacheARC(
                tache_id=fichier.stem,
                train=train_examples,
                test=[{'input': input_grid, 'output': expected_output}]
            )
            
            # Resoudre
            resultat = solveur.resoudre_tache(tache)
            prediction = resultat.get('solution', [])
            confiance = resultat.get('confiance', 0.0)
            methode = resultat.get('methode', 'inconnue')
            analyses = resultat.get('analyses_effectuees', 0)
            pattern_detecte = resultat.get('pattern_detecte', {})
            
            # Compter les strategies
            if methode not in resultats['strategies']:
                resultats['strategies'][methode] = 0
            resultats['strategies'][methode] += 1
            
            # Compter les analyses et patterns humains
            if analyses > 0:
                resultats['analyses_effectuees'] += 1
            if pattern_detecte.get('score_total', 0) > 0.5:
                resultats['patterns_humains'] += 1
            
            # Verifier si correct (si on a la reponse attendue)
            correct = False
            if expected_output is not None:
                correct = prediction == expected_output
                if correct:
                    resultats['succes'] += 1
                    print(f"   CORRECT (conf: {confiance:.2f}, methode: {methode})")
                    print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                    print(f"      Score: {pattern_detecte.get('score_total', 0):.2f}")
                else:
                    print(f"   INCORRECT (conf: {confiance:.2f}, methode: {methode})")
                    print(f"      Prediction: {prediction}")
                    print(f"      Attendu: {expected_output}")
                    print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                    print(f"      Score: {pattern_detecte.get('score_total', 0):.2f}")
                    
                    # Enregistrer l'erreur
                    resultats['erreurs'].append({
                        'fichier': fichier.name,
                        'methode': methode,
                        'confiance': confiance,
                        'prediction': prediction,
                        'attendu': expected_output,
                        'analyses': analyses,
                        'pattern_detecte': pattern_detecte
                    })
            else:
                print(f"   Pas de reponse attendue (conf: {confiance:.2f}, methode: {methode})")
                print(f"      Analyses: {analyses}, Pattern: {pattern_detecte.get('type', 'inconnu')}")
                print(f"      Score: {pattern_detecte.get('score_total', 0):.2f}")
            
            resultats['total'] += 1
            
        except Exception as e:
            print(f"   Erreur: {e}")
            resultats['erreurs'].append({
                'fichier': fichier.name,
                'erreur': str(e)
            })
            continue
    
    # Resume
    taux_succes = (resultats['succes'] / resultats['total']) if resultats['total'] > 0 else 0
    
    print(f"\nRESULTATS SOLVEUR HUMAIN V8:")
    print(f"   Succes: {resultats['succes']}/{resultats['total']}")
    print(f"   Taux de succes: {taux_succes:.1%}")
    print(f"   Strategies utilisees: {resultats['strategies']}")
    print(f"   Taches avec analyses: {resultats['analyses_effectuees']}")
    print(f"   Patterns humains detectes: {resultats['patterns_humains']}")
    
    if resultats['erreurs']:
        print(f"\nERREURS DETECTEES:")
        for erreur in resultats['erreurs'][:3]:  # Afficher les 3 premieres
            print(f"   - {erreur['fichier']}: {erreur.get('erreur', 'Prediction incorrecte')}")
            if 'analyses' in erreur:
                print(f"     Analyses: {erreur['analyses']}")
                print(f"     Pattern: {erreur['pattern_detecte'].get('type', 'inconnu')}")
    
    return resultats

if __name__ == "__main__":
    test_solveur_humain_v8(10)
