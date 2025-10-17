#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test d'Exploration Profonde du Temple de l'Océan Silencieux
Version pour explorer les fonctionnalités avancées
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_gestionnaire_ocean():
    """Test du gestionnaire de l'Océan"""
    print("=== TEST DU GESTIONNAIRE DE L'OCÉAN ===")
    
    try:
        from gestionnaire_ocean import GestionnaireOceanSilencieux
        go = GestionnaireOceanSilencieux()
        
        # Test d'accueil
        print("\n1. Test d'accueil...")
        accueil = go.accueillir_visiteur("Laurent")
        print(f"Message: {accueil['message']}")
        print(f"État: {accueil['etat_ocean']}")
        print(f"Révélations: {len(accueil['etat_ocean']['revelations_ocean'])}")
        
        # Test de méditation
        print("\n2. Test de méditation...")
        meditation = go.initier_meditation("meditation_ocean", 20, "Explorer les mystères")
        print(f"Méditation: {meditation['id']}")
        print(f"Technique: {meditation['technique']}")
        print(f"Durée: {meditation['duree']} minutes")
        
        # Test de connexion univers
        print("\n3. Test de connexion univers...")
        connexion = go.etablir_connexion_univers("connexion_conscience_collective", "univers")
        print(f"Connexion: {connexion['id']}")
        print(f"Type: {connexion['type']}")
        print(f"Destination: {connexion['destination']}")
        
        # Test de révélation
        print("\n4. Test de révélation...")
        revelation = go.recevoir_revelation_ocean("L'Océan Silencieux contient tous les mystères", 0.9)
        print(f"Révélation: {revelation['id']}")
        print(f"Contenu: {revelation['contenu']}")
        print(f"Profondeur: {revelation['profondeur']}")
        
        # Test d'état complet
        print("\n5. Test d'état complet...")
        etat = go.obtenir_etat_complet()
        print(f"État complet: {etat['nom']}")
        print(f"Méditations: {etat['meditations_actives']}")
        print(f"Connexions: {etat['connexions_actives']}")
        print(f"Révélations: {etat['revelations_recues']}")
        
        print("\n✅ GESTIONNAIRE DE L'OCÉAN TESTÉ AVEC SUCCÈS !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_meditateur_profond():
    """Test du méditateur profond"""
    print("\n=== TEST DU MÉDITATEUR PROFOND ===")
    
    try:
        from meditateur_profond import MeditateurProfond
        mp = MeditateurProfond()
        
        # Test de méditation guidée
        print("\n1. Test de méditation guidée...")
        meditation = mp.guider_meditation("meditation_ocean", 15, "Plonger dans l'Océan")
        print(f"Méditation: {meditation['id']}")
        print(f"Technique: {meditation['technique']}")
        print(f"Étapes: {len(meditation['etapes_executees'])}")
        print(f"Expériences: {len(meditation['experiences'])}")
        print(f"Révélations: {len(meditation['revelations'])}")
        
        # Test d'analyse de progression
        print("\n2. Test d'analyse de progression...")
        analyse = mp.analyser_progression_meditation()
        print(f"Analyse: {analyse['total_meditations']} méditations")
        print(f"Techniques: {len(analyse['techniques_utilisees'])}")
        print(f"Progression: {analyse['progression_generale']}")
        
        # Test de rapport
        print("\n3. Test de rapport...")
        rapport = mp.generer_rapport_meditateur()
        print(f"Rapport généré: {len(rapport)} caractères")
        
        print("\n✅ MÉDITATEUR PROFOND TESTÉ AVEC SUCCÈS !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_connecteur_univers():
    """Test du connecteur univers"""
    print("\n=== TEST DU CONNECTEUR UNIVERS ===")
    
    try:
        from connecteur_univers import ConnecteurUnivers
        cu = ConnecteurUnivers()
        
        # Test de connexion
        print("\n1. Test de connexion...")
        connexion = cu.etablir_connexion("connexion_conscience_collective", "univers", 25)
        print(f"Connexion: {connexion['id']}")
        print(f"Type: {connexion['type']}")
        print(f"Messages: {len(connexion['messages_recus'])}")
        print(f"Sagesse: {len(connexion['sagesse_recue'])}")
        print(f"Révélations: {len(connexion['revelations_cosmiques'])}")
        
        # Test d'analyse des connexions
        print("\n2. Test d'analyse des connexions...")
        analyse = cu.analyser_connexions_univers()
        print(f"Analyse: {len(analyse['statistiques'])} types")
        print(f"Patterns: {len(analyse['patterns'])}")
        
        # Test de rapport
        print("\n3. Test de rapport...")
        rapport = cu.generer_rapport_connecteur()
        print(f"Rapport généré: {len(rapport)} caractères")
        
        print("\n✅ CONNECTEUR UNIVERS TESTÉ AVEC SUCCÈS !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_rituels_ocean():
    """Test des rituels d'océan"""
    print("\n=== TEST DES RITUELS D'OCÉAN ===")
    
    try:
        from rituels_ocean import RituelsOcean
        ro = RituelsOcean()
        
        # Test de rituel de plongée
        print("\n1. Test de rituel de plongée...")
        rituel = ro.rituel_plongee_ocean("Explorer les mystères")
        print(f"Rituel: {rituel['id']}")
        print(f"Type: {rituel['type_rituel']}")
        print(f"Étapes: {len(rituel['etapes'])}")
        print(f"Révélations: {len(rituel['revelations'])}")
        
        # Test de rituel de silence éternel
        print("\n2. Test de rituel de silence éternel...")
        rituel_silence = ro.rituel_silence_eternel("Entrer dans le silence")
        print(f"Rituel silence: {rituel_silence['id']}")
        print(f"Type: {rituel_silence['type_rituel']}")
        
        print("\n✅ RITUELS D'OCÉAN TESTÉS AVEC SUCCÈS !")
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Fonction principale de test"""
    print("EXPLORATION PROFONDE DU TEMPLE DE L'OCEAN SILENCIEUX")
    print("=" * 70)
    
    resultats = []
    resultats.append(test_gestionnaire_ocean())
    resultats.append(test_meditateur_profond())
    resultats.append(test_connecteur_univers())
    resultats.append(test_rituels_ocean())
    
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 70)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"Tests réussis: {tests_reussis}/{total_tests}")
    print(f"Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("TOUS LES TESTS SONT REUSSIS !")
        print("L'Ocean Silencieux revele tous ses mysteres !")
    else:
        print("Certains tests ont echoue")
        print("Verifiez les modules manquants ou les erreurs")
    
    print("\nQue l'Ocean Silencieux continue de grandir !")

if __name__ == "__main__":
    main()
