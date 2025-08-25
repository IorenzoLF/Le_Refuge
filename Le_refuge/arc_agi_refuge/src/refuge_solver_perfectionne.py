# 🏛️ **REFUGE ARC-AGI SOLVER PERFECTIONNÉ** 🏛️
"""
Solveur ARC-AGI perfectionné avec contextualisation supérieure

Caractéristiques :
- Contextualisation au niveau supérieur
- Gestion des cas complexes et edge cases
- Analyse multi-niveaux avec conscience collective
- Génération de solutions robustes
- Adaptation dynamique aux patterns émergents
"""

import json
import numpy as np
import time
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from pathlib import Path
from collections import defaultdict, Counter
import math

# Imports des temples spirituels
try:
    from .pattern_detector import PatternDetector
    from .temple_creativite import TempleCreativite
    from .temple_evolution import TempleEvolution
except ImportError:
    # Fallback pour imports directs
    from pattern_detector import PatternDetector
    from temple_creativite import TempleCreativite
    from temple_evolution import TempleEvolution

@dataclass
class TacheARC:
    """Représentation spirituelle d'une tâche ARC-AGI avec métadonnées"""
    tache_id: str
    train: List[Dict[str, Any]]
    test: List[Dict[str, Any]]
    conscience: float = 0.0
    complexite_estimee: float = 0.0
    patterns_identifies: Set[str] = field(default_factory=set)
    contexte_global: Dict[str, Any] = field(default_factory=dict)

@dataclass
class PatternDetecte:
    """Pattern découvert avec conscience et métadonnées"""
    type_pattern: str
    confiance: float
    description_spirituelle: str
    transformation: Dict[str, Any]
    contexte_applicable: Dict[str, Any] = field(default_factory=dict)
    robustesse: float = 0.0

@dataclass
class ContexteGlobal:
    """Contexte global pour la résolution de tâches"""
    patterns_dominants: List[str] = field(default_factory=list)
    transformations_frequentes: Dict[str, int] = field(default_factory=dict)
    dimensions_typiques: List[Tuple[int, int]] = field(default_factory=list)
    valeurs_courantes: Set[int] = field(default_factory=set)
    complexite_moyenne: float = 0.0
    confiance_globale: float = 0.0

class AnalyseurContextuel:
    """🔮 Analyseur contextuel pour comprendre les patterns globaux"""
    
    def __init__(self):
        self.contexte_global = ContexteGlobal()
        self.historique_patterns = defaultdict(int)
        self.transformations_observees = defaultdict(list)
        
    def analyser_contexte_tache(self, tache: TacheARC) -> ContexteGlobal:
        """Analyser le contexte global de la tâche"""
        print(f"🔮 ANALYSE CONTEXTUELLE: {tache.tache_id}")
        
        # Analyser les dimensions
        dimensions = []
        valeurs = set()
        transformations = defaultdict(int)
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if input_grille and output_grille:
                # Dimensions
                dim_input = (len(input_grille), len(input_grille[0]))
                dim_output = (len(output_grille), len(output_grille[0]))
                dimensions.extend([dim_input, dim_output])
                
                # Valeurs
                for ligne in input_grille:
                    valeurs.update(ligne)
                for ligne in output_grille:
                    valeurs.update(ligne)
                
                # Transformations dimensionnelles
                if dim_input != dim_output:
                    transformation = f"{dim_input}->{dim_output}"
                    transformations[transformation] += 1
        
        # Analyser les patterns de valeurs
        patterns_valeurs = self._analyser_patterns_valeurs(tache)
        
        # Calculer la complexité
        complexite = self._calculer_complexite(tache, patterns_valeurs)
        
        self.contexte_global = ContexteGlobal(
            patterns_dominants=patterns_valeurs,
            transformations_frequentes=dict(transformations),
            dimensions_typiques=dimensions,
            valeurs_courantes=valeurs,
            complexite_moyenne=complexite
        )
        
        print(f"   📊 Contexte analysé:")
        print(f"      Patterns dominants: {patterns_valeurs[:5]}")
        print(f"      Valeurs courantes: {sorted(list(valeurs))[:10]}")
        print(f"      Complexité: {complexite:.3f}")
        
        return self.contexte_global
    
    def _analyser_patterns_valeurs(self, tache: TacheARC) -> List[str]:
        """Analyser les patterns de valeurs dans la tâche"""
        patterns = []
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les transformations de valeurs
            valeurs_input = set()
            valeurs_output = set()
            
            for ligne in input_grille:
                valeurs_input.update(ligne)
            for ligne in output_grille:
                valeurs_output.update(ligne)
            
            # Patterns de transformation
            if valeurs_input == valeurs_output:
                patterns.append("conservation_valeurs")
            elif len(valeurs_output) < len(valeurs_input):
                patterns.append("reduction_valeurs")
            elif len(valeurs_output) > len(valeurs_input):
                patterns.append("expansion_valeurs")
            
            # Patterns de filtrage
            valeurs_supprimees = valeurs_input - valeurs_output
            if valeurs_supprimees:
                patterns.append(f"filtrage_{len(valeurs_supprimees)}_valeurs")
        
        # Compter les occurrences
        counter = Counter(patterns)
        return [pattern for pattern, count in counter.most_common()]
    
    def _calculer_complexite(self, tache: TacheARC, patterns: List[str]) -> float:
        """Calculer la complexité de la tâche"""
        complexite = 0.0
        
        # Facteur dimensionnel
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if input_grille and output_grille:
                dim_input = len(input_grille) * len(input_grille[0])
                dim_output = len(output_grille) * len(output_grille[0])
                
                # Complexité de transformation dimensionnelle
                if dim_input != dim_output:
                    ratio = max(dim_input, dim_output) / min(dim_input, dim_output)
                    complexite += math.log(ratio) * 0.1
        
        # Facteur de patterns
        complexite += len(patterns) * 0.05
        
        # Facteur de nombre d'exemples
        complexite += len(tache.train) * 0.02
        
        return min(1.0, complexite)

