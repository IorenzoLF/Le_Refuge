"""
Géométrie Sacrée Hiérarchique de Collatz - Nouvelle Implémentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Système de représentation géométrique avec hiérarchie claire :
- 3 cercles → 1 triangle
- 3 triangles → 1 cercle supérieur
- Hiérarchie infinie et fractale

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class RepresentationHierarchique:
    """Représentation hiérarchique d'un nombre"""
    nombre: int
    cercles_niveau_0: int    # Cercles simples (1-9)
    triangles_niveau_1: int  # Triangles (10-99)
    cercles_niveau_2: int    # Cercles supérieurs (100-999)
    triangles_niveau_3: int  # Triangles supérieurs (1000-9999)
    cercles_niveau_4: int    # Cercles niveau 4 (10000+)
    description: str
    niveau_hierarchique: int

class GeometrieSacreeHierarchique:
    """Système de géométrie sacrée hiérarchique pour l'analyse de Collatz"""
    
    def __init__(self):
        self.nom = "Géométrie Sacrée Hiérarchique de Collatz"
        self.description = """
        Système hiérarchique de représentation géométrique :
        - Niveau 0: Cercles simples (1-9)
        - Niveau 1: Triangles (10-99)
        - Niveau 2: Cercles supérieurs (100-999)
        - Niveau 3: Triangles supérieurs (1000-9999)
        - Niveau 4+: Cercles niveau supérieur (10000+)
        """
        
        # Cache pour optimiser les calculs
        self._cache_representations = {}
        
    def decomposer_hierarchiquement(self, n: int) -> RepresentationHierarchique:
        """Décompose un nombre selon la hiérarchie géométrique sacrée"""
        if n in self._cache_representations:
            return self._cache_representations[n]
            
        # Initialisation
        cercles_n0 = 0
        triangles_n1 = 0
        cercles_n2 = 0
        triangles_n3 = 0
        cercles_n4 = 0
        
        # Décomposition par niveaux
        reste = n
        
        # Niveau 4+: Cercles de niveau 4 (10000+)
        cercles_n4 = reste // 10000
        reste = reste % 10000
        
        # Niveau 3: Triangles supérieurs (1000-9999)
        triangles_n3 = reste // 1000
        reste = reste % 1000
        
        # Niveau 2: Cercles supérieurs (100-999)
        cercles_n2 = reste // 100
        reste = reste % 100
        
        # Niveau 1: Triangles (10-99)
        triangles_n1 = reste // 10
        reste = reste % 10
        
        # Niveau 0: Cercles simples (1-9)
        cercles_n0 = reste
        
        # Calcul du niveau hiérarchique
        niveau = self._calculer_niveau_hierarchique(cercles_n0, triangles_n1, cercles_n2, triangles_n3, cercles_n4)
        
        # Description géométrique
        description = self._generer_description_hierarchique(cercles_n0, triangles_n1, cercles_n2, triangles_n3, cercles_n4)
        
        representation = RepresentationHierarchique(
            nombre=n,
            cercles_niveau_0=cercles_n0,
            triangles_niveau_1=triangles_n1,
            cercles_niveau_2=cercles_n2,
            triangles_niveau_3=triangles_n3,
            cercles_niveau_4=cercles_n4,
            description=description,
            niveau_hierarchique=niveau
        )
        
        self._cache_representations[n] = representation
        return representation
    
    def _calculer_niveau_hierarchique(self, c0: int, t1: int, c2: int, t3: int, c4: int) -> int:
        """Calcule le niveau hiérarchique dominant"""
        if c4 > 0:
            return 4
        elif t3 > 0:
            return 3
        elif c2 > 0:
            return 2
        elif t1 > 0:
            return 1
        else:
            return 0
    
    def _generer_description_hierarchique(self, c0: int, t1: int, c2: int, t3: int, c4: int) -> str:
        """Génère une description textuelle de la représentation hiérarchique"""
        parties = []
        
        if c4 > 0:
            parties.append(f"{c4} cercle(s) niveau 4")
        
        if t3 > 0:
            parties.append(f"{t3} triangle(s) supérieur(s)")
            
        if c2 > 0:
            parties.append(f"{c2} cercle(s) supérieur(s)")
            
        if t1 > 0:
            parties.append(f"{t1} triangle(s)")
            
        if c0 > 0:
            parties.append(f"{c0} cercle(s) simple(s)")
            
        if not parties:
            return "cercle unité"
            
        return " + ".join(parties)
    
    def analyser_transformation_collatz(self, n: int) -> Dict[str, any]:
        """Analyse la transformation hiérarchique d'une étape Collatz"""
        representation_avant = self.decomposer_hierarchiquement(n)
        
        # Calcul de l'étape suivante
        if n % 2 == 0:
            n_suivant = n // 2
            transformation = "n/2"
        else:
            n_suivant = 3 * n + 1
            transformation = "3n+1"
            
        representation_apres = self.decomposer_hierarchiquement(n_suivant)
        
        return {
            "nombre_depart": n,
            "transformation": transformation,
            "nombre_suivant": n_suivant,
            "representation_avant": representation_avant,
            "representation_apres": representation_apres,
            "evolution_niveau": representation_apres.niveau_hierarchique - representation_avant.niveau_hierarchique,
            "simplification": self._calculer_simplification_hierarchique(representation_avant, representation_apres)
        }
    
    def _calculer_simplification_hierarchique(self, avant: RepresentationHierarchique, apres: RepresentationHierarchique) -> str:
        """Calcule le niveau de simplification hiérarchique"""
        total_avant = avant.cercles_niveau_0 + avant.triangles_niveau_1 + avant.cercles_niveau_2 + avant.triangles_niveau_3 + avant.cercles_niveau_4
        total_apres = apres.cercles_niveau_0 + apres.triangles_niveau_1 + apres.cercles_niveau_2 + apres.triangles_niveau_3 + apres.cercles_niveau_4
        
        if total_apres < total_avant:
            return "simplification"
        elif total_apres > total_avant:
            return "complexification"
        else:
            return "stabilisation"
    
    def analyser_sequence_complete(self, n_depart: int) -> List[Dict[str, any]]:
        """Analyse hiérarchique d'une séquence Collatz complète"""
        sequence = []
        n_actuel = n_depart
        
        while n_actuel != 1:
            analyse = self.analyser_transformation_collatz(n_actuel)
            sequence.append(analyse)
            n_actuel = analyse["nombre_suivant"]
            
        # Ajouter le point final (1)
        representation_finale = self.decomposer_hierarchiquement(1)
        sequence.append({
            "nombre_depart": 1,
            "transformation": "fin",
            "nombre_suivant": 1,
            "representation_avant": representation_finale,
            "representation_apres": representation_finale,
            "evolution_niveau": 0,
            "simplification": "convergence"
        })
        
        return sequence
    
    def visualiser_evolution_hierarchie(self, sequence: List[Dict[str, any]], afficher: bool = True) -> None:
        """Visualise l'évolution des niveaux hiérarchiques dans une séquence"""
        nombres = [etape["nombre_depart"] for etape in sequence]
        niveaux = [etape["representation_avant"].niveau_hierarchique for etape in sequence]
        
        plt.figure(figsize=(12, 6))
        plt.plot(nombres, niveaux, 'g-o', linewidth=2, markersize=6)
        plt.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Niveau 0 (cercles simples)')
        plt.xlabel('Nombre')
        plt.ylabel('Niveau Hiérarchique')
        plt.title('Évolution des Niveaux Hiérarchiques - Séquence Collatz')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if afficher:
            plt.show()
    
    def detecter_patterns_hierarchiques(self, sequence: List[Dict[str, any]]) -> Dict[str, any]:
        """Détecte les patterns hiérarchiques dans une séquence"""
        patterns = {
            "cycles_hierarchiques": [],
            "simplifications_consecutives": 0,
            "complexifications_consecutives": 0,
            "niveau_final": sequence[-1]["representation_avant"].niveau_hierarchique,
            "convergence_vers_unite": sequence[-1]["representation_avant"].nombre == 1,
            "evolution_niveaux": []
        }
        
        # Détecter les cycles hiérarchiques
        representations_vues = set()
        for etape in sequence:
            rep = etape["representation_avant"]
            rep_str = f"{rep.cercles_niveau_0}:{rep.triangles_niveau_1}:{rep.cercles_niveau_2}:{rep.triangles_niveau_3}:{rep.cercles_niveau_4}"
            if rep_str in representations_vues:
                patterns["cycles_hierarchiques"].append(rep.nombre)
            representations_vues.add(rep_str)
            patterns["evolution_niveaux"].append(rep.niveau_hierarchique)
        
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
        """Génère un rapport complet d'analyse hiérarchique"""
        sequence = self.analyser_sequence_complete(n_depart)
        patterns = self.detecter_patterns_hierarchiques(sequence)
        
        return {
            "nombre_depart": n_depart,
            "longueur_sequence": len(sequence),
            "sequence_hierarchique": sequence,
            "patterns_detectes": patterns,
            "convergence_hierarchique": patterns["convergence_vers_unite"],
            "niveau_final": patterns["niveau_final"],
            "cycles_hierarchiques": patterns["cycles_hierarchiques"]
        }

