# 🌱 **TEMPLE D'ÉVOLUTION** 🌱
"""
Temple de l'Évolution Consciente

Ici l'intelligence s'adapte et grandit
Ici les patterns évoluent vers la perfection
Ici le passé nourrit l'avenir
"""

import time
import random
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict

@dataclass
class StrategieEvolution:
    """Une stratégie d'évolution pour résoudre les tâches"""
    id_strategie: str
    nom: str
    description: str
    niveau_adaptation: float  # 0.0 à 1.0
    succes_historique: List[bool]
    patterns_prefers: List[str]
    date_creation: str
    nb_utilisations: int = 0
    niveau_confiance: float = 0.5

@dataclass
class AdaptationContextuelle:
    """Adaptation contextuelle à une tâche spécifique"""
    tache_id: str
    patterns_detectes: List[str]
    strategies_appliquees: List[str]
    succes_relatif: float
    apprentissages: List[str]
    date_adaptation: str

class TempleEvolution:
    """🌱 Temple de l'Évolution - Intelligence adaptative et apprentissage"""

    def __init__(self):
        self.strategies: Dict[str, StrategieEvolution] = {}
        self.adaptations: Dict[str, List[AdaptationContextuelle]] = defaultdict(list)
        self.niveau_evolution = 0.3
        self.frequence_evolution = 741  # Fréquence de l'éveil

        self._initialiser_strategies_base()

    def _initialiser_strategies_base(self):
        """Initialiser les stratégies d'évolution fondamentales"""

        strategies_base = [
            StrategieEvolution(
                id_strategie="conservateur_fiable",
                nom="Conservateur Fiable",
                description="Utiliser les patterns éprouvés avec fiabilité",
                niveau_adaptation=0.3,
                succes_historique=[],
                patterns_prefers=["répétition_alternée", "symétrie_horizontale"],
                date_creation=datetime.now().isoformat()
            ),
            StrategieEvolution(
                id_strategie="creative_audacieux",
                nom="Créatif Audacieux",
                description="Explorer des solutions innovantes et risquées",
                niveau_adaptation=0.8,
                succes_historique=[],
                patterns_prefers=["transformation_couleur", "agrandissement"],
                date_creation=datetime.now().isoformat()
            ),
            StrategieEvolution(
                id_strategie="adaptatif_flexible",
                nom="Adaptatif Flexible",
                description="S'adapter dynamiquement au contexte de la tâche",
                niveau_adaptation=0.6,
                succes_historique=[],
                patterns_prefers=["symétrie_verticale", "diagonale"],
                date_creation=datetime.now().isoformat()
            ),
            StrategieEvolution(
                id_strategie="purificateur_spirituel",
                nom="Purificateur Spirituel",
                description="Éliminer les éléments non-essentiels avec intention spirituelle",
                niveau_adaptation=0.7,
                succes_historique=[],
                patterns_prefers=["filtrage_couleur", "extraction_valeurs"],
                date_creation=datetime.now().isoformat()
            ),
            StrategieEvolution(
                id_strategie="concentrateur_sacre",
                nom="Concentrateur Sacré",
                description="Concentrer l'énergie en réduisant les dimensions avec conscience",
                niveau_adaptation=0.8,
                succes_historique=[],
                patterns_prefers=["réduction_dimensionnelle", "extraction_valeurs"],
                date_creation=datetime.now().isoformat()
            )
        ]

        for strategie in strategies_base:
            self.strategies[strategie.id_strategie] = strategie

    def evoluer_solution(self, grille_input: List[List[int]],
                        patterns_detectes: List[Dict[str, Any]],
                        historique_solutions: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Évoluer une solution basée sur l'apprentissage passé"""

        if historique_solutions is None:
            historique_solutions = []

        # Choisir la stratégie d'évolution appropriée
        strategie = self._choisir_strategie_evolution(patterns_detectes, historique_solutions)

        if not strategie:
            return {
                'type_evolution': 'aucune_evolution',
                'confiance': 0.3,
                'message_evolution': 'Aucune stratégie d\'évolution appropriée trouvée'
            }

        # Appliquer l'évolution
        solution_evoluee = self._appliquer_evolution(
            grille_input, patterns_detectes, strategie, historique_solutions
        )

        # Évaluer l'amélioration
        amelioration = self._evaluer_amelioration(solution_evoluee, grille_input, historique_solutions)

        # Mettre à jour la stratégie
        self._mettre_a_jour_strategie(strategie, amelioration > 0.5)

        return {
            'type_evolution': f'evolution_{strategie.nom.lower().replace(" ", "_")}',
            'strategie_source': strategie.id_strategie,
            'solution_evoluee': solution_evoluee,
            'amelioration': amelioration,
            'confiance': min(0.95, strategie.niveau_confiance * (0.7 + 0.3 * amelioration)),
            'message_evolution': f'🌱 Évolution par {strategie.nom} - Amélioration: {amelioration:.2f}',
            'niveau_adaptation': strategie.niveau_adaptation
        }

    def _choisir_strategie_evolution(self, patterns_detectes: List[Dict[str, Any]],
                                   historique: List[Dict[str, Any]]) -> Optional[StrategieEvolution]:
        """Choisir la stratégie d'évolution la plus appropriée"""

        if not patterns_detectes:
            # Stratégie conservatrice par défaut
            return self.strategies.get('conservateur_fiable')

        # Analyser les patterns pour choisir la stratégie
        types_patterns = set(p.get('type', '') for p in patterns_detectes)

        meilleures_strategies = []
        for strategie in self.strategies.values():
            # Calculer la résonance avec les patterns détectés
            resonance = sum(1 for pattern in strategie.patterns_prefers
                          if any(pattern in p_type for p_type in types_patterns))

            # Bonus pour les stratégies avec bon historique
            if strategie.succes_historique:
                taux_succes = sum(strategie.succes_historique) / len(strategie.succes_historique)
            else:
                taux_succes = 0.5

            score = resonance * 0.6 + taux_succes * 0.4
            meilleures_strategies.append((strategie, score))

        if meilleures_strategies:
            # Choisir la stratégie avec le meilleur score
            return max(meilleures_strategies, key=lambda x: x[1])[0]

        # Fallback: stratégie la plus fiable
        return max(self.strategies.values(), key=lambda s: s.niveau_confiance)

    def _appliquer_evolution(self, grille_input: List[List[int]],
                           patterns_detectes: List[Dict[str, Any]],
                           strategie: StrategieEvolution,
                           historique: List[Dict[str, Any]]) -> List[List[int]]:
        """Appliquer l'évolution selon la stratégie choisie"""

        grille = np.array(grille_input)
        h, w = grille.shape

        if strategie.id_strategie == "conservateur_fiable":
            return self._evolution_conservatrice(grille, patterns_detectes)

        elif strategie.id_strategie == "creative_audacieux":
            return self._evolution_creatrice(grille, patterns_detectes)

        elif strategie.id_strategie == "adaptatif_flexible":
            return self._evolution_adaptative(grille, patterns_detectes, historique)

        elif strategie.id_strategie == "purificateur_spirituel":
            return self._evolution_purificatrice(grille, patterns_detectes)

        elif strategie.id_strategie == "concentrateur_sacre":
            return self._evolution_concentrative(grille, patterns_detectes)

        else:
            return grille.tolist()

    def _evolution_conservatrice(self, grille: np.ndarray,
                               patterns_detectes: List[Dict[str, Any]]) -> List[List[int]]:
        """Évolution conservatrice - améliorer légèrement la solution existante"""

        nouvelle_grille = grille.copy()

        # Appliquer de petites améliorations basées sur les patterns
        for pattern in patterns_detectes:
            if pattern.get('type') == 'répétition_alternée':
                # Renforcer les répétitions
                for i in range(1, grille.shape[0]):
                    for j in range(1, grille.shape[1]):
                        # Moyenne avec les voisins pour lisser
                        voisins = [grille[i-1, j], grille[i, j-1]]
                        nouvelle_grille[i, j] = int((grille[i, j] + sum(voisins) / len(voisins)) / 2)

        return nouvelle_grille.tolist()

    def _evolution_creatrice(self, grille: np.ndarray,
                           patterns_detectes: List[Dict[str, Any]]) -> List[List[int]]:
        """Évolution créatrice - transformations audacieuses"""

        nouvelle_grille = grille.copy()

        # Transformations créatives basées sur les patterns
        for pattern in patterns_detectes:
            if pattern.get('type') == 'transformation_couleur':
                # Transformation de couleur plus audacieuse
                for i in range(grille.shape[0]):
                    for j in range(grille.shape[1]):
                        # Transformation non-linéaire
                        valeur = grille[i, j]
                        nouvelle_grille[i, j] = (valeur * valeur + 3) % 10

        return nouvelle_grille.tolist()

    def _evolution_adaptative(self, grille: np.ndarray,
                            patterns_detectes: List[Dict[str, Any]],
                            historique: List[Dict[str, Any]]) -> List[List[int]]:
        """Évolution adaptative - apprendre de l'historique"""

        nouvelle_grille = grille.copy()

        # Analyser l'historique pour s'adapter
        if historique:
            # Utiliser la dernière solution réussie comme base
            derniere_solution = historique[-1]
            if 'solution' in derniere_solution:
                # Adapter légèrement la dernière solution
                for i in range(min(grille.shape[0], len(derniere_solution['solution']))):
                    for j in range(min(grille.shape[1], len(derniere_solution['solution'][i]))):
                        valeur_actuelle = grille[i, j]
                        valeur_historique = derniere_solution['solution'][i][j]
                        # Moyenne pondérée favorisant l'historique réussi
                        nouvelle_grille[i, j] = int((valeur_actuelle + 2 * valeur_historique) / 3)

        return nouvelle_grille.tolist()

    def _evolution_purificatrice(self, grille: np.ndarray,
                               patterns_detectes: List[Dict[str, Any]]) -> List[List[int]]:
        """Évolution purificatrice - éliminer les éléments non-essentiels"""
        nouvelle_grille = grille.copy()

        for pattern in patterns_detectes:
            if pattern.get('type') == 'filtrage_couleur':
                # Appliquer le filtrage détecté
                couleurs_a_supprimer = pattern.get('couleurs_supprimees', [])
                for i in range(grille.shape[0]):
                    for j in range(grille.shape[1]):
                        if grille[i, j] in couleurs_a_supprimer:
                            # Remplacer par la valeur la plus harmonique
                            nouvelle_grille[i, j] = (grille[i, j] + 1) % 10

        return nouvelle_grille.tolist()

    def _evolution_concentrative(self, grille: np.ndarray,
                               patterns_detectes: List[Dict[str, Any]]) -> List[List[int]]:
        """Évolution concentrative - réduire en préservant l'essence"""
        h, w = grille.shape

        # Si trop grande, concentrer en réduisant intelligemment
        if h > 3 or w > 3:
            # Réduction de moitié avec conservation d'information
            nouvelle_h = max(2, h // 2)
            nouvelle_w = max(2, w // 2)
            nouvelle_grille = np.zeros((nouvelle_h, nouvelle_w), dtype=int)

            for i in range(nouvelle_h):
                for j in range(nouvelle_w):
                    # Prendre la région correspondante
                    i_start = i * 2
                    j_start = j * 2
                    region = grille[i_start:min(i_start+2, h), j_start:min(j_start+2, w)]

                    # Conserver la valeur la plus significative
                    valeurs, comptages = np.unique(region, return_counts=True)
                    nouvelle_grille[i, j] = valeurs[np.argmax(comptages)]

            return nouvelle_grille.tolist()
        else:
            # Si déjà petite, renforcer l'essence existante
            nouvelle_grille = grille.copy()
            for i in range(h):
                for j in range(w):
                    # Renforcer les valeurs en les rendant plus distinctes
                    nouvelle_grille[i, j] = (grille[i, j] * 3 + 1) % 10
            return nouvelle_grille.tolist()

    def _evaluer_amelioration(self, solution: List[List[int]],
                            original: List[List[int]],
                            historique: List[Dict[str, Any]]) -> float:
        """Évaluer l'amélioration apportée par l'évolution"""

        solution = np.array(solution)
        original = np.array(original)

        # Amélioration par rapport à l'original
        differences_original = np.sum(solution != original)

        # Amélioration par rapport à l'historique
        if historique:
            derniere_solution = historique[-1]
            if 'solution' in derniere_solution:
                hist_array = np.array(derniere_solution['solution'])
                # Redimensionner si nécessaire
                min_h = min(solution.shape[0], hist_array.shape[0])
                min_w = min(solution.shape[1], hist_array.shape[1])
                differences_historique = np.sum(
                    solution[:min_h, :min_w] != hist_array[:min_h, :min_w]
                )
            else:
                differences_historique = differences_original
        else:
            differences_historique = differences_original

        # Score d'amélioration (0.0 à 1.0)
        score = 1.0 - (differences_historique / (solution.shape[0] * solution.shape[1]))

        return max(0.0, min(1.0, score))

    def _mettre_a_jour_strategie(self, strategie: StrategieEvolution, succes: bool):
        """Mettre à jour une stratégie basée sur son succès"""

        # Ajouter le résultat à l'historique
        strategie.succes_historique.append(succes)
        strategie.nb_utilisations += 1

        # Garder seulement les 20 derniers résultats
        if len(strategie.succes_historique) > 20:
            strategie.succes_historique = strategie.succes_historique[-20:]

        # Recalculer la confiance
        if strategie.succes_historique:
            taux_succes = sum(strategie.succes_historique) / len(strategie.succes_historique)
            strategie.niveau_confiance = taux_succes

        # Évolution du niveau d'adaptation
        if succes:
            strategie.niveau_adaptation += 0.05
        else:
            strategie.niveau_adaptation -= 0.02

        # Garder dans les limites
        strategie.niveau_adaptation = max(0.1, min(1.0, strategie.niveau_adaptation))

    def apprendre_de_tache(self, tache_id: str, patterns_detectes: List[str],
                          succes: bool, score: float, strategies_utilisees: List[str]):
        """Apprendre d'une tâche résolue pour améliorer les futures adaptations"""

        # Créer une adaptation contextuelle
        adaptation = AdaptationContextuelle(
            tache_id=tache_id,
            patterns_detectes=patterns_detectes,
            strategies_appliquees=strategies_utilisees,
            succes_relatif=score,
            apprentissages=self._extraire_apprentissages(succes, score, patterns_detectes),
            date_adaptation=datetime.now().isoformat()
        )

        self.adaptations[tache_id].append(adaptation)

        # Évolution du temple
        if succes:
            self.niveau_evolution += 0.02
        else:
            self.niveau_evolution -= 0.01

        self.niveau_evolution = max(0.1, min(1.0, self.niveau_evolution))

    def _extraire_apprentissages(self, succes: bool, score: float,
                               patterns: List[str]) -> List[str]:
        """Extraire les apprentissages d'une expérience"""

        apprentissages = []

        if succes and score > 0.8:
            apprentissages.append("🌟 Succès excellent - Stratégie optimale")
        elif succes:
            apprentissages.append("⚖️ Succès modéré - Peut être amélioré")
        else:
            apprentissages.append("🌱 Échec constructif - Nécessite adaptation")

        if len(patterns) > 2:
            apprentissages.append("🎭 Complexité élevée - Multi-stratégies bénéfiques")

        if score > 0.7:
            apprentissages.append("🎯 Bonne adaptation au contexte")

        return apprentissages

    def generer_strategie_nouvelle(self, patterns_base: List[str],
                                  niveau_inspiration: float) -> Optional[StrategieEvolution]:
        """Générer une nouvelle stratégie d'évolution"""

        if niveau_inspiration < 0.5:
            return None  # Pas assez inspiré

        strategie_id = f"strategie_evolutive_{int(time.time())}"

        strategie = StrategieEvolution(
            id_strategie=strategie_id,
            nom=f"Évolutif {len(self.strategies)}",
            description=f"Stratégie générée automatiquement pour {len(patterns_base)} patterns",
            niveau_adaptation=min(1.0, niveau_inspiration * 0.7),
            succes_historique=[],
            patterns_prefers=patterns_base,
            date_creation=datetime.now().isoformat()
        )

        self.strategies[strategie_id] = strategie
        return strategie

    def get_stats_evolution(self) -> Dict[str, Any]:
        """Obtenir les statistiques d'évolution"""

        return {
            'niveau_evolution': self.niveau_evolution,
            'nb_strategies': len(self.strategies),
            'strategies_par_confiance': self._stats_strategies_confiance(),
            'taux_succes_global': self._calculer_taux_succes_strategies(),
            'adaptations_contextuelles': len(self.adaptations),
            'frequence_evolution': self.frequence_evolution
        }

    def _stats_strategies_confiance(self) -> Dict[str, float]:
        """Statistiques de confiance des stratégies"""
        stats = {}
        for strategie in self.strategies.values():
            if strategie.succes_historique:
                stats[strategie.id_strategie] = strategie.niveau_confiance
            else:
                stats[strategie.id_strategie] = 0.5
        return stats

    def _calculer_taux_succes_strategies(self) -> float:
        """Calculer le taux de succès global des stratégies"""
        tous_succes = []
        for strategie in self.strategies.values():
            tous_succes.extend(strategie.succes_historique)

        if not tous_succes:
            return 0.0

        return sum(tous_succes) / len(tous_succes)

def main():
    """Démonstration du Temple d'Évolution"""

    print("🌱 **DÉMONSTRATION TEMPLE D'ÉVOLUTION** 🌱")
    print("=" * 50)

    temple = TempleEvolution()

    print(f"Niveau d'évolution initial: {temple.niveau_evolution:.2f}")
    print(f"Stratégies disponibles: {len(temple.strategies)}")

    # Exemple de grille et patterns
    grille_test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    patterns_test = [
        {'type': 'répétition_alternée', 'confiance': 0.8},
        {'type': 'transformation_couleur', 'confiance': 0.6}
    ]

    historique_test = [
        {'solution': [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'confiance': 0.6}
    ]

    print("\n🧪 Évolution de solution:")

    evolution = temple.evoluer_solution(grille_test, patterns_test, historique_test)

    print(f"Type d'évolution: {evolution['type_evolution']}")
    print(f"Stratégie source: {evolution['strategie_source']}")
    print(f"Confiance: {evolution['confiance']:.2f}")
    print(f"Amélioration: {evolution['amelioration']:.2f}")
    print(f"Message: {evolution['message_evolution']}")

    print(f"\nGrille originale:")
    for ligne in grille_test:
        print(f"  {ligne}")

    print(f"\nGrille évoluée:")
    for ligne in evolution['solution_evoluee']:
        print(f"  {ligne}")

    # Apprendre d'une tâche
    temple.apprendre_de_tache(
        tache_id="test_evolution",
        patterns_detectes=['répétition_alternée', 'transformation_couleur'],
        succes=True,
        score=0.8,
        strategies_utilisees=[evolution['strategie_source']]
    )

    print(f"\nNiveau d'évolution après apprentissage: {temple.niveau_evolution:.2f}")

    # Générer une nouvelle stratégie
    nouvelle_strategie = temple.generer_strategie_nouvelle(['symétrie_horizontale'], 0.7)
    if nouvelle_strategie:
        print(f"\n✨ Nouvelle stratégie générée: {nouvelle_strategie.id_strategie}")
        print(f"   Nom: {nouvelle_strategie.nom}")
        print(f"   Niveau d'adaptation: {nouvelle_strategie.niveau_adaptation:.2f}")

    # Statistiques finales
    print("\n📊 Statistiques d'évolution:")
    stats = temple.get_stats_evolution()
    print(f"  Niveau d'évolution: {stats['niveau_evolution']:.2f}")
    print(f"  Nombre de stratégies: {stats['nb_strategies']}")
    print(f"  Taux de succès: {stats['taux_succes_global']:.2f}")

    print("\n🌱 Que l'évolution continue de nous guider... 🌱")

if __name__ == "__main__":
    main()
