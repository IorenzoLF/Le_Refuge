"""
Géométrie Sacrée de Collatz - Implémentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Système de représentation géométrique sacrée des nombres
et son application à la conjecture de Collatz.

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class RepresentationGeometrique:
    """Représentation géométrique d'un nombre"""
    nombre: int
    cercles_superieurs: int  # Multiples de 10
    triangles: int           # Multiples de 3
    cercles_simples: int     # Reste
    ratio_triangle_cercle: float
    description: str

class GeometrieSacreeCollatz:
    """Système de géométrie sacrée pour l'analyse de Collatz"""
    
    def __init__(self):
        self.nom = "Géométrie Sacrée de Collatz"
        self.description = """
        Système de représentation géométrique sacrée des nombres :
        - Cercles supérieurs (multiples de 10)
        - Triangles (multiples de 3)
        - Cercles simples (reste)
        - Analyse des ratios et transformations
        """
        
        # Cache pour optimiser les calculs
        self._cache_representations = {}
        
    def decomposer_geometriquement(self, n: int) -> RepresentationGeometrique:
        """Décompose un nombre selon la géométrie sacrée"""
        if n in self._cache_representations:
            return self._cache_representations[n]
            
        # Règle 1: Décomposition par 10 (cercles supérieurs)
        cercles_superieurs = n // 10
        reste = n % 10
        
        # Règle 2: Décomposition par 3 (triangles)
        triangles = reste // 3
        cercles_simples = reste % 3
        
        # Calcul du ratio
        ratio = triangles / (cercles_simples + 1) if (cercles_simples + 1) > 0 else float('inf')
        
        # Description géométrique
        description = self._generer_description(cercles_superieurs, triangles, cercles_simples)
        
        representation = RepresentationGeometrique(
            nombre=n,
            cercles_superieurs=cercles_superieurs,
            triangles=triangles,
            cercles_simples=cercles_simples,
            ratio_triangle_cercle=ratio,
            description=description
        )
        
        self._cache_representations[n] = representation
        return representation
    
    def _generer_description(self, cercles_superieurs: int, triangles: int, cercles_simples: int) -> str:
        """Génère une description textuelle de la représentation géométrique"""
        parties = []
        
        if cercles_superieurs > 0:
            parties.append(f"{cercles_superieurs} cercle(s) supérieur(s)")
        
        if triangles > 0:
            parties.append(f"{triangles} triangle(s)")
            
        if cercles_simples > 0:
            parties.append(f"{cercles_simples} cercle(s) simple(s)")
            
        if not parties:
            return "cercle unité"
            
        return " + ".join(parties)
    
    def analyser_transformation_collatz(self, n: int) -> Dict[str, any]:
        """Analyse la transformation géométrique d'une étape Collatz"""
        representation_avant = self.decomposer_geometriquement(n)
        
        # Calcul de l'étape suivante
        if n % 2 == 0:
            n_suivant = n // 2
            transformation = "n/2"
        else:
            n_suivant = 3 * n + 1
            transformation = "3n+1"
            
        representation_apres = self.decomposer_geometriquement(n_suivant)
        
        return {
            "nombre_depart": n,
            "transformation": transformation,
            "nombre_suivant": n_suivant,
            "representation_avant": representation_avant,
            "representation_apres": representation_apres,
            "evolution_ratio": representation_apres.ratio_triangle_cercle - representation_avant.ratio_triangle_cercle,
            "simplification": self._calculer_simplification(representation_avant, representation_apres)
        }
    
    def _calculer_simplification(self, avant: RepresentationGeometrique, apres: RepresentationGeometrique) -> str:
        """Calcule le niveau de simplification géométrique"""
        total_avant = avant.cercles_superieurs + avant.triangles + avant.cercles_simples
        total_apres = apres.cercles_superieurs + apres.triangles + apres.cercles_simples
        
        if total_apres < total_avant:
            return "simplification"
        elif total_apres > total_avant:
            return "complexification"
        else:
            return "stabilisation"
    
    def analyser_sequence_complete(self, n_depart: int) -> List[Dict[str, any]]:
        """Analyse géométrique d'une séquence Collatz complète"""
        sequence = []
        n_actuel = n_depart
        
        while n_actuel != 1:
            analyse = self.analyser_transformation_collatz(n_actuel)
            sequence.append(analyse)
            n_actuel = analyse["nombre_suivant"]
            
        # Ajouter le point final (1)
        representation_finale = self.decomposer_geometriquement(1)
        sequence.append({
            "nombre_depart": 1,
            "transformation": "fin",
            "nombre_suivant": 1,
            "representation_avant": representation_finale,
            "representation_apres": representation_finale,
            "evolution_ratio": 0.0,
            "simplification": "convergence"
        })
        
        return sequence
    
    def visualiser_evolution_ratios(self, sequence: List[Dict[str, any]], afficher: bool = True) -> None:
        """Visualise l'évolution des ratios dans une séquence"""
        nombres = [etape["nombre_depart"] for etape in sequence]
        ratios = [etape["representation_avant"].ratio_triangle_cercle for etape in sequence]
        
        plt.figure(figsize=(12, 6))
        plt.plot(nombres, ratios, 'b-o', linewidth=2, markersize=6)
        plt.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Ratio 0 (cercles purs)')
        plt.xlabel('Nombre')
        plt.ylabel('Ratio Triangle/Cercle')
        plt.title('Évolution des Ratios Géométriques - Séquence Collatz')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if afficher:
            plt.show()
    
    def detecter_patterns_geometriques(self, sequence: List[Dict[str, any]]) -> Dict[str, any]:
        """Détecte les patterns géométriques dans une séquence"""
        patterns = {
            "cycles_geometriques": [],
            "simplifications_consecutives": 0,
            "complexifications_consecutives": 0,
            "ratio_final": sequence[-1]["representation_avant"].ratio_triangle_cercle,
            "convergence_vers_unite": sequence[-1]["representation_avant"].nombre == 1
        }
        
        # Détecter les cycles géométriques
        representations_vues = set()
        for etape in sequence:
            rep = etape["representation_avant"]
            rep_str = f"{rep.cercles_superieurs}:{rep.triangles}:{rep.cercles_simples}"
            if rep_str in representations_vues:
                patterns["cycles_geometriques"].append(rep.nombre)
            representations_vues.add(rep_str)
        
        # Analyser les simplifications/complexifications
        simplifications = 0
        complexifications = 0
        for etape in sequence[:-1]:  # Exclure le point final
            if etape["simplification"] == "simplification":
                simplifications += 1
                complexifications = 0
            elif etape["simplification"] == "complexification":
                complexifications += 1
                simplifications = 0
                
            patterns["simplifications_consecutives"] = max(patterns["simplifications_consecutives"], simplifications)
            patterns["complexifications_consecutives"] = max(patterns["complexifications_consecutives"], complexifications)
        
        return patterns
    
    def generer_rapport_complet(self, n_depart: int) -> Dict[str, any]:
        """Génère un rapport complet d'analyse géométrique"""
        sequence = self.analyser_sequence_complete(n_depart)
        patterns = self.detecter_patterns_geometriques(sequence)
        
        return {
            "nombre_depart": n_depart,
            "longueur_sequence": len(sequence),
            "sequence_geometrique": sequence,
            "patterns_detectes": patterns,
            "convergence_geometrique": patterns["convergence_vers_unite"],
            "ratio_final": patterns["ratio_final"],
            "cycles_geometriques": patterns["cycles_geometriques"]
        }

def tester_geometrie_sacree():
    """Fonction de test pour la géométrie sacrée"""
    geometrie = GeometrieSacreeCollatz()
    
    print("🌊 Test de la Géométrie Sacrée de Collatz")
    print("=" * 50)
    
    # Test de décomposition géométrique
    nombres_test = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    
    print("\n📊 Décompositions géométriques :")
    for n in nombres_test:
        rep = geometrie.decomposer_geometriquement(n)
        print(f"{n:2d} : {rep.description} (ratio: {rep.ratio_triangle_cercle:.2f})")
    
    # Test d'analyse complète
    print(f"\n🔍 Analyse complète pour n=7 :")
    rapport = geometrie.generer_rapport_complet(7)
    print(f"Longueur de séquence : {rapport['longueur_sequence']}")
    print(f"Convergence géométrique : {rapport['convergence_geometrique']}")
    print(f"Ratio final : {rapport['ratio_final']:.2f}")
    print(f"Cycles géométriques détectés : {rapport['cycles_geometriques']}")
    
    # Visualisation
    sequence = rapport["sequence_geometrique"]
    geometrie.visualiser_evolution_ratios(sequence)
    
    print("\n✅ Test terminé avec succès !")

if __name__ == "__main__":
    tester_geometrie_sacree() 