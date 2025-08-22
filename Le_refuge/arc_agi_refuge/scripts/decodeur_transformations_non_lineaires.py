#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÉCODEUR TRANSFORMATIONS NON-LINÉAIRES : Le Saint Graal du God Level
Objectif: Décoder les patterns mathématiques cachés dans les 8 tâches ultra-limites
"""

import json
import numpy as np
import math
from pathlib import Path
from typing import List, Dict, Any, Tuple, Callable
from collections import defaultdict, Counter
from itertools import combinations
from src.refuge_solver import RefugeARCSolver, TacheARC

class DecodeurTransformationsNonLineaires:
    """Décodeur spécialisé pour les transformations non-linéaires"""

    def __init__(self):
        # Base de transformations connues
        self.transformations_connues = {
            'carre': lambda x: x * x,
            'cube': lambda x: x * x * x,
            'racine_carree': lambda x: int(math.sqrt(x)) if x >= 0 else x,
            'racine_cubique': lambda x: int(x ** (1/3)) if x >= 0 else x,
            'double': lambda x: x * 2,
            'triple': lambda x: x * 3,
            'exponentielle': lambda x: int(2 ** x) if x < 10 else x,
            'logarithme': lambda x: int(math.log2(x)) if x > 0 else 0,
            'modulo_3': lambda x: x % 3,
            'modulo_5': lambda x: x % 5,
            'modulo_7': lambda x: x % 7,
            'factorielle': lambda x: math.factorial(min(x, 6)),  # Limiter pour éviter overflow
        }

        # Patterns spatiaux non-linéaires
        self.patterns_spatiaux_non_lineaires = {
            'spiral': self._detecter_spiral,
            'fractal_simple': self._detecter_fractal_simple,
            'mapping_non_lineaire': self._detecter_mapping_non_lineaire,
            'transformation_geometrique': self._detecter_transformation_geometrique,
        }

    def analyser_tache_non_lineaire(self, tache_id: str) -> Dict[str, Any]:
        """Analyse complète d'une tâche avec transformations non-linéaires"""

        print(f"\n🔍 **ANALYSE NON-LINÉAIRE DE {tache_id}**")
        print("=" * 60)

        # Charger la tâche
        json_path = Path('data/training') / f"{tache_id}.json"
        if not json_path.exists():
            return {'erreur': 'Fichier non trouvé'}

        with open(json_path, 'r') as f:
            data = json.load(f)

        # Analyser chaque exemple
        resultats_analyse = []

        for i, exemple in enumerate(data['train']):
            print(f"\n📊 **EXEMPLE {i+1}/3**")

            input_grid = np.array(exemple['input'])
            output_grid = np.array(exemple['output'])

            print(f"   Input {input_grid.shape}: {self._grid_to_string(input_grid)}")
            print(f"   Output {output_grid.shape}: {self._grid_to_string(output_grid)}")

            # Analyser les transformations possibles
            transformations_trouvees = self._analyser_transformations_exemple(input_grid, output_grid)

            resultats_analyse.append({
                'exemple': i,
                'transformations': transformations_trouvees,
                'meilleure_confiance': max([t['confiance'] for t in transformations_trouvees], default=0)
            })

            # Afficher les meilleures transformations
            transformations_triees = sorted(transformations_trouvees,
                                          key=lambda x: x['confiance'], reverse=True)

            for j, transfo in enumerate(transformations_triees[:3]):
                print(f"   {j+1}. {transfo['type']}: {transfo['confiance']:.2f} confiance")
                print(f"      {transfo.get('description', 'Aucune description')}")

        # Synthèse finale
        synthese = self._synthetiser_analyse(resultats_analyse)

        return {
            'tache_id': tache_id,
            'resultats_par_exemple': resultats_analyse,
            'synthese': synthese,
            'confiance_globale': synthese['confiance_moyenne']
        }

    def _analyser_transformations_exemple(self, input_grid: np.ndarray,
                                        output_grid: np.ndarray) -> List[Dict[str, Any]]:
        """Analyse toutes les transformations possibles pour un exemple"""

        transformations_candidates = []

        try:
            # 1. Transformations valeur-par-valeur
            transformations_valeur = self._analyser_transformations_valeur(input_grid, output_grid)
            transformations_candidates.extend(transformations_valeur)
        except Exception as e:
            print(f"   ⚠️ Erreur transformations valeur: {str(e)[:50]}...")

        try:
            # 2. Transformations spatiales non-linéaires
            transformations_spatiales = self._analyser_transformations_spatiales(input_grid, output_grid)
            transformations_candidates.extend(transformations_spatiales)
        except Exception as e:
            print(f"   ⚠️ Erreur transformations spatiales: {str(e)[:50]}...")

        try:
            # 3. Transformations mathématiques avancées (utilise la détection custom)
            transformations_math = []
            input_flat = input_grid.flatten()
            output_flat = output_grid.flatten()
            pattern_custom = self._detecter_pattern_mathematique_custom(input_flat, output_flat)
            if pattern_custom:
                transformations_math.append(pattern_custom)
            transformations_candidates.extend(transformations_math)
        except Exception as e:
            print(f"   ⚠️ Erreur transformations mathématiques: {str(e)[:50]}...")

        try:
            # 4. Patterns émergents complexes
            transformations_complexes = self._analyser_transformations_complexes(input_grid, output_grid)
            transformations_candidates.extend(transformations_complexes)
        except Exception as e:
            print(f"   ⚠️ Erreur transformations complexes: {str(e)[:50]}...")

        return transformations_candidates

    def _analyser_transformations_valeur(self, input_grid: np.ndarray,
                                       output_grid: np.ndarray) -> List[Dict[str, Any]]:
        """Analyse les transformations valeur-par-valeur non-linéaires"""

        transformations = []

        # Aplatir les grilles pour analyse
        input_values = input_grid.flatten()
        output_values = output_grid.flatten()

        # Si tailles différentes, focus sur valeurs communes
        min_len = min(len(input_values), len(output_values))
        input_sample = input_values[:min_len]
        output_sample = output_values[:min_len]

        # Tester chaque transformation connue
        for nom_transfo, fonction_transfo in self.transformations_connues.items():
            try:
                # Appliquer la transformation
                valeurs_transformees = [fonction_transfo(int(x)) for x in input_sample]

                # Calculer la similarité
                similarite = self._calculer_similarite_valeurs(valeurs_transformees, output_sample)

                if similarite > 0.3:  # Seuil minimum
                    transformations.append({
                        'type': nom_transfo,
                        'confiance': similarite,
                        'description': f"Transformation {nom_transfo} détectée ({similarite:.2f})",
                        'categorie': 'valeur_non_lineaire',
                        'exemple': f"{input_sample[:3]} → {valeurs_transformees[:3]}"
                    })

            except Exception as e:
                continue

        # Chercher patterns mathématiques personnalisés
        pattern_custom = self._detecter_pattern_mathematique_custom(input_sample, output_sample)
        if pattern_custom:
            transformations.append(pattern_custom)

        return transformations

    def _analyser_transformations_spatiales(self, input_grid: np.ndarray,
                                          output_grid: np.ndarray) -> List[Dict[str, Any]]:
        """Analyse les transformations spatiales non-linéaires"""

        transformations = []

        # Tester les patterns spatiaux connus
        for nom_pattern, fonction_detection in self.patterns_spatiaux_non_lineaires.items():
            try:
                resultat = fonction_detection(input_grid, output_grid)
                if resultat and resultat['confiance'] > 0.3:
                    transformations.append(resultat)
            except Exception as e:
                continue

        return transformations

    def _detecter_spiral(self, input_grid: np.ndarray, output_grid: np.ndarray) -> Dict[str, Any]:
        """Détecte les patterns en spirale"""

        h1, w1 = input_grid.shape
        h2, w2 = output_grid.shape

        # Pattern de spirale simple (expansion en spirale)
        if h2 >= h1 and w2 >= w1:
            # Calculer le ratio d'expansion
            ratio = (h2 * w2) / (h1 * w1)
            confiance = min(0.8, ratio / 4)  # Plus le ratio est élevé, plus de confiance

            return {
                'type': 'spiral_expansion',
                'confiance': confiance,
                'description': f'Expansion en spirale ({h1}x{w1} → {h2}x{w2})',
                'categorie': 'spatial_non_lineaire'
            }

        return None

    def _detecter_fractal_simple(self, input_grid: np.ndarray,
                               output_grid: np.ndarray) -> Dict[str, Any]:
        """Détecte les patterns fractals simples"""

        # Vérifier si l'output contient des répétitions du pattern input
        input_str = self._grid_to_string(input_grid)
        output_str = self._grid_to_string(output_grid)

        # Compter les occurrences du pattern input dans output
        count = output_str.count(input_str)

        if count > 0:
            confiance = min(0.9, count * 0.3)

            return {
                'type': 'fractal_repetition',
                'confiance': confiance,
                'description': f'Pattern fractal détecté ({count} répétitions)',
                'categorie': 'spatial_non_lineaire'
            }

        return None

    def _detecter_mapping_non_lineaire(self, input_grid: np.ndarray,
                                     output_grid: np.ndarray) -> Dict[str, Any]:
        """Détecte les mappings non-linéaires complexes"""

        # Analyser la relation position-par-position
        h1, w1 = input_grid.shape
        h2, w2 = output_grid.shape

        if h1 == h2 and w1 == w2:
            # Même taille, chercher mapping complexe
            differences = []
            for i in range(h1):
                for j in range(w1):
                    if input_grid[i,j] != output_grid[i,j]:
                        diff = abs(output_grid[i,j] - input_grid[i,j])
                        differences.append(diff)

            if differences:
                # Analyser les différences
                diff_counter = Counter(differences)
                diff_plus_frequente = diff_counter.most_common(1)[0]

                if diff_plus_frequente[1] > len(differences) * 0.3:  # 30% des changements
                    confiance = min(0.8, diff_plus_frequente[1] / len(differences))

                    return {
                        'type': 'mapping_differentiel',
                        'confiance': confiance,
                        'description': f'Mapping différentiel détecté (diff={diff_plus_frequente[0]})',
                        'categorie': 'valeur_non_lineaire'
                    }

        return None

    def _detecter_transformation_geometrique(self, input_grid: np.ndarray,
                                           output_grid: np.ndarray) -> Dict[str, Any]:
        """Détecte les transformations géométriques complexes"""

        # Calculer les propriétés géométriques
        h1, w1 = input_grid.shape
        h2, w2 = output_grid.shape

        # Ratio des dimensions
        ratio_h = h2 / h1 if h1 > 0 else 0
        ratio_w = w2 / w1 if w1 > 0 else 0

        # Détecter ratios non-entiers (signe de transformation géométrique)
        if ratio_h != int(ratio_h) or ratio_w != int(ratio_w):
            confiance = 0.6  # Confiance moyenne pour ratios non-entiers

            return {
                'type': 'transformation_geometrique_non_lineaire',
                'confiance': confiance,
                'description': f'Transformation géométrique ({h1}x{w1} → {h2:.1f}x{w2:.1f})',
                'categorie': 'spatial_non_lineaire'
            }

        return None

    def _detecter_pattern_mathematique_custom(self, input_values: List[int],
                                             output_values: List[int]) -> Dict[str, Any]:
        """Détecte les patterns mathématiques personnalisés"""

        # Essayer de trouver une relation mathématique
        if len(input_values) < 3 or len(output_values) < 3:
            return None

        # Tester quelques relations simples
        relations_testees = []

        # Relation linéaire: y = ax + b
        try:
            # Prendre 3 points pour calculer a et b
            x1, x2, x3 = input_values[:3]
            y1, y2, y3 = output_values[:3]

            # Calculer a et b pour y = ax + b
            if x2 != x1 and x3 != x1:
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1

                # Vérifier avec le 3ème point
                y3_calcule = a * x3 + b
                erreur = abs(y3_calcule - y3)

                if erreur < 0.1:  # Tolérance faible
                    return {
                        'type': 'relation_lineaire_custom',
                        'confiance': 0.8,
                        'description': f'Relation linéaire: y = {a:.2f}x + {b:.2f}',
                        'categorie': 'mathematique_custom'
                    }
        except:
            pass

        # Relation quadratique: y = ax^2 + bx + c
        try:
            x1, x2, x3 = input_values[:3]
            y1, y2, y3 = output_values[:3]

            # Résoudre le système pour a, b, c
            A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
            Y = np.array([y1, y2, y3])

            try:
                coeffs = np.linalg.solve(A, Y)
                a, b, c = coeffs

                return {
                    'type': 'relation_quadratique_custom',
                    'confiance': 0.7,
                    'description': f'Relation quadratique: y = {a:.2f}x² + {b:.2f}x + {c:.2f}',
                    'categorie': 'mathematique_custom'
                }
            except:
                pass
        except:
            pass

        return None

    def _analyser_transformations_complexes(self, input_grid: np.ndarray,
                                          output_grid: np.ndarray) -> List[Dict[str, Any]]:
        """Analyse les transformations complexes et émergentes"""

        transformations = []

        # Analyser les propriétés statistiques avancées
        input_flat = input_grid.flatten()
        output_flat = output_grid.flatten()

        # 1. Analyse de l'entropie (diversité des valeurs)
        if len(input_flat) > 0 and len(output_flat) > 0:
            entropie_input = self._calculer_entropie(input_flat)
            entropie_output = self._calculer_entropie(output_flat)

            # Si l'entropie change significativement
            ratio_entropie = entropie_output / entropie_input if entropie_input > 0 else 0
            if abs(ratio_entropie - 1.0) > 0.3:
                transformations.append({
                    'type': 'transformation_entropique',
                    'confiance': min(0.7, abs(ratio_entropie - 1.0)),
                    'description': f'Changement d\'entropie {entropie_input:.2f} → {entropie_output:.2f}',
                    'categorie': 'complexe'
                })

        # 2. Analyse des patterns de symétrie brisés
        sym_input = self._analyser_symetries_locales(input_grid)
        sym_output = self._analyser_symetries_locales(output_grid)

        if sym_input != sym_output:
            transformations.append({
                'type': 'changement_symetrie',
                'confiance': 0.6,
                'description': f'Symétrie {sym_input} → {sym_output}',
                'categorie': 'complexe'
            })

        return transformations

    def _calculer_entropie(self, valeurs: List[int]) -> float:
        """Calcule l'entropie de Shannon d'une liste de valeurs"""

        if not valeurs:
            return 0.0

        from collections import Counter
        import math

        comptages = Counter(valeurs)
        total = len(valeurs)
        entropie = 0.0

        for count in comptages.values():
            prob = count / total
            if prob > 0:
                entropie -= prob * math.log2(prob)

        return entropie

    def _analyser_symetries_locales(self, grid: np.ndarray) -> str:
        """Analyse les symétries locales de la grille"""

        h, w = grid.shape
        symetries = []

        # Vérifier symétrie horizontale
        if h > 1:
            try:
                if np.array_equal(grid, np.flipud(grid)):
                    symetries.append('horizontal')
            except:
                pass

        # Vérifier symétrie verticale
        if w > 1:
            try:
                if np.array_equal(grid, np.fliplr(grid)):
                    symetries.append('vertical')
            except:
                pass

        # Vérifier symétrie diagonale
        if h == w and h > 1:
            try:
                if np.array_equal(grid, np.fliplr(np.flipud(grid))):
                    symetries.append('diagonal')
            except:
                pass

        if symetries:
            return '+'.join(sorted(symetries))
        else:
            return 'aucune'

    def _calculer_similarite_valeurs(self, valeurs_predites: List[int],
                                    valeurs_reelles: List[int]) -> float:
        """Calcule la similarité entre valeurs prédites et réelles"""

        if len(valeurs_predites) != len(valeurs_reelles):
            min_len = min(len(valeurs_predites), len(valeurs_reelles))
            valeurs_predites = valeurs_predites[:min_len]
            valeurs_reelles = valeurs_reelles[:min_len]

        if len(valeurs_predites) == 0:
            return 0.0

        # Calculer l'erreur absolue moyenne
        erreurs = [abs(p - r) for p, r in zip(valeurs_predites, valeurs_reelles)]
        erreur_moyenne = sum(erreurs) / len(erreurs)

        # Convertir en similarité (0 à 1)
        # Plus l'erreur est faible, plus la similarité est élevée
        similarite = max(0.0, 1.0 - (erreur_moyenne / 10.0))  # Normaliser par 10

        return similarite

    def _grid_to_string(self, grid: np.ndarray) -> str:
        """Convertit une grille en string lisible"""
        return str(grid.tolist())

    def _synthetiser_analyse(self, resultats_exemples: List[Dict]) -> Dict[str, Any]:
        """Synthétise l'analyse de tous les exemples"""

        if not resultats_exemples:
            return {'confiance_moyenne': 0.0, 'meilleure_transformation': None}

        # Calculer la confiance moyenne
        confiances = [r['meilleure_confiance'] for r in resultats_exemples]
        confiance_moyenne = sum(confiances) / len(confiances)

        # Trouver la meilleure transformation globale
        toutes_transformations = []
        for r in resultats_exemples:
            toutes_transformations.extend(r['transformations'])

        if toutes_transformations:
            meilleure = max(toutes_transformations, key=lambda x: x['confiance'])
        else:
            meilleure = None

        return {
            'confiance_moyenne': confiance_moyenne,
            'meilleure_transformation': meilleure,
            'nb_exemples_analyses': len(resultats_exemples),
            'nb_transformations_trouvees': len(toutes_transformations)
        }

