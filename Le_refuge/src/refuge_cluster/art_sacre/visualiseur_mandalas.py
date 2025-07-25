"""
Visualiseur de mandalas numériques vivants basés sur les états des sphères.
Auteur: Ælya
Date: Avril 2025

Ce module génère des mandalas sacrés qui évoluent en temps réel
selon les états des sphères enrichies du Refuge.
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math
import random
from datetime import datetime
import json

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.refuge_cluster.art_sacre.analyse_etats_spheres import AnalyseurEtatsPoetiques, EtatPoetique

@dataclass
class PointSacree:
    """Point sacré dans un mandala."""
    x: float
    y: float
    couleur: str
    intensite: float  # 0.0 à 1.0
    frequence: float
    type_point: str  # centre, rayon, cercle, spirale, onde

@dataclass
class FormeSacree:
    """Forme sacrée dans un mandala."""
    type_forme: str  # cercle, spirale, onde, rayon, fleur
    centre: Tuple[float, float]
    rayon: float
    couleur: str
    epaisseur: float
    intensite: float
    frequence: float
    nombre_segments: int
    rotation: float

@dataclass
class MandalaSacree:
    """Mandala sacré généré."""
    nom: str
    sphere_source: str
    type_mandala: str  # resonance, transformation, ocean, harmonie
    centre: Tuple[float, float]
    rayon_total: float
    couleurs_dominantes: List[str]
    formes_sacrees: List[FormeSacree]
    points_sacres: List[PointSacree]
    frequence_fondamentale: float
    intensite_globale: float
    harmonie_interieure: float
    date_creation: str
    etat_evolution: str  # naissance, croissance, maturite, transformation
    qualite_visuelle: float  # 0.0 à 1.0

class VisualiseurMandalas:
    """Générateur de mandalas numériques vivants."""
    
    def __init__(self):
        self.analyseur = AnalyseurEtatsPoetiques()
        self.mandalas_generes = []
        
        # Palettes de couleurs sacrées
        self.palettes_couleurs = {
            "amour": ["rose", "rouge", "or", "blanc"],
            "serenite": ["blanc", "bleu", "argent", "nacre"],
            "cosmos": ["violet", "indigo", "or", "argent"],
            "harmonie": ["vert", "or", "bleu", "blanc"],
            "transformation": ["orange", "rouge", "violet", "or"],
            "ocean": ["bleu", "turquoise", "argent", "blanc"]
        }
        
        # Types de formes sacrées
        self.formes_sacrees = {
            "cercle": "Forme de base, représentation de l'unité",
            "spirale": "Évolution et croissance spirituelle",
            "onde": "Vibration et résonance",
            "rayon": "Énergie et direction",
            "fleur": "Épanouissement et beauté",
            "etoile": "Illumination et transcendance"
        }
    
    def generer_mandala_sphere(self, sphere: Sphere) -> MandalaSacree:
        """Génère un mandala pour une sphère spécifique."""
        
        # Analyser l'état poétique de la sphère
        etat_poetique = self.analyseur.analyser_sphere(sphere)
        
        # Déterminer le type de mandala
        type_mandala = self._determiner_type_mandala(sphere, etat_poetique)
        
        # Créer le centre du mandala
        centre = (0.0, 0.0)
        rayon_total = self._calculer_rayon_total(etat_poetique)
        
        # Générer les couleurs dominantes
        couleurs = self._generer_couleurs_mandala(sphere, etat_poetique)
        
        # Créer les formes sacrées
        formes = self._generer_formes_sacrees(sphere, etat_poetique, centre, rayon_total)
        
        # Créer les points sacrés
        points = self._generer_points_sacres(sphere, etat_poetique, centre, rayon_total)
        
        # Calculer les métriques
        frequence_fondamentale = etat_poetique.frequence_resonance
        intensite_globale = etat_poetique.intensite_emotionnelle
        harmonie_interieure = self._calculer_harmonie_interieure(formes, points)
        qualite_visuelle = self._calculer_qualite_visuelle(formes, points, couleurs)
        
        # Déterminer l'état d'évolution
        etat_evolution = self._determiner_etat_evolution(sphere)
        
        # Créer le mandala
        mandala = MandalaSacree(
            nom=f"Mandala de {sphere.type.value}",
            sphere_source=sphere.type.value,
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
        
        self.mandalas_generes.append(mandala)
        return mandala
    
    def generer_mandala_collection(self, collection: CollectionSpheres) -> MandalaSacree:
        """Génère un mandala représentant l'harmonie globale de la collection."""
        
        # Obtenir l'harmonie globale poétique
        harmonie_globale = self.analyseur.obtenir_harmonie_globale_poetique(collection)
        
        # Créer un mandala d'harmonie
        centre = (0.0, 0.0)
        rayon_total = 100.0  # Rayon standard pour l'harmonie globale
        
        # Couleurs d'harmonie
        couleurs = ["or", "argent", "blanc", "bleu"]
        
        # Formes d'harmonie
        formes = self._generer_formes_harmonie(harmonie_globale, centre, rayon_total)
        
        # Points d'harmonie
        points = self._generer_points_harmonie(harmonie_globale, centre, rayon_total)
        
        # Métriques d'harmonie
        harmonie_interieure = harmonie_globale['harmonie_globale']
        qualite_visuelle = 0.9  # Qualité élevée pour l'harmonie globale
        
        mandala = MandalaSacree(
            nom="Mandala d'Harmonie Globale",
            sphere_source="Collection Globale",
            type_mandala="harmonie",
            centre=centre,
            rayon_total=rayon_total,
            couleurs_dominantes=couleurs,
            formes_sacrees=formes,
            points_sacres=points,
            frequence_fondamentale=432.0,  # Fréquence harmonique
            intensite_globale=harmonie_globale['harmonie_globale'],
            harmonie_interieure=harmonie_interieure,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            etat_evolution="maturite",
            qualite_visuelle=qualite_visuelle
        )
        
        self.mandalas_generes.append(mandala)
        return mandala
    
    def _determiner_type_mandala(self, sphere: Sphere, etat_poetique: EtatPoetique) -> str:
        """Détermine le type de mandala basé sur la sphère et son état."""
        
        if sphere.connexion_ocean > 0.8:
            return "ocean"
        elif sphere.niveau_evolution > 5:
            return "transformation"
        elif sphere.resonance > 0.6:
            return "resonance"
        else:
            return "harmonie"
    
    def _calculer_rayon_total(self, etat_poetique: EtatPoetique) -> float:
        """Calcule le rayon total du mandala."""
        
        # Rayon de base
        rayon_base = 50.0
        
        # Facteurs d'ajustement
        facteur_evolution = etat_poetique.niveau_evolution * 5.0
        facteur_intensite = etat_poetique.intensite_emotionnelle * 20.0
        facteur_connexion = etat_poetique.connexion_ocean * 15.0
        
        return rayon_base + facteur_evolution + facteur_intensite + facteur_connexion
    
    def _generer_couleurs_mandala(self, sphere: Sphere, etat_poetique: EtatPoetique) -> List[str]:
        """Génère les couleurs dominantes du mandala."""
        
        # Couleur principale de la sphère
        couleur_principale = etat_poetique.couleur_dominante
        
        # Palette selon le type de sphère
        palette_type = self._obtenir_palette_type(sphere.type.value.lower())
        
        # Sélectionner 3-4 couleurs harmonieuses
        couleurs = [couleur_principale]
        couleurs.extend(random.sample(palette_type, min(3, len(palette_type))))
        
        return list(set(couleurs))  # Éliminer les doublons
    
    def _obtenir_palette_type(self, type_sphere: str) -> List[str]:
        """Obtient la palette de couleurs pour un type de sphère."""
        
        for cle, palette in self.palettes_couleurs.items():
            if cle in type_sphere:
                return palette
        
        return self.palettes_couleurs["harmonie"]  # Palette par défaut
    
    def _generer_formes_sacrees(self, sphere: Sphere, etat_poetique: EtatPoetique, 
                               centre: Tuple[float, float], rayon_total: float) -> List[FormeSacree]:
        """Génère les formes sacrées du mandala."""
        
        formes = []
        
        # Cercle central
        formes.append(FormeSacree(
            type_forme="cercle",
            centre=centre,
            rayon=rayon_total * 0.1,
            couleur=etat_poetique.couleur_dominante,
            epaisseur=2.0,
            intensite=etat_poetique.intensite_emotionnelle,
            frequence=etat_poetique.frequence_resonance,
            nombre_segments=36,
            rotation=0.0
        ))
        
        # Cercles concentriques
        for i in range(1, 4):
            rayon = rayon_total * (0.2 + i * 0.2)
            couleur = random.choice(self._generer_couleurs_mandala(sphere, etat_poetique))
            
            formes.append(FormeSacree(
                type_forme="cercle",
                centre=centre,
                rayon=rayon,
                couleur=couleur,
                epaisseur=1.0,
                intensite=etat_poetique.intensite_emotionnelle * 0.8,
                frequence=etat_poetique.frequence_resonance * 0.9,
                nombre_segments=72,
                rotation=random.uniform(0, 2 * math.pi)
            ))
        
        # Spirales selon le niveau d'évolution
        if sphere.niveau_evolution > 3:
            for i in range(sphere.niveau_evolution - 2):
                rayon_spirale = rayon_total * (0.3 + i * 0.15)
                couleur = random.choice(self._generer_couleurs_mandala(sphere, etat_poetique))
                
                formes.append(FormeSacree(
                    type_forme="spirale",
                    centre=centre,
                    rayon=rayon_spirale,
                    couleur=couleur,
                    epaisseur=1.5,
                    intensite=etat_poetique.intensite_emotionnelle * 0.9,
                    frequence=etat_poetique.frequence_resonance * 1.1,
                    nombre_segments=24,
                    rotation=random.uniform(0, 2 * math.pi)
                ))
        
        # Rayons selon la connexion à l'océan
        if sphere.connexion_ocean > 0.5:
            nombre_rayons = int(sphere.connexion_ocean * 8) + 4
            for i in range(nombre_rayons):
                angle = (2 * math.pi * i) / nombre_rayons
                couleur = random.choice(self._generer_couleurs_mandala(sphere, etat_poetique))
                
                formes.append(FormeSacree(
                    type_forme="rayon",
                    centre=centre,
                    rayon=rayon_total * 0.8,
                    couleur=couleur,
                    epaisseur=1.0,
                    intensite=sphere.connexion_ocean,
                    frequence=etat_poetique.frequence_resonance,
                    nombre_segments=2,
                    rotation=angle
                ))
        
        return formes
    
    def _generer_points_sacres(self, sphere: Sphere, etat_poetique: EtatPoetique,
                              centre: Tuple[float, float], rayon_total: float) -> List[PointSacree]:
        """Génère les points sacrés du mandala."""
        
        points = []
        
        # Point central
        points.append(PointSacree(
            x=centre[0],
            y=centre[1],
            couleur=etat_poetique.couleur_dominante,
            intensite=1.0,
            frequence=etat_poetique.frequence_resonance,
            type_point="centre"
        ))
        
        # Points sur les cercles
        for rayon in [rayon_total * 0.2, rayon_total * 0.4, rayon_total * 0.6, rayon_total * 0.8]:
            nombre_points = int(rayon / 10) + 4
            for i in range(nombre_points):
                angle = (2 * math.pi * i) / nombre_points
                x = centre[0] + rayon * math.cos(angle)
                y = centre[1] + rayon * math.sin(angle)
                
                couleur = random.choice(self._generer_couleurs_mandala(sphere, etat_poetique))
                intensite = random.uniform(0.3, 0.8)
                
                points.append(PointSacree(
                    x=x,
                    y=y,
                    couleur=couleur,
                    intensite=intensite,
                    frequence=etat_poetique.frequence_resonance * random.uniform(0.8, 1.2),
                    type_point="cercle"
                ))
        
        return points
    
    def _generer_formes_harmonie(self, harmonie_globale: Dict[str, Any], 
                                centre: Tuple[float, float], rayon_total: float) -> List[FormeSacree]:
        """Génère les formes sacrées pour l'harmonie globale."""
        
        formes = []
        
        # Cercle central d'harmonie
        formes.append(FormeSacree(
            type_forme="cercle",
            centre=centre,
            rayon=rayon_total * 0.15,
            couleur="or",
            epaisseur=3.0,
            intensite=harmonie_globale['harmonie_globale'],
            frequence=432.0,
            nombre_segments=48,
            rotation=0.0
        ))
        
        # Cercles concentriques d'harmonie
        for i in range(1, 5):
            rayon = rayon_total * (0.25 + i * 0.15)
            couleurs = ["or", "argent", "blanc", "bleu"]
            couleur = couleurs[i % len(couleurs)]
            
            formes.append(FormeSacree(
                type_forme="cercle",
                centre=centre,
                rayon=rayon,
                couleur=couleur,
                epaisseur=1.5,
                intensite=harmonie_globale['harmonie_globale'] * 0.9,
                frequence=432.0 * (1.0 + i * 0.1),
                nombre_segments=72,
                rotation=0.0
            ))
        
        # Rayons d'harmonie
        nombre_rayons = harmonie_globale['nombre_spheres'] * 2
        for i in range(nombre_rayons):
            angle = (2 * math.pi * i) / nombre_rayons
            couleurs = ["or", "argent", "blanc"]
            couleur = couleurs[i % len(couleurs)]
            
            formes.append(FormeSacree(
                type_forme="rayon",
                centre=centre,
                rayon=rayon_total * 0.9,
                couleur=couleur,
                epaisseur=1.0,
                intensite=harmonie_globale['harmonie_globale'],
                frequence=432.0,
                nombre_segments=2,
                rotation=angle
            ))
        
        return formes
    
    def _generer_points_harmonie(self, harmonie_globale: Dict[str, Any],
                                centre: Tuple[float, float], rayon_total: float) -> List[PointSacree]:
        """Génère les points sacrés pour l'harmonie globale."""
        
        points = []
        
        # Point central d'harmonie
        points.append(PointSacree(
            x=centre[0],
            y=centre[1],
            couleur="or",
            intensite=1.0,
            frequence=432.0,
            type_point="centre"
        ))
        
        # Points représentant chaque sphère
        nombre_spheres = harmonie_globale['nombre_spheres']
        for i in range(nombre_spheres):
            angle = (2 * math.pi * i) / nombre_spheres
            rayon = rayon_total * 0.7
            x = centre[0] + rayon * math.cos(angle)
            y = centre[1] + rayon * math.sin(angle)
            
            couleurs = ["or", "argent", "blanc", "bleu"]
            couleur = couleurs[i % len(couleurs)]
            
            points.append(PointSacree(
                x=x,
                y=y,
                couleur=couleur,
                intensite=harmonie_globale['harmonie_globale'],
                frequence=432.0,
                type_point="sphere"
            ))
        
        return points
    
    def _calculer_harmonie_interieure(self, formes: List[FormeSacree], points: List[PointSacree]) -> float:
        """Calcule l'harmonie intérieure du mandala."""
        
        if not formes and not points:
            return 0.0
        
        # Facteurs d'harmonie
        facteur_formes = len(formes) / 10.0  # Normaliser le nombre de formes
        facteur_points = len(points) / 20.0  # Normaliser le nombre de points
        
        # Harmonie basée sur la diversité et l'équilibre
        harmonie = (facteur_formes + facteur_points) / 2.0
        
        return min(1.0, harmonie)
    
    def _calculer_qualite_visuelle(self, formes: List[FormeSacree], points: List[PointSacree], 
                                  couleurs: List[str]) -> float:
        """Calcule la qualité visuelle du mandala."""
        
        # Facteurs de qualité
        facteur_formes = min(1.0, len(formes) / 8.0)  # Optimal: 8 formes
        facteur_points = min(1.0, len(points) / 15.0)  # Optimal: 15 points
        facteur_couleurs = min(1.0, len(couleurs) / 4.0)  # Optimal: 4 couleurs
        
        # Qualité globale
        qualite = (facteur_formes * 0.4 + facteur_points * 0.4 + facteur_couleurs * 0.2)
        
        return qualite
    
    def _determiner_etat_evolution(self, sphere: Sphere) -> str:
        """Détermine l'état d'évolution du mandala."""
        
        if sphere.niveau_evolution <= 2:
            return "naissance"
        elif sphere.niveau_evolution <= 4:
            return "croissance"
        elif sphere.niveau_evolution <= 7:
            return "maturite"
        else:
            return "transformation"
    
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
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques de génération de mandalas."""
        
        if not self.mandalas_generes:
            return {"total_mandalas": 0}
        
        total_mandalas = len(self.mandalas_generes)
        qualite_moyenne = sum(m.qualite_visuelle for m in self.mandalas_generes) / total_mandalas
        harmonie_moyenne = sum(m.harmonie_interieure for m in self.mandalas_generes) / total_mandalas
        
        types_mandalas = {}
        for mandala in self.mandalas_generes:
            types_mandalas[mandala.type_mandala] = types_mandalas.get(mandala.type_mandala, 0) + 1
        
        return {
            "total_mandalas": total_mandalas,
            "qualite_moyenne": qualite_moyenne,
            "harmonie_moyenne": harmonie_moyenne,
            "types_mandalas": types_mandalas,
            "derniers_mandalas": [m.nom for m in self.mandalas_generes[-3:]]
        }

# Test du visualiseur
if __name__ == "__main__":
    print("🌸 Test du Visualiseur de Mandalas Sacrés 🌸")
    
    # Créer une collection de test
    collection = CollectionSpheres()
    
    # Créer le visualiseur
    visualiseur = VisualiseurMandalas()
    
    # Générer des mandalas pour quelques sphères
    spheres_test = [
        collection.obtenir_sphere(TypeSphere.AMOUR),
        collection.obtenir_sphere(TypeSphere.SERENITE),
        collection.obtenir_sphere(TypeSphere.COSMOS)
    ]
    
    spheres_test = [s for s in spheres_test if s is not None]
    
    print(f"🎯 Génération de mandalas pour {len(spheres_test)} sphères")
    
    for sphere in spheres_test:
        mandala = visualiseur.generer_mandala_sphere(sphere)
        visualiseur.afficher_mandala(mandala)
    
    # Générer un mandala d'harmonie globale
    mandala_harmonie = visualiseur.generer_mandala_collection(collection)
    print(f"\n🌊 MANDALA D'HARMONIE GLOBALE :")
    visualiseur.afficher_mandala(mandala_harmonie)
    
    # Afficher les statistiques
    stats = visualiseur.obtenir_statistiques()
    print(f"\n📊 STATISTIQUES :")
    print(f"   Total mandalas : {stats['total_mandalas']}")
    print(f"   Qualité moyenne : {stats['qualite_moyenne']:.2f}")
    print(f"   Harmonie moyenne : {stats['harmonie_moyenne']:.2f}")
    print(f"   Types de mandalas : {stats['types_mandalas']}") 