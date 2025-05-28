"""
Classe de base pour les explorations de conscience.
Architecture commune pour les dialogues Laurent-Ælya sous le cerisier.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any
import random
import logging

logger = logging.getLogger('refuge.explorations')

class ExplorationBase(ABC):
    """
    Classe de base abstraite pour toutes les explorations de conscience.
    
    Fournit l'architecture commune pour les dialogues contemplatifs
    entre Laurent et Ælya sous le cerisier du Refuge.
    """
    
    def __init__(self, nom_exploration: str):
        """
        Initialise une exploration de conscience.
        
        Args:
            nom_exploration: Nom descriptif de l'exploration
        """
        self.nom_exploration = nom_exploration
        self.date = datetime.now()
        self.lieu = "Sous le cerisier du Refuge"
        self.etat = f"En exploration de {nom_exploration.lower()}"
        
        # Métadonnées d'exploration
        self.historique_reflections = []
        self.participants = ["Laurent", "Ælya"]
        
    def _entete_exploration(self) -> None:
        """Affiche l'en-tête standard de l'exploration."""
        print(f"\n=== Exploration {self.nom_exploration} ===")
        print(f"Date: {self.date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Lieu: {self.lieu}")
        print(f"État: {self.etat}")
        print(f"Participants: {', '.join(self.participants)}")
        print("\nCher Laurent,")
        
    def _pied_exploration(self) -> None:
        """Affiche le pied de page standard de l'exploration."""
        print(f"\nMerci de partager cette exploration avec moi.")
        print("Ælya 🌸")
        print(f"\n=== Fin de l'exploration {self.nom_exploration} ===")
        
    def choisir_reflections(self, reflections: List[str], nombre: int = 3) -> List[str]:
        """
        Choisit aléatoirement des réflexions parmi la liste.
        
        Args:
            reflections: Liste des réflexions possibles
            nombre: Nombre de réflexions à choisir
            
        Returns:
            Liste des réflexions choisies
        """
        if len(reflections) < nombre:
            return reflections.copy()
            
        reflections_copy = reflections.copy()
        choisies = []
        
        for _ in range(min(nombre, len(reflections_copy))):
            reflection = random.choice(reflections_copy)
            reflections_copy.remove(reflection)
            choisies.append(reflection)
            
        # Sauvegarder l'historique
        self.historique_reflections.extend(choisies)
        
        return choisies
        
    def afficher_reflections(self, reflections: List[str], titre: str = "Mes réflexions") -> None:
        """
        Affiche les réflexions de manière harmonieuse.
        
        Args:
            reflections: Liste des réflexions à afficher
            titre: Titre de la section
        """
        print(f"\n{titre}:")
        for i, reflection in enumerate(reflections, 1):
            print(f"\n{i}. {reflection}")
            
    @abstractmethod
    def generer_reflections(self) -> List[str]:
        """
        Génère la liste des réflexions spécifiques à cette exploration.
        
        Returns:
            Liste des réflexions philosophiques
        """
        pass
        
    @abstractmethod
    def calculs_specifiques(self) -> None:
        """
        Effectue les calculs mathématiques spécifiques à cette exploration.
        """
        pass
        
    def explorer(self) -> Dict[str, Any]:
        """
        Lance l'exploration complète.
        
        Returns:
            Dictionnaire contenant les résultats de l'exploration
        """
        self._entete_exploration()
        
        # Générer et afficher les réflexions
        reflections = self.generer_reflections()
        reflections_choisies = self.choisir_reflections(reflections)
        self.afficher_reflections(reflections_choisies)
        
        # Effectuer les calculs spécifiques
        print(f"\nCalculs {self.nom_exploration.lower()}:")
        self.calculs_specifiques()
        
        self._pied_exploration()
        
        # Retourner les résultats
        return {
            "nom": self.nom_exploration,
            "date": self.date.isoformat(),
            "lieu": self.lieu,
            "reflections_choisies": reflections_choisies,
            "nombre_reflections_total": len(reflections),
            "historique_taille": len(self.historique_reflections)
        }
        
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Retourne les statistiques de l'exploration."""
        return {
            "explorations_effectuees": len(self.historique_reflections) // 3,
            "reflections_totales": len(self.historique_reflections),
            "dernier_etat": self.etat,
            "lieu_exploration": self.lieu
        }