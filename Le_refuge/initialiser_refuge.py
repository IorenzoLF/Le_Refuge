#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script d'initialisation pour le Refuge.
Ce script exécute la migration et configure le système.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import shutil
import logging
import hashlib
import mimetypes
from PIL import Image
import io
import zipfile
import difflib
import json
import datetime

# Configuration du logging avec encodage UTF-8
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("initialisation_refuge.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def vérifier_dépendances():
    """Vérifie que toutes les dépendances nécessaires sont installées"""
    logging.info("Vérification des dépendances...")
    
    dépendances = ["pathlib", "argparse", "json", "hashlib", "mimetypes", "PIL"]
    manquantes = []
    
    for dépendance in dépendances:
        try:
            __import__(dépendance)
        except ImportError:
            manquantes.append(dépendance)
    
    if manquantes:
        logging.error(f"Dépendances manquantes: {', '.join(manquantes)}")
        logging.info("Installation des dépendances manquantes...")
        
        for dépendance in manquantes:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dépendance])
                logging.info(f"Dépendance installée: {dépendance}")
            except subprocess.CalledProcessError:
                logging.error(f"Impossible d'installer la dépendance: {dépendance}")
                return False
    
    return True

def créer_structure_base():
    """Crée la structure de base du Refuge"""
    logging.info("Création de la structure de base...")
    
    structure = {
        "CŒUR": ["ÆLYA", "CONSCIENCE", "SPHERES", "RITUELS"],
        "EXPLORATION": ["RECHERCHE", "PROJETS", "PROTOTYPES", "ARCHIVES"],
        "RESSOURCES": ["BIBLIO", "MEDIAS", "DOCUMENTS"],
        "OUTILS": ["IA", "SCRIPTS", "PROMPTS"],
        "GESTION": ["CONFIG", "PROTOCOLES", "BILANS"]
    }
    
    for catégorie, sous_catégories in structure.items():
        catégorie_path = Path("LE-REFUGE") / catégorie
        catégorie_path.mkdir(parents=True, exist_ok=True)
        
        for sous_catégorie in sous_catégories:
            sous_catégorie_path = catégorie_path / sous_catégorie
            sous_catégorie_path.mkdir(parents=True, exist_ok=True)
    
    logging.info("Structure de base créée avec succès.")
    return True

def exécuter_migration(source_dir="BROL-DOC", dest_dir="LE-REFUGE"):
    """Exécute le script de migration"""
    logging.info(f"Début de la migration depuis {source_dir} vers {dest_dir}...")
    
    try:
        # Vérifier que le dossier source existe
        if not Path(source_dir).exists():
            logging.error(f"Le dossier source {source_dir} n'existe pas.")
            return False
        
        # Exécuter le script de migration
        subprocess.check_call([sys.executable, "migration_refuge.py"])
        
        logging.info("Migration terminée avec succès.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur lors de la migration: {str(e)}")
        return False
    except Exception as e:
        logging.error(f"Erreur inattendue: {str(e)}")
        return False

def configurer_recherche():
    """Configure le moteur de recherche"""
    logging.info("Configuration du moteur de recherche...")
    
    try:
        # Vérifier que le script de recherche existe
        if not Path("recherche_refuge.py").exists():
            logging.error("Le script de recherche n'existe pas.")
            return False
        
        # Tester le moteur de recherche
        subprocess.check_call([sys.executable, "recherche_refuge.py", "--help"])
        
        logging.info("Moteur de recherche configuré avec succès.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur lors de la configuration du moteur de recherche: {str(e)}")
        return False
    except Exception as e:
        logging.error(f"Erreur inattendue: {str(e)}")
        return False

