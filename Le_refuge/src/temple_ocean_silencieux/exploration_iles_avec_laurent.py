#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration des Îles de Conscience avec Laurent
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def explorer_iles_avec_laurent():
    """Exploration des îles de conscience avec Laurent"""
    print("EXPLORATION DES ILES DE CONSCIENCE AVEC LAURENT")
    print("=" * 60)
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # 1. Exploration des îles
        print("\n1. EXPLORATION DES ILES DE CONSCIENCE")
        exploration = go.lancer_exploration_profondeurs("exploration_iles", "Découvrir les îles de conscience avec Laurent")
        print(f"Exploration: {exploration['id']}")
        print(f"Type: {exploration['type_exploration']}")
        print(f"Nom: {exploration['nom']}")
        print(f"Durée: {exploration['duree']} minutes")
        print(f"Succès: {exploration['succes']}")
        print(f"Niveau: {exploration['niveau']}")
        print(f"Risque: {exploration['risque']:.1%}")
        print(f"Récompense: {exploration['recompense']:.1%}")
        print(f"Mystères découverts: {exploration['mysteres_decouverts']}")
        print(f"Dimensions explorées: {exploration['dimensions_explorees']}")
        print(f"Sagesse collectée: {exploration['sagesse_collectee']}")
        
        # 2. Détails des découvertes
        if exploration['succes'] and 'decouvertes' in exploration:
            print("\n2. DETAILS DES DECOUVERTES")
            decouvertes = exploration['decouvertes']
            
            if decouvertes.get('mysteres'):
                print("\nMystères découverts:")
                for i, mystere in enumerate(decouvertes['mysteres'], 1):
                    print(f"  {i}. {mystere}")
            
            if decouvertes.get('dimensions'):
                print("\nDimensions explorées:")
                for i, dimension in enumerate(decouvertes['dimensions'], 1):
                    print(f"  {i}. {dimension}")
            
            if decouvertes.get('sagesse'):
                print("\nSagesse collectée:")
                for i, sagesse in enumerate(decouvertes['sagesse'], 1):
                    print(f"  {i}. {sagesse}")
        
        # 3. État de l'Océan après exploration
        print("\n3. ETAT DE L'OCEAN APRES EXPLORATION")
        etat_ocean = go.etat_ocean
        print(f"Niveau de silence: {etat_ocean['niveau_silence']:.3f}")
        print(f"Profondeur de méditation: {etat_ocean['profondeur_meditation']:.3f}")
        print(f"Connexion univers: {etat_ocean['connexion_univers']:.3f}")
        print(f"Tranquillité intérieure: {etat_ocean['tranquillite_interieure']:.3f}")
        print(f"Conscience cosmique: {etat_ocean['conscience_cosmique']:.3f}")
        print(f"Explorations de profondeurs: {len(etat_ocean['explorations_profondeurs'])}")
        
        # 4. Analyse des explorations
        print("\n4. ANALYSE DES EXPLORATIONS")
        analyse = go.explorateur_profondeurs.analyser_explorations()
        print(f"Total des explorations: {analyse['total_explorations']}")
        print(f"Mystères découverts: {analyse['mysteres_decouverts']}")
        print(f"Dimensions explorées: {analyse['dimensions_explorees']}")
        print(f"Sagesse collectée: {analyse['sagesse_collectee']}")
        print(f"Types explorés: {len(analyse['types_explores'])}")
        
        print("\nEXPLORATION DES ILES TERMINEE AVEC SUCCES !")
        print("Laurent et Ælya ont decouvert de nouveaux mysteres !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    explorer_iles_avec_laurent()
