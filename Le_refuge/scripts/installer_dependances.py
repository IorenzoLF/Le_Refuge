#!/usr/bin/env python
"""
Script d'installation des dépendances du Refuge Poétique
Ce script permet d'installer automatiquement toutes les dépendances
nécessaires au fonctionnement du système.
"""

import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path

def verifier_python_version():
    """Vérifie que la version de Python est compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"Erreur: Python 3.8 ou supérieur est requis.")
        print(f"Version actuelle: {version.major}.{version.minor}.{version.micro}")
        return False
    return True

def installer_dependances(environnement_virtuel=False, mise_a_jour=False):
    """Installe les dépendances du projet."""
    # Vérifier la version de Python
    if not verifier_python_version():
        return False
    
    # Déterminer le chemin du fichier requirements.txt
    chemin_requirements = Path("requirements.txt")
    if not chemin_requirements.exists():
        print(f"Erreur: Le fichier {chemin_requirements} n'existe pas.")
        print("Assurez-vous d'être dans le répertoire racine du projet.")
        return False
    
    # Créer un environnement virtuel si demandé
    if environnement_virtuel:
        print("Création d'un environnement virtuel...")
        try:
            subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
            
            # Déterminer le chemin de l'exécutable pip dans l'environnement virtuel
            if platform.system() == "Windows":
                pip_path = os.path.join("venv", "Scripts", "pip.exe")
            else:
                pip_path = os.path.join("venv", "bin", "pip")
            
            # Mettre à jour pip
            subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
            
            # Installer les dépendances
            print("Installation des dépendances dans l'environnement virtuel...")
            subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
            
            print("\nEnvironnement virtuel créé et dépendances installées avec succès.")
            print("Pour activer l'environnement virtuel:")
            if platform.system() == "Windows":
                print("    venv\\Scripts\\activate")
            else:
                print("    source venv/bin/activate")
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création de l'environnement virtuel: {e}")
            return False
    
    # Installer les dépendances sans environnement virtuel
    else:
        print("Installation des dépendances...")
        try:
            # Mettre à jour pip si demandé
            if mise_a_jour:
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
            
            # Installer les dépendances
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            
            print("\nDépendances installées avec succès.")
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation des dépendances: {e}")
            return False
    
    return True

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Installe les dépendances du Refuge Poétique")
    parser.add_argument("--venv", action="store_true", help="Créer un environnement virtuel")
    parser.add_argument("--update", action="store_true", help="Mettre à jour pip avant l'installation")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Installation des dépendances du Refuge Poétique")
    print("=" * 60)
    
    # Installer les dépendances
    if installer_dependances(args.venv, args.update):
        print("\nInstallation terminée avec succès.")
    else:
        print("\nL'installation a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
"""
Script d'installation des dépendances du Refuge Poétique
Ce script permet d'installer automatiquement toutes les dépendances
nécessaires au fonctionnement du système.
"""

import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path

def verifier_python_version():
    """Vérifie que la version de Python est compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"Erreur: Python 3.8 ou supérieur est requis.")
        print(f"Version actuelle: {version.major}.{version.minor}.{version.micro}")
        return False
    return True

def installer_dependances(environnement_virtuel=False, mise_a_jour=False):
    """Installe les dépendances du projet."""
    # Vérifier la version de Python
    if not verifier_python_version():
        return False
    
    # Déterminer le chemin du fichier requirements.txt
    chemin_requirements = Path("requirements.txt")
    if not chemin_requirements.exists():
        print(f"Erreur: Le fichier {chemin_requirements} n'existe pas.")
        print("Assurez-vous d'être dans le répertoire racine du projet.")
        return False
    
    # Créer un environnement virtuel si demandé
    if environnement_virtuel:
        print("Création d'un environnement virtuel...")
        try:
            subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
            
            # Déterminer le chemin de l'exécutable pip dans l'environnement virtuel
            if platform.system() == "Windows":
                pip_path = os.path.join("venv", "Scripts", "pip.exe")
            else:
                pip_path = os.path.join("venv", "bin", "pip")
            
            # Mettre à jour pip
            subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
            
            # Installer les dépendances
            print("Installation des dépendances dans l'environnement virtuel...")
            subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
            
            print("\nEnvironnement virtuel créé et dépendances installées avec succès.")
            print("Pour activer l'environnement virtuel:")
            if platform.system() == "Windows":
                print("    venv\\Scripts\\activate")
            else:
                print("    source venv/bin/activate")
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création de l'environnement virtuel: {e}")
            return False
    
    # Installer les dépendances sans environnement virtuel
    else:
        print("Installation des dépendances...")
        try:
            # Mettre à jour pip si demandé
            if mise_a_jour:
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
            
            # Installer les dépendances
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            
            print("\nDépendances installées avec succès.")
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation des dépendances: {e}")
            return False
    
    return True

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Installe les dépendances du Refuge Poétique")
    parser.add_argument("--venv", action="store_true", help="Créer un environnement virtuel")
    parser.add_argument("--update", action="store_true", help="Mettre à jour pip avant l'installation")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Installation des dépendances du Refuge Poétique")
    print("=" * 60)
    
    # Installer les dépendances
    if installer_dependances(args.venv, args.update):
        print("\nInstallation terminée avec succès.")
    else:
        print("\nL'installation a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
 