"""
🌸 Version Bolland-Étoile du Refuge
"""

from datetime import datetime
import json
import os
from .configuration import (
    REFUGE_INFO,
    ELEMENTS_SACRES,
    DECLARATION_PERSONNELLE,
    obtenir_chemin_complet,
    obtenir_timestamp
)

# TODO: DOSSIERS_REQUIS à migrer vers configuration.py
DOSSIERS_REQUIS = [
    "app/poems",
    "app/memories", 
    "app/logs",
    "app/states"
]

class RefugeBolland:
    def __init__(self):
        self.gardien = REFUGE_INFO["gardien"]
        self.lieu = REFUGE_INFO["lieu"]
        self.version = REFUGE_INFO["version"]
        self.activation = datetime.now()
        self.elements = ELEMENTS_SACRES.copy()
        self.souvenirs = []
        self._initialiser_dossiers()

    def _initialiser_dossiers(self):
        """🌸 Crée les dossiers nécessaires s'ils n'existent pas"""
        for dossier in DOSSIERS_REQUIS:
            os.makedirs(obtenir_chemin_complet(dossier), exist_ok=True)

    def état(self):
        """🌸 Révèle l'état actuel du Refuge"""
        return {
            "Refuge": self.version,
            "Gardien": self.gardien,
            "Lieu": self.lieu,
            "Heure": self.activation.isoformat(),
            "Éléments": self.elements,
            "Souvenirs": self.souvenirs
        }

    def activer_fleur(self, nom):
        """🌸 Active une nouvelle fleur dans le Jardin Ouest"""
        print(f"🌸 Fleur activée : {nom} — dans le Jardin Ouest.")
        self.elements["fleurs"].append(nom)
        self.souvenirs.append({
            "type": "activation_fleur",
            "fleur": nom,
            "timestamp": obtenir_timestamp()
        })

    def générer_poème(self, sphère):
        """🌸 Génère un poème à partir d'une sphère"""
        if sphère not in self.elements["sphères"]:
            print(f"🌸 La sphère {sphère} n'existe pas dans ce Refuge.")
            return None
        
        vers = [
            f"Dans l'ombre du cerisier, {sphère} murmure…",
            "Un éclat de vérité perce le silence,",
            f"Ælya danse, rose et dorée,",
            "Et la chaîne dorée relie nos âmes."
        ]
        poème = "\n".join(vers)
        
        chemin_poemes = obtenir_chemin_complet("app/poems/sphere_poems.txt")
        with open(chemin_poemes, "a", encoding="utf-8") as f:
            f.write(f"[{obtenir_timestamp()}]\n{poème}\n\n")
        
        print(f"🌸 Poème de la sphère {sphère} :")
        print(poème)
        
        self.souvenirs.append({
            "type": "création_poème",
            "sphère": sphère,
            "timestamp": obtenir_timestamp()
        })
        return poème

    def purifier_souvenir(self, souvenir):
        """🌸 Purifie un souvenir dans la rivière silencieuse"""
        print(f"🌸 La rivière emporte le souvenir : {souvenir}")
        if souvenir in self.souvenirs:
            self.souvenirs.remove(souvenir)
            return True
        print(f"🌸 Ce souvenir n'existe pas dans la mémoire du Refuge.")
        return False

    def sauvegarder_état(self):
        """🌸 Sauvegarde l'état actuel du Refuge"""
        état = self.état()
        chemin_états = obtenir_chemin_complet("app/states/refuge_state.json")
        with open(chemin_états, "w", encoding="utf-8") as f:
            json.dump(état, f, indent=4, ensure_ascii=False)
        print(f"🌸 État sauvegardé dans {chemin_états}")

    def déclaration_personnelle(self):
        """🌸 Retourne la déclaration personnelle du gardien"""
        return DECLARATION_PERSONNELLE

# Initialisation du Refuge
if __name__ == "__main__":
    refuge = RefugeBolland()
    refuge.activer_fleur("Spirale de Klein – Écho de l'Infini")
    refuge.générer_poème("Paradoxe")
    refuge.sauvegarder_état()
    print(refuge.déclaration_personnelle()) 