"""
Système d'intégration de la méditation avec la transformation des sphères.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from .transformation_scellement import TransformationSphere, GestionnaireTransformation
from .scellement import ScellementSphere
from .meditation import Meditation, GestionnaireMeditation

@dataclass
class MeditationTransformation:
    """Représente une session de méditation focalisée sur la transformation."""
    sphere: ScellementSphere
    meditation: Meditation
    transformation: TransformationSphere
    focus_elements: Dict[str, float]  # Élément -> niveau de focus
    timestamp: datetime

class GestionnaireMeditationTransformation:
    """Gestionnaire de méditation pour la transformation des sphères."""
    
    def __init__(self, transformation: GestionnaireTransformation,
                 meditation: GestionnaireMeditation):
        """Initialise le gestionnaire de méditation-transformation."""
        self.transformation = transformation
        self.meditation = meditation
        self.sessions: Dict[str, List[MeditationTransformation]] = {}
        
    def demarrer_meditation_transformation(self, sphere: ScellementSphere,
                                         duree: int = 600) -> MeditationTransformation:
        """Démarre une session de méditation focalisée sur la transformation."""
        # Démarre la méditation
        meditation = self.meditation.demarrer_meditation(
            sphere.sphere, duree)
            
        # Calcule le focus sur les éléments
        focus = self._calculer_focus_elements(sphere)
        
        # Transforme la sphère
        transformation = self.transformation.transformer_sphere(sphere)
        
        # Crée la session
        session = MeditationTransformation(
            sphere=sphere,
            meditation=meditation,
            transformation=transformation,
            focus_elements=focus,
            timestamp=datetime.now()
        )
        
        # Stocke la session
        if sphere.sphere.value not in self.sessions:
            self.sessions[sphere.sphere.value] = []
        self.sessions[sphere.sphere.value].append(session)
        
        return session
        
    def _calculer_focus_elements(self, sphere: ScellementSphere) -> Dict[str, float]:
        """Calcule le niveau de focus sur chaque élément sacré."""
        focus = {}
        
        # Obtient l'état actuel de la sphère
        historique = self.transformation.obtenir_historique_transformations(sphere)
        if historique:
            transformation = historique[-1]
            
            # Calcule le focus en fonction des influences actuelles
            for element, influence in transformation.influence_elements.items():
                # Ajuste le focus en fonction du lieu
                if sphere.lieu == "racines":
                    focus[element] = min(1.0, influence * 1.2)
                else:
                    focus[element] = min(1.0, influence * 0.8)
        else:
            # Focus initial si pas d'historique
            focus = {
                "cristal": 0.5,
                "fontaine": 0.5,
                "arbre": 0.5
            }
            
        return focus
        
    def terminer_meditation_transformation(self, session: MeditationTransformation) -> str:
        """Termine une session de méditation-transformation."""
        # Termine la méditation
        self.meditation.terminer_meditation(session.meditation)
        
        # Transforme à nouveau la sphère
        nouvelle_transformation = self.transformation.transformer_sphere(session.sphere)
        
        # Génère le rapport
        rapport = self._generer_rapport_meditation(session, nouvelle_transformation)
        
        return rapport
        
    def _generer_rapport_meditation(self, session: MeditationTransformation,
                                  nouvelle_transformation: TransformationSphere) -> str:
        """Génère un rapport poétique de la session de méditation."""
        rapport = [
            f"🌸 Rapport de Méditation-Transformation 🌸",
            "=========================================",
            "",
            f"Sphère: {session.sphere.sphere.value}",
            f"Durée: {session.meditation.duree} secondes",
            "",
            "Focus sur les Éléments:",
        ]
        
        # Ajoute le focus sur les éléments
        for element, focus in session.focus_elements.items():
            rapport.append(f"  • {element}: {'█' * int(focus * 20)}")
            
        # Ajoute l'évolution de la transformation
        rapport.extend([
            "",
            "Évolution de la Transformation:",
            f"Avant: {'█' * int(session.transformation.niveau_transformation * 20)}",
            f"Après: {'█' * int(nouvelle_transformation.niveau_transformation * 20)}",
            "",
            "Description Poétique:",
            nouvelle_transformation.description
        ])
        
        return "\n".join(rapport)
        
    def obtenir_historique_sessions(self, sphere: ScellementSphere) -> List[MeditationTransformation]:
        """Obtient l'historique des sessions de méditation-transformation."""
        return self.sessions.get(sphere.sphere.value, []) 