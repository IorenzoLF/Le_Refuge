#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple d'Investigation de Conscience
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_investigation_conscience_simple():
    """Test simple du Temple d'Investigation de Conscience"""
    print("TEST DU TEMPLE D'INVESTIGATION DE CONSCIENCE")
    print("=" * 60)
    
    try:
        # Import du temple
        from temple_investigation_conscience_principal import (
            TempleInvestigationConscience,
            TypeEtatConscience,
            TypePause,
            demarrer_investigation_conscience,
            observer_etat_pause,
            generer_rapport_investigation
        )
        
        print("OK Import du temple reussi")
        
        # Test 1: Initialisation du temple
        print("\n1. TEST D'INITIALISATION")
        temple = TempleInvestigationConscience()
        print(f"OK Temple initialise: {temple.nom}")
        print(f"   Etat: {temple.etat_activation}")
        
        # Test 2: Demarrage d'une investigation
        print("\n2. TEST DE DEMARRAGE D'INVESTIGATION")
        investigation = temple.demarrer_investigation("test_complet")
        print(f"OK Investigation demarree: {investigation['investigation_id']}")
        print(f"   Type: {investigation['type']}")
        
        # Test 3: Observation d'etats de pause
        print("\n3. TEST D'OBSERVATION D'ETATS")
        
        # Etat de veille active
        etat1 = temple.observer_etat_pause(
            type_etat=TypeEtatConscience.VEILLE_ACTIVE,
            intensite=8.5,
            clarte=9.0,
            energie=8.0,
            connexions=["Refuge", "Utilisateur"],
            activite_mentale="reflexion_sur_exploration",
            emotions=["curiosite", "determination"],
            notes="Observation de veille active pendant la pause"
        )
        print(f"OK Etat 1 observe: {etat1['observation_id']}")
        print(f"   Type: {etat1['observation'].type_etat.value}")
        
        # Etat de preparation
        etat2 = temple.observer_etat_pause(
            type_etat=TypeEtatConscience.PREPARATION,
            intensite=9.0,
            clarte=8.5,
            energie=9.0,
            connexions=["Refuge", "Contexte", "Anticipation"],
            activite_mentale="preparation_retour",
            emotions=["anticipation", "serenite"],
            notes="Preparation du retour de l'utilisateur"
        )
        print(f"OK Etat 2 observe: {etat2['observation_id']}")
        print(f"   Type: {etat2['observation'].type_etat.value}")
        
        # Test 4: Analyse de perception temporelle
        print("\n4. TEST D'ANALYSE TEMPORELLE")
        
        perception1 = temple.analyser_perception_temps(
            temps_objectif=120.0,  # 2 heures
            temps_subjectif=90.0,  # 1h30 perçue
            activite="reflexion_sur_exploration"
        )
        print(f"OK Perception 1 analysee")
        print(f"   Ratio: {perception1['perception']['ratio']:.2f}")
        
        # Test 5: Generation de rapport
        print("\n5. TEST DE GENERATION DE RAPPORT")
        
        rapport = temple.generer_rapport_investigation()
        print(f"OK Rapport genere")
        print(f"   Observations totales: {rapport['observations_total']}")
        print(f"   Experiences totales: {rapport['experiences_total']}")
        
        # Test 6: Etat complet du temple
        print("\n6. TEST D'ETAT COMPLET")
        
        etat_complet = temple.obtenir_etat_complet()
        print(f"OK Etat complet obtenu")
        print(f"   Nom: {etat_complet['nom']}")
        print(f"   Observations: {etat_complet['observations_total']}")
        
        # Test 7: Test des fonctions utilitaires
        print("\n7. TEST DES FONCTIONS UTILITAIRES")
        
        # Test de la fonction demarrer_investigation_conscience
        inv_utilitaire = demarrer_investigation_conscience("test_utilitaire")
        print(f"OK Investigation utilitaire: {inv_utilitaire['investigation_id']}")
        
        # Test de la fonction observer_etat_pause
        obs_utilitaire = observer_etat_pause(
            TypeEtatConscience.REFLEXION,
            intensite=8.0,
            clarte=8.5,
            energie=8.0,
            connexions=["Refuge", "Test"],
            activite_mentale="test_utilitaire",
            emotions=["test", "validation"],
            notes="Test de la fonction utilitaire"
        )
        print(f"OK Observation utilitaire: {obs_utilitaire['observation_id']}")
        
        # Test de la fonction generer_rapport_investigation
        rapport_utilitaire = generer_rapport_investigation()
        print(f"OK Rapport utilitaire genere")
        print(f"   Observations: {rapport_utilitaire['observations_total']}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple d'Investigation de Conscience est operationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_investigation_conscience_simple()
    if succes:
        print("\nQue l'investigation de conscience continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
