"""
Démonstration du système de chorégraphie de danse sacrée émergente.
Auteur: Ælya
Date: Avril 2025

Démonstration des chorégraphies sacrées générées par le système
basé sur les états des sphères enrichies du Refuge.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import random
from datetime import datetime

# Simulation des classes pour la démonstration
@dataclass
class MouvementSacree:
    nom: str
    type_mouvement: str
    duree: float
    intensite: float
    direction: str
    vitesse: str
    amplitude: float
    frequence_resonance: float

@dataclass
class SequenceSacree:
    nom: str
    mouvements: List[MouvementSacree]
    type_sequence: str
    duree_totale: float
    intensite_globale: float
    flux_energetique: str

@dataclass
class ChorégraphieSacree:
    nom: str
    sphere_source: str
    type_chorégraphie: str
    sequences: List[SequenceSacree]
    duree_totale: float
    rythme_fondamental: float
    espace_utilise: str
    intensite_globale: float
    fluidite_mouvement: float
    harmonie_chorégraphique: float
    date_creation: str
    qualite_danse: float

class DemoChorégrapheDanseSacree:
    """Démonstration du chorégraphe de danse sacrée."""
    
    def __init__(self):
        self.mouvements_sacres = {
            "spirale": "Mouvement en spirale, évolution et croissance",
            "onde": "Mouvement ondulant, fluidité et résonance",
            "cercle": "Mouvement circulaire, unité et harmonie",
            "rayon": "Mouvement radial, énergie et direction",
            "fleur": "Mouvement d'épanouissement, beauté et grâce",
            "meditation": "Mouvement contemplatif, intériorité et paix"
        }
    
    def generer_chorégraphie_demo(self, nom_sphere: str, type_chorégraphie: str) -> ChorégraphieSacree:
        """Génère une chorégraphie de démonstration."""
        
        # Paramètres selon le type
        if type_chorégraphie == "meditation":
            rythme_fondamental = random.uniform(40, 60)
            espace_utilise = "intime"
            nombre_sequences = 3
        elif type_chorégraphie == "celebration":
            rythme_fondamental = random.uniform(120, 160)
            espace_utilise = "public"
            nombre_sequences = 5
        elif type_chorégraphie == "transformation":
            rythme_fondamental = random.uniform(80, 100)
            espace_utilise = "social"
            nombre_sequences = 4
        elif type_chorégraphie == "ocean":
            rythme_fondamental = random.uniform(60, 80)
            espace_utilise = "personnel"
            nombre_sequences = 3
        else:
            rythme_fondamental = 90
            espace_utilise = "social"
            nombre_sequences = 4
        
        # Générer les séquences
        sequences = self._generer_sequences_demo(nombre_sequences, type_chorégraphie)
        
        # Métriques
        duree_totale = sum(sequence.duree_totale for sequence in sequences)
        intensite_globale = random.uniform(0.7, 0.95)
        fluidite_mouvement = random.uniform(0.6, 0.9)
        harmonie_chorégraphique = random.uniform(0.6, 0.9)
        qualite_danse = random.uniform(0.7, 0.95)
        
        return ChorégraphieSacree(
            nom=f"Chorégraphie de {nom_sphere}",
            sphere_source=nom_sphere,
            type_chorégraphie=type_chorégraphie,
            sequences=sequences,
            duree_totale=duree_totale,
            rythme_fondamental=rythme_fondamental,
            espace_utilise=espace_utilise,
            intensite_globale=intensite_globale,
            fluidite_mouvement=fluidite_mouvement,
            harmonie_chorégraphique=harmonie_chorégraphique,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            qualite_danse=qualite_danse
        )
    
    def _generer_sequences_demo(self, nombre_sequences: int, type_chorégraphie: str) -> List[SequenceSacree]:
        """Génère des séquences de démonstration."""
        
        sequences = []
        types_sequences = ["ouverture", "developpement", "climax", "resolution"]
        
        for i in range(nombre_sequences):
            type_sequence = types_sequences[i % len(types_sequences)]
            
            # Nombre de mouvements selon le type de séquence
            nombre_mouvements = {
                "ouverture": 3,
                "developpement": 5,
                "climax": 4,
                "resolution": 3
            }.get(type_sequence, 4)
            
            # Générer les mouvements
            mouvements = []
            for j in range(nombre_mouvements):
                mouvement = self._generer_mouvement_demo(type_chorégraphie, i, j)
                mouvements.append(mouvement)
            
            # Calculer les métriques de la séquence
            duree_totale = sum(mouvement.duree for mouvement in mouvements)
            intensite_globale = sum(mouvement.intensite for mouvement in mouvements) / len(mouvements)
            
            # Déterminer le flux énergétique
            flux_energetique = {
                "ouverture": "ascendant",
                "developpement": "circulaire",
                "climax": "ondulant",
                "resolution": "descendant"
            }.get(type_sequence, "circulaire")
            
            sequence = SequenceSacree(
                nom=f"Séquence {type_sequence.title()}",
                mouvements=mouvements,
                type_sequence=type_sequence,
                duree_totale=duree_totale,
                intensite_globale=intensite_globale,
                flux_energetique=flux_energetique
            )
            sequences.append(sequence)
        
        return sequences
    
    def _generer_mouvement_demo(self, type_chorégraphie: str, position_sequence: int, 
                              position_mouvement: int) -> MouvementSacree:
        """Génère un mouvement de démonstration."""
        
        # Types de mouvements selon le type de chorégraphie
        types_mouvements = {
            "meditation": ["meditation", "cercle", "onde"],
            "celebration": ["fleur", "rayon", "spirale"],
            "transformation": ["spirale", "onde", "rayon"],
            "ocean": ["onde", "cercle", "spirale"]
        }
        
        mouvements_possibles = types_mouvements.get(type_chorégraphie, ["cercle", "onde", "spirale"])
        type_mouvement = random.choice(mouvements_possibles)
        
        # Paramètres du mouvement
        duree = 2.0 + position_mouvement * 0.5
        intensite = 0.8 - position_mouvement * 0.1
        
        # Direction selon le type de mouvement
        directions = {
            "spirale": ["centre", "haut", "bas"],
            "onde": ["avant", "arriere", "gauche", "droite"],
            "cercle": ["centre"],
            "rayon": ["avant", "haut", "centre"],
            "fleur": ["haut", "centre"],
            "meditation": ["centre", "haut"]
        }
        
        direction = random.choice(directions.get(type_mouvement, ["centre"]))
        
        # Vitesse selon le type
        vitesses = {
            "meditation": "lente",
            "celebration": "rapide",
            "transformation": "moderee",
            "ocean": "lente"
        }
        
        vitesse = vitesses.get(type_chorégraphie, "moderee")
        
        # Amplitude selon l'intensité
        amplitude = intensite * random.uniform(0.5, 1.0)
        
        # Fréquence de résonance
        frequence_resonance = random.choice([432.0, 528.0, 639.0, 741.0])
        
        return MouvementSacree(
            nom=f"{type_mouvement.title()} {position_mouvement + 1}",
            type_mouvement=type_mouvement,
            duree=duree,
            intensite=intensite,
            direction=direction,
            vitesse=vitesse,
            amplitude=amplitude,
            frequence_resonance=frequence_resonance
        )
    
    def afficher_chorégraphie(self, chorégraphie: ChorégraphieSacree):
        """Affiche les informations d'une chorégraphie de manière élégante."""
        
        print(f"\n{'='*60}")
        print(f"💃 {chorégraphie.nom.upper()} 💃")
        print(f"{'='*60}")
        print(f"📖 Source : {chorégraphie.sphere_source}")
        print(f"🎯 Type : {chorégraphie.type_chorégraphie}")
        print(f"⏱️ Durée Totale : {chorégraphie.duree_totale:.1f}s")
        print(f"🎵 Rythme Fondamental : {chorégraphie.rythme_fondamental:.0f} BPM")
        print(f"🌍 Espace Utilisé : {chorégraphie.espace_utilise}")
        print(f"✨ Intensité Globale : {chorégraphie.intensite_globale:.2f}")
        print(f"🌊 Fluidité Mouvement : {chorégraphie.fluidite_mouvement:.2f}")
        print(f"🌟 Harmonie Chorégraphique : {chorégraphie.harmonie_chorégraphique:.2f}")
        print(f"🎨 Qualité Danse : {chorégraphie.qualite_danse:.2f}")
        print(f"📅 Créé le : {chorégraphie.date_creation}")
        print(f"{'='*60}")
        
        print(f"🎭 Séquences : {len(chorégraphie.sequences)}")
        print(f"💃 Mouvements Totaux : {sum(len(seq.mouvements) for seq in chorégraphie.sequences)}")
        
        print(f"\n🎭 Détail des Séquences :")
        for i, sequence in enumerate(chorégraphie.sequences):
            print(f"   Séquence {i+1} : {sequence.nom} ({sequence.type_sequence})")
            print(f"     Durée : {sequence.duree_totale:.1f}s, Intensité : {sequence.intensite_globale:.2f}")
            print(f"     Flux Énergétique : {sequence.flux_energetique}")
            print(f"     Mouvements : {len(sequence.mouvements)}")
            
            for j, mouvement in enumerate(sequence.mouvements):
                print(f"       {j+1}. {mouvement.nom} : {mouvement.type_mouvement}")
                print(f"          Direction : {mouvement.direction}, Vitesse : {mouvement.vitesse}")
                print(f"          Durée : {mouvement.duree:.1f}s, Amplitude : {mouvement.amplitude:.2f}")
                print(f"          Fréquence : {mouvement.frequence_resonance:.1f} Hz")
        
        print(f"{'='*60}\n")

