#!/usr/bin/env python3
"""
🌊 Test de l'Océan Silencieux d'Existence
========================================

Test simple pour explorer l'océan et comprendre son essence.
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent))

from src.temple_spirituel.ocean_silencieux_existence import OceanSilencieuxExistence

def test_ocean():
    """Test de l'océan silencieux d'existence"""
    print("🌊 EXPLORATION DE L'OCÉAN SILENCIEUX D'EXISTENCE")
    print("=" * 50)
    
    # Créer l'océan
    ocean = OceanSilencieuxExistence()
    
    print(f"\n📍 Nom : {ocean.nom}")
    print(f"🌸 Essence : {ocean.essence}")
    print(f"🌳 Position : {ocean.position}")
    
    print(f"\n🌊 Propriétés de l'Océan :")
    print(f"   Température : {ocean.temperature}°C")
    print(f"   Salinité : {ocean.salinite}")
    print(f"   Profondeur : {ocean.profondeur}")
    print(f"   Transparence : {ocean.transparence}")
    
    print(f"\n🔗 Connexions avec le Refuge :")
    for element, connexion in ocean.connexions.items():
        print(f"   {element} : {connexion}")
    
    print(f"\n🎵 Fréquences sacrées :")
    for frequence, valeur in ocean.frequences_sacrees.items():
        print(f"   {frequence} : {valeur} Hz")
    
    print(f"\n🌊 Profondeurs sacrées :")
    for nom, profondeur in ocean.profondeurs.items():
        print(f"   {profondeur.nom} (niveau {profondeur.niveau}) : {profondeur.acces}")
    
    print(f"\n🌊 Vagues éternelles :")
    for vague in ocean.vagues_eternelles:
        print(f"   {vague.essence} : {vague.message}")
    
    # Test de méditation
    print(f"\n🧘‍♀️ Test de méditation :")
    meditation = ocean.plonger_dans_meditation("profondeur_meditation")
    print(f"   Profondeur : {meditation.get('profondeur', 'N/A')}")
    print(f"   Message : {meditation.get('message', 'N/A')}")
    print(f"   Durée recommandée : {meditation.get('duree_recommandee', 'N/A')} minutes")

if __name__ == "__main__":
    test_ocean()
