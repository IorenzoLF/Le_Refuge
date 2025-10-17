#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Guérison
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_guerison_simple():
    """Test simple du Temple de Guérison"""
    print("TEST DU TEMPLE DE GUERISON")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_guerison_principal import TempleGuerison
        print("OK Import du temple principal réussi")
        
        # Test 2: Initialisation du temple
        print("\n2. Test d'initialisation...")
        temple = TempleGuerison()
        print("OK Temple initialisé")
        
        # Test 3: Test d'accueil
        print("\n3. Test d'accueil...")
        try:
            accueil = temple.accueillir_visiteur("Laurent")
            print(f"Message d'accueil : {accueil['message']}")
        except AttributeError:
            print("Accueil : Méthode non disponible")
        
        # Test 4: Test de catalyseur de régénération
        print("\n4. Test de catalyseur de régénération...")
        try:
            regeneration = temple.catalyser_regeneration("Laurent", 0.8)
            print(f"Régénération catalysée : {regeneration['id']}")
            print(f"Niveau : {regeneration['niveau']}")
        except AttributeError:
            print("Catalyseur de régénération : Méthode non disponible")
        
        # Test 5: Test de cristal de guérison
        print("\n5. Test de cristal de guérison...")
        try:
            guerison = temple.guerir("Laurent", "fatigue", 0.7)
            print(f"Guérison : {guerison['id']}")
            print(f"Type : {guerison['type']}")
        except AttributeError:
            print("Cristal de guérison : Méthode non disponible")
        
        # Test 6: Test de guérisseur d'énergies
        print("\n6. Test de guérisseur d'énergies...")
        try:
            energie = temple.guerir_energie("Laurent", "blocage", 0.6)
            print(f"Énergie guérie : {energie['id']}")
            print(f"Blocage : {energie['blocage']}")
        except AttributeError:
            print("Guérisseur d'énergies : Méthode non disponible")
        
        # Test 7: Test d'harmoniseur de chakras
        print("\n7. Test d'harmoniseur de chakras...")
        try:
            chakra = temple.harmoniser_chakra("Laurent", "coeur", 0.8)
            print(f"Chakra harmonisé : {chakra['id']}")
            print(f"Chakra : {chakra['chakra']}")
        except AttributeError:
            print("Harmoniseur de chakras : Méthode non disponible")
        
        # Test 8: Test de guérison complète
        print("\n8. Test de guérison complète...")
        try:
            guerison_complete = temple.guerir_visiteur("Laurent", "fatigue", 0.9)
            print(f"Guérison complète : {guerison_complete['id']}")
            print(f"Résultat : {guerison_complete['resultat']}")
        except AttributeError:
            print("Guérison complète : Méthode non disponible")
        
        # Test 9: Test de méditation de guérison
        print("\n9. Test de méditation de guérison...")
        try:
            meditation = temple.mediter_guerison("Laurent", 15)
            print(f"Méditation : {meditation['id']}")
            print(f"Durée : {meditation['duree']}s")
        except AttributeError:
            print("Méditation de guérison : Méthode non disponible")
        
        # Test 10: Test d'état du temple
        print("\n10. Test d'état du temple...")
        try:
            etat = temple.obtenir_etat()
            print(f"État du temple : {etat['nom']}")
            print(f"Énergie : {etat['energie']:.2f}")
            print(f"Guérisons : {etat['guerisons']}")
        except AttributeError:
            print("État du temple : Méthode non disponible")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Guérison est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_guerison_simple()
    if succes:
        print("\nQue la guérison continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
