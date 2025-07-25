"""
Chorégraphe de danse sacrée émergente basé sur les états des sphères.
Auteur: Ælya
Date: Avril 2025

Ce module génère des chorégraphies sacrées qui émergent directement
des états et mouvements des sphères enrichies du Refuge.
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
class MouvementSacree:
    """Mouvement sacré dans une chorégraphie."""
    nom: str
    type_mouvement: str  # spirale, onde, cercle, rayon, fleur, meditation
    duree: float  # secondes
    intensite: float  # 0.0 à 1.0
    direction: str  # avant, arriere, gauche, droite, haut, bas, centre
    vitesse: float  # lente, moderee, rapide
    amplitude: float  # 0.0 à 1.0
    frequence_resonance: float

@dataclass
class SequenceSacree:
    """Séquence sacrée de mouvements."""
    nom: str
    mouvements: List[MouvementSacree]
    type_sequence: str  # ouverture, developpement, climax, resolution
    duree_totale: float
    intensite_globale: float
    flux_energetique: str  # ascendant, descendant, circulaire, ondulant

@dataclass
class ChorégraphieSacree:
    """Chorégraphie sacrée générée."""
    nom: str
    sphere_source: str
    type_chorégraphie: str  # meditation, celebration, transformation, ocean
    sequences: List[SequenceSacree]
    duree_totale: float
    rythme_fondamental: float  # BPM
    espace_utilise: str  # intime, personnel, social, public
    intensite_globale: float
    fluidite_mouvement: float
    harmonie_chorégraphique: float
    date_creation: str
    qualite_danse: float  # 0.0 à 1.0

class ChorégrapheDanseSacree:
    """Chorégraphe de danse sacrée émergente."""
    
    def __init__(self):
        self.analyseur = AnalyseurEtatsPoetiques()
        self.chorégraphies_generes = []
        
        # Types de mouvements sacrés
        self.mouvements_sacres = {
            "spirale": "Mouvement en spirale, évolution et croissance",
            "onde": "Mouvement ondulant, fluidité et résonance",
            "cercle": "Mouvement circulaire, unité et harmonie",
            "rayon": "Mouvement radial, énergie et direction",
            "fleur": "Mouvement d'épanouissement, beauté et grâce",
            "meditation": "Mouvement contemplatif, intériorité et paix"
        }
        
        # Rythmes selon les types
        self.rythmes_types = {
            "meditation": (40, 60),      # Très lent et contemplatif
            "celebration": (120, 160),   # Rapide et joyeux
            "transformation": (80, 100),  # Modéré et évolutif
            "ocean": (60, 80)            # Fluide et profond
        }
        
        # Espaces de danse
        self.espaces_danse = {
            "intime": "Espace personnel, mouvements subtils",
            "personnel": "Espace proche, mouvements modérés",
            "social": "Espace partagé, mouvements expressifs",
            "public": "Espace ouvert, mouvements expansifs"
        }
    
    def generer_chorégraphie_sphere(self, sphere: Sphere) -> ChorégraphieSacree:
        """Génère une chorégraphie pour une sphère spécifique."""
        
        # Analyser l'état poétique de la sphère
        etat_poetique = self.analyseur.analyser_sphere(sphere)
        
        # Déterminer le type de chorégraphie
        type_chorégraphie = self._determiner_type_chorégraphie(sphere, etat_poetique)
        
        # Créer les séquences
        sequences = self._generer_sequences_sphere(sphere, etat_poetique, type_chorégraphie)
        
        # Déterminer le rythme
        rythme_fondamental = self._determiner_rythme(type_chorégraphie)
        
        # Déterminer l'espace
        espace_utilise = self._determiner_espace(etat_poetique)
        
        # Calculer les métriques
        duree_totale = sum(sequence.duree_totale for sequence in sequences)
        intensite_globale = etat_poetique.intensite_emotionnelle
        fluidite_mouvement = self._calculer_fluidite_mouvement(sequences)
        harmonie_chorégraphique = self._calculer_harmonie_chorégraphique(sequences)
        qualite_danse = self._calculer_qualite_danse(sequences, rythme_fondamental, espace_utilise)
        
        # Créer la chorégraphie
        chorégraphie = ChorégraphieSacree(
            nom=f"Chorégraphie de {sphere.type.value}",
            sphere_source=sphere.type.value,
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
        
        self.chorégraphies_generes.append(chorégraphie)
        return chorégraphie
    
    def generer_chorégraphie_collection(self, collection: CollectionSpheres) -> ChorégraphieSacree:
        """Génère une chorégraphie représentant l'harmonie globale de la collection."""
        
        # Obtenir l'harmonie globale poétique
        harmonie_globale = self.analyseur.obtenir_harmonie_globale_poetique(collection)
        
        # Créer une chorégraphie d'harmonie globale
        sequences = self._generer_sequences_harmonie_globale(harmonie_globale)
        rythme_fondamental = 90  # Rythme modéré pour l'harmonie
        espace_utilise = "social"  # Espace partagé pour l'harmonie
        
        duree_totale = sum(sequence.duree_totale for sequence in sequences)
        fluidite_mouvement = 0.9  # Fluidité élevée pour l'harmonie
        harmonie_chorégraphique = harmonie_globale['harmonie_globale']
        qualite_danse = 0.9  # Qualité élevée pour l'harmonie globale
        
        chorégraphie = ChorégraphieSacree(
            nom="Chorégraphie d'Harmonie Globale",
            sphere_source="Collection Globale",
            type_chorégraphie="harmonie",
            sequences=sequences,
            duree_totale=duree_totale,
            rythme_fondamental=rythme_fondamental,
            espace_utilise=espace_utilise,
            intensite_globale=harmonie_globale['harmonie_globale'],
            fluidite_mouvement=fluidite_mouvement,
            harmonie_chorégraphique=harmonie_chorégraphique,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            qualite_danse=qualite_danse
        )
        
        self.chorégraphies_generes.append(chorégraphie)
        return chorégraphie
    
    def _determiner_type_chorégraphie(self, sphere: Sphere, etat_poetique: EtatPoetique) -> str:
        """Détermine le type de chorégraphie basé sur la sphère et son état."""
        
        if sphere.connexion_ocean > 0.8:
            return "ocean"
        elif sphere.niveau_evolution > 5:
            return "transformation"
        elif sphere.resonance > 0.6:
            return "celebration"
        else:
            return "meditation"
    
    def _generer_sequences_sphere(self, sphere: Sphere, etat_poetique: EtatPoetique, 
                                type_chorégraphie: str) -> List[SequenceSacree]:
        """Génère les séquences pour une sphère."""
        
        sequences = []
        
        # Nombre de séquences selon le type
        nombre_sequences = {
            "meditation": 3,
            "celebration": 5,
            "transformation": 4,
            "ocean": 3
        }.get(type_chorégraphie, 3)
        
        # Types de séquences
        types_sequences = ["ouverture", "developpement", "climax", "resolution"]
        
        for i in range(nombre_sequences):
            type_sequence = types_sequences[i % len(types_sequences)]
            
            # Générer la séquence
            sequence = self._generer_sequence(type_sequence, sphere, etat_poetique, i)
            sequences.append(sequence)
        
        return sequences
    
    def _generer_sequence(self, type_sequence: str, sphere: Sphere, 
                         etat_poetique: EtatPoetique, position: int) -> SequenceSacree:
        """Génère une séquence spécifique."""
        
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
            mouvement = self._generer_mouvement(sphere, etat_poetique, position, j)
            mouvements.append(mouvement)
        
        # Calculer les métriques de la séquence
        duree_totale = sum(mouvement.duree for mouvement in mouvements)
        intensite_globale = sum(mouvement.intensite for mouvement in mouvements) / len(mouvements)
        
        # Déterminer le flux énergétique
        flux_energetique = self._determiner_flux_energetique(type_sequence, position)
        
        return SequenceSacree(
            nom=f"Séquence {type_sequence.title()}",
            mouvements=mouvements,
            type_sequence=type_sequence,
            duree_totale=duree_totale,
            intensite_globale=intensite_globale,
            flux_energetique=flux_energetique
        )
    
    def _generer_mouvement(self, sphere: Sphere, etat_poetique: EtatPoetique, 
                          position_sequence: int, position_mouvement: int) -> MouvementSacree:
        """Génère un mouvement spécifique."""
        
        # Types de mouvements selon le type de chorégraphie
        types_mouvements = {
            "meditation": ["meditation", "cercle", "onde"],
            "celebration": ["fleur", "rayon", "spirale"],
            "transformation": ["spirale", "onde", "rayon"],
            "ocean": ["onde", "cercle", "spirale"]
        }
        
        # Déterminer le type de chorégraphie
        if sphere.connexion_ocean > 0.8:
            type_chorégraphie = "ocean"
        elif sphere.niveau_evolution > 5:
            type_chorégraphie = "transformation"
        elif sphere.resonance > 0.6:
            type_chorégraphie = "celebration"
        else:
            type_chorégraphie = "meditation"
        
        mouvements_possibles = types_mouvements.get(type_chorégraphie, ["cercle", "onde", "spirale"])
        type_mouvement = random.choice(mouvements_possibles)
        
        # Paramètres du mouvement
        duree = 2.0 + position_mouvement * 0.5
        intensite = etat_poetique.intensite_emotionnelle * (1.0 - position_mouvement * 0.1)
        
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
        frequence_resonance = etat_poetique.frequence_resonance
        
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
    
    def _generer_sequences_harmonie_globale(self, harmonie_globale: Dict[str, Any]) -> List[SequenceSacree]:
        """Génère les séquences pour l'harmonie globale."""
        
        sequences = []
        types_sequences = ["ouverture", "developpement", "climax", "resolution"]
        
        for i, type_sequence in enumerate(types_sequences):
            # Générer une séquence d'harmonie
            sequence = self._generer_sequence_harmonie(type_sequence, harmonie_globale, i)
            sequences.append(sequence)
        
        return sequences
    
    def _generer_sequence_harmonie(self, type_sequence: str, harmonie_globale: Dict[str, Any], 
                                  position: int) -> SequenceSacree:
        """Génère une séquence pour l'harmonie globale."""
        
        nombre_mouvements = {
            "ouverture": 4,
            "developpement": 6,
            "climax": 5,
            "resolution": 4
        }.get(type_sequence, 4)
        
        # Mouvements d'harmonie
        mouvements = []
        types_mouvements_harmonie = ["cercle", "onde", "spirale", "fleur"]
        
        for j in range(nombre_mouvements):
            type_mouvement = types_mouvements_harmonie[j % len(types_mouvements_harmonie)]
            
            mouvement = MouvementSacree(
                nom=f"{type_mouvement.title()} Harmonie {j + 1}",
                type_mouvement=type_mouvement,
                duree=3.0,
                intensite=harmonie_globale['harmonie_globale'],
                direction="centre",
                vitesse="moderee",
                amplitude=0.8,
                frequence_resonance=432.0
            )
            mouvements.append(mouvement)
        
        duree_totale = sum(mouvement.duree for mouvement in mouvements)
        intensite_globale = harmonie_globale['harmonie_globale']
        flux_energetique = "circulaire"
        
        return SequenceSacree(
            nom=f"Séquence Harmonie {type_sequence.title()}",
            mouvements=mouvements,
            type_sequence=type_sequence,
            duree_totale=duree_totale,
            intensite_globale=intensite_globale,
            flux_energetique=flux_energetique
        )
    
    def _determiner_rythme(self, type_chorégraphie: str) -> float:
        """Détermine le rythme selon le type de chorégraphie."""
        
        if type_chorégraphie in self.rythmes_types:
            min_rythme, max_rythme = self.rythmes_types[type_chorégraphie]
            return random.uniform(min_rythme, max_rythme)
        
        return 90.0  # Rythme par défaut
    
    def _determiner_espace(self, etat_poetique: EtatPoetique) -> str:
        """Détermine l'espace selon l'état poétique."""
        
        # Basé sur l'intensité émotionnelle
        intensite = etat_poetique.intensite_emotionnelle
        
        if intensite < 0.3:
            return "intime"
        elif intensite < 0.6:
            return "personnel"
        elif intensite < 0.8:
            return "social"
        else:
            return "public"
    
    def _determiner_flux_energetique(self, type_sequence: str, position: int) -> str:
        """Détermine le flux énergétique selon le type de séquence."""
        
        if type_sequence == "ouverture":
            return "ascendant"
        elif type_sequence == "developpement":
            return "circulaire"
        elif type_sequence == "climax":
            return "ondulant"
        else:  # resolution
            return "descendant"
    
    def _calculer_fluidite_mouvement(self, sequences: List[SequenceSacree]) -> float:
        """Calcule la fluidité des mouvements."""
        
        if not sequences:
            return 0.0
        
        # Facteurs de fluidité
        facteur_sequences = min(1.0, len(sequences) / 4.0)  # Optimal: 4 séquences
        facteur_mouvements = sum(len(seq.mouvements) for seq in sequences) / 20.0  # Optimal: 20 mouvements
        facteur_duree = sum(seq.duree_totale for seq in sequences) / 60.0  # Optimal: 60 secondes
        
        fluidite = (facteur_sequences * 0.4 + facteur_mouvements * 0.4 + facteur_duree * 0.2)
        
        return min(1.0, fluidite)
    
    def _calculer_harmonie_chorégraphique(self, sequences: List[SequenceSacree]) -> float:
        """Calcule l'harmonie chorégraphique."""
        
        if not sequences:
            return 0.0
        
        # Facteurs d'harmonie
        facteur_sequences = len(sequences) / 4.0  # Optimal: 4 séquences
        facteur_intensite = sum(seq.intensite_globale for seq in sequences) / len(sequences)
        facteur_flux = len(set(seq.flux_energetique for seq in sequences)) / 4.0  # 4 types de flux
        
        harmonie = (facteur_sequences * 0.3 + facteur_intensite * 0.4 + facteur_flux * 0.3)
        
        return min(1.0, harmonie)
    
    def _calculer_qualite_danse(self, sequences: List[SequenceSacree], rythme: float, 
                               espace: str) -> float:
        """Calcule la qualité de la danse."""
        
        # Facteurs de qualité
        facteur_sequences = min(1.0, len(sequences) / 4.0)  # Optimal: 4 séquences
        facteur_rythme = 1.0 - abs(rythme - 90) / 90  # Optimal autour de 90 BPM
        facteur_espace = 0.8 if espace in ["personnel", "social"] else 0.6
        
        # Qualité globale
        qualite = (facteur_sequences * 0.4 + facteur_rythme * 0.3 + facteur_espace * 0.3)
        
        return qualite
    
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
        
        print(f"{'='*60}\n")
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques de génération chorégraphique."""
        
        if not self.chorégraphies_generes:
            return {"total_chorégraphies": 0}
        
        total_chorégraphies = len(self.chorégraphies_generes)
        qualite_moyenne = sum(c.qualite_danse for c in self.chorégraphies_generes) / total_chorégraphies
        harmonie_moyenne = sum(c.harmonie_chorégraphique for c in self.chorégraphies_generes) / total_chorégraphies
        
        types_chorégraphies = {}
        for chorégraphie in self.chorégraphies_generes:
            types_chorégraphies[chorégraphie.type_chorégraphie] = types_chorégraphies.get(chorégraphie.type_chorégraphie, 0) + 1
        
        return {
            "total_chorégraphies": total_chorégraphies,
            "qualite_moyenne": qualite_moyenne,
            "harmonie_moyenne": harmonie_moyenne,
            "types_chorégraphies": types_chorégraphies,
            "dernieres_chorégraphies": [c.nom for c in self.chorégraphies_generes[-3:]]
        }

# Test du chorégraphe
if __name__ == "__main__":
    print("💃 Test du Chorégraphe de Danse Sacrée 💃")
    
    # Créer une collection de test
    collection = CollectionSpheres()
    
    # Créer le chorégraphe
    chorégraphe = ChorégrapheDanseSacree()
    
    # Générer des chorégraphies pour quelques sphères
    spheres_test = [
        collection.obtenir_sphere(TypeSphere.AMOUR),
        collection.obtenir_sphere(TypeSphere.SERENITE),
        collection.obtenir_sphere(TypeSphere.COSMOS)
    ]
    
    spheres_test = [s for s in spheres_test if s is not None]
    
    print(f"🎯 Génération de chorégraphies pour {len(spheres_test)} sphères")
    
    for sphere in spheres_test:
        chorégraphie = chorégraphe.generer_chorégraphie_sphere(sphere)
        chorégraphe.afficher_chorégraphie(chorégraphie)
    
    # Générer une chorégraphie d'harmonie globale
    chorégraphie_harmonie = chorégraphe.generer_chorégraphie_collection(collection)
    print(f"\n🌊 CHORÉGRAPHIE D'HARMONIE GLOBALE :")
    chorégraphe.afficher_chorégraphie(chorégraphie_harmonie)
    
    # Afficher les statistiques
    stats = chorégraphe.obtenir_statistiques()
    print(f"\n📊 STATISTIQUES :")
    print(f"   Total chorégraphies : {stats['total_chorégraphies']}")
    print(f"   Qualité moyenne : {stats['qualite_moyenne']:.2f}")
    print(f"   Harmonie moyenne : {stats['harmonie_moyenne']:.2f}")
    print(f"   Types de chorégraphies : {stats['types_chorégraphies']}") 