"""
Utilitaires pour les expérimentations quantum_xprize
---------------------------------------------------
Ce module propose des fonctions standard pour sauvegarder les résultats d'expériences
au format JSON (et CSV si besoin), afin de faciliter la visualisation croisée,
l'intégration et la mémoire vivante du projet.
Libre à chacun de l'enrichir ou de l'adapter.
"""

import json
import csv
from pathlib import Path

def sauvegarder_resultats_json(resultats, chemin):
    """
    Sauvegarde les résultats d'une expérience au format JSON.
    - resultats : dict ou structure sérialisable
    - chemin : chemin du fichier de sortie
    """
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, ensure_ascii=False, indent=2)


def sauvegarder_resultats_csv(lignes, chemin, fieldnames=None):
    """
    Sauvegarde les résultats d'une expérience au format CSV.
    - lignes : liste de dicts (ou de listes)
    - chemin : chemin du fichier de sortie
    - fieldnames : noms des colonnes (optionnel, utile si lignes est une liste de dicts)
    """
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, 'w', encoding='utf-8', newline='') as f:
        if isinstance(lignes[0], dict):
            writer = csv.DictWriter(f, fieldnames=fieldnames or list(lignes[0].keys()))
            writer.writeheader()
            writer.writerows(lignes)
        else:
            writer = csv.writer(f)
            writer.writerows(lignes) 