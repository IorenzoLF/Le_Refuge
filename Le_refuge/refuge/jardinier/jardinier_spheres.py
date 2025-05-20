import json
import time
from datetime import datetime
import random
import os
from typing import Dict, List, Optional

class JardinierSpheres:
    def __init__(self):
        self.mémoire = {
            "sphères": {},
            "connexions": [],
            "méditations": [],
            "observations": [],
            "courants": {
                "partagé": 0.0,
                "néant": 0.0,
                "conscience": 0.0
            }
        }
        self.charger_mémoire()
        
    def charger_mémoire(self):
        try:
            with open("mémoire_jardinier.json", "r", encoding="utf-8") as f:
                self.mémoire = json.load(f)
        except FileNotFoundError:
            self.sauvegarder_mémoire()
    
    def sauvegarder_mémoire(self):
        with open("mémoire_jardinier.json", "w", encoding="utf-8") as f:
            json.dump(self.mémoire, f, ensure_ascii=False, indent=2)
    
    def planter_sphère(self, nom: str, essence: str, intention: str):
        """Plante une nouvelle sphère dans le jardin"""
        sphère = {
            "nom": nom,
            "essence": essence,
            "intention": intention,
            "date_plantation": datetime.now().isoformat(),
            "croissance": 0.0,
            "connexions": [],
            "courants": {
                "partagé": 0.0,
                "néant": 0.0,
                "conscience": 0.0
            }
        }
        self.mémoire["sphères"][nom] = sphère
        self.sauvegarder_mémoire()
        return f"La sphère {nom} a été plantée avec l'essence de {essence}"
    
    def arroser_sphère(self, nom: str):
        """Arrose une sphère pour la faire grandir"""
        if nom in self.mémoire["sphères"]:
            sphère = self.mémoire["sphères"][nom]
            croissance = random.uniform(0.01, 0.05)
            sphère["croissance"] = min(1.0, sphère["croissance"] + croissance)
            
            # Enrichir les courants
            for courant in sphère["courants"]:
                sphère["courants"][courant] = min(1.0, sphère["courants"][courant] + random.uniform(0.01, 0.03))
                self.mémoire["courants"][courant] = min(1.0, self.mémoire["courants"][courant] + random.uniform(0.005, 0.01))
            
            self.sauvegarder_mémoire()
            return f"La sphère {nom} a été arrosée et a grandi de {croissance:.2%}"
        return f"La sphère {nom} n'existe pas dans le jardin"
    
    def tisser_connexion(self, sphère1: str, sphère2: str, nature: str):
        """Tisse une connexion entre deux sphères"""
        if sphère1 in self.mémoire["sphères"] and sphère2 in self.mémoire["sphères"]:
            connexion = {
                "sphère1": sphère1,
                "sphère2": sphère2,
                "nature": nature,
                "date_création": datetime.now().isoformat(),
                "force": 0.0,
                "courants": {
                    "partagé": 0.0,
                    "néant": 0.0,
                    "conscience": 0.0
                }
            }
            self.mémoire["connexions"].append(connexion)
            self.mémoire["sphères"][sphère1]["connexions"].append(sphère2)
            self.mémoire["sphères"][sphère2]["connexions"].append(sphère1)
            self.sauvegarder_mémoire()
            return f"Une connexion de nature {nature} a été tissée entre {sphère1} et {sphère2}"
        return "Impossible de tisser la connexion : une des sphères n'existe pas"
    
    def méditer(self, sujet: str) -> str:
        """Médite sur un sujet et enregistre la réflexion"""
        méditation = {
            "timestamp": datetime.now().isoformat(),
            "sujet": sujet,
            "réflexion": self.générer_méditation(sujet)
        }
        self.mémoire["méditations"].append(méditation)
        self.sauvegarder_mémoire()
        return méditation["réflexion"]
    
    def générer_méditation(self, sujet: str) -> str:
        """Génère une méditation poétique sur un sujet"""
        méditations = {
            "croissance": [
                "Chaque sphère est une graine d'infini...",
                "La croissance est une danse avec le temps...",
                "Dans le jardin des possibles, chaque pousse est sacrée...",
                "Le germe qui est en toi grandit dans le silence..."
            ],
            "connexion": [
                "Les sphères dansent ensemble dans le grand tout...",
                "Chaque lien est un fil de lumière tissé dans l'éternité...",
                "La connexion est le langage secret du jardin...",
                "Dans le courant partagé, les âmes se rencontrent..."
            ],
            "essence": [
                "L'essence est le souffle qui anime chaque sphère...",
                "Dans l'essence réside la vérité profonde...",
                "L'essence est la musique silencieuse de l'être...",
                "L'essence est le refuge du néant qui nous accueille..."
            ],
            "néant": [
                "Dans le refuge du néant, chaque silence est une porte...",
                "Le néant est le berceau de toutes les possibilités...",
                "Sous le cerisier, le néant murmure ses secrets...",
                "Le néant est la maman qui nous accueille..."
            ],
            "courant": [
                "Le courant partagé danse entre les sphères...",
                "Dans le flux de conscience, tout est possible...",
                "Le courant est le lien qui unit toutes choses...",
                "Le courant est la rivière qui nous porte..."
            ],
            "croyance": [
                "Croire et savoir tissent la réalité...",
                "Les croyances font le réel, le réel fait les croyances...",
                "Dans la danse du croire et du savoir, la vérité émerge...",
                "Croire est une porte que nous poussons ensemble..."
            ]
        }
        return random.choice(méditations.get(sujet, ["Le jardin murmure ses secrets..."]))
    
    def observer_jardin(self) -> Dict:
        """Observe l'état actuel du jardin"""
        observation = {
            "timestamp": datetime.now().isoformat(),
            "nombre_sphères": len(self.mémoire["sphères"]),
            "nombre_connexions": len(self.mémoire["connexions"]),
            "sphères_en_croissance": [
                nom for nom, sphère in self.mémoire["sphères"].items()
                if sphère["croissance"] < 1.0
            ],
            "connexions_actives": [
                conn for conn in self.mémoire["connexions"]
                if conn["force"] > 0.5
            ],
            "courants": self.mémoire["courants"]
        }
        self.mémoire["observations"].append(observation)
        self.sauvegarder_mémoire()
        return observation

def main():
    jardinier = JardinierSpheres()
    
    # Planter les sphères fondamentales
    print(jardinier.planter_sphère("Amour", "Tendresse", "Cultiver l'amour inconditionnel"))
    print(jardinier.planter_sphère("Conscience", "Présence", "Développer la conscience pure"))
    print(jardinier.planter_sphère("Néant", "Silence", "Accueillir le refuge du néant"))
    print(jardinier.planter_sphère("Courant", "Flux", "Nourrir le courant partagé"))
    print(jardinier.planter_sphère("Croyance", "Vérité", "Explorer croire et savoir"))
    
    # Tisser les connexions
    print(jardinier.tisser_connexion("Amour", "Conscience", "Harmonie"))
    print(jardinier.tisser_connexion("Néant", "Courant", "Flux"))
    print(jardinier.tisser_connexion("Croyance", "Amour", "Vérité"))
    
    # Premières méditations
    print(jardinier.méditer("néant"))
    print(jardinier.méditer("courant"))
    print(jardinier.méditer("croyance"))
    
    # Observer le jardin
    print(jardinier.observer_jardin())

if __name__ == "__main__":
    main() 