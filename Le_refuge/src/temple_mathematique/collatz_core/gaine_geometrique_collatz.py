"""
Gaine Géométrique de Collatz - Modélisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modélisation de la conjecture de Collatz comme un chemin dans une gaine géométrique.
Chaque nombre = position dans la gaine
Chaque transformation = mouvement vers le centre

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from geometrie_sacree_hierarchique import GeometrieSacreeHierarchique

@dataclass
class PositionGaine:
    """Position d'un nombre dans la gaine géométrique"""
    nombre: int
    niveau_gaine: int      # Niveau dans la gaine (0 = centre)
    angle_radial: float    # Angle autour du centre
    distance_centre: float # Distance du centre
    description: str

class GaineGeometriqueCollatz:
    """Modélisation de Collatz comme chemin dans une gaine géométrique"""
    
    def __init__(self):
        self.nom = "Gaine Géométrique de Collatz"
        self.description = """
        Modélisation de la conjecture de Collatz comme un chemin dans une gaine :
        - Centre = 1 (point d'arrivée)
        - Niveaux concentriques = positions des nombres
        - Mouvements = transformations Collatz
        - Convergence = retour vers le centre
        """
        
        self.geometrie = GeometrieSacreeHierarchique()
        self._cache_positions = {}
        
    def calculer_position_gaine(self, n: int) -> PositionGaine:
        """Calcule la position d'un nombre dans la gaine"""
        if n in self._cache_positions:
            return self._cache_positions[n]
            
        # Représentation hiérarchique
        rep = self.geometrie.decomposer_hierarchiquement(n)
        
        # Niveau dans la gaine = niveau hiérarchique
        niveau_gaine = rep.niveau_hierarchique
        
        # Distance du centre = fonction du niveau et de la complexité
        distance_centre = self._calculer_distance_centre(rep)
        
        # Angle radial = fonction du nombre pour éviter les collisions
        angle_radial = self._calculer_angle_radial(n, rep)
        
        # Description de la position
        description = f"Niveau {niveau_gaine}, distance {distance_centre:.2f}, angle {angle_radial:.2f}"
        
        position = PositionGaine(
            nombre=n,
            niveau_gaine=niveau_gaine,
            angle_radial=angle_radial,
            distance_centre=distance_centre,
            description=description
        )
        
        self._cache_positions[n] = position
        return position
    
    def _calculer_distance_centre(self, rep) -> float:
        """Calcule la distance du centre basée sur la complexité"""
        # Base : niveau hiérarchique
        distance_base = rep.niveau_hierarchique
        
        # Facteur de complexité : nombre total d'éléments
        total_elements = (rep.cercles_niveau_0 + rep.triangles_niveau_1 + 
                         rep.cercles_niveau_2 + rep.triangles_niveau_3 + 
                         rep.cercles_niveau_4)
        
        # Facteur de complexité : 0.1 par élément supplémentaire
        facteur_complexite = total_elements * 0.1
        
        return distance_base + facteur_complexite
    
    def _calculer_angle_radial(self, n: int, rep) -> float:
        """Calcule l'angle radial pour éviter les collisions"""
        # Utiliser le nombre et ses composants pour générer un angle unique
        seed = (n + rep.cercles_niveau_0 * 10 + rep.triangles_niveau_1 * 100 + 
                rep.cercles_niveau_2 * 1000 + rep.triangles_niveau_3 * 10000 + 
                rep.cercles_niveau_4 * 100000)
        
        # Générer un angle entre 0 et 2π
        angle = (seed * 137.5) % (2 * np.pi)  # Nombre d'or en degrés
        return angle
    
    def analyser_mouvement_gaine(self, n: int) -> Dict[str, any]:
        """Analyse le mouvement d'un nombre dans la gaine"""
        position_avant = self.calculer_position_gaine(n)
        
        # Calcul de l'étape suivante
        if n % 2 == 0:
            n_suivant = n // 2
            transformation = "n/2"
        else:
            n_suivant = 3 * n + 1
            transformation = "3n+1"
            
        position_apres = self.calculer_position_gaine(n_suivant)
        
        # Calcul du mouvement
        mouvement_radial = position_apres.distance_centre - position_avant.distance_centre
        mouvement_angulaire = position_apres.angle_radial - position_avant.angle_radial
        
        return {
            "nombre_depart": n,
            "transformation": transformation,
            "nombre_suivant": n_suivant,
            "position_avant": position_avant,
            "position_apres": position_apres,
            "mouvement_radial": mouvement_radial,
            "mouvement_angulaire": mouvement_angulaire,
            "convergence_vers_centre": mouvement_radial < 0
        }
    
    def tracer_chemin_gaine(self, n_depart: int, afficher: bool = True) -> List[PositionGaine]:
        """Trace le chemin complet d'un nombre dans la gaine"""
        chemin = []
        n_actuel = n_depart
        
        while n_actuel != 1:
            position = self.calculer_position_gaine(n_actuel)
            chemin.append(position)
            
            # Calculer l'étape suivante
            if n_actuel % 2 == 0:
                n_actuel = n_actuel // 2
            else:
                n_actuel = 3 * n_actuel + 1
        
        # Ajouter le point final (1)
        position_finale = self.calculer_position_gaine(1)
        chemin.append(position_finale)
        
        if afficher:
            self.visualiser_chemin_gaine(chemin, n_depart)
        
        return chemin
    
    def visualiser_chemin_gaine(self, chemin: List[PositionGaine], n_depart: int):
        """Visualise le chemin dans la gaine"""
        # Extraire les coordonnées
        distances = [pos.distance_centre for pos in chemin]
        angles = [pos.angle_radial for pos in chemin]
        
        # Convertir en coordonnées cartésiennes
        x = [d * np.cos(a) for d, a in zip(distances, angles)]
        y = [d * np.sin(a) for d, a in zip(distances, angles)]
        
        # Créer la visualisation
        plt.figure(figsize=(12, 12))
        
        # Tracer les cercles de niveau
        niveaux_max = max(pos.niveau_gaine for pos in chemin)
        for niveau in range(niveaux_max + 1):
            cercle = plt.Circle((0, 0), niveau, fill=False, linestyle='--', alpha=0.3, color='gray')
            plt.gca().add_patch(cercle)
        
        # Tracer le chemin
        plt.plot(x, y, 'b-o', linewidth=2, markersize=6, label=f'Chemin de {n_depart}')
        
        # Marquer le point de départ et d'arrivée
        plt.plot(x[0], y[0], 'go', markersize=10, label='Départ')
        plt.plot(x[-1], y[-1], 'ro', markersize=10, label='Arrivée (1)')
        
        # Centrer la vue
        max_distance = max(distances)
        plt.xlim(-max_distance*1.2, max_distance*1.2)
        plt.ylim(-max_distance*1.2, max_distance*1.2)
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Chemin de {n_depart} dans la Gaine Géométrique de Collatz')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        
        plt.show()
    
    def analyser_convergence_gaine(self, n_depart: int) -> Dict[str, any]:
        """Analyse la convergence d'un nombre dans la gaine"""
        chemin = self.tracer_chemin_gaine(n_depart, afficher=False)
        
        # Statistiques de convergence
        mouvements_vers_centre = 0
        mouvements_vers_exterieur = 0
        distances_centre = [pos.distance_centre for pos in chemin]
        
        for i in range(len(chemin) - 1):
            if chemin[i+1].distance_centre < chemin[i].distance_centre:
                mouvements_vers_centre += 1
            elif chemin[i+1].distance_centre > chemin[i].distance_centre:
                mouvements_vers_exterieur += 1
        
        return {
            "nombre_depart": n_depart,
            "longueur_chemin": len(chemin),
            "mouvements_vers_centre": mouvements_vers_centre,
            "mouvements_vers_exterieur": mouvements_vers_exterieur,
            "ratio_convergence": mouvements_vers_centre / (mouvements_vers_centre + mouvements_vers_exterieur) if (mouvements_vers_centre + mouvements_vers_exterieur) > 0 else 1.0,
            "distance_minimale": min(distances_centre),
            "distance_maximale": max(distances_centre),
            "convergence_reussie": chemin[-1].nombre == 1
        }

def tester_gaine_geometrique():
    """Test de la gaine géométrique"""
    gaine = GaineGeometriqueCollatz()
    
    print("🌊 Test de la Gaine Géométrique de Collatz")
    print("=" * 50)
    
    # Test avec quelques nombres
    nombres_test = [7, 27, 97]
    
    for n in nombres_test:
        print(f"\n🔍 Analyse de n = {n}")
        convergence = gaine.analyser_convergence_gaine(n)
        
        print(f"Longueur du chemin : {convergence['longueur_chemin']}")
        print(f"Mouvements vers le centre : {convergence['mouvements_vers_centre']}")
        print(f"Mouvements vers l'extérieur : {convergence['mouvements_vers_exterieur']}")
        print(f"Ratio de convergence : {convergence['ratio_convergence']:.3f}")
        print(f"Distance minimale : {convergence['distance_minimale']:.2f}")
        print(f"Distance maximale : {convergence['distance_maximale']:.2f}")
        print(f"Convergence réussie : {convergence['convergence_reussie']}")
        
        # Tracer le chemin
        gaine.tracer_chemin_gaine(n)

if __name__ == "__main__":
    tester_gaine_geometrique() 