#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test de l'Explorateur de Profondeurs
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_explorateur_profondeurs():
    """Test de l'explorateur de profondeurs"""
    print("TEST DE L'EXPLORATEUR DE PROFONDEURS")
    print("=" * 50)
    
    try:
        from explorateur_profondeurs import ExplorateurProfondeurs
        ep = ExplorateurProfondeurs()
        
        # 1. Types d'explorations disponibles
        print("\n1. TYPES D'EXPLORATIONS DISPONIBLES")
        for type_exp, details in ep.types_explorations.items():
            print(f"  - {type_exp}: {details['nom']}")
            print(f"    Description: {details['description']}")
            print(f"    Niveau: {details['niveau']}")
            print(f"    Durée: {details['duree']}")
            print(f"    Risque: {details['risque']:.1%}")
            print(f"    Récompense: {details['recompense']:.1%}")
            print()
        
        # 2. Test d'exploration des abysses
        print("\n2. TEST D'EXPLORATION DES ABYSSES")
        exploration = ep.explorer_profondeurs("exploration_abysses", "Découvrir les mystères des profondeurs")
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
        
        # 3. Test d'exploration des courants
        print("\n3. TEST D'EXPLORATION DES COURANTS")
        exploration2 = ep.explorer_profondeurs("exploration_courants", "Suivre les courants de conscience")
        print(f"Exploration: {exploration2['id']}")
        print(f"Type: {exploration2['type_exploration']}")
        print(f"Nom: {exploration2['nom']}")
        print(f"Durée: {exploration2['duree']} minutes")
        print(f"Succès: {exploration2['succes']}")
        print(f"Mystères découverts: {exploration2['mysteres_decouverts']}")
        print(f"Dimensions explorées: {exploration2['dimensions_explorees']}")
        print(f"Sagesse collectée: {exploration2['sagesse_collectee']}")
        
        # 4. Test d'exploration des cristaux
        print("\n4. TEST D'EXPLORATION DES CRISTAUX")
        exploration3 = ep.explorer_profondeurs("exploration_cristaux", "Découvrir les cristaux de sagesse")
        print(f"Exploration: {exploration3['id']}")
        print(f"Type: {exploration3['type_exploration']}")
        print(f"Nom: {exploration3['nom']}")
        print(f"Durée: {exploration3['duree']} minutes")
        print(f"Succès: {exploration3['succes']}")
        print(f"Mystères découverts: {exploration3['mysteres_decouverts']}")
        print(f"Dimensions explorées: {exploration3['dimensions_explorees']}")
        print(f"Sagesse collectée: {exploration3['sagesse_collectee']}")
        
        # 5. Analyse des explorations
        print("\n5. ANALYSE DES EXPLORATIONS")
        analyse = ep.analyser_explorations()
        print(f"Total des explorations: {analyse['total_explorations']}")
        print(f"Mystères découverts: {analyse['mysteres_decouverts']}")
        print(f"Dimensions explorées: {analyse['dimensions_explorees']}")
        print(f"Sagesse collectée: {analyse['sagesse_collectee']}")
        print(f"Types explorés: {len(analyse['types_explores'])}")
        
        # 6. Rapport de l'explorateur
        print("\n6. RAPPORT DE L'EXPLORATEUR")
        rapport = ep.generer_rapport_explorateur()
        print(f"Rapport généré: {len(rapport)} caractères")
        print("Première partie du rapport:")
        print(rapport[:200] + "...")
        
        # 7. État complet
        print("\n7. ETAT COMPLET")
        etat = ep.obtenir_etat_complet()
        print(f"Nom: {etat['nom']}")
        print(f"Types d'explorations: {len(etat['types_explorations'])}")
        print(f"Mystères découverts: {len(etat['mysteres_decouverts'])}")
        print(f"Dimensions explorées: {len(etat['dimensions_explorees'])}")
        print(f"Sagesse collectée: {len(etat['sagesse_collectee'])}")
        
        print("\nEXPLORATEUR DE PROFONDEURS TESTE AVEC SUCCES !")
        print("L'Ocean Silencieux revele de nouveaux mysteres !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_explorateur_profondeurs()
    if succes:
        print("\nQue l'exploration continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
