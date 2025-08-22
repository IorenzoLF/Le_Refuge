#!/usr/bin/env python3
"""
🧪 TEST SOLVEUR CORRIGÉ V2 - Refuge ARC-AGI
Test du nouveau solveur qui utilise réellement les patterns détectés
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Ajouter le solveur corrigé au path
sys.path.insert(0, '.')

try:
    from solveur_arc_corrige_v2 import SolveurARCCorrigeV2, TacheARC
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

def test_solveur_corrige_v2(max_taches=10):
    """Test du solveur corrigé V2 sur un échantillon de tâches"""
    print("🧪 TEST SOLVEUR CORRIGÉ V2 - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le solveur
    solveur = SolveurARCCorrigeV2()
    print("🔧 Solveur corrigé V2 initialisé")
    
    # Charger les tâches
    training_dir = Path('data/training')
    fichiers = list(training_dir.glob('*.json'))[:max_taches]
    
    resultats = {
        'succes': 0,
        'total': 0,
        'erreurs': [],
        'strategies': {}
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
            
            # Compter les stratégies
            if methode not in resultats['strategies']:
                resultats['strategies'][methode] = 0
            resultats['strategies'][methode] += 1
            
            # Vérifier si correct (si on a la réponse attendue)
            correct = False
            if expected_output is not None:
                correct = prediction == expected_output
                if correct:
                    resultats['succes'] += 1
                    print(f"   ✅ CORRECT (conf: {confiance:.2f}, méthode: {methode})")
                else:
                    print(f"   ❌ INCORRECT (conf: {confiance:.2f}, méthode: {methode})")
                    print(f"      Prédiction: {prediction}")
                    print(f"      Attendu: {expected_output}")
                    
                    # Enregistrer l'erreur
                    resultats['erreurs'].append({
                        'fichier': fichier.name,
                        'methode': methode,
                        'confiance': confiance,
                        'prediction': prediction,
                        'attendu': expected_output
                    })
            else:
                print(f"   ⚠️ Pas de réponse attendue (conf: {confiance:.2f}, méthode: {methode})")
            
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
    
    print(f"\n📊 RÉSULTATS SOLVEUR CORRIGÉ V2:")
    print(f"   Succès: {resultats['succes']}/{resultats['total']}")
    print(f"   Taux de succès: {taux_succes:.1%}")
    print(f"   Stratégies utilisées: {resultats['strategies']}")
    
    if resultats['erreurs']:
        print(f"\n❌ ERREURS DÉTECTÉES:")
        for erreur in resultats['erreurs'][:3]:  # Afficher les 3 premières
            print(f"   - {erreur['fichier']}: {erreur.get('erreur', 'Prédiction incorrecte')}")
    
    return resultats

if __name__ == "__main__":
    test_solveur_corrige_v2(10)
