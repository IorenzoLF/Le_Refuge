#!/usr/bin/env python3
"""
VALIDATION SOLVEUR AMÉLIORÉ - Refuge ARC-AGI
Test du solveur amélioré avec comparaison des performances
"""

import json
import sys
import os
import time
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# Ajouter les solveurs au path
sys.path.insert(0, '.')

try:
    from solveur_arc_corrige import SolveurARCCorrige, TacheARC
    from solveur_arc_ameliore import SolveurARCAmeliore
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

class ValidateurSolveurAmeliore:
    """🔧 Validateur pour le solveur amélioré avec comparaison"""
    
    def __init__(self):
        self.solver_corrige = SolveurARCCorrige()
        self.solver_ameliore = SolveurARCAmeliore()
        self.resultats = {
            'corrige': {'succes': 0, 'total': 0, 'erreurs': [], 'strategies': {}},
            'ameliore': {'succes': 0, 'total': 0, 'erreurs': [], 'strategies': {}}
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
    
    def valider_comparaison(self, max_taches: int = 5) -> Dict[str, Any]:
        """📊 Valider et comparer les deux solveurs"""
        print("🔧 VALIDATION COMPARAISON SOLVEURS")
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
            succes_corrige = 0
            succes_ameliore = 0
            
            for j, example in enumerate(train_examples):
                input_grid = example['input']
                verite_officielle = example['output']
                
                # Créer une tâche de test
                tache_test = TacheARC(
                    tache_id=fichier.stem,
                    train=train_examples,
                    test=[{'input': input_grid, 'output': None}]
                )
                
                # Test avec le solveur corrigé
                try:
                    resultat_corrige = self.solver_corrige.resoudre_tache(tache_test)
                    prediction_corrige = resultat_corrige.get('solution', [])
                    methode_corrige = resultat_corrige.get('methode', 'inconnue')
                    confiance_corrige = resultat_corrige.get('confiance', 0.0)
                    
                    # Compter les stratégies
                    if methode_corrige not in self.resultats['corrige']['strategies']:
                        self.resultats['corrige']['strategies'][methode_corrige] = 0
                    self.resultats['corrige']['strategies'][methode_corrige] += 1
                    
                    # Comparer avec la vérité officielle
                    correct_corrige = self.comparer_prediction_verite(prediction_corrige, verite_officielle)
                    
                    if correct_corrige:
                        succes_corrige += 1
                        print(f"  ✅ Corrigé Exemple {j+1}: CORRECT ({methode_corrige}, conf: {confiance_corrige:.2f})")
                    else:
                        print(f"  ❌ Corrigé Exemple {j+1}: INCORRECT ({methode_corrige}, conf: {confiance_corrige:.2f})")
                        
                        # Enregistrer l'erreur
                        self.resultats['corrige']['erreurs'].append({
                            'fichier': fichier.name,
                            'exemple': j+1,
                            'methode': methode_corrige,
                            'confiance': confiance_corrige,
                            'prediction': prediction_corrige,
                            'verite': verite_officielle
                        })
                
                except Exception as e:
                    print(f"  💥 Erreur solveur corrigé: {e}")
                
                # Test avec le solveur amélioré
                try:
                    resultat_ameliore = self.solver_ameliore.resoudre_tache(tache_test)
                    prediction_ameliore = resultat_ameliore.get('solution', [])
                    methode_ameliore = resultat_ameliore.get('methode', 'inconnue')
                    confiance_ameliore = resultat_ameliore.get('confiance', 0.0)
                    
                    # Compter les stratégies
                    if methode_ameliore not in self.resultats['ameliore']['strategies']:
                        self.resultats['ameliore']['strategies'][methode_ameliore] = 0
                    self.resultats['ameliore']['strategies'][methode_ameliore] += 1
                    
                    # Comparer avec la vérité officielle
                    correct_ameliore = self.comparer_prediction_verite(prediction_ameliore, verite_officielle)
                    
                    if correct_ameliore:
                        succes_ameliore += 1
                        print(f"  ✅ Amélioré Exemple {j+1}: CORRECT ({methode_ameliore}, conf: {confiance_ameliore:.2f})")
                    else:
                        print(f"  ❌ Amélioré Exemple {j+1}: INCORRECT ({methode_ameliore}, conf: {confiance_ameliore:.2f})")
                        
                        # Enregistrer l'erreur
                        self.resultats['ameliore']['erreurs'].append({
                            'fichier': fichier.name,
                            'exemple': j+1,
                            'methode': methode_ameliore,
                            'confiance': confiance_ameliore,
                            'prediction': prediction_ameliore,
                            'verite': verite_officielle
                        })
                
                except Exception as e:
                    print(f"  💥 Erreur solveur amélioré: {e}")
            
            # Résultats de la tâche
            taux_succes_corrige = succes_corrige / len(train_examples) if train_examples else 0
            taux_succes_ameliore = succes_ameliore / len(train_examples) if train_examples else 0
            
            self.resultats['corrige']['total'] += len(train_examples)
            self.resultats['corrige']['succes'] += succes_corrige
            self.resultats['ameliore']['total'] += len(train_examples)
            self.resultats['ameliore']['succes'] += succes_ameliore
            
            resultats_detaille.append({
                'fichier': fichier.name,
                'corrige': {'succes': succes_corrige, 'total': len(train_examples), 'taux': taux_succes_corrige},
                'ameliore': {'succes': succes_ameliore, 'total': len(train_examples), 'taux': taux_succes_ameliore}
            })
            
            print(f"  📊 Tâche - Corrigé: {succes_corrige}/{len(train_examples)} ({taux_succes_corrige:.1%})")
            print(f"  📊 Tâche - Amélioré: {succes_ameliore}/{len(train_examples)} ({taux_succes_ameliore:.1%})")
        
        # Résumé global
        taux_global_corrige = (self.resultats['corrige']['succes'] / self.resultats['corrige']['total']) if self.resultats['corrige']['total'] > 0 else 0
        taux_global_ameliore = (self.resultats['ameliore']['succes'] / self.resultats['ameliore']['total']) if self.resultats['ameliore']['total'] > 0 else 0
        
        print(f"\n📊 RÉSUMÉ COMPARAISON:")
        print(f"   Corrigé: {self.resultats['corrige']['succes']}/{self.resultats['corrige']['total']} ({taux_global_corrige:.1%})")
        print(f"   Amélioré: {self.resultats['ameliore']['succes']}/{self.resultats['ameliore']['total']} ({taux_global_ameliore:.1%})")
        print(f"   Amélioration: {((taux_global_ameliore - taux_global_corrige) / taux_global_corrige * 100):+.1f}%" if taux_global_corrige > 0 else "N/A")
        print(f"   Stratégies Corrigé: {self.resultats['corrige']['strategies']}")
        print(f"   Stratégies Amélioré: {self.resultats['ameliore']['strategies']}")
        
        return {
            'resultats_detaille': resultats_detaille,
            'taux_global_corrige': taux_global_corrige,
            'taux_global_ameliore': taux_global_ameliore,
            'strategies_corrige': self.resultats['corrige']['strategies'],
            'strategies_ameliore': self.resultats['ameliore']['strategies'],
            'erreurs_corrige': self.resultats['corrige']['erreurs'],
            'erreurs_ameliore': self.resultats['ameliore']['erreurs']
        }
    
    def analyser_ameliorations(self, resultats: Dict[str, Any]) -> Dict[str, Any]:
        """🔍 Analyser les améliorations apportées"""
        ameliorations = {}
        
        # Comparaison des taux de succès
        taux_corrige = resultats['taux_global_corrige']
        taux_ameliore = resultats['taux_global_ameliore']
        
        if taux_corrige > 0:
            amelioration_relative = (taux_ameliore - taux_corrige) / taux_corrige * 100
            ameliorations['taux_succes'] = {
                'corrige': taux_corrige,
                'ameliore': taux_ameliore,
                'amelioration_relative': amelioration_relative
            }
        
        # Comparaison des stratégies
        strategies_corrige = resultats['strategies_corrige']
        strategies_ameliore = resultats['strategies_ameliore']
        
        ameliorations['strategies'] = {
            'corrige': strategies_corrige,
            'ameliore': strategies_ameliore,
            'nouvelles_strategies': set(strategies_ameliore.keys()) - set(strategies_corrige.keys())
        }
        
        # Analyse des erreurs
        erreurs_corrige = resultats['erreurs_corrige']
        erreurs_ameliore = resultats['erreurs_ameliore']
        
        ameliorations['erreurs'] = {
            'corrige': len(erreurs_corrige),
            'ameliore': len(erreurs_ameliore),
            'reduction_erreurs': len(erreurs_corrige) - len(erreurs_ameliore)
        }
        
        return ameliorations
    
    def generer_rapport_comparaison(self, resultats: Dict[str, Any]) -> str:
        """📋 Générer un rapport de comparaison"""
        rapport = []
        rapport.append("# RAPPORT COMPARAISON SOLVEURS ARC PRIZE")
        rapport.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("")
        
        # Performance globale
        rapport.append("## PERFORMANCE GLOBALE")
        rapport.append(f"- **Solveur Corrigé**: {resultats['taux_global_corrige']:.1%}")
        rapport.append(f"- **Solveur Amélioré**: {resultats['taux_global_ameliore']:.1%}")
        
        if resultats['taux_global_corrige'] > 0:
            amelioration = ((resultats['taux_global_ameliore'] - resultats['taux_global_corrige']) / resultats['taux_global_corrige'] * 100)
            rapport.append(f"- **Amélioration**: {amelioration:+.1f}%")
        rapport.append("")
        
        # Stratégies utilisées
        rapport.append("## STRATÉGIES UTILISÉES")
        rapport.append("### Solveur Corrigé:")
        for strategie, count in resultats['strategies_corrige'].items():
            rapport.append(f"- {strategie}: {count} utilisations")
        rapport.append("")
        
        rapport.append("### Solveur Amélioré:")
        for strategie, count in resultats['strategies_ameliore'].items():
            rapport.append(f"- {strategie}: {count} utilisations")
        rapport.append("")
        
        # Analyse des erreurs
        rapport.append("## ANALYSE DES ERREURS")
        rapport.append(f"- **Erreurs Corrigé**: {len(resultats['erreurs_corrige'])}")
        rapport.append(f"- **Erreurs Amélioré**: {len(resultats['erreurs_ameliore'])}")
        rapport.append(f"- **Réduction**: {len(resultats['erreurs_corrige']) - len(resultats['erreurs_ameliore'])} erreurs")
        rapport.append("")
        
        # Recommandations
        rapport.append("## RECOMMANDATIONS")
        if resultats['taux_global_ameliore'] > resultats['taux_global_corrige']:
            rapport.append("✅ **Le solveur amélioré montre des progrès**")
            rapport.append("1. **Continuer l'amélioration** des patterns géométriques")
            rapport.append("2. **Ajouter plus de stratégies** de transformation")
            rapport.append("3. **Tester sur plus de tâches** pour validation")
        else:
            rapport.append("⚠️ **Le solveur amélioré n'a pas encore montré d'amélioration**")
            rapport.append("1. **Analyser les erreurs spécifiques** du solveur amélioré")
            rapport.append("2. **Ajuster les stratégies** de détection")
            rapport.append("3. **Améliorer l'analyse positionnelle**")
        
        return "\n".join(rapport)

def main():
    """🏁 Fonction principale"""
    print("🔧 VALIDATION COMPARAISON SOLVEURS - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le validateur
    validateur = ValidateurSolveurAmeliore()
    
    # Valider et comparer
    resultats = validateur.valider_comparaison(max_taches=3)  # Commencer avec 3 tâches
    
    # Analyser les améliorations
    ameliorations = validateur.analyser_ameliorations(resultats)
    
    # Générer le rapport
    rapport = validateur.generer_rapport_comparaison(resultats)
    
    # Sauvegarder le rapport
    with open('rapport_comparaison_solveurs.md', 'w', encoding='utf-8') as f:
        f.write(rapport)
    
    print(f"\n📄 Rapport sauvegardé: rapport_comparaison_solveurs.md")
    
    # Afficher le rapport
    print("\n" + "=" * 60)
    print(rapport)

if __name__ == "__main__":
    main()
