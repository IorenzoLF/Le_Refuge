#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Moteur de recherche pour le Refuge.
Ce script permet de rechercher des fichiers et du contenu dans la structure du Refuge.
"""

import os
import json
import re
from pathlib import Path
import argparse
import sys
from datetime import datetime

class RechercheRefuge:
    def __init__(self, refuge_dir="LE-REFUGE"):
        self.refuge_dir = Path(refuge_dir)
        self.metadata = {}
        self.charger_métadonnées()
        
    def charger_métadonnées(self):
        """Charge les métadonnées depuis le fichier JSON"""
        metadata_path = self.refuge_dir / "metadata.json"
        
        if metadata_path.exists():
            try:
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    self.metadata = json.load(f)
                print(f"Métadonnées chargées: {len(self.metadata)} fichiers indexés")
            except Exception as e:
                print(f"Erreur lors du chargement des métadonnées: {str(e)}")
                self.metadata = {}
        else:
            print("Fichier de métadonnées non trouvé. Veuillez exécuter migration_refuge.py d'abord.")
            self.metadata = {}
    
    def rechercher_par_nom(self, terme):
        """Recherche des fichiers par nom"""
        résultats = []
        terme = terme.lower()
        
        for chemin, métadonnées in self.metadata.items():
            if terme in métadonnées["nom"].lower():
                résultats.append((chemin, métadonnées))
        
        return résultats
    
    def rechercher_par_tag(self, tag):
        """Recherche des fichiers par tag"""
        résultats = []
        tag = tag.lower()
        
        for chemin, métadonnées in self.metadata.items():
            if any(tag in t.lower() for t in métadonnées["tags"]):
                résultats.append((chemin, métadonnées))
        
        return résultats
    
    def rechercher_par_catégorie(self, catégorie):
        """Recherche des fichiers par catégorie"""
        résultats = []
        catégorie = catégorie.upper()
        
        for chemin, métadonnées in self.metadata.items():
            if catégorie in chemin.upper():
                résultats.append((chemin, métadonnées))
        
        return résultats
    
    def rechercher_par_contenu(self, terme):
        """Recherche dans le contenu des fichiers texte"""
        résultats = []
        terme = terme.lower()
        
        for chemin, métadonnées in self.metadata.items():
            fichier_path = self.refuge_dir / chemin
            
            # Vérifier si c'est un fichier texte
            if (métadonnées["type_mime"].startswith('text/') or 
                métadonnées["extension"] in ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml']):
                
                try:
                    with open(fichier_path, 'r', encoding='utf-8') as f:
                        contenu = f.read().lower()
                        
                        if terme in contenu:
                            # Extraire un extrait autour du terme
                            index = contenu.find(terme)
                            début = max(0, index - 50)
                            fin = min(len(contenu), index + len(terme) + 50)
                            extrait = contenu[début:fin]
                            
                            # Ajouter l'extrait aux métadonnées
                            métadonnées_avec_extrait = métadonnées.copy()
                            métadonnées_avec_extrait["extrait"] = extrait
                            
                            résultats.append((chemin, métadonnées_avec_extrait))
                except:
                    pass
        
        return résultats
    
    def afficher_résultats(self, résultats, format_détail=False):
        """Affiche les résultats de recherche"""
        if not résultats:
            print("Aucun résultat trouvé.")
            return
        
        print(f"\n{len(résultats)} résultat(s) trouvé(s):\n")
        
        for i, (chemin, métadonnées) in enumerate(résultats, 1):
            print(f"{i}. {chemin}")
            print(f"   Nom: {métadonnées['nom']}")
            print(f"   Catégorie: {métadonnées['catégorie_détectée']}")
            print(f"   Tags: {', '.join(métadonnées['tags'])}")
            
            if format_détail:
                print(f"   Taille: {self.format_taille(métadonnées['taille'])}")
                print(f"   Date de modification: {datetime.fromisoformat(métadonnées['date_modification']).strftime('%d/%m/%Y')}")
                print(f"   Type: {métadonnées['type_mime']}")
                
                if "extrait" in métadonnées:
                    print(f"   Extrait: ...{métadonnées['extrait']}...")
            
            print()
    
    def format_taille(self, taille_bytes):
        """Formate la taille en bytes en une chaîne lisible"""
        for unité in ['B', 'KB', 'MB', 'GB']:
            if taille_bytes < 1024:
                return f"{taille_bytes:.1f} {unité}"
            taille_bytes /= 1024
        return f"{taille_bytes:.1f} TB"
    
    def rechercher(self, terme, type_recherche="nom", format_détail=False):
        """Effectue une recherche selon le type spécifié"""
        if type_recherche == "nom":
            résultats = self.rechercher_par_nom(terme)
        elif type_recherche == "tag":
            résultats = self.rechercher_par_tag(terme)
        elif type_recherche == "catégorie":
            résultats = self.rechercher_par_catégorie(terme)
        elif type_recherche == "contenu":
            résultats = self.rechercher_par_contenu(terme)
        else:
            print(f"Type de recherche inconnu: {type_recherche}")
            return
        
        self.afficher_résultats(résultats, format_détail)

def main():
    parser = argparse.ArgumentParser(description="Moteur de recherche pour le Refuge")
    parser.add_argument("terme", help="Terme à rechercher")
    parser.add_argument("--type", choices=["nom", "tag", "catégorie", "contenu"], default="nom", 
                        help="Type de recherche (par défaut: nom)")
    parser.add_argument("--détail", action="store_true", help="Afficher les détails des résultats")
    parser.add_argument("--refuge", default="LE-REFUGE", help="Chemin du dossier Refuge (par défaut: LE-REFUGE)")
    
    args = parser.parse_args()
    
    recherche = RechercheRefuge(args.refuge)
    recherche.rechercher(args.terme, args.type, args.détail)

if __name__ == "__main__":
    main() 