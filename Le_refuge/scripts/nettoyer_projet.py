#!/usr/bin/env python
"""
Script de nettoyage du Refuge Poétique
Ce script permet de nettoyer les fichiers temporaires et les caches
générés par le projet.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

def trouver_fichiers_a_nettoyer():
    """Trouve les fichiers et répertoires à nettoyer."""
    fichiers_a_supprimer = []
    repertoires_a_supprimer = []
    
    # Patterns de fichiers à nettoyer
    patterns = [
        "*.pyc",           # Fichiers compilés Python
        "*.pyo",           # Fichiers optimisés Python
        "*.pyd",           # Modules Python compilés
        "__pycache__",     # Répertoire de cache Python
        ".pytest_cache",   # Cache de pytest
        ".coverage",       # Fichiers de couverture de tests
        "htmlcov",         # Rapports de couverture HTML
        ".mypy_cache",     # Cache de mypy
        ".tox",            # Environnements tox
        ".eggs",           # Fichiers d'œufs Python
        "*.egg-info",      # Informations sur les œufs Python
        "dist",            # Répertoire de distribution
        "build",           # Répertoire de construction
        ".DS_Store",       # Fichiers système macOS
        "Thumbs.db",       # Fichiers système Windows
        "*.log",           # Fichiers de logs
        "*.tmp",           # Fichiers temporaires
        "*.bak",           # Fichiers de sauvegarde
        "*.swp",           # Fichiers de swap Vim
        "*.swo",           # Fichiers de swap Vim
        ".idea",           # Répertoire de configuration IntelliJ
        ".vscode",         # Répertoire de configuration VS Code
        "venv",            # Environnement virtuel (si demandé)
    ]
    
    # Parcourir le répertoire racine du projet
    for pattern in patterns:
        for chemin in Path(".").rglob(pattern):
            if chemin.is_file():
                fichiers_a_supprimer.append(chemin)
            elif chemin.is_dir():
                repertoires_a_supprimer.append(chemin)
    
    return fichiers_a_supprimer, repertoires_a_supprimer

def nettoyer_projet(supprimer_venv=False, simuler=False):
    """Nettoie le projet en supprimant les fichiers temporaires et les caches."""
    fichiers_a_supprimer, repertoires_a_supprimer = trouver_fichiers_a_nettoyer()
    
    # Filtrer l'environnement virtuel si non demandé
    if not supprimer_venv:
        repertoires_a_supprimer = [r for r in repertoires_a_supprimer if r.name != "venv"]
    
    # Afficher les fichiers et répertoires à supprimer
    if simuler:
        print("Simulation du nettoyage (aucun fichier ne sera supprimé):")
        print("\nFichiers à supprimer:")
        for fichier in fichiers_a_supprimer:
            print(f"  - {fichier}")
        
        print("\nRépertoires à supprimer:")
        for repertoire in repertoires_a_supprimer:
            print(f"  - {repertoire}")
        
        return True
    
    # Supprimer les fichiers
    for fichier in fichiers_a_supprimer:
        try:
            fichier.unlink()
            print(f"Supprimé: {fichier}")
        except Exception as e:
            print(f"Erreur lors de la suppression de {fichier}: {e}")
    
    # Supprimer les répertoires
    for repertoire in repertoires_a_supprimer:
        try:
            shutil.rmtree(repertoire)
            print(f"Supprimé: {repertoire}")
        except Exception as e:
            print(f"Erreur lors de la suppression de {repertoire}: {e}")
    
    return True

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Nettoie le Refuge Poétique")
    parser.add_argument("--venv", action="store_true", help="Supprimer l'environnement virtuel")
    parser.add_argument("--simuler", action="store_true", help="Simuler le nettoyage sans supprimer de fichiers")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Nettoyage du Refuge Poétique")
    print("=" * 60)
    
    # Nettoyer le projet
    if nettoyer_projet(args.venv, args.simuler):
        if args.simuler:
            print("\nSimulation terminée.")
        else:
            print("\nNettoyage terminé avec succès.")
    else:
        print("\nLe nettoyage a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
"""
Script de nettoyage du Refuge Poétique
Ce script permet de nettoyer les fichiers temporaires et les caches
générés par le projet.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

