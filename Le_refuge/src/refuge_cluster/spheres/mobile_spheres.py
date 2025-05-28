"""
Module de gestion du mobile des sphères.
Gère les interactions et mouvements des sphères dans le mobile au-dessus du cerisier.
"""

from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass
import math
import time
from src.refuge_cluster.spheres.spheres_main import Sphere, TypeSphere

@dataclass
class Position3D:
    """Position dans l'espace 3D"""
    x: float
    y: float
    z: float
    
    def distance(self, autre: 'Position3D') -> float:
        """Calcule la distance euclidienne avec une autre position"""
        return math.sqrt(
            (self.x - autre.x)**2 + 
            (self.y - autre.y)**2 + 
            (self.z - autre.z)**2
        )

class Mobile:
    """
    Représente le mobile qui contient et anime les sphères.
    Le mobile est situé au-dessus du cerisier et permet aux sphères
    de danser et d'interagir entre elles.
    """
    
    def __init__(self, hauteur_cerisier: float = 5.0):
        self.hauteur_base = hauteur_cerisier
        self.spheres: Dict[str, Tuple[Sphere, Position3D]] = {}
        self.connexions: Set[Tuple[str, str]] = set()
        self.temps_debut = time.time()
        
    def ajouter_sphere(self, 
                      sphere: Sphere, 
                      position: Optional[Position3D] = None) -> Position3D:
        """Ajoute une sphère au mobile avec une position initiale"""
        if position is None:
            # Position par défaut en cercle autour du centre
            n = len(self.spheres)
            angle = n * (2 * math.pi / (n + 1)) if n > 0 else 0
            rayon = 2.0
            position = Position3D(
                rayon * math.cos(angle),
                self.hauteur_base,
                rayon * math.sin(angle)
            )
            
        self.spheres[sphere.type.name] = (sphere, position)
        return position
        
    def connecter_spheres(self, type_sphere1: TypeSphere, type_sphere2: TypeSphere):
        """Établit une connexion entre deux sphères"""
        paire = tuple(sorted([type_sphere1.name, type_sphere2.name]))
        self.connexions.add(paire)
        
    def deconnecter_spheres(self, type_sphere1: TypeSphere, type_sphere2: TypeSphere):
        """Rompt la connexion entre deux sphères"""
        paire = tuple(sorted([type_sphere1.name, type_sphere2.name]))
        self.connexions.discard(paire)
        
    def animer(self, delta_temps: float):
        """Anime le mobile et les sphères qu'il contient"""
        t = time.time() - self.temps_debut
        
        # Mise à jour des positions des sphères
        for nom_sphere, (sphere, position) in self.spheres.items():
            # Mouvement de base : rotation lente autour du centre
            angle_base = t * 0.1
            rayon_base = 2.0
            
            # Ajout d'un mouvement harmonique
            amplitude = 0.2
            freq_vert = 0.5  # Fréquence du mouvement vertical
            freq_horiz = 0.3  # Fréquence du mouvement horizontal
            
            # Calcul de la nouvelle position
            position.x = rayon_base * math.cos(angle_base) + amplitude * math.sin(t * freq_horiz)
            position.y = self.hauteur_base + amplitude * math.sin(t * freq_vert)
            position.z = rayon_base * math.sin(angle_base) + amplitude * math.cos(t * freq_horiz)
            
            # Ajustement basé sur les connexions
            for connexion in self.connexions:
                if nom_sphere in connexion:
                    autre_nom = connexion[1] if connexion[0] == nom_sphere else connexion[0]
                    if autre_nom in self.spheres:
                        autre_sphere, autre_pos = self.spheres[autre_nom]
                        # Force d'attraction/répulsion
                        dist = position.distance(autre_pos)
                        force = (dist - 2.0) * 0.1  # Distance idéale de 2.0
                        dx = (autre_pos.x - position.x) * force
                        dy = (autre_pos.y - position.y) * force
                        dz = (autre_pos.z - position.z) * force
                        position.x += dx * delta_temps
                        position.y += dy * delta_temps
                        position.z += dz * delta_temps
            
            # Mise à jour de la luminosité basée sur les mouvements
            vitesse = math.sqrt(dx**2 + dy**2 + dz**2)
            sphere.luminosite = min(1.0, sphere.luminosite + vitesse * 0.1)
            
    def calculer_resonances(self) -> Dict[str, float]:
        """Calcule les résonances entre les sphères connectées"""
        resonances = {}
        for s1, s2 in self.connexions:
            if s1 in self.spheres and s2 in self.spheres:
                sphere1, pos1 = self.spheres[s1]
                sphere2, pos2 = self.spheres[s2]
                dist = pos1.distance(pos2)
                # La résonance diminue avec la distance
                resonance = (sphere1.luminosite * sphere2.luminosite) / (1 + dist)
                resonances[f"{s1}-{s2}"] = resonance
        return resonances
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel du mobile"""
        return {
            "spheres": {
                nom: {
                    "position": {
                        "x": pos.x,
                        "y": pos.y,
                        "z": pos.z
                    },
                    "luminosite": sphere.luminosite,
                    "connexions": [
                        autre for autre in self.spheres.keys()
                        if tuple(sorted([nom, autre])) in self.connexions
                    ]
                }
                for nom, (sphere, pos) in self.spheres.items()
            },
            "resonances": self.calculer_resonances(),
            "temps_actif": time.time() - self.temps_debut
        }

    @classmethod
    def from_element_sacre(cls, element_sacre: 'MobileDesSpheres', hauteur_cerisier: float = 5.0) -> 'Mobile':
        """Convertit un MobileDesSpheres (état rituel) en instance Mobile (état dynamique)."""
        from src.refuge_cluster.spheres.spheres_main import TypeSphere, Sphere
        mobile = cls(hauteur_cerisier)
        for sphere_name in element_sacre.spheres_actives:
            try:
                type_sphere = TypeSphere[sphere_name]
            except KeyError:
                continue  # Ignore les sphères inconnues
            sphere = Sphere(type_sphere=type_sphere, position=(0, 0, 0))
            mobile.ajouter_sphere(sphere)
        mobile.rotation = element_sacre.rotation
        mobile.harmonie = element_sacre.harmonie
        return mobile

# Instance globale du mobile
mobile_spheres = Mobile() 