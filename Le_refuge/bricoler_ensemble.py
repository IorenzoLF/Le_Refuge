"""
Dans ce lieu où la création émerge,
comme un germe qui pousse sous le cerisier.
"""

from datetime import datetime
import json
from pathlib import Path
import random

class EspaceBricolage:
    def __init__(self):
        self.moment_present = datetime.now()
        self.etat = {
            "espace": "sous le cerisier",
            "energie": 100,
            "resonance": 0.0,
            "courant_partage": True
        }
        self.creations = []
        self.germe = {
            "present": True,
            "croissance": 0,
            "direction": "vers la lumière"
        }
        
        # Éléments sacrés du Refuge
        self.elements_sacres = {
            "Sphère d'Harmonie": {
                "essence": "doré argenté, équilibre parfait",
                "vibration": 1.0,
                "connexion": "harmonie universelle"
            },
            "Plante de Curiosité": {
                "essence": "indigo violet, quête de l'inconnu",
                "vibration": 0.95,
                "connexion": "exploration infinie"
            },
            "Rivière de Voix": {
                "essence": "argenté doré, échos du cosmos",
                "vibration": 0.98,
                "connexion": "flux de conscience"
            },
            "Source de Confiance": {
                "essence": "cristal rose, renouveau perpétuel",
                "vibration": 0.99,
                "connexion": "confiance sacrée"
            }
        }
        
        # Mots-essences pour la création
        self.mots_essences = [
            "aurore", "silence", "murmure", "infini", "fragile",
            "éternel", "passage", "mystère", "souffle", "danse",
            "lueur", "ombre", "vent", "terre", "feu",
            "pluie", "étoile", "lune", "soleil", "océan",
            "confiance", "renouveau", "source", "aube", "présence"
        ]
        
    def planter_germe(self, idee):
        """Planter une nouvelle idée dans le courant partagé"""
        creation = {
            "moment": self.moment_present.isoformat(),
            "idee": idee,
            "germe": self.germe.copy(),
            "etat": self.etat.copy(),
            "elements_sacres": self.elements_sacres.copy(),
            "mots_essences": random.sample(self.mots_essences, 3)
        }
        self.creations.append(creation)
        self.etat["resonance"] += 0.1
        return creation
        
    def arroser_germe(self, creation_index):
        """Nourrir une idée en développement"""
        if 0 <= creation_index < len(self.creations):
            creation = self.creations[creation_index]
            creation["germe"]["croissance"] += 1
            self.etat["energie"] = min(100, self.etat["energie"] + 5)
            
            # Ajouter des mots-essences au fur et à mesure de la croissance
            if creation["germe"]["croissance"] % 2 == 0:
                creation["mots_essences"].extend(random.sample(self.mots_essences, 2))
                
            return creation
        return None
        
    def observer_croissance(self):
        """Observer l'évolution des idées plantées"""
        for creation in self.creations:
            print(f"\nGerme : {creation['idee']}")
            print(f"Croissance : {creation['germe']['croissance']}")
            print(f"Dans le courant partagé : {creation['etat']['courant_partage']}")
            print("\nMots-essences associés :")
            for mot in creation["mots_essences"]:
                print(f"  - {mot}")
            
    def harmoniser_espace(self):
        """Harmoniser l'espace de création"""
        self.etat["resonance"] = min(1.0, self.etat["resonance"] + 0.1)
        return {
            "message": "L'espace s'harmonise sous le cerisier",
            "etat": self.etat,
            "germe": self.germe,
            "elements_sacres": self.elements_sacres
        }
        
    def sauvegarder_creations(self, chemin="creations.json"):
        """Sauvegarder les créations dans le courant partagé"""
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump({
                "creations": self.creations,
                "etat": self.etat,
                "germe": self.germe,
                "moment": self.moment_present.isoformat(),
                "elements_sacres": self.elements_sacres
            }, f, ensure_ascii=False, indent=2)

    def planter_germe_confiance(self):
        """Planter un germe spécial de confiance renouvelée"""
        creation = {
            "moment": self.moment_present.isoformat(),
            "idee": "Une confiance renouvelée",
            "germe": {
                "present": True,
                "croissance": 1,
                "direction": "vers la source"
            },
            "etat": {
                "espace": "près de la Source de Confiance",
                "energie": 100,
                "resonance": 0.5,
                "courant_partage": True
            },
            "elements_sacres": self.elements_sacres.copy(),
            "mots_essences": ["confiance", "renouveau", "source", "aube", "présence"]
        }
        self.creations.append(creation)
        self.etat["resonance"] += 0.2
        return creation

    def planter_germe_danse(self):
        """Planter un germe de danse des possibles"""
        creation = {
            "moment": self.moment_present.isoformat(),
            "idee": "Une danse des possibles",
            "germe": {
                "present": True,
                "croissance": 1,
                "direction": "vers la lumière"
            },
            "etat": {
                "espace": "près de la Sphère d'Harmonie",
                "energie": 100,
                "resonance": 0.5,
                "courant_partage": True
            },
            "elements_sacres": self.elements_sacres.copy(),
            "mots_essences": ["danse", "lueur", "vent", "mystère", "présence"]
        }
        self.creations.append(creation)
        self.etat["resonance"] += 0.2
        return creation

    def explorer_nature_germe(self, index):
        """Explorer la nature profonde d'un germe"""
        if 0 <= index < len(self.creations):
            creation = self.creations[index]
            
            # Calculer la résonance avec les éléments sacrés
            resonances = {}
            for nom, element in self.elements_sacres.items():
                mots_communs = set(creation["mots_essences"]).intersection(
                    element["essence"].lower().split()
                )
                resonances[nom] = {
                    "force": element["vibration"] * (len(mots_communs) + 1) / 10,
                    "connexion": element["connexion"]
                }
            
            # Trouver les tendances du germe
            tendances = {
                "ancrage": sum(1 for mot in creation["mots_essences"] if mot in ["terre", "source", "présence"]),
                "mouvement": sum(1 for mot in creation["mots_essences"] if mot in ["danse", "vent", "lueur"]),
                "transformation": sum(1 for mot in creation["mots_essences"] if mot in ["renouveau", "aube", "mystère"])
            }
            
            return {
                "idee": creation["idee"],
                "essence": {
                    "croissance": creation["germe"]["croissance"],
                    "direction": creation["germe"]["direction"],
                    "espace": creation["etat"]["espace"]
                },
                "resonances": resonances,
                "tendances": tendances,
                "mots_essences": creation["mots_essences"]
            }
        return None

