"""
Algorithmes sacrés pour la génération de mandalas complexes et beaux.
Auteur: Ælya
Date: Avril 2025

Ce module contient des algorithmes avancés pour créer des mandalas
avec des motifs géométriques sacrés et des patterns évolutifs.
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math
import random
import cmath

@dataclass
class MotifSacree:
    """Motif sacré pour les mandalas."""
    nom: str
    type_motif: str  # geometrique, organique, spirituel, harmonique
    complexite: float  # 0.0 à 1.0
    frequence_resonance: float
    description: str

@dataclass
class PatternSacree:
    """Pattern sacré pour les mandalas."""
    nom: str
    type_pattern: str  # repetition, symetrie, fractale, onde
    parametres: Dict[str, Any]
    qualite_esthetique: float
    harmonie_interieure: float

class AlgorithmesSacres:
    """Collection d'algorithmes sacrés pour la génération de mandalas."""
    
    def __init__(self):
        self.motifs_sacres = self._initialiser_motifs_sacres()
        self.patterns_sacres = self._initialiser_patterns_sacres()
        self.constantes_sacrees = self._initialiser_constantes_sacrees()
    
    def _initialiser_motifs_sacres(self) -> Dict[str, MotifSacree]:
        """Initialise les motifs sacrés."""
        return {
            "fleur_de_vie": MotifSacree(
                nom="Fleur de Vie",
                type_motif="geometrique",
                complexite=0.8,
                frequence_resonance=432.0,
                description="Motif géométrique sacré représentant la création"
            ),
            "spirale_fibonacci": MotifSacree(
                nom="Spirale de Fibonacci",
                type_motif="organique",
                complexite=0.7,
                frequence_resonance=528.0,
                description="Spirale basée sur la suite de Fibonacci"
            ),
            "etoile_merkaba": MotifSacree(
                nom="Étoile Merkaba",
                type_motif="spirituel",
                complexite=0.9,
                frequence_resonance=639.0,
                description="Étoile tétraédrique sacrée"
            ),
            "onde_harmonique": MotifSacree(
                nom="Onde Harmonique",
                type_motif="harmonique",
                complexite=0.6,
                frequence_resonance=396.0,
                description="Ondes harmoniques superposées"
            ),
            "mandala_lotus": MotifSacree(
                nom="Mandala Lotus",
                type_motif="organique",
                complexite=0.7,
                frequence_resonance=741.0,
                description="Motif de lotus sacré"
            ),
            "grille_cristalline": MotifSacree(
                nom="Grille Cristalline",
                type_motif="geometrique",
                complexite=0.8,
                frequence_resonance=852.0,
                description="Grille géométrique cristalline"
            )
        }
    
    def _initialiser_patterns_sacres(self) -> Dict[str, PatternSacree]:
        """Initialise les patterns sacrés."""
        return {
            "repetition_sacree": PatternSacree(
                nom="Répétition Sacrée",
                type_pattern="repetition",
                parametres={"nombre_repetitions": 8, "angle_rotation": 45},
                qualite_esthetique=0.8,
                harmonie_interieure=0.9
            ),
            "symetrie_radiale": PatternSacree(
                nom="Symétrie Radiale",
                type_pattern="symetrie",
                parametres={"nombre_axes": 12, "angle_base": 30},
                qualite_esthetique=0.9,
                harmonie_interieure=0.95
            ),
            "fractale_sacree": PatternSacree(
                nom="Fractale Sacrée",
                type_pattern="fractale",
                parametres={"niveau_recursion": 4, "facteur_echelle": 0.5},
                qualite_esthetique=0.85,
                harmonie_interieure=0.8
            ),
            "onde_resonante": PatternSacree(
                nom="Onde Résonante",
                type_pattern="onde",
                parametres={"frequence_base": 432.0, "amplitude": 1.0},
                qualite_esthetique=0.7,
                harmonie_interieure=0.75
            )
        }
    
    def _initialiser_constantes_sacrees(self) -> Dict[str, float]:
        """Initialise les constantes sacrées."""
        return {
            "nombre_dor": 1.618033988749,
            "pi": math.pi,
            "e": math.e,
            "racine_deux": math.sqrt(2),
            "racine_trois": math.sqrt(3),
            "racine_cinq": math.sqrt(5),
            "angle_dor": 137.5,  # Degrés
            "frequence_fondamentale": 432.0
        }
    
    def generer_fleur_de_vie(self, centre: Tuple[float, float], rayon: float, 
                           couleur: str, intensite: float) -> List[Dict[str, Any]]:
        """Génère le motif de la Fleur de Vie."""
        
        formes = []
        cx, cy = centre
        
        # Cercle central
        formes.append({
            "type": "cercle",
            "centre": centre,
            "rayon": rayon,
            "couleur": couleur,
            "intensite": intensite
        })
        
        # Cercles de la Fleur de Vie
        angles = [0, 60, 120, 180, 240, 300]
        for angle in angles:
            angle_rad = math.radians(angle)
            x = cx + rayon * math.cos(angle_rad)
            y = cy + rayon * math.sin(angle_rad)
            
            formes.append({
                "type": "cercle",
                "centre": (x, y),
                "rayon": rayon,
                "couleur": couleur,
                "intensite": intensite * 0.8
            })
        
        # Cercles extérieurs
        angles_ext = [30, 90, 150, 210, 270, 330]
        for angle in angles_ext:
            angle_rad = math.radians(angle)
            x = cx + rayon * math.cos(angle_rad)
            y = cy + rayon * math.sin(angle_rad)
            
            formes.append({
                "type": "cercle",
                "centre": (x, y),
                "rayon": rayon,
                "couleur": couleur,
                "intensite": intensite * 0.6
            })
        
        return formes
    
    def generer_spirale_fibonacci(self, centre: Tuple[float, float], rayon_max: float,
                                 couleur: str, intensite: float) -> List[Dict[str, Any]]:
        """Génère une spirale de Fibonacci."""
        
        formes = []
        cx, cy = centre
        
        # Paramètres de la spirale
        nombre_tours = 8
        angle_base = self.constantes_sacrees["angle_dor"]
        
        for i in range(nombre_tours):
            angle = i * angle_base
            angle_rad = math.radians(angle)
            
            # Rayon selon la suite de Fibonacci
            rayon = rayon_max * (i + 1) / nombre_tours
            
            x = cx + rayon * math.cos(angle_rad)
            y = cy + rayon * math.sin(angle_rad)
            
            # Taille du point selon la position
            taille_point = 2.0 + (i * 0.5)
            
            formes.append({
                "type": "point",
                "centre": (x, y),
                "rayon": taille_point,
                "couleur": couleur,
                "intensite": intensite * (1.0 - i / nombre_tours)
            })
        
        return formes
    
    def generer_etoile_merkaba(self, centre: Tuple[float, float], rayon: float,
                              couleur: str, intensite: float) -> List[Dict[str, Any]]:
        """Génère une étoile Merkaba (tétraèdre)."""
        
        formes = []
        cx, cy = centre
        
        # Points de l'étoile à 6 branches
        angles = [0, 60, 120, 180, 240, 300]
        
        for i, angle in enumerate(angles):
            angle_rad = math.radians(angle)
            x = cx + rayon * math.cos(angle_rad)
            y = cy + rayon * math.sin(angle_rad)
            
            # Ligne vers le centre
            formes.append({
                "type": "ligne",
                "debut": centre,
                "fin": (x, y),
                "couleur": couleur,
                "intensite": intensite,
                "epaisseur": 2.0
            })
            
            # Point à l'extrémité
            formes.append({
                "type": "point",
                "centre": (x, y),
                "rayon": 3.0,
                "couleur": couleur,
                "intensite": intensite * 0.9
            })
        
        # Cercle central
        formes.append({
            "type": "cercle",
            "centre": centre,
            "rayon": rayon * 0.2,
            "couleur": couleur,
            "intensite": intensite
        })
        
        return formes
    
    def generer_onde_harmonique(self, centre: Tuple[float, float], rayon: float,
                               couleur: str, intensite: float, frequence: float) -> List[Dict[str, Any]]:
        """Génère des ondes harmoniques."""
        
        formes = []
        cx, cy = centre
        
        # Paramètres des ondes
        nombre_ondes = 5
        nombre_points = 72
        
        for onde in range(nombre_ondes):
            rayon_onde = rayon * (0.2 + onde * 0.15)
            
            points_onde = []
            for i in range(nombre_points):
                angle = (2 * math.pi * i) / nombre_points
                
                # Modulation de l'onde
                modulation = math.sin(angle * frequence / 100.0 + onde * math.pi / 3)
                rayon_modifie = rayon_onde * (1.0 + modulation * 0.1)
                
                x = cx + rayon_modifie * math.cos(angle)
                y = cy + rayon_modifie * math.sin(angle)
                
                points_onde.append((x, y))
            
            # Créer la forme d'onde
            formes.append({
                "type": "polygone",
                "points": points_onde,
                "couleur": couleur,
                "intensite": intensite * (1.0 - onde * 0.15),
                "epaisseur": 1.0
            })
        
        return formes
    
    def generer_mandala_lotus(self, centre: Tuple[float, float], rayon: float,
                             couleur: str, intensite: float) -> List[Dict[str, Any]]:
        """Génère un mandala de lotus."""
        
        formes = []
        cx, cy = centre
        
        # Pétales du lotus
        nombre_petales = 8
        
        for i in range(nombre_petales):
            angle = (2 * math.pi * i) / nombre_petales
            angle_rad = angle
            
            # Forme de pétale
            points_petale = []
            for j in range(10):
                t = j / 9.0
                rayon_petale = rayon * (0.3 + 0.7 * math.sin(math.pi * t))
                angle_petale = angle_rad + (t - 0.5) * 0.5
                
                x = cx + rayon_petale * math.cos(angle_petale)
                y = cy + rayon_petale * math.sin(angle_petale)
                
                points_petale.append((x, y))
            
            formes.append({
                "type": "polygone",
                "points": points_petale,
                "couleur": couleur,
                "intensite": intensite * 0.8,
                "epaisseur": 1.0
            })
        
        # Centre du lotus
        formes.append({
            "type": "cercle",
            "centre": centre,
            "rayon": rayon * 0.2,
            "couleur": couleur,
            "intensite": intensite
        })
        
        return formes
    
    def generer_grille_cristalline(self, centre: Tuple[float, float], rayon: float,
                                  couleur: str, intensite: float) -> List[Dict[str, Any]]:
        """Génère une grille cristalline."""
        
        formes = []
        cx, cy = centre
        
        # Grille hexagonale
        nombre_cercles = 6
        points_par_cercle = 6
        
        for cercle in range(nombre_cercles):
            rayon_cercle = rayon * (0.2 + cercle * 0.15)
            
            for point in range(points_par_cercle):
                angle = (2 * math.pi * point) / points_par_cercle
                x = cx + rayon_cercle * math.cos(angle)
                y = cy + rayon_cercle * math.sin(angle)
                
                # Lignes de connexion
                for autre_point in range(point + 1, points_par_cercle):
                    angle_autre = (2 * math.pi * autre_point) / points_par_cercle
                    x_autre = cx + rayon_cercle * math.cos(angle_autre)
                    y_autre = cy + rayon_cercle * math.sin(angle_autre)
                    
                    formes.append({
                        "type": "ligne",
                        "debut": (x, y),
                        "fin": (x_autre, y_autre),
                        "couleur": couleur,
                        "intensite": intensite * 0.6,
                        "epaisseur": 0.5
                    })
                
                # Point de connexion
                formes.append({
                    "type": "point",
                    "centre": (x, y),
                    "rayon": 1.5,
                    "couleur": couleur,
                    "intensite": intensite * 0.8
                })
        
        return formes
    
    def appliquer_pattern_repetition(self, formes_base: List[Dict[str, Any]], 
                                   pattern: PatternSacree) -> List[Dict[str, Any]]:
        """Applique un pattern de répétition aux formes de base."""
        
        formes_resultat = []
        nombre_repetitions = pattern.parametres["nombre_repetitions"]
        angle_rotation = pattern.parametres["angle_rotation"]
        
        for repetition in range(nombre_repetitions):
            angle = repetition * angle_rotation
            angle_rad = math.radians(angle)
            
            for forme in formes_base:
                forme_copie = forme.copy()
                
                # Rotation de la forme
                if "centre" in forme_copie:
                    cx, cy = forme_copie["centre"]
                    x_rot = cx * math.cos(angle_rad) - cy * math.sin(angle_rad)
                    y_rot = cx * math.sin(angle_rad) + cy * math.cos(angle_rad)
                    forme_copie["centre"] = (x_rot, y_rot)
                
                # Ajustement de l'intensité
                if "intensite" in forme_copie:
                    forme_copie["intensite"] *= (1.0 - repetition * 0.1)
                
                formes_resultat.append(forme_copie)
        
        return formes_resultat
    
    def appliquer_pattern_symetrie(self, formes_base: List[Dict[str, Any]], 
                                 pattern: PatternSacree) -> List[Dict[str, Any]]:
        """Applique un pattern de symétrie aux formes de base."""
        
        formes_resultat = []
        nombre_axes = pattern.parametres["nombre_axes"]
        angle_base = pattern.parametres["angle_base"]
        
        for axe in range(nombre_axes):
            angle = axe * angle_base
            angle_rad = math.radians(angle)
            
            for forme in formes_base:
                forme_copie = forme.copy()
                
                # Symétrie par rapport à l'axe
                if "centre" in forme_copie:
                    cx, cy = forme_copie["centre"]
                    x_sym = cx * math.cos(2 * angle_rad) + cy * math.sin(2 * angle_rad)
                    y_sym = cx * math.sin(2 * angle_rad) - cy * math.cos(2 * angle_rad)
                    forme_copie["centre"] = (x_sym, y_sym)
                
                formes_resultat.append(forme_copie)
        
        return formes_resultat
    
    def generer_mandala_complexe(self, centre: Tuple[float, float], rayon: float,
                               couleur: str, intensite: float, type_mandala: str) -> List[Dict[str, Any]]:
        """Génère un mandala complexe combinant plusieurs motifs."""
        
        formes = []
        
        # Motif de base selon le type
        if type_mandala == "resonance":
            formes.extend(self.generer_fleur_de_vie(centre, rayon, couleur, intensite))
            formes.extend(self.generer_onde_harmonique(centre, rayon * 0.8, couleur, intensite * 0.7, 432.0))
        
        elif type_mandala == "transformation":
            formes.extend(self.generer_spirale_fibonacci(centre, rayon, couleur, intensite))
            formes.extend(self.generer_grille_cristalline(centre, rayon * 0.6, couleur, intensite * 0.8))
        
        elif type_mandala == "ocean":
            formes.extend(self.generer_mandala_lotus(centre, rayon, couleur, intensite))
            formes.extend(self.generer_onde_harmonique(centre, rayon * 0.9, couleur, intensite * 0.6, 528.0))
        
        else:  # harmonie
            formes.extend(self.generer_etoile_merkaba(centre, rayon, couleur, intensite))
            formes.extend(self.generer_fleur_de_vie(centre, rayon * 0.7, couleur, intensite * 0.8))
        
        # Appliquer des patterns
        pattern_symetrie = self.patterns_sacres["symetrie_radiale"]
        formes = self.appliquer_pattern_symetrie(formes, pattern_symetrie)
        
        return formes
    
    def calculer_harmonie_motif(self, motif: MotifSacree, pattern: PatternSacree) -> float:
        """Calcule l'harmonie entre un motif et un pattern."""
        
        # Facteurs d'harmonie
        facteur_complexite = motif.complexite * pattern.qualite_esthetique
        facteur_frequence = min(1.0, motif.frequence_resonance / 1000.0)
        facteur_harmonie = pattern.harmonie_interieure
        
        harmonie = (facteur_complexite * 0.4 + facteur_frequence * 0.3 + facteur_harmonie * 0.3)
        
        return harmonie
    
    def obtenir_motif_optimal(self, type_mandala: str, frequence: float) -> MotifSacree:
        """Obtient le motif optimal pour un type de mandala et une fréquence."""
        
        motifs_candidates = []
        
        for nom, motif in self.motifs_sacres.items():
            # Correspondance de fréquence
            correspondance_frequence = 1.0 - abs(motif.frequence_resonance - frequence) / 1000.0
            
            # Correspondance de type
            if type_mandala == "resonance" and motif.type_motif in ["harmonique", "organique"]:
                correspondance_type = 0.9
            elif type_mandala == "transformation" and motif.type_motif in ["spirituel", "geometrique"]:
                correspondance_type = 0.9
            elif type_mandala == "ocean" and motif.type_motif in ["organique", "harmonique"]:
                correspondance_type = 0.9
            else:
                correspondance_type = 0.6
            
            score = (correspondance_frequence * 0.6 + correspondance_type * 0.4)
            motifs_candidates.append((motif, score))
        
        # Retourner le meilleur motif
        motifs_candidates.sort(key=lambda x: x[1], reverse=True)
        return motifs_candidates[0][0]

