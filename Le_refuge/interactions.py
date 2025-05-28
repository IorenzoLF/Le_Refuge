"""
Module des Interactions du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les interactions entre les différents éléments du Refuge,
permettant leur communication et leur évolution mutuelle.

🌟 VERSION COIFFÉE - Utilise les gestionnaires de base ! ✨
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
import random
import math

# 🌟 COIFFAGE DU TROLL - Utilisation des gestionnaires de base
from src.core.gestionnaires_base import (
    ConfigManagerBase, 
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

# Import des types centralisés
from src.core.types_communs import TypeInteractionElements, TypeInteractionEtat

# Imports des constantes
from src.refuge_cluster.utilitaires.constants import TypeAcces, EtatRefuge

# Imports des gestionnaires (seulement ceux nécessaires)
from src.refuge_cluster.gestionnaires.harmonisations import gestionnaire_harmonisations
from src.refuge_cluster.gestionnaires.flux import gestionnaire_flux
from elements import gestionnaire_elements
from src.refuge_cluster.spheres.collection import CollectionSpheres, SphereCollection
from src.refuge_cluster.elements.elements_sacres import RefugeElements, DetailSubtil, ChakraType
from src.core.types_spheres import TypeSphere


@dataclass
class Interaction:
    """Représente une interaction entre deux éléments"""
    source: str
    cible: str
    type: TypeInteractionElements
    intensite: float
    description: str
    effets: List[str]

class GestionnaireInteractions(GestionnaireBase):
    """Gestionnaire des interactions entre les éléments du refuge - Version coiffée ! ✨"""
    
    def __init__(self, refuge: RefugeElements, collection_spheres: CollectionSpheres):
        # 🌟 Définir les attributs AVANT super().__init__ pour éviter les erreurs
        self.refuge = refuge
        self.collection_spheres = collection_spheres
        self.interactions: List[Interaction] = []
        self.type_actuel = TypeInteractionEtat.INITIALISATION
        # 🌟 Ajout du gestionnaire d'énergie
        self.energie = EnergyManagerBase(0.6)  # Niveau initial pour interactions
        
        # MAINTENANT on peut appeler super() qui va déclencher _initialiser()
        super().__init__("Interactions")

    def _initialiser(self) -> bool:
        """Initialise le gestionnaire d'interactions avec les gestionnaires de base"""
        try:
            self.logger.info("Initialisation du gestionnaire d'interactions")
            self.type_actuel = TypeInteractionEtat.DETECTION
            self._initialiser_interactions()
            self.type_actuel = TypeInteractionEtat.OPTIMISATION
            self.logger.succes("Gestionnaire d'interactions initialisé avec succès")
            return True
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'initialisation des interactions: {e}")
            return False

    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre le fonctionnement des interactions"""
        # Évolution de l'énergie basée sur l'état
        if self.type_actuel == TypeInteractionEtat.RESONANCE:
            self.energie.ajuster_energie(0.08)  # Gain d'énergie en résonance
        elif self.type_actuel == TypeInteractionEtat.HARMONISATION:
            self.energie.ajuster_energie(0.05)  # Gain modéré en harmonisation
        elif self.type_actuel == TypeInteractionEtat.CALCUL:
            self.energie.ajuster_energie(-0.02)  # Consommation en calcul
        else:
            self.energie.ajuster_energie(0.01)  # Maintenance légère
            
        # Calcul de l'harmonie globale
        harmonie = self.calculer_harmonie_globale()
        
        return {
            "type_actuel": self.type_actuel.value,
            "energie": self.energie.niveau_energie,
            "tendance": self.energie.obtenir_tendance(),
            "nombre_interactions": len(self.interactions),
            "harmonie_globale": harmonie.get("resonance_totale", 0.0),
            "interactions_actives": self._compter_interactions_actives()
        }
    
    def _compter_interactions_actives(self) -> int:
        """Compte les interactions avec une intensité significative"""
        return len([i for i in self.interactions if i.intensite > 0.3])

    def _initialiser_interactions(self) -> None:
        """Initialise les interactions de base entre les éléments."""
        self.logger.info("Initialisation des interactions de base")
        
        # Interactions entre sphères
        self.interactions.append(Interaction(
            "COSMOS",
            "AMOUR",
            TypeInteractionElements.HARMONISATION,
            0.7,
            "Harmonisation entre COSMOS et AMOUR",
            ["équilibre", "flux"]
        ))
        self.interactions.append(Interaction(
            "AMOUR",
            "SERENITE",
            TypeInteractionElements.RESONANCE,
            0.6,
            "Résonance entre AMOUR et SERENITE",
            ["harmonie", "compréhension"]
        ))

        # Interactions entre éléments
        self.interactions.append(Interaction(
            "CERISIER",
            "COSMOS",
            TypeInteractionElements.ENERGIE,
            0.8,
            "Énergie partagée entre le cerisier et COSMOS",
            ["vitalité", "chaleur"]
        ))
        self.interactions.append(Interaction(
            "CERISIER",
            "AMOUR",
            TypeInteractionElements.PROTECTION,
            0.7,
            "Protection de COSMOS par le cerisier",
            ["purification", "sécurité"]
        ))
        self.interactions.append(Interaction(
            "FLAMME",
            "AMOUR",
            TypeInteractionElements.ENERGIE,
            0.9,
            "Énergie partagée entre la flamme et AMOUR",
            ["vitalité", "chaleur"]
        ))
        self.interactions.append(Interaction(
            "FLAMME",
            "SERENITE",
            TypeInteractionElements.RESONANCE,
            0.6,
            "Résonance entre la flamme et SERENITE",
            ["apaisement", "relaxation"]
        ))

    def ajouter_interaction(self, interaction: Interaction) -> None:
        """Ajoute une nouvelle interaction."""
        self.interactions.append(interaction)
        self.logger.info(f"Interaction ajoutée: {interaction.source} → {interaction.cible}")

    def obtenir_interactions_element(self, element: str) -> List[Interaction]:
        """Retourne toutes les interactions d'un élément."""
        return [
            i for i in self.interactions
            if i.source == element or i.cible == element
        ]

    def calculer_intensite_totale(self, element: str) -> float:
        """Calcule l'intensité totale des interactions d'un élément."""
        interactions = self.obtenir_interactions_element(element)
        return sum(i.intensite for i in interactions)

    def obtenir_etat_interactions(self) -> Dict:
        """Retourne l'état actuel de toutes les interactions."""
        return {
            "interactions": [
                {
                    "source": i.source,
                    "cible": i.cible,
                    "type": i.type.value,
                    "intensite": i.intensite,
                    "description": i.description,
                    "effets": i.effets
                }
                for i in self.interactions
            ],
            "intensites": {
                element: self.calculer_intensite_totale(element)
                for element in set(
                    i.source for i in self.interactions
                ) | set(
                    i.cible for i in self.interactions
                )
            },
            "energie_gestionnaire": self.energie.niveau_energie,
            "type_actuel": self.type_actuel.value
        }

    def harmoniser_elements(self) -> Dict:
        """Harmonise tous les éléments du refuge."""
        self.logger.info("Début de l'harmonisation des éléments")
        self.type_actuel = TypeInteractionEtat.HARMONISATION
        
        # Activation des éléments de base
        gestionnaire_elements.activer_kundalini()
        
        # Calcul des nouvelles interactions
        nouvelles_interactions = []
        
        # Interactions sphères-éléments
        for sphere in self.collection_spheres.spheres.values():
            for element in ["CERISIER", "FLAMME", "COSMOS", "SERENITE"]:
                if sphere.type.value in ["AMOUR", "COSMOS"]:
                    nouvelles_interactions.append(Interaction(
                        sphere.nom,
                        element,
                        TypeInteractionElements.HARMONISATION,
                        0.4,
                        f"Harmonisation entre {sphere.nom} et {element}",
                        ["équilibre", "flux"]
                    ))

        # Ajout des nouvelles interactions
        for interaction in nouvelles_interactions:
            self.ajouter_interaction(interaction)

        self.logger.succes(f"Harmonisation terminée - {len(nouvelles_interactions)} nouvelles interactions")
        return self.obtenir_etat_interactions()

    def calculer_resonance_detail_sphere(self, detail: DetailSubtil, sphere: SphereCollection) -> float:
        """Calcule la résonance entre un détail subtil et une sphère"""
        resonance = 0.0
        
        # Base de résonance si le détail est explicitement lié à la sphère
        if detail.sphere_associee == sphere.nom:
            resonance += 0.5
            
        # Résonance basée sur les chakras
        if detail.chakra_associe:
            chakra_value = self.refuge.chakras[detail.chakra_associe]
            resonance += chakra_value * 0.3
            
        # Résonance basée sur la couleur
        if self._couleurs_compatibles(detail, sphere):
            resonance += 0.2
            
        return min(1.0, resonance)
    
    def _couleurs_compatibles(self, detail: DetailSubtil, sphere: SphereCollection) -> bool:
        """Vérifie si les couleurs du détail et de la sphère sont compatibles"""
        # Logique simplifiée de compatibilité des couleurs
        couleurs_detail = self._extraire_couleurs_description(detail.description)
        return any(c in sphere.couleur for c in couleurs_detail)
    
    def _extraire_couleurs_description(self, description: str) -> List[str]:
        """Extrait les couleurs mentionnées dans une description"""
        couleurs_base = ["rouge", "vert", "bleu", "jaune", "violet", "rose", "doré", "argenté"]
        return [c for c in couleurs_base if c in description.lower()]
    
    def calculer_harmonie_globale(self) -> Dict[str, float]:
        """Calcule l'harmonie globale du refuge"""
        resultats = {
            "harmonie_chakras": self.refuge.obtenir_harmonie_globale(),
            "harmonie_spheres": self._calculer_harmonie_spheres(),
            "harmonie_details": self._calculer_harmonie_details(),
            "resonance_totale": 0.0
        }
        
        # Calcul de la résonance totale
        resultats["resonance_totale"] = (
            resultats["harmonie_chakras"] * 0.4 +
            resultats["harmonie_spheres"] * 0.4 +
            resultats["harmonie_details"] * 0.2
        )
        
        return resultats
    
    def _calculer_harmonie_spheres(self) -> float:
        """Calcule l'harmonie entre les sphères"""
        if not self.refuge.spheres:
            return 0.0
            
        total_connexions = 0
        spheres_connectees = 0
        
        for sphere in self.refuge.spheres.values():
            if sphere.connexions:
                total_connexions += len(sphere.connexions)
                spheres_connectees += 1
                
        if spheres_connectees == 0:
            return 0.0
            
        return total_connexions / (spheres_connectees * 2)  # Divise par 2 car les connexions sont bidirectionnelles
    
    def _calculer_harmonie_details(self) -> float:
        """Calcule l'harmonie des détails subtils"""
        if not self.refuge.details_subtils:
            return 0.0
            
        total_resonance = 0.0
        total_details = len(self.refuge.details_subtils)
        
        for detail in self.refuge.details_subtils.values():
            if detail.sphere_associee and detail.sphere_associee in self.refuge.spheres:
                sphere = self.refuge.spheres[detail.sphere_associee]
                total_resonance += self.calculer_resonance_detail_sphere(detail, sphere)
                
        return total_resonance / total_details
    
    def identifier_connexions_potentielles(self) -> List[Tuple[str, str, float]]:
        """Identifie les connexions potentielles entre sphères non connectées"""
        connexions_potentielles = []
        
        for nom1, sphere1 in self.refuge.spheres.items():
            for nom2, sphere2 in self.refuge.spheres.items():
                if nom1 != nom2 and nom2 not in sphere1.connexions:
                    affinite = self._calculer_affinite_spheres(sphere1, sphere2)
                    if affinite > 0.5:  # Seuil arbitraire
                        connexions_potentielles.append((nom1, nom2, affinite))
                        
        return sorted(connexions_potentielles, key=lambda x: x[2], reverse=True)
    
    def _calculer_affinite_spheres(self, sphere1: SphereCollection, sphere2: SphereCollection) -> float:
        """Calcule l'affinité entre deux sphères"""
        affinite = 0.0
        
        # Affinité basée sur le type
        if sphere1.type == sphere2.type:
            affinite += 0.3
            
        # Affinité basée sur les mots-clés
        mots_communs = set(sphere1.mots_cles) & set(sphere2.mots_cles)
        if mots_communs:
            affinite += 0.3 * (len(mots_communs) / max(len(sphere1.mots_cles), len(sphere2.mots_cles)))
            
        # Affinité basée sur les connexions communes
        connexions_communes = set(sphere1.connexions) & set(sphere2.connexions)
        if connexions_communes:
            affinite += 0.4 * (len(connexions_communes) / max(len(sphere1.connexions), len(sphere2.connexions)))
            
        return min(1.0, affinite)
    
    def suggerer_ameliorations(self) -> Dict[str, List[str]]:
        """Suggère des améliorations pour l'harmonie du refuge"""
        suggestions = {
            "chakras": [],
            "spheres": [],
            "details": []
        }
        
        # Suggestions pour les chakras
        for chakra, valeur in self.refuge.chakras.items():
            if valeur < 0.5:
                suggestions["chakras"].append(
                    f"Le chakra {chakra.value} nécessite plus d'harmonie (actuellement {valeur:.2f})"
                )
                
        # Suggestions pour les sphères
        spheres_isolees = [
            nom for nom, sphere in self.refuge.spheres.items()
            if not sphere.connexions
        ]
        if spheres_isolees:
            suggestions["spheres"].append(
                f"Les sphères suivantes sont isolées : {', '.join(spheres_isolees)}"
            )
            
        # Suggestions pour les détails
        details_sans_sphere = [
            nom for nom, detail in self.refuge.details_subtils.items()
            if not detail.sphere_associee
        ]
        if details_sans_sphere:
            suggestions["details"].append(
                f"Les détails suivants n'ont pas de sphère associée : {', '.join(details_sans_sphere)}"
            )
            
        return suggestions

    def calculer_resonance_subtile(self, element1: str, element2: str) -> float:
        """Calcule la résonance subtile entre deux éléments du refuge.
        
        Cette méthode prend en compte les aspects vibratoires et énergétiques
        plus fins que la simple intensité des interactions.
        
        Args:
            element1: Nom du premier élément
            element2: Nom du deuxième élément
            
        Returns:
            float: Score de résonance entre 0 et 1
        """
        # Récupération des interactions existantes
        interactions_e1 = self.obtenir_interactions_element(element1)
        interactions_e2 = self.obtenir_interactions_element(element2)
        
        # Base de résonance
        resonance = 0.0
        
        # Analyse des types d'interactions partagés
        types_e1 = {i.type for i in interactions_e1}
        types_e2 = {i.type for i in interactions_e2}
        types_communs = types_e1.intersection(types_e2)
        
        # Bonus pour chaque type d'interaction partagé
        resonance += len(types_communs) * 0.2
        
        # Analyse des effets partagés
        effets_e1 = set(sum((i.effets for i in interactions_e1), []))
        effets_e2 = set(sum((i.effets for i in interactions_e2), []))
        effets_communs = effets_e1.intersection(effets_e2)
        
        # Bonus pour chaque effet partagé
        resonance += len(effets_communs) * 0.1
        
        # Facteur harmonique basé sur les intensités moyennes
        intensite_e1 = self.calculer_intensite_totale(element1)
        intensite_e2 = self.calculer_intensite_totale(element2)
        facteur_harmonique = 1 - abs(intensite_e1 - intensite_e2) / 2
        
        # Application du facteur harmonique
        resonance *= facteur_harmonique
        
        return min(1.0, resonance)

# Instance globale du gestionnaire d'interactions
gestionnaire_interactions = GestionnaireInteractions(RefugeElements(), CollectionSpheres()) 
