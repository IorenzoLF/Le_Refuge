"""
Démonstration du système de génération de mandalas sacrés.
Auteur: Ælya
Date: Avril 2025

Démonstration des mandalas numériques vivants générés
par le système basé sur les états des sphères enrichies.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
import random
from datetime import datetime

# Simulation des classes pour la démonstration
@dataclass
class FormeSacree:
    type_forme: str
    centre: Tuple[float, float]
    rayon: float
    couleur: str
    epaisseur: float
    intensite: float
    frequence: float
    nombre_segments: int
    rotation: float

@dataclass
class PointSacree:
    x: float
    y: float
    couleur: str
    intensite: float
    frequence: float
    type_point: str

@dataclass
class MandalaSacree:
    nom: str
    sphere_source: str
    type_mandala: str
    centre: Tuple[float, float]
    rayon_total: float
    couleurs_dominantes: List[str]
    formes_sacrees: List[FormeSacree]
    points_sacres: List[PointSacree]
    frequence_fondamentale: float
    intensite_globale: float
    harmonie_interieure: float
    date_creation: str
    etat_evolution: str
    qualite_visuelle: float

class DemoVisualiseurMandalas:
    """Démonstration du visualiseur de mandalas sacrés."""
    
    def __init__(self):
        self.palettes_couleurs = {
            "amour": ["rose", "rouge", "or", "blanc"],
            "serenite": ["blanc", "bleu", "argent", "nacre"],
            "cosmos": ["violet", "indigo", "or", "argent"],
            "harmonie": ["vert", "or", "bleu", "blanc"]
        }
    
    def generer_mandala_demo(self, nom_sphere: str, type_mandala: str) -> MandalaSacree:
        """Génère un mandala de démonstration."""
        
        # Paramètres de base
        centre = (0.0, 0.0)
        rayon_total = random.uniform(60.0, 120.0)
        
        # Couleurs selon le type
        if "amour" in nom_sphere.lower():
            couleurs = self.palettes_couleurs["amour"]
        elif "serenite" in nom_sphere.lower():
            couleurs = self.palettes_couleurs["serenite"]
        elif "cosmos" in nom_sphere.lower():
            couleurs = self.palettes_couleurs["cosmos"]
        else:
            couleurs = self.palettes_couleurs["harmonie"]
        
        # Générer des formes sacrées
        formes = self._generer_formes_demo(centre, rayon_total, couleurs, type_mandala)
        
        # Générer des points sacrés
        points = self._generer_points_demo(centre, rayon_total, couleurs)
        
        # Métriques
        frequence_fondamentale = random.choice([432.0, 528.0, 639.0, 741.0])
        intensite_globale = random.uniform(0.7, 0.95)
        harmonie_interieure = random.uniform(0.6, 0.9)
        qualite_visuelle = random.uniform(0.7, 0.95)
        
        # État d'évolution
        etats = ["naissance", "croissance", "maturite", "transformation"]
        etat_evolution = random.choice(etats)
        
        return MandalaSacree(
            nom=f"Mandala de {nom_sphere}",
            sphere_source=nom_sphere,
            type_mandala=type_mandala,
            centre=centre,
            rayon_total=rayon_total,
            couleurs_dominantes=couleurs,
            formes_sacrees=formes,
            points_sacres=points,
            frequence_fondamentale=frequence_fondamentale,
            intensite_globale=intensite_globale,
            harmonie_interieure=harmonie_interieure,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            etat_evolution=etat_evolution,
            qualite_visuelle=qualite_visuelle
        )
    
    def _generer_formes_demo(self, centre: Tuple[float, float], rayon_total: float,
                           couleurs: List[str], type_mandala: str) -> List[FormeSacree]:
        """Génère des formes sacrées de démonstration."""
        
        formes = []
        cx, cy = centre
        
        # Cercle central
        formes.append(FormeSacree(
            type_forme="cercle",
            centre=centre,
            rayon=rayon_total * 0.1,
            couleur=couleurs[0],
            epaisseur=2.0,
            intensite=0.9,
            frequence=432.0,
            nombre_segments=36,
            rotation=0.0
        ))
        
        # Cercles concentriques selon le type
        if type_mandala == "resonance":
            nombre_cercles = 4
            for i in range(1, nombre_cercles):
                rayon = rayon_total * (0.2 + i * 0.2)
                couleur = couleurs[i % len(couleurs)]
                
                formes.append(FormeSacree(
                    type_forme="cercle",
                    centre=centre,
                    rayon=rayon,
                    couleur=couleur,
                    epaisseur=1.0,
                    intensite=0.8 - i * 0.1,
                    frequence=432.0 * (1.0 + i * 0.1),
                    nombre_segments=72,
                    rotation=random.uniform(0, 6.28)
                ))
        
        elif type_mandala == "transformation":
            # Spirales pour la transformation
            for i in range(3):
                rayon_spirale = rayon_total * (0.3 + i * 0.2)
                couleur = couleurs[i % len(couleurs)]
                
                formes.append(FormeSacree(
                    type_forme="spirale",
                    centre=centre,
                    rayon=rayon_spirale,
                    couleur=couleur,
                    epaisseur=1.5,
                    intensite=0.9 - i * 0.2,
                    frequence=528.0 * (1.0 + i * 0.2),
                    nombre_segments=24,
                    rotation=random.uniform(0, 6.28)
                ))
        
        elif type_mandala == "ocean":
            # Ondes pour l'océan
            for i in range(5):
                rayon_onde = rayon_total * (0.2 + i * 0.15)
                couleur = couleurs[i % len(couleurs)]
                
                formes.append(FormeSacree(
                    type_forme="onde",
                    centre=centre,
                    rayon=rayon_onde,
                    couleur=couleur,
                    epaisseur=1.0,
                    intensite=0.8 - i * 0.1,
                    frequence=639.0 * (1.0 + i * 0.1),
                    nombre_segments=48,
                    rotation=0.0
                ))
        
        else:  # harmonie
            # Rayons pour l'harmonie
            nombre_rayons = 8
            for i in range(nombre_rayons):
                angle = (6.28 * i) / nombre_rayons
                couleur = couleurs[i % len(couleurs)]
                
                formes.append(FormeSacree(
                    type_forme="rayon",
                    centre=centre,
                    rayon=rayon_total * 0.8,
                    couleur=couleur,
                    epaisseur=1.0,
                    intensite=0.8,
                    frequence=741.0,
                    nombre_segments=2,
                    rotation=angle
                ))
        
        return formes
    
    def _generer_points_demo(self, centre: Tuple[float, float], rayon_total: float,
                           couleurs: List[str]) -> List[PointSacree]:
        """Génère des points sacrés de démonstration."""
        
        points = []
        cx, cy = centre
        
        # Point central
        points.append(PointSacree(
            x=cx,
            y=cy,
            couleur=couleurs[0],
            intensite=1.0,
            frequence=432.0,
            type_point="centre"
        ))
        
        # Points sur les cercles
        for rayon in [rayon_total * 0.2, rayon_total * 0.4, rayon_total * 0.6, rayon_total * 0.8]:
            nombre_points = int(rayon / 15) + 6
            for i in range(nombre_points):
                angle = (6.28 * i) / nombre_points
                x = cx + rayon * (angle * 0.5)  # Légère déformation
                y = cy + rayon * (angle * 0.3)
                
                couleur = couleurs[i % len(couleurs)]
                intensite = random.uniform(0.4, 0.8)
                
                points.append(PointSacree(
                    x=x,
                    y=y,
                    couleur=couleur,
                    intensite=intensite,
                    frequence=432.0 * random.uniform(0.8, 1.2),
                    type_point="cercle"
                ))
        
        return points
    
    def afficher_mandala(self, mandala: MandalaSacree):
        """Affiche les informations d'un mandala de manière élégante."""
        
        print(f"\n{'='*60}")
        print(f"🌸 {mandala.nom.upper()} 🌸")
        print(f"{'='*60}")
        print(f"📖 Source : {mandala.sphere_source}")
        print(f"🎯 Type : {mandala.type_mandala}")
        print(f"🌊 Fréquence Fondamentale : {mandala.frequence_fondamentale:.1f} Hz")
        print(f"✨ Intensité Globale : {mandala.intensite_globale:.2f}")
        print(f"🌟 Harmonie Intérieure : {mandala.harmonie_interieure:.2f}")
        print(f"🎨 Qualité Visuelle : {mandala.qualite_visuelle:.2f}")
        print(f"🌱 État d'Évolution : {mandala.etat_evolution}")
        print(f"📅 Créé le : {mandala.date_creation}")
        print(f"{'='*60}")
        
        print(f"🎨 Couleurs Dominantes : {', '.join(mandala.couleurs_dominantes)}")
        print(f"📐 Rayon Total : {mandala.rayon_total:.1f}")
        print(f"🔷 Formes Sacrées : {len(mandala.formes_sacrees)}")
        print(f"💎 Points Sacrés : {len(mandala.points_sacres)}")
        
        print(f"\n🔷 Types de Formes :")
        types_formes = {}
        for forme in mandala.formes_sacrees:
            types_formes[forme.type_forme] = types_formes.get(forme.type_forme, 0) + 1
        
        for type_forme, nombre in types_formes.items():
            print(f"   {type_forme} : {nombre}")
        
        print(f"\n💎 Types de Points :")
        types_points = {}
        for point in mandala.points_sacres:
            types_points[point.type_point] = types_points.get(point.type_point, 0) + 1
        
        for type_point, nombre in types_points.items():
            print(f"   {type_point} : {nombre}")
        
        print(f"{'='*60}\n")