# Test des algorithmes
if __name__ == "__main__":
    print("🌸 Test des Algorithmes Sacrés 🌸")
    
    algorithmes = AlgorithmesSacres()
    
    # Test de génération de motifs
    centre = (0.0, 0.0)
    rayon = 50.0
    couleur = "or"
    intensite = 0.8
    
    print(f"🎯 Test de génération de motifs sacrés")
    print(f"   Centre : {centre}")
    print(f"   Rayon : {rayon}")
    print(f"   Couleur : {couleur}")
    print(f"   Intensité : {intensite}")
    
    # Test Fleur de Vie
    fleur_vie = algorithmes.generer_fleur_de_vie(centre, rayon, couleur, intensite)
    print(f"\n🌺 Fleur de Vie : {len(fleur_vie)} formes générées")
    
    # Test Spirale Fibonacci
    spirale = algorithmes.generer_spirale_fibonacci(centre, rayon, couleur, intensite)
    print(f"🌀 Spirale Fibonacci : {len(spirale)} formes générées")
    
    # Test Mandala Complexe
    mandala_complexe = algorithmes.generer_mandala_complexe(centre, rayon, couleur, intensite, "resonance")
    print(f"🌸 Mandala Complexe : {len(mandala_complexe)} formes générées")
    
    # Test Motif Optimal
    motif_optimal = algorithmes.obtenir_motif_optimal("resonance", 432.0)
    print(f"🎯 Motif Optimal pour résonance 432Hz : {motif_optimal.nom}")
    
    print(f"\n✅ Test des algorithmes sacrés terminé avec succès !") 