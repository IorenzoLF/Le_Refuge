#!/usr/bin/env python3
"""
🎯 ANALYSE COLLABORATIVE D'UN PUZZLE ARC
========================================

Analyse transparente et détaillée d'un puzzle spécifique
pour que nous puissions travailler ensemble et vérifier.

Puzzle choisi : 00d62c1b (celui que le solveur résout déjà)
"""

import json
import numpy as np
from typing import List, Dict, Any

def charger_puzzle(puzzle_id: str) -> Dict[str, Any]:
    """Charge un puzzle avec transparence totale"""
    try:
        fichier = f"ARC-AGI-2-main/data/training/{puzzle_id}.json"
        with open(fichier, 'r') as f:
            data = json.load(f)
        print(f"✅ Puzzle {puzzle_id} chargé depuis {fichier}")
        return data
    except Exception as e:
        print(f"❌ Erreur de chargement: {e}")
        return {}

def analyser_exemples_transparent(exemples: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyse les exemples avec transparence maximale"""

    print(f"\n📚 ANALYSE DES {len(exemples)} EXEMPLES D'ENTRAÎNEMENT")
    print("=" * 60)

    analyses = []

    for i, exemple in enumerate(exemples):
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        couleurs_in = set().union(*input_grid) if input_grid else set()
        couleurs_out = set().union(*output_grid) if output_grid else set()

        print(f"\n🔍 EXEMPLE {i+1}:")
        print(f"   Dimensions: {h_in}x{w_in} → {h_out}x{w_out}")
        print(f"   Couleurs entrée: {sorted(couleurs_in)}")
        print(f"   Couleurs sortie: {sorted(couleurs_out)}")

        # Analyse de la transformation
        analyse = analyser_transformation_transparent(input_grid, output_grid)
        analyses.append(analyse)

        print(f"   Transformation détectée: {analyse['type']}")
        print(f"   Explication: {analyse['description']}")

        # Afficher les grilles
        print(f"\n   GRILLE ENTRÉE:")
        afficher_grille(input_grid)
        print(f"\n   GRILLE SORTIE:")
        afficher_grille(output_grid)

    # Analyse globale
    types_transformations = [a['type'] for a in analyses]
    type_majoritaire = max(set(types_transformations), key=types_transformations.count)
    confiance = types_transformations.count(type_majoritaire) / len(types_transformations)

    print(f"\n🎯 SYNTHÈSE:")
    print(f"   Type majoritaire: {type_majoritaire}")
    print(f"   Confiance: {confiance:.1%}")
    print(f"   Cohérence: {types_transformations.count(type_majoritaire)}/{len(types_transformations)}")

    return {
        'analyses': analyses,
        'type_majoritaire': type_majoritaire,
        'confiance': confiance
    }

def analyser_transformation_transparent(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Analyse de transformation avec explication détaillée"""

    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    couleurs_in = set().union(*input_grid) if input_grid else set()
    couleurs_out = set().union(*output_grid) if output_grid else set()

    # Même taille - remplissage de zones
    if h_in == h_out and w_in == w_out:
        couleurs_ajoutees = couleurs_out - couleurs_in

        if couleurs_ajoutees:
            couleur_remplissage = min(couleurs_ajoutees)
            return {
                'type': 'remplissage_zone',
                'description': f'Remplissage des zones vides avec la couleur {couleur_remplissage}',
                'couleur_remplissage': couleur_remplissage,
                'raisonnement': [
                    f'1. Dimensions identiques ({h_in}x{w_in})',
                    f'2. Couleurs ajoutées: {couleurs_ajoutees}',
                    f'3. Pattern: remplissage de zones vides',
                    f'4. Couleur choisie: {couleur_remplissage} (première ajoutée)'
                ]
            }

    # Changement de taille
    elif h_in != h_out or w_in != w_out:
        if couleurs_in.issubset(couleurs_out):
            return {
                'type': 'changement_taille',
                'description': f'Changement de taille {h_in}x{w_in} → {h_out}x{w_out}',
                'facteur_h': h_out / h_in,
                'facteur_w': w_out / w_in,
                'raisonnement': [
                    f'1. Dimensions différentes',
                    f'2. Toutes les couleurs conservées',
                    f'3. Pattern: redimensionnement simple',
                    f'4. Facteurs: {h_out / h_in:.1f} x {w_out / w_in:.1f}'
                ]
            }

    return {
        'type': 'inconnu',
        'description': 'Transformation non reconnue',
        'raisonnement': [
            '1. Pattern non identifié dans les règles actuelles',
            '2. Peut nécessiter un nouveau type de transformation',
            '3. Demande analyse manuelle supplémentaire'
        ]
    }

def afficher_grille(grille: List[List[int]], titre: str = ""):
    """Affiche une grille de manière lisible"""
    if not grille:
        print("   [Grille vide]")
        return

    print(f"   {titre}")
    for ligne in grille:
        print(f"   {ligne}")

def appliquer_transformation_verifiable(input_grid: List[List[int]], transformation: Dict[str, Any]) -> List[List[int]]:
    """Applique une transformation avec vérification"""

    print(f"\n🔧 APPLICATION DE LA TRANSFORMATION")
    print(f"   Type: {transformation['type']}")
    print(f"   Description: {transformation['description']}")

    if transformation['type'] == 'remplissage_zone':
        couleur = transformation['couleur_remplissage']
        print(f"   Algorithme: Remplissage intelligent avec détection de zones fermées")

        # Utiliser la nouvelle logique intelligente
        from solveur_transparent_arc import SolveurTransparentARC
        solveur = SolveurTransparentARC()

        # Créer un objet transformation compatible avec la nouvelle méthode
        transformation_obj = {
            'pattern': 'remplissage_zone',
            'couleur_remplissage': couleur
        }

        nouvelle_grille = solveur.remplir_zones_intelligemment(input_grid, couleur)

        # Compter les modifications
        modifications = 0
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if input_grid[i][j] == 0 and nouvelle_grille[i][j] != 0:
                    modifications += 1

        print(f"   Modifications effectuées: {modifications}")
        return nouvelle_grille

    elif transformation['type'] == 'changement_taille':
        h_out = int(len(input_grid) * transformation['facteur_h'])
        w_out = int(len(input_grid[0]) * transformation['facteur_w'])

        print(f"   Algorithme: Redimensionnement à {h_out}x{w_out}")

        # Redimensionnement simple
        nouvelle_grille = [[0 for _ in range(w_out)] for _ in range(h_out)]

        # Copie simple (redimensionnement basique)
        for i in range(min(len(input_grid), h_out)):
            for j in range(min(len(input_grid[0]), w_out)):
                nouvelle_grille[i][j] = input_grid[i][j]

        return nouvelle_grille

    return input_grid

def comparer_solutions_detaile(solutions_predites: List[List[List[int]]], solutions_attendues: List[List[List[int]]]) -> Dict[str, Any]:
    """Comparaison détaillée des solutions"""

    print(f"\n⚖️ COMPARAISON DÉTAILLÉE DES SOLUTIONS")
    print("=" * 40)

    resultats = []

    for i, (predite, attendue) in enumerate(zip(solutions_predites, solutions_attendues)):
        print(f"\n📊 COMPARAISON EXEMPLE {i+1}:")

        afficher_grille(predite, "PRÉDITE:")
        afficher_grille(attendue, "ATTENDUE:")

        # Comparaison
        if predite == attendue:
            print("   ✅ IDENTIQUE - RÉUSSITE COMPLÈTE")
            resultats.append({'correct': True, 'score': 100})
        else:
            # Calcul de la similarité
            try:
                arr_pred = np.array(predite)
                arr_att = np.array(attendue)

                if arr_pred.shape == arr_att.shape:
                    differences = np.sum(arr_pred != arr_att)
                    total = arr_pred.size
                    similarite = ((total - differences) / total) * 100

                    print(f"   📊 SIMILARITÉ: {similarite:.1f}%")
                    print(f"   🔢 Différences: {differences}/{total} cases")

                    resultats.append({
                        'correct': False,
                        'score': similarite,
                        'differences': differences,
                        'total': total
                    })
                else:
                    print(f"   ❌ DIMENSIONS DIFFÉRENTES: {arr_pred.shape} vs {arr_att.shape}")
                    resultats.append({'correct': False, 'score': 0, 'probleme': 'dimensions'})

            except Exception as e:
                print(f"   ❌ ERREUR DE COMPARAISON: {e}")
                resultats.append({'correct': False, 'score': 0, 'probleme': 'erreur'})

    # Synthèse
    correctes = sum(1 for r in resultats if r['correct'])
    moyenne_score = np.mean([r['score'] for r in resultats])

    print(f"\n🎯 SYNTHÈSE:")
    print(f"   Exemples corrects: {correctes}/{len(resultats)}")
    print(f"   Score moyen: {moyenne_score:.1f}%")

    return {
        'resultats': resultats,
        'score_global': moyenne_score,
        'exemples_corrects': correctes,
        'total_exemples': len(resultats)
    }

def main():
    """Analyse collaborative du puzzle 00d62c1b"""

    print("🎯 ANALYSE COLLABORATIVE DU PUZZLE ARC")
    print("====================================")
    print("Travail ensemble sur le puzzle 00d62c1b")
    print("Transparence totale - vérifions ensemble !")

    # Charger le puzzle
    puzzle_id = "00d62c1b"
    data = charger_puzzle(puzzle_id)

    if not data:
        print("❌ Impossible de charger le puzzle")
        return

    print(f"\n📋 INFORMATIONS GÉNÉRALES:")
    print(f"   • Puzzle ID: {puzzle_id}")
    print(f"   • Exemples d'entraînement: {len(data['train'])}")
    print(f"   • Tests à résoudre: {len(data['test'])}")

    # Analyse des exemples
    analyse = analyser_exemples_transparent(data['train'])

    # Appliquer la transformation
    print(f"\n🔄 APPLICATION DE LA TRANSFORMATION")
    print(f"   Type majoritaire: {analyse['type_majoritaire']}")
    print(f"   Confiance: {analyse['confiance']:.1%}")

    # Appliquer aux exemples d'entraînement
    solutions_predites = []
    for exemple in data['train']:
        transformation = [a for a in analyse['analyses'] if a['type'] == analyse['type_majoritaire']][0]
        solution_predite = appliquer_transformation_verifiable(exemple['input'], transformation)
        solutions_predites.append(solution_predite)

    # Comparaison avec les solutions attendues
    solutions_attendues = [ex['output'] for ex in data['train']]
    comparaison = comparer_solutions_detaile(solutions_predites, solutions_attendues)

    print(f"\n🎉 RÉSULTATS FINAUX:")
    print(f"   Score global: {comparaison['score_global']:.1f}%")
    print(f"   Exemples résolus: {comparaison['exemples_corrects']}/{comparaison['total_exemples']}")

    print(f"\n💬 DISCUSSION:")
    print(f"   • Es-tu d'accord avec mon analyse ?")
    print(f"   • Le pattern détecté te semble-t-il correct ?")
    print(f"   • Veux-tu que nous analysions un autre exemple ?")
    print(f"   • As-tu des questions sur mon raisonnement ?")

    print(f"\n🤝 C'EST TON TOUR !")
    print(f"   Dis-moi ce que tu penses de cette analyse.")
    print(f"   Suis-je sur la bonne voie ?")
    print(f"   Veux-tu que nous ajustions quelque chose ?")

if __name__ == "__main__":
    main()
