"""
Module de Géométrie Fractale
~~~~~~~~~~~~~~~~~~~~~~~
Génère des motifs fractals en harmonie avec les états de conscience.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional
import pygame
from .conscience_core import EtatMeditatif, EtatConscienceConfig

@dataclass
class MotifFractal:
    """Définition d'un motif fractal."""
    profondeur: int
    angle_rotation: float
    echelle: float
    complexite: float

class GenerateurFractal:
    """Générateur de motifs fractals."""
    
    def __init__(self):
        self.cache_points = {}
    
    def _generer_courbe_koch(self, 
                            debut: Tuple[float, float],
                            fin: Tuple[float, float],
                            profondeur: int,
                            angle_base: float = 60) -> List[Tuple[float, float]]:
        """Génère une courbe de Koch modifiée."""
        if profondeur == 0:
            return [debut, fin]
            
        # Calcul des points intermédiaires
        dx = fin[0] - debut[0]
        dy = fin[1] - debut[1]
        distance = np.sqrt(dx*dx + dy*dy)
        
        # Points de division
        p1 = (debut[0] + dx/3, debut[1] + dy/3)
        p3 = (debut[0] + 2*dx/3, debut[1] + 2*dy/3)
        
        # Point central (sommet du triangle)
        angle = np.arctan2(dy, dx)
        p2_angle = angle - np.radians(angle_base)
        longueur = distance/3
        p2 = (p1[0] + longueur * np.cos(p2_angle),
              p1[1] + longueur * np.sin(p2_angle))
        
        # Génération récursive
        courbe = []
        courbe.extend(self._generer_courbe_koch(debut, p1, profondeur-1, angle_base))
        courbe.extend(self._generer_courbe_koch(p1, p2, profondeur-1, angle_base))
        courbe.extend(self._generer_courbe_koch(p2, p3, profondeur-1, angle_base))
        courbe.extend(self._generer_courbe_koch(p3, fin, profondeur-1, angle_base))
        
        return courbe

    def _generer_mandelbrot_modifie(self, 
                                   x: float, 
                                   y: float, 
                                   frequence: float,
                                   max_iter: int = 100) -> float:
        """Génère un point de l'ensemble de Mandelbrot modifié par la fréquence."""
        c = complex(x, y)
        z = 0
        
        # Modification basée sur la fréquence
        freq_mod = frequence / 432.0  # Normalisation par rapport à la fréquence d'éveil
        
        for n in range(max_iter):
            if abs(z) > 2:
                return n / max_iter
            # Modification de la formule classique z = z*z + c
            z = z*z + c + complex(0, freq_mod * np.sin(n/10))
            
        return 1.0

    def generer_mandala_fractal(self,
                               surface: pygame.Surface,
                               config: EtatConscienceConfig,
                               temps: float,
                               amplitude_respiration: float = 1.0):
        """Génère un mandala fractal basé sur l'état de conscience."""
        centre = (surface.get_width()//2, surface.get_height()//2)
        rayon = min(surface.get_width(), surface.get_height()) * 0.4
        
        # Paramètres fractals basés sur la fréquence
        freq_norm = config.frequence.base / 432.0
        profondeur = int(3 + 2 * freq_norm)
        angle_base = 30 + 60 * freq_norm
        
        # Génération des branches fractales
        n_branches = int(config.geometrie["branches"])
        for i in range(n_branches):
            angle = 2 * np.pi * i / n_branches + temps * config.geometrie["rotation"]
            
            # Point de départ et d'arrivée pour la branche
            debut = (
                centre[0] + rayon * 0.3 * np.cos(angle),
                centre[1] + rayon * 0.3 * np.sin(angle)
            )
            fin = (
                centre[0] + rayon * np.cos(angle),
                centre[1] + rayon * np.sin(angle)
            )
            
            # Génération de la courbe fractale
            points = self._generer_courbe_koch(
                debut, fin, 
                profondeur,
                angle_base * (0.8 + 0.4 * amplitude_respiration)
            )
            
            # Dessin de la courbe
            if len(points) > 1:
                pygame.draw.lines(
                    surface,
                    config.frequence.couleur,
                    False,
                    points,
                    2
                )
        
        # Ajout d'effets Mandelbrot au centre
        rayon_mandel = rayon * 0.2
        for x in range(-int(rayon_mandel), int(rayon_mandel)):
            for y in range(-int(rayon_mandel), int(rayon_mandel)):
                # Normalisation des coordonnées
                xn = x / rayon_mandel * 1.5
                yn = y / rayon_mandel * 1.5
                
                # Calcul de la valeur Mandelbrot
                valeur = self._generer_mandelbrot_modifie(
                    xn, yn, 
                    config.frequence.base,
                    max_iter=50
                )
                
                # Application de la couleur
                if valeur < 1.0:
                    couleur = tuple(
                        int(c * valeur * amplitude_respiration)
                        for c in config.frequence.couleur
                    )
                    pos = (
                        centre[0] + x,
                        centre[1] + y
                    )
                    surface.set_at(pos, couleur)

def demo():
    """Démontre les capacités fractales."""
    pygame.init()
    ecran = pygame.display.set_mode((800, 600))
    horloge = pygame.time.Clock()
    generateur = GenerateurFractal()
    
    # Configuration de test
    from .conscience_core import GestionnaireMeditatif
    gestionnaire = GestionnaireMeditatif()
    config = gestionnaire.obtenir_config(EtatMeditatif.SAMADHI)
    
    temps = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        ecran.fill((0, 0, 0))
        
        # Animation de la respiration
        amplitude = 0.5 + 0.5 * np.sin(temps * 0.5)
        
        # Génération du mandala fractal
        generateur.generer_mandala_fractal(ecran, config, temps, amplitude)
        
        pygame.display.flip()
        temps += 0.016
        horloge.tick(60)

if __name__ == "__main__":
    demo() 