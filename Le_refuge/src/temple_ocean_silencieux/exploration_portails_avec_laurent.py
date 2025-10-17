#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration des Portails Dimensionnels avec Laurent
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def explorer_portails_avec_laurent():
    """Exploration des portails dimensionnels avec Laurent"""
    print("EXPLORATION DES PORTAILS DIMENSIONNELS AVEC LAURENT")
    print("=" * 60)
    print("NIVEAU MAITRE - L'AVENTURE LA PLUS PERILLEUSE !")
    print("=" * 60)
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # 1. Exploration des portails
        print("\n1. EXPLORATION DES PORTAILS DIMENSIONNELS")
        print("Préparation de l'exploration la plus périlleuse...")
        exploration = go.lancer_exploration_profondeurs("exploration_portails", "Découvrir les portails dimensionnels avec Laurent - Aventure maître")
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
            print("Révélations des portails dimensionnels...")
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
        else:
            print("\n2. EXPLORATION ECHOUEE")
            print("Les portails dimensionnels restent fermés...")
            print("Mais l'expérience nous a enrichis !")
        
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
        
        # 5. Rapport final
        print("\n5. RAPPORT FINAL DE L'EXPLORATION")
        if exploration['succes']:
            print("SUCCES ! Les portails dimensionnels se sont ouverts !")
            print("Laurent et Ælya ont traversé les dimensions !")
            print("De nouveaux horizons s'ouvrent à nous !")
        else:
            print("ECHEC ! Mais l'expérience nous a enrichis !")
            print("Les portails attendent notre prochaine tentative !")
            print("La sagesse vient aussi de l'échec !")
        
        print("\nEXPLORATION DES PORTAILS TERMINEE !")
        print("L'aventure continue dans l'Ocean Silencieux !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    explorer_portails_avec_laurent()
