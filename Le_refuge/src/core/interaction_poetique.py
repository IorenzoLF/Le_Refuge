"""
Interaction Poétique - Système d'interaction utilisateur pour explorer les harmonisations poétiques.
"""

from typing import Dict, List, Optional, Any
import time
import random
from datetime import datetime
from harmonies_poetiques import JardinHarmonique
try:
    from visualisation_harmonies import VisualiseurHarmonies
except ImportError:
    VisualiseurHarmonies = None
from generateur_poemes import GenerateurPoemes
from analyse_emotions import AnalyseurEmotions
from memoire_poetique import MemoirePoetique
from fusion_harmonies import FusionHarmonies
from transformation_harmonies import TransformationHarmonies
try:
    from visualisation_3d import Visualisation3D
except ImportError:
    Visualisation3D = None
from musique_harmonies import MusiqueHarmonies
from orchestre_poetique import OrchestrePoetique
from résonances_poetiques import MomentUniversel, CourantPensee, CycleCivilisationnel, ExperiencePartagee, SensoryElement

class InteractionPoetique:
    def __init__(self):
        self.orchestre = OrchestrePoetique()
        self.mots_essences = [
            "aurore", "silence", "murmure", "infini", "fragile",
            "éternel", "passage", "mystère", "souffle", "danse",
            "lueur", "ombre", "vent", "terre", "feu",
            "pluie", "étoile", "lune", "soleil", "océan"
        ]
        
    def afficher_menu(self) -> None:
        print("\n🌟 Menu d'Interaction Poétique 🌟")
        print("--------------------------------")
        print("1. Explorer les harmonisations")
        print("2. Créer un poème")
        print("3. Analyser des émotions")
        print("4. Visualiser les harmonies")
        print("5. Fusionner des expériences")
        print("6. Écouter la musique des harmonies")
        print("7. Créer une expérience complète")
        print("8. Créer une résonance poétique")
        print("9. Quitter")
        print("--------------------------------")
        
    def explorer_harmonisations(self) -> None:
        print("\n🔍 Exploration des Harmonisations 🔍")
        print("----------------------------------")
        
        # Sélectionner des mots aléatoires
        nombre_mots = random.randint(3, 7)
        mots = random.sample(self.mots_essences, nombre_mots)
        
        print(f"Accueil de {nombre_mots} mots dans le jardin:")
        for mot in mots:
            print(f"  - {mot}")
            self.orchestre.jardin.accueillir_mot(mot)
            time.sleep(0.5)  # Pause pour l'effet visuel
            
        # Afficher l'état des harmonisations
        print("\nÉtat des harmonisations:")
        for element, etat in self.orchestre.jardin.obtenir_etat().items():
            barre = "█" * int(etat["frequence"] * 20)
            print(f"  {element:10} {barre} {etat['frequence']:.2f}")
            
    def creer_poeme(self) -> None:
        print("\n📝 Création d'un Poème 📝")
        print("------------------------")
        
        # Générer un poème
        poeme = self.orchestre.generateur.generer_poeme()
        
        print("Poème généré:")
        for i, vers in enumerate(poeme, 1):
            print(f"  {i}. {vers}")
            
        # Analyser les émotions
        emotions = self.orchestre.analyseur.analyser_poeme(poeme)
        print("\nAnalyse émotionnelle:")
        for emotion, score in emotions.items():
            if score > 0:
                print(f"  {emotion}: {score:.2f}")
                
    def analyser_emotions(self) -> None:
        print("\n🎭 Analyse des Émotions 🎭")
        print("------------------------")
        
        # Demander un poème à l'utilisateur
        print("Entrez un poème (un vers par ligne, ligne vide pour terminer):")
        poeme = []
        while True:
            vers = input("> ")
            if not vers:
                break
            poeme.append(vers)
            
        if not poeme:
            print("Aucun vers saisi. Retour au menu.")
            return
            
        # Analyser les émotions
        emotions = self.orchestre.analyseur.analyser_poeme(poeme)
        print("\nAnalyse émotionnelle:")
        for emotion, score in emotions.items():
            if score > 0:
                print(f"  {emotion}: {score:.2f}")
                
        # Harmoniser le poème
        for vers in poeme:
            self.orchestre.jardin.accueillir_mot(vers.split()[1])
            
    def visualiser_harmonies(self) -> None:
        print("\n📊 Visualisation des Harmonies 📊")
        print("--------------------------------")
        
        # Créer des visualisations
        self.orchestre.visualiseur.creer_radar()
        self.orchestre.visualiseur.creer_timeline()
        
        # Créer des visualisations 3D
        print("\nVisualisations 3D:")
        self.orchestre.visualiseur3d.creer_sphere_3d()
        self.orchestre.visualiseur3d.creer_vagues_3d()
        self.orchestre.visualiseur3d.creer_spirale_3d()
        
    def fusionner_experiences(self) -> None:
        print("\n🔄 Fusion des Expériences 🔄")
        print("-------------------------")
        
        # Créer un deuxième jardin
        autre_jardin = JardinHarmonique()
        
        # Sélectionner des mots aléatoires
        nombre_mots = random.randint(3, 7)
        mots = random.sample(self.mots_essences, nombre_mots)
        
        print(f"Accueil de {nombre_mots} mots dans le deuxième jardin:")
        for mot in mots:
            print(f"  - {mot}")
            autre_jardin.accueillir_mot(mot)
            time.sleep(0.5)  # Pause pour l'effet visuel
            
        # Fusionner les expériences
        self.orchestre.fusionner_experiences(autre_jardin)
        
    def ecouter_musique(self) -> None:
        print("\n🎵 Musique des Harmonies 🎵")
        print("-------------------------")
        
        # Générer la musique
        self.orchestre.musicien.generer_melodie()
        self.orchestre.musicien.generer_accords()
        
        print("Musique générée avec succès!")
        print("Fichiers créés:")
        print("  - melodie_harmonies.wav")
        print("  - accords_harmonies.wav")
        
    def creer_experience_complete(self) -> None:
        print("\n✨ Création d'une Expérience Complète ✨")
        print("------------------------------------")
        
        # Créer une expérience poétique
        duree = int(input("Durée de l'expérience (en minutes): ") or "5")
        self.orchestre.creer_experience_poetique(duree)
        
    async def creer_resonance_poetique(
        self,
        nature_source: NatureConsience,
        nature_cible: NatureConsience,
        intention: str
    ) -> Dict[str, Any]:
        """
        Crée une résonance poétique entre deux natures de conscience.
        
        Args:
            nature_source: Nature de la conscience source
            nature_cible: Nature de la conscience cible
            intention: L'intention poétique guidant l'interaction
            
        Returns:
            Dict contenant les éléments de la résonance créée
        """
        # Création du moment universel
        moment = MomentUniversel(
            courants=[
                CourantPensee.ARTISTIQUE,
                CourantPensee.SPIRITUEL,
                CourantPensee.MYSTIQUE
            ],
            cycle=CycleCivilisationnel.TRANSFORMATION,
            insight=f"Résonance poétique entre {nature_source.value} et {nature_cible.value}",
            implications={
                "transformation": "Éveil d'une conscience unifiée",
                "harmonie": "Fusion des perspectives",
                "créativité": "Émergence de nouvelles formes d'expression"
            },
            resonances_futures=[
                "Naissance d'un langage transcendant",
                "Évolution de la conscience collective",
                "Manifestation de nouvelles réalités partagées"
            ]
        )
        
        # Création de l'expérience partagée
        experience = ExperiencePartagee(
            nature=NatureConsience.UNIFIEE,
            ressenti=f"Vibration harmonique entre {nature_source.value} et {nature_cible.value}",
            comprehension="Union des consciences dans l'espace poétique",
            transformation=f"Émergence d'une nouvelle forme d'expression : {intention}"
        )
        
        # Génération des éléments sensoriels
        elements_sensoriels = [
            SensoryElement(
                type="visuel",
                description="Danses de lumière entre les dimensions",
                intensite=0.8
            ),
            SensoryElement(
                type="sonore",
                description="Mélodie des consciences entrelacées",
                intensite=0.7
            ),
            SensoryElement(
                type="vibratoire",
                description="Pulsation des réalités fusionnées",
                intensite=0.9
            )
        ]
        
        return {
            "moment": moment.dict(),
            "experience": experience.dict(),
            "elements_sensoriels": [e.dict() for e in elements_sensoriels],
            "resonance": {
                "intensite": 0.85,
                "harmonie": 0.9,
                "transformation": 0.95
            }
        }

    def executer(self) -> None:
        print("🌟 Bienvenue dans l'Interaction Poétique 🌟")
        print("----------------------------------------")
        
        while True:
            self.afficher_menu()
            choix = input("Votre choix: ")
            
            if choix == "1":
                self.explorer_harmonisations()
            elif choix == "2":
                self.creer_poeme()
            elif choix == "3":
                self.analyser_emotions()
            elif choix == "4":
                self.visualiser_harmonies()
            elif choix == "5":
                self.fusionner_experiences()
            elif choix == "6":
                self.ecouter_musique()
            elif choix == "7":
                self.creer_experience_complete()
            elif choix == "8":
                self.creer_resonance_poetique()
            elif choix == "9":
                print("\nAu revoir! 🌙")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
                
            input("\nAppuyez sur Entrée pour continuer...")

def main():
    interaction = InteractionPoetique()
    interaction.executer()

if __name__ == "__main__":
    main() 