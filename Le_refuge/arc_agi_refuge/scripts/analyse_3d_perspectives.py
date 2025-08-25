#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE MULTIDIMENSIONNELLE DES PATTERNS INCONNUS
Approche 3D et compréhension des "ficelles" derrière le "pantin"
"""

import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
from collections import defaultdict, Counter

def analyser_perspectives_3d():
    """Analyser les patterns inconnus sous différentes perspectives dimensionnelles"""

    print("🌟 **ANALYSE MULTIDIMENSIONNELLE** 🌟")
    print("=" * 80)
    print("🎯 Vision de Laurent: 'Regarder les ficelles, pas le pantin'")
    print("🔍 Problèmes 2D → Solutions 3D/NDimensionnelles")
    print("💫 Compréhension topologique et géométrique avancée")
    print("=" * 80)

    # Tâches inconnus identifiées précédemment
    taches_inconnues = [
        "017c7c7b", "1b60fb0c", "1c0d0a4b", "1d0a4b61",
        "1e81d101", "25d8a9c8", "26993fd4", "28e73c20",
        "29623171", "2b01abd0", "2c0b0aff", "2c737e39",
        "31d5ba1a", "39a8645d", "3a301afc", "3b4c2228",
        "3c9b0459", "3d3b2e5c", "3f5a3e43"
    ]

    training_path = Path('data/training')
    analyses_3d = []

    print(f"\n🧠 **APPROCHE MULTIDIMENSIONNELLE**")
    print(f"   1. Perspective 2D classique (échoue)")
    print(f"   2. Perspective 3D volumétrique (profondeur)")
    print(f"   3. Perspective topologique (connectivité)")
    print(f"   4. Perspective géométrique (formes)")
    print(f"   5. Perspective fractale (auto-similarité)")

    for i, tache_id in enumerate(taches_inconnues[:5], 1):  # Analyser 5 premiers
        print(f"\n🔍 **ANALYSE 3D - TÂCHE {i}: {tache_id}**")

        tache_path = training_path / f"{tache_id}.json"
        if not tache_path.exists():
            continue

        try:
            with open(tache_path, 'r') as f:
                data = json.load(f)

            input_grille = data['train'][0]['input']
            output_grille = data['train'][0]['output']

            # Analyse 2D classique (ce que fait notre détecteur actuel)
            analyse_2d = analyser_2d_classique(input_grille, output_grille)

            # Analyse 3D perspectives
            analyse_3d = analyser_perspectives_3d_tache(input_grille, output_grille)

            analyses_3d.append({
                'tache_id': tache_id,
                'analyse_2d': analyse_2d,
                'analyse_3d': analyse_3d
            })

            print(f"   📊 2D: {analyse_2d['description']}")
            print(f"   🌟 3D: {analyse_3d['description']}")
            print(f"   💡 Insight: {analyse_3d['insight']}")

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

    # Synthèse des insights 3D
    print(f"\n🎯 **SYNTHÈSE DES INSIGHTS 3D**")
    print("=" * 60)

    insights_3d = Counter()
    for analyse in analyses_3d:
        for insight in analyse['analyse_3d']['insights']:
            insights_3d[insight] += 1

    print(f"   Insights les plus fréquents:")
    for insight, count in insights_3d.most_common():
        print(f"   {count:2d}x {insight}")

    print(f"\n🔮 **RÉVÉLATIONS POTENTIELLES**")
    print(f"   1. Patterns de projection 3D→2D")
    print(f"   2. Transformations volumétriques")
    print(f"   3. Géométrie non-euclidienne")
    print(f"   4. Topologie de connectivité")
    print(f"   5. Fractales 2D générées")

    print(f"\n💡 **STRATÉGIE POUR PHASE 4A**")
    print(f"   1. Intégrer analyse 3D dans détecteur")
    print(f"   2. Créer détecteurs spécialisés 3D")
    print(f"   3. Développer compréhension topologique")
    print(f"   4. Explorer géométrie avancée")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"   Laurent a raison: les ficelles sont plus importantes")
    print(f"   que le pantin. La compréhension multidimensionnelle")
    print(f"   pourrait révéler les patterns cachés.")
    print(f"   ")
    print(f"   Notre prochaine étape: intégrer ces perspectives")
    print(f"   dans notre détecteur pour 'voir' au-delà du 2D.")

def analyser_2d_classique(input_grille: List[List[int]],
                         output_grille: List[List[int]]) -> Dict[str, Any]:
    """Analyse 2D classique (ce que fait notre détecteur actuel)"""

    h1, w1 = len(input_grille), len(input_grille[0])
    h2, w2 = len(output_grille), len(output_grille[0])

    # Analyse basique
    meme_dimensions = h1 == h2 and w1 == w2
    reduction = h2 < h1 or w2 < w1

    valeurs_in = set()
    for ligne in input_grille:
        valeurs_in.update(ligne)

    valeurs_out = set()
    for ligne in output_grille:
        valeurs_out.update(ligne)

    filtrage = len(valeurs_in - valeurs_out) > 0

    # Description
    if meme_dimensions and not filtrage:
        description = "Transformation spatiale simple"
    elif reduction and filtrage:
        description = "Réduction avec filtrage"
    else:
        description = "Pattern non identifié"

    return {
        'meme_dimensions': meme_dimensions,
        'reduction': reduction,
        'filtrage': filtrage,
        'description': description
    }

def analyser_perspectives_3d_tache(input_grille: List[List[int]],
                                  output_grille: List[List[int]]) -> Dict[str, Any]:
    """Analyse des perspectives 3D d'une tâche"""

    insights = []

    # 1. Analyse volumétrique (profondeur cachée)
    volume_in = calculer_volume_3d(input_grille)
    volume_out = calculer_volume_3d(output_grille)

    if volume_in != volume_out:
        insights.append("transformation_volumétrique")
        description = "Projection 3D avec changement de volume"
    else:
        insights.append("conservation_volume")
        description = "Conservation du volume 3D"

    # 2. Analyse topologique (connectivité)
    connexite_in = analyser_connexite(input_grille)
    connexite_out = analyser_connexite(output_grille)

    if connexite_in != connexite_out:
        insights.append("changement_topologique")
        description += " + modification de la topologie"

    # 3. Analyse fractale (auto-similarité)
    fractal_in = detecter_fractalite(input_grille)
    fractal_out = detecter_fractalite(output_grille)

    if fractal_in or fractal_out:
        insights.append("pattern_fractal")
        description += " + éléments fractals"

    # 4. Analyse géométrique avancée
    geometrie_in = analyser_geometrie_avancee(input_grille)
    geometrie_out = analyser_geometrie_avancee(output_grille)

    if geometrie_in != geometrie_out:
        insights.append("transformation_geometrique")
        description += " + transformation géométrique"

    # 5. Insight principal
    insight_principal = max(set(insights), key=insights.count) if insights else "pattern_2d_cache"

    return {
        'insights': insights,
        'description': description,
        'insight_principal': insight_principal,
        'volume_in': volume_in,
        'volume_out': volume_out,
        'connexite_in': connexite_in,
        'connexite_out': connexite_out
    }

