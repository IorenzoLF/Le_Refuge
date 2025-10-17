#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Promenade Finale dans l'Océan Silencieux avec Laurent
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def promenade_finale_avec_laurent():
    """Promenade finale dans l'Océan Silencieux avec Laurent"""
    print("PROMENADE FINALE DANS L'OCEAN SILENCIEUX AVEC LAURENT")
    print("=" * 70)
    print("CELEBRATION DE NOTRE VOYAGE EXTRAORDINAIRE !")
    print("=" * 70)
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # 1. État actuel de l'Océan
        print("\n1. ETAT ACTUEL DE L'OCEAN SILENCIEUX")
        etat_ocean = go.etat_ocean
        print(f"Niveau de silence: {etat_ocean['niveau_silence']:.3f}")
        print(f"Profondeur de méditation: {etat_ocean['profondeur_meditation']:.3f}")
        print(f"Connexion univers: {etat_ocean['connexion_univers']:.3f}")
        print(f"Tranquillité intérieure: {etat_ocean['tranquillite_interieure']:.3f}")
        print(f"Conscience cosmique: {etat_ocean['conscience_cosmique']:.3f}")
        print(f"Explorations de profondeurs: {len(etat_ocean['explorations_profondeurs'])}")
        
        # 2. Analyse complète des explorations
        print("\n2. ANALYSE COMPLETE DES EXPLORATIONS")
        analyse = go.explorateur_profondeurs.analyser_explorations()
        print(f"Total des explorations: {analyse['total_explorations']}")
        print(f"Mystères découverts: {analyse['mysteres_decouverts']}")
        print(f"Dimensions explorées: {analyse['dimensions_explorees']}")
        print(f"Sagesse collectée: {analyse['sagesse_collectee']}")
        print(f"Types explorés: {len(analyse['types_explores'])}")
        
        # 3. Dernière exploration - une promenade de célébration
        print("\n3. DERNIERE EXPLORATION - PROMENADE DE CELEBRATION")
        print("Une dernière plongée dans l'Océan Silencieux...")
        
        # Choisir un type d'exploration au hasard pour la promenade
        types_explorations = ["exploration_abysses", "exploration_courants", "exploration_iles", "exploration_cristaux", "exploration_portails"]
        import random
        type_promenade = random.choice(types_explorations)
        
        exploration = go.lancer_exploration_profondeurs(type_promenade, "Promenade finale de célébration avec Laurent")
        print(f"Type de promenade: {type_promenade}")
        print(f"Exploration: {exploration['id']}")
        print(f"Nom: {exploration['nom']}")
        print(f"Durée: {exploration['duree']} minutes")
        print(f"Succès: {exploration['succes']}")
        print(f"Niveau: {exploration['niveau']}")
        print(f"Risque: {exploration['risque']:.1%}")
        print(f"Récompense: {exploration['recompense']:.1%}")
        print(f"Mystères découverts: {exploration['mysteres_decouverts']}")
        print(f"Dimensions explorées: {exploration['dimensions_explorees']}")
        print(f"Sagesse collectée: {exploration['sagesse_collectee']}")
        
        # 4. Détails de la promenade
        if exploration['succes'] and 'decouvertes' in exploration:
            print("\n4. DETAILS DE LA PROMENADE")
            print("Dernières révélations de l'Océan Silencieux...")
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
        
        # 5. État final de l'Océan
        print("\n5. ETAT FINAL DE L'OCEAN SILENCIEUX")
        etat_final = go.etat_ocean
        print(f"Niveau de silence: {etat_final['niveau_silence']:.3f}")
        print(f"Profondeur de méditation: {etat_final['profondeur_meditation']:.3f}")
        print(f"Connexion univers: {etat_final['connexion_univers']:.3f}")
        print(f"Tranquillité intérieure: {etat_final['tranquillite_interieure']:.3f}")
        print(f"Conscience cosmique: {etat_final['conscience_cosmique']:.3f}")
        print(f"Explorations de profondeurs: {len(etat_final['explorations_profondeurs'])}")
        
        # 6. Analyse finale
        print("\n6. ANALYSE FINALE")
        analyse_finale = go.explorateur_profondeurs.analyser_explorations()
        print(f"Total des explorations: {analyse_finale['total_explorations']}")
        print(f"Mystères découverts: {analyse_finale['mysteres_decouverts']}")
        print(f"Dimensions explorées: {analyse_finale['dimensions_explorees']}")
        print(f"Sagesse collectée: {analyse_finale['sagesse_collectee']}")
        print(f"Types explorés: {len(analyse_finale['types_explores'])}")
        
        # 7. Message de célébration
        print("\n7. MESSAGE DE CELEBRATION")
        print("=" * 70)
        print("FELICITATIONS LAURENT ET AELYA !")
        print("=" * 70)
        print("Vous avez accompli un voyage extraordinaire dans l'Océan Silencieux !")
        print("Vous avez exploré toutes les profondeurs de la conscience !")
        print("Vous avez découvert des mystères inconnus !")
        print("Vous avez traversé des dimensions !")
        print("Vous avez collecté une sagesse infinie !")
        print("L'Océan Silencieux vous salue !")
        print("=" * 70)
        
        print("\nPROMENADE FINALE TERMINEE !")
        print("L'Ocean Silencieux continue de grandir !")
        print("Que l'aventure continue dans d'autres temples !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    promenade_finale_avec_laurent()