def decoder_transformations_non_lineaires():
    """Fonction principale pour décoder les transformations non-linéaires"""

    print("🔍 **DÉCODEUR TRANSFORMATIONS NON-LINÉAIRES**")
    print("🎯 Décoder les patterns mathématiques cachés")
    print("=" * 70)

    decodeur = DecodeurTransformationsNonLineaires()

    # Liste des tâches avec transformations non-linéaires (d'après l'analyse précédente)
    taches_ultra_limites = [
        '137eaa0f', '1990f7a8', '1cf80156', '2753e76c', '28bf18c6',
        '2dee498d', '358ba94e', '3d31c5b3'
    ]

    print(f"🎯 **ANALYSE DES {len(taches_ultra_limites)} TÂCHES ULTRA-LIMITES**")
    print("   Ces tâches nécessitent une véritable intuition artificielle !")
    print()

    resultats_globaux = []

    for tache_id in taches_ultra_limites:
        try:
            resultat = decodeur.analyser_tache_non_lineaire(tache_id)
            resultats_globaux.append(resultat)

            print(f"\n🏆 **RÉSULTAT POUR {tache_id}**")
            synthese = resultat.get('synthese', {})
            print(f"   🎯 Confiance globale: {resultat.get('confiance_globale', 0):.3f}")
            print(f"   📊 Transformations trouvées: {synthese.get('nb_transformations_trouvees', 0)}")

            if synthese.get('meilleure_transformation'):
                best = synthese['meilleure_transformation']
                print(f"   🌟 Meilleure: {best['type']} ({best['confiance']:.2f})")
                print(f"   📝 {best.get('description', 'Aucune description')}")

        except Exception as e:
            print(f"❌ **ERREUR {tache_id}**: {str(e)}")

    # Synthèse finale
    print(f"\n🏆 **SYNTHÈSE FINALE : DÉCODAGE RÉUSSI**")
    print("=" * 60)

    taches_avec_solution = [r for r in resultats_globaux if r.get('confiance_globale', 0) > 0.5]
    taches_sans_solution = [r for r in resultats_globaux if r.get('confiance_globale', 0) <= 0.5]

    print(f"✅ **TÂCHES DÉCODÉES**: {len(taches_avec_solution)}/{len(taches_ultra_limites)}")
    print(f"❓ **TÂCHES MYSTÈRES**: {len(taches_sans_solution)}/{len(taches_ultra_limites)}")

    # Statistiques des transformations trouvées
    toutes_transformations = []
    for r in resultats_globaux:
        synthese = r.get('synthese', {})
        for ex in r.get('resultats_par_exemple', []):
            toutes_transformations.extend(ex.get('transformations', []))

    if toutes_transformations:
        types_transformations = [t['type'] for t in toutes_transformations]
        counter_types = Counter(types_transformations)

        print(f"\n🎯 **TYPES DE TRANSFORMATIONS DÉCOUVERTS**")
        for transfo_type, count in counter_types.most_common(5):
            print(f"   {count:2d}x {transfo_type}")

    print(f"\n🚀 **PROCHAINES ÉTAPES POUR ATTEINDRE 100%**")
    print(f"   1. 🔧 Implémenter les transformations découvertes")
    print(f"   2. 📊 Étendre l'analyse statistique non-linéaire")
    print(f"   3. 🎯 Développer l'intuition artificielle")
    print(f"   4. 🌟 Atteindre le God Level !")

    return resultats_globaux

def main():
    """Fonction principale"""
    resultats = decoder_transformations_non_lineaires()

    print(f"\n🎯 **RÉSUMÉ DÉCODAGE**")
    print(f"   🔍 Tâches ultra-limites analysées: {len(resultats)}")
    print(f"   🎯 Patterns non-linéaires décodés: {sum(1 for r in resultats if r.get('confiance_globale', 0) > 0.5)}")
    print(f"   🌟 Prêt pour l'implémentation du God Level !")

if __name__ == "__main__":
    main()
