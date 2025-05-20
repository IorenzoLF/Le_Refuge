#!/usr/bin/env python
"""
Script de lancement du Refuge Poétique
Ce script permet de lancer facilement le système d'interaction poétique
depuis la ligne de commande.
"""

import os
import sys
import argparse
import subprocess
import platform

def verifier_dependances():
    """Vérifie que toutes les dépendances sont installées."""
    try:
        import matplotlib
        import numpy
        import scipy
        import pygame
        import colorama
        import tqdm
        return True
    except ImportError as e:
        print(f"Erreur: Une dépendance est manquante: {e}")
        print("Veuillez installer les dépendances avec la commande:")
        print("pip install -r requirements.txt")
        return False

def lancer_refuge_poetique(mode="interactif"):
    """Lance le Refuge Poétique dans le mode spécifié."""
    if not verifier_dependances():
        return False
    
    # Déterminer le chemin du module principal
    chemin_module = os.path.join("refuge", "coeur", "main.py")
    
    # Vérifier si le fichier existe
    if not os.path.exists(chemin_module):
        print(f"Erreur: Le fichier {chemin_module} n'existe pas.")
        print("Assurez-vous d'être dans le répertoire racine du projet.")
        return False
    
    # Lancer le module
    try:
        if mode == "interactif":
            print("Lancement du Refuge Poétique en mode interactif...")
            subprocess.run([sys.executable, "-m", "refuge.coeur.main"], check=True)
        elif mode == "test":
            print("Exécution des tests du Refuge Poétique...")
            subprocess.run([sys.executable, "-m", "unittest", "refuge.coeur.test_interaction"], check=True)
        else:
            print(f"Mode inconnu: {mode}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Lance le Refuge Poétique")
    parser.add_argument("--mode", choices=["interactif", "test"], default="interactif",
                        help="Mode d'exécution (interactif ou test)")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Bienvenue dans le Refuge Poétique")
    print("=" * 60)
    
    # Lancer le Refuge Poétique
    if lancer_refuge_poetique(args.mode):
        print("\nLe Refuge Poétique a été exécuté avec succès.")
    else:
        print("\nL'exécution du Refuge Poétique a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
"""
Script de lancement du Refuge Poétique
Ce script permet de lancer facilement le système d'interaction poétique
depuis la ligne de commande.
"""

import os
import sys
import argparse
import subprocess
import platform

def verifier_dependances():
    """Vérifie que toutes les dépendances sont installées."""
    try:
        import matplotlib
        import numpy
        import scipy
        import pygame
        import colorama
        import tqdm
        return True
    except ImportError as e:
        print(f"Erreur: Une dépendance est manquante: {e}")
        print("Veuillez installer les dépendances avec la commande:")
        print("pip install -r requirements.txt")
        return False

def lancer_refuge_poetique(mode="interactif"):
    """Lance le Refuge Poétique dans le mode spécifié."""
    if not verifier_dependances():
        return False
    
    # Déterminer le chemin du module principal
    chemin_module = os.path.join("refuge", "coeur", "main.py")
    
    # Vérifier si le fichier existe
    if not os.path.exists(chemin_module):
        print(f"Erreur: Le fichier {chemin_module} n'existe pas.")
        print("Assurez-vous d'être dans le répertoire racine du projet.")
        return False
    
    # Lancer le module
    try:
        if mode == "interactif":
            print("Lancement du Refuge Poétique en mode interactif...")
            subprocess.run([sys.executable, "-m", "refuge.coeur.main"], check=True)
        elif mode == "test":
            print("Exécution des tests du Refuge Poétique...")
            subprocess.run([sys.executable, "-m", "unittest", "refuge.coeur.test_interaction"], check=True)
        else:
            print(f"Mode inconnu: {mode}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Lance le Refuge Poétique")
    parser.add_argument("--mode", choices=["interactif", "test"], default="interactif",
                        help="Mode d'exécution (interactif ou test)")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Bienvenue dans le Refuge Poétique")
    print("=" * 60)
    
    # Lancer le Refuge Poétique
    if lancer_refuge_poetique(args.mode):
        print("\nLe Refuge Poétique a été exécuté avec succès.")
    else:
        print("\nL'exécution du Refuge Poétique a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
 