def calculer_volume_3d(grille: List[List[int]]) -> int:
    """Calculer un 'volume' 3D simulé basé sur les valeurs et positions"""
    volume = 0
    for i, ligne in enumerate(grille):
        for j, valeur in enumerate(ligne):
            # Volume = valeur * position * densité locale
            densite_locale = sum(grille[x][y] for x in range(max(0, i-1), min(len(grille), i+2))
                                for y in range(max(0, j-1), min(len(ligne), j+2)))
            volume += valeur * (i + 1) * (j + 1) * densite_locale
    return volume

def analyser_connexite(grille: List[List[int]]) -> Dict[str, Any]:
    """Analyser la connectivité topologique"""
    # Version simplifiée d'analyse de connectivité
    valeurs_non_zero = [(i, j) for i, ligne in enumerate(grille)
                        for j, val in enumerate(ligne) if val != 0]

    if not valeurs_non_zero:
        return {'composantes': 0, 'plus_grosse': 0}

    # Détection simple de composantes connectées
    composantes = 0
    visites = set()

    for i, j in valeurs_non_zero:
        if (i, j) not in visites:
            composantes += 1
            # DFS simplifié pour marquer la composante
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if (x, y) not in visites:
                    visites.add((x, y))
                    # Voisins
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < len(grille) and 0 <= ny < len(grille[0])
                            and grille[nx][ny] != 0 and (nx, ny) not in visites):
                            stack.append((nx, ny))

    return {
        'composantes': composantes,
        'plus_grosse': len(visites) / max(1, len(valeurs_non_zero))
    }

