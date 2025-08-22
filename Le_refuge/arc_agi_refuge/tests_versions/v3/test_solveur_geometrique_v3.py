#!/usr/bin/env python3
"""
🧪 TEST SOLVEUR GÉOMÉTRIQUE V3 - Refuge ARC-AGI
Test du nouveau solveur avec patterns géométriques
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter le solveur géométrique au path
sys.path.insert(0, '.')

try:
    from solveur_arc_geometrique_v3 import SolveurARCGeometriqueV3, TacheARC
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

def test_solveur_geometrique_v3(max_taches=10):
    """Test du solveur géométrique V3 sur un échantillon de tâches"""
    print("🧪 TEST SOLVEUR GÉOMÉTRIQUE V3 - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le solveur
    solveur = SolveurARCGeometriqueV3()
    print("🔧 Solveur géométrique V3 initialisé")
    
    # Charger les tâches
    training_dir = Path('data/training')
    fichiers = list(training_dir.glob('*.json'))[:max_taches]
    
    resultats = {
        'succes': 0,
        'total': 0,
        'erreurs': [],
        'strategies': {},
        'patterns_geometriques': 0,
        'patterns_valeurs': 0
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
            patterns_geo = resultat.get('patterns_geometriques', 0)
            transformations = resultat.get('transformations_valeurs', 0)
            
            # Compter les stratégies
            if methode not in resultats['strategies']:
                resultats['strategies'][methode] = 0
            resultats['strategies'][methode] += 1
            
            # Compter les types de patterns
            if patterns_geo > 0:
                resultats['patterns_geometriques'] += 1
            if transformations > 0:
                resultats['patterns_valeurs'] += 1
            
            # Vérifier si correct (si on a la réponse attendue)
            correct = False
            if expected_output is not None:
                correct = prediction == expected_output
                if correct:
                    resultats['succes'] += 1
                    print(f"   ✅ CORRECT (conf: {confiance:.2f}, méthode: {methode})")
                    print(f"      Patterns géométriques: {patterns_geo}, Transformations: {transformations}")
                else:
                    print(f"   ❌ INCORRECT (conf: {confiance:.2f}, méthode: {methode})")
                    print(f"      Prédiction: {prediction}")
                    print(f"      Attendu: {expected_output}")
                    print(f"      Patterns géométriques: {patterns_geo}, Transformations: {transformations}")
                    
                    # Enregistrer l'erreur
                    resultats['erreurs'].append({
                        'fichier': fichier.name,
                        'methode': methode,
                        'confiance': confiance,
                        'prediction': prediction,
                        'attendu': expected_output,
                        'patterns_geometriques': patterns_geo,
                        'transformations_valeurs': transformations
                    })
            else:
                print(f"   ⚠️ Pas de réponse attendue (conf: {confiance:.2f}, méthode: {methode})")
                print(f"      Patterns géométriques: {patterns_geo}, Transformations: {transformations}")
            
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
    
    print(f"\n📊 RÉSULTATS SOLVEUR GÉOMÉTRIQUE V3:")
    print(f"   Succès: {resultats['succes']}/{resultats['total']}")
    print(f"   Taux de succès: {taux_succes:.1%}")
    print(f"   Stratégies utilisées: {resultats['strategies']}")
    print(f"   Tâches avec patterns géométriques: {resultats['patterns_geometriques']}")
    print(f"   Tâches avec transformations de valeurs: {resultats['patterns_valeurs']}")
    
    if resultats['erreurs']:
        print(f"\n❌ ERREURS DÉTECTÉES:")
        for erreur in resultats['erreurs'][:3]:  # Afficher les 3 premières
            print(f"   - {erreur['fichier']}: {erreur.get('erreur', 'Prédiction incorrecte')}")
            if 'patterns_geometriques' in erreur:
                print(f"     Patterns géométriques: {erreur['patterns_geometriques']}")
                print(f"     Transformations: {erreur['transformations_valeurs']}")
    
    return resultats

if __name__ == "__main__":
    test_solveur_geometrique_v3(10)