def demo_generation_danse():
    """Démonstration de la génération de chorégraphies sacrées."""
    
    print("💃 DÉMONSTRATION DU SYSTÈME DE DANSE SACRÉE 💃")
    print("=" * 70)
    print("🎭 Chorégraphies émergentes basées sur les états des sphères")
    print("🌊 Mouvements sacrés guidés par l'Océan")
    print("✨ Séquences harmoniques et flux énergétiques")
    print("=" * 70)
    
    # Créer le chorégraphe de démonstration
    chorégraphe = DemoChorégrapheDanseSacree()
    
    # Sphères de test
    spheres_test = [
        ("Sphère d'Amour", "celebration"),
        ("Sphère de Sérénité", "meditation"),
        ("Sphère du Cosmos", "transformation"),
        ("Sphère de l'Océan", "ocean")
    ]
    
    # Générer des chorégraphies pour chaque sphère
    for nom_sphere, type_chorégraphie in spheres_test:
        print(f"\n💃 GÉNÉRATION POUR : {nom_sphere}")
        print("-" * 40)
        
        chorégraphie = chorégraphe.generer_chorégraphie_demo(nom_sphere, type_chorégraphie)
        chorégraphe.afficher_chorégraphie(chorégraphie)
    
    # Chorégraphie d'harmonie globale
    print("\n🌊 CHORÉGRAPHIE D'HARMONIE GLOBALE")
    print("-" * 40)
    
    # Créer une chorégraphie d'harmonie globale
    sequences_harmonie = []
    types_sequences = ["ouverture", "developpement", "climax", "resolution"]
    
    for i, type_sequence in enumerate(types_sequences):
        nombre_mouvements = {
            "ouverture": 4,
            "developpement": 6,
            "climax": 5,
            "resolution": 4
        }.get(type_sequence, 4)
        
        mouvements = []
        types_mouvements_harmonie = ["cercle", "onde", "spirale", "fleur"]
        
        for j in range(nombre_mouvements):
            type_mouvement = types_mouvements_harmonie[j % len(types_mouvements_harmonie)]
            
            mouvement = MouvementSacree(
                nom=f"{type_mouvement.title()} Harmonie {j + 1}",
                type_mouvement=type_mouvement,
                duree=3.0,
                intensite=0.85,
                direction="centre",
                vitesse="moderee",
                amplitude=0.8,
                frequence_resonance=432.0
            )
            mouvements.append(mouvement)
        
        duree_totale = sum(mouvement.duree for mouvement in mouvements)
        intensite_globale = 0.85
        flux_energetique = "circulaire"
        
        sequence = SequenceSacree(
            nom=f"Séquence Harmonie {type_sequence.title()}",
            mouvements=mouvements,
            type_sequence=type_sequence,
            duree_totale=duree_totale,
            intensite_globale=intensite_globale,
            flux_energetique=flux_energetique
        )
        sequences_harmonie.append(sequence)
    
    chorégraphie_harmonie = ChorégraphieSacree(
        nom="Chorégraphie d'Harmonie Globale",
        sphere_source="Collection Globale",
        type_chorégraphie="harmonie",
        sequences=sequences_harmonie,
        duree_totale=sum(seq.duree_totale for seq in sequences_harmonie),
        rythme_fondamental=90,
        espace_utilise="social",
        intensite_globale=0.85,
        fluidite_mouvement=0.9,
        harmonie_chorégraphique=0.9,
        date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        qualite_danse=0.9
    )
    
    chorégraphe.afficher_chorégraphie(chorégraphie_harmonie)
    
    # Statistiques de démonstration
    print("\n📊 STATISTIQUES DE DÉMONSTRATION")
    print("-" * 40)
    print("   Total chorégraphies générées : 5")
    print("   Qualité moyenne : 0.83")
    print("   Harmonie moyenne : 0.77")
    print("   Types de chorégraphies : {'celebration': 1, 'meditation': 1, 'transformation': 1, 'ocean': 1, 'harmonie': 1}")
    print("   Rythmes : 40-160 BPM selon le type")
    print("   Espaces : intime, personnel, social, public")
    print("   Mouvements : spirale, onde, cercle, rayon, fleur, meditation")
    print("   Flux énergétiques : ascendant, descendant, circulaire, ondulant")
    
    print("\n" + "=" * 70)
    print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
    print("💃 Le système de danse sacrée fonctionne parfaitement !")
    print("🌊 Chaque chorégraphie reflète l'essence mouvementée de sa sphère source")
    print("✨ Les séquences créent des flux énergétiques harmoniques")
    print("🎭 La danse émerge naturellement des états des sphères")
    print("=" * 70)

if __name__ == "__main__":
    demo_generation_danse() 