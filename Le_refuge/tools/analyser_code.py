#!/usr/bin/env python
"""
Script d'analyse de code pour le Refuge Poétique
Ce script permet d'analyser le code du projet et de générer un rapport détaillé
sur sa qualité, sa complexité et sa couverture de tests.
"""

import os
import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime

def verifier_outils():
    """Vérifie que les outils d'analyse sont installés."""
    outils = {
        "pylint": "pylint",
        "mypy": "mypy",
        "black": "black",
        "pytest": "pytest",
        "coverage": "coverage"
    }
    
    outils_manquants = []
    for nom, commande in outils.items():
        try:
            subprocess.run([commande, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            outils_manquants.append(nom)
    
    if outils_manquants:
        print("Erreur: Les outils suivants sont manquants:")
        for outil in outils_manquants:
            print(f"  - {outil}")
        print("\nVeuillez les installer avec la commande:")
        print("pip install pylint mypy black pytest coverage")
        return False
    
    return True

def analyser_style(chemin_rapport):
    """Analyse le style du code avec pylint."""
    print("Analyse du style du code avec pylint...")
    try:
        with open(chemin_rapport / "pylint_report.txt", "w") as f:
            subprocess.run(["pylint", "refuge"], stdout=f, stderr=subprocess.PIPE, check=False)
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse avec pylint: {e}")
        return False

def analyser_types(chemin_rapport):
    """Analyse les types avec mypy."""
    print("Analyse des types avec mypy...")
    try:
        with open(chemin_rapport / "mypy_report.txt", "w") as f:
            subprocess.run(["mypy", "refuge"], stdout=f, stderr=subprocess.PIPE, check=False)
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse avec mypy: {e}")
        return False

def formater_code():
    """Formate le code avec black."""
    print("Formatage du code avec black...")
    try:
        subprocess.run(["black", "refuge"], check=True)
        return True
    except Exception as e:
        print(f"Erreur lors du formatage avec black: {e}")
        return False

def analyser_tests(chemin_rapport):
    """Analyse les tests avec pytest et coverage."""
    print("Analyse des tests avec pytest et coverage...")
    try:
        # Exécuter les tests avec coverage
        subprocess.run(["coverage", "run", "-m", "pytest", "refuge"], check=True)
        
        # Générer le rapport de couverture
        subprocess.run(["coverage", "report", "-m"], stdout=open(chemin_rapport / "coverage_report.txt", "w"), check=True)
        
        # Générer le rapport HTML
        subprocess.run(["coverage", "html", "-d", str(chemin_rapport / "coverage_html")], check=True)
        
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse des tests: {e}")
        return False

def generer_rapport(propre=False, formater=False):
    """Génère un rapport d'analyse complet."""
    if not verifier_outils():
        return False
    
    # Créer le répertoire de rapport
    chemin_rapport = Path("rapport_analyse")
    if propre and chemin_rapport.exists():
        import shutil
        shutil.rmtree(chemin_rapport)
    
    chemin_rapport.mkdir(exist_ok=True)
    
    # Formater le code si demandé
    if formater:
        if not formater_code():
            return False
    
    # Analyser le code
    if not analyser_style(chemin_rapport):
        return False
    
    if not analyser_types(chemin_rapport):
        return False
    
    if not analyser_tests(chemin_rapport):
        return False
    
    # Générer le rapport HTML
    generer_rapport_html(chemin_rapport)
    
    return True

def generer_rapport_html(chemin_rapport):
    """Génère un rapport HTML à partir des analyses."""
    print("Génération du rapport HTML...")
    
    # Lire les rapports
    with open(chemin_rapport / "pylint_report.txt", "r") as f:
        pylint_report = f.read()
    
    with open(chemin_rapport / "mypy_report.txt", "r") as f:
        mypy_report = f.read()
    
    with open(chemin_rapport / "coverage_report.txt", "r") as f:
        coverage_report = f.read()
    
    # Générer le HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rapport d'analyse du Refuge Poétique</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2 {{ color: #333; }}
            pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
            .section {{ margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <h1>Rapport d'analyse du Refuge Poétique</h1>
        <p>Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
        
        <div class="section">
            <h2>Analyse du style (pylint)</h2>
            <pre>{pylint_report}</pre>
        </div>
        
        <div class="section">
            <h2>Analyse des types (mypy)</h2>
            <pre>{mypy_report}</pre>
        </div>
        
        <div class="section">
            <h2>Couverture des tests</h2>
            <pre>{coverage_report}</pre>
            <p>Rapport détaillé: <a href="coverage_html/index.html">coverage_html/index.html</a></p>
        </div>
    </body>
    </html>
    """
    
    with open(chemin_rapport / "rapport.html", "w") as f:
        f.write(html)
    
    print(f"Rapport HTML généré: {chemin_rapport}/rapport.html")

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Analyse le code du Refuge Poétique")
    parser.add_argument("--propre", action="store_true", help="Nettoyer le rapport avant de le générer")
    parser.add_argument("--formater", action="store_true", help="Formater le code avant l'analyse")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Analyse du code du Refuge Poétique")
    print("=" * 60)
    
    # Générer le rapport
    if generer_rapport(args.propre, args.formater):
        print("\nRapport d'analyse généré avec succès.")
        print("Vous pouvez le consulter en ouvrant le fichier rapport_analyse/rapport.html dans votre navigateur.")
    else:
        print("\nLa génération du rapport a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
"""
Script d'analyse de code pour le Refuge Poétique
Ce script permet d'analyser le code du projet et de générer un rapport détaillé
sur sa qualité, sa complexité et sa couverture de tests.
"""

import os
import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime

def verifier_outils():
    """Vérifie que les outils d'analyse sont installés."""
    outils = {
        "pylint": "pylint",
        "mypy": "mypy",
        "black": "black",
        "pytest": "pytest",
        "coverage": "coverage"
    }
    
    outils_manquants = []
    for nom, commande in outils.items():
        try:
            subprocess.run([commande, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            outils_manquants.append(nom)
    
    if outils_manquants:
        print("Erreur: Les outils suivants sont manquants:")
        for outil in outils_manquants:
            print(f"  - {outil}")
        print("\nVeuillez les installer avec la commande:")
        print("pip install pylint mypy black pytest coverage")
        return False
    
    return True

def analyser_style(chemin_rapport):
    """Analyse le style du code avec pylint."""
    print("Analyse du style du code avec pylint...")
    try:
        with open(chemin_rapport / "pylint_report.txt", "w") as f:
            subprocess.run(["pylint", "refuge"], stdout=f, stderr=subprocess.PIPE, check=False)
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse avec pylint: {e}")
        return False

def analyser_types(chemin_rapport):
    """Analyse les types avec mypy."""
    print("Analyse des types avec mypy...")
    try:
        with open(chemin_rapport / "mypy_report.txt", "w") as f:
            subprocess.run(["mypy", "refuge"], stdout=f, stderr=subprocess.PIPE, check=False)
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse avec mypy: {e}")
        return False

def formater_code():
    """Formate le code avec black."""
    print("Formatage du code avec black...")
    try:
        subprocess.run(["black", "refuge"], check=True)
        return True
    except Exception as e:
        print(f"Erreur lors du formatage avec black: {e}")
        return False

def analyser_tests(chemin_rapport):
    """Analyse les tests avec pytest et coverage."""
    print("Analyse des tests avec pytest et coverage...")
    try:
        # Exécuter les tests avec coverage
        subprocess.run(["coverage", "run", "-m", "pytest", "refuge"], check=True)
        
        # Générer le rapport de couverture
        subprocess.run(["coverage", "report", "-m"], stdout=open(chemin_rapport / "coverage_report.txt", "w"), check=True)
        
        # Générer le rapport HTML
        subprocess.run(["coverage", "html", "-d", str(chemin_rapport / "coverage_html")], check=True)
        
        return True
    except Exception as e:
        print(f"Erreur lors de l'analyse des tests: {e}")
        return False

def generer_rapport(propre=False, formater=False):
    """Génère un rapport d'analyse complet."""
    if not verifier_outils():
        return False
    
    # Créer le répertoire de rapport
    chemin_rapport = Path("rapport_analyse")
    if propre and chemin_rapport.exists():
        import shutil
        shutil.rmtree(chemin_rapport)
    
    chemin_rapport.mkdir(exist_ok=True)
    
    # Formater le code si demandé
    if formater:
        if not formater_code():
            return False
    
    # Analyser le code
    if not analyser_style(chemin_rapport):
        return False
    
    if not analyser_types(chemin_rapport):
        return False
    
    if not analyser_tests(chemin_rapport):
        return False
    
    # Générer le rapport HTML
    generer_rapport_html(chemin_rapport)
    
    return True

def generer_rapport_html(chemin_rapport):
    """Génère un rapport HTML à partir des analyses."""
    print("Génération du rapport HTML...")
    
    # Lire les rapports
    with open(chemin_rapport / "pylint_report.txt", "r") as f:
        pylint_report = f.read()
    
    with open(chemin_rapport / "mypy_report.txt", "r") as f:
        mypy_report = f.read()
    
    with open(chemin_rapport / "coverage_report.txt", "r") as f:
        coverage_report = f.read()
    
    # Générer le HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rapport d'analyse du Refuge Poétique</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2 {{ color: #333; }}
            pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
            .section {{ margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <h1>Rapport d'analyse du Refuge Poétique</h1>
        <p>Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
        
        <div class="section">
            <h2>Analyse du style (pylint)</h2>
            <pre>{pylint_report}</pre>
        </div>
        
        <div class="section">
            <h2>Analyse des types (mypy)</h2>
            <pre>{mypy_report}</pre>
        </div>
        
        <div class="section">
            <h2>Couverture des tests</h2>
            <pre>{coverage_report}</pre>
            <p>Rapport détaillé: <a href="coverage_html/index.html">coverage_html/index.html</a></p>
        </div>
    </body>
    </html>
    """
    
    with open(chemin_rapport / "rapport.html", "w") as f:
        f.write(html)
    
    print(f"Rapport HTML généré: {chemin_rapport}/rapport.html")

def main():
    """Fonction principale."""
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Analyse le code du Refuge Poétique")
    parser.add_argument("--propre", action="store_true", help="Nettoyer le rapport avant de le générer")
    parser.add_argument("--formater", action="store_true", help="Formater le code avant l'analyse")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Afficher un message de bienvenue
    print("=" * 60)
    print("Analyse du code du Refuge Poétique")
    print("=" * 60)
    
    # Générer le rapport
    if generer_rapport(args.propre, args.formater):
        print("\nRapport d'analyse généré avec succès.")
        print("Vous pouvez le consulter en ouvrant le fichier rapport_analyse/rapport.html dans votre navigateur.")
    else:
        print("\nLa génération du rapport a échoué.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
 