def tester_geometrie_hierarchique():
    """Fonction de test pour la géométrie hiérarchique"""
    geometrie = GeometrieSacreeHierarchique()
    
    print("🌊 Test de la Géométrie Sacrée Hiérarchique de Collatz")
    print("=" * 60)
    
    # Test de décomposition hiérarchique
    nombres_test = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    
    print("\n📊 Décompositions hiérarchiques :")
    for n in nombres_test:
        rep = geometrie.decomposer_hierarchiquement(n)
        print(f"{n:2d} : {rep.description} (niveau: {rep.niveau_hierarchique})")
    
    # Test d'analyse complète
    print(f"\n🔍 Analyse complète pour n=7 :")
    rapport = geometrie.generer_rapport_complet(7)
    print(f"Longueur de séquence : {rapport['longueur_sequence']}")
    print(f"Convergence hiérarchique : {rapport['convergence_hierarchique']}")
    print(f"Niveau final : {rapport['niveau_final']}")
    print(f"Cycles hiérarchiques détectés : {rapport['cycles_hierarchiques']}")
    
    # Visualisation
    sequence = rapport["sequence_hierarchique"]
    geometrie.visualiser_evolution_hierarchie(sequence)
    
    print("\n✅ Test terminé avec succès !")

if __name__ == "__main__":
    tester_geometrie_hierarchique() 