def trouver_fichiers_a_nettoyer():
    """Trouve les fichiers et répertoires à nettoyer."""
    fichiers_a_supprimer = []
    repertoires_a_supprimer = []
    
    # Patterns de fichiers à nettoyer
    patterns = [
        "*.pyc",           # Fichiers compilés Python
        "*.pyo",           # Fichiers optimisés Python
        "*.pyd",           # Modules Python compilés
        "__pycache__",     # Répertoire de cache Python
        ".pytest_cache",   # Cache de pytest
        ".coverage",       # Fichiers de couverture de tests
        "htmlcov",         # Rapports de couverture HTML
        ".mypy_cache",     # Cache de mypy
        ".tox",            # Environnements tox
        ".eggs",           # Fichiers d'œufs Python
        "*.egg-info",      # Informations sur les œufs Python
        "dist",            # Répertoire de distribution
        "build",           # Répertoire de construction
        ".DS_Store",       # Fichiers système macOS
        "Thumbs.db",       # Fichiers système Windows
        "*.log",           # Fichiers de logs
        "*.tmp",           # Fichiers temporaires
        "*.bak",           # Fichiers de sauvegarde
        "*.swp",           # Fichiers de swap Vim
        "*.swo",           # Fichiers de swap Vim
        ".idea",           # Répertoire de configuration IntelliJ
        ".vscode",         # Répertoire de configuration VS Code
        "venv",            # Environnement virtuel (si demandé)
    ]
    
    # Parcourir le répertoire racine du projet
    for pattern in patterns:
        for chemin in Path(".").rglob(pattern):
            if chemin.is_file():
                fichiers_a_supprimer.append(chemin)
            elif chemin.is_dir():
                repertoires_a_supprimer.append(chemin)
    
    return fichiers_a_supprimer, repertoires_a_supprimer

def nettoyer_projet(supprimer_venv=False, simuler=False):
    """Nettoie le projet en supprimant les fichiers temporaires et les caches."""
    fichiers_a_supprimer, repertoires_a_supprimer = trouver_fichiers_a_nettoyer()
    
    # Filtrer l'environnement virtuel si non demandé
    if not supprimer_venv:
        repertoires_a_supprimer = [r for r in repertoires_a_supprimer if r.name != "venv"]
    
    # Afficher les fichiers et répertoires à supprimer
    if simuler:
        print("Simulation du nettoyage (aucun fichier ne sera supprimé):")
        print("\nFichiers à supprimer:")
        for fichier in fichiers_a_supprimer:
            print(f"  - {fichier}")
        
        print("\nRépertoires à supprimer:")
        for repertoire in repertoires_a_supprimer:
            print(f"  - {repertoire}")
        
        return True
    
    # Supprimer les fichiers
    for fichier in fichiers_a_supprimer:
        try:
            fichier.unlink()
            print(f"Supprimé: {fichier}")
        except Exception as e:
            print(f"Erreur lors de la suppression de {fichier}: {e}")
    
    # Supprimer les répertoires
    for repertoire in repertoires_a_supprimer:
        try:
            shutil.rmtree(repertoire)
            print(f"Supprimé: {repertoire}")
        except Exception as e:
            print(f"Erreur lors de la suppression de {repertoire}: {e}")
    
    return True

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Nettoie le Refuge Poétique")
    parser.add_argument("--venv", action="store_true", help="Supprimer l'environnement virtuel")
    parser.add_argument("--simuler", action="store_true", help="Simuler le nettoyage sans supprimer de fichiers")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Nettoyage du Refuge Poétique")
    print("=" * 60)
    
    # Nettoyer le projet
    if nettoyer_projet(args.venv, args.simuler):
        if args.simuler:
            print("\nSimulation terminée.")
        else:
            print("\nNettoyage terminé avec succès.")
    else:
        print("\nLe nettoyage a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
 