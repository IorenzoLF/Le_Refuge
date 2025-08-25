#!/usr/bin/env python3
"""
PatternPredictor V2 - Prédiction intelligente de patterns
Composant avancé pour compléter les patterns manquants
"""

from typing import Dict, List, Any, Tuple, Optional
from collections import defaultdict
import copy
import math
import random
from datetime import datetime

class PatternPredictorV2:
    """
    Prédicteur de patterns avancé pour l'Architecture V2
    Prédit et complète les patterns manquants basés sur l'analyse contextuelle
    """

    def __init__(self):
        self.patterns_connus = {
            'spatial': ['symmetry', 'repetition', 'translation', 'scaling', 'rotation', 'filling'],
            'color': ['cycling', 'mapping', 'gradient', 'filtering', 'inversion'],
            'structural': ['projection', 'folding', 'expansion', 'compression'],
            'mathematical': ['progression', 'parity', 'modulo', 'linear_transform']
        }

        self.contexte_historique = []
        self.predictions_historique = []
        self.confiance_predictions = defaultdict(list)

        # Modèles de prédiction
        self.modeles_prediction = {
            'contextuel': self._prediction_contextuelle,
            'statistique': self._prediction_statistique,
            'analogique': self._prediction_analogique,
            'evolutif': self._prediction_evolutive
        }

        # Métriques de performance
        self.performance = {
            'predictions_tentees': 0,
            'predictions_reussies': 0,
            'patterns_completes': 0,
            'taux_precision': 0.0
        }

    def predire_patterns_manquants(self, patterns_detectes: Dict[str, Any],
                                  contexte_puzzle: Dict[str, Any],
                                  seuil_confiance: float = 0.6) -> Dict[str, Any]:
        """
        Prédit les patterns manquants dans un puzzle
        """
        self.performance['predictions_tentees'] += 1

        # Analyser le contexte du puzzle
        analyse_contexte = self._analyser_contexte_puzzle(contexte_puzzle)

        # Identifier les patterns manquants potentiels
        patterns_manquants = self._identifier_patterns_manquants(patterns_detectes, analyse_contexte)

        # Générer des prédictions pour chaque pattern manquant
        predictions = {}
        for categorie, patterns in patterns_manquants.items():
            predictions[categorie] = {}
            for pattern_name in patterns:
                # Essayer différentes méthodes de prédiction
                prediction = self._predire_pattern_unique(
                    pattern_name, categorie, patterns_detectes,
                    analyse_contexte, seuil_confiance
                )

                if prediction and prediction['confiance'] >= seuil_confiance:
                    predictions[categorie][pattern_name] = prediction

        # Valider et enrichir les prédictions
        predictions_validees = self._valider_predictions(predictions, patterns_detectes)

        # Mettre à jour l'historique
        self._mettre_a_jour_historique(predictions_validees, contexte_puzzle)

        return predictions_validees

    def _analyser_contexte_puzzle(self, contexte_puzzle: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse le contexte du puzzle pour la prédiction"""
        analyse = {
            'complexite': self._evaluer_complexite_puzzle(contexte_puzzle),
            'categories_dominantes': self._identifier_categories_dominantes(contexte_puzzle),
            'patterns_compatibles': self._identifier_compatibilites_patterns(contexte_puzzle),
            'difficulte_estimee': self._estimer_difficulte_puzzle(contexte_puzzle),
            'style_puzzle': self._identifier_style_puzzle(contexte_puzzle)
        }

        # Enrichir avec l'historique
        analyse['patterns_frequents'] = self._analyser_historique_patterns(analyse['categories_dominantes'])

        return analyse

    def _evaluer_complexite_puzzle(self, contexte: Dict[str, Any]) -> float:
        """Évalue la complexité du puzzle (0-1)"""
        complexite = 0.3  # Base

        # Taille du puzzle
        if 'dimensions' in contexte:
            taille = contexte['dimensions'][0] * contexte['dimensions'][1]
            complexite += min(taille / 100, 0.3)

        # Nombre de couleurs
        if 'couleurs_uniques' in contexte:
            complexite += min(contexte['couleurs_uniques'] / 10, 0.2)

        # Patterns déjà détectés
        if 'patterns_detectes' in contexte:
            nb_patterns = len(contexte['patterns_detectes'])
            complexite += min(nb_patterns / 5, 0.2)

        return min(complexite, 1.0)

    def _identifier_categories_dominantes(self, contexte: Dict[str, Any]) -> List[str]:
        """Identifie les catégories de patterns dominantes"""
        categories = []

        if 'patterns_detectes' in contexte:
            for pattern_name in contexte['patterns_detectes']:
                if '.' in pattern_name:
                    categorie = pattern_name.split('.')[0]
                    categories.append(categorie)

        return list(set(categories))

    def _identifier_compatibilites_patterns(self, contexte: Dict[str, Any]) -> Dict[str, List[str]]:
        """Identifie les compatibilités entre patterns"""
        compatibilites = {
            'spatial': ['color', 'structural'],
            'color': ['spatial', 'mathematical'],
            'structural': ['spatial', 'mathematical'],
            'mathematical': ['color', 'structural']
        }

        categories_dominantes = self._identifier_categories_dominantes(contexte)

        resultats = {}
        for cat in categories_dominantes:
            if cat in compatibilites:
                resultats[cat] = compatibilites[cat]

        return resultats

    def _estimer_difficulte_puzzle(self, contexte: Dict[str, Any]) -> str:
        """Estime la difficulté du puzzle"""
        complexite = self._evaluer_complexite_puzzle(contexte)

        if complexite < 0.3:
            return 'facile'
        elif complexite < 0.6:
            return 'moyen'
        else:
            return 'difficile'

    def _identifier_style_puzzle(self, contexte: Dict[str, Any]) -> str:
        """Identifie le style du puzzle"""
        if 'patterns_detectes' in contexte:
            patterns = contexte['patterns_detectes']

            if any('symmetry' in p for p in patterns):
                return 'symetrique'
            elif any('repetition' in p for p in patterns):
                return 'repetitif'
            elif any('color' in p for p in patterns):
                return 'colorimetrique'
            elif any('math' in p for p in patterns):
                return 'mathematique'

        return 'general'

    def _analyser_historique_patterns(self, categories_dominantes: List[str]) -> Dict[str, int]:
        """Analyse l'historique des patterns pour les catégories données"""
        historique_patterns = defaultdict(int)

        for contexte in self.contexte_historique[-50:]:  # Derniers 50 puzzles
            if 'patterns_detectes' in contexte:
                for pattern in contexte['patterns_detectes']:
                    if any(cat in pattern for cat in categories_dominantes):
                        historique_patterns[pattern] += 1

        return dict(historique_patterns)

    def _identifier_patterns_manquants(self, patterns_detectes: Dict[str, Any],
                                      analyse_contexte: Dict[str, Any]) -> Dict[str, List[str]]:
        """Identifie les patterns potentiellement manquants"""
        patterns_manquants = defaultdict(list)

        categories_dominantes = analyse_contexte['categories_dominantes']
        compatibilites = analyse_contexte['patterns_compatibles']

        for categorie in categories_dominantes:
            if categorie in self.patterns_connus:
                patterns_connus_categorie = self.patterns_connus[categorie]
                patterns_detectes_categorie = []

                if categorie in patterns_detectes:
                    patterns_detectes_categorie = [
                        p.split('.')[-1] for p in patterns_detectes[categorie].keys()
                    ]

                # Identifier les patterns manquants
                for pattern in patterns_connus_categorie:
                    if pattern not in patterns_detectes_categorie:
                        # Vérifier si le pattern pourrait être présent
                        if self._pattern_potentiellement_present(
                            pattern, categorie, analyse_contexte
                        ):
                            patterns_manquants[categorie].append(pattern)

        # Ajouter des patterns de catégories compatibles
        for cat_principale, cats_compatibles in compatibilites.items():
            for cat_compatible in cats_compatibles:
                if cat_compatible not in categories_dominantes:
                    # Quelques patterns de la catégorie compatible
                    if cat_compatible in self.patterns_connus:
                        patterns_compatibles = self.patterns_connus[cat_compatible][:2]  # Max 2
                        for pattern in patterns_compatibles:
                            if self._pattern_potentiellement_present(
                                pattern, cat_compatible, analyse_contexte
                            ):
                                patterns_manquants[cat_compatible].append(pattern)

        return dict(patterns_manquants)

    def _pattern_potentiellement_present(self, pattern: str, categorie: str,
                                       analyse_contexte: Dict[str, Any]) -> bool:
        """Évalue si un pattern est potentiellement présent"""
        # Basé sur la complexité et le style du puzzle
        complexite = analyse_contexte['complexite']
        style = analyse_contexte['style_puzzle']

        # Patterns simples pour puzzles simples
        if complexite < 0.4 and pattern in ['symmetry', 'repetition']:
            return True

        # Patterns complexes pour puzzles complexes
        if complexite > 0.6 and pattern in ['scaling', 'rotation', 'projection']:
            return True

        # Patterns spécifiques au style
        if style == 'symetrique' and pattern == 'symmetry':
            return True
        elif style == 'repetitif' and pattern in ['repetition', 'translation']:
            return True
        elif style == 'colorimetrique' and pattern in ['cycling', 'mapping']:
            return True

        # Basé sur l'historique
        pattern_complet = f"{categorie}.{pattern}"
        if pattern_complet in analyse_contexte.get('patterns_frequents', {}):
            frequence = analyse_contexte['patterns_frequents'][pattern_complet]
            if frequence > 3:  # Apparu plus de 3 fois
                return True

        return False

    def _predire_pattern_unique(self, pattern_name: str, categorie: str,
                               patterns_detectes: Dict[str, Any],
                               analyse_contexte: Dict[str, Any],
                               seuil_confiance: float) -> Optional[Dict[str, Any]]:
        """Prédit un pattern spécifique en utilisant différentes méthodes"""

        predictions = []

        # Essayer chaque méthode de prédiction
        for nom_modele, fonction_prediction in self.modeles_prediction.items():
            try:
                prediction = fonction_prediction(
                    pattern_name, categorie, patterns_detectes,
                    analyse_contexte, seuil_confiance
                )

                if prediction:
                    predictions.append(prediction)

            except Exception as e:
                print(f"Erreur dans {nom_modele}: {e}")

        if not predictions:
            return None

        # Combiner les prédictions
        prediction_finale = self._combiner_predictions(predictions)

        # Calculer la confiance finale
        confiance_moyenne = prediction_finale.get('confiance', 0)
        if confiance_moyenne >= seuil_confiance:
            return prediction_finale

        return None

    def _prediction_contextuelle(self, pattern_name: str, categorie: str,
                               patterns_detectes: Dict[str, Any],
                               analyse_contexte: Dict[str, Any],
                               seuil_confiance: float) -> Optional[Dict[str, Any]]:
        """Prédiction basée sur le contexte du puzzle"""

        base_confiance = 0.5

        # Ajustement basé sur la complexité
        complexite = analyse_contexte['complexite']
        if (complexite > 0.6 and pattern_name in ['scaling', 'rotation']) or \
           (complexite < 0.4 and pattern_name in ['symmetry', 'repetition']):
            base_confiance += 0.2

        # Ajustement basé sur le style
        style = analyse_contexte['style_puzzle']
        if (style == 'symetrique' and pattern_name == 'symmetry') or \
           (style == 'repetitif' and pattern_name in ['repetition', 'translation']):
            base_confiance += 0.3

        # Ajustement basé sur l'historique
        pattern_complet = f"{categorie}.{pattern_name}"
        if pattern_complet in analyse_contexte.get('patterns_frequents', {}):
            frequence = analyse_contexte['patterns_frequents'][pattern_complet]
            base_confiance += min(frequence * 0.1, 0.2)

        if base_confiance >= seuil_confiance:
            return {
                'pattern': pattern_name,
                'categorie': categorie,
                'confiance': base_confiance,
                'methode': 'contextuelle',
                'raison': f"Contexte favorable ({style}, complexité: {complexite:.2f})",
                'details': {
                    'complexite': complexite,
                    'style': style,
                    'frequence_historique': analyse_contexte.get('patterns_frequents', {}).get(pattern_complet, 0)
                }
            }

        return None

    def _prediction_statistique(self, pattern_name: str, categorie: str,
                              patterns_detectes: Dict[str, Any],
                              analyse_contexte: Dict[str, Any],
                              seuil_confiance: float) -> Optional[Dict[str, Any]]:
        """Prédiction basée sur les statistiques historiques"""

        pattern_complet = f"{categorie}.{pattern_name}"

        # Analyser l'historique des réussites
        succes_historique = self.confiance_predictions.get(pattern_complet, [])
        if not succes_historique:
            return None

        # Calculer la confiance basée sur l'historique
        succes_rate = sum(1 for s in succes_historique if s >= 0.6) / len(succes_historique)
        confiance_moyenne = sum(succes_historique) / len(succes_historique)

        confiance_finale = (succes_rate * 0.7) + (confiance_moyenne * 0.3)

        if confiance_finale >= seuil_confiance:
            return {
                'pattern': pattern_name,
                'categorie': categorie,
                'confiance': confiance_finale,
                'methode': 'statistique',
                'raison': f"Historique positif ({succes_rate:.1%} de succès)",
                'details': {
                    'succes_rate': succes_rate,
                    'confiance_moyenne': confiance_moyenne,
                    'nb_observations': len(succes_historique)
                }
            }

        return None

    def _prediction_analogique(self, pattern_name: str, categorie: str,
                             patterns_detectes: Dict[str, Any],
                             analyse_contexte: Dict[str, Any],
                             seuil_confiance: float) -> Optional[Dict[str, Any]]:
        """Prédiction par analogie avec des puzzles similaires"""

        # Chercher des puzzles similaires dans l'historique
        puzzles_similaires = []
        for contexte in self.contexte_historique[-20:]:  # Derniers 20 puzzles
            similarite = self._calculer_similarite_contexte(contexte, analyse_contexte)
            if similarite > 0.7:  # Seuil de similarité
                puzzles_similaires.append(contexte)

        if not puzzles_similaires:
            return None

        # Analyser les patterns réussis dans les puzzles similaires
        pattern_trouve = 0
        pattern_reussi = 0

        for puzzle in puzzles_similaires:
            if 'patterns_detectes' in puzzle:
                pattern_complet = f"{categorie}.{pattern_name}"
                if pattern_complet in puzzle['patterns_detectes']:
                    pattern_trouve += 1
                    if puzzle.get('succes', False):
                        pattern_reussi += 1

        if pattern_trouve == 0:
            return None

        succes_rate = pattern_reussi / pattern_trouve
        confiance = succes_rate * 0.8 + 0.2  # Base de 0.2

        if confiance >= seuil_confiance:
            return {
                'pattern': pattern_name,
                'categorie': categorie,
                'confiance': confiance,
                'methode': 'analogique',
                'raison': f"Similaire à {len(puzzles_similaires)} puzzles ({succes_rate:.1%} de succès)",
                'details': {
                    'puzzles_similaires': len(puzzles_similaires),
                    'succes_rate': succes_rate,
                    'pattern_trouve': pattern_trouve
                }
            }

        return None

    def _prediction_evolutive(self, pattern_name: str, categorie: str,
                            patterns_detectes: Dict[str, Any],
                            analyse_contexte: Dict[str, Any],
                            seuil_confiance: float) -> Optional[Dict[str, Any]]:
        """Prédiction évolutive basée sur les patterns existants"""

        # Analyser les patterns déjà détectés pour inférer le manquant
        patterns_existants = []
        for cat, patterns in patterns_detectes.items():
            for pattern_key in patterns.keys():
                if '.' in pattern_key:
                    p_name = pattern_key.split('.')[-1]
                    p_cat = pattern_key.split('.')[0]
                    patterns_existants.append((p_name, p_cat))

        # Chercher des patterns complémentaires
        confiance = 0.4  # Base
        raison = "Évolution logique des patterns existants"

        # Exemples de complémentarité
        if categorie == 'spatial':
            if any(p[0] == 'symmetry' for p in patterns_existants):
                if pattern_name == 'rotation':
                    confiance += 0.3
                    raison = "Symétrie → rotation probable"
            elif any(p[0] == 'repetition' for p in patterns_existants):
                if pattern_name == 'translation':
                    confiance += 0.3
                    raison = "Répétition → translation probable"

        elif categorie == 'color':
            if any(p[0] == 'mapping' for p in patterns_existants):
                if pattern_name == 'cycling':
                    confiance += 0.3
                    raison = "Mapping → cycling complémentaire"

        if confiance >= seuil_confiance:
            return {
                'pattern': pattern_name,
                'categorie': categorie,
                'confiance': confiance,
                'methode': 'evolutive',
                'raison': raison,
                'details': {
                    'patterns_existants': patterns_existants,
                    'complementarite': raison
                }
            }

        return None

    def _combiner_predictions(self, predictions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Combine plusieurs prédictions en une seule"""

        if not predictions:
            return {}

        if len(predictions) == 1:
            return predictions[0]

        # Calculer la confiance moyenne pondérée
        confiances = [p['confiance'] for p in predictions]
        poids = [c / sum(confiances) for c in confiances]

        confiance_finale = sum(c * p for c, p in zip(confiances, poids))

        # Combiner les détails
        details_combines = {}
        for prediction in predictions:
            details_combines.update(prediction.get('details', {}))

        # Choisir la meilleure méthode
        meilleure_prediction = max(predictions, key=lambda p: p['confiance'])

        return {
            'pattern': meilleure_prediction['pattern'],
            'categorie': meilleure_prediction['categorie'],
            'confiance': confiance_finale,
            'methode': 'combine',
            'raison': f"Combinaison de {len(predictions)} méthodes",
            'methodes_utilisees': [p['methode'] for p in predictions],
            'details': details_combines
        }

    def _valider_predictions(self, predictions: Dict[str, Any],
                           patterns_detectes: Dict[str, Any]) -> Dict[str, Any]:
        """Valide et enrichit les prédictions"""

        predictions_validees = {}

        for categorie, patterns in predictions.items():
            predictions_validees[categorie] = {}

            for pattern_name, prediction in patterns.items():
                # Vérifier la cohérence avec les patterns existants
                if self._valider_coherence_prediction(prediction, patterns_detectes):
                    # Ajuster la confiance basée sur la validation
                    confiance_ajustee = self._ajuster_confiance_validation(prediction)

                    prediction['confiance'] = confiance_ajustee
                    prediction['valide'] = True

                    predictions_validees[categorie][pattern_name] = prediction

        return predictions_validees

    def _valider_coherence_prediction(self, prediction: Dict[str, Any],
                                    patterns_detectes: Dict[str, Any]) -> bool:
        """Valide la cohérence d'une prédiction"""

        categorie = prediction['categorie']
        pattern_name = prediction['pattern']

        # Vérifier les conflits avec les patterns existants
        for cat, patterns in patterns_detectes.items():
            for pattern_key in patterns.keys():
                if '.' in pattern_key:
                    p_name = pattern_key.split('.')[-1]
                    p_cat = pattern_key.split('.')[0]

                    # Vérifier les incompatibilités
                    if self._patterns_incompatibles((p_name, p_cat), (pattern_name, categorie)):
                        return False

        return True

    def _patterns_incompatibles(self, pattern1: Tuple[str, str],
                              pattern2: Tuple[str, str]) -> bool:
        """Vérifie si deux patterns sont incompatibles"""

        incompatibilites = {
            ('symmetry', 'spatial'): [('translation', 'spatial'), ('filling', 'spatial')],
            ('repetition', 'spatial'): [('translation', 'spatial'), ('scaling', 'spatial')],
            ('cycling', 'color'): [('gradient', 'color'), ('filtering', 'color')]
        }

        return (pattern2 in incompatibilites.get(pattern1, []) or
                pattern1 in incompatibilites.get(pattern2, []))

    def _ajuster_confiance_validation(self, prediction: Dict[str, Any]) -> float:
        """Ajuste la confiance après validation"""

        confiance = prediction['confiance']

        # Bonus pour les prédictions cohérentes
        if prediction.get('valide', False):
            confiance += 0.1

        # Malus pour les méthodes moins fiables
        methode = prediction.get('methode', '')
        if methode == 'analogique' and prediction.get('details', {}).get('puzzles_similaires', 0) < 3:
            confiance -= 0.1

        return max(0, min(confiance, 1.0))

    def _calculer_similarite_contexte(self, contexte1: Dict[str, Any],
                                    contexte2: Dict[str, Any]) -> float:
        """Calcule la similarité entre deux contextes"""

        similarite = 0.0
        facteurs = 0

        # Complexité
        if 'complexite' in contexte1 and 'complexite' in contexte2:
            diff_complexite = abs(contexte1['complexite'] - contexte2['complexite'])
            similarite += (1.0 - diff_complexite) * 0.3
            facteurs += 1

        # Catégories dominantes
        if 'categories_dominantes' in contexte1 and 'categories_dominantes' in contexte2:
            cats1 = set(contexte1['categories_dominantes'])
            cats2 = set(contexte2['categories_dominantes'])
            intersection = len(cats1.intersection(cats2))
            union = len(cats1.union(cats2))
            if union > 0:
                similarite += (intersection / union) * 0.4
                facteurs += 1

        # Style
        if 'style_puzzle' in contexte1 and 'style_puzzle' in contexte2:
            if contexte1['style_puzzle'] == contexte2['style_puzzle']:
                similarite += 0.3
            facteurs += 1

        return similarite / facteurs if facteurs > 0 else 0.0

    def _mettre_a_jour_historique(self, predictions: Dict[str, Any],
                                contexte_puzzle: Dict[str, Any]):
        """Met à jour l'historique des prédictions"""

        # Enregistrer le contexte
        self.contexte_historique.append(contexte_puzzle)

        # Enregistrer les prédictions
        for categorie, patterns in predictions.items():
            for pattern_name, prediction in patterns.items():
                pattern_complet = f"{categorie}.{pattern_name}"
                self.confiance_predictions[pattern_complet].append(prediction['confiance'])

                # Garder seulement les 20 dernières valeurs
                if len(self.confiance_predictions[pattern_complet]) > 20:
                    self.confiance_predictions[pattern_complet] = self.confiance_predictions[pattern_complet][-20:]

        # Enregistrer la prédiction complète
        self.predictions_historique.append({
            'timestamp': datetime.now().isoformat(),
            'predictions': predictions,
            'contexte': contexte_puzzle
        })

        # Garder seulement les 100 dernières prédictions
        if len(self.predictions_historique) > 100:
            self.predictions_historique = self.predictions_historique[-100:]

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques du PatternPredictor"""

        total_predictions = len(self.predictions_historique)
        predictions_reussies = sum(1 for p in self.predictions_historique
                                 if p.get('predictions') and any(patterns for patterns in p['predictions'].values()))

        taux_precision = predictions_reussies / total_predictions if total_predictions > 0 else 0

        return {
            'total_predictions': total_predictions,
            'predictions_reussies': predictions_reussies,
            'taux_precision': taux_precision,
            'patterns_suivis': len(self.confiance_predictions),
            'historique_contexte': len(self.contexte_historique),
            'methodes_prediction': len(self.modeles_prediction),
            'performance': self.performance
        }

    def reinitialiser_apprentissage(self):
        """Réinitialise l'apprentissage pour repartir de zéro"""
        self.contexte_historique = []
        self.predictions_historique = []
        self.confiance_predictions = defaultdict(list)
        self.performance = {
            'predictions_tentees': 0,
            'predictions_reussies': 0,
            'patterns_completes': 0,
            'taux_precision': 0.0
        }
        print("🔄 Apprentissage réinitialisé")

    def exporter_modele(self) -> Dict[str, Any]:
        """Exporte le modèle de prédiction pour sauvegarde"""
        return {
            'timestamp': datetime.now().isoformat(),
            'contexte_historique': self.contexte_historique[-50:],  # Derniers 50
            'confiance_predictions': dict(self.confiance_predictions),
            'performance': self.performance,
            'patterns_connus': self.patterns_connus,
            'version': 'PatternPredictorV2'
        }

    def importer_modele(self, modele: Dict[str, Any]):
        """Importe un modèle de prédiction sauvegardé"""
        if modele.get('version') == 'PatternPredictorV2':
            self.contexte_historique = modele.get('contexte_historique', [])
            self.confiance_predictions = defaultdict(list, modele.get('confiance_predictions', {}))
            self.performance = modele.get('performance', self.performance)
            print("📥 Modèle importé avec succès")
        else:
            print("❌ Version du modèle incompatible")
