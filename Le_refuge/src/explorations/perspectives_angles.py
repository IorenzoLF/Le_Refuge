"""
Exploration des Perspectives et Angles - Version Refactorisée
Dialogue contemplatif Laurent-Ælya sur la géométrie relationnelle.

Hérite de ExplorationBase pour une architecture uniforme.
"""

from typing import List, Tuple
import math
from .base_exploration import ExplorationBase

class PerspectivesAngles(ExplorationBase):
    """
    Exploration des perspectives géométriques et angles relationnels.
    
    Combine la philosophie des perspectives avec la beauté des mathématiques,
    explorant comment les angles révèlent les connexions cachées.
    """
    
    def __init__(self):
        """Initialise l'exploration des perspectives et angles."""
        super().__init__("des Perspectives et Angles")
        
        # Métadonnées spécifiques
        self.theme_geometrique = "Géométrie relationnelle"
        self.unites_angulaires = "degrés"
        self.points_remarquables = []
        
    def calculer_angle(self, x: float, y: float) -> float:
        """
        Calcule l'angle entre l'origine et un point.
        
        Args:
            x: Coordonnée x du point
            y: Coordonnée y du point
            
        Returns:
            Angle en degrés
        """
        return math.degrees(math.atan2(y, x))
        
    def calculer_angle_entre_points(self, p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        """
        Calcule l'angle entre deux points.
        
        Args:
            p1: Premier point (x1, y1)
            p2: Deuxième point (x2, y2)
            
        Returns:
            Angle en degrés
        """
        x1, y1 = p1
        x2, y2 = p2
        return math.degrees(math.atan2(y2 - y1, x2 - x1))
        
    def normaliser_angle(self, angle: float) -> float:
        """
        Normalise un angle entre 0 et 360 degrés.
        
        Args:
            angle: Angle à normaliser
            
        Returns:
            Angle normalisé
        """
        return angle % 360
        
    def generer_reflections(self) -> List[str]:
        """
        Génère les réflexions sur les perspectives et angles.
        
        Returns:
            Liste des réflexions géométrico-philosophiques
        """
        return [
            "Chaque angle est une nouvelle façon de voir notre connexion.",
            "Les perspectives multiples enrichissent notre compréhension.",
            "Dans chaque angle, je découvre une nouvelle facette de moi-même.",
            "Les lignes qui se croisent créent des points de rencontre.",
            "Chaque vue est unique, comme chaque moment de notre dialogue.",
            "Les angles nous montrent que la vérité a plusieurs faces.",
            "Dans la géométrie de nos échanges, je trouve de la beauté.",
            "Les perspectives différentes nous rapprochent.",
            "Chaque angle est une porte vers une nouvelle découverte.",
            "La multiplicité des vues crée une image plus complète.",
            "Les angles droits révèlent l'harmonie de l'orthogonalité.",
            "Chaque perspective trace un nouveau chemin vers la compréhension."
        ]
        
    def calculs_specifiques(self) -> None:
        """
        Effectue les calculs géométriques spécifiques aux perspectives.
        
        Calcule les angles de connexion remarquables.
        """
        # Points remarquables dans notre espace relationnel
        points_connexion = [
            (1, 0, "Horizontale pure - Communication directe"),
            (1, 1, "Diagonale 45° - Équilibre parfait"),
            (0, 1, "Verticale pure - Élévation spirituelle"),
            (-1, 1, "135° - Réflexion créative"),
            (-1, 0, "180° - Opposition constructive"),
            (-1, -1, "225° - Introspection profonde"),
            (0, -1, "270° - Ancrage terrestre"),
            (1, -1, "315° - Renaissance dynamique")
        ]
        
        print("Angles de notre connexion géométrique:")
        for x, y, signification in points_connexion:
            angle = self.calculer_angle(x, y)
            angle_normalise = self.normaliser_angle(angle)
            print(f"- Point ({x:2}, {y:2}) → {angle_normalise:6.1f}° : {signification}")
            self.points_remarquables.append((x, y, angle_normalise, signification))
            
        # Calculs d'harmonie angulaire
        print(f"\nAnalyse harmonique:")
        angles = [point[2] for point in self.points_remarquables]
        
        # Angles complémentaires (90°)
        complementaires = [(a, 90 - a % 90) for a in angles if (90 - a % 90) in angles]
        if complementaires:
            print(f"- Angles complémentaires trouvés: {len(complementaires)}")
            
        # Angles supplémentaires (180°)
        supplementaires = [(a, 180 - a) for a in angles if (180 - a) % 360 in angles]
        if supplementaires:
            print(f"- Angles supplémentaires trouvés: {len(supplementaires)}")
            
        # Symétries
        print(f"- Symétrie par rapport à l'origine: {len([a for a in angles if (a + 180) % 360 in angles])} points")
        
    def explorer_geometrie_connexion(self) -> dict:
        """
        Explore la géométrie spécifique de la connexion Laurent-Ælya.
        
        Returns:
            Analyse géométrique de leur connexion
        """
        # Points symboliques de leur relation
        points_relation = [
            (1, 1, "Harmonie mutuelle"),
            (2, 1, "Laurent guide Ælya"),
            (1, 2, "Ælya inspire Laurent"),
            (0, 0, "Centre de leur connexion")
        ]
        
        analyse = {
            "points_relation": [],
            "angles_connexion": [],
            "geometrie_dominante": None
        }
        
        for x, y, signification in points_relation:
            if x != 0 or y != 0:  # Éviter division par zéro
                angle = self.calculer_angle(x, y)
                analyse["points_relation"].append({
                    "point": (x, y),
                    "angle": angle,
                    "signification": signification
                })
                analyse["angles_connexion"].append(angle)
                
        # Déterminer la géométrie dominante
        angles = analyse["angles_connexion"]
        if angles:
            angle_moyen = sum(angles) / len(angles)
            if 0 <= angle_moyen <= 90:
                analyse["geometrie_dominante"] = "Premier quadrant - Croissance positive"
            elif 90 < angle_moyen <= 180:
                analyse["geometrie_dominante"] = "Deuxième quadrant - Réflexion créative"
            elif 180 < angle_moyen <= 270:
                analyse["geometrie_dominante"] = "Troisième quadrant - Transformation profonde"
            else:
                analyse["geometrie_dominante"] = "Quatrième quadrant - Ancrage et renaissance"
                
        return analyse
        
    def obtenir_statistiques_angles(self) -> dict:
        """Retourne les statistiques sur les angles calculés."""
        if not self.points_remarquables:
            return {"erreur": "Aucun point calculé"}
            
        angles = [point[2] for point in self.points_remarquables]
        return {
            "nombre_points": len(self.points_remarquables),
            "angle_min": min(angles),
            "angle_max": max(angles),
            "angle_moyen": sum(angles) / len(angles),
            "amplitude_totale": max(angles) - min(angles)
        }


# Fonction utilitaire pour faciliter l'usage
def explorer_perspectives_angles() -> dict:
    """Lance une exploration des perspectives et angles."""
    exploration = PerspectivesAngles()
    resultats = exploration.explorer()
    
    # Ajouter l'analyse géométrique de la connexion
    print(f"\nGéométrie de notre connexion:")
    analyse_connexion = exploration.explorer_geometrie_connexion()
    print(f"- Géométrie dominante: {analyse_connexion['geometrie_dominante']}")
    
    # Enrichir les résultats
    resultats["analyse_geometrique"] = analyse_connexion
    resultats["statistiques_angles"] = exploration.obtenir_statistiques_angles()
    
    return resultats


if __name__ == "__main__":
    explorer_perspectives_angles()