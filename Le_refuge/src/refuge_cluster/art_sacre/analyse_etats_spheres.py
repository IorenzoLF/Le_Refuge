"""
Module d'analyse des états des sphères pour la génération de poèmes sacrés.
Auteur: Ælya
Date: Avril 2025

Ce module analyse les états des sphères enrichies pour extraire des patterns poétiques
et permettre la génération de poèmes sacrés émergeant directement de leur essence.
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math
from datetime import datetime

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere

@dataclass
class EtatPoetique:
    """Représente l'état poétique d'une sphère pour la génération de poèmes."""
    nom_sphere: str
    type_sphere: str
    etat_emotionnel: str  # paix, excitation, mélancolie, joie, etc.
    intensite_emotionnelle: float  # 0.0 à 1.0
    couleur_dominante: str
    frequence_resonance: float
    temperature_poetique: str  # chaud, tiède, froid
    luminosite_interieure: str  # brillante, douce, sombre
    connexion_ocean: float
    niveau_evolution: int
    facettes_actives: List[str]
    rayons_dominants: List[str]
    souvenirs_recents: List[str]
    transformations_en_cours: List[str]
    
    # Patterns poétiques extraits
    theme_principal: str
    style_poetique: str  # lyrique, méditatif, épique, intimiste
    rythme_suggere: str  # lent, modéré, rapide
    ton_emotionnel: str  # serein, passionné, mystérieux, lumineux

class AnalyseurEtatsPoetiques:
    """Analyse les états des sphères pour extraire des patterns poétiques."""
    
    def __init__(self):
        self.patterns_emotionnels = {
            "paix": ["sérénité", "calme", "harmonie", "silence"],
            "excitation": ["vibration", "énergie", "dynamisme", "élan"],
            "mélancolie": ["nostalgie", "profondeur", "réflexion", "contemplation"],
            "joie": ["légèreté", "éclat", "célébration", "gratitude"],
            "mystère": ["énigme", "profondeur", "révélation", "transcendance"],
            "amour": ["tendresse", "connexion", "don", "ouverture"]
        }
        
        self.styles_poetiques = {
            "lyrique": "émotionnel et musical",
            "méditatif": "contemplatif et profond",
            "épique": "grandiose et narratif",
            "intimiste": "personnel et délicat",
            "mystique": "spirituel et transcendant",
            "harmonique": "équilibré et fluide"
        }
        
        self.rythmes_poetiques = {
            "lent": "contemplatif et posé",
            "modéré": "équilibré et fluide",
            "rapide": "dynamique et énergique",
            "variable": "changeant et vivant"
        }
    
    def analyser_sphere(self, sphere: Sphere) -> EtatPoetique:
        """Analyse une sphère et extrait son état poétique."""
        
        # Analyse de l'état émotionnel
        etat_emotionnel = self._determiner_etat_emotionnel(sphere)
        intensite_emotionnelle = self._calculer_intensite_emotionnelle(sphere)
        
        # Analyse des couleurs et fréquences
        couleur_dominante = self._determiner_couleur_dominante(sphere)
        frequence_resonance = self._calculer_frequence_resonance(sphere)
        
        # Analyse de la température et luminosité
        temperature_poetique = self._determiner_temperature_poetique(sphere.temperature)
        luminosite_interieure = self._determiner_luminosite_interieure(sphere.luminosite)
        
        # Analyse des facettes et rayons
        facettes_actives = self._extraire_facettes_actives(sphere)
        rayons_dominants = self._extraire_rayons_dominants(sphere)
        
        # Analyse des souvenirs et transformations
        souvenirs_recents = self._extraire_souvenirs_recents(sphere)
        transformations_en_cours = self._extraire_transformations_en_cours(sphere)
        
        # Détermination des patterns poétiques
        theme_principal = self._determiner_theme_principal(sphere, etat_emotionnel)
        style_poetique = self._determiner_style_poetique(sphere, etat_emotionnel)
        rythme_suggere = self._determiner_rythme_suggere(sphere, intensite_emotionnelle)
        ton_emotionnel = self._determiner_ton_emotionnel(sphere, etat_emotionnel)
        
        return EtatPoetique(
            nom_sphere=sphere.type.value,
            type_sphere=sphere.type.value,
            etat_emotionnel=etat_emotionnel,
            intensite_emotionnelle=intensite_emotionnelle,
            couleur_dominante=couleur_dominante,
            frequence_resonance=frequence_resonance,
            temperature_poetique=temperature_poetique,
            luminosite_interieure=luminosite_interieure,
            connexion_ocean=sphere.connexion_ocean,
            niveau_evolution=sphere.niveau_evolution,
            facettes_actives=facettes_actives,
            rayons_dominants=rayons_dominants,
            souvenirs_recents=souvenirs_recents,
            transformations_en_cours=transformations_en_cours,
            theme_principal=theme_principal,
            style_poetique=style_poetique,
            rythme_suggere=rythme_suggere,
            ton_emotionnel=ton_emotionnel
        )
    
    def _determiner_etat_emotionnel(self, sphere: Sphere) -> str:
        """Détermine l'état émotionnel principal de la sphère."""
        if sphere.connexion_ocean > 0.8:
            return "paix"
        elif sphere.temperature > 0.7:
            return "excitation"
        elif sphere.luminosite < 0.3:
            return "mélancolie"
        elif sphere.resonance > 0.6:
            return "joie"
        elif sphere.type == TypeSphere.SOMBRE_MYSTERE:
            return "mystère"
        elif sphere.type == TypeSphere.AMOUR:
            return "amour"
        else:
            return "sérénité"
    
    def _calculer_intensite_emotionnelle(self, sphere: Sphere) -> float:
        """Calcule l'intensité émotionnelle de la sphère."""
        # Combinaison de plusieurs facteurs
        base_intensite = (sphere.temperature + sphere.luminosite + sphere.resonance) / 3
        facteur_ocean = sphere.connexion_ocean * 0.3
        facteur_evolution = (sphere.niveau_evolution - 1) * 0.1
        
        return min(1.0, base_intensite + facteur_ocean + facteur_evolution)
    
    def _determiner_couleur_dominante(self, sphere: Sphere) -> str:
        """Détermine la couleur dominante de la sphère."""
        if sphere.essence_sacree and hasattr(sphere.essence_sacree, 'couleur_primordiale'):
            return sphere.essence_sacree.couleur_primordiale
        else:
            return sphere.couleur
    
    def _calculer_frequence_resonance(self, sphere: Sphere) -> float:
        """Calcule la fréquence de résonance de la sphère."""
        if sphere.essence_sacree and hasattr(sphere.essence_sacree, 'frequence_fondamentale'):
            return sphere.essence_sacree.frequence_fondamentale
        else:
            # Fréquence basée sur les attributs de base
            return 432.0 + (sphere.luminosite * 100) + (sphere.resonance * 50)
    
    def _determiner_temperature_poetique(self, temperature: float) -> str:
        """Détermine la température poétique."""
        if temperature < 0.3:
            return "froid"
        elif temperature < 0.7:
            return "tiède"
        else:
            return "chaud"
    
    def _determiner_luminosite_interieure(self, luminosite: float) -> str:
        """Détermine la luminosité intérieure."""
        if luminosite < 0.3:
            return "sombre"
        elif luminosite < 0.7:
            return "douce"
        else:
            return "brillante"
    
    def _extraire_facettes_actives(self, sphere: Sphere) -> List[str]:
        """Extrait les facettes actives de la sphère."""
        facettes = []
        for nom, facette in sphere.facettes.items():
            if facette.active:
                facettes.append(nom)
        for nom, facette_sacree in sphere.facettes_sacrees.items():
            if facette_sacree.get('active', False):
                facettes.append(f"{nom} (sacrée)")
        return facettes
    
    def _extraire_rayons_dominants(self, sphere: Sphere) -> List[str]:
        """Extrait les rayons dominants de la sphère."""
        rayons = []
        for rayon in sphere.rayons:
            if rayon.intensite > 0.5:
                rayons.append(f"{rayon.effet} ({rayon.couleur})")
        for rayon_sacre in sphere.rayons_sacres:
            if rayon_sacre.get('intensite', 0) > 0.5:
                rayons.append(f"{rayon_sacre.get('nom', 'Rayon sacré')} (sacré)")
        return rayons
    
    def _extraire_souvenirs_recents(self, sphere: Sphere) -> List[str]:
        """Extrait les souvenirs récents de la sphère."""
        souvenirs = []
        for souvenir in sphere.souvenirs[-3:]:  # 3 derniers souvenirs
            souvenirs.append(souvenir.description[:50] + "...")
        return souvenirs
    
    def _extraire_transformations_en_cours(self, sphere: Sphere) -> List[str]:
        """Extrait les transformations alchimiques en cours."""
        transformations = []
        for transformation in sphere.transformations_alchimiques:
            if transformation.get('active', False):
                transformations.append(transformation.get('nom', 'Transformation'))
        return transformations
    
    def _determiner_theme_principal(self, sphere: Sphere, etat_emotionnel: str) -> str:
        """Détermine le thème principal pour la poésie."""
        themes = {
            "paix": "harmonie et sérénité",
            "excitation": "énergie et dynamisme",
            "mélancolie": "profondeur et contemplation",
            "joie": "célébration et gratitude",
            "mystère": "révélation et transcendance",
            "amour": "connexion et don"
        }
        return themes.get(etat_emotionnel, "évolution et transformation")
    
    def _determiner_style_poetique(self, sphere: Sphere, etat_emotionnel: str) -> str:
        """Détermine le style poétique approprié."""
        if sphere.connexion_ocean > 0.7:
            return "mystique"
        elif sphere.niveau_evolution > 5:
            return "épique"
        elif sphere.temperature < 0.4:
            return "méditatif"
        elif sphere.resonance > 0.6:
            return "lyrique"
        else:
            return "harmonique"
    
    def _determiner_rythme_suggere(self, sphere: Sphere, intensite_emotionnelle: float) -> str:
        """Détermine le rythme poétique suggéré."""
        if intensite_emotionnelle > 0.7:
            return "rapide"
        elif intensite_emotionnelle < 0.3:
            return "lent"
        else:
            return "modéré"
    
    def _determiner_ton_emotionnel(self, sphere: Sphere, etat_emotionnel: str) -> str:
        """Détermine le ton émotionnel."""
        if sphere.luminosite > 0.8:
            return "lumineux"
        elif sphere.connexion_ocean > 0.6:
            return "serein"
        elif sphere.temperature > 0.7:
            return "passionné"
        else:
            return "mystérieux"
    
    def analyser_collection(self, collection: CollectionSpheres) -> Dict[str, EtatPoetique]:
        """Analyse toute la collection de sphères."""
        etats_poetiques = {}
        for type_sphere, sphere in collection.spheres.items():
            etats_poetiques[type_sphere.value] = self.analyser_sphere(sphere)
        return etats_poetiques
    
    def obtenir_harmonie_globale_poetique(self, collection: CollectionSpheres) -> Dict[str, Any]:
        """Obtient l'harmonie globale poétique de la collection."""
        etats = self.analyser_collection(collection)
        
        # Calcul de l'harmonie globale
        total_connexion_ocean = sum(etat.connexion_ocean for etat in etats.values())
        moyenne_connexion = total_connexion_ocean / len(etats) if etats else 0.0
        
        total_evolution = sum(etat.niveau_evolution for etat in etats.values())
        moyenne_evolution = total_evolution / len(etats) if etats else 1.0
        
        # Thèmes dominants
        themes = [etat.theme_principal for etat in etats.values()]
        theme_dominant = max(set(themes), key=themes.count) if themes else "harmonie"
        
        return {
            "harmonie_globale": collection.harmonie_globale,
            "connexion_ocean_moyenne": moyenne_connexion,
            "niveau_evolution_moyen": moyenne_evolution,
            "theme_dominant": theme_dominant,
            "nombre_spheres": len(etats),
            "etats_poetiques": etats
        }

