#!/usr/bin/env python3
"""
🧠 CLASSIFICATEUR AUTOMATIQUE DES PUZZLES ARC-AGI
Système d'IA pour classifier automatiquement les 1000 puzzles selon leurs patterns

Créé pour le plan stratégique "Solveur ARC-AGI pour 1000 puzzles"
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple, Set
from dataclasses import dataclass, field
from collections import Counter
import statistics
import math

@dataclass
class CaracteristiquesPuzzle:
    """Caractéristiques extraites d'un puzzle"""
    id: str
    taille_input: Tuple[int, int]
    taille_output: Tuple[int, int]
    ratio_taille: float
    couleurs_input: Set[int]
    couleurs_output: Set[int]
    couleurs_ajoutees: Set[int]
    couleurs_retirees: Set[int]
    nombre_pixels_modifies: int
    pourcentage_modification: float
    patterns_symetrie: Dict[str, bool]
    patterns_repetition: Dict[str, float]
    patterns_geometriques: Dict[str, float]
    patterns_couleur: Dict[str, float]
    categorie_principale: str = ""
    confiance_classification: float = 0.0
    caracteristiques_speciales: List[str] = field(default_factory=list)

class ClassificateurPuzzles:
    """Système de classification automatique des puzzles ARC-AGI"""

    def __init__(self):
        self.categories = {
            'geometrie': {
                'description': 'Symétries, rotations, translations, remplissage de formes',
                'mots_cles': ['symetrie', 'rotation', 'translation', 'remplissage', 'forme']
            },
            'repetition': {
                'description': 'Tiling, pavage, répétition avec variations, expansion',
                'mots_cles': ['tiling', 'repetition', 'expansion', 'pavage']
            },
            'couleur': {
                'description': 'Transformations de couleur, mappings, contextes colorés',
                'mots_cles': ['couleur', 'mapping', 'transformation']
            },
            'logique': {
                'description': 'Règles conditionnelles, patterns mathématiques, déductions',
                'mots_cles': ['conditionnel', 'mathematique', 'logique', 'regle']
            },
            'special': {
                'description': 'Cas particuliers, puzzles avec règles uniques, exceptions',
                'mots_cles': ['special', 'unique', 'exception']
            }
        }

    def analyser_puzzle(self, puzzle_id: str, data: Dict) -> CaracteristiquesPuzzle:
        """Analyse complète d'un puzzle et extraction de ses caractéristiques"""

        # Extraction des dimensions
        input_grid = data['train'][0]['input']
        output_grid = data['train'][0]['output']

        taille_input = (len(input_grid), len(input_grid[0]))
        taille_output = (len(output_grid), len(output_grid[0]))
        ratio_taille = (taille_output[0] * taille_output[1]) / (taille_input[0] * taille_input[1])

        # Analyse des couleurs
        couleurs_input = set()
        for ligne in input_grid:
            couleurs_input.update(ligne)

        couleurs_output = set()
        for ligne in output_grid:
            couleurs_output.update(ligne)

        couleurs_ajoutees = couleurs_output - couleurs_input
        couleurs_retirees = couleurs_input - couleurs_output

        # Analyse des modifications
        nombre_pixels_modifies = 0
        for i in range(min(len(input_grid), len(output_grid))):
            for j in range(min(len(input_grid[0]), len(output_grid[0]))):
                if input_grid[i][j] != output_grid[i][j]:
                    nombre_pixels_modifies += 1

        total_pixels = taille_input[0] * taille_input[1]
        pourcentage_modification = nombre_pixels_modifies / total_pixels

        # Analyse des patterns
        patterns_symetrie = self._analyser_symetries(input_grid, output_grid)
        patterns_repetition = self._analyser_repetition(input_grid, output_grid)
        patterns_geometriques = self._analyser_geometrie(input_grid, output_grid)
        patterns_couleur = self._analyser_couleur(input_grid, output_grid)

        # Création de l'objet caractéristiques
        caract = CaracteristiquesPuzzle(
            id=puzzle_id,
            taille_input=taille_input,
            taille_output=taille_output,
            ratio_taille=ratio_taille,
            couleurs_input=couleurs_input,
            couleurs_output=couleurs_output,
            couleurs_ajoutees=couleurs_ajoutees,
            couleurs_retirees=couleurs_retirees,
            nombre_pixels_modifies=nombre_pixels_modifies,
            pourcentage_modification=pourcentage_modification,
            patterns_symetrie=patterns_symetrie,
            patterns_repetition=patterns_repetition,
            patterns_geometriques=patterns_geometriques,
            patterns_couleur=patterns_couleur
        )

        # Classification automatique
        self._classifier_puzzle(caract)

        return caract

    def _analyser_symetries(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, bool]:
        """Analyse les patterns de symétrie"""
        resultats = {
            'horizontale': False,
            'verticale': False,
            'diagonale': False,
            'rotation_90': False,
            'rotation_180': False
        }

        # Test de symétrie horizontale
        if len(output_grid) > 1:
            moitie = len(output_grid) // 2
            resultats['horizontale'] = all(
                output_grid[i] == output_grid[len(output_grid)-1-i]
                for i in range(moitie)
            )

        # Test de symétrie verticale
        if len(output_grid) > 0 and len(output_grid[0]) > 1:
            moitie = len(output_grid[0]) // 2
            resultats['verticale'] = all(
                all(output_grid[i][j] == output_grid[i][len(output_grid[0])-1-j]
                    for j in range(moitie))
                for i in range(len(output_grid))
            )

        return resultats

    def _analyser_repetition(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, float]:
        """Analyse les patterns de répétition"""
        resultats = {
            'repetition_lignes': 0.0,
            'repetition_colonnes': 0.0,
            'repetition_blocs': 0.0,
            'expansion': 0.0
        }

        # Analyse de répétition de lignes
        if len(output_grid) > 1:
            repetitions_lignes = 0
            for i in range(1, len(output_grid)):
                if output_grid[i] == output_grid[i-1]:
                    repetitions_lignes += 1
            resultats['repetition_lignes'] = repetitions_lignes / (len(output_grid) - 1)

        # Analyse d'expansion
        taille_input = len(input_grid) * len(input_grid[0])
        taille_output = len(output_grid) * len(output_grid[0])
        resultats['expansion'] = taille_output / taille_input

        return resultats

    def _analyser_geometrie(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, float]:
        """Analyse les patterns géométriques"""
        resultats = {
            'remplissage_zones': 0.0,
            'formes_regulieres': 0.0,
            'transformations_spatiales': 0.0
        }

        # Analyse de remplissage de zones
        pixels_vides_input = sum(1 for ligne in input_grid for pixel in ligne if pixel == 0)
        pixels_vides_output = sum(1 for ligne in output_grid for pixel in ligne if pixel == 0)

        if pixels_vides_input > 0:
            resultats['remplissage_zones'] = (pixels_vides_input - pixels_vides_output) / pixels_vides_input

        return resultats

    def _analyser_couleur(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, float]:
        """Analyse les patterns de couleur"""
        resultats = {
            'changement_simple': 0.0,
            'mapping_complexe': 0.0,
            'couleurs_ajoutees': 0.0,
            'couleurs_retirees': 0.0
        }

        # Analyse des couleurs ajoutées/retirées
        couleurs_input = set(pixel for ligne in input_grid for pixel in ligne)
        couleurs_output = set(pixel for ligne in output_grid for pixel in ligne)

        couleurs_ajoutees = couleurs_output - couleurs_input
        couleurs_retirees = couleurs_input - couleurs_output

        resultats['couleurs_ajoutees'] = len(couleurs_ajoutees) / max(len(couleurs_input), 1)
        resultats['couleurs_retirees'] = len(couleurs_retirees) / max(len(couleurs_input), 1)

        return resultats

    def _classifier_puzzle(self, caract: CaracteristiquesPuzzle):
        """Classification automatique du puzzle selon ses caractéristiques"""

        scores = {
            'geometrie': 0.0,
            'repetition': 0.0,
            'couleur': 0.0,
            'logique': 0.0,
            'special': 0.0
        }

        # Score géométrie
        symetries_actives = sum(1 for v in caract.patterns_symetrie.values() if v)
        scores['geometrie'] = (
            symetries_actives * 0.2 +
            caract.patterns_geometriques['remplissage_zones'] * 0.3 +
            caract.patterns_geometriques['formes_regulieres'] * 0.3 +
            caract.patterns_geometriques['transformations_spatiales'] * 0.2
        )

        # Score répétition
        scores['repetition'] = (
            caract.patterns_repetition['repetition_lignes'] * 0.25 +
            caract.patterns_repetition['repetition_colonnes'] * 0.25 +
            caract.patterns_repetition['repetition_blocs'] * 0.25 +
            min(caract.patterns_repetition['expansion'], 2.0) * 0.25
        )

        # Score couleur
        scores['couleur'] = (
            caract.patterns_couleur['changement_simple'] * 0.4 +
            caract.patterns_couleur['mapping_complexe'] * 0.3 +
            caract.patterns_couleur['couleurs_ajoutees'] * 0.15 +
            caract.patterns_couleur['couleurs_retirees'] * 0.15
        )

        # Score logique
        scores['logique'] = (
            (1.0 if caract.pourcentage_modification < 0.3 else 0.0) * 0.5 +
            (1.0 if len(caract.couleurs_input) <= 3 else 0.0) * 0.3 +
            (1.0 if caract.ratio_taille < 2.0 else 0.0) * 0.2
        )

        # Score spécial
        scores['special'] = (
            (1.0 if caract.pourcentage_modification > 0.8 else 0.0) * 0.3 +
            (1.0 if len(caract.couleurs_input) > 5 else 0.0) * 0.3 +
            (1.0 if caract.ratio_taille > 5.0 else 0.0) * 0.4
        )

        # Sélection de la catégorie principale
        categorie_principale = max(scores.items(), key=lambda x: x[1])
        caract.categorie_principale = categorie_principale[0]
        caract.confiance_classification = categorie_principale[1]