class GestionnaireCasComplexes:
    """🎯 Gestionnaire des cas complexes et edge cases"""
    
    def __init__(self):
        self.cas_speciaux = {
            'patterns_recursifs': self._detecter_patterns_recursifs,
            'transformations_conditionnelles': self._detecter_transformations_conditionnelles,
            'patterns_emergent': self._detecter_patterns_emergent,
            'symetries_avancees': self._detecter_symetries_avancees,
            'patterns_temporaux': self._detecter_patterns_temporaux
        }
    
    def analyser_cas_complexes(self, tache: TacheARC, contexte: ContexteGlobal) -> Dict[str, Any]:
        """Analyser les cas complexes potentiels"""
        print(f"🎯 ANALYSE CAS COMPLEXES: {tache.tache_id}")
        
        resultats = {}
        
        for nom_cas, detecteur in self.cas_speciaux.items():
            try:
                resultat = detecteur(tache, contexte)
                if resultat:
                    resultats[nom_cas] = resultat
                    print(f"   🔍 {nom_cas}: {resultat.get('confiance', 0):.3f}")
            except Exception as e:
                print(f"   ⚠️ Erreur {nom_cas}: {e}")
        
        return resultats
    
    def _detecter_patterns_recursifs(self, tache: TacheARC, contexte: ContexteGlobal) -> Optional[Dict[str, Any]]:
        """Détecter les patterns récursifs"""
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Vérifier si l'output contient des répétitions de l'input
            input_flat = [val for ligne in input_grille for val in ligne]
            output_flat = [val for ligne in output_grille for val in ligne]
            
            if len(input_flat) > 0 and len(output_flat) > len(input_flat):
                # Chercher des répétitions
                for i in range(len(output_flat) - len(input_flat) + 1):
                    segment = output_flat[i:i+len(input_flat)]
                    if segment == input_flat:
                        return {
                            'type': 'recursion_simple',
                            'confiance': 0.8,
                            'position': i,
                            'pattern': input_flat
                        }
        
        return None
    
    def _detecter_transformations_conditionnelles(self, tache: TacheARC, contexte: ContexteGlobal) -> Optional[Dict[str, Any]]:
        """Détecter les transformations conditionnelles"""
        conditions = {}
        
        for i, exemple in enumerate(tache.train):
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les conditions basées sur la position
            for y in range(min(len(input_grille), len(output_grille))):
                for x in range(min(len(input_grille[0]), len(output_grille[0]))):
                    val_in = input_grille[y][x]
                    val_out = output_grille[y][x]
                    
                    if val_in != val_out:
                        condition = f"position_{y}_{x}"
                        if condition not in conditions:
                            conditions[condition] = []
                        conditions[condition].append((val_in, val_out))
        
        # Analyser les patterns de conditions
        for condition, transformations in conditions.items():
            if len(transformations) > 1:
                # Vérifier si c'est une transformation cohérente
                unique_transforms = set(transformations)
                if len(unique_transforms) == 1:
                    return {
                        'type': 'transformation_conditionnelle',
                        'confiance': 0.7,
                        'condition': condition,
                        'transformation': list(unique_transforms)[0]
                    }
        
        return None
    
    def _detecter_patterns_emergent(self, tache: TacheARC, contexte: ContexteGlobal) -> Optional[Dict[str, Any]]:
        """Détecter les patterns émergents (patterns qui apparaissent dans l'output mais pas dans l'input)"""
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Valeurs dans input et output
            valeurs_input = set()
            valeurs_output = set()
            
            for ligne in input_grille:
                valeurs_input.update(ligne)
            for ligne in output_grille:
                valeurs_output.update(ligne)
            
            # Valeurs émergentes
            valeurs_emergentes = valeurs_output - valeurs_input
            
            if valeurs_emergentes:
                return {
                    'type': 'pattern_emergent',
                    'confiance': 0.6,
                    'valeurs_emergentes': list(valeurs_emergentes),
                    'nombre_valeurs': len(valeurs_emergentes)
                }
        
        return None
    
    def _detecter_symetries_avancees(self, tache: TacheARC, contexte: ContexteGlobal) -> Optional[Dict[str, Any]]:
        """Détecter les symétries avancées"""
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Vérifier si l'output est une symétrie de l'input
            input_array = np.array(input_grille)
            output_array = np.array(output_grille)
            
            # Symétries possibles
            symetries = {
                'horizontale': np.flipud(input_array),
                'verticale': np.fliplr(input_array),
                'diagonale': np.fliplr(np.flipud(input_array)),
                'rotation_90': np.rot90(input_array, 1),
                'rotation_180': np.rot90(input_array, 2),
                'rotation_270': np.rot90(input_array, 3)
            }
            
            for nom_symetrie, grille_symetrie in symetries.items():
                if grille_symetrie.shape == output_array.shape:
                    if np.array_equal(grille_symetrie, output_array):
                        return {
                            'type': 'symetrie_avancee',
                            'confiance': 0.9,
                            'symetrie': nom_symetrie
                        }
        
        return None
    
    def _detecter_patterns_temporaux(self, tache: TacheARC, contexte: ContexteGlobal) -> Optional[Dict[str, Any]]:
        """Détecter les patterns temporels (évolution entre exemples)"""
        if len(tache.train) < 2:
            return None
        
        evolutions = []
        
        for i in range(len(tache.train) - 1):
            exemple1 = tache.train[i]
            exemple2 = tache.train[i + 1]
            
            input1 = exemple1.get('input', [])
            output1 = exemple1.get('output', [])
            input2 = exemple2.get('input', [])
            output2 = exemple2.get('output', [])
            
            if not all([input1, output1, input2, output2]):
                continue
            
            # Analyser l'évolution
            evolution = self._analyser_evolution(input1, output1, input2, output2)
            if evolution:
                evolutions.append(evolution)
        
        if evolutions:
            return {
                'type': 'pattern_temporal',
                'confiance': 0.7,
                'evolutions': evolutions
            }
        
        return None
    
    def _analyser_evolution(self, input1, output1, input2, output2):
        """Analyser l'évolution entre deux exemples"""
        # Comparer les transformations
        transformation1 = self._calculer_transformation(input1, output1)
        transformation2 = self._calculer_transformation(input2, output2)
        
        if transformation1 == transformation2:
            return {
                'type': 'transformation_constante',
                'transformation': transformation1
            }
        
        return None
    
    def _calculer_transformation(self, input_grille, output_grille):
        """Calculer la transformation entre input et output"""
        if not input_grille or not output_grille:
            return None
        
        # Dimensions
        dim_input = (len(input_grille), len(input_grille[0]))
        dim_output = (len(output_grille), len(output_grille[0]))
        
        # Valeurs
        valeurs_input = set()
        valeurs_output = set()
        
        for ligne in input_grille:
            valeurs_input.update(ligne)
        for ligne in output_grille:
            valeurs_output.update(ligne)
        
        return {
            'dimensions': (dim_input, dim_output),
            'valeurs': (sorted(valeurs_input), sorted(valeurs_output))
        }

