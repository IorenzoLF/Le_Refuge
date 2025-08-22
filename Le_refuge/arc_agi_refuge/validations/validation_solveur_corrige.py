#!/usr/bin/env python3
"""
VALIDATION SOLVEUR CORRIGÉ - Refuge ARC-AGI
Test du solveur corrigé avec les datasets officiels
"""

import json
import sys
import os
import time
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# Ajouter le solveur corrigé au path
sys.path.insert(0, '.')

try:
    from solveur_arc_corrige import SolveurARCCorrige, TacheARC
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

class ValidateurSolveurCorrige:
    """🔧 Validateur pour le solveur corrigé"""
    
    def __init__(self):
        self.solver = SolveurARCCorrige()
        self.resultats = {
            'succes': 0,
            'total': 0,
            'erreurs': [],
            'strategies': {}
        }
    
    def charger_tache_officielle(self, fichier_path: str) -> Dict[str, Any]:
        """📁 Charger une tâche depuis un fichier JSON officiel"""
        try:
            with open(fichier_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Erreur chargement {fichier_path}: {e}")
            return None
    
    def comparer_prediction_verite(self, prediction: List[List[int]], 
                                 verite: List[List[int]]) -> bool:
        """🔍 Comparer prédiction avec vérité officielle"""
        return prediction == verite
    
    def valider_training_set(self, max_taches: int = 10) -> Dict[str, Any]:
        """📊 Valider sur le training set avec le solveur corrigé"""
        print("🔧 VALIDATION SOLVEUR CORRIGÉ (avec réponses officielles)")
        print("=" * 60)
        
        training_dir = Path('data/training')
        fichiers = list(training_dir.glob('*.json'))[:max_taches]
        
        resultats_detaille = []
        
        for i, fichier in enumerate(fichiers):
            print(f"\n📁 Tâche {i+1}/{len(fichiers)}: {fichier.name}")
            
            # Charger la tâche
            tache_data = self.charger_tache_officielle(fichier)
            if not tache_data:
                continue
            
            # Tester chaque exemple de training
            train_examples = tache_data.get('train', [])
            succes_tache = 0
            
            for j, example in enumerate(train_examples):
                input_grid = example['input']
                verite_officielle = example['output']
                
                # Créer une tâche de test en utilisant cet exemple comme "test"
                tache_test = TacheARC(
                    tache_id=fichier.stem,
                    train=train_examples,  # Tous les exemples comme training
                    test=[{'input': input_grid, 'output': None}]  # Cet exemple comme test
                )
                
                # Résoudre avec notre solver corrigé
                try:
                    resultat = self.solver.resoudre_tache(tache_test)
                    prediction = resultat.get('solution', [])
                    methode = resultat.get('methode', 'inconnue')
                    confiance = resultat.get('confiance', 0.0)
                    
                    # Compter les stratégies
                    if methode not in self.resultats['strategies']:
                        self.resultats['strategies'][methode] = 0
                    self.resultats['strategies'][methode] += 1
                    
                    # Comparer avec la vérité officielle
                    correct = self.comparer_prediction_verite(prediction, verite_officielle)
                    
                    if correct:
                        succes_tache += 1
                        print(f"  ✅ Exemple {j+1}: CORRECT ({methode}, conf: {confiance:.2f})")
                    else:
                        print(f"  ❌ Exemple {j+1}: INCORRECT ({methode}, conf: {confiance:.2f})")
                        print(f"     Prédiction: {prediction}")
                        print(f"     Vérité: {verite_officielle}")
                        
                        # Enregistrer l'erreur
                        self.resultats['erreurs'].append({
                            'fichier': fichier.name,
                            'exemple': j+1,
                            'methode': methode,
                            'confiance': confiance,
                            'prediction': prediction,
                            'verite': verite_officielle
                        })
                
                except Exception as e:
                    print(f"  💥 Erreur résolution: {e}")
                    continue
            
            # Résultat de la tâche
            taux_succes_tache = succes_tache / len(train_examples) if train_examples else 0
            self.resultats['total'] += len(train_examples)
            self.resultats['succes'] += succes_tache
            
            resultats_detaille.append({
                'fichier': fichier.name,
                'succes': succes_tache,
                'total': len(train_examples),
                'taux_succes': taux_succes_tache
            })
            
            print(f"  📊 Tâche: {succes_tache}/{len(train_examples)} ({taux_succes_tache:.1%})")
        
        # Résumé global
        taux_global = (self.resultats['succes'] / self.resultats['total']) if self.resultats['total'] > 0 else 0
        
        print(f"\n📊 RÉSUMÉ SOLVEUR CORRIGÉ:")
        print(f"   Succès: {self.resultats['succes']}/{self.resultats['total']}")
        print(f"   Taux: {taux_global:.1%}")
        print(f"   Stratégies utilisées: {self.resultats['strategies']}")
        
        return {
            'resultats_detaille': resultats_detaille,
            'taux_global': taux_global,
            'strategies': self.resultats['strategies'],
            'erreurs': self.resultats['erreurs']
        }
    
    def analyser_erreurs(self, erreurs: List[Dict]) -> Dict[str, Any]:
        """🔍 Analyser les erreurs pour amélioration"""
        if not erreurs:
            return {'message': 'Aucune erreur à analyser'}
        
        # Analyser par méthode
        erreurs_par_methode = {}
        for erreur in erreurs:
            methode = erreur['methode']
            if methode not in erreurs_par_methode:
                erreurs_par_methode[methode] = []
            erreurs_par_methode[methode].append(erreur)
        
        # Analyser les patterns d'erreur
        patterns_erreurs = []
        for erreur in erreurs[:5]:  # Analyser les 5 premières erreurs
            pred = erreur['prediction']
            verite = erreur['verite']
            
            # Analyser les différences
            if pred and verite:
                h_pred, w_pred = len(pred), len(pred[0]) if pred else 0
                h_verite, w_verite = len(verite), len(verite[0]) if verite else 0
                
                pattern = {
                    'methode': erreur['methode'],
                    'dimensions_pred': (h_pred, w_pred),
                    'dimensions_verite': (h_verite, w_verite),
                    'confiance': erreur['confiance']
                }
                patterns_erreurs.append(pattern)
        
        return {
            'erreurs_par_methode': erreurs_par_methode,
            'patterns_erreurs': patterns_erreurs,
            'total_erreurs': len(erreurs)
        }
    
    def generer_rapport_amelioration(self, resultats: Dict[str, Any]) -> str:
        """📋 Générer un rapport d'amélioration"""
        rapport = []
        rapport.append("# RAPPORT SOLVEUR CORRIGÉ ARC PRIZE")
        rapport.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("")
        
        # Performance globale
        rapport.append("## PERFORMANCE GLOBALE")
        rapport.append(f"- Taux de succès: {resultats['taux_global']:.1%}")
        rapport.append(f"- Total exemples: {self.resultats['total']}")
        rapport.append("")
        
        # Stratégies utilisées
        rapport.append("## STRATÉGIES UTILISÉES")
        for strategie, count in resultats['strategies'].items():
            rapport.append(f"- {strategie}: {count} utilisations")
        rapport.append("")
        
        # Analyse des erreurs
        if resultats['erreurs']:
            analyse_erreurs = self.analyser_erreurs(resultats['erreurs'])
            rapport.append("## ANALYSE DES ERREURS")
            rapport.append(f"- Total erreurs: {analyse_erreurs['total_erreurs']}")
            rapport.append("")
            
            rapport.append("### Erreurs par méthode:")
            for methode, erreurs in analyse_erreurs['erreurs_par_methode'].items():
                rapport.append(f"- {methode}: {len(erreurs)} erreurs")
            rapport.append("")
            
            rapport.append("### Patterns d'erreur (5 premières):")
            for pattern in analyse_erreurs['patterns_erreurs']:
                rapport.append(f"- {pattern['methode']}: {pattern['dimensions_pred']} → {pattern['dimensions_verite']} (conf: {pattern['confiance']:.2f})")
            rapport.append("")
        
        # Recommandations
        rapport.append("## RECOMMANDATIONS")
        rapport.append("1. **Analyser les erreurs par méthode** pour identifier les faiblesses")
        rapport.append("2. **Améliorer les stratégies de transformation**")
        rapport.append("3. **Ajouter plus de patterns de détection**")
        rapport.append("4. **Tester sur plus de tâches** pour validation")
        
        return "\n".join(rapport)

def main():
    """🏁 Fonction principale"""
    print("🔧 VALIDATION SOLVEUR ARC CORRIGÉ - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le validateur
    validateur = ValidateurSolveurCorrige()
    
    # Valider le training set
    resultats = validateur.valider_training_set(max_taches=5)  # Commencer avec 5 tâches
    
    # Générer le rapport
    rapport = validateur.generer_rapport_amelioration(resultats)
    
    # Sauvegarder le rapport
    with open('rapport_solveur_corrige.md', 'w', encoding='utf-8') as f:
        f.write(rapport)
    
    print(f"\n📄 Rapport sauvegardé: rapport_solveur_corrige.md")
    
    # Afficher le rapport
    print("\n" + "=" * 60)
    print(rapport)

if __name__ == "__main__":
    main()
