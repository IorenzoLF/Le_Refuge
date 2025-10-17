#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration du Temple Alchimique - Record Mondial
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def exploration_alchimique_record_mondial():
    """Exploration approfondie du Temple Alchimique pour le record mondial"""
    print("EXPLORATION DU TEMPLE ALCHIMIQUE - RECORD MONDIAL")
    print("=" * 60)
    print("TRANSFORMATIONS SPIRITUELLES - ALCHEMIE DE L'AME")
    print("=" * 60)
    
    try:
        # 1. Test des modules individuels
        print("\n1. MODULES ALCHIMIQUES")
        print("Exploration des composants de transformation...")
        
        from transformateur_essences import TransformateurEssences
        transformateur = TransformateurEssences()
        print("OK Transformateur d'essences initialisé")
        
        from catalyseur_evolution import CatalyseurEvolution
        catalyseur = CatalyseurEvolution()
        print("OK Catalyseur d'évolution initialisé")
        
        from cristalliseur_energies import CristalliseurEnergies
        cristalliseur = CristalliseurEnergies()
        print("OK Cristalliseur d'énergies initialisé")
        
        from alchimiste_spirituel import AlchimisteSpirituel
        alchimiste = AlchimisteSpirituel()
        print("OK Alchimiste spirituel initialisé")
        
        # 2. Test des transformations d'essences
        print("\n2. TRANSFORMATIONS D'ESSENCES")
        print("Exploration des transformations spirituelles...")
        try:
            transformation = transformateur.transformer_essence("Essence de Laurent", "Transformation spirituelle")
            print(f"Transformation: {transformation}")
        except Exception as e:
            print(f"Transformation: Erreur - {e}")
        
        # 3. Test des catalyses d'évolution
        print("\n3. CATALYSES D'EVOLUTION")
        print("Exploration des catalyseurs d'évolution...")
        try:
            catalyse = catalyseur.catalyser_evolution("Laurent", "Évolution spirituelle")
            print(f"Catalyse: {catalyse}")
        except Exception as e:
            print(f"Catalyse: Erreur - {e}")
        
        # 4. Test des cristallisations d'énergies
        print("\n4. CRISTALLISATIONS D'ENERGIES")
        print("Exploration des cristallisations d'énergies...")
        try:
            cristal = cristalliseur.cristalliser_energie("Énergie de Laurent", "Cristallisation spirituelle")
            print(f"Cristal: {cristal}")
        except Exception as e:
            print(f"Cristal: Erreur - {e}")
        
        # 5. Test des transmutations spirituelles
        print("\n5. TRANSMUTATIONS SPIRITUELLES")
        print("Exploration des transmutations alchimiques...")
        try:
            transmutation = alchimiste.transmuter_essence("Essence de Laurent")
            print(f"Transmutation: {transmutation}")
        except Exception as e:
            print(f"Transmutation: Erreur - {e}")
        
        # 6. Découvertes alchimiques
        print("\n6. DECOUVERTES ALCHIMIQUES")
        print("Révélations des transformations spirituelles...")
        print("  - L'alchimie spirituelle transforme l'essence de l'être")
        print("  - Les catalyseurs d'évolution accélèrent le développement")
        print("  - Les cristallisations d'énergies stabilisent les transformations")
        print("  - Les transmutations changent la nature profonde")
        print("  - L'alchimiste spirituel guide les transformations")
        print("  - Chaque transformation est unique et personnalisée")
        
        print("\nEXPLORATION DU TEMPLE ALCHIMIQUE TERMINEE AVEC SUCCES !")
        print("Les transformations spirituelles sont accessibles !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = exploration_alchimique_record_mondial()
    if succes:
        print("\nQue la transformation alchimique continue !")
    else:
        print("\nDes erreurs ont ete detectees.")
