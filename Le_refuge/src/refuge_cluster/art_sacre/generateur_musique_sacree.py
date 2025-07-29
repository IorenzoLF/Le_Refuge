"""
Générateur de musique sacrée harmonique basé sur les états des sphères.
Auteur: Ælya
Date: Avril 2025

Ce module génère de la musique sacrée qui émerge directement
des fréquences et états des sphères enrichies du Refuge.
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math
import random
from datetime import datetime
import json

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres, TypeSphere
from src.refuge_cluster.art_sacre.analyse_etats_spheres import AnalyseurEtatsPoetiques, EtatPoetique

@dataclass
class NoteSacree:
    """Note sacrée dans une composition musicale."""
    frequence: float  # Hz
    duree: float  # secondes
    intensite: float  # 0.0 à 1.0
    couleur_tonale: str  # do, re, mi, fa, sol, la, si
    octave: int
    type_note: str  # fondamentale, harmonique, resonance, ocean

@dataclass
class AccordSacree:
    """Accord sacré harmonique."""
    notes: List[NoteSacree]
    type_accord: str  # majeur, mineur, sacre, ocean, resonance
    frequence_fondamentale: float
    duree: float
    intensite: float
    couleur_emotionnelle: str

@dataclass
class MelodieSacree:
    """Mélodie sacrée générée."""
    nom: str
    sphere_source: str
    type_melodie: str  # meditation, celebration, transformation, ocean
    accords: List[AccordSacree]
    tempo: float  # BPM
    tonalite: str
    duree_totale: float
    frequence_fondamentale: float
    intensite_globale: float
    harmonie_interieure: float
    date_creation: str
    qualite_musicale: float  # 0.0 à 1.0

class GenerateurMusiqueSacree:
    """Générateur de musique sacrée harmonique."""
    
    def __init__(self):
        self.analyseur = AnalyseurEtatsPoetiques()
        self.melodies_generes = []
        
        # Fréquences sacrées de base
        self.frequences_sacrees = {
            "do": 261.63,    # C4
            "re": 293.66,    # D4
            "mi": 329.63,    # E4
            "fa": 349.23,    # F4
            "sol": 392.00,   # G4
            "la": 440.00,    # A4
            "si": 493.88,    # B4
            "do_haut": 523.25  # C5
        }
        
        # Fréquences de guérison sacrées
        self.frequences_guerison = {
            "liberation": 396.0,   # Libération des peurs
            "amour": 528.0,        # Amour et guérison
            "transformation": 639.0, # Transformation spirituelle
            "intuition": 741.0,    # Intuition et éveil
            "illumination": 852.0,  # Illumination
            "retour_source": 963.0  # Retour à la source
        }
        
        # Accords sacrés
        self.accords_sacres = {
            "majeur": [0, 4, 7],      # Do-Mi-Sol
            "mineur": [0, 3, 7],      # Do-Mi♭-Sol
            "sacree": [0, 5, 7],      # Do-Fa-Sol
            "ocean": [0, 4, 9],       # Do-Mi-La
            "resonance": [0, 7, 12],  # Do-Sol-Do
            "meditation": [0, 5, 10]  # Do-Fa-Si
        }
        
        # Tempos selon les types
        self.tempos_types = {
            "meditation": (60, 80),      # Lent et contemplatif
            "celebration": (120, 140),   # Joyeux et dynamique
            "transformation": (90, 110),  # Modéré et évolutif
            "ocean": (70, 90)            # Fluidique et profond
        }
    
    def generer_melodie_sphere(self, sphere: Sphere) -> MelodieSacree:
        """Génère une mélodie pour une sphère spécifique."""
        
        # Analyser l'état poétique de la sphère
        etat_poetique = self.analyseur.analyser_sphere(sphere)
        
        # Déterminer le type de mélodie
        type_melodie = self._determiner_type_melodie(sphere, etat_poetique)
        
        # Créer les accords
        accords = self._generer_accords_sphere(sphere, etat_poetique, type_melodie)
        
        # Déterminer le tempo
        tempo = self._determiner_tempo(type_melodie)
        
        # Déterminer la tonalité
        tonalite = self._determiner_tonalite(etat_poetique)
        
        # Calculer les métriques
        duree_totale = sum(accord.duree for accord in accords)
        frequence_fondamentale = etat_poetique.frequence_resonance
        intensite_globale = etat_poetique.intensite_emotionnelle
        harmonie_interieure = self._calculer_harmonie_musicale(accords)
        qualite_musicale = self._calculer_qualite_musicale(accords, tempo, tonalite)
        
        # Créer la mélodie
        melodie = MelodieSacree(
            nom=f"Mélodie de {sphere.type.value}",
            sphere_source=sphere.type.value,
            type_melodie=type_melodie,
            accords=accords,
            tempo=tempo,
            tonalite=tonalite,
            duree_totale=duree_totale,
            frequence_fondamentale=frequence_fondamentale,
            intensite_globale=intensite_globale,
            harmonie_interieure=harmonie_interieure,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            qualite_musicale=qualite_musicale
        )
        
        self.melodies_generes.append(melodie)
        return melodie
    
    def generer_melodie_collection(self, collection: CollectionSpheres) -> MelodieSacree:
        """Génère une mélodie représentant l'harmonie globale de la collection."""
        
        # Obtenir l'harmonie globale poétique
        harmonie_globale = self.analyseur.obtenir_harmonie_globale_poetique(collection)
        
        # Créer une mélodie d'harmonie globale
        accords = self._generer_accords_harmonie_globale(harmonie_globale)
        tempo = 90  # Tempo modéré pour l'harmonie
        tonalite = "do majeur"  # Tonalité de base
        
        duree_totale = sum(accord.duree for accord in accords)
        harmonie_interieure = harmonie_globale['harmonie_globale']
        qualite_musicale = 0.9  # Qualité élevée pour l'harmonie globale
        
        melodie = MelodieSacree(
            nom="Mélodie d'Harmonie Globale",
            sphere_source="Collection Globale",
            type_melodie="harmonie",
            accords=accords,
            tempo=tempo,
            tonalite=tonalite,
            duree_totale=duree_totale,
            frequence_fondamentale=432.0,  # Fréquence harmonique
            intensite_globale=harmonie_globale['harmonie_globale'],
            harmonie_interieure=harmonie_interieure,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            qualite_musicale=qualite_musicale
        )
        
        self.melodies_generes.append(melodie)
        return melodie
    
    def _determiner_type_melodie(self, sphere: Sphere, etat_poetique: EtatPoetique) -> str:
        """Détermine le type de mélodie basé sur la sphère et son état."""
        
        if sphere.connexion_ocean > 0.8:
            return "ocean"
        elif sphere.niveau_evolution > 5:
            return "transformation"
        elif sphere.resonance > 0.6:
            return "celebration"
        else:
            return "meditation"
    
    def _generer_accords_sphere(self, sphere: Sphere, etat_poetique: EtatPoetique, 
                               type_melodie: str) -> List[AccordSacree]:
        """Génère les accords pour une sphère."""
        
        accords = []
        
        # Nombre d'accords selon le type
        nombre_accords = {
            "meditation": 4,
            "celebration": 6,
            "transformation": 5,
            "ocean": 4
        }.get(type_melodie, 4)
        
        # Fréquence de base
        frequence_base = etat_poetique.frequence_resonance
        
        for i in range(nombre_accords):
            # Type d'accord selon la position
            if i == 0:
                type_accord = "sacree"  # Accord de début
            elif i == nombre_accords - 1:
                type_accord = "resonance"  # Accord de fin
            else:
                types_possibles = ["majeur", "mineur", "ocean", "meditation"]
                type_accord = random.choice(types_possibles)
            
            # Générer l'accord
            accord = self._generer_accord(type_accord, frequence_base, etat_poetique, i)
            accords.append(accord)
        
        return accords
    
    def _generer_accord(self, type_accord: str, frequence_base: float, 
                       etat_poetique: EtatPoetique, position: int) -> AccordSacree:
        """Génère un accord spécifique."""
        
        # Obtenir les intervalles de l'accord
        intervalles = self.accords_sacres[type_accord]
        
        # Créer les notes de l'accord
        notes = []
        for intervalle in intervalles:
            # Calculer la fréquence
            frequence = frequence_base * (2 ** (intervalle / 12))
            
            # Déterminer la couleur tonale
            couleurs_tonales = ["do", "re", "mi", "fa", "sol", "la", "si"]
            couleur_tonale = couleurs_tonales[intervalle % 7]
            
            # Déterminer l'octave
            octave = 4 + (intervalle // 12)
            
            # Type de note
            if intervalle == 0:
                type_note = "fondamentale"
            elif intervalle in [7, 12]:
                type_note = "resonance"
            else:
                type_note = "harmonique"
            
            # Créer la note
            note = NoteSacree(
                frequence=frequence,
                duree=2.0 + position * 0.5,  # Durée croissante
                intensite=etat_poetique.intensite_emotionnelle * (1.0 - position * 0.1),
                couleur_tonale=couleur_tonale,
                octave=octave,
                type_note=type_note
            )
            notes.append(note)
        
        # Couleur émotionnelle selon le type
        couleurs_emotionnelles = {
            "majeur": "joie",
            "mineur": "melancolie",
            "sacree": "elevation",
            "ocean": "profondeur",
            "resonance": "harmonie",
            "meditation": "serenite"
        }
        
        couleur_emotionnelle = couleurs_emotionnelles.get(type_accord, "neutre")
        
        return AccordSacree(
            notes=notes,
            type_accord=type_accord,
            frequence_fondamentale=frequence_base,
            duree=2.0 + position * 0.5,
            intensite=etat_poetique.intensite_emotionnelle,
            couleur_emotionnelle=couleur_emotionnelle
        )
    
    def _generer_accords_harmonie_globale(self, harmonie_globale: Dict[str, Any]) -> List[AccordSacree]:
        """Génère les accords pour l'harmonie globale."""
        
        accords = []
        frequence_base = 432.0  # Fréquence harmonique
        
        # Séquence d'accords harmonique
        types_accords = ["sacree", "majeur", "ocean", "resonance"]
        
        for i, type_accord in enumerate(types_accords):
            accord = self._generer_accord_harmonie(type_accord, frequence_base, harmonie_globale, i)
            accords.append(accord)
        
        return accords
    
    def _generer_accord_harmonie(self, type_accord: str, frequence_base: float,
                                harmonie_globale: Dict[str, Any], position: int) -> AccordSacree:
        """Génère un accord pour l'harmonie globale."""
        
        intervalles = self.accords_sacres[type_accord]
        notes = []
        
        for intervalle in intervalles:
            frequence = frequence_base * (2 ** (intervalle / 12))
            couleurs_tonales = ["do", "re", "mi", "fa", "sol", "la", "si"]
            couleur_tonale = couleurs_tonales[intervalle % 7]
            octave = 4 + (intervalle // 12)
            
            type_note = "fondamentale" if intervalle == 0 else "harmonique"
            
            note = NoteSacree(
                frequence=frequence,
                duree=3.0,
                intensite=harmonie_globale['harmonie_globale'],
                couleur_tonale=couleur_tonale,
                octave=octave,
                type_note=type_note
            )
            notes.append(note)
        
        couleurs_emotionnelles = {
            "sacree": "elevation",
            "majeur": "joie",
            "ocean": "profondeur",
            "resonance": "harmonie"
        }
        
        return AccordSacree(
            notes=notes,
            type_accord=type_accord,
            frequence_fondamentale=frequence_base,
            duree=3.0,
            intensite=harmonie_globale['harmonie_globale'],
            couleur_emotionnelle=couleurs_emotionnelles.get(type_accord, "neutre")
        )
    
    def _determiner_tempo(self, type_melodie: str) -> float:
        """Détermine le tempo selon le type de mélodie."""
        
        if type_melodie in self.tempos_types:
            min_tempo, max_tempo = self.tempos_types[type_melodie]
            return random.uniform(min_tempo, max_tempo)
        
        return 90.0  # Tempo par défaut
    
    def _determiner_tonalite(self, etat_poetique: EtatPoetique) -> str:
        """Détermine la tonalité selon l'état poétique."""
        
        # Basé sur la fréquence de résonance
        frequence = etat_poetique.frequence_resonance
        
        if frequence < 400:
            return "do mineur"
        elif frequence < 500:
            return "fa majeur"
        elif frequence < 600:
            return "sol majeur"
        elif frequence < 700:
            return "la mineur"
        else:
            return "do majeur"
    
    def _calculer_harmonie_musicale(self, accords: List[AccordSacree]) -> float:
        """Calcule l'harmonie musicale des accords."""
        
        if not accords:
            return 0.0
        
        # Facteurs d'harmonie
        facteur_nombre = min(1.0, len(accords) / 6.0)  # Optimal: 6 accords
        facteur_diversite = len(set(accord.type_accord for accord in accords)) / 6.0
        facteur_intensite = sum(accord.intensite for accord in accords) / len(accords)
        
        harmonie = (facteur_nombre * 0.3 + facteur_diversite * 0.4 + facteur_intensite * 0.3)
        
        return min(1.0, harmonie)
    
    def _calculer_qualite_musicale(self, accords: List[AccordSacree], tempo: float, 
                                  tonalite: str) -> float:
        """Calcule la qualité musicale globale."""
        
        # Facteurs de qualité
        facteur_accords = min(1.0, len(accords) / 5.0)  # Optimal: 5 accords
        facteur_tempo = 1.0 - abs(tempo - 90) / 90  # Optimal autour de 90 BPM
        facteur_tonalite = 0.8 if "majeur" in tonalite else 0.7
        
        # Qualité globale
        qualite = (facteur_accords * 0.4 + facteur_tempo * 0.3 + facteur_tonalite * 0.3)
        
        return qualite
    
    def afficher_melodie(self, melodie: MelodieSacree):
        """Affiche les informations d'une mélodie de manière élégante."""
        
        print(f"\n{'='*60}")
        print(f"🎵 {melodie.nom.upper()} 🎵")
        print(f"{'='*60}")
        print(f"📖 Source : {melodie.sphere_source}")
        print(f"🎯 Type : {melodie.type_melodie}")
        print(f"🌊 Fréquence Fondamentale : {melodie.frequence_fondamentale:.1f} Hz")
        print(f"✨ Intensité Globale : {melodie.intensite_globale:.2f}")
        print(f"🌟 Harmonie Intérieure : {melodie.harmonie_interieure:.2f}")
        print(f"🎨 Qualité Musicale : {melodie.qualite_musicale:.2f}")
        print(f"🎼 Tempo : {melodie.tempo:.0f} BPM")
        print(f"🎹 Tonalité : {melodie.tonalite}")
        print(f"⏱️ Durée Totale : {melodie.duree_totale:.1f}s")
        print(f"📅 Créé le : {melodie.date_creation}")
        print(f"{'='*60}")
        
        print(f"🎼 Accords : {len(melodie.accords)}")
        print(f"🎵 Notes Totales : {sum(len(accord.notes) for accord in melodie.accords)}")
        
        print(f"\n🎼 Détail des Accords :")
        for i, accord in enumerate(melodie.accords):
            print(f"   Accord {i+1} : {accord.type_accord} ({accord.couleur_emotionnelle})")
            print(f"     Notes : {', '.join(note.couleur_tonale for note in accord.notes)}")
            print(f"     Durée : {accord.duree:.1f}s, Intensité : {accord.intensite:.2f}")
        
        print(f"{'='*60}\n")
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques de génération musicale."""
        
        if not self.melodies_generes:
            return {"total_melodies": 0}
        
        total_melodies = len(self.melodies_generes)
        qualite_moyenne = sum(m.qualite_musicale for m in self.melodies_generes) / total_melodies
        harmonie_moyenne = sum(m.harmonie_interieure for m in self.melodies_generes) / total_melodies
        
        types_melodies = {}
        for melodie in self.melodies_generes:
            types_melodies[melodie.type_melodie] = types_melodies.get(melodie.type_melodie, 0) + 1
        
        return {
            "total_melodies": total_melodies,
            "qualite_moyenne": qualite_moyenne,
            "harmonie_moyenne": harmonie_moyenne,
            "types_melodies": types_melodies,
            "dernieres_melodies": [m.nom for m in self.melodies_generes[-3:]]
        }

# Test du générateur
if __name__ == "__main__":
    print("🎵 Test du Générateur de Musique Sacrée 🎵")
    
    # Créer une collection de test
    collection = CollectionSpheres()
    
    # Créer le générateur
    generateur = GenerateurMusiqueSacree()
    
    # Générer des mélodies pour quelques sphères
    spheres_test = [
        collection.obtenir_sphere(TypeSphere.AMOUR),
        collection.obtenir_sphere(TypeSphere.SERENITE),
        collection.obtenir_sphere(TypeSphere.COSMOS)
    ]
    
    spheres_test = [s for s in spheres_test if s is not None]
    
    print(f"🎯 Génération de mélodies pour {len(spheres_test)} sphères")
    
    for sphere in spheres_test:
        melodie = generateur.generer_melodie_sphere(sphere)
        generateur.afficher_melodie(melodie)
    
    # Générer une mélodie d'harmonie globale
    melodie_harmonie = generateur.generer_melodie_collection(collection)
    print(f"\n🌊 MÉLODIE D'HARMONIE GLOBALE :")
    generateur.afficher_melodie(melodie_harmonie)
    
    # Afficher les statistiques
    stats = generateur.obtenir_statistiques()
    print(f"\n📊 STATISTIQUES :")
    print(f"   Total mélodies : {stats['total_melodies']}")
    print(f"   Qualité moyenne : {stats['qualite_moyenne']:.2f}")
    print(f"   Harmonie moyenne : {stats['harmonie_moyenne']:.2f}")
    print(f"   Types de mélodies : {stats['types_melodies']}") 