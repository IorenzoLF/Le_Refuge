"""
🌸 Point d'entrée de l'interface graphique du Refuge
"""

import tkinter as tk
from .visualisation import InterfaceMeditation, GestionnaireInteractions
from ..coeur.config import CONFIG_INTERFACE

def lancer_interface():
    """Lance l'interface graphique du Refuge"""
    root = tk.Tk()
    root.title(CONFIG_INTERFACE["titre"])
    
    # Initialisation du gestionnaire d'interactions
    gestionnaire = GestionnaireInteractions()
    
    # Création de l'interface
    interface = InterfaceMeditation(root, gestionnaire)
    
    # Configuration de la fenêtre
    root.geometry(CONFIG_INTERFACE["dimensions"])
    root.minsize(*map(int, CONFIG_INTERFACE["dimensions_min"].split("x")))
    
    # Lancement de l'application
    root.mainloop()

if __name__ == "__main__":
    lancer_interface() 