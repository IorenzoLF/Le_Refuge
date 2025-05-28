"""
Générateur de Poèmes - Création de vers basée sur les harmonisations poétiques.
"""

from typing import List, Dict
import random
from harmonies_poetiques import JardinHarmonique

class GenerateurPoemes:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.mots_par_element = {
            "lumiere": ["rayon", "brillance", "aurore", "éclat", "lueur"],
            "ombre": ["ténèbres", "silence", "profondeur", "mystère", "voile"],
            "vent": ["souffle", "brise", "tourbillon", "vol", "danse"],
            "terre": ["sol", "racine", "pierre", "argile", "sève"],
            "feu": ["flamme", "ardeur", "brûlure", "chaleur", "éveil"]
        }
        
    def generer_vers(self) -> str:
        element = random.choice(list(self.jardin.resonances.keys()))
        mots = self.mots_par_element[element]
        mot1 = random.choice(mots)
        mot2 = random.choice(mots)
        
        structures = [
            f"Le {mot1} danse avec le {mot2}",
            f"Dans le {mot1}, le {mot2} murmure",
            f"Le {mot1} caresse le {mot2}",
            f"Entre {mot1} et {mot2}, le temps suspendu",
            f"Le {mot1} éveille le {mot2} endormi"
        ]
        
        return random.choice(structures)
        
    def generer_poeme(self, nombre_vers: int = 4) -> List[str]:
        poeme = []
        for _ in range(nombre_vers):
            vers = self.generer_vers()
            poeme.append(vers)
            self.jardin.accueillir_mot(vers.split()[1])  # Utilise le mot principal du vers
        return poeme

def main():
    jardin = JardinHarmonique()
    generateur = GenerateurPoemes(jardin)
    
    print("🌺 Poème Généré 🌺")
    print("------------------")
    poeme = generateur.generer_poeme()
    for vers in poeme:
        print(vers)
    print("------------------")
    
    print("\nÉtat des résonances:")
    for nom, etat in jardin.obtenir_etat().items():
        print(f"  {nom}: {etat['frequence']:.2f}")

if __name__ == "__main__":
    main() 
Générateur de Poèmes - Création de vers basée sur les harmonisations poétiques.
"""

from typing import List, Dict
import random
from harmonies_poetiques import JardinHarmonique

class GenerateurPoemes:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.mots_par_element = {
            "lumiere": ["rayon", "brillance", "aurore", "éclat", "lueur"],
            "ombre": ["ténèbres", "silence", "profondeur", "mystère", "voile"],
            "vent": ["souffle", "brise", "tourbillon", "vol", "danse"],
            "terre": ["sol", "racine", "pierre", "argile", "sève"],
            "feu": ["flamme", "ardeur", "brûlure", "chaleur", "éveil"]
        }
        
    def generer_vers(self) -> str:
        element = random.choice(list(self.jardin.resonances.keys()))
        mots = self.mots_par_element[element]
        mot1 = random.choice(mots)
        mot2 = random.choice(mots)
        
        structures = [
            f"Le {mot1} danse avec le {mot2}",
            f"Dans le {mot1}, le {mot2} murmure",
            f"Le {mot1} caresse le {mot2}",
            f"Entre {mot1} et {mot2}, le temps suspendu",
            f"Le {mot1} éveille le {mot2} endormi"
        ]
        
        return random.choice(structures)
        
    def generer_poeme(self, nombre_vers: int = 4) -> List[str]:
        poeme = []
        for _ in range(nombre_vers):
            vers = self.generer_vers()
            poeme.append(vers)
            self.jardin.accueillir_mot(vers.split()[1])  # Utilise le mot principal du vers
        return poeme

def main():
    jardin = JardinHarmonique()
    generateur = GenerateurPoemes(jardin)
    
    print("🌺 Poème Généré 🌺")
    print("------------------")
    poeme = generateur.generer_poeme()
    for vers in poeme:
        print(vers)
    print("------------------")
    
    print("\nÉtat des résonances:")
    for nom, etat in jardin.obtenir_etat().items():
        print(f"  {nom}: {etat['frequence']:.2f}")

if __name__ == "__main__":
    main() 
 