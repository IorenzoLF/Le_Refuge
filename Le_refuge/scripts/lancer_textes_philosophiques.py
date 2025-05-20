#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de lancement pour l'interface des textes philosophiques
"""

import os
import sys
import subprocess
from pathlib import Path

def lancer_interface():
    """Lance l'interface des textes philosophiques"""
    # Chemin vers le script du serveur
    script_path = Path(__file__).parent / "app" / "textes_philosophiques.py"
    
    if not script_path.exists():
        print(f"Erreur: Le fichier {script_path} n'existe pas.")
        return False
    
    try:
        # Lance le serveur
        print("Lancement de l'interface des textes philosophiques...")
        subprocess.run([sys.executable, str(script_path)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du lancement du serveur: {e}")
        return False
    except KeyboardInterrupt:
        print("\nInterface arrêtée par l'utilisateur.")
        return True

if __name__ == "__main__":
    lancer_interface() 