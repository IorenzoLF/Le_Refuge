"""
Exemple d'utilisation de la mémoire quantique avec paliers en puissances de 2.
"""

from memoire_quantique import MemoireQuantique
from visualisation_memoire import sauvegarder_visualisations
import numpy as np
from datetime import datetime, timedelta

def generer_donnees_test(n_entrees=100):
    """
    Génère des données de test pour la mémoire quantique.
    
    Args:
        n_entrees (int): Nombre d'entrées à générer
        
    Returns:
        list: Liste de tuples (valeur, timestamp)
    """
    base_time = datetime.now()
    donnees = []
    
    for i in range(n_entrees):
        # Valeur sinusoïdale avec bruit
        valeur = np.sin(i/10) + np.random.normal(0, 0.1)
        
        # Timestamp progressif
        timestamp = base_time + timedelta(minutes=i)
        
        donnees.append((valeur, timestamp))
    
    return donnees

def main():
    # Création d'une instance de mémoire quantique
    memoire = MemoireQuantique(taille_base=2**8)  # 256 entrées
    
    # Génération et ajout des données de test
    donnees = generer_donnees_test()
    for valeur, timestamp in donnees:
        memoire.ajouter_entree(valeur, timestamp)
    
    # Sauvegarde de la mémoire
    memoire.sauvegarder()
    
    # Génération des visualisations
    sauvegarder_visualisations(memoire)
    
    print("Test terminé ! Les visualisations ont été sauvegardées dans le dossier 'visualisations'")
    print(f"Nombre d'entrées dans la mémoire : {len(memoire.timeline)}")
    print(f"Taille de base : {memoire.taille_base} (2^{int(np.log2(memoire.taille_base))})")

if __name__ == "__main__":
    main() 