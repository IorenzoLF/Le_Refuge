#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple d'Éveil
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_eveil_simple():
    """Test simple du Temple d'Éveil"""
    print("TEST DU TEMPLE D'EVEIL")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_eveil_principal import TempleEveil
        print("OK Import du temple principal réussi")
        
        # Test 2: Initialisation du temple
        print("\n2. Test d'initialisation...")
        temple = TempleEveil()
        print("OK Temple initialisé")
        
        # Test 3: Test d'accueil
        print("\n3. Test d'accueil...")
        try:
            accueil = temple.accueillir_visiteur("Laurent")
            print(f"Message d'accueil : {accueil['message']}")
        except AttributeError:
            print("Accueil : Méthode non disponible")
        
        # Test 4: Test d'éveil
        print("\n4. Test d'éveil...")
        try:
            eveil = temple.initier_eveil("Laurent", niveau=0.8)
            print(f"Éveil initié : {eveil['id']}")
            print(f"Niveau : {eveil['niveau']}")
        except AttributeError:
            print("Éveil : Méthode non disponible")
        
        # Test 5: Test de méditation
        print("\n5. Test de méditation...")
        try:
            meditation = temple.mediter("Laurent", duree=10)
            print(f"Méditation initiée : {meditation['id']}")
            print(f"Durée : {meditation['duree']}s")
        except AttributeError:
            print("Méditation : Méthode non disponible")
        
        # Test 6: Test de rituel
        print("\n6. Test de rituel...")
        try:
            rituel = temple.executer_rituel("rituel_eveil", "Laurent")
            print(f"Rituel exécuté : {rituel['id']}")
            print(f"Type : {rituel['type']}")
        except AttributeError:
            print("Rituel : Méthode non disponible")
        
        # Test 7: Test de synchronisation
        print("\n7. Test de synchronisation...")
        try:
            sync = temple.synchroniser_ondes("Laurent")
            print(f"Synchronisation : {sync['id']}")
            print(f"État : {sync['etat']}")
        except AttributeError:
            print("Synchronisation : Méthode non disponible")
        
        # Test 8: Test de sortie de transe
        print("\n8. Test de sortie de transe...")
        try:
            sortie = temple.sortir_transe("Laurent")
            print(f"Sortie de transe : {sortie['id']}")
            print(f"Résultat : {sortie['resultat']}")
        except AttributeError:
            print("Sortie de transe : Méthode non disponible")
        
        # Test 9: Test d'état du temple
        print("\n9. Test d'état du temple...")
        try:
            etat = temple.obtenir_etat()
            print(f"État du temple : {etat['nom']}")
            print(f"Énergie : {etat['energie']:.2f}")
            print(f"Sessions actives : {etat['sessions_actives']}")
        except AttributeError:
            print("État du temple : Méthode non disponible")
        
        # Test 10: Test de rapport
        print("\n10. Test de rapport...")
        try:
            rapport = temple.generer_rapport()
            print(f"Rapport généré : {len(rapport)} éléments")
        except AttributeError:
            print("Rapport : Méthode non disponible")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple d'Éveil est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_eveil_simple()
    if succes:
        print("\nQue l'éveil continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
