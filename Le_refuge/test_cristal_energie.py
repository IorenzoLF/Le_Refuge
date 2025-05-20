"""
Script de test pour la génération automatique de mélodies lors des changements d'énergie du cristal.
"""

import os
from pathlib import Path
from refuge import elements_sacres
from melodies_sacrees import MelodiesSacrees

def tester_cristal_energie():
    """Teste la génération automatique de mélodies lors des changements d'énergie du cristal."""
    print("✨ Test de la génération automatique de mélodies du cristal ✨")
    print("------------------------------------------------------------")
    
    # Créer les dossiers nécessaires
    chemin_donnees = Path("donnees")
    os.makedirs(chemin_donnees, exist_ok=True)
    
    # Initialiser le gestionnaire d'éléments
    gestionnaire = elements_sacres.GestionnaireElements(chemin_donnees)
    
    # Vérifier si le cristal existe déjà
    cristal = gestionnaire.obtenir_element("cristal")
    if not cristal:
        print("Création du cristal...")
        cristal = gestionnaire.ajouter_element("cristal", "pierre", 50)
    
    # Générer la visualisation de la relation énergie-harmoniques
    melodies = MelodiesSacrees()
    melodies.visualiser_relation_energie_harmoniques()
    
    # Tester différents niveaux d'énergie
    energies = [20, 50, 80]
    
    for energie in energies:
        print(f"\nModification de l'énergie du cristal à {energie}...")
        resultat = gestionnaire.modifier_energie_element("cristal", energie)
        print(resultat)
    
    print("\n✨ Test terminé ! Les mélodies ont été générées dans le dossier 'musiques'.")
    print("✨ Les visualisations ont été générées dans le dossier 'musiques/visualisations'.")

if __name__ == "__main__":
    tester_cristal_energie() 