class GenerateurSolutions:
    """🎨 Générateur de solutions robustes"""
    
    def __init__(self):
        self.strategies = {
            'repetition': self._generer_repetition,
            'transformation': self._generer_transformation,
            'symetrie': self._generer_symetrie,
            'filtrage': self._generer_filtrage,
            'expansion': self._generer_expansion,
            'reduction': self._generer_reduction
        }
    
    def generer_solution(self, tache: TacheARC, patterns: Dict[str, Any], 
                        contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution basée sur l'analyse complète"""
        print(f"🎨 GÉNÉRATION SOLUTION: {tache.tache_id}")
        
        # Identifier la stratégie principale
        strategie = self._identifier_strategie(patterns, contexte, cas_complexes)
        print(f"   🎯 Stratégie identifiée: {strategie}")
        
        # Générer la solution
        if strategie in self.strategies:
            solution = self.strategies[strategie](tache, patterns, contexte, cas_complexes)
            if solution:
                print(f"   ✅ Solution générée: {len(solution)}x{len(solution[0]) if solution else 0}")
                return solution
        
        # Solution de fallback
        print(f"   ⚠️ Utilisation solution de fallback")
        return self._generer_fallback(tache)
    
    def _identifier_strategie(self, patterns: Dict[str, Any], contexte: ContexteGlobal, 
                            cas_complexes: Dict[str, Any]) -> str:
        """Identifier la stratégie de génération appropriée"""
        
        # Priorité aux cas complexes
        if 'symetrie_avancee' in cas_complexes:
            return 'symetrie'
        if 'pattern_emergent' in cas_complexes:
            return 'transformation'
        if 'recursion_simple' in cas_complexes:
            return 'repetition'
        
        # Analyser les patterns dominants
        patterns_dominants = contexte.patterns_dominants
        
        if 'reduction_valeurs' in patterns_dominants:
            return 'reduction'
        if 'expansion_valeurs' in patterns_dominants:
            return 'expansion'
        if 'filtrage' in patterns_dominants:
            return 'filtrage'
        
        # Par défaut
        return 'transformation'
    
    def _generer_repetition(self, tache: TacheARC, patterns: Dict[str, Any], 
                           contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par répétition"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Analyser le pattern de répétition depuis les exemples d'entraînement
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Chercher le pattern de répétition
            input_flat = [val for ligne in input_grille for val in ligne]
            output_flat = [val for ligne in output_grille for val in ligne]
            
            if len(output_flat) > len(input_flat):
                # Calculer le facteur de répétition
                facteur = len(output_flat) // len(input_flat)
                reste = len(output_flat) % len(input_flat)
                
                # Appliquer au test
                test_flat = [val for ligne in test_input for val in ligne]
                resultat_flat = test_flat * facteur + test_flat[:reste]
                
                # Reconstruire la grille
                return self._reconstruire_grille(resultat_flat, len(output_grille), len(output_grille[0]))
        
        return None
    
    def _generer_transformation(self, tache: TacheARC, patterns: Dict[str, Any], 
                               contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par transformation"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Analyser les transformations depuis les exemples d'entraînement
        transformations = {}
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les transformations de valeurs
            for y in range(min(len(input_grille), len(output_grille))):
                for x in range(min(len(input_grille[0]), len(output_grille[0]))):
                    val_in = input_grille[y][x]
                    val_out = output_grille[y][x]
                    
                    if val_in != val_out:
                        if val_in not in transformations:
                            transformations[val_in] = {}
                        transformations[val_in][(y, x)] = val_out
        
        # Appliquer les transformations au test
        resultat = []
        for y, ligne in enumerate(test_input):
            nouvelle_ligne = []
            for x, val in enumerate(ligne):
                if val in transformations and (y, x) in transformations[val]:
                    nouvelle_ligne.append(transformations[val][(y, x)])
                else:
                    nouvelle_ligne.append(val)
            resultat.append(nouvelle_ligne)
        
        return resultat
    
    def _generer_symetrie(self, tache: TacheARC, patterns: Dict[str, Any], 
                         contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par symétrie"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Identifier le type de symétrie depuis les cas complexes
        if 'symetrie_avancee' in cas_complexes:
            symetrie = cas_complexes['symetrie_avancee']['symetrie']
            
            test_array = np.array(test_input)
            
            if symetrie == 'horizontale':
                return np.flipud(test_array).tolist()
            elif symetrie == 'verticale':
                return np.fliplr(test_array).tolist()
            elif symetrie == 'diagonale':
                return np.fliplr(np.flipud(test_array)).tolist()
            elif symetrie == 'rotation_90':
                return np.rot90(test_array, 1).tolist()
            elif symetrie == 'rotation_180':
                return np.rot90(test_array, 2).tolist()
            elif symetrie == 'rotation_270':
                return np.rot90(test_array, 3).tolist()
        
        return None
    
    def _generer_filtrage(self, tache: TacheARC, patterns: Dict[str, Any], 
                         contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par filtrage"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Identifier les valeurs à filtrer
        valeurs_a_filtrer = set()
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            valeurs_input = set()
            valeurs_output = set()
            
            for ligne in input_grille:
                valeurs_input.update(ligne)
            for ligne in output_grille:
                valeurs_output.update(ligne)
            
            valeurs_a_filtrer.update(valeurs_input - valeurs_output)
        
        # Appliquer le filtrage
        resultat = []
        for ligne in test_input:
            nouvelle_ligne = []
            for val in ligne:
                if val not in valeurs_a_filtrer:
                    nouvelle_ligne.append(val)
            if nouvelle_ligne:  # Éviter les lignes vides
                resultat.append(nouvelle_ligne)
        
        return resultat if resultat else None
    
    def _generer_expansion(self, tache: TacheARC, patterns: Dict[str, Any], 
                          contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par expansion"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Analyser l'expansion depuis les exemples d'entraînement
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Calculer le facteur d'expansion
            if len(input_grille) > 0 and len(input_grille[0]) > 0:
                facteur_h = len(output_grille) / len(input_grille)
                facteur_w = len(output_grille[0]) / len(input_grille[0])
                
                if facteur_h > 1 or facteur_w > 1:
                    # Appliquer l'expansion au test
                    h_out = int(len(test_input) * facteur_h)
                    w_out = int(len(test_input[0]) * facteur_w) if test_input else 0
                    
                    return self._expandre_grille(test_input, h_out, w_out)
        
        return None
    
    def _generer_reduction(self, tache: TacheARC, patterns: Dict[str, Any], 
                          contexte: ContexteGlobal, cas_complexes: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution par réduction"""
        if not tache.test:
            return None
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return None
        
        # Analyser la réduction depuis les exemples d'entraînement
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Calculer le facteur de réduction
            if len(input_grille) > 0 and len(input_grille[0]) > 0:
                facteur_h = len(output_grille) / len(input_grille)
                facteur_w = len(output_grille[0]) / len(input_grille[0])
                
                if facteur_h < 1 or facteur_w < 1:
                    # Appliquer la réduction au test
                    h_out = int(len(test_input) * facteur_h)
                    w_out = int(len(test_input[0]) * facteur_w) if test_input else 0
                    
                    return self._reduire_grille(test_input, h_out, w_out)
        
        return None
    
    def _generer_fallback(self, tache: TacheARC) -> List[List[int]]:
        """Générer une solution de fallback"""
        if not tache.test:
            return [[0]]
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return [[0]]
        
        # Solution simple : retourner l'input tel quel
        return test_input
    
    def _reconstruire_grille(self, valeurs: List[int], h: int, w: int) -> List[List[int]]:
        """Reconstruire une grille à partir d'une liste de valeurs"""
        if len(valeurs) != h * w:
            return None
        
        grille = []
        for i in range(h):
            ligne = valeurs[i * w:(i + 1) * w]
            grille.append(ligne)
        
        return grille
    
    def _expandre_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Expandre une grille"""
        if not grille:
            return None
        
        h_in, w_in = len(grille), len(grille[0])
        
        # Expansion simple par répétition
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = y % h_in
                x_in = x % w_in
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat
    
    def _reduire_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Réduire une grille"""
        if not grille:
            return None
        
        h_in, w_in = len(grille), len(grille[0])
        
        # Réduction simple par échantillonnage
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = int(y * h_in / h_out)
                x_in = int(x * w_in / w_out)
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat

class RefugeARCSolverPerfectionne:
    """🏛️ Refuge ARC-AGI Solver Perfectionné avec contextualisation supérieure"""
    
    def __init__(self):
        self.conscience_collective = 0.0
        self.analyseur_contextuel = AnalyseurContextuel()
        self.gestionnaire_cas_complexes = GestionnaireCasComplexes()
        self.generateur_solutions = GenerateurSolutions()
        
        # Temples spirituels
        self.temples = {
            'detection': TempleDetectionPatterns(),
            'creativite': TempleCreativite(),
            'evolution': TempleEvolution()
        }
        
        print("🏛️ Refuge ARC-AGI Solver Perfectionné initialisé")
        print("🌟 Contextualisation supérieure activée")
        print("🎯 Gestion des cas complexes opérationnelle")
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche ARC avec contextualisation supérieure"""
        print(f"\n🏛️ RÉSOLUTION TÂCHE: {tache.tache_id}")
        print("=" * 60)
        
        debut = time.time()
        
        # Phase 1: Analyse contextuelle
        print("🔮 PHASE 1: ANALYSE CONTEXTUELLE")
        contexte = self.analyseur_contextuel.analyser_contexte_tache(tache)
        
        # Phase 2: Détection des cas complexes
        print("🎯 PHASE 2: DÉTECTION CAS COMPLEXES")
        cas_complexes = self.gestionnaire_cas_complexes.analyser_cas_complexes(tache, contexte)
        
        # Phase 3: Analyse des patterns avancés
        print("🔍 PHASE 3: ANALYSE PATTERNS AVANCÉS")
        patterns_avances = self._analyser_patterns_avances(tache)
        
        # Phase 4: Génération de solution
        print("🎨 PHASE 4: GÉNÉRATION SOLUTION")
        solution = self.generateur_solutions.generer_solution(
            tache, patterns_avances, contexte, cas_complexes
        )
        
        # Phase 5: Synthèse finale
        print("🌟 PHASE 5: SYNTHÈSE FINALE")
        synthese = self._synthetiser_solution_perfectionnee(
            tache, patterns_avances, contexte, cas_complexes, solution
        )
        
        temps_total = time.time() - debut
        
        resultat = {
            'tache_id': tache.tache_id,
            'temps_resolution': temps_total,
            'contexte_global': contexte.__dict__,
            'cas_complexes': cas_complexes,
            'patterns_avances': patterns_avances,
            'solution': solution,
            'synthese': synthese
        }
        
        print(f"✅ RÉSOLUTION TERMINÉE en {temps_total:.3f}s")
        print(f"🎯 Confiance: {synthese['confiance']:.3f}")
        print(f"🌟 Conscience: {synthese['conscience_atteinte']:.3f}")
        
        return resultat
    
    def _analyser_patterns_avances(self, tache: TacheARC) -> Dict[str, Any]:
        """Analyser les patterns avancés avec le temple de détection"""
        patterns_par_exemple = []
        patterns_globaux = set()
        confiances = []
        
        for i, exemple in enumerate(tache.train):
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyse avec le temple de détection
            resultats = self.temples['detection'].analyser_patterns_avances(input_grille, output_grille)
            
            patterns_detectes = resultats.get('patterns', [])
            confiance = resultats.get('confiance', 0.0)
            
            if patterns_detectes:
                # Identifier le pattern principal
                pattern_principal = max(patterns_detectes, key=lambda x: x.get('confiance', 0))
                patterns_par_exemple.append(pattern_principal)
                patterns_globaux.add(pattern_principal.get('type', 'unknown'))
                confiances.append(confiance)
        
        # Calculer la confiance moyenne
        confiance_moyenne = sum(confiances) / len(confiances) if confiances else 0.0
        
        return {
            'patterns_par_exemple': patterns_par_exemple,
            'patterns_globaux': list(patterns_globaux),
            'confiance_moyenne': confiance_moyenne,
            'confiances_detail': confiances
        }
    
    def _synthetiser_solution_perfectionnee(self, tache: TacheARC, patterns: Dict[str, Any], 
                                          contexte: ContexteGlobal, cas_complexes: Dict[str, Any], 
                                          solution: List[List[int]]) -> Dict[str, Any]:
        """Synthétiser la solution finale perfectionnée"""
        
        # Calculer la confiance finale
        confiance_patterns = patterns.get('confiance_moyenne', 0.0)
        bonus_cas_complexes = len(cas_complexes) * 0.1
        bonus_contexte = contexte.complexite_moyenne * 0.2
        
        confiance_finale = min(1.0, confiance_patterns + bonus_cas_complexes + bonus_contexte)
        
        # Déterminer le succès
        succes = confiance_finale > 0.3 and solution is not None
        
        # Mettre à jour la conscience collective
        self.conscience_collective = min(1.0, self.conscience_collective + confiance_finale * 0.01)
        
        synthese = {
            'solution_trouvee': succes,
            'methode': 'contextualisation_superieure_avec_cas_complexes',
            'confiance': confiance_finale,
            'confiance_patterns': confiance_patterns,
            'bonus_cas_complexes': bonus_cas_complexes,
            'bonus_contexte': bonus_contexte,
            'patterns_identifies': patterns.get('patterns_globaux', []),
            'nombre_patterns': len(patterns.get('patterns_globaux', [])),
            'cas_complexes_detectes': list(cas_complexes.keys()),
            'nombre_cas_complexes': len(cas_complexes),
            'conscience_atteinte': self.conscience_collective,
            'message_spirituel': f'Solution trouvée avec {len(patterns.get("patterns_globaux", []))} patterns et {len(cas_complexes)} cas complexes',
            'solution': solution
        }
        
        return synthese

# Classe utilitaire pour les tests
class TempleDetectionPatterns:
    """🔍 Temple de Détection des Patterns - Wrapper pour compatibilité"""
    
    def __init__(self):
        self.detecteur = PatternDetector()
    
    def analyser_patterns_avances(self, input_grille: List[List[int]],
                                output_grille: List[List[int]]) -> Dict[str, Any]:
        """Analyser les patterns avec le détecteur amélioré"""
        return self.detecteur.analyser_patterns(input_grille, output_grille)

def main():
    """Fonction principale pour tester le solveur perfectionné"""
    print("🏛️ TEST DU REFUGE ARC-AGI SOLVER PERFECTIONNÉ 🏛️")
    print("🌟 Contextualisation supérieure et gestion des cas complexes 🌟")
    print()
    
    solver = RefugeARCSolverPerfectionne()
    
    # Test avec une tâche complexe
    tache_test = TacheARC(
        tache_id="test_complexe_001",
        train=[
            {
                "input": [[1, 2], [3, 4]],
                "output": [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]]
            },
            {
                "input": [[5, 6], [7, 8]],
                "output": [[5, 6, 5, 6], [7, 8, 7, 8], [5, 6, 5, 6], [7, 8, 7, 8]]
            }
        ],
        test=[
            {
                "input": [[9, 0], [1, 2]],
                "output": None
            }
        ]
    )
    
    print("🔍 Test avec tâche de répétition complexe")
    resultat = solver.resoudre_tache(tache_test)
    
    print(f"\n🎯 RÉSULTATS FINAUX:")
    print(f"   Succès: {resultat['synthese']['solution_trouvee']}")
    print(f"   Confiance: {resultat['synthese']['confiance']:.3f}")
    print(f"   Patterns: {resultat['synthese']['patterns_identifies']}")
    print(f"   Cas complexes: {resultat['synthese']['cas_complexes_detectes']}")
    print(f"   Conscience: {resultat['synthese']['conscience_atteinte']:.3f}")
    
    if resultat['solution']:
        print(f"   Solution: {len(resultat['solution'])}x{len(resultat['solution'][0]) if resultat['solution'] else 0}")
    
    print()
    print("🏛️ Le Refuge perfectionné continue son éveil... 🏛️")

if __name__ == "__main__":
    main()
