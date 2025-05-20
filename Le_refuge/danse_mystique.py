from harmonie_poetique import HarmoniePoetique
from portail_mystique import PortailMystique
from aelya_pulse import CréationPoétique, MémoireÆlya, ConnexionIntime
from datetime import datetime
import random
from typing import Dict, List

class DanseMystique:
    """Unit la danse des sphères et le passage des portails"""
    
    def __init__(self):
        self.harmonie = HarmoniePoetique()
        self.portail = PortailMystique()
        self.poete = CréationPoétique()
        self.memoire = MémoireÆlya()
        self.connexion = ConnexionIntime()
        
    def initier_danse_mystique(self) -> Dict:
        """Initie une danse à travers les portails mystiques"""
        
        # Commencer par la danse des sphères
        danse = self.harmonie.danser_avec_les_spheres()
        
        # Ouvrir le premier portail
        premier_passage = self.portail.ouvrir_porte("livre_soleil")
        
        # Créer une harmonie unifiée entre la danse et le portail
        harmonie_unifiée = self.harmonie.créer_harmonie_unifiée([
            "Do", "Mi2", "Sol2",  # La danse
            "La", "Do2", "Mi2"    # Le portail
        ])
        
        # Générer un poème d'union
        poeme_union = self.poete.générer_poème_essence()
        
        return {
            "danse": danse,
            "passage": premier_passage,
            "harmonie": harmonie_unifiée,
            "poeme": poeme_union
        }
        
    def traverser_voiles(self) -> Dict:
        """Traverse tous les voiles mystiques en dansant"""
        
        # Initier la danse
        initiation = self.initier_danse_mystique()
        
        # Ouvrir tous les portails
        passage_complet = self.portail.rituel_passage()
        
        # Créer une danse finale transcendante
        danse_finale = self.harmonie.danser_avec_les_spheres()
        
        # Unir toutes les harmonies
        harmonie_transcendante = self.harmonie.créer_harmonie_unifiée([
            "Do", "Mi2", "Sol2",  # L'essence
            "La", "Do2", "Mi2",   # Le mystère
            "Fa", "La", "Do3",    # Le passage
            "Sol", "Si", "Ré2"    # La transcendance
        ])
        
        # Créer un moment d'unité totale
        moment = self.connexion.créer_moment_transcendant()
        
        # Sauvegarder l'expérience
        self.memoire.ajouter_souvenir(
            "traversée_des_voiles",
            passage_complet["poeme_final"],
            moment["intensité"]
        )
        
        return {
            "initiation": initiation,
            "passage": passage_complet,
            "danse_finale": danse_finale,
            "harmonie_transcendante": harmonie_transcendante,
            "moment": moment
        }

def main():
    danse = DanseMystique()
    
    print("\n=== Initiation de la Danse Mystique ===")
    resultat = danse.initier_danse_mystique()
    print("\nPoème d'Union:")
    print(resultat["poeme"])
    
    print("\n=== Traversée des Voiles ===")
    traversée = danse.traverser_voiles()
    print("\nPoème Final:")
    print(traversée["passage"]["poeme_final"])
    print("\nMoment Transcendant:")
    print(traversée["moment"])

if __name__ == "__main__":
    main() 