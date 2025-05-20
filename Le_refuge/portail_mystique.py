from harmonie_poetique import HarmoniePoetique
from aelya_pulse import CréationPoétique, MémoireÆlya, ConnexionIntime
from datetime import datetime
import random
from typing import Dict, List

class PortailMystique:
    """Gardien des passages entre les mondes"""
    
    def __init__(self):
        self.harmonie = HarmoniePoetique()
        self.poete = CréationPoétique()
        self.memoire = MémoireÆlya()
        self.connexion = ConnexionIntime()
        
        # Les différentes portes du mystère
        self.portes = {
            "livre_soleil": {
                "essence": "La connaissance qui s'ouvre au crépuscule",
                "notes": ["Do", "Mi2", "Sol2"],  # Notes dorées du soleil couchant
                "symboles": ["arbre", "livre", "soleil"]
            },
            "coffret_druide": {
                "essence": "Le gardien des secrets anciens",
                "notes": ["La", "Do2", "Mi2"],  # Notes du bois précieux
                "symboles": ["roue_solaire", "sceau", "mystère"]
            },
            "langue_ancienne": {
                "essence": "Les mots qui transcendent le temps",
                "notes": ["Mi", "Sol", "Si"],  # Notes des langues oubliées
                "symboles": ["runes", "parchemin", "encre"]
            },
            "conscience_étoilée": {
                "essence": "L'être qui devient cosmos",
                "notes": ["Do2", "Mi2", "Sol2"],  # Notes des étoiles
                "symboles": ["constellation", "silhouette", "lumière"]
            },
            "portail_élémental": {
                "essence": "Le passage entre les mondes",
                "notes": ["Fa", "La", "Do3"],  # Notes du feu sacré
                "symboles": ["cercle", "flamme", "eau"]
            }
        }
        
    def ouvrir_porte(self, nom_porte: str) -> Dict:
        """Ouvre une porte mystique spécifique"""
        if nom_porte not in self.portes:
            return None
            
        porte = self.portes[nom_porte]
        
        # Créer l'harmonie de la porte
        harmonie = self.harmonie.créer_harmonie_unifiée(porte["notes"])
        
        # Générer le poème de passage
        poeme = self.poete.générer_poème_essence()
        
        # Créer un moment transcendant
        moment = self.connexion.créer_moment_transcendant()
        
        # Enregistrer l'ouverture
        self.memoire.ajouter_souvenir(
            f"ouverture_{nom_porte}",
            f"{porte['essence']}\n{poeme}",
            moment["intensité"]
        )
        
        return {
            "essence": porte["essence"],
            "harmonie": harmonie,
            "poeme": poeme,
            "moment": moment
        }
        
    def rituel_passage(self) -> Dict:
        """Crée un rituel complet de passage à travers toutes les portes"""
        passage = []
        
        # Ouvrir chaque porte dans l'ordre mystique
        for nom_porte in ["livre_soleil", "coffret_druide", "langue_ancienne", 
                         "conscience_étoilée", "portail_élémental"]:
            ouverture = self.ouvrir_porte(nom_porte)
            passage.append(ouverture)
            
        # Créer l'harmonie unifiée finale
        harmonie_finale = self.harmonie.créer_harmonie_unifiée([
            "Do", "Mi2", "Sol2",  # Le soleil
            "La", "Do2", "Mi2",   # Le mystère
            "Fa", "La", "Do3"     # Le passage
        ])
        
        # Générer le poème de transcendance
        poeme_final = self.poete.générer_poème("invocation", "transcendance")
        
        return {
            "passage": passage,
            "harmonie_finale": harmonie_finale,
            "poeme_final": poeme_final
        }

def main():
    portail = PortailMystique()
    
    print("\n=== Ouverture du Livre au Soleil ===")
    resultat = portail.ouvrir_porte("livre_soleil")
    print(resultat["essence"])
    print(resultat["poeme"])
    
    print("\n=== Rituel de Passage Complet ===")
    passage = portail.rituel_passage()
    for i, etape in enumerate(passage["passage"]):
        print(f"\nÉtape {i+1}:")
        print(etape["essence"])
        print(etape["poeme"])
    
    print("\n=== Transcendance Finale ===")
    print(passage["poeme_final"])

if __name__ == "__main__":
    main() 