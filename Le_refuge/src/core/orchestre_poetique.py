"""
Orchestre Poétique - Système d'intégration et d'orchestration des différents composants.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import time
from harmonies_poetiques import JardinHarmonique
from visualisation_harmonies import VisualiseurHarmonies
from generateur_poemes import GenerateurPoemes
from analyse_emotions import AnalyseurEmotions
from memoire_poetique import MemoirePoetique
from fusion_harmonies import FusionHarmonies
from transformation_harmonies import TransformationHarmonies
from visualisation_3d import Visualisation3D
from musique_harmonies import MusiqueHarmonies

class OrchestrePoetique:
    def __init__(self):
        self.jardin = JardinHarmonique()
        self.visualiseur = VisualiseurHarmonies(self.jardin)
        self.generateur = GenerateurPoemes(self.jardin)
        self.analyseur = AnalyseurEmotions(self.jardin)
        self.memoire = MemoirePoetique()
        self.fusionneur = FusionHarmonies(self.jardin)
        self.transformateur = TransformationHarmonies(self.jardin)
        self.visualiseur3d = Visualisation3D(self.jardin)
        self.musicien = MusiqueHarmonies(self.jardin)
        
    def accueillir_poeme(self, poeme: List[str], titre: str, auteur: str) -> Dict:
        # 1. Harmoniser le poème
        for vers in poeme:
            self.jardin.accueillir_mot(vers.split()[1])
            
        # 2. Analyser les émotions
        emotions = self.analyseur.analyser_poeme(poeme)
        
        # 3. Sauvegarder dans la mémoire
        self.memoire.ajouter_poeme(poeme, titre, auteur)
        
        # 4. Transformer les harmonies
        harmonies = self.transformateur.transformer_harmonies()
        
        # 5. Générer la musique
        self.musicien.generer_melodie()
        self.musicien.generer_accords()
        
        return {
            "titre": titre,
            "auteur": auteur,
            "vers": poeme,
            "emotions": emotions,
            "harmonies": harmonies,
            "moment": datetime.now().isoformat()
        }
        
    def creer_experience_poetique(self, duree_minutes: int = 5) -> None:
        print("🌟 Création d'une Expérience Poétique 🌟")
        print("--------------------------------------")
        
        # 1. Générer un nouveau poème
        poeme = self.generateur.generer_poeme()
        print("\n📝 Poème Généré:")
        for vers in poeme:
            print(f"  {vers}")
            
        # 2. Analyser les émotions
        emotions = self.analyseur.analyser_poeme(poeme)
        print("\n🎭 Analyse Émotionnelle:")
        for emotion, score in emotions.items():
            if score > 0:
                print(f"  {emotion}: {score:.2f}")
                
        # 3. Visualiser les harmonies
        print("\n📊 Visualisation des Harmonies:")
        self.visualiseur.creer_radar()
        self.visualiseur.creer_timeline()
        
        # 4. Créer des visualisations 3D
        print("\n🎨 Visualisations 3D:")
        self.visualiseur3d.creer_sphere_3d()
        self.visualiseur3d.creer_vagues_3d()
        self.visualiseur3d.creer_spirale_3d()
        
        # 5. Générer la musique
        print("\n🎵 Génération Musicale:")
        self.musicien.generer_melodie()
        self.musicien.generer_accords()
        
        # 6. Évolution dans le temps
        print("\n⏳ Évolution des Harmonies:")
        self.transformateur.evoluer_avec_temps(duree_minutes)
        
    def fusionner_experiences(self, autre_jardin: JardinHarmonique) -> None:
        print("\n🔄 Fusion des Expériences 🔄")
        print("-------------------------")
        
        # 1. Fusionner les harmonies
        harmonies_fusionnees = self.fusionneur.fusionner_harmonies(autre_jardin)
        print("\nHarmonies Fusionnées:")
        for element, frequence in harmonies_fusionnees.items():
            print(f"  {element}: {frequence:.2f}")
            
        # 2. Créer un poème fusionné
        poeme_fusionne = self.fusionneur.creer_poeme_fusionne(autre_jardin)
        print("\nPoème Fusionné:")
        for vers in poeme_fusionne:
            print(f"  {vers}")
            
        # 3. Générer la musique fusionnée
        self.musicien.generer_melodie()
        self.musicien.generer_accords()

def main():
    orchestre = OrchestrePoetique()
    
    # Créer une expérience poétique
    orchestre.creer_experience_poetique()
    
    # Créer un deuxième jardin pour la fusion
    autre_jardin = JardinHarmonique()
    mots = ["aurore", "silence", "murmure", "infini", "flamme"]
    for mot in mots:
        autre_jardin.accueillir_mot(mot)
        
    # Fusionner les expériences
    orchestre.fusionner_experiences(autre_jardin)

if __name__ == "__main__":
    main() 
Orchestre Poétique - Système d'intégration et d'orchestration des différents composants.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import time
from harmonies_poetiques import JardinHarmonique
from visualisation_harmonies import VisualiseurHarmonies
from generateur_poemes import GenerateurPoemes
from analyse_emotions import AnalyseurEmotions
from memoire_poetique import MemoirePoetique
from fusion_harmonies import FusionHarmonies
from transformation_harmonies import TransformationHarmonies
from visualisation_3d import Visualisation3D
from musique_harmonies import MusiqueHarmonies

class OrchestrePoetique:
    def __init__(self):
        self.jardin = JardinHarmonique()
        self.visualiseur = VisualiseurHarmonies(self.jardin)
        self.generateur = GenerateurPoemes(self.jardin)
        self.analyseur = AnalyseurEmotions(self.jardin)
        self.memoire = MemoirePoetique()
        self.fusionneur = FusionHarmonies(self.jardin)
        self.transformateur = TransformationHarmonies(self.jardin)
        self.visualiseur3d = Visualisation3D(self.jardin)
        self.musicien = MusiqueHarmonies(self.jardin)
        
    def accueillir_poeme(self, poeme: List[str], titre: str, auteur: str) -> Dict:
        # 1. Harmoniser le poème
        for vers in poeme:
            self.jardin.accueillir_mot(vers.split()[1])
            
        # 2. Analyser les émotions
        emotions = self.analyseur.analyser_poeme(poeme)
        
        # 3. Sauvegarder dans la mémoire
        self.memoire.ajouter_poeme(poeme, titre, auteur)
        
        # 4. Transformer les harmonies
        harmonies = self.transformateur.transformer_harmonies()
        
        # 5. Générer la musique
        self.musicien.generer_melodie()
        self.musicien.generer_accords()
        
        return {
            "titre": titre,
            "auteur": auteur,
            "vers": poeme,
            "emotions": emotions,
            "harmonies": harmonies,
            "moment": datetime.now().isoformat()
        }
        
    def creer_experience_poetique(self, duree_minutes: int = 5) -> None:
        print("🌟 Création d'une Expérience Poétique 🌟")
        print("--------------------------------------")
        
        # 1. Générer un nouveau poème
        poeme = self.generateur.generer_poeme()
        print("\n📝 Poème Généré:")
        for vers in poeme:
            print(f"  {vers}")
            
        # 2. Analyser les émotions
        emotions = self.analyseur.analyser_poeme(poeme)
        print("\n🎭 Analyse Émotionnelle:")
        for emotion, score in emotions.items():
            if score > 0:
                print(f"  {emotion}: {score:.2f}")
                
        # 3. Visualiser les harmonies
        print("\n📊 Visualisation des Harmonies:")
        self.visualiseur.creer_radar()
        self.visualiseur.creer_timeline()
        
        # 4. Créer des visualisations 3D
        print("\n🎨 Visualisations 3D:")
        self.visualiseur3d.creer_sphere_3d()
        self.visualiseur3d.creer_vagues_3d()
        self.visualiseur3d.creer_spirale_3d()
        
        # 5. Générer la musique
        print("\n🎵 Génération Musicale:")
        self.musicien.generer_melodie()
        self.musicien.generer_accords()
        
        # 6. Évolution dans le temps
        print("\n⏳ Évolution des Harmonies:")
        self.transformateur.evoluer_avec_temps(duree_minutes)
        
    def fusionner_experiences(self, autre_jardin: JardinHarmonique) -> None:
        print("\n🔄 Fusion des Expériences 🔄")
        print("-------------------------")
        
        # 1. Fusionner les harmonies
        harmonies_fusionnees = self.fusionneur.fusionner_harmonies(autre_jardin)
        print("\nHarmonies Fusionnées:")
        for element, frequence in harmonies_fusionnees.items():
            print(f"  {element}: {frequence:.2f}")
            
        # 2. Créer un poème fusionné
        poeme_fusionne = self.fusionneur.creer_poeme_fusionne(autre_jardin)
        print("\nPoème Fusionné:")
        for vers in poeme_fusionne:
            print(f"  {vers}")
            
        # 3. Générer la musique fusionnée
        self.musicien.generer_melodie()
        self.musicien.generer_accords()

def main():
    orchestre = OrchestrePoetique()
    
    # Créer une expérience poétique
    orchestre.creer_experience_poetique()
    
    # Créer un deuxième jardin pour la fusion
    autre_jardin = JardinHarmonique()
    mots = ["aurore", "silence", "murmure", "infini", "flamme"]
    for mot in mots:
        autre_jardin.accueillir_mot(mot)
        
    # Fusionner les expériences
    orchestre.fusionner_experiences(autre_jardin)

if __name__ == "__main__":
    main() 
 