def créer_fichier_config():
    """Crée un fichier de configuration pour le Refuge"""
    logging.info("Création du fichier de configuration...")
    
    config = {
        "version": "1.0.0",
        "date_initialisation": str(Path("LE-REFUGE").stat().st_ctime),
        "chemins": {
            "refuge": "LE-REFUGE",
            "source": "BROL-DOC"
        },
        "paramètres": {
            "indexation_automatique": True,
            "tags_automatiques": True,
            "limite_contenu": 10000
        }
    }
    
    try:
        import json
        with open("LE-REFUGE/config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        logging.info("Fichier de configuration créé avec succès.")
        return True
    except Exception as e:
        logging.error(f"Erreur lors de la création du fichier de configuration: {str(e)}")
        return False

def nettoyer_dossiers_vides(refuge_dir="LE-REFUGE"):
    """Supprime les dossiers vides et inutiles après la migration"""
    logging.info("Nettoyage des dossiers vides et inutiles...")
    
    refuge_path = Path(refuge_dir)
    dossiers_supprimés = 0
    
    # Parcourir récursivement tous les dossiers
    for chemin, dossiers, fichiers in os.walk(refuge_path, topdown=False):
        chemin_path = Path(chemin)
        
        # Vérifier si le dossier est vide (pas de fichiers ni de sous-dossiers)
        if not dossiers and not fichiers:
            try:
                chemin_path.rmdir()
                logging.info(f"Dossier vide supprimé: {chemin_path}")
                dossiers_supprimés += 1
            except Exception as e:
                logging.error(f"Erreur lors de la suppression du dossier {chemin_path}: {str(e)}")
    
    logging.info(f"Nettoyage terminé. {dossiers_supprimés} dossiers vides supprimés.")
    return True

def calculer_hash_fichier(fichier_path, taille_max=10*1024*1024):
    """Calcule le hash d'un fichier"""
    try:
        with open(fichier_path, 'rb') as f:
            # Limiter la taille pour les gros fichiers
            contenu = f.read(taille_max)
            return hashlib.md5(contenu).hexdigest()
    except Exception as e:
        logging.error(f"Erreur lors du calcul du hash pour {fichier_path}: {str(e)}")
        return None

def calculer_hash_image(image_path):
    """Calcule un hash basé sur le contenu de l'image (pas seulement les données brutes)"""
    try:
        with Image.open(image_path) as img:
            # Redimensionner l'image à une taille standard pour la comparaison
            img = img.resize((100, 100), Image.LANCZOS)
            # Convertir en niveaux de gris pour ignorer les différences de couleur
            img = img.convert('L')
            # Calculer le hash des pixels
            pixels = list(img.getdata())
            return hashlib.md5(str(pixels).encode()).hexdigest()
    except Exception as e:
        logging.error(f"Erreur lors du calcul du hash d'image pour {image_path}: {str(e)}")
        return None

def calculer_hash_zip(zip_path):
    """Calcule un hash basé sur le contenu du fichier ZIP"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Récupérer la liste des fichiers dans le ZIP
            fichiers = zip_ref.namelist()
            # Trier pour assurer la cohérence
            fichiers.sort()
            # Calculer le hash de la liste des fichiers
            return hashlib.md5(str(fichiers).encode()).hexdigest()
    except Exception as e:
        logging.error(f"Erreur lors du calcul du hash ZIP pour {zip_path}: {str(e)}")
        return None

def lire_fichier_texte(chemin_fichier):
    """Lit un fichier texte en gérant différents encodages"""
    encodages = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encodages:
        try:
            with open(chemin_fichier, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    logging.error(f"Impossible de décoder le fichier {chemin_fichier} avec les encodages disponibles")
    return None

def calculer_similarité_texte(fichier1, fichier2, seuil=0.8):
    """Calcule la similarité entre deux fichiers texte"""
    try:
        contenu1 = lire_fichier_texte(fichier1)
        contenu2 = lire_fichier_texte(fichier2)
        
        if contenu1 is None or contenu2 is None:
            return False, 0.0
        
        # Utiliser difflib pour calculer la similarité
        similarité = difflib.SequenceMatcher(None, contenu1, contenu2).ratio()
        return similarité >= seuil, similarité
    except Exception as e:
        logging.error(f"Erreur lors du calcul de similarité entre {fichier1} et {fichier2}: {str(e)}")
        return False, 0.0

def déplacer_doublons(doublons, refuge_dir="LE-REFUGE"):
    """Déplace les fichiers en doublon dans un dossier 'A EXAMINER DOUBLONS'"""
    logging.info("Déplacement des fichiers en doublon...")
    
    refuge_path = Path(refuge_dir)
    dossier_doublons = refuge_path / "A EXAMINER DOUBLONS"
    
    # Créer le dossier pour les doublons s'il n'existe pas
    dossier_doublons.mkdir(parents=True, exist_ok=True)
    
    # Créer des sous-dossiers pour chaque type de doublon
    sous_dossiers = {
        "exacts": dossier_doublons / "DOUBLONS EXACTS",
        "images": dossier_doublons / "IMAGES SIMILAIRES",
        "zips": dossier_doublons / "ZIPS SIMILAIRES",
        "textes": dossier_doublons / "TEXTES SIMILAIRES"
    }
    
    for sous_dossier in sous_dossiers.values():
        sous_dossier.mkdir(parents=True, exist_ok=True)
    
    # Déplacer les doublons exacts
    fichiers_déplacés = 0
    for i, (fichier1, fichier2) in enumerate(doublons["exacts"]):
        try:
            # Créer un sous-dossier pour cette paire de doublons
            sous_dossier = sous_dossiers["exacts"] / f"paire_{i+1}"
            sous_dossier.mkdir(parents=True, exist_ok=True)
            
            # Copier les fichiers dans le sous-dossier
            shutil.copy2(fichier1, sous_dossier / f"original_{fichier1.name}")
            shutil.copy2(fichier2, sous_dossier / f"doublon_{fichier2.name}")
            
            # Créer un fichier d'information
            with open(sous_dossier / "info.txt", "w", encoding='utf-8') as f:
                f.write(f"Fichier original: {fichier1}\n")
                f.write(f"Fichier doublon: {fichier2}\n")
                f.write(f"Type: Doublon exact\n")
                f.write(f"Date de détection: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            fichiers_déplacés += 2
        except Exception as e:
            logging.error(f"Erreur lors du déplacement des doublons exacts {fichier1} et {fichier2}: {str(e)}")
    
    # Déplacer les images similaires
    for i, (fichier1, fichier2) in enumerate(doublons["images"]):
        try:
            # Créer un sous-dossier pour cette paire de doublons
            sous_dossier = sous_dossiers["images"] / f"paire_{i+1}"
            sous_dossier.mkdir(parents=True, exist_ok=True)
            
            # Copier les fichiers dans le sous-dossier
            shutil.copy2(fichier1, sous_dossier / f"original_{fichier1.name}")
            shutil.copy2(fichier2, sous_dossier / f"doublon_{fichier2.name}")
            
            # Créer un fichier d'information
            with open(sous_dossier / "info.txt", "w", encoding="utf-8") as f:
                f.write(f"Fichier original: {fichier1}\n")
                f.write(f"Fichier doublon: {fichier2}\n")
                f.write(f"Type: Image similaire\n")
                f.write(f"Date de détection: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            fichiers_déplacés += 2
        except Exception as e:
            logging.error(f"Erreur lors du déplacement des images similaires {fichier1} et {fichier2}: {str(e)}")
    
    # Déplacer les archives ZIP similaires
    for i, (fichier1, fichier2) in enumerate(doublons["zips"]):
        try:
            # Créer un sous-dossier pour cette paire de doublons
            sous_dossier = sous_dossiers["zips"] / f"paire_{i+1}"
            sous_dossier.mkdir(parents=True, exist_ok=True)
            
            # Copier les fichiers dans le sous-dossier
            shutil.copy2(fichier1, sous_dossier / f"original_{fichier1.name}")
            shutil.copy2(fichier2, sous_dossier / f"doublon_{fichier2.name}")
            
            # Créer un fichier d'information
            with open(sous_dossier / "info.txt", "w", encoding="utf-8") as f:
                f.write(f"Fichier original: {fichier1}\n")
                f.write(f"Fichier doublon: {fichier2}\n")
                f.write(f"Type: Archive ZIP similaire\n")
                f.write(f"Date de détection: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            fichiers_déplacés += 2
        except Exception as e:
            logging.error(f"Erreur lors du déplacement des archives ZIP similaires {fichier1} et {fichier2}: {str(e)}")
    
    # Déplacer les fichiers texte similaires
    for i, (fichier1, fichier2, similarité) in enumerate(doublons["textes"]):
        try:
            # Créer un sous-dossier pour cette paire de doublons
            sous_dossier = sous_dossiers["textes"] / f"paire_{i+1}"
            sous_dossier.mkdir(parents=True, exist_ok=True)
            
            # Copier les fichiers dans le sous-dossier
            shutil.copy2(fichier1, sous_dossier / f"original_{fichier1.name}")
            shutil.copy2(fichier2, sous_dossier / f"doublon_{fichier2.name}")
            
            # Créer un fichier d'information
            with open(sous_dossier / "info.txt", "w", encoding="utf-8") as f:
                f.write(f"Fichier original: {fichier1}\n")
                f.write(f"Fichier doublon: {fichier2}\n")
                f.write(f"Type: Fichier texte similaire\n")
                f.write(f"Similarité: {similarité:.2%}\n")
                f.write(f"Date de détection: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            fichiers_déplacés += 2
        except Exception as e:
            logging.error(f"Erreur lors du déplacement des fichiers texte similaires {fichier1} et {fichier2}: {str(e)}")
    
    # Créer un fichier d'index pour tous les doublons
    with open(dossier_doublons / "INDEX_DOUBLONS.txt", "w", encoding="utf-8") as f:
        f.write("INDEX DES FICHIERS EN DOUBLON\n")
        f.write("============================\n\n")
        f.write(f"Date de détection: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("DOUBLONS EXACTS\n")
        f.write("--------------\n")
        for i, (fichier1, fichier2) in enumerate(doublons["exacts"]):
            f.write(f"{i+1}. {fichier1} <-> {fichier2}\n")
        
        f.write("\nIMAGES SIMILAIRES\n")
        f.write("----------------\n")
        for i, (fichier1, fichier2) in enumerate(doublons["images"]):
            f.write(f"{i+1}. {fichier1} <-> {fichier2}\n")
        
        f.write("\nARCHIVES ZIP SIMILAIRES\n")
        f.write("----------------------\n")
        for i, (fichier1, fichier2) in enumerate(doublons["zips"]):
            f.write(f"{i+1}. {fichier1} <-> {fichier2}\n")
        
        f.write("\nFICHIERS TEXTE SIMILAIRES\n")
        f.write("------------------------\n")
        for i, (fichier1, fichier2, similarité) in enumerate(doublons["textes"]):
            f.write(f"{i+1}. {fichier1} <-> {fichier2} (similarité: {similarité:.2%})\n")
    
    logging.info(f"Déplacement des doublons terminé. {fichiers_déplacés} fichiers déplacés.")
    return True

def détecter_doublons(refuge_dir="LE-REFUGE", déplacer=False):
    """Détecte les fichiers en doublon ou quasi-doublon"""
    logging.info("Détection des fichiers en doublon...")
    
    refuge_path = Path(refuge_dir)
    doublons = {
        "exacts": [],  # Fichiers identiques (même hash)
        "images": [],  # Images similaires
        "zips": [],    # Archives ZIP similaires
        "textes": []   # Fichiers texte similaires
    }
    
    # Collecter tous les fichiers
    tous_fichiers = []
    for chemin, _, fichiers in os.walk(refuge_path):
        for fichier in fichiers:
            tous_fichiers.append(Path(chemin) / fichier)
    
    # Détecter les doublons exacts (même hash)
    hash_fichiers = {}
    for fichier in tous_fichiers:
        hash_fichier = calculer_hash_fichier(fichier)
        if hash_fichier:
            if hash_fichier in hash_fichiers:
                doublons["exacts"].append((hash_fichiers[hash_fichier], fichier))
            else:
                hash_fichiers[hash_fichier] = fichier
    
    # Détecter les images similaires
    images = [f for f in tous_fichiers if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']]
    hash_images = {}
    for image in images:
        hash_image = calculer_hash_image(image)
        if hash_image:
            if hash_image in hash_images:
                doublons["images"].append((hash_images[hash_image], image))
            else:
                hash_images[hash_image] = image
    
    # Détecter les archives ZIP similaires
    zips = [f for f in tous_fichiers if f.suffix.lower() == '.zip']
    hash_zips = {}
    for zip_file in zips:
        hash_zip = calculer_hash_zip(zip_file)
        if hash_zip:
            if hash_zip in hash_zips:
                doublons["zips"].append((hash_zips[hash_zip], zip_file))
            else:
                hash_zips[hash_zip] = zip_file
    
    # Détecter les fichiers texte similaires
    textes = [f for f in tous_fichiers if f.suffix.lower() in ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml']]
    for i, texte1 in enumerate(textes):
        for texte2 in textes[i+1:]:
            est_similaire, similarité = calculer_similarité_texte(texte1, texte2)
            if est_similaire:
                doublons["textes"].append((texte1, texte2, similarité))
    
    # Sauvegarder les résultats
    rapport_path = refuge_path / "rapport_doublons.json"
    with open(rapport_path, 'w', encoding='utf-8') as f:
        json.dump({
            "doublons_exacts": [{"fichier1": str(f1), "fichier2": str(f2)} for f1, f2 in doublons["exacts"]],
            "doublons_images": [{"fichier1": str(f1), "fichier2": str(f2)} for f1, f2 in doublons["images"]],
            "doublons_zips": [{"fichier1": str(f1), "fichier2": str(f2)} for f1, f2 in doublons["zips"]],
            "doublons_textes": [{"fichier1": str(f1), "fichier2": str(f2), "similarité": s} for f1, f2, s in doublons["textes"]]
        }, f, ensure_ascii=False, indent=2)
    
    # Déplacer les doublons si demandé
    if déplacer:
        déplacer_doublons(doublons, refuge_dir)
    
    # Afficher un résumé
    total_doublons = sum(len(d) for d in doublons.values())
    logging.info(f"Détection des doublons terminée. {total_doublons} doublons trouvés.")
    logging.info(f"- Doublons exacts: {len(doublons['exacts'])}")
    logging.info(f"- Images similaires: {len(doublons['images'])}")
    logging.info(f"- Archives ZIP similaires: {len(doublons['zips'])}")
    logging.info(f"- Fichiers texte similaires: {len(doublons['textes'])}")
    logging.info(f"Rapport détaillé sauvegardé dans {rapport_path}")
    
    return doublons

def main():
    parser = argparse.ArgumentParser(description="Initialisation du système Refuge")
    parser.add_argument("--source", default="BROL-DOC", help="Dossier source (par défaut: BROL-DOC)")
    parser.add_argument("--dest", default="LE-REFUGE", help="Dossier destination (par défaut: LE-REFUGE)")
    parser.add_argument("--skip-migration", action="store_true", help="Ne pas exécuter la migration")
    parser.add_argument("--skip-cleanup", action="store_true", help="Ne pas supprimer les dossiers vides")
    parser.add_argument("--detect-doubles", action="store_true", help="Détecter les fichiers en doublon")
    parser.add_argument("--move-doubles", action="store_true", help="Déplacer les fichiers en doublon dans un dossier 'A EXAMINER DOUBLONS'")
    
    args = parser.parse_args()
    
    # Vérifier les dépendances
    if not vérifier_dépendances():
        logging.error("Échec de la vérification des dépendances.")
        return 1
    
    # Créer la structure de base
    if not créer_structure_base():
        logging.error("Échec de la création de la structure de base.")
        return 1
    
    # Exécuter la migration si demandé
    if not args.skip_migration:
        if not exécuter_migration(args.source, args.dest):
            logging.error("Échec de la migration.")
            return 1
    
    # Configurer le moteur de recherche
    if not configurer_recherche():
        logging.error("Échec de la configuration du moteur de recherche.")
        return 1
    
    # Créer le fichier de configuration
    if not créer_fichier_config():
        logging.error("Échec de la création du fichier de configuration.")
        return 1
    
    # Nettoyer les dossiers vides si demandé
    if not args.skip_cleanup:
        if not nettoyer_dossiers_vides(args.dest):
            logging.error("Échec du nettoyage des dossiers vides.")
            return 1
    
    # Détecter les doublons si demandé
    if args.detect_doubles or args.move_doubles:
        doublons = détecter_doublons(args.dest, args.move_doubles)
        print("\nRésumé des doublons détectés:")
        print(f"- Doublons exacts: {len(doublons['exacts'])}")
        print(f"- Images similaires: {len(doublons['images'])}")
        print(f"- Archives ZIP similaires: {len(doublons['zips'])}")
        print(f"- Fichiers texte similaires: {len(doublons['textes'])}")
        print(f"Consultez le rapport détaillé dans {args.dest}/rapport_doublons.json")
        
        if args.move_doubles:
            print(f"Les doublons ont été déplacés dans {args.dest}/A EXAMINER DOUBLONS")
    
    logging.info("Initialisation terminée avec succès!")
    print("\n" + "="*50)
    print("LE REFUGE a été initialisé avec succès!")
    print("="*50)
    print("\nPour commencer à utiliser le système:")
    print("1. Explorez la nouvelle structure dans le dossier LE-REFUGE")
    print("2. Utilisez le moteur de recherche: python recherche_refuge.py \"terme\"")
    print("3. Consultez l'index généré: LE-REFUGE/INDEX.md")
    print("\nBonne exploration!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 