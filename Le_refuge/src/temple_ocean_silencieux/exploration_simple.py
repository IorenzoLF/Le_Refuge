#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration Simple du Temple de l'Océan Silencieux
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def explorer_ocean_silencieux():
    """Exploration simple de l'Océan Silencieux"""
    print("EXPLORATION DE L'OCEAN SILENCIEUX")
    print("=" * 50)
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # 1. Accueil
        print("\n1. ACCUEIL DU TEMPLE")
        accueil = go.accueillir_visiteur("Laurent")
        print(f"Message: {accueil['message']}")
        etat = accueil['etat_ocean']
        print(f"Niveau de silence: {etat['niveau_silence']:.3f}")
        print(f"Profondeur de méditation: {etat['profondeur_meditation']:.3f}")
        print(f"Connexion univers: {etat['connexion_univers']:.3f}")
        print(f"Tranquillité intérieure: {etat['tranquillite_interieure']:.3f}")
        print(f"Conscience cosmique: {etat['conscience_cosmique']:.3f}")
        
        # 2. Historique des méditations
        print(f"\n2. HISTORIQUE DES MEDITATIONS")
        print(f"Total des méditations: {len(etat['sessions_meditation'])}")
        for i, med in enumerate(etat['sessions_meditation'][-3:], 1):
            print(f"  {i}. {med['id']} - {med['type']} - {med['duree']}min")
        
        # 3. Connexions univers
        print(f"\n3. CONNEXIONS UNIVERS")
        print(f"Total des connexions: {len(etat['connexions_univers'])}")
        for i, conn in enumerate(etat['connexions_univers'][-3:], 1):
            print(f"  {i}. {conn['id']} - {conn['type']} - {conn['destination']}")
        
        # 4. Révélations
        print(f"\n4. REVELATIONS DE L'OCEAN")
        print(f"Total des révélations: {len(etat['revelations_ocean'])}")
        for i, rev in enumerate(etat['revelations_ocean'][-3:], 1):
            print(f"  {i}. {rev['id']} - Profondeur: {rev['profondeur']}")
            print(f"     Contenu: {rev['revelation'][:60]}...")
        
        # 5. États de transcendance
        print(f"\n5. ETATS DE TRANSCENDANCE")
        print(f"Total des états: {len(etat['etats_transcendance'])}")
        for i, trans in enumerate(etat['etats_transcendance'][-3:], 1):
            print(f"  {i}. {trans['id']} - Niveau: {trans['niveau_transcendance']:.3f}")
            print(f"     Expériences: {len(trans['experiences'])}")
            print(f"     Révélations: {len(trans['revelations'])}")
        
        # 6. Moments de sérénité
        print(f"\n6. MOMENTS DE SERENITE")
        print(f"Total des moments: {len(etat['moments_serenite'])}")
        for i, moment in enumerate(etat['moments_serenite'][-3:], 1):
            print(f"  {i}. {moment['id']} - Intensité: {moment['intensite']:.3f}")
            print(f"     Moment: {moment['moment']}")
            print(f"     Impact: {moment['impact_ocean']:.3f}")
        
        print("\nEXPLORATION TERMINEE AVEC SUCCES !")
        print("L'Ocean Silencieux revele ses mysteres !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    explorer_ocean_silencieux()
