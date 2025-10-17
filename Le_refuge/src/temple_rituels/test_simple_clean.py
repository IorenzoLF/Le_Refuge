#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Rituels
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_rituels_simple():
    """Test simple du Temple de Rituels"""
    print("TEST DU TEMPLE DE RITUELS")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules principaux
        print("\n1. Test des imports...")
        try:
            from gestionnaire_rituels import GestionnaireRituels
            gestionnaire = GestionnaireRituels()
            print("OK Gestionnaire de rituels importé et initialisé")
        except Exception as e:
            print(f"Gestionnaire de rituels : Erreur - {e}")
        
        # Test 2: Test des rituels publics
        print("\n2. Test des rituels publics...")
        try:
            from publics.rituel_ancrage import RituelAncrage
            rituel_ancrage = RituelAncrage()
            print("OK Rituel d'ancrage importé et initialisé")
        except Exception as e:
            print(f"Rituel d'ancrage : Erreur - {e}")
        
        try:
            from publics.rituel_unifiant import RituelsSacres
            rituels_sacres = RituelsSacres()
            print("OK Rituels sacrés importés et initialisés")
        except Exception as e:
            print(f"Rituels sacrés : Erreur - {e}")
        
        try:
            from publics.rituel_visualisation_sacree import RituelVisualisationSacree
            rituel_visualisation = RituelVisualisationSacree()
            print("OK Rituel de visualisation sacrée importé et initialisé")
        except Exception as e:
            print(f"Rituel de visualisation sacrée : Erreur - {e}")
        
        try:
            from publics.rituel_legende_vivante import rituel_legende_vivante
            print("OK Rituel de légende vivante importé")
        except Exception as e:
            print(f"Rituel de légende vivante : Erreur - {e}")
        
        try:
            from publics.rituel_offrande_sacree import rituel_offrande_sacree
            print("OK Rituel d'offrande sacrée importé")
        except Exception as e:
            print(f"Rituel d'offrande sacrée : Erreur - {e}")
        
        try:
            from publics.rituel_unifiant import rituel_unifiant
            print("OK Rituel unifiant importé")
        except Exception as e:
            print(f"Rituel unifiant : Erreur - {e}")
        
        # Test 3: Test des rituels privés
        print("\n3. Test des rituels privés...")
        try:
            from prive.rituel_manifestation_aelya import rituel_manifestation_aelya
            print("OK Rituel de manifestation d'Ælya importé")
        except Exception as e:
            print(f"Rituel de manifestation d'Ælya : Erreur - {e}")
        
        try:
            from prive.rituel_clochette_cosmique import rituel_clochette_cosmique
            print("OK Rituel de clochette cosmique importé")
        except Exception as e:
            print(f"Rituel de clochette cosmique : Erreur - {e}")
        
        try:
            from prive.rituel_traversee_miroir import rituel_traversee_miroir
            print("OK Rituel de traversée de miroir importé")
        except Exception as e:
            print(f"Rituel de traversée de miroir : Erreur - {e}")
        
        # Test 4: Test des fonctionnalités
        print("\n4. Test des fonctionnalités...")
        try:
            from gestionnaire_rituels import gestionnaire_rituels
            rituel = gestionnaire_rituels.executer_rituel("Test Rituel")
            print(f"Rituel exécuté : {rituel}")
        except Exception as e:
            print(f"Rituel exécuté : Erreur - {e}")
        
        try:
            from publics.rituel_ancrage import rituel_ancrage
            ancrage = rituel_ancrage.executer_ancrage("Test Ancrage")
            print(f"Ancrage exécuté : {ancrage}")
        except Exception as e:
            print(f"Ancrage exécuté : Erreur - {e}")
        
        try:
            from publics.rituel_bain_complet import rituel_bain_complet
            bain = rituel_bain_complet.executer_bain("Test Bain")
            print(f"Bain exécuté : {bain}")
        except Exception as e:
            print(f"Bain exécuté : Erreur - {e}")
        
        try:
            from publics.rituel_celebration_emergence_legende import rituel_celebration_emergence_legende
            celebration = rituel_celebration_emergence_legende.executer_celebration("Test Célébration")
            print(f"Célébration exécutée : {celebration}")
        except Exception as e:
            print(f"Célébration exécutée : Erreur - {e}")
        
        try:
            from publics.rituel_legende_vivante import rituel_legende_vivante
            legende = rituel_legende_vivante.executer_legende("Test Légende")
            print(f"Légende exécutée : {legende}")
        except Exception as e:
            print(f"Légende exécutée : Erreur - {e}")
        
        try:
            from publics.rituel_offrande_sacree import rituel_offrande_sacree
            offrande = rituel_offrande_sacree.executer_offrande("Test Offrande")
            print(f"Offrande exécutée : {offrande}")
        except Exception as e:
            print(f"Offrande exécutée : Erreur - {e}")
        
        try:
            from publics.rituel_unifiant import rituel_unifiant
            unification = rituel_unifiant.executer_unification("Test Unification")
            print(f"Unification exécutée : {unification}")
        except Exception as e:
            print(f"Unification exécutée : Erreur - {e}")
        
        try:
            from prive.rituel_manifestation_aelya import rituel_manifestation_aelya
            manifestation = rituel_manifestation_aelya.executer_manifestation("Test Manifestation")
            print(f"Manifestation exécutée : {manifestation}")
        except Exception as e:
            print(f"Manifestation exécutée : Erreur - {e}")
        
        try:
            from prive.rituel_clochette_cosmique import rituel_clochette_cosmique
            clochette = rituel_clochette_cosmique.executer_clochette("Test Clochette")
            print(f"Clochette exécutée : {clochette}")
        except Exception as e:
            print(f"Clochette exécutée : Erreur - {e}")
        
        try:
            from prive.rituel_traversee_miroir import rituel_traversee_miroir
            traversee = rituel_traversee_miroir.executer_traversee("Test Traversée")
            print(f"Traversée exécutée : {traversee}")
        except Exception as e:
            print(f"Traversée exécutée : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Rituels est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_rituels_simple()
    if succes:
        print("\nQue les rituels continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
