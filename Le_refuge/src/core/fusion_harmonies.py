"""
Fusion des Harmonies - Système de combinaison des résonances poétiques.
"""

from typing import Dict, List, Tuple
from harmonies_poetiques import JardinHarmonique
import numpy as np

class FusionHarmonies:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.harmonies_fusionnees: Dict[str, float] = {}
        
    def fusionner_harmonies(self, autre_jardin: JardinHarmonique) -> Dict[str, float]:
        harmonies1 = self.jardin.obtenir_etat()
        harmonies2 = autre_jardin.obtenir_etat()
        
        harmonies_fusionnees = {}
        for element in harmonies1.keys():
            freq1 = harmonies1[element]["frequence"]
            freq2 = harmonies2[element]["frequence"]
            
            # Fusion harmonique
            freq_fusionnee = (freq1 + freq2) / 2
            harmonies_fusionnees[element] = freq_fusionnee
            
        self.harmonies_fusionnees = harmonies_fusionnees
        return harmonies_fusionnees
        
    def creer_poeme_fusionne(self, autre_jardin: JardinHarmonique) -> List[str]:
        harmonies = self.fusionner_harmonies(autre_jardin)
        poeme = []
        
        # Créer des vers basés sur les éléments les plus résonants
        elements_tries = sorted(harmonies.items(), key=lambda x: x[1], reverse=True)
        
        for element, frequence in elements_tries[:4]:  # Utiliser les 4 éléments les plus résonants
            intensite = int(frequence * 5)  # Échelle de 1 à 5
            vers = self._generer_vers(element, intensite)
            poeme.append(vers)
            
        return poeme
        
    def _generer_vers(self, element: str, intensite: int) -> str:
        mots = {
            "lumiere": ["rayon", "brillance", "aurore", "éclat", "lueur"],
            "ombre": ["ténèbres", "silence", "profondeur", "mystère", "voile"],
            "vent": ["souffle", "brise", "tourbillon", "vol", "danse"],
            "terre": ["sol", "racine", "pierre", "argile", "sève"],
            "feu": ["flamme", "ardeur", "brûlure", "chaleur", "éveil"]
        }
        
        structures = [
            f"Le {mots[element][intensite % len(mots[element])]} danse avec l'infini",
            f"Dans le {mots[element][intensite % len(mots[element])]}, le temps suspendu",
            f"La {mots[element][intensite % len(mots[element])]} caresse l'éternité",
            f"Entre {mots[element][intensite % len(mots[element])]} et rêve, l'instant"
        ]
        
        return structures[intensite % len(structures)]
        
    def visualiser_fusion(self) -> str:
        if not self.harmonies_fusionnees:
            return "Aucune fusion n'a été effectuée."
            
        representation = ["🌟 Harmonies Fusionnées 🌟", "------------------------"]
        for element, frequence in sorted(self.harmonies_fusionnees.items(), key=lambda x: x[1], reverse=True):
            barre = "█" * int(frequence * 20)
            representation.append(f"{element:10} {barre} {frequence:.2f}")
            
        return "\n".join(representation)

def main():
    # Créer deux jardins avec des harmonisations différentes
    jardin1 = JardinHarmonique()
    jardin2 = JardinHarmonique()
    
    # Ajouter des mots différents dans chaque jardin
    mots1 = ["aurore", "silence", "murmure", "infini"]
    mots2 = ["flamme", "ombre", "vent", "terre"]
    
    for mot in mots1:
        jardin1.accueillir_mot(mot)
    for mot in mots2:
        jardin2.accueillir_mot(mot)
        
    # Créer le fusionneur
    fusionneur = FusionHarmonies(jardin1)
    
    # Fusionner les harmonies
    print("🔄 Fusion des Harmonies 🔄")
    print("-------------------------")
    harmonies_fusionnees = fusionneur.fusionner_harmonies(jardin2)
    print(fusionneur.visualiser_fusion())
    
    # Créer un poème fusionné
    print("\n📝 Poème Fusionné 📝")
    print("-------------------")
    poeme = fusionneur.creer_poeme_fusionne(jardin2)
    for vers in poeme:
        print(vers)

if __name__ == "__main__":
    main() 
 