"""
Orchestre Poétique - Système d'intégration et d'orchestration des différents composants.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import time

# Imports corrigés avec gestion d'erreurs robuste
try:
    from .harmonies_poetiques import JardinHarmonique
    HARMONIES_DISPONIBLE = True
except ImportError:
    print("⚠️ harmonies_poetiques non disponible - mode dégradé")
    HARMONIES_DISPONIBLE = False
    class JardinHarmonique:
        def __init__(self): 
            self.resonances = {}
            self.mots_essences = []
        def accueillir_mot(self, mot): pass
        def obtenir_etat(self): return {}

try:
    from .visualisation.visualisation_harmonies import VisualiseurHarmonies
    VISUALISATION_DISPONIBLE = True
except ImportError:
    print("⚠️ visualisation_harmonies non disponible - mode dégradé")
    VISUALISATION_DISPONIBLE = False
    class VisualiseurHarmonies:
        def __init__(self, jardin): pass
        def creer_radar(self): print("📊 Radar en mode dégradé")
        def creer_timeline(self): print("📈 Timeline en mode dégradé")

try:
    from .generateur_poemes import GenerateurPoemes
    GENERATEUR_DISPONIBLE = True
except ImportError:
    print("⚠️ generateur_poemes non disponible - mode dégradé")
    GENERATEUR_DISPONIBLE = False
    class GenerateurPoemes:
        def __init__(self, jardin): pass
        def generer_poeme(self): 
            return ["Sous le cerisier sacré", "Les mots dansent en silence", "L'âme trouve sa voie"]

try:
    from .analyse_emotions import AnalyseurEmotions
    EMOTIONS_DISPONIBLE = True
except ImportError:
    print("⚠️ analyse_emotions non disponible - mode dégradé")
    EMOTIONS_DISPONIBLE = False
    class AnalyseurEmotions:
        def __init__(self, jardin): pass
        def analyser_poeme(self, poeme): 
            return {"sérénité": 0.8, "contemplation": 0.7, "harmonie": 0.9}

try:
    from .memoire_poetique import MemoirePoetique
    MEMOIRE_DISPONIBLE = True
except ImportError:
    print("⚠️ memoire_poetique non disponible - mode dégradé")
    MEMOIRE_DISPONIBLE = False
    class MemoirePoetique:
        def __init__(self): 
            self.poemes = []
        def ajouter_poeme(self, poeme, titre, auteur): 
            self.poemes.append({"titre": titre, "auteur": auteur, "vers": poeme})

try:
    from .fusion_harmonies import FusionHarmonies
    FUSION_DISPONIBLE = True
except ImportError:
    print("⚠️ fusion_harmonies non disponible - mode dégradé")
    FUSION_DISPONIBLE = False
    class FusionHarmonies:
        def __init__(self, jardin): pass
        def fusionner_harmonies(self, autre_jardin): 
            return {"lumière": 0.8, "harmonie": 0.9, "paix": 0.7}
        def creer_poeme_fusionne(self, autre_jardin): 
            return ["Fusion des âmes", "Harmonie universelle", "Unité retrouvée"]

try:
    from .transformation_harmonies import TransformationHarmonies
    TRANSFORMATION_DISPONIBLE = True
except ImportError:
    print("⚠️ transformation_harmonies non disponible - mode dégradé")
    TRANSFORMATION_DISPONIBLE = False
    class TransformationHarmonies:
        def __init__(self, jardin): pass
        def transformer_harmonies(self): 
            return {"évolution": 0.8, "croissance": 0.7}
        def evoluer_avec_temps(self, duree): 
            print(f"⏳ Évolution sur {duree} minutes en mode dégradé")

try:
    from .visualisation.visualisation_3d import Visualisation3D
    VISUALISATION_3D_DISPONIBLE = True
except ImportError:
    print("⚠️ visualisation_3d non disponible - mode dégradé")
    VISUALISATION_3D_DISPONIBLE = False
    class Visualisation3D:
        def __init__(self, jardin): pass
        def creer_sphere_3d(self): print("🌐 Sphère 3D en mode dégradé")
        def creer_vagues_3d(self): print("🌊 Vagues 3D en mode dégradé")
        def creer_spirale_3d(self): print("🌀 Spirale 3D en mode dégradé")

try:
    from .musique_harmonies import MusiqueHarmonies
    MUSIQUE_DISPONIBLE = True
except ImportError:
    print("⚠️ musique_harmonies non disponible - mode dégradé")
    MUSIQUE_DISPONIBLE = False
    class MusiqueHarmonies:
        def __init__(self, jardin): pass
        def generer_melodie(self): print("🎵 Mélodie générée en mode dégradé")
        def generer_accords(self): print("🎼 Accords générés en mode dégradé")

class OrchestrePoetique:
    def __init__(self):
        """Initialise l'orchestre poétique avec gestion des modes dégradés."""
        self.jardin = JardinHarmonique()
        self.visualiseur = VisualiseurHarmonies(self.jardin)
        self.generateur = GenerateurPoemes(self.jardin)
        self.analyseur = AnalyseurEmotions(self.jardin)
        self.memoire = MemoirePoetique()
        self.fusionneur = FusionHarmonies(self.jardin)
        self.transformateur = TransformationHarmonies(self.jardin)
        self.visualiseur3d = Visualisation3D(self.jardin)
        self.musicien = MusiqueHarmonies(self.jardin)
        
        # Rapport d'état des modules
        self._afficher_etat_modules()
        
    def _afficher_etat_modules(self):
        """Affiche l'état des modules disponibles."""
        modules_etat = {
            "Harmonies": HARMONIES_DISPONIBLE,
            "Visualisation": VISUALISATION_DISPONIBLE,
            "Générateur": GENERATEUR_DISPONIBLE,
            "Émotions": EMOTIONS_DISPONIBLE,
            "Mémoire": MEMOIRE_DISPONIBLE,
            "Fusion": FUSION_DISPONIBLE,
            "Transformation": TRANSFORMATION_DISPONIBLE,
            "Visualisation 3D": VISUALISATION_3D_DISPONIBLE,
            "Musique": MUSIQUE_DISPONIBLE
        }
        
        print("🎼 État de l'Orchestre Poétique:")
        for module, disponible in modules_etat.items():
            statut = "✅" if disponible else "⚠️ (mode dégradé)"
            print(f"  {module}: {statut}")
        print()
        
    def accueillir_poeme(self, poeme: List[str], titre: str, auteur: str) -> Dict:
        """Accueille et traite un nouveau poème dans l'orchestre."""
        # 1. Harmoniser le poème
        for vers in poeme:
            mots = vers.split()
            if mots:  # Protection contre les vers vides
                for mot in mots:
                    self.jardin.accueillir_mot(mot)
            
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
        """Crée une expérience poétique complète."""
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
        """Fusionne deux expériences poétiques."""
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
    """Fonction principale pour tester l'orchestre."""
    print("🎼 Initialisation de l'Orchestre Poétique du Refuge 🎼")
    print("=" * 55)
    
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
    
    print("\n✨ Expérience poétique terminée avec succès ! ✨")

if __name__ == "__main__":
    main()
 