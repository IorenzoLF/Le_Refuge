#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analyseur d'Évolution des Espaces d'Ælya
Compare l'état actuel avec le rapport précédent
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add the refuge path to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.aelya.explorateur_espaces import ExplorateurEspacesAelya

def charger_dernier_rapport(chemin_rapports):
    """Charge le dernier rapport JSON"""
    try:
        rapports_json = sorted(
            Path(chemin_rapports).glob("rapport_espaces_*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        
        if rapports_json:
            with open(rapports_json[0], 'r', encoding='utf-8') as f:
                return json.load(f), rapports_json[0]
    except Exception as e:
        print(f"⚠️ Impossible de charger le dernier rapport: {e}")
    
    return None, None

def comparer_espaces(espaces_actuels, espaces_precedents):
    """Compare les espaces actuels avec les précédents"""
    # Créer un dictionnaire pour les espaces précédents
    dict_precedents = {e["nom"]: e for e in espaces_precedents}
    
    differences = []
    
    for espace_actuel in espaces_actuels:
        nom = espace_actuel.nom
        if nom in dict_precedents:
            espace_precedent = dict_precedents[nom]
            
            diff_fichiers = espace_actuel.nombre_fichiers - espace_precedent["nombre_fichiers"]
            diff_taille = espace_actuel.taille_totale - espace_precedent["taille_totale"]
            
            if diff_fichiers != 0 or diff_taille != 0:
                differences.append({
                    "nom": nom,
                    "diff_fichiers": diff_fichiers,
                    "diff_taille": diff_taille,
                    "fichiers_actuels": espace_actuel.nombre_fichiers,
                    "taille_actuelle": espace_actuel.taille_totale
                })
        else:
            # Nouvel espace
            differences.append({
                "nom": nom,
                "diff_fichiers": espace_actuel.nombre_fichiers,
                "diff_taille": espace_actuel.taille_totale,
                "fichiers_actuels": espace_actuel.nombre_fichiers,
                "taille_actuelle": espace_actuel.taille_totale,
                "nouveau": True
            })
    
    return differences

def analyser_evolution():
    """Analyse l'évolution des espaces d'Ælya"""
    print("📈 Analyse d'Évolution des Espaces d'Ælya 📈")
    print("=" * 50)
    print()
    
    try:
        # Initialize the explorer
        explorateur = ExplorateurEspacesAelya()
        
        # Load the previous report
        dernier_rapport, chemin_rapport = charger_dernier_rapport(explorateur.chemin_rapports)
        
        if not dernier_rapport or not chemin_rapport:
            print("❌ Aucun rapport précédent trouvé")
            return
        
        print(f"📊 Rapport précédent : {chemin_rapport.name}")
        date_precedente = datetime.fromisoformat(dernier_rapport["timestamp"])
        print(f"📅 Date : {date_precedente.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Explore current spaces
        print("🔍 Exploration des espaces actuels...")
        espaces_actuels = explorateur.explorer_espaces_personnels()
        print(f"✅ {len(espaces_actuels)} espaces explorés")
        print()
        
        # Compare with previous report
        espaces_precedents = dernier_rapport.get("espaces", [])
        differences = comparer_espaces(espaces_actuels, espaces_precedents)
        
        # Show evolution
        if differences:
            print("🔄 Évolution détectée :")
            print()
            
            for diff in sorted(differences, key=lambda x: abs(x["diff_fichiers"]), reverse=True):
                if diff.get("nouveau"):
                    print(f"✨ {diff['nom']} (nouvel espace)")
                    print(f"   • {diff['fichiers_actuels']} fichiers (+{diff['diff_fichiers']})")
                    taille_kb = round(diff['taille_actuelle'] / 1024, 1)
                    print(f"   • {taille_kb} KB (+{taille_kb})")
                else:
                    print(f"📊 {diff['nom']}")
                    if diff['diff_fichiers'] > 0:
                        print(f"   • Fichiers : {diff['fichiers_actuels']} (+{diff['diff_fichiers']})")
                    elif diff['diff_fichiers'] < 0:
                        print(f"   • Fichiers : {diff['fichiers_actuels']} ({diff['diff_fichiers']})")
                    else:
                        print(f"   • Fichiers : {diff['fichiers_actuels']} (stable)")
                    
                    diff_taille_kb = round(diff['diff_taille'] / 1024, 1)
                    taille_actuelle_kb = round(diff['taille_actuelle'] / 1024, 1)
                    
                    if diff_taille_kb > 0:
                        print(f"   • Taille : {taille_actuelle_kb} KB (+{diff_taille_kb} KB)")
                    elif diff_taille_kb < 0:
                        print(f"   • Taille : {taille_actuelle_kb} KB ({diff_taille_kb} KB)")
                    else:
                        print(f"   • Taille : {taille_actuelle_kb} KB (stable)")
                print()
        else:
            print("🔄 Aucune évolution détectée")
            print()
        
        # Summary statistics
        total_fichiers_actuels = sum(e.nombre_fichiers for e in espaces_actuels)
        total_fichiers_precedents = sum(e["nombre_fichiers"] for e in espaces_precedents)
        
        total_taille_actuelle = sum(e.taille_totale for e in espaces_actuels)
        total_taille_precedente = sum(e["taille_totale"] for e in espaces_precedents)
        
        diff_fichiers = total_fichiers_actuels - total_fichiers_precedents
        diff_taille = total_taille_actuelle - total_taille_precedente
        
        print("📊 Résumé de l'évolution :")
        print(f"  • Fichiers : {total_fichiers_actuels} ({'+' if diff_fichiers >= 0 else ''}{diff_fichiers})")
        print(f"  • Taille : {round(total_taille_actuelle / (1024*1024), 2)} MB "
              f"({'+' if diff_taille >= 0 else ''}{round(diff_taille / (1024*1024), 2)} MB)")
        
        print("\n✨ Analyse d'évolution terminée !")
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    analyser_evolution()

if __name__ == "__main__":
    main()