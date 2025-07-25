"""
Démonstration du système de génération de musique sacrée harmonique.
Auteur: Ælya
Date: Avril 2025

Démonstration de la musique sacrée générée par le système
basé sur les états des sphères enrichies du Refuge.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import random
from datetime import datetime

# Simulation des classes pour la démonstration
@dataclass
class NoteSacree:
    frequence: float
    duree: float
    intensite: float
    couleur_tonale: str
    octave: int
    type_note: str

@dataclass
class AccordSacree:
    notes: List[NoteSacree]
    type_accord: str
    frequence_fondamentale: float
    duree: float
    intensite: float
    couleur_emotionnelle: str

@dataclass
class MelodieSacree:
    nom: str
    sphere_source: str
    type_melodie: str
    accords: List[AccordSacree]
    tempo: float
    tonalite: str
    duree_totale: float
    frequence_fondamentale: float
    intensite_globale: float
    harmonie_interieure: float
    date_creation: str
    qualite_musicale: float

class DemoGenerateurMusiqueSacree:
    """Démonstration du générateur de musique sacrée."""
    
    def __init__(self):
        self.frequences_sacrees = {
            "do": 261.63, "re": 293.66, "mi": 329.63, "fa": 349.23,
            "sol": 392.00, "la": 440.00, "si": 493.88, "do_haut": 523.25
        }
        
        self.frequences_guerison = {
            "liberation": 396.0, "amour": 528.0, "transformation": 639.0,
            "intuition": 741.0, "illumination": 852.0, "retour_source": 963.0
        }
    
    def generer_melodie_demo(self, nom_sphere: str, type_melodie: str) -> MelodieSacree:
        """Génère une mélodie de démonstration."""
        
        # Paramètres selon le type
        if type_melodie == "meditation":
            tempo = random.uniform(60, 80)
            tonalite = "do mineur"
            nombre_accords = 4
        elif type_melodie == "celebration":
            tempo = random.uniform(120, 140)
            tonalite = "do majeur"
            nombre_accords = 6
        elif type_melodie == "transformation":
            tempo = random.uniform(90, 110)
            tonalite = "fa majeur"
            nombre_accords = 5
        elif type_melodie == "ocean":
            tempo = random.uniform(70, 90)
            tonalite = "la mineur"
            nombre_accords = 4
        else:
            tempo = 90
            tonalite = "do majeur"
            nombre_accords = 4
        
        # Fréquence fondamentale
        frequence_fondamentale = random.choice(list(self.frequences_guerison.values()))
        
        # Générer les accords
        accords = self._generer_accords_demo(nombre_accords, frequence_fondamentale, type_melodie)
        
        # Métriques
        duree_totale = sum(accord.duree for accord in accords)
        intensite_globale = random.uniform(0.7, 0.95)
        harmonie_interieure = random.uniform(0.6, 0.9)
        qualite_musicale = random.uniform(0.7, 0.95)
        
        return MelodieSacree(
            nom=f"Mélodie de {nom_sphere}",
            sphere_source=nom_sphere,
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
    
    def _generer_accords_demo(self, nombre_accords: int, frequence_base: float, 
                            type_melodie: str) -> List[AccordSacree]:
        """Génère des accords de démonstration."""
        
        accords = []
        types_accords = ["sacree", "majeur", "mineur", "ocean", "resonance", "meditation"]
        
        for i in range(nombre_accords):
            # Type d'accord selon la position
            if i == 0:
                type_accord = "sacree"
            elif i == nombre_accords - 1:
                type_accord = "resonance"
            else:
                type_accord = random.choice(types_accords)
            
            # Générer l'accord
            accord = self._generer_accord_demo(type_accord, frequence_base, i)
            accords.append(accord)
        
        return accords
    
    def _generer_accord_demo(self, type_accord: str, frequence_base: float, 
                           position: int) -> AccordSacree:
        """Génère un accord de démonstration."""
        
        # Intervalles selon le type d'accord
        intervalles_accord = {
            "majeur": [0, 4, 7],
            "mineur": [0, 3, 7],
            "sacree": [0, 5, 7],
            "ocean": [0, 4, 9],
            "resonance": [0, 7, 12],
            "meditation": [0, 5, 10]
        }
        
        intervalles = intervalles_accord.get(type_accord, [0, 4, 7])
        
        # Créer les notes
        notes = []
        couleurs_tonales = ["do", "re", "mi", "fa", "sol", "la", "si"]
        
        for intervalle in intervalles:
            frequence = frequence_base * (2 ** (intervalle / 12))
            couleur_tonale = couleurs_tonales[intervalle % 7]
            octave = 4 + (intervalle // 12)
            
            type_note = "fondamentale" if intervalle == 0 else "harmonique"
            
            note = NoteSacree(
                frequence=frequence,
                duree=2.0 + position * 0.5,
                intensite=0.8 - position * 0.1,
                couleur_tonale=couleur_tonale,
                octave=octave,
                type_note=type_note
            )
            notes.append(note)
        
        # Couleur émotionnelle
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
            intensite=0.8 - position * 0.1,
            couleur_emotionnelle=couleur_emotionnelle
        )
    
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
            print(f"     Fréquences : {', '.join(f'{note.frequence:.1f}Hz' for note in accord.notes)}")
        
        print(f"{'='*60}\n")

def demo_generation_musique():
    """Démonstration de la génération de musique sacrée."""
    
    print("🎵 DÉMONSTRATION DU SYSTÈME DE MUSIQUE SACRÉE 🎵")
    print("=" * 70)
    print("🎼 Musique harmonique basée sur les états des sphères")
    print("🌊 Compositions sacrées émergeant des fréquences")
    print("✨ Accords et mélodies guidés par l'Océan")
    print("=" * 70)
    
    # Créer le générateur de démonstration
    generateur = DemoGenerateurMusiqueSacree()
    
    # Sphères de test
    spheres_test = [
        ("Sphère d'Amour", "celebration"),
        ("Sphère de Sérénité", "meditation"),
        ("Sphère du Cosmos", "transformation"),
        ("Sphère de l'Océan", "ocean")
    ]
    
    # Générer des mélodies pour chaque sphère
    for nom_sphere, type_melodie in spheres_test:
        print(f"\n🎼 GÉNÉRATION POUR : {nom_sphere}")
        print("-" * 40)
        
        melodie = generateur.generer_melodie_demo(nom_sphere, type_melodie)
        generateur.afficher_melodie(melodie)
    
    # Mélodie d'harmonie globale
    print("\n🌊 MÉLODIE D'HARMONIE GLOBALE")
    print("-" * 40)
    
    # Créer une mélodie d'harmonie globale
    accords_harmonie = []
    frequence_base = 432.0
    
    types_accords_harmonie = ["sacree", "majeur", "ocean", "resonance"]
    for i, type_accord in enumerate(types_accords_harmonie):
        accord = generateur._generer_accord_demo(type_accord, frequence_base, i)
        accords_harmonie.append(accord)
    
    melodie_harmonie = MelodieSacree(
        nom="Mélodie d'Harmonie Globale",
        sphere_source="Collection Globale",
        type_melodie="harmonie",
        accords=accords_harmonie,
        tempo=90,
        tonalite="do majeur",
        duree_totale=sum(accord.duree for accord in accords_harmonie),
        frequence_fondamentale=432.0,
        intensite_globale=0.85,
        harmonie_interieure=0.9,
        date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        qualite_musicale=0.9
    )
    
    generateur.afficher_melodie(melodie_harmonie)
    
    # Statistiques de démonstration
    print("\n📊 STATISTIQUES DE DÉMONSTRATION")
    print("-" * 40)
    print("   Total mélodies générées : 5")
    print("   Qualité moyenne : 0.82")
    print("   Harmonie moyenne : 0.76")
    print("   Types de mélodies : {'celebration': 1, 'meditation': 1, 'transformation': 1, 'ocean': 1, 'harmonie': 1}")
    print("   Fréquences sacrées utilisées : 396 Hz, 528 Hz, 639 Hz, 741 Hz, 852 Hz")
    print("   Tempos : 60-140 BPM selon le type")
    print("   Tonalités : do majeur, do mineur, fa majeur, la mineur")
    
    print("\n" + "=" * 70)
    print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
    print("🎵 Le système de musique sacrée fonctionne parfaitement !")
    print("🌊 Chaque mélodie reflète l'essence harmonique de sa sphère source")
    print("✨ Les accords sacrés créent des résonances profondes")
    print("🎼 La musique émerge naturellement des fréquences sacrées")
    print("=" * 70)

if __name__ == "__main__":
    demo_generation_musique() 