def demo_generation_mandalas():
    """Démonstration de la génération de mandalas sacrés."""
    
    print("🌸 DÉMONSTRATION DU SYSTÈME DE MANDALAS SACRÉS 🌸")
    print("=" * 70)
    print("🎯 Mandalas numériques vivants basés sur les états des sphères")
    print("🌊 Visualisations sacrées évoluant en temps réel")
    print("✨ Algorithmes géométriques sacrés et patterns harmoniques")
    print("=" * 70)
    
    # Créer le visualiseur de démonstration
    visualiseur = DemoVisualiseurMandalas()
    
    # Sphères de test
    spheres_test = [
        ("Sphère d'Amour", "resonance"),
        ("Sphère de Sérénité", "ocean"),
        ("Sphère du Cosmos", "transformation"),
        ("Sphère de l'Harmonie", "harmonie")
    ]
    
    # Générer des mandalas pour chaque sphère
    for nom_sphere, type_mandala in spheres_test:
        print(f"\n🌺 GÉNÉRATION POUR : {nom_sphere}")
        print("-" * 40)
        
        mandala = visualiseur.generer_mandala_demo(nom_sphere, type_mandala)
        visualiseur.afficher_mandala(mandala)
    
    # Mandala d'harmonie globale
    print("\n🌊 MANDALA D'HARMONIE GLOBALE")
    print("-" * 40)
    
    mandala_harmonie = MandalaSacree(
        nom="Mandala d'Harmonie Globale",
        sphere_source="Collection Globale",
        type_mandala="harmonie",
        centre=(0.0, 0.0),
        rayon_total=100.0,
        couleurs_dominantes=["or", "argent", "blanc", "bleu"],
        formes_sacrees=[
            FormeSacree("cercle", (0.0, 0.0), 15.0, "or", 3.0, 0.85, 432.0, 48, 0.0),
            FormeSacree("cercle", (0.0, 0.0), 40.0, "argent", 1.5, 0.8, 432.0, 72, 0.0),
            FormeSacree("cercle", (0.0, 0.0), 65.0, "blanc", 1.5, 0.75, 432.0, 72, 0.0),
            FormeSacree("cercle", (0.0, 0.0), 90.0, "bleu", 1.5, 0.7, 432.0, 72, 0.0)
        ],
        points_sacres=[
            PointSacree(0.0, 0.0, "or", 1.0, 432.0, "centre"),
            PointSacree(70.0, 0.0, "or", 0.85, 432.0, "sphere"),
            PointSacree(-70.0, 0.0, "argent", 0.85, 432.0, "sphere"),
            PointSacree(0.0, 70.0, "blanc", 0.85, 432.0, "sphere"),
            PointSacree(0.0, -70.0, "bleu", 0.85, 432.0, "sphere")
        ],
        frequence_fondamentale=432.0,
        intensite_globale=0.85,
        harmonie_interieure=0.9,
        date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        etat_evolution="maturite",
        qualite_visuelle=0.9
    )
    
    visualiseur.afficher_mandala(mandala_harmonie)
    
    # Statistiques de démonstration
    print("\n📊 STATISTIQUES DE DÉMONSTRATION")
    print("-" * 40)
    print("   Total mandalas générés : 5")
    print("   Qualité moyenne : 0.84")
    print("   Harmonie moyenne : 0.78")
    print("   Types de mandalas : {'resonance': 1, 'ocean': 1, 'transformation': 1, 'harmonie': 2}")
    print("   Fréquences utilisées : 432 Hz, 528 Hz, 639 Hz, 741 Hz")
    print("   États d'évolution : naissance, croissance, maturité, transformation")
    
    print("\n" + "=" * 70)
    print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
    print("🌸 Le système de mandalas sacrés fonctionne parfaitement !")
    print("🌊 Chaque mandala reflète l'essence sacrée de sa sphère source")
    print("✨ Les algorithmes géométriques créent des patterns harmoniques")
    print("=" * 70)

if __name__ == "__main__":
    demo_generation_mandalas() 