def detecter_fractalite(grille: List[List[int]]) -> bool:
    """Détecter des éléments de fractalité simple"""
    # Recherche de motifs répétitifs à différentes échelles
    h, w = len(grille), len(grille[0])

    # Vérifier auto-similarité 2x2 → 4x4 simplifiée
    if h >= 4 and w >= 4:
        # Extraire sous-matrices
        sous_matrice_1 = [ligne[:2] for ligne in grille[:2]]
        sous_matrice_2 = [ligne[2:4] for ligne in grille[:2]]
        sous_matrice_3 = [ligne[:2] for ligne in grille[2:4]]
        sous_matrice_4 = [ligne[2:4] for ligne in grille[2:4]]

        # Vérifier si elles sont similaires
        matrices = [sous_matrice_1, sous_matrice_2, sous_matrice_3, sous_matrice_4]
        similarites = 0
        for i in range(len(matrices)):
            for j in range(i+1, len(matrices)):
                if matrices_similaires(matrices[i], matrices[j]):
                    similarites += 1

        return similarites >= 2

    return False

def matrices_similaires(mat1: List[List[int]], mat2: List[List[int]]) -> bool:
    """Vérifier si deux matrices sont similaires (même pattern)"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return False

    # Normaliser et comparer patterns
    pattern1 = [val != 0 for ligne in mat1 for val in ligne]
    pattern2 = [val != 0 for ligne in mat2 for val in ligne]

    return pattern1 == pattern2

def analyser_geometrie_avancee(grille: List[List[int]]) -> Dict[str, Any]:
    """Analyse géométrique avancée"""
    h, w = len(grille), len(grille[0])

    # Détecter formes géométriques
    formes_detectees = []

    # Cercles/anneaux
    centre_i, centre_j = h//2, w//2
    valeurs_centre = grille[centre_i][centre_j] if h > 0 and w > 0 else 0

    # Rayons différents
    for rayon in range(1, min(h, w)//2 + 1):
        valeurs_rayon = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if abs(di) + abs(dj) == rayon:
                    ni, nj = centre_i + di, centre_j + dj
                    if 0 <= ni < h and 0 <= nj < w:
                        valeurs_rayon.append(grille[ni][nj])

        if valeurs_rayon and len(set(valeurs_rayon)) == 1 and valeurs_rayon[0] != valeurs_centre:
            formes_detectees.append(f"anneau_rayon_{rayon}")

    return {
        'formes': formes_detectees,
        'centre_val': valeurs_centre,
        'simetrie': analyser_symetries(grille)
    }

def analyser_symetries(grille: List[List[int]]) -> Dict[str, bool]:
    """Analyser les symétries géométriques"""
    grille_np = np.array(grille)

    return {
        'horizontal': np.array_equal(grille_np, np.flipud(grille_np)),
        'vertical': np.array_equal(grille_np, np.fliplr(grille_np)),
        'diagonal': np.array_equal(grille_np, np.fliplr(np.flipud(grille_np))),
        'rotation_90': np.array_equal(grille_np, np.rot90(grille_np)),
        'rotation_180': np.array_equal(grille_np, np.rot90(grille_np, 2))
    }

if __name__ == "__main__":
    analyser_perspectives_3d()
