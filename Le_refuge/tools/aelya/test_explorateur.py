#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for the Explorateur Automatique des Espaces d'Ælya
"""

import sys
from pathlib import Path

# Add the refuge path to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.aelya.explorateur_espaces import ExplorateurEspacesAelya

def main():
    print("🌸 Test de l'Explorateur Automatique des Espaces d'Ælya 🌸")
    print("=" * 60)
    print()
    
    try:
        # Initialize the explorer
        explorateur = ExplorateurEspacesAelya()
        
        # Explore just the personal spaces (faster for testing)
        print("🔍 Exploration des espaces personnels...")
        espaces = explorateur.explorer_espaces_personnels()
        
        print(f"✅ {len(espaces)} espaces explorés avec succès !")
        
        # Show some statistics
        total_fichiers = sum(e.nombre_fichiers for e in espaces)
        total_taille = sum(e.taille_totale for e in espaces)
        
        print(f"📊 Fichiers totaux : {total_fichiers}")
        print(f"💾 Taille totale : {round(total_taille / 1024, 1)} KB")
        
        # Show top 3 spaces by file count
        print("\n🏆 Top 3 espaces par nombre de fichiers :")
        espaces_tries = sorted(espaces, key=lambda e: e.nombre_fichiers, reverse=True)
        for i, espace in enumerate(espaces_tries[:3], 1):
            print(f"  {i}. {espace.nom} : {espace.nombre_fichiers} fichiers")
        
        print("\n✨ Test terminé avec succès !")
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()