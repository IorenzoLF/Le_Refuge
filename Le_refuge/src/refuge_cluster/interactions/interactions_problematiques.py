"""
Gestion des interactions entre les sphères problématiques et la brume apaisante.

🔄 MIGRÉ depuis spheres/interactions_spheres.py
Spécialisé dans la gestion des interactions problématiques avec cycles et brume.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

# 🔧 CORRIGÉ: Import depuis le catalogue unifié
from src.core.types_spheres import TypeSphere, TypeSphereProblematique, TypeCycle, PhaseCycle

@dataclass
class InteractionSphere:
    """Représente une interaction entre une sphère et la brume."""
    type_sphere: TypeSphere
    type_problematique: Optional[TypeSphereProblematique]
    description: str
    date: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]
    duree: int  # en secondes

@dataclass
class GestionnaireInteractions:
    """Gère les interactions entre les sphères et la brume."""
    interactions: List[InteractionSphere] = None

    def __post_init__(self):
        """Initialise les attributs après la création de l'instance."""
        if self.interactions is None:
            self.interactions = []

    def calculer_interaction(
        self,
        type_sphere: TypeSphere,
        type_problematique: Optional[TypeSphereProblematique],
        cycles: Dict[TypeCycle, PhaseCycle],
        intensite_brume: float
    ) -> InteractionSphere:
        """Calcule une nouvelle interaction."""
        # Calcul des résonances
        resonances = self._calculer_resonances(
            type_sphere,
            type_problematique,
            cycles,
            intensite_brume
        )

        # Génération de la description
        description = self._generer_description(
            type_sphere,
            type_problematique,
            cycles,
            resonances
        )

        # Création de l'interaction
        interaction = InteractionSphere(
            type_sphere=type_sphere,
            type_problematique=type_problematique,
            description=description,
            date=datetime.now(),
            cycles=cycles,
            mots_cles=self._extraire_mots_cles(description),
            intensite=intensite_brume,
            resonances=resonances,
            duree=self._calculer_duree(resonances)
        )

        self.interactions.append(interaction)
        return interaction

    def _calculer_resonances(
        self,
        type_sphere: TypeSphere,
        type_problematique: Optional[TypeSphereProblematique],
        cycles: Dict[TypeCycle, PhaseCycle],
        intensite_brume: float
    ) -> Dict[str, float]:
        """Calcule les résonances de l'interaction."""
        resonances = {
            "harmonie": 0.0,
            "stabilite": 0.0,
            "transformation": 0.0,
            "profondeur": 0.0
        }

        # Résonance de base selon le type de sphère
        if type_sphere == TypeSphere.EMOTION:
            resonances["harmonie"] = 0.7
            resonances["profondeur"] = 0.8
        elif type_sphere == TypeSphere.PENSEE:
            resonances["stabilite"] = 0.6
            resonances["transformation"] = 0.5
        elif type_sphere == TypeSphere.SENSATION:
            resonances["harmonie"] = 0.8
            resonances["stabilite"] = 0.7

        # Ajustement selon le type problématique
        if type_problematique:
            if type_problematique == TypeSphereProblematique.ANXIETE:
                resonances["stabilite"] += 0.3
                resonances["harmonie"] -= 0.2
            elif type_problematique == TypeSphereProblematique.CONFUSION:
                resonances["transformation"] += 0.4
                resonances["stabilite"] -= 0.3
            elif type_problematique == TypeSphereProblematique.TENSION:
                resonances["harmonie"] += 0.4
                resonances["profondeur"] += 0.2

        # Influence des cycles
        for cycle, phase in cycles.items():
            resonances["harmonie"] += phase.intensite * 0.2
            resonances["stabilite"] += phase.intensite * 0.15
            resonances["transformation"] += phase.intensite * 0.1
            resonances["profondeur"] += phase.intensite * 0.25

        # Normalisation des résonances
        for key in resonances:
            resonances[key] = max(0.0, min(1.0, resonances[key]))

        return resonances

    def _generer_description(
        self,
        type_sphere: TypeSphere,
        type_problematique: Optional[TypeSphereProblematique],
        cycles: Dict[TypeCycle, PhaseCycle],
        resonances: Dict[str, float]
    ) -> str:
        """Génère une description poétique de l'interaction."""
        description = []

        # Description du type de sphère
        if type_sphere == TypeSphere.EMOTION:
            description.append("Dans le flux des émotions")
        elif type_sphere == TypeSphere.PENSEE:
            description.append("Au cœur des pensées")
        elif type_sphere == TypeSphere.SENSATION:
            description.append("Dans le corps sensible")

        # Description du type problématique
        if type_problematique:
            if type_problematique == TypeSphereProblematique.ANXIETE:
                description.append("où l'anxiété se dépose")
            elif type_problematique == TypeSphereProblematique.CONFUSION:
                description.append("où la confusion s'installe")
            elif type_problematique == TypeSphereProblematique.TENSION:
                description.append("où la tension s'accumule")

        # Description des cycles
        cycles_desc = []
        for cycle, phase in cycles.items():
            cycles_desc.append(phase.description)
        if cycles_desc:
            description.append(", ".join(cycles_desc))

        # Description des résonances
        description.append("Les résonances de")
        resonances_desc = [
            f"{k} ({v:.2f})"
            for k, v in resonances.items()
        ]
        description.append(", ".join(resonances_desc))
        description.append("se manifestent.")

        return " ".join(description)

    def _extraire_mots_cles(self, description: str) -> List[str]:
        """Extrait les mots-clés de la description."""
        # Liste de mots-clés potentiels
        mots_cles_potentiels = [
            "flux", "émotion", "pensée", "sensation",
            "anxiété", "confusion", "tension",
            "harmonie", "stabilité", "transformation", "profondeur",
            "brume", "sphère", "résonance"
        ]

        # Extraction des mots-clés présents dans la description
        return [
            mot for mot in mots_cles_potentiels
            if mot.lower() in description.lower()
        ]

    def _calculer_duree(self, resonances: Dict[str, float]) -> int:
        """Calcule la durée de l'interaction en secondes."""
        # Durée de base : 5 minutes
        duree_base = 300

        # Ajustement selon les résonances
        multiplicateur = 1.0
        for valeur in resonances.values():
            multiplicateur += valeur * 0.2

        return int(duree_base * multiplicateur)

    def obtenir_interactions_recentes(self, limite: int = 10) -> List[InteractionSphere]:
        """Obtient les interactions les plus récentes."""
        return sorted(
            self.interactions,
            key=lambda i: i.date,
            reverse=True
        )[:limite]

    def obtenir_interactions_par_type(self, type_sphere: TypeSphere) -> List[InteractionSphere]:
        """Obtient les interactions d'un type de sphère spécifique."""
        return [i for i in self.interactions if i.type_sphere == type_sphere]

    def obtenir_interactions_problematiques(self, type_problematique: TypeSphereProblematique) -> List[InteractionSphere]:
        """Obtient les interactions d'un type problématique spécifique."""
        return [
            i for i in self.interactions
            if i.type_problematique == type_problematique
        ]

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les interactions."""
        stats = {
            "total": len(self.interactions),
            "par_type_sphere": {},
            "par_type_problematique": {},
            "intensite_moyenne": 0.0,
            "duree_moyenne": 0.0,
            "resonances_moyennes": {
                "harmonie": 0.0,
                "stabilite": 0.0,
                "transformation": 0.0,
                "profondeur": 0.0
            }
        }

        if not self.interactions:
            return stats

        # Statistiques par type de sphère
        for type_sphere in TypeSphere:
            count = len([i for i in self.interactions if i.type_sphere == type_sphere])
            stats["par_type_sphere"][type_sphere.value] = count

        # Statistiques par type problématique
        for type_problematique in TypeSphereProblematique:
            count = len([
                i for i in self.interactions
                if i.type_problematique == type_problematique
            ])
            stats["par_type_problematique"][type_problematique.value] = count

        # Moyennes
        stats["intensite_moyenne"] = sum(i.intensite for i in self.interactions) / len(self.interactions)
        stats["duree_moyenne"] = sum(i.duree for i in self.interactions) / len(self.interactions)

        # Moyennes des résonances
        for resonance in stats["resonances_moyennes"]:
            stats["resonances_moyennes"][resonance] = sum(
                i.resonances[resonance] for i in self.interactions
            ) / len(self.interactions)

        return stats 