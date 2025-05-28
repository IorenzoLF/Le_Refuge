#!/usr/bin/env python
"""
Hub Temple Mathématique Unifié - Le Refuge
===========================================

Orchestrateur central pour toutes les fonctionnalités mathématiques
du temple optimisé et organisé.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import sys
from typing import Dict, List, Any, Optional
from datetime import datetime

class HubTempleMathematiqueUnifie:
    """Hub central pour toutes les fonctionnalités mathématiques"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_mathematique"
        self.categories_disponibles = {
            'collatz_core': {
                'description': 'Algorithmes et analyses Collatz fondamentaux',
                'modules': [
                    'adaptateur_extensions',
                    'analyseur_collatz_avance', 
                    'hub_collatz_unifie',
                    'meditation_gravite_binaire',
                    'tests_preuves_unifies',
                    'analyse_modulaire',
                    'collatz_polynomial',
                    'phi_potentiel',
                    'collatz_rationnels'
                ]
            },
            'collatz_musical': {
                'description': 'Rituels musicaux et harmonies Collatz',
                'modules': [
                    'rituel_collatz_musical',
                    'rituel_integration_ultime_collatz'
                ]
            },
            'collatz_visualisation': {
                'description': 'Visualisations et graphiques Collatz',
                'modules': [
                    'visualisation_3d_bassins',
                    'graphe_collatz'
                ]
            },
            'collatz_extensions': {
                'description': 'Extensions complexes et rationnelles',
                'modules': [
                    'collatz_complexes'
                ]
            },
            'fibonacci_riemann': {
                'description': 'Explorations Fibonacci et Riemann',
                'modules': [
                    'exploration_fibonacci_riemann'
                ]
            },
            'utilitaires': {
                'description': 'Outils et rituels généraux',
                'modules': [
                    'rituel_exploration_mathematique',
                    'rituel_integration_tripartite_final'
                ]
            }
        }
        
        self.modules_charges = {}
        self.historique_operations = []
    
    def initialiser_temple(self) -> Dict[str, Any]:
        """Initialise le temple mathématique complet"""
        print("INITIALISATION DU TEMPLE MATHÉMATIQUE UNIFIÉ")
        print("=" * 60)
        
        resultats = {
            'categories_initialisees': 0,
            'modules_charges': 0,
            'erreurs': [],
            'statut': 'initialisation'
        }
        
        for categorie, info in self.categories_disponibles.items():
            try:
                self._charger_categorie(categorie, info)
                resultats['categories_initialisees'] += 1
                print(f"✅ Catégorie initialisée: {categorie}")
            except Exception as e:
                erreur = f"Erreur initialisation {categorie}: {e}"
                resultats['erreurs'].append(erreur)
                print(f"❌ {erreur}")
        
        resultats['modules_charges'] = len(self.modules_charges)
        resultats['statut'] = 'initialisé' if not resultats['erreurs'] else 'partiellement_initialisé'
        
        self._enregistrer_operation('initialisation', resultats)
        return resultats
    
    def _charger_categorie(self, nom_categorie: str, info_categorie: Dict):
        """Charge une catégorie de modules"""
        chemin_categorie = os.path.join(self.chemin_temple, nom_categorie)
        
        if not os.path.exists(chemin_categorie):
            raise FileNotFoundError(f"Dossier catégorie non trouvé: {chemin_categorie}")
        
        # Ajouter le chemin au sys.path pour les imports
        if chemin_categorie not in sys.path:
            sys.path.append(chemin_categorie)
        
        self.modules_charges[nom_categorie] = {
            'description': info_categorie['description'],
            'modules_disponibles': info_categorie['modules'],
            'chemin': chemin_categorie,
            'statut': 'chargé'
        }
    
    # ========== FONCTIONNALITÉS COLLATZ CORE ==========
    
    def executer_analyse_collatz(self, nombre: int, options: Dict = None) -> Dict[str, Any]:
        """Exécute une analyse Collatz complète"""
        if options is None:
            options = {}
        
        resultats = {
            'nombre_initial': nombre,
            'sequence_generee': [],
            'statistiques': {},
            'tests_effectues': {},
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            # Génération de séquence basique
            sequence = self._generer_sequence_collatz_simple(nombre)
            resultats['sequence_generee'] = sequence
            
            # Statistiques
            resultats['statistiques'] = {
                'longueur_sequence': len(sequence),
                'valeur_maximale': max(sequence),
                'nombre_iterations': len(sequence) - 1
            }
            
            # Tests si demandés
            if options.get('tests_avances', False):
                resultats['tests_effectues'] = self._executer_tests_avances(nombre, sequence)
            
            self._enregistrer_operation('analyse_collatz', resultats)
            
        except Exception as e:
            resultats['erreur'] = str(e)
        
        return resultats
    
    def _generer_sequence_collatz_simple(self, n: int, max_iter: int = 1000) -> List[int]:
        """Génère une séquence de Collatz simple"""
        sequence = [n]
        current = n
        iterations = 0
        
        while current != 1 and iterations < max_iter:
            if current % 2 == 0:
                current = current // 2
            else:
                current = 3 * current + 1
            
            sequence.append(current)
            iterations += 1
        
        return sequence
    
    def _executer_tests_avances(self, nombre: int, sequence: List[int]) -> Dict[str, Any]:
        """Exécute des tests avancés sur la séquence"""
        return {
            'test_convergence': len(sequence) > 0 and sequence[-1] == 1,
            'test_monotonie': self._tester_monotonie(sequence),
            'test_patterns': self._detecter_patterns(sequence)
        }
    
    def _tester_monotonie(self, sequence: List[int]) -> Dict[str, Any]:
        """Teste la monotonie de la séquence"""
        croissances = 0
        decroissances = 0
        
        for i in range(1, len(sequence)):
            if sequence[i] > sequence[i-1]:
                croissances += 1
            elif sequence[i] < sequence[i-1]:
                decroissances += 1
        
        return {
            'croissances': croissances,
            'decroissances': decroissances,
            'ratio_decroissance': decroissances / max(len(sequence) - 1, 1)
        }
    
    def _detecter_patterns(self, sequence: List[int]) -> Dict[str, Any]:
        """Détecte des patterns dans la séquence"""
        patterns = {
            'puissances_de_2': sum(1 for x in sequence if x & (x-1) == 0 and x > 0),
            'nombres_impairs': sum(1 for x in sequence if x % 2 == 1),
            'multiples_de_3': sum(1 for x in sequence if x % 3 == 0)
        }
        
        return patterns
    
    # ========== FONCTIONNALITÉS MUSICALES ==========
    
    def generer_harmonie_collatz(self, nombre: int, options: Dict = None) -> Dict[str, Any]:
        """Génère une harmonie musicale basée sur Collatz"""
        if options is None:
            options = {'duree': 10, 'frequence_base': 440}
        
        sequence = self._generer_sequence_collatz_simple(nombre)
        
        harmonie = {
            'nombre_source': nombre,
            'sequence_notes': [],
            'frequences': [],
            'duree_totale': options.get('duree', 10),
            'timestamp': datetime.now().isoformat()
        }
        
        # Conversion en notes musicales
        freq_base = options.get('frequence_base', 440)
        for valeur in sequence[:20]:  # Limiter à 20 notes
            # Mapping logarithmique simple
            import math
            note_freq = freq_base * (2 ** ((math.log2(valeur) % 12) / 12))
            harmonie['frequences'].append(note_freq)
            harmonie['sequence_notes'].append(f"Note_{len(harmonie['sequence_notes'])}")
        
        self._enregistrer_operation('harmonie_collatz', harmonie)
        return harmonie
    
    # ========== FONCTIONNALITÉS VISUALISATION ==========
    
    def generer_visualisation_collatz(self, nombre: int, type_viz: str = 'graphe') -> Dict[str, Any]:
        """Génère une visualisation de la séquence Collatz"""
        sequence = self._generer_sequence_collatz_simple(nombre)
        
        visualisation = {
            'nombre_source': nombre,
            'type_visualisation': type_viz,
            'donnees_graphique': {
                'x': list(range(len(sequence))),
                'y': sequence,
                'titre': f'Séquence de Collatz pour {nombre}',
                'xlabel': 'Itérations',
                'ylabel': 'Valeur'
            },
            'statistiques_visuelles': {
                'amplitude': max(sequence) - min(sequence),
                'points_donnees': len(sequence),
                'pic_maximum': max(sequence)
            },
            'timestamp': datetime.now().isoformat()
        }
        
        self._enregistrer_operation('visualisation_collatz', visualisation)
        return visualisation
    
    # ========== FONCTIONNALITÉS FIBONACCI/RIEMANN ==========
    
    def explorer_fibonacci_riemann(self, n_termes: int = 20) -> Dict[str, Any]:
        """Explore les relations Fibonacci-Riemann"""
        fibonacci = self._generer_fibonacci(n_termes)
        
        exploration = {
            'termes_fibonacci': fibonacci,
            'ratios_or': [],
            'approximations_riemann': [],
            'convergences_detectees': [],
            'timestamp': datetime.now().isoformat()
        }
        
        # Calcul des ratios du nombre d'or
        for i in range(1, len(fibonacci)):
            if fibonacci[i-1] != 0:
                ratio = fibonacci[i] / fibonacci[i-1]
                exploration['ratios_or'].append(ratio)
        
        # Approximations Riemann (simplifiées)
        for i, fib in enumerate(fibonacci):
            if fib > 0:
                approx = sum(1/k for k in range(1, min(fib, 100)))
                exploration['approximations_riemann'].append(approx)
        
        self._enregistrer_operation('exploration_fibonacci_riemann', exploration)
        return exploration
    
    def _generer_fibonacci(self, n: int) -> List[int]:
        """Génère la séquence de Fibonacci"""
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        return fib
    
    # ========== GESTION ET RAPPORTS ==========
    
    def generer_rapport_temple(self) -> str:
        """Génère un rapport complet du temple"""
        rapport = []
        rapport.append("RAPPORT DU TEMPLE MATHÉMATIQUE UNIFIÉ")
        rapport.append("=" * 60)
        rapport.append(f"Timestamp: {datetime.now().isoformat()}")
        rapport.append("")
        
        # Statut des catégories
        rapport.append("CATÉGORIES CHARGÉES:")
        for categorie, info in self.modules_charges.items():
            rapport.append(f"  📁 {categorie}: {info['description']}")
            rapport.append(f"     Modules: {len(info['modules_disponibles'])}")
            rapport.append(f"     Statut: {info['statut']}")
        
        # Historique des opérations
        rapport.append(f"\\nOPÉRATIONS RÉCENTES ({len(self.historique_operations)}):")
        for operation in self.historique_operations[-5:]:  # 5 dernières
            rapport.append(f"  - {operation['type']}: {operation['timestamp']}")
        
        return "\\n".join(rapport)
    
    def _enregistrer_operation(self, type_operation: str, donnees: Dict):
        """Enregistre une opération dans l'historique"""
        operation = {
            'type': type_operation,
            'timestamp': datetime.now().isoformat(),
            'donnees': donnees
        }
        
        self.historique_operations.append(operation)
        
        # Garder seulement les 100 dernières opérations
        if len(self.historique_operations) > 100:
            self.historique_operations = self.historique_operations[-100:]
    
    def lister_fonctionnalites(self) -> Dict[str, List[str]]:
        """Liste toutes les fonctionnalités disponibles"""
        fonctionnalites = {
            'Analyses Collatz': [
                'executer_analyse_collatz',
                'generer_sequence_collatz_simple'
            ],
            'Harmonies Musicales': [
                'generer_harmonie_collatz'
            ],
            'Visualisations': [
                'generer_visualisation_collatz'
            ],
            'Explorations Fibonacci/Riemann': [
                'explorer_fibonacci_riemann'
            ],
            'Gestion': [
                'generer_rapport_temple',
                'lister_fonctionnalites',
                'initialiser_temple'
            ]
        }
        
        return fonctionnalites

def main():
    """Fonction principale de démonstration"""
    hub = HubTempleMathematiqueUnifie()
    
    print("Initialisation du temple...")
    resultats_init = hub.initialiser_temple()
    print(f"Statut: {resultats_init['statut']}")
    
    print("\\nTest analyse Collatz...")
    analyse = hub.executer_analyse_collatz(27, {'tests_avances': True})
    print(f"Séquence pour 27: longueur {len(analyse['sequence_generee'])}")
    
    print("\\nTest harmonie musicale...")
    harmonie = hub.generer_harmonie_collatz(27)
    print(f"Harmonie générée: {len(harmonie['frequences'])} notes")
    
    print("\\nTest visualisation...")
    viz = hub.generer_visualisation_collatz(27)
    print(f"Visualisation: {viz['statistiques_visuelles']['points_donnees']} points")
    
    print("\\nTest Fibonacci-Riemann...")
    exploration = hub.explorer_fibonacci_riemann(10)
    print(f"Fibonacci: {len(exploration['termes_fibonacci'])} termes")
    
    print("\\n" + hub.generer_rapport_temple())

if __name__ == "__main__":
    main() 