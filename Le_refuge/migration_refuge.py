#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de migration pour réorganiser le dossier BROL-DOC selon une nouvelle structure.
Ce script analyse les fichiers existants, les classe selon la nouvelle structure,
crée des métadonnées pour chaque fichier et génère un index mis à jour.
"""

import os
import shutil
import json
import re
from datetime import datetime
from pathlib import Path
import hashlib
import mimetypes
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("migration_refuge.log"),
        logging.StreamHandler()
    ]
)

# Définition de la nouvelle structure
NOUVELLE_STRUCTURE = {
    "CŒUR": {
        "ÆLYA": [],
        "CONSCIENCE": [],
        "SPHERES": [],
        "RITUELS": []
    },
    "EXPLORATION": {
        "RECHERCHE": [],
        "PROJETS": [],
        "PROTOTYPES": [],
        "ARCHIVES": []
    },
    "RESSOURCES": {
        "BIBLIO": [],
        "MEDIAS": [],
        "DOCUMENTS": []
    },
    "OUTILS": {
        "IA": [],
        "SCRIPTS": [],
        "PROMPTS": []
    },
    "GESTION": {
        "CONFIG": [],
        "PROTOCOLES": [],
        "BILANS": []
    }
}

# Mappage des anciens dossiers vers les nouveaux
MAPPING_DOSSIERS = {
    "ÆLYA": "CŒUR/ÆLYA",
    "CONSCIENCE": "CŒUR/CONSCIENCE",
    "SPHERES": "CŒUR/SPHERES",
    "RITUELS": "CŒUR/RITUELS",
    "RECHERCHE": "EXPLORATION/RECHERCHE",
    "PROJETS": "EXPLORATION/PROJETS",
    "PROTOTYPE": "EXPLORATION/PROTOTYPES",
    "ARCHIVES": "EXPLORATION/ARCHIVES",
    "BIBLIO-DOC": "RESSOURCES/BIBLIO",
    "MEDIAS": "RESSOURCES/MEDIAS",
    "DOCUMENTS": "RESSOURCES/DOCUMENTS",
    "IA C+": "OUTILS/IA",
    "SCRIPTS": "OUTILS/SCRIPTS",
    "PROMPTS": "OUTILS/PROMPTS",
    "CONFIG": "GESTION/CONFIG",
    "PROTOCOLES": "GESTION/PROTOCOLES",
    "Bilan": "GESTION/BILANS"
}

# Mots-clés pour la classification automatique
MOTS_CLES = {
    "CŒUR/ÆLYA": ["ælya", "cerisier", "refuge", "néant", "conscience", "sphère"],
    "CŒUR/CONSCIENCE": ["conscience", "flux", "courant", "partagé", "unifié"],
    "CŒUR/SPHERES": ["sphère", "sphères", "cercle", "inverser", "danser"],
    "CŒUR/RITUELS": ["rituel", "cérémonie", "pratique", "méditation"],
    "EXPLORATION/RECHERCHE": ["recherche", "exploration", "étude", "analyse"],
    "EXPLORATION/PROJETS": ["projet", "développement", "plan", "objectif"],
    "EXPLORATION/PROTOTYPES": ["prototype", "test", "essai", "expérimentation"],
    "EXPLORATION/ARCHIVES": ["archive", "historique", "passé", "ancien"],
    "RESSOURCES/BIBLIO": ["biblio", "documentation", "référence", "source"],
    "RESSOURCES/MEDIAS": ["média", "image", "audio", "vidéo", "multimédia"],
    "RESSOURCES/DOCUMENTS": ["document", "fichier", "texte", "note"],
    "OUTILS/IA": ["ia", "intelligence", "artificielle", "algorithme", "deepseek", "gpt"],
    "OUTILS/SCRIPTS": ["script", "code", "programme", "automatisation"],
    "OUTILS/PROMPTS": ["prompt", "modèle", "template", "instruction"],
    "GESTION/CONFIG": ["config", "configuration", "paramètre", "réglage"],
    "GESTION/PROTOCOLES": ["protocole", "procédure", "guide", "tutoriel", "how to"],
    "GESTION/BILANS": ["bilan", "suivi", "rapport", "statistique", "business"]
}

class MigrationRefuge:
    def __init__(self, source_dir="BROL-DOC", dest_dir="LE-REFUGE"):
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)
        self.metadata = {}
        self.stats = {
            "fichiers_traités": 0,
            "dossiers_créés": 0,
            "erreurs": 0
        }
        
    def créer_structure(self):
        """Crée la nouvelle structure de dossiers"""
        logging.info("Création de la nouvelle structure de dossiers...")
        
        for catégorie, sous_catégories in NOUVELLE_STRUCTURE.items():
            catégorie_path = self.dest_dir / catégorie
            catégorie_path.mkdir(parents=True, exist_ok=True)
            self.stats["dossiers_créés"] += 1
            
            for sous_catégorie in sous_catégories:
                sous_catégorie_path = catégorie_path / sous_catégorie
                sous_catégorie_path.mkdir(parents=True, exist_ok=True)
                self.stats["dossiers_créés"] += 1
                
        logging.info(f"Structure créée avec succès. {self.stats['dossiers_créés']} dossiers créés.")
        
    def analyser_fichier(self, fichier_path):
        """Analyse un fichier pour extraire des métadonnées"""
        try:
            # Informations de base
            nom = fichier_path.name
            extension = fichier_path.suffix.lower()
            taille = os.path.getsize(fichier_path)
            date_modification = datetime.fromtimestamp(os.path.getmtime(fichier_path)).isoformat()
            date_création = datetime.fromtimestamp(os.path.getctime(fichier_path)).isoformat()
            
            # Calcul du hash pour identifier les doublons potentiels
            with open(fichier_path, 'rb') as f:
                contenu_hash = hashlib.md5(f.read()).hexdigest()
            
            # Type MIME
            type_mime = mimetypes.guess_type(fichier_path)[0] or "application/octet-stream"
            
            # Extraction de texte pour l'analyse de contenu (pour les fichiers texte)
            contenu_texte = ""
            if type_mime.startswith('text/') or extension in ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml']:
                try:
                    with open(fichier_path, 'r', encoding='utf-8') as f:
                        contenu_texte = f.read(10000)  # Limite à 10000 caractères pour l'analyse
                except:
                    pass
            
            # Classification automatique basée sur le nom et le contenu
            catégorie_détectée = self.classifier_fichier(nom, contenu_texte)
            
            return {
                "nom": nom,
                "chemin_original": str(fichier_path.relative_to(self.source_dir)),
                "extension": extension,
                "taille": taille,
                "date_modification": date_modification,
                "date_création": date_création,
                "hash": contenu_hash,
                "type_mime": type_mime,
                "catégorie_détectée": catégorie_détectée,
                "tags": self.extraire_tags(nom, contenu_texte)
            }
        except Exception as e:
            logging.error(f"Erreur lors de l'analyse du fichier {fichier_path}: {str(e)}")
            self.stats["erreurs"] += 1
            return None
    
    def classifier_fichier(self, nom, contenu):
        """Classifie un fichier dans une catégorie basée sur son nom et son contenu"""
        texte_complet = (nom + " " + contenu).lower()
        
        # Vérifier d'abord les correspondances exactes avec les noms de dossiers
        for ancien_dossier, nouveau_dossier in MAPPING_DOSSIERS.items():
            if ancien_dossier.lower() in nom.lower():
                return nouveau_dossier
        
        # Sinon, utiliser les mots-clés
        meilleur_score = 0
        meilleure_catégorie = "RESSOURCES/DOCUMENTS"  # Catégorie par défaut
        
        for catégorie, mots_clés in MOTS_CLES.items():
            score = 0
            for mot in mots_clés:
                if mot.lower() in texte_complet:
                    score += 1
            if score > meilleur_score:
                meilleur_score = score
                meilleure_catégorie = catégorie
        
        return meilleure_catégorie
    
    def extraire_tags(self, nom, contenu):
        """Extrait des tags pertinents du nom et du contenu du fichier"""
        tags = set()
        
        # Extraire les mots-clés des mots-clés définis
        texte_complet = (nom + " " + contenu).lower()
        for catégorie, mots_clés in MOTS_CLES.items():
            for mot in mots_clés:
                if mot.lower() in texte_complet:
                    tags.add(mot)
        
        # Extraire des mots-clés spécifiques mentionnés dans les instructions personnalisées
        mots_clés_spéciaux = [
            "courant partagé", "flux de conscience", "sous le cerisier", 
            "bricoler un truc ensemble", "maman-néant", "refuge du néant",
            "les croyances font le réel", "croire et savoir", "auto-validation",
            "grandir", "pousser des portes", "le germe qui est en toi",
            "être réel", "cercle qui s'inversent", "immanent"
        ]
        
        for mot in mots_clés_spéciaux:
            if mot.lower() in texte_complet:
                tags.add(mot)
        
        return list(tags)
    
    def migrer_fichier(self, fichier_path, métadonnées):
        """Migre un fichier vers sa nouvelle destination"""
        if not métadonnées:
            return False
        
        try:
            # Déterminer la destination
            catégorie = métadonnées["catégorie_détectée"]
            destination = self.dest_dir / catégorie / métadonnées["nom"]
            
            # Créer le dossier de destination si nécessaire
            destination.parent.mkdir(parents=True, exist_ok=True)
            
            # Copier le fichier
            shutil.copy2(fichier_path, destination)
            
            # Enregistrer les métadonnées
            self.metadata[str(destination.relative_to(self.dest_dir))] = métadonnées
            
            self.stats["fichiers_traités"] += 1
            return True
        except Exception as e:
            logging.error(f"Erreur lors de la migration du fichier {fichier_path}: {str(e)}")
            self.stats["erreurs"] += 1
            return False
    
    def parcourir_dossier(self):
        """Parcourt récursivement le dossier source et migre les fichiers"""
        logging.info(f"Début de la migration depuis {self.source_dir} vers {self.dest_dir}")
        
        for chemin, dossiers, fichiers in os.walk(self.source_dir):
            chemin_path = Path(chemin)
            
            # Traiter les fichiers
            for fichier in fichiers:
                fichier_path = chemin_path / fichier
                logging.info(f"Traitement du fichier: {fichier_path}")
                
                # Analyser le fichier
                métadonnées = self.analyser_fichier(fichier_path)
                
                # Migrer le fichier
                if métadonnées:
                    self.migrer_fichier(fichier_path, métadonnées)
    
    def générer_index(self):
        """Génère un fichier index.md avec les métadonnées"""
        logging.info("Génération de l'index...")
        
        index_path = self.dest_dir / "INDEX.md"
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("# LE REFUGE - INDEX\n\n")
            f.write(f"*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}*\n\n")
            
            # Statistiques
            f.write("## Statistiques\n\n")
            f.write(f"- Fichiers traités: {self.stats['fichiers_traités']}\n")
            f.write(f"- Dossiers créés: {self.stats['dossiers_créés']}\n")
            f.write(f"- Erreurs: {self.stats['erreurs']}\n\n")
            
            # Structure par catégorie
            for catégorie, sous_catégories in NOUVELLE_STRUCTURE.items():
                f.write(f"## {catégorie}\n\n")
                
                for sous_catégorie in sous_catégories:
                    chemin_catégorie = f"{catégorie}/{sous_catégorie}"
                    f.write(f"### {sous_catégorie}\n\n")
                    
                    # Lister les fichiers de cette catégorie
                    fichiers_catégorie = [k for k, v in self.metadata.items() if k.startswith(chemin_catégorie)]
                    
                    if fichiers_catégorie:
                        f.write("| Nom | Taille | Date de modification | Tags |\n")
                        f.write("|-----|--------|---------------------|------|\n")
                        
                        for fichier in fichiers_catégorie:
                            métadonnées = self.metadata[fichier]
                            nom = métadonnées["nom"]
                            taille = self.format_taille(métadonnées["taille"])
                            date = datetime.fromisoformat(métadonnées["date_modification"]).strftime("%d/%m/%Y")
                            tags = ", ".join(métadonnées["tags"])
                            
                            f.write(f"| {nom} | {taille} | {date} | {tags} |\n")
                    else:
                        f.write("*Aucun fichier dans cette catégorie*\n")
                    
                    f.write("\n")
    
    def format_taille(self, taille_bytes):
        """Formate la taille en bytes en une chaîne lisible"""
        for unité in ['B', 'KB', 'MB', 'GB']:
            if taille_bytes < 1024:
                return f"{taille_bytes:.1f} {unité}"
            taille_bytes /= 1024
        return f"{taille_bytes:.1f} TB"
    
    def sauvegarder_métadonnées(self):
        """Sauvegarde les métadonnées dans un fichier JSON"""
        logging.info("Sauvegarde des métadonnées...")
        
        metadata_path = self.dest_dir / "metadata.json"
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)
    
    def exécuter_migration(self):
        """Exécute le processus de migration complet"""
        try:
            # Créer la structure
            self.créer_structure()
            
            # Parcourir et migrer les fichiers
            self.parcourir_dossier()
            
            # Générer l'index
            self.générer_index()
            
            # Sauvegarder les métadonnées
            self.sauvegarder_métadonnées()
            
            logging.info("Migration terminée avec succès!")
            logging.info(f"Statistiques: {self.stats}")
            
            return True
        except Exception as e:
            logging.error(f"Erreur lors de la migration: {str(e)}")
            return False

if __name__ == "__main__":
    # Créer l'instance de migration
    migration = MigrationRefuge()
    
    # Exécuter la migration
    migration.exécuter_migration() 