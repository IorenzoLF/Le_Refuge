#!/usr/bin/env python3
"""
ANALYSE TÂCHE ÉCHOUÉE - ARC-AGI REFUGE
Analyse détaillée d'une tâche qui a échoué pour comprendre le problème
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le dossier src au path
sys.path.insert(0, 'src')

def analyser_tache_echouee(tache_id="137eaa0f"):
    """Analyser une tâche échouée spécifique"""
    print(f"ANALYSE TÂCHE ÉCHOUÉE: {tache_id}")
    print("=" * 50)
    
    # Chercher le fichier de la tâche
    data_dir = Path("data/training")
    fichier_tache = data_dir / f"{tache_id}.json"
    
    if not fichier_tache.exists():
        print(f"ERREUR: Fichier {tache_id}.json non trouve")
        return None
    
    print(f"Fichier trouve: {fichier_tache}")
    
    try:
        with open(fichier_tache, 'r', encoding='utf-8') as f:
            tache = json.load(f)
        
        print(f"Tache chargee avec succes")
        
        # Analyser la structure
        train = tache.get('train', [])
        test = tache.get('test', [])
        
        print(f"Exemples d'entrainement: {len(train)}")
        print(f"Exemples de test: {len(test)}")
        
        # Analyser le premier exemple d'entraînement
        if train:
            exemple = train[0]
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            print(f"\nPREMIER EXEMPLE D'ENTRAINEMENT:")
            print(f"  Input: {len(input_grille)}x{len(input_grille[0]) if input_grille else 0}")
            print(f"  Output: {len(output_grille)}x{len(output_grille[0]) if output_grille else 0}")
            
            # Analyser les couleurs
            couleurs_input = set()
            couleurs_output = set()
            
            for ligne in input_grille:
                couleurs_input.update(ligne)
            for ligne in output_grille:
                couleurs_output.update(ligne)
            
            print(f"  Couleurs input: {sorted(couleurs_input)}")
            print(f"  Couleurs output: {sorted(couleurs_output)}")
            
            # Afficher les grilles
            print(f"\n  GRILLE INPUT:")
            for ligne in input_grille:
                print(f"    {ligne}")
            
            print(f"\n  GRILLE OUTPUT:")
            for ligne in output_grille:
                print(f"    {ligne}")
        
        # Analyser les exemples de test
        if test:
            print(f"\nEXEMPLES DE TEST:")
            for i, exemple in enumerate(test):
                input_grille = exemple.get('input', [])
                if input_grille:
                    print(f"  Test {i+1}: {len(input_grille)}x{len(input_grille[0])}")
        
        return tache
        
    except Exception as e:
        print(f"ERREUR analyse: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_solveur_sur_tache_echouee(tache):
    """Tester le solveur sur une tâche échouée"""
    print(f"\nTEST SOLVEUR SUR TÂCHE ÉCHOUÉE:")
    print("=" * 40)
    
    try:
        from refuge_solver import RefugeARCSolver, TacheARC
        
        solver = RefugeARCSolver()
        
        # Créer l'objet TacheARC
        tache_id = tache.get('task_id', 'test')
        train = tache['train']
        test = tache['test']
        
        tache_obj = TacheARC(tache_id=tache_id, train=train, test=test)
        
        print(f"Resolution de la tache: {tache_id}")
        
        # Résoudre la tâche
        resultats = solver.resoudre_tache(tache_obj)
        
        # Analyser les résultats
        synthese = resultats.get('synthese', {})
        succes = synthese.get('solution_trouvee', False)
        confiance = synthese.get('confiance', 0)
        
        print(f"Resultats:")
        print(f"  Succes: {succes}")
        print(f"  Confiance: {confiance:.3f}")
        
        # Analyser les patterns détectés
        patterns_info = resultats.get('patterns_info', {})
        patterns_detectes = patterns_info.get('patterns_detectes', 0)
        confiance_patterns = patterns_info.get('confiance_moyenne', 0)
        
        print(f"  Patterns detectes: {patterns_detectes}")
        print(f"  Confiance patterns: {confiance_patterns:.3f}")
        
        return resultats
        
    except Exception as e:
        print(f"ERREUR test solveur: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Test principal"""
    print("ANALYSE TÂCHE ÉCHOUÉE ARC-AGI REFUGE")
    print("=" * 60)
    
    # Analyser une tâche échouée
    tache = analyser_tache_echouee("137eaa0f")
    if not tache:
        print("Impossible d'analyser la tache")
        return
    
    # Tester le solveur
    resultats = test_solveur_sur_tache_echouee(tache)
    if resultats:
        print(f"\nAnalyse terminee avec succes!")

if __name__ == "__main__":
    main()