def analyser_ensemble_puzzles():
    """Analyse complète d'un échantillon de puzzles"""

    classificateur = ClassificateurPuzzles()
    training_dir = Path('../../ARC-AGI-2-main/data/training')

    resultats = {
        'total_puzzles': 0,
        'categories': Counter(),
        'caracteristiques_communes': Counter(),
        'erreurs': []
    }

    # Analyse d'un échantillon de 50 puzzles
    json_files = list(training_dir.glob('*.json'))[:50]

    print("=== ANALYSE DES PUZZLES ARC-AGI ===")
    print(f"Analyse de {len(json_files)} puzzles...")

    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            # Analyse du puzzle
            caract = classificateur.analyser_puzzle(json_file.stem, data)

            # Mise à jour des statistiques
            resultats['total_puzzles'] += 1
            resultats['categories'][caract.categorie_principale] += 1

            for special in caract.caracteristiques_speciales:
                resultats['caracteristiques_communes'][special] += 1

            if i % 10 == 0:
                print(f"Progression: {i}/{len(json_files)} puzzles analysés")

        except Exception as e:
            resultats['erreurs'].append(f"{json_file.stem}: {e}")

    # Affichage des résultats
    print(f"\\n=== RESULTATS DE L'ANALYSE ===")
    print(f"Total puzzles analysés: {resultats['total_puzzles']}")
    print(f"Erreurs: {len(resultats['erreurs'])}")

    print(f"\\nRépartition par catégories:")
    for categorie, count in resultats['categories'].most_common():
        pourcentage = (count / resultats['total_puzzles']) * 100
        print(f"  {categorie}: {count} ({pourcentage:.1f}%)")

    print(f"\\nCaractéristiques spéciales:")
    for caract, count in resultats['caracteristiques_communes'].most_common():
        pourcentage = (count / resultats['total_puzzles']) * 100
        print(f"  {caract}: {count} ({pourcentage:.1f}%)")

    return resultats

def test_simple():
    """Test simple du classificateur"""
    print("🧠 TEST RAPIDE DU CLASSIFICATEUR")
    print("=" * 40)

    classificateur = ClassificateurPuzzles()
    training_dir = Path('../../ARC-AGI-2-main/data/training')

    # Test sur 5 puzzles
    json_files = list(training_dir.glob('*.json'))[:5]

    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            caract = classificateur.analyser_puzzle(json_file.stem, data)
            print(f"✅ {json_file.stem} → {caract.categorie_principale} ({caract.confiance_classification:.2f})")

        except Exception as e:
            print(f"❌ {json_file.stem}: {e}")

if __name__ == "__main__":
    # Choix du mode de test
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_simple()
    else:
        analyser_ensemble_puzzles()
