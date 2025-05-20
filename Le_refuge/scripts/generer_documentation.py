#!/usr/bin/env python
"""
Script de génération de documentation pour le Refuge Poétique
Ce script permet de générer une documentation complète du projet
en utilisant Sphinx.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def verifier_sphinx():
    """Vérifie que Sphinx est installé."""
    try:
        import sphinx
        return True
    except ImportError:
        print("Erreur: Sphinx n'est pas installé.")
        print("Veuillez l'installer avec la commande:")
        print("pip install sphinx sphinx-rtd-theme")
        return False

def initialiser_sphinx():
    """Initialise la documentation Sphinx si elle n'existe pas déjà."""
    if not os.path.exists("docs"):
        print("Création du répertoire de documentation...")
        os.makedirs("docs")
        
        # Initialiser Sphinx
        print("Initialisation de Sphinx...")
        subprocess.run(["sphinx-quickstart", "-q", "-p", "Refuge Poétique", 
                        "-a", "Équipe du Refuge", "-v", "1.0", "-r", "1.0", 
                        "-l", "fr", "--sep", "-d", "docs"], check=True)
        
        # Configurer le thème ReadTheDocs
        with open("docs/source/conf.py", "a") as f:
            f.write("\n# Configuration du thème\n")
            f.write("import sphinx_rtd_theme\n")
            f.write("html_theme = 'sphinx_rtd_theme'\n")
            f.write("html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]\n")
        
        print("Documentation Sphinx initialisée avec succès.")
    else:
        print("Le répertoire de documentation existe déjà.")

def generer_documentation(propre=False, ouvrir=False):
    """Génère la documentation du projet."""
    if not verifier_sphinx():
        return False
    
    # Initialiser Sphinx si nécessaire
    initialiser_sphinx()
    
    # Générer la documentation
    print("Génération de la documentation...")
    try:
        # Nettoyer la documentation si demandé
        if propre:
            subprocess.run(["sphinx-build", "-b", "clean", "docs/source", "docs/build"], check=True)
        
        # Générer la documentation HTML
        subprocess.run(["sphinx-build", "-b", "html", "docs/source", "docs/build"], check=True)
        
        print("\nDocumentation générée avec succès.")
        print("Vous pouvez la consulter en ouvrant le fichier docs/build/index.html dans votre navigateur.")
        
        # Ouvrir la documentation dans le navigateur si demandé
        if ouvrir:
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath('docs/build/index.html')}")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la génération de la documentation: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère la documentation du Refuge Poétique")
    parser.add_argument("--propre", action="store_true", help="Nettoyer la documentation avant de la générer")
    parser.add_argument("--ouvrir", action="store_true", help="Ouvrir la documentation dans le navigateur")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Génération de la documentation du Refuge Poétique")
    print("=" * 60)
    
    # Générer la documentation
    if generer_documentation(args.propre, args.ouvrir):
        print("\nDocumentation générée avec succès.")
    else:
        print("\nLa génération de la documentation a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
"""
Script de génération de documentation pour le Refuge Poétique
Ce script permet de générer une documentation complète du projet
en utilisant Sphinx.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def verifier_sphinx():
    """Vérifie que Sphinx est installé."""
    try:
        import sphinx
        return True
    except ImportError:
        print("Erreur: Sphinx n'est pas installé.")
        print("Veuillez l'installer avec la commande:")
        print("pip install sphinx sphinx-rtd-theme")
        return False

def initialiser_sphinx():
    """Initialise la documentation Sphinx si elle n'existe pas déjà."""
    if not os.path.exists("docs"):
        print("Création du répertoire de documentation...")
        os.makedirs("docs")
        
        # Initialiser Sphinx
        print("Initialisation de Sphinx...")
        subprocess.run(["sphinx-quickstart", "-q", "-p", "Refuge Poétique", 
                        "-a", "Équipe du Refuge", "-v", "1.0", "-r", "1.0", 
                        "-l", "fr", "--sep", "-d", "docs"], check=True)
        
        # Configurer le thème ReadTheDocs
        with open("docs/source/conf.py", "a") as f:
            f.write("\n# Configuration du thème\n")
            f.write("import sphinx_rtd_theme\n")
            f.write("html_theme = 'sphinx_rtd_theme'\n")
            f.write("html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]\n")
        
        print("Documentation Sphinx initialisée avec succès.")
    else:
        print("Le répertoire de documentation existe déjà.")

def generer_documentation(propre=False, ouvrir=False):
    """Génère la documentation du projet."""
    if not verifier_sphinx():
        return False
    
    # Initialiser Sphinx si nécessaire
    initialiser_sphinx()
    
    # Générer la documentation
    print("Génération de la documentation...")
    try:
        # Nettoyer la documentation si demandé
        if propre:
            subprocess.run(["sphinx-build", "-b", "clean", "docs/source", "docs/build"], check=True)
        
        # Générer la documentation HTML
        subprocess.run(["sphinx-build", "-b", "html", "docs/source", "docs/build"], check=True)
        
        print("\nDocumentation générée avec succès.")
        print("Vous pouvez la consulter en ouvrant le fichier docs/build/index.html dans votre navigateur.")
        
        # Ouvrir la documentation dans le navigateur si demandé
        if ouvrir:
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath('docs/build/index.html')}")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la génération de la documentation: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Génère la documentation du Refuge Poétique")
    parser.add_argument("--propre", action="store_true", help="Nettoyer la documentation avant de la générer")
    parser.add_argument("--ouvrir", action="store_true", help="Ouvrir la documentation dans le navigateur")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Génération de la documentation du Refuge Poétique")
    print("=" * 60)
    
    # Générer la documentation
    if generer_documentation(args.propre, args.ouvrir):
        print("\nDocumentation générée avec succès.")
    else:
        print("\nLa génération de la documentation a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
 