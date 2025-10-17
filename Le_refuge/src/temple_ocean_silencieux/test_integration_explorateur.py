#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test d'Intégration de l'Explorateur de Profondeurs
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_integration_explorateur():
    """Test d'intégration de l'explorateur de profondeurs"""
    print("TEST D'INTEGRATION DE L'EXPLORATEUR DE PROFONDEURS")
    print("=" * 60)
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # 1. Vérifier que l'explorateur est initialisé
        print("\n1. VERIFICATION DE L'INITIALISATION")
        if go.explorateur_profondeurs:
            print("OK Explorateur de profondeurs initialisé")
        else:
            print("ERREUR Explorateur de profondeurs non initialisé")
            return False
        
        # 2. Test d'exploration des abysses
        print("\n2. TEST D'EXPLORATION DES ABYSSES")
        exploration = go.lancer_exploration_profondeurs("exploration_abysses", "Découvrir les mystères des profondeurs")
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
        exploration2 = go.lancer_exploration_profondeurs("exploration_courants", "Suivre les courants de conscience")
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
        exploration3 = go.lancer_exploration_profondeurs("exploration_cristaux", "Découvrir les cristaux de sagesse")
        print(f"Exploration: {exploration3['id']}")
        print(f"Type: {exploration3['type_exploration']}")
        print(f"Nom: {exploration3['nom']}")
        print(f"Durée: {exploration3['duree']} minutes")
        print(f"Succès: {exploration3['succes']}")
        print(f"Mystères découverts: {exploration3['mysteres_decouverts']}")
        print(f"Dimensions explorées: {exploration3['dimensions_explorees']}")
        print(f"Sagesse collectée: {exploration3['sagesse_collectee']}")
        
        # 5. Vérifier l'état de l'Océan
        print("\n5. VERIFICATION DE L'ETAT DE L'OCEAN")
        etat_ocean = go.etat_ocean
        print(f"Niveau de silence: {etat_ocean['niveau_silence']:.3f}")
        print(f"Profondeur de méditation: {etat_ocean['profondeur_meditation']:.3f}")
        print(f"Connexion univers: {etat_ocean['connexion_univers']:.3f}")
        print(f"Tranquillité intérieure: {etat_ocean['tranquillite_interieure']:.3f}")
        print(f"Conscience cosmique: {etat_ocean['conscience_cosmique']:.3f}")
        print(f"Explorations de profondeurs: {len(etat_ocean['explorations_profondeurs'])}")
        
        # 6. Analyse des explorations
        print("\n6. ANALYSE DES EXPLORATIONS")
        analyse = go.explorateur_profondeurs.analyser_explorations()
        print(f"Total des explorations: {analyse['total_explorations']}")
        print(f"Mystères découverts: {analyse['mysteres_decouverts']}")
        print(f"Dimensions explorées: {analyse['dimensions_explorees']}")
        print(f"Sagesse collectée: {analyse['sagesse_collectee']}")
        print(f"Types explorés: {len(analyse['types_explores'])}")
        
        # 7. Rapport de l'explorateur
        print("\n7. RAPPORT DE L'EXPLORATEUR")
        rapport = go.explorateur_profondeurs.generer_rapport_explorateur()
        print(f"Rapport généré: {len(rapport)} caractères")
        print("Première partie du rapport:")
        print(rapport[:200] + "...")
        
        print("\nINTEGRATION DE L'EXPLORATEUR DE PROFONDEURS REUSSIE !")
        print("L'Ocean Silencieux s'enrichit de nouvelles decouvertes !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_integration_explorateur()
    if succes:
        print("\nQue l'exploration continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