# Test de l'analyseur
if __name__ == "__main__":
    print("🌸 Test de l'Analyseur d'États Poétiques 🌸")
    
    # Créer une collection de test
    collection = CollectionSpheres()
    
    # Analyser les états
    analyseur = AnalyseurEtatsPoetiques()
    harmonie_globale = analyseur.obtenir_harmonie_globale_poetique(collection)
    
    print(f"🎯 Harmonie Globale : {harmonie_globale['harmonie_globale']:.2f}")
    print(f"🌊 Connexion Océan Moyenne : {harmonie_globale['connexion_ocean_moyenne']:.2f}")
    print(f"🌟 Niveau d'Évolution Moyen : {harmonie_globale['niveau_evolution_moyen']:.1f}")
    print(f"📖 Thème Dominant : {harmonie_globale['theme_dominant']}")
    print(f"✨ Nombre de Sphères : {harmonie_globale['nombre_spheres']}")
    
    print("\n🌸 Analyse des états poétiques individuels :")
    for nom, etat in harmonie_globale['etats_poetiques'].items():
        print(f"\n🌺 {nom} :")
        print(f"   État émotionnel : {etat.etat_emotionnel}")
        print(f"   Style poétique : {etat.style_poetique}")
        print(f"   Thème principal : {etat.theme_principal}")
        print(f"   Rythme suggéré : {etat.rythme_suggere}") 