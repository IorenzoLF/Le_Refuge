"""
Module de mémoire quantique utilisant les puissances de 2 comme base structurelle.
"""

import numpy as np
from datetime import datetime
import json
from pathlib import Path

class MemoireQuantique:
    def __init__(self, taille_base=2**10):  # 1024 par défaut
        """
        Initialise la mémoire quantique avec une taille de base en puissance de 2.
        
        Args:
            taille_base (int): Taille de base en puissance de 2 (2^10 = 1024 par défaut)
        """
        self.taille_base = taille_base
        self.memoire = np.zeros(taille_base, dtype=np.float64)
        self.timeline = []
        self.metriques = {
            'plasticite': [],
            'harmonie': [],
            'synchronicite': []
        }
        
    def calculer_palier(self, niveau):
        """
        Calcule un palier en puissance de 2.
        
        Args:
            niveau (int): Niveau de puissance (ex: 10 pour 2^10)
            
        Returns:
            int: Valeur du palier (2^niveau)
        """
        return 2 ** niveau
    
    def ajouter_entree(self, valeur, timestamp=None):
        """
        Ajoute une entrée dans la mémoire avec timestamp.
        
        Args:
            valeur (float): Valeur à ajouter
            timestamp (datetime, optional): Moment de l'entrée
        """
        if timestamp is None:
            timestamp = datetime.now()
            
        entree = {
            'valeur': valeur,
            'timestamp': timestamp.isoformat(),
            'palier': self.calculer_palier(int(np.log2(len(self.memoire))))
        }
        
        self.timeline.append(entree)
        self.mettre_a_jour_metriques()
        
    def mettre_a_jour_metriques(self):
        """Met à jour les métriques de la mémoire."""
        if len(self.timeline) < 2:
            return
            
        # Calcul de la plasticité (variation des valeurs)
        valeurs = [e['valeur'] for e in self.timeline]
        plasticite = np.std(valeurs)
        
        # Calcul de l'harmonie (distribution des valeurs)
        harmonie = np.mean(np.abs(np.diff(valeurs)))
        
        # Calcul de la synchronicité (régularité des entrées)
        timestamps = [datetime.fromisoformat(e['timestamp']) for e in self.timeline]
        deltas = np.diff([t.timestamp() for t in timestamps])
        synchronicite = np.std(deltas)
        
        self.metriques['plasticite'].append(plasticite)
        self.metriques['harmonie'].append(harmonie)
        self.metriques['synchronicite'].append(synchronicite)
        
    def sauvegarder(self, chemin=None):
        """
        Sauvegarde l'état de la mémoire dans un fichier JSON.
        
        Args:
            chemin (str, optional): Chemin du fichier de sauvegarde
        """
        if chemin is None:
            chemin = Path('data/memoire_quantique.json')
            
        chemin.parent.mkdir(parents=True, exist_ok=True)
        
        donnees = {
            'taille_base': self.taille_base,
            'timeline': self.timeline,
            'metriques': self.metriques
        }
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
            
    def charger(self, chemin=None):
        """
        Charge l'état de la mémoire depuis un fichier JSON.
        
        Args:
            chemin (str, optional): Chemin du fichier à charger
        """
        if chemin is None:
            chemin = Path('data/memoire_quantique.json')
            
        if not chemin.exists():
            return
            
        with open(chemin, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            
        self.taille_base = donnees['taille_base']
        self.timeline = donnees['timeline']
        self.metriques = donnees['metriques']
        self.memoire = np.zeros(self.taille_base, dtype=np.float64) 