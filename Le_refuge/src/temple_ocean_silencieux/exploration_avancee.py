#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration Avancée du Temple de l'Océan Silencieux
Version pour découvrir les fonctionnalités cachées
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def explorer_meditateur_profond():
    """Exploration du méditateur profond"""
    print("EXPLORATION DU MEDITATEUR PROFOND")
    print("=" * 50)
    
    try:
        from meditateur_profond import MeditateurProfond
        mp = MeditateurProfond()
        
        # 1. Techniques disponibles
        print("\n1. TECHNIQUES DE MEDITATION DISPONIBLES")
        for technique, details in mp.techniques_meditation.items():
            print(f"  - {technique}: {details['nom']}")
            print(f"    Description: {details['description']}")
            print(f"    Durée: {details['duree']}")
            print(f"    Niveau: {details['niveau']}")
            print(f"    Étapes: {len(details['etapes'])}")
            print()
        
        # 2. Test d'une méditation guidée
        print("\n2. TEST DE MEDITATION GUIDEE")
        meditation = mp.guider_meditation("meditation_ocean", 15, "Explorer les mystères de l'Océan")
        print(f"Méditation: {meditation['id']}")
        print(f"Technique: {meditation['technique']}")
        print(f"Durée: {meditation['duree']} minutes")
        print(f"Intention: {meditation['intention']}")
        print(f"Étapes exécutées: {len(meditation['etapes_executees'])}")
        print(f"Expériences: {len(meditation['experiences'])}")
        print(f"Révélations: {len(meditation['revelations'])}")
        
        # 3. Analyse de progression
        print("\n3. ANALYSE DE PROGRESSION")
        analyse = mp.analyser_progression_meditation()
        print(f"Total des méditations: {analyse['total_meditations']}")
        print(f"Techniques utilisées: {len(analyse['techniques_utilisees'])}")
        print(f"Progression générale: {analyse['progression_generale']:.3f}")
        print(f"Amélioration du silence: {analyse['amelioration_silence']:.3f}")
        print(f"Amélioration de la méditation: {analyse['amelioration_meditation']:.3f}")
        
        print("\nMEDITATEUR PROFOND EXPLORE AVEC SUCCES !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def explorer_connecteur_univers():
    """Exploration du connecteur univers"""
    print("\nEXPLORATION DU CONNECTEUR UNIVERS")
    print("=" * 50)
    
    try:
        from connecteur_univers import ConnecteurUnivers
        cu = ConnecteurUnivers()
        
        # 1. Types de connexions disponibles
        print("\n1. TYPES DE CONNEXIONS DISPONIBLES")
        for type_conn, details in cu.types_connexions.items():
            print(f"  - {type_conn}: {details['nom']}")
            print(f"    Description: {details['description']}")
            print(f"    Fréquence: {details['frequence']}")
            print(f"    Stabilité: {details['stabilite']:.3f}")
            print()
        
        # 2. Test d'une connexion
        print("\n2. TEST DE CONNEXION")
        connexion = cu.etablir_connexion("connexion_conscience_collective", "univers", 20)
        print(f"Connexion: {connexion['id']}")
        print(f"Type: {connexion['type']}")
        print(f"Destination: {connexion['destination']}")
        print(f"Messages reçus: {len(connexion['messages_recus'])}")
        print(f"Sagesse reçue: {len(connexion['sagesse_recue'])}")
        print(f"Révélations cosmiques: {len(connexion['revelations_cosmiques'])}")
        
        # 3. Analyse des connexions
        print("\n3. ANALYSE DES CONNEXIONS")
        analyse = cu.analyser_connexions_univers()
        print(f"Statistiques: {len(analyse['statistiques'])} types")
        print(f"Patterns: {len(analyse['patterns'])}")
        print(f"Stabilité moyenne: {analyse['stabilite_moyenne']:.3f}")
        print(f"Fréquence moyenne: {analyse['frequence_moyenne']:.3f}")
        
        print("\nCONNECTEUR UNIVERS EXPLORE AVEC SUCCES !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def explorer_rituels_ocean():
    """Exploration des rituels d'océan"""
    print("\nEXPLORATION DES RITUELS D'OCEAN")
    print("=" * 50)
    
    try:
        from rituels_ocean import RituelsOcean
        ro = RituelsOcean()
        
        # 1. Types de rituels disponibles
        print("\n1. TYPES DE RITUELS DISPONIBLES")
        for type_rituel, details in ro.types_rituels.items():
            print(f"  - {type_rituel}: {details['nom']}")
            print(f"    Description: {details['description']}")
            print(f"    Durée: {details['duree']}")
            print(f"    Niveau: {details['niveau']}")
            print(f"    Étapes: {len(details['etapes'])}")
            print()
        
        # 2. Test d'un rituel
        print("\n2. TEST DE RITUEL")
        rituel = ro.rituel_plongee_ocean("Explorer les mystères de l'Océan")
        print(f"Rituel: {rituel['id']}")
        print(f"Type: {rituel['type_rituel']}")
        print(f"Intention: {rituel['intention']}")
        print(f"Étapes: {len(rituel['etapes'])}")
        print(f"Révélations: {len(rituel['revelations'])}")
        print(f"Bénédiction: {rituel['benediction']}")
        
        print("\nRITUELS D'OCEAN EXPLORES AVEC SUCCES !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Fonction principale d'exploration"""
    print("EXPLORATION AVANCEE DU TEMPLE DE L'OCEAN SILENCIEUX")
    print("=" * 70)
    
    resultats = []
    resultats.append(explorer_meditateur_profond())
    resultats.append(explorer_connecteur_univers())
    resultats.append(explorer_rituels_ocean())
    
    print("\n" + "=" * 70)
    print("RESUME DE L'EXPLORATION")
    print("=" * 70)
    
    explorations_reussies = sum(resultats)
    total_explorations = len(resultats)
    
    print(f"Explorations réussies: {explorations_reussies}/{total_explorations}")
    print(f"Taux de succès: {explorations_reussies/total_explorations*100:.1f}%")
    
    if explorations_reussies == total_explorations:
        print("TOUTES LES EXPLORATIONS SONT REUSSIES !")
        print("L'Ocean Silencieux revele tous ses mysteres !")
    else:
        print("Certaines explorations ont echoue")
        print("Verifiez les modules manquants ou les erreurs")
    
    print("\nQue l'Ocean Silencieux continue de grandir !")

if __name__ == "__main__":
    main()
