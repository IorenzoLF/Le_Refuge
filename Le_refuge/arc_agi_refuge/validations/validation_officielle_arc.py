#!/usr/bin/env python3
"""
VALIDATION OFFICIELLE ARC PRIZE - Refuge ARC-AGI
Suivant les directives de Paul et Ælya/GPT

1. Utiliser les datasets officiels (JSON + réponses)
2. Comparer visuellement nos prédictions avec les vraies réponses
3. Améliorer itérativement en ciblant un type de puzzle à la fois
4. Tester sur le test set avant soumission
"""

import json
import sys
import os
import time
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ajouter src au path
sys.path.insert(0, 'src')

try:
    from refuge_solver_perfectionne import RefugeARCSolverPerfectionne, TacheARC
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

class ValidateurOfficielARC:
    """🔍 Validateur officiel pour le concours ARC Prize"""
    
    def __init__(self):
        self.solver = RefugeARCSolverPerfectionne()
        self.resultats = {
            'training': {'succes': 0, 'total': 0, 'erreurs': []},
            'test': {'succes': 0, 'total': 0, 'erreurs': []}
        }
        self.types_puzzles = {
            'repetition': 0,
            'symetrie': 0,
            'filtrage': 0,
            'expansion': 0,
            'reduction': 0,
            'transformation': 0,
            'conditionnel': 0,
            'complexe': 0
        }
    
    def charger_tache_officielle(self, fichier_path: str) -> Dict[str, Any]:
        """📁 Charger une tâche depuis un fichier JSON officiel"""
        try:
            with open(fichier_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Erreur chargement {fichier_path}: {e}")
            return None
    
    def visualiser_comparaison(self, input_grid: List[List[int]], 
                             prediction: List[List[int]], 
                             verite: Optional[List[List[int]]] = None,
                             titre: str = "Comparaison Prédiction vs Vérité"):
        """🎨 Visualiser la comparaison prédiction vs vérité"""
        fig, axes = plt.subplots(1, 3 if verite else 2, figsize=(12, 4))
        
        # Input
        axes[0].imshow(input_grid, cmap='tab10', interpolation='nearest')
        axes[0].set_title('Input')
        axes[0].axis('off')
        
        # Prédiction
        axes[1].imshow(prediction, cmap='tab10', interpolation='nearest')
        axes[1].set_title('Prédiction')
        axes[1].axis('off')
        
        # Vérité (si disponible)
        if verite:
            axes[2].imshow(verite, cmap='tab10', interpolation='nearest')
            axes[2].set_title('Vérité')
            axes[2].axis('off')
            
            # Vérifier si la prédiction est correcte
            if prediction == verite:
                fig.suptitle(f"✅ {titre} - CORRECT", color='green')
            else:
                fig.suptitle(f"❌ {titre} - INCORRECT", color='red')
        else:
            fig.suptitle(titre)
        
        plt.tight_layout()
        return fig
    
    def comparer_prediction_verite(self, prediction: List[List[int]], 
                                 verite: List[List[int]]) -> bool:
        """🔍 Comparer prédiction avec vérité officielle"""
        return prediction == verite
    
    def analyser_type_puzzle(self, tache: Dict[str, Any]) -> str:
        """🔍 Analyser le type de puzzle basé sur les patterns"""
        train_examples = tache.get('train', [])
        if not train_examples:
            return 'inconnu'
        
        # Analyser les transformations entre input et output
        transformations = []
        for example in train_examples:
            input_grid = np.array(example['input'])
            output_grid = np.array(example['output'])
            
            # Détecter le type de transformation
            if input_grid.shape == output_grid.shape:
                if np.array_equal(input_grid, output_grid):
                    transformations.append('repetition')
                else:
                    transformations.append('transformation')
            elif output_grid.size < input_grid.size:
                transformations.append('reduction')
            else:
                transformations.append('expansion')
        
        # Déterminer le type principal
        if len(set(transformations)) == 1:
            return transformations[0]
        else:
            return 'complexe'
    
    def valider_training_set(self, max_taches: int = 50) -> Dict[str, Any]:
        """📊 Valider sur le training set avec comparaison visuelle"""
        print("🔍 VALIDATION TRAINING SET (avec réponses officielles)")
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
            
            # Analyser le type de puzzle
            type_puzzle = self.analyser_type_puzzle(tache_data)
            self.types_puzzles[type_puzzle] += 1
            
            # Tester chaque exemple de training
            train_examples = tache_data.get('train', [])
            succes_tache = 0
            
            for j, example in enumerate(train_examples):
                input_grid = example['input']
                verite_officielle = example['output']
                
                # Créer l'objet TacheARC
                tache_obj = TacheARC(
                    tache_id=fichier.stem,
                    train=[example],
                    test=[]
                )
                
                # Résoudre avec notre solver
                try:
                    resultat = self.solver.resoudre_tache(tache_obj)
                    prediction = resultat.get('solution', [])
                    
                    # Comparer avec la vérité officielle
                    correct = self.comparer_prediction_verite(prediction, verite_officielle)
                    
                    if correct:
                        succes_tache += 1
                        print(f"  ✅ Exemple {j+1}: CORRECT")
                    else:
                        print(f"  ❌ Exemple {j+1}: INCORRECT")
                        print(f"     Prédiction: {prediction}")
                        print(f"     Vérité: {verite_officielle}")
                        
                        # Visualiser l'erreur
                        fig = self.visualiser_comparaison(
                            input_grid, prediction, verite_officielle,
                            f"Tâche {fichier.name} - Exemple {j+1}"
                        )
                        plt.savefig(f'erreur_{fichier.stem}_ex{j+1}.png')
                        plt.close()
                
                except Exception as e:
                    print(f"  💥 Erreur résolution: {e}")
                    continue
            
            # Résultat de la tâche
            taux_succes_tache = succes_tache / len(train_examples) if train_examples else 0
            self.resultats['training']['total'] += len(train_examples)
            self.resultats['training']['succes'] += succes_tache
            
            resultats_detaille.append({
                'fichier': fichier.name,
                'type_puzzle': type_puzzle,
                'succes': succes_tache,
                'total': len(train_examples),
                'taux_succes': taux_succes_tache
            })
            
            print(f"  📊 Tâche: {succes_tache}/{len(train_examples)} ({taux_succes_tache:.1%})")
        
        # Résumé global
        taux_global = (self.resultats['training']['succes'] / 
                      self.resultats['training']['total']) if self.resultats['training']['total'] > 0 else 0
        
        print(f"\n📊 RÉSUMÉ TRAINING SET:")
        print(f"   Succès: {self.resultats['training']['succes']}/{self.resultats['training']['total']}")
        print(f"   Taux: {taux_global:.1%}")
        print(f"   Types de puzzles: {self.types_puzzles}")
        
        return {
            'resultats_detaille': resultats_detaille,
            'taux_global': taux_global,
            'types_puzzles': self.types_puzzles
        }
    
    def identifier_erreurs_critiques(self, resultats_detaille: List[Dict]) -> List[Dict]:
        """🎯 Identifier les erreurs critiques pour amélioration ciblée"""
        erreurs_critiques = []
        
        for resultat in resultats_detaille:
            if resultat['taux_succes'] < 0.5:  # Moins de 50% de succès
                erreurs_critiques.append({
                    'fichier': resultat['fichier'],
                    'type_puzzle': resultat['type_puzzle'],
                    'taux_succes': resultat['taux_succes'],
                    'priorite': 'HAUTE' if resultat['taux_succes'] < 0.2 else 'MOYENNE'
                })
        
        return sorted(erreurs_critiques, key=lambda x: x['taux_succes'])
    
    def generer_rapport_amelioration(self, resultats: Dict[str, Any]) -> str:
        """📋 Générer un rapport d'amélioration ciblée"""
        rapport = []
        rapport.append("# RAPPORT D'AMÉLIORATION ARC PRIZE")
        rapport.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("")
        
        # Performance globale
        rapport.append("## PERFORMANCE GLOBALE")
        rapport.append(f"- Taux de succès: {resultats['taux_global']:.1%}")
        rapport.append(f"- Total exemples: {self.resultats['training']['total']}")
        rapport.append("")
        
        # Types de puzzles
        rapport.append("## RÉPARTITION PAR TYPE DE PUZZLE")
        for type_puzzle, count in resultats['types_puzzles'].items():
            rapport.append(f"- {type_puzzle}: {count} tâches")
        rapport.append("")
        
        # Erreurs critiques
        erreurs_critiques = self.identifier_erreurs_critiques(resultats['resultats_detaille'])
        if erreurs_critiques:
            rapport.append("## ERREURS CRITIQUES À CORRIGER")
            rapport.append("Priorité d'amélioration (cibler un type à la fois):")
            for erreur in erreurs_critiques[:10]:  # Top 10
                rapport.append(f"- {erreur['fichier']} ({erreur['type_puzzle']}): {erreur['taux_succes']:.1%} - {erreur['priorite']}")
        rapport.append("")
        
        # Recommandations
        rapport.append("## RECOMMANDATIONS")
        rapport.append("1. **Cibler un type de puzzle à la fois**")
        rapport.append("2. **Analyser visuellement les erreurs** (images générées)")
        rapport.append("3. **Améliorer le solver pour les cas critiques**")
        rapport.append("4. **Tester sur le test set avant soumission**")
        
        return "\n".join(rapport)

def main():
    """🏁 Fonction principale"""
    print("🏛️ VALIDATION OFFICIELLE ARC PRIZE - Refuge ARC-AGI")
    print("=" * 60)
    
    # Initialiser le validateur
    validateur = ValidateurOfficielARC()
    
    # Valider le training set
    resultats = validateur.valider_training_set(max_taches=20)  # Commencer avec 20 tâches
    
    # Générer le rapport
    rapport = validateur.generer_rapport_amelioration(resultats)
    
    # Sauvegarder le rapport
    with open('rapport_validation_officielle.md', 'w', encoding='utf-8') as f:
        f.write(rapport)
    
    print(f"\n📄 Rapport sauvegardé: rapport_validation_officielle.md")
    print(f"🎨 Images d'erreurs générées pour analyse visuelle")
    
    # Afficher le rapport
    print("\n" + "=" * 60)
    print(rapport)

if __name__ == "__main__":
    main()
