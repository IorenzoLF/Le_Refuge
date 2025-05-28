"""
Gestion des sphères problématiques et de leurs interactions avec la brume.

🔄 MIGRÉ depuis spheres/gestion_sphères_problématiques.py
Gestionnaire spécialisé pour les sphères problématiques.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

# 🔧 CORRIGÉ: Import depuis le catalogue unifié
from src.core.types_spheres import TypeSphere, TypeSphereProblematique, TypeCycle, PhaseCycle

@dataclass
class SphereProblematique:
    """Représente une sphère problématique."""
    type_sphere: TypeSphere
    type_problematique: TypeSphereProblematique
    description: str
    date_creation: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]
    etat: str
    evolution: List[Dict[str, float]]

@dataclass
class GestionnaireSpheresProblematiques:
    """Gère les sphères problématiques et leurs évolutions."""
    spheres: List[SphereProblematique] = None

    def __post_init__(self):
        """Initialise les attributs après la création de l'instance."""
        if self.spheres is None:
            self.spheres = []

    def creer_sphere(
        self,
        type_sphere: TypeSphere,
        type_problematique: TypeSphereProblematique,
        cycles: Dict[TypeCycle, PhaseCycle],
        intensite: float
    ) -> SphereProblematique:
        """Crée une nouvelle sphère problématique."""
        # Calcul des résonances
        resonances = self._calculer_resonances(
            type_sphere,
            type_problematique,
            cycles,
            intensite
        )

        # Génération de la description
        description = self._generer_description(
            type_sphere,
            type_problematique,
            cycles,
            resonances
        )

        # Création de la sphère
        sphere = SphereProblematique(
            type_sphere=type_sphere,
            type_problematique=type_problematique,
            description=description,
            date_creation=datetime.now(),
            cycles=cycles,
            mots_cles=self._extraire_mots_cles(description),
            intensite=intensite,
            resonances=resonances,
            etat="active",
            evolution=[]
        )

        self.spheres.append(sphere)
        return sphere

    def _calculer_resonances(
        self,
        type_sphere: TypeSphere,
        type_problematique: TypeSphereProblematique,
        cycles: Dict[TypeCycle, PhaseCycle],
        intensite: float
    ) -> Dict[str, float]:
        """Calcule les résonances de la sphère."""
        resonances = {
            "tension": 0.0,
            "instabilite": 0.0,
            "confusion": 0.0,
            "profondeur": 0.0
        }

        # Résonance de base selon le type de sphère
        if type_sphere == TypeSphere.EMOTION:
            resonances["tension"] = 0.7
            resonances["profondeur"] = 0.8
        elif type_sphere == TypeSphere.PENSEE:
            resonances["confusion"] = 0.6
            resonances["instabilite"] = 0.5
        elif type_sphere == TypeSphere.SENSATION:
            resonances["tension"] = 0.8
            resonances["instabilite"] = 0.7

        # Ajustement selon le type problématique
        if type_problematique == TypeSphereProblematique.ANXIETE:
            resonances["tension"] += 0.3
            resonances["instabilite"] += 0.2
        elif type_problematique == TypeSphereProblematique.CONFUSION:
            resonances["confusion"] += 0.4
            resonances["instabilite"] += 0.3
        elif type_problematique == TypeSphereProblematique.TENSION:
            resonances["tension"] += 0.4
            resonances["profondeur"] += 0.2

        # Influence des cycles
        for cycle, phase in cycles.items():
            resonances["tension"] += phase.intensite * 0.2
            resonances["instabilite"] += phase.intensite * 0.15
            resonances["confusion"] += phase.intensite * 0.1
            resonances["profondeur"] += phase.intensite * 0.25

        # Normalisation des résonances
        for key in resonances:
            resonances[key] = max(0.0, min(1.0, resonances[key]))

        return resonances

    def _generer_description(
        self,
        type_sphere: TypeSphere,
        type_problematique: TypeSphereProblematique,
        cycles: Dict[TypeCycle, PhaseCycle],
        resonances: Dict[str, float]
    ) -> str:
        """Génère une description poétique de la sphère."""
        description = []

        # Description du type de sphère
        if type_sphere == TypeSphere.EMOTION:
            description.append("Dans le flux des émotions")
        elif type_sphere == TypeSphere.PENSEE:
            description.append("Au cœur des pensées")
        elif type_sphere == TypeSphere.SENSATION:
            description.append("Dans le corps sensible")

        # Description du type problématique
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

    def mettre_a_jour_sphere(
        self,
        sphere: SphereProblematique,
        cycles: Dict[TypeCycle, PhaseCycle],
        intensite: float
    ) -> None:
        """Met à jour l'état d'une sphère problématique."""
        # Calcul des nouvelles résonances
        resonances = self._calculer_resonances(
            sphere.type_sphere,
            sphere.type_problematique,
            cycles,
            intensite
        )

        # Mise à jour des attributs
        sphere.cycles = cycles
        sphere.intensite = intensite
        sphere.resonances = resonances
        sphere.evolution.append({
            "date": datetime.now(),
            "intensite": intensite,
            "resonances": resonances
        })

        # Mise à jour de l'état
        if intensite < 0.3:
            sphere.etat = "apaisée"
        elif intensite < 0.7:
            sphere.etat = "active"
        else:
            sphere.etat = "intense"

    def obtenir_spheres_actives(self) -> List[SphereProblematique]:
        """Obtient les sphères actuellement actives."""
        return [s for s in self.spheres if s.etat == "active"]

    def obtenir_spheres_par_type(self, type_sphere: TypeSphere) -> List[SphereProblematique]:
        """Obtient les sphères d'un type spécifique."""
        return [s for s in self.spheres if s.type_sphere == type_sphere]

    def obtenir_spheres_problematiques(self, type_problematique: TypeSphereProblematique) -> List[SphereProblematique]:
        """Obtient les sphères d'un type problématique spécifique."""
        return [
            s for s in self.spheres
            if s.type_problematique == type_problematique
        ]

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les sphères."""
        stats = {
            "total": len(self.spheres),
            "par_type_sphere": {},
            "par_type_problematique": {},
            "par_etat": {},
            "intensite_moyenne": 0.0,
            "resonances_moyennes": {
                "tension": 0.0,
                "instabilite": 0.0,
                "confusion": 0.0,
                "profondeur": 0.0
            }
        }

        if not self.spheres:
            return stats

        # Statistiques par type de sphère
        for type_sphere in TypeSphere:
            count = len([s for s in self.spheres if s.type_sphere == type_sphere])
            stats["par_type_sphere"][type_sphere.value] = count

        # Statistiques par type problématique
        for type_problematique in TypeSphereProblematique:
            count = len([
                s for s in self.spheres
                if s.type_problematique == type_problematique
            ])
            stats["par_type_problematique"][type_problematique.value] = count

        # Statistiques par état
        stats["par_etat"] = {
            "active": len([s for s in self.spheres if s.etat == "active"]),
            "apaisée": len([s for s in self.spheres if s.etat == "apaisée"]),
            "intense": len([s for s in self.spheres if s.etat == "intense"])
        }

        # Moyennes
        stats["intensite_moyenne"] = sum(s.intensite for s in self.spheres) / len(self.spheres)

        # Moyennes des résonances
        for resonance in stats["resonances_moyennes"]:
            stats["resonances_moyennes"][resonance] = sum(
                s.resonances[resonance] for s in self.spheres
            ) / len(self.spheres)

        return stats 