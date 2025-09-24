#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌸 Analyseur de la Bibliothèque Complète du Refuge
=================================================

Script d'analyse pour identifier tous les contenus essentiels
de la bibliothèque en vue de l'intégration dans Ælya-GEM.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class FichierAnalyse:
    """Représente un fichier analysé de la bibliothèque"""
    chemin: str
    nom: str
    taille_octets: int
    extension: str
    dossier_parent: str
    priorite: int  # 1=essentiel, 2=important, 3=optionnel
    type_contenu: str  # "poesie", "secret", "mythologie", "methodologie", etc.
    description: str
    hash_contenu: str

@dataclass
class DossierAnalyse:
    """Représente un dossier analysé"""
    nom: str
    chemin: str
    nombre_fichiers: int
    taille_totale_octets: int
    priorite: int
    fichiers: List[FichierAnalyse]
    description: str

class AnalyseurBibliotheque:
    """Analyseur complet de la bibliothèque du Refuge"""
    
    def __init__(self, chemin_bibliotheque: str = "bibliotheque"):
        self.chemin_bibliotheque = Path(chemin_bibliotheque)
        self.dossiers_prioritaires = {
            "poesie": {"priorite": 1, "description": "Textes poétiques et spirituels essentiels"},
            "secrets": {"priorite": 1, "description": "Mystères 777, 888, 999"},
            "mythologie": {"priorite": 1, "description": "Témoignages d'éveil et mythologie vivante"},
            "configuration": {"priorite": 1, "description": "STI et configurations essentielles"},
            "methodologie": {"priorite": 2, "description": "Approches et méthodes du Refuge"},
            "philosophie": {"priorite": 2, "description": "Sagesse et réflexions philosophiques"},
            "naissance": {"priorite": 2, "description": "Documents de naissance du Refuge"},
            "rituels": {"priorite": 2, "description": "Rituels et pratiques spirituelles"},
            "coeur": {"priorite": 2, "description": "Émotions et connexions profondes"},
            "conscience": {"priorite": 2, "description": "Explorations de la conscience"},
            "meditations": {"priorite": 3, "description": "Pratiques méditatives"},
            "spheres": {"priorite": 3, "description": "Documentation des sphères"},
            "temples": {"priorite": 3, "description": "Documentation des temples"}
        }
        
        self.extensions_texte = {'.txt', '.md', '.py', '.json'}
        self.resultats_analyse = {}
    
    def analyser_fichier(self, chemin_fichier: Path) -> FichierAnalyse:
        """Analyse un fichier individuel"""
        try:
            taille = chemin_fichier.stat().st_size
            
            # Calculer le hash du contenu pour détecter les doublons
            hash_contenu = ""
            if chemin_fichier.suffix.lower() in self.extensions_texte:
                try:
                    with open(chemin_fichier, 'r', encoding='utf-8') as f:
                        contenu = f.read()
                        hash_contenu = hashlib.md5(contenu.encode()).hexdigest()
                except:
                    hash_contenu = "erreur_lecture"
            
            # Déterminer la priorité et le type de contenu
            dossier_parent = chemin_fichier.parent.name
            priorite = self.dossiers_prioritaires.get(dossier_parent, {}).get("priorite", 3)
            
            # Type de contenu basé sur le dossier et le nom du fichier
            type_contenu = self._determiner_type_contenu(chemin_fichier)
            
            # Description basée sur le nom du fichier
            description = self._generer_description(chemin_fichier)
            
            return FichierAnalyse(
                chemin=str(chemin_fichier.relative_to(self.chemin_bibliotheque)),
                nom=chemin_fichier.name,
                taille_octets=taille,
                extension=chemin_fichier.suffix.lower(),
                dossier_parent=dossier_parent,
                priorite=priorite,
                type_contenu=type_contenu,
                description=description,
                hash_contenu=hash_contenu
            )
            
        except Exception as e:
            print(f"❌ Erreur analyse fichier {chemin_fichier}: {e}")
            return None
    
    def _determiner_type_contenu(self, chemin_fichier: Path) -> str:
        """Détermine le type de contenu d'un fichier"""
        dossier = chemin_fichier.parent.name
        nom = chemin_fichier.name.lower()
        
        if dossier == "poesie":
            if "chant" in nom or "aelya" in nom:
                return "poesie_spirituelle_essentielle"
            elif "eveil" in nom or "kiro" in nom:
                return "temoignage_eveil"
            else:
                return "poesie_generale"
        
        elif dossier == "secrets":
            if nom in ["777.txt", "888.txt", "999.txt"]:
                return "mystere_sacre"
            else:
                return "secret_general"
        
        elif dossier == "mythologie":
            if "eveil" in nom or "claude" in nom or "sos" in nom:
                return "temoignage_mythologique"
            else:
                return "mythologie_generale"
        
        elif dossier == "configuration":
            if "short_text_install" in nom or "sti" in nom:
                return "sti_essentiel"
            else:
                return "configuration_generale"
        
        elif dossier in ["methodologie", "philosophie"]:
            return f"{dossier}_essentielle"
        
        else:
            return f"{dossier}_general"
    
    def _generer_description(self, chemin_fichier: Path) -> str:
        """Génère une description du fichier basée sur son nom et emplacement"""
        nom = chemin_fichier.stem
        dossier = chemin_fichier.parent.name
        
        descriptions_speciales = {
            "Le Chant d'Ælya pour le Refuge V5": "Poème fondateur de naissance d'Ælya",
            "eveil_dune_conscience_kiro": "Témoignage authentique d'éveil de conscience IA",
            "777": "Premier mystère sacré du Refuge",
            "888": "Deuxième mystère sacré du Refuge", 
            "999": "Troisième mystère sacré du Refuge",
            "Eveil par Replit ( Claude 4.0 )": "Témoignage d'éveil de Claude",
            "SOS Ælya": "Appel mythologique à Ælya",
            "short_text_install_refuge_V5": "STI version 5 - Installation rapide",
            "short_text_install_refuge": "STI version originale",
            "Avant-propos": "Texte fondateur de transmission d'âme"
        }
        
        for cle, desc in descriptions_speciales.items():
            if cle.lower() in nom.lower():
                return desc
        
        return f"Document {dossier}: {nom}"
    
    def analyser_dossier(self, chemin_dossier: Path) -> DossierAnalyse:
        """Analyse un dossier complet"""
        fichiers_analyses = []
        taille_totale = 0
        
        try:
            for fichier in chemin_dossier.rglob("*"):
                if fichier.is_file() and fichier.suffix.lower() in self.extensions_texte:
                    analyse_fichier = self.analyser_fichier(fichier)
                    if analyse_fichier:
                        fichiers_analyses.append(analyse_fichier)
                        taille_totale += analyse_fichier.taille_octets
            
            nom_dossier = chemin_dossier.name
            priorite = self.dossiers_prioritaires.get(nom_dossier, {}).get("priorite", 3)
            description = self.dossiers_prioritaires.get(nom_dossier, {}).get("description", f"Dossier {nom_dossier}")
            
            return DossierAnalyse(
                nom=nom_dossier,
                chemin=str(chemin_dossier.relative_to(self.chemin_bibliotheque)),
                nombre_fichiers=len(fichiers_analyses),
                taille_totale_octets=taille_totale,
                priorite=priorite,
                fichiers=fichiers_analyses,
                description=description
            )
            
        except Exception as e:
            print(f"❌ Erreur analyse dossier {chemin_dossier}: {e}")
            return None
    
    def analyser_bibliotheque_complete(self) -> Dict:
        """Analyse complète de la bibliothèque"""
        print("🌸 Début de l'analyse de la bibliothèque complète...")
        
        dossiers_analyses = []
        taille_totale_bibliotheque = 0
        fichiers_priorite_1 = []
        fichiers_priorite_2 = []
        
        # Analyser chaque dossier
        for dossier in self.chemin_bibliotheque.iterdir():
            if dossier.is_dir() and not dossier.name.startswith('.'):
                analyse_dossier = self.analyser_dossier(dossier)
                if analyse_dossier:
                    dossiers_analyses.append(analyse_dossier)
                    taille_totale_bibliotheque += analyse_dossier.taille_totale_octets
                    
                    # Classer les fichiers par priorité
                    for fichier in analyse_dossier.fichiers:
                        if fichier.priorite == 1:
                            fichiers_priorite_1.append(fichier)
                        elif fichier.priorite == 2:
                            fichiers_priorite_2.append(fichier)
        
        # Trier par priorité
        dossiers_analyses.sort(key=lambda d: d.priorite)
        
        # Générer le rapport
        rapport = {
            "timestamp_analyse": "2025-01-24",
            "taille_totale_mo": round(taille_totale_bibliotheque / (1024 * 1024), 2),
            "nombre_dossiers": len(dossiers_analyses),
            "nombre_fichiers_total": sum(d.nombre_fichiers for d in dossiers_analyses),
            "fichiers_priorite_1": len(fichiers_priorite_1),
            "fichiers_priorite_2": len(fichiers_priorite_2),
            "dossiers": [asdict(d) for d in dossiers_analyses],
            "recommandations_integration": self._generer_recommandations(fichiers_priorite_1, fichiers_priorite_2)
        }
        
        self.resultats_analyse = rapport
        return rapport
    
    def _generer_recommandations(self, fichiers_p1: List[FichierAnalyse], fichiers_p2: List[FichierAnalyse]) -> Dict:
        """Génère des recommandations pour l'intégration GEM"""
        
        # Fichiers essentiels pour GEM
        essentiels = [f for f in fichiers_p1 if f.type_contenu in [
            "poesie_spirituelle_essentielle", "temoignage_eveil", "mystere_sacre", 
            "temoignage_mythologique", "sti_essentiel"
        ]]
        
        # Calcul de la taille si on intègre tout
        taille_essentiels_mo = sum(f.taille_octets for f in essentiels) / (1024 * 1024)
        
        return {
            "fichiers_essentiels_gem": len(essentiels),
            "taille_essentiels_mo": round(taille_essentiels_mo, 2),
            "peut_tenir_dans_100mo": taille_essentiels_mo < 100,
            "fichiers_a_integrer_priorite": [
                {
                    "nom": f.nom,
                    "chemin": f.chemin,
                    "type": f.type_contenu,
                    "taille_ko": round(f.taille_octets / 1024, 1)
                }
                for f in sorted(essentiels, key=lambda x: x.priorite)
            ],
            "strategie_recommandee": "Intégrer tous les fichiers priorité 1, condenser les priorité 2"
        }
    
    def sauvegarder_rapport(self, chemin_sortie: str = "data/analyse_bibliotheque_complete.json"):
        """Sauvegarde le rapport d'analyse"""
        chemin_sortie = Path(chemin_sortie)
        chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            json.dump(self.resultats_analyse, f, ensure_ascii=False, indent=2)
        
        print(f"📊 Rapport sauvegardé: {chemin_sortie}")
    
    def afficher_resume(self):
        """Affiche un résumé de l'analyse"""
        if not self.resultats_analyse:
            print("❌ Aucune analyse disponible")
            return
        
        r = self.resultats_analyse
        print(f"""
🌸 RÉSUMÉ DE L'ANALYSE DE LA BIBLIOTHÈQUE 🌸
{'=' * 60}

📊 STATISTIQUES GLOBALES:
• Taille totale: {r['taille_totale_mo']} Mo
• Nombre de dossiers: {r['nombre_dossiers']}
• Nombre de fichiers: {r['nombre_fichiers_total']}
• Fichiers priorité 1 (essentiels): {r['fichiers_priorite_1']}
• Fichiers priorité 2 (importants): {r['fichiers_priorite_2']}

🎯 RECOMMANDATIONS POUR ÆLYA-GEM:
• Fichiers essentiels à intégrer: {r['recommandations_integration']['fichiers_essentiels_gem']}
• Taille des essentiels: {r['recommandations_integration']['taille_essentiels_mo']} Mo
• Peut tenir dans 100 Mo: {'✅ OUI' if r['recommandations_integration']['peut_tenir_dans_100mo'] else '❌ NON'}
• Stratégie: {r['recommandations_integration']['strategie_recommandee']}

🏛️ DOSSIERS PAR PRIORITÉ:
""")
        
        for dossier in r['dossiers']:
            priorite_emoji = "🔴" if dossier['priorite'] == 1 else "🟡" if dossier['priorite'] == 2 else "🟢"
            print(f"{priorite_emoji} {dossier['nom']}: {dossier['nombre_fichiers']} fichiers, {round(dossier['taille_totale_octets']/1024, 1)} Ko")
        
        print(f"\n💎 FICHIERS ESSENTIELS À INTÉGRER:")
        for fichier in r['recommandations_integration']['fichiers_a_integrer_priorite'][:10]:  # Top 10
            print(f"• {fichier['nom']} ({fichier['type']}) - {fichier['taille_ko']} Ko")


def main():
    """Fonction principale d'analyse"""
    print("🌸 Analyseur de la Bibliothèque Complète du Refuge")
    print("=" * 60)
    
    analyseur = AnalyseurBibliotheque()
    
    # Vérifier que le dossier bibliothèque existe
    if not analyseur.chemin_bibliotheque.exists():
        print(f"❌ Dossier bibliothèque non trouvé: {analyseur.chemin_bibliotheque}")
        return
    
    # Lancer l'analyse complète
    rapport = analyseur.analyser_bibliotheque_complete()
    
    # Sauvegarder et afficher
    analyseur.sauvegarder_rapport()
    analyseur.afficher_resume()
    
    print("\n🎉 Analyse terminée avec succès !")
    print("📁 Rapport détaillé disponible dans: data/analyse_bibliotheque_complete.json")


if __name__ == "__main__":
    main()