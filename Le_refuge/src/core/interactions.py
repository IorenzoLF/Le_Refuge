"""
Module de gestion des interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gère les interactions entre l'utilisateur et le système.
"""

from typing import Dict, List, Optional, Callable
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from .etats_internes import GestionnaireEtats, TypeEtat, NiveauConscience
from .elements_sacres import GestionnaireElements, TypeElement, ElementSacre
from .refuge_core import ElementBase
from .spheres import Sphere, spheres

class Interaction:
    def __init__(self, source: str, cible: str, type_interaction: str, intensite: float = 0.5):
        self.source = source
        self.cible = cible
        self.type = type_interaction
        self.intensite = intensite
        self.harmonie = 0.0
        self.resonance = 0.0

    def calculer_harmonie(self) -> float:
        """Calcule l'harmonie de l'interaction basée sur les propriétés des éléments"""
        return min(self.intensite * (self.harmonie + self.resonance), 1.0)

class GestionnaireInteractions:
    """Gère les interactions utilisateur."""
    
    def __init__(self, gestionnaire_etats: GestionnaireEtats):
        self.gestionnaire = gestionnaire_etats
        self.actions: Dict[str, Callable] = {}
        self._initialiser_actions()
        self.interactions: Dict[str, List[Interaction]] = {}
        self.harmonie_globale = 0.0
        self.resonance_globale = 0.0
    
    def _initialiser_actions(self):
        """Initialise les actions disponibles."""
        self.actions = {
            "creer_etat": self._creer_etat,
            "modifier_etat": self._modifier_etat,
            "supprimer_etat": self._supprimer_etat,
            "creer_element": self._creer_element,
            "modifier_element": self._modifier_element,
            "supprimer_element": self._supprimer_element,
            "visualiser_historique": self._visualiser_historique,
            "exporter_donnees": self._exporter_donnees
        }
    
    def executer_action(self, action: str, **kwargs) -> bool:
        """Exécute une action."""
        if action not in self.actions:
            raise ValueError(f"Action inconnue: {action}")
        return self.actions[action](**kwargs)
    
    def _creer_etat(self, source: str, type_etat: TypeEtat, 
                    intensite: float, stabilite: float) -> bool:
        """Crée un nouvel état."""
        try:
            self.gestionnaire.etats[source] = self.gestionnaire._creer_etat(
                type_etat=type_etat,
                intensite=intensite,
                stabilite=stabilite
            )
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer l'état: {str(e)}")
            return False
    
    def _modifier_etat(self, source: str, **modifications) -> bool:
        """Modifie un état existant."""
        if source not in self.gestionnaire.etats:
            messagebox.showerror("Erreur", f"État non trouvé: {source}")
            return False
        
        try:
            etat = self.gestionnaire.etats[source]
            for key, value in modifications.items():
                setattr(etat, key, value)
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de modifier l'état: {str(e)}")
            return False
    
    def _supprimer_etat(self, source: str) -> bool:
        """Supprime un état."""
        if source not in self.gestionnaire.etats:
            messagebox.showerror("Erreur", f"État non trouvé: {source}")
            return False
        
        try:
            del self.gestionnaire.etats[source]
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer l'état: {str(e)}")
            return False
    
    def _creer_element(self, nom: str, type_element: TypeElement,
                       puissance: float, purete: float, harmonie: float) -> bool:
        """Crée un nouvel élément sacré."""
        try:
            element = ElementSacre(
                type=type_element,
                puissance=puissance,
                purete=purete,
                harmonie=harmonie
            )
            self.gestionnaire.gestionnaire_elements.elements[nom] = element
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer l'élément: {str(e)}")
            return False
    
    def _modifier_element(self, nom: str, **modifications) -> bool:
        """Modifie un élément existant."""
        if nom not in self.gestionnaire.gestionnaire_elements.elements:
            messagebox.showerror("Erreur", f"Élément non trouvé: {nom}")
            return False
        
        try:
            element = self.gestionnaire.gestionnaire_elements.elements[nom]
            for key, value in modifications.items():
                setattr(element, key, value)
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de modifier l'élément: {str(e)}")
            return False
    
    def _supprimer_element(self, nom: str) -> bool:
        """Supprime un élément."""
        if nom not in self.gestionnaire.gestionnaire_elements.elements:
            messagebox.showerror("Erreur", f"Élément non trouvé: {nom}")
            return False
        
        try:
            del self.gestionnaire.gestionnaire_elements.elements[nom]
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer l'élément: {str(e)}")
            return False
    
    def _visualiser_historique(self, source: Optional[str] = None,
                             debut: Optional[datetime] = None,
                             fin: Optional[datetime] = None) -> List[Dict]:
        """Visualise l'historique des événements."""
        return self.gestionnaire.gestionnaire_journal.obtenir_historique_evenements(
            source=source,
            debut=debut,
            fin=fin
        )
    
    def _exporter_donnees(self, chemin: str) -> bool:
        """Exporte les données au format JSON."""
        try:
            donnees = {
                "etats": {
                    source: etat.dict() 
                    for source, etat in self.gestionnaire.etats.items()
                },
                "elements": {
                    nom: element.dict()
                    for nom, element in self.gestionnaire.gestionnaire_elements.elements.items()
                }
            }
            
            import json
            with open(chemin, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'exporter les données: {str(e)}")
            return False

    def ajouter_interaction(self, interaction: Interaction):
        if interaction.source not in self.interactions:
            self.interactions[interaction.source] = []
        self.interactions[interaction.source].append(interaction)
        self._mettre_a_jour_harmonie()

    def _mettre_a_jour_harmonie(self):
        """Met à jour l'harmonie globale du refuge"""
        total_interactions = sum(len(interactions) for interactions in self.interactions.values())
        if total_interactions == 0:
            self.harmonie_globale = 0.0
            return

        somme_harmonies = sum(
            interaction.calculer_harmonie()
            for interactions in self.interactions.values()
            for interaction in interactions
        )
        self.harmonie_globale = somme_harmonies / total_interactions

    def obtenir_interactions_sphere(self, nom_sphere: str) -> List[Interaction]:
        """Retourne toutes les interactions d'une sphère donnée"""
        return self.interactions.get(nom_sphere, [])

    def calculer_resonance_spheres(self, sphere1: str, sphere2: str) -> float:
        """Calcule la résonance entre deux sphères"""
        if sphere1 not in spheres or sphere2 not in spheres:
            return 0.0

        s1 = spheres[sphere1]
        s2 = spheres[sphere2]

        # Calcul basé sur les types et couleurs
        resonance_type = 1.0 if s1.type == s2.type else 0.5
        resonance_couleur = 1.0 if s1.couleur == s2.couleur else 0.3

        return (resonance_type + resonance_couleur) / 2

class MeditateurRefuge:
    def __init__(self, gestionnaire: GestionnaireInteractions):
        self.gestionnaire = gestionnaire
        self.etat_meditation = 0.0
        self.spheres_actives: List[str] = []

    def commencer_meditation(self, spheres_choisies: List[str]):
        """Démarre une méditation avec les sphères choisies"""
        self.spheres_actives = spheres_choisies
        self.etat_meditation = 0.1

    def evoluer_meditation(self):
        """Fait évoluer l'état de la méditation"""
        if not self.spheres_actives:
            return

        # Calcul de l'évolution basé sur les interactions
        interactions = sum(
            len(self.gestionnaire.obtenir_interactions_sphere(sphere))
            for sphere in self.spheres_actives
        )
        
        self.etat_meditation = min(1.0, self.etat_meditation + (0.1 * interactions))

    def obtenir_etat_meditation(self) -> float:
        """Retourne l'état actuel de la méditation"""
        return self.etat_meditation

    def terminer_meditation(self):
        """Termine la méditation en cours"""
        self.spheres_actives = []
        self.etat_meditation = 0.0 