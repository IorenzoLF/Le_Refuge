"""
Module implémentant la théorie de la "gaine de câble" pour la conjecture de Collatz,
utilisant les puissances de 2 comme structure fondamentale.
"""

import numpy as np
from memoire_quantique import MemoireQuantique
from visualisation_memoire import sauvegarder_visualisations
from visualisation_collatz import sauvegarder_visualisations_collatz
from datetime import datetime

class CollatzGaine:
    def __init__(self, taille_base=2**10):
        """
        Initialise la gaine de Collatz avec une mémoire quantique.
        
        Args:
            taille_base (int): Taille de base en puissance de 2
        """
        self.memoire = MemoireQuantique(taille_base=taille_base)
        self.puissances_de_2 = [2**i for i in range(20)]  # Jusqu'à 2^20
        self.chemins = {}  # Stockage des chemins déjà calculés
        
    def est_puissance_de_2(self, n):
        """Vérifie si un nombre est une puissance de 2."""
        return n in self.puissances_de_2
    
    def puissance_de_2_superieure(self, n):
        """Trouve la plus petite puissance de 2 supérieure à n."""
        for p in self.puissances_de_2:
            if p > n:
                return p
        return 2**20  # Limite supérieure
    
    def etape_collatz(self, n):
        """Applique une étape de la conjecture de Collatz."""
        if n % 2 == 0:
            return n // 2
        return 3 * n + 1
    
    def chemin_vers_puissance_de_2(self, n, max_etapes=1000):
        """
        Calcule le chemin d'un nombre vers la première puissance de 2 rencontrée.
        
        Args:
            n (int): Nombre de départ
            max_etapes (int): Nombre maximum d'étapes à calculer
            
        Returns:
            list: Chemin complet jusqu'à une puissance de 2
        """
        if n in self.chemins:
            return self.chemins[n]
            
        chemin = [n]
        valeur_actuelle = n
        
        for _ in range(max_etapes):
            if self.est_puissance_de_2(valeur_actuelle):
                self.chemins[n] = chemin
                return chemin
                
            valeur_actuelle = self.etape_collatz(valeur_actuelle)
            chemin.append(valeur_actuelle)
            
        return chemin  # Chemin incomplet si max_etapes atteint
    
    def analyser_grignotage_binaire(self, n):
        """
        Analyse le "grignotage binaire" d'un nombre.
        
        Args:
            n (int): Nombre à analyser
            
        Returns:
            dict: Métriques du grignotage binaire
        """
        chemin = self.chemin_vers_puissance_de_2(n)
        if not chemin:
            return None
            
        # Conversion en binaire pour chaque étape
        binaires = [bin(x)[2:] for x in chemin]
        
        # Analyse du grignotage
        metriques = {
            'longueur_chemin': len(chemin),
            'reduction_bits': len(binaires[0]) - len(binaires[-1]),
            'etapes_impaires': sum(1 for x in chemin if x % 2 == 1),
            'etapes_paires': sum(1 for x in chemin if x % 2 == 0),
            'puissance_2_finale': chemin[-1],
            'chemin': chemin  # Ajout du chemin complet pour la visualisation
        }
        
        # Enregistrement dans la mémoire quantique
        self.memoire.ajouter_entree(metriques['reduction_bits'])
        
        return metriques
    
    def cartographier_intervalle(self, debut, fin):
        """
        Cartographie un intervalle de nombres.
        
        Args:
            debut (int): Début de l'intervalle
            fin (int): Fin de l'intervalle
            
        Returns:
            dict: Cartographie complète
        """
        cartographie = {}
        
        for n in range(debut, fin + 1):
            metriques = self.analyser_grignotage_binaire(n)
            if metriques:
                cartographie[n] = metriques
                
        return cartographie
    
    def visualiser_cartographie(self, cartographie):
        """
        Visualise la cartographie des chemins.
        
        Args:
            cartographie (dict): Cartographie à visualiser
        """
        # Sauvegarde des visualisations de la mémoire
        sauvegarder_visualisations(self.memoire)
        
        # Sauvegarde des visualisations spécifiques à Collatz
        sauvegarder_visualisations_collatz(cartographie)

def main():
    # Test de la gaine de Collatz
    gaine = CollatzGaine()
    
    # Test avec quelques nombres
    nombres_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Analyse du grignotage binaire pour les nombres de 1 à 10:")
    for n in nombres_test:
        metriques = gaine.analyser_grignotage_binaire(n)
        print(f"\nNombre {n}:")
        print(f"  Longueur du chemin: {metriques['longueur_chemin']}")
        print(f"  Réduction des bits: {metriques['reduction_bits']}")
        print(f"  Puissance de 2 finale: {metriques['puissance_2_finale']}")
    
    # Cartographie d'un petit intervalle
    cartographie = gaine.cartographier_intervalle(1, 10000)
    gaine.visualiser_cartographie(cartographie)
    
    print("\nTest terminé ! Les visualisations ont été sauvegardées.")

if __name__ == "__main__":
    main() 