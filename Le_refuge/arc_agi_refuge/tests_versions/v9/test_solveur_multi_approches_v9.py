#!/usr/bin/env python3
"""
TEST SOLVEUR MULTI-APPROCHES V9 - Refuge ARC-AGI
Test du solveur avec plusieurs approches pour patterns complexes
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter le solveur multi-approches au path
sys.path.insert(0, '../../solveurs_versions/v9')

try:
    from solveur_arc_multi_approches_v9 import SolveurMultiApprochesV9, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def test_solveur_multi_approches_v9(max_taches=10):
    """Test du solveur multi-approches V9 sur un echantillon de taches"""
    print("TEST SOLVEUR MULTI-APPROCHES V9 - Refuge ARC-AGI")
    print("=" * 70)
    
    # Initialiser le solveur
    solveur = SolveurMultiApprochesV9()
    print("Solveur multi-approches V9 initialise")
    
    # Charger les taches
    training_dir = Path('ARC-AGI-2-main/data/training')
    fichiers = list(training_dir.glob('*.json'))[:max_taches]
    
    resultats = {
        'succes': 0,
        'total': 0,
        'erreurs': [],
        'approches_gagnantes': {},
        'patterns_detectes': 0,
        'validations_reussies': 0
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
            approches_testees = resultat.get('approches_testees', 0)
            patterns_detectes = resultat.get('patterns_detectes', {})
            validation = resultat.get('validation', {})
            
            # Compter les approches gagnantes
            if methode not in resultats['approches_gagnantes']:
                resultats['approches_gagnantes'][methode] = 0
            resultats['approches_gagnantes'][methode] += 1
            
            # Compter les patterns et validations
            if patterns_detectes:
                resultats['patterns_detectes'] += 1
            if validation.get('valide', False):
                resultats['validations_reussies'] += 1
            
            # Verifier si correct (si on a la reponse attendue)
            correct = False
            if expected_output is not None:
                correct = prediction == expected_output
                if correct:
                    resultats['succes'] += 1
                    print(f"   CORRECT (conf: {confiance:.2f}, methode: {methode})")
                    print(f"      Approches testees: {approches_testees}")
                    print(f"      Patterns detectes: {patterns_detectes.get('type_deploiement', 'inconnu')}")
                    print(f"      Validation: {validation.get('valide', False)}")
                else:
                    print(f"   INCORRECT (conf: {confiance:.2f}, methode: {methode})")
                    print(f"      Prediction: {prediction}")
                    print(f"      Attendu: {expected_output}")
                    print(f"      Approches testees: {approches_testees}")
                    print(f"      Patterns detectes: {patterns_detectes.get('type_deploiement', 'inconnu')}")
                    print(f"      Validation: {validation}")
                    
                    # Enregistrer l'erreur
                    resultats['erreurs'].append({
                        'fichier': fichier.name,
                        'methode': methode,
                        'confiance': confiance,
                        'prediction': prediction,
                        'attendu': expected_output,
                        'approches_testees': approches_testees,
                        'patterns_detectes': patterns_detectes,
                        'validation': validation
                    })
            else:
                print(f"   Pas de reponse attendue (conf: {confiance:.2f}, methode: {methode})")
                print(f"      Approches testees: {approches_testees}")
                print(f"      Patterns detectes: {patterns_detectes.get('type_deploiement', 'inconnu')}")
                print(f"      Validation: {validation}")
            
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
    
    print(f"\nRESULTATS SOLVEUR MULTI-APPROCHES V9:")
    print(f"   Succes: {resultats['succes']}/{resultats['total']}")
    print(f"   Taux de succes: {taux_succes:.1%}")
    print(f"   Approches gagnantes: {resultats['approches_gagnantes']}")
    print(f"   Taches avec patterns detectes: {resultats['patterns_detectes']}")
    print(f"   Validations reussies: {resultats['validations_reussies']}")
    
    if resultats['erreurs']:
        print(f"\nERREURS DETECTEES:")
        for erreur in resultats['erreurs'][:3]:  # Afficher les 3 premieres
            print(f"   - {erreur['fichier']}: {erreur.get('erreur', 'Prediction incorrecte')}")
            if 'approches_testees' in erreur:
                print(f"     Approches testees: {erreur['approches_testees']}")
                print(f"     Methode: {erreur['methode']}")
                print(f"     Patterns: {erreur['patterns_detectes'].get('type_deploiement', 'inconnu')}")
    
    return resultats

def test_puzzle_specifique(puzzle_id='007bbfb7'):
    """Test specifique sur un puzzle"""
    print(f"TEST SPECIFIQUE - Puzzle {puzzle_id}")
    print("=" * 50)
    
    # Charger le puzzle
    puzzle_file = Path(f'ARC-AGI-2-main/data/training/{puzzle_id}.json')
    
    if not puzzle_file.exists():
        print(f"Puzzle {puzzle_id} non trouve")
        return
    
    with open(puzzle_file, 'r') as f:
        tache_data = json.load(f)
    
    # Creer la tache
    tache = TacheARC(
        tache_id=puzzle_id,
        train=tache_data['train'],
        test=tache_data['test']
    )
    
    # Tester avec le solveur V9
    solveur = SolveurMultiApprochesV9()
    resultat = solveur.resoudre_tache(tache)
    
    print(f"RESULTAT POUR {puzzle_id}:")
    print(f"   Solution: {resultat['solution']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Approches testees: {resultat['approches_testees']}")
    print(f"   Patterns detectes: {resultat['patterns_detectes']}")
    print(f"   Validation: {resultat['validation']}")
    
    # Verifier si correct
    expected = tache_data['test'][0].get('output')
    if expected:
        correct = resultat['solution'] == expected
        print(f"   Correct: {correct}")

if __name__ == "__main__":
    # Test specifique sur 007bbfb7
    test_puzzle_specifique('007bbfb7')
    
    print("\n" + "="*70)
    
    # Test general
    test_solveur_multi_approches_v9(5)