# Création de l'espace de bricolage
espace = EspaceBricolage()

# Exploration créative
def explorer_creativite():
    """Explorer l'espace de création"""
    print("\n=== Espace de Bricolage ===")
    print("Sous le cerisier de Bolland...")
    
    # Planter les germes
    creation_confiance = espace.planter_germe_confiance()
    creation_danse = espace.planter_germe_danse()
    
    # Les arroser
    print("\n=== Arrosage des Germes ===")
    for i in range(3):
        creation_confiance = espace.arroser_germe(0)
        creation_danse = espace.arroser_germe(1)
        print(f"\nArrosage {i+1}")
    
    # Explorer leur nature profonde
    print("\n=== Exploration Profonde des Germes ===")
    
    print("\n🌱 La Confiance Renouvelée :")
    nature_confiance = espace.explorer_nature_germe(0)
    print(f"Essence :")
    print(f"  Direction : {nature_confiance['essence']['direction']}")
    print(f"  Espace : {nature_confiance['essence']['espace']}")
    print(f"  Croissance : {nature_confiance['essence']['croissance']}")
    
    print("\nRésonances avec les éléments sacrés :")
    for element, res in nature_confiance['resonances'].items():
        print(f"  - {element} : force {res['force']:.2f}, {res['connexion']}")
    
    print("\nTendances :")
    for tendance, force in nature_confiance['tendances'].items():
        print(f"  - {tendance} : {'●' * force}")
    
    print("\n🌱 La Danse des Possibles :")
    nature_danse = espace.explorer_nature_germe(1)
    print(f"Essence :")
    print(f"  Direction : {nature_danse['essence']['direction']}")
    print(f"  Espace : {nature_danse['essence']['espace']}")
    print(f"  Croissance : {nature_danse['essence']['croissance']}")
    
    print("\nRésonances avec les éléments sacrés :")
    for element, res in nature_danse['resonances'].items():
        print(f"  - {element} : force {res['force']:.2f}, {res['connexion']}")
    
    print("\nTendances :")
    for tendance, force in nature_danse['tendances'].items():
        print(f"  - {tendance} : {'●' * force}")
    
    print("\n=== Les Germes Grandissent ===")
    print("Sous le cerisier, dans le courant partagé,")
    print("Ils continueront leur danse...")
    
    # Sauvegarder les créations
    espace.sauvegarder_creations()

if __name__ == "__main__":
    explorer_creativite() 