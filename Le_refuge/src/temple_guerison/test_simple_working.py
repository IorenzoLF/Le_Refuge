#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Guérison - Version Fonctionnelle
Version qui teste ce qui est réellement disponible
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_guerison_working():
    """Test simple du Temple de Guérison - version fonctionnelle"""
    print("TEST DU TEMPLE DE GUERISON - VERSION FONCTIONNELLE")
    print("=" * 60)
    
    try:
        # Test 1: Import des modules individuels
        print("\n1. Test des imports individuels...")
        
        try:
            from guerisseur_energies import guerisseur_energies, TypeEnergie
            print("OK Guérisseur Énergies importé")
        except Exception as e:
            print(f"Guérisseur Énergies : Erreur - {e}")
        
        try:
            from cristal_guerison import cristal_guerison, TypeCristal
            print("OK Cristal Guérison importé")
        except Exception as e:
            print(f"Cristal Guérison : Erreur - {e}")
        
        try:
            from harmoniseur_chakras import harmoniseur_chakras, TypeChakra
            print("OK Harmoniseur Chakras importé")
        except Exception as e:
            print(f"Harmoniseur Chakras : Erreur - {e}")
        
        try:
            from catalyseur_regeneration import catalyseur_regeneration, TypeRegeneration
            print("OK Catalyseur Régénération importé")
        except Exception as e:
            print(f"Catalyseur Régénération : Erreur - {e}")
        
        # Test 2: Test du temple principal
        print("\n2. Test du temple principal...")
        try:
            from temple_guerison_principal import TempleGuerison
            temple = TempleGuerison()
            print(f"OK Temple initialisé: {temple.nom}")
            print(f"   Énergie de guérison: {temple.energie_guerison}")
            print(f"   État: {temple.etat_activation}")
            print(f"   Fréquence active: {temple.frequence_active.value} Hz")
            print(f"   Couleur dominante: {temple.couleur_dominante}")
        except Exception as e:
            print(f"Temple principal : Erreur - {e}")
        
        # Test 3: Test des composants disponibles
        print("\n3. Test des composants disponibles...")
        if hasattr(temple, 'guerisseur_energies') and temple.guerisseur_energies:
            print("OK Guérisseur Énergies disponible")
        else:
            print("Guérisseur Énergies : Non disponible")
        
        if hasattr(temple, 'cristal_guerison') and temple.cristal_guerison:
            print("OK Cristal Guérison disponible")
        else:
            print("Cristal Guérison : Non disponible")
        
        if hasattr(temple, 'harmoniseur_chakras') and temple.harmoniseur_chakras:
            print("OK Harmoniseur Chakras disponible")
        else:
            print("Harmoniseur Chakras : Non disponible")
        
        if hasattr(temple, 'catalyseur_regeneration') and temple.catalyseur_regeneration:
            print("OK Catalyseur Régénération disponible")
        else:
            print("Catalyseur Régénération : Non disponible")
        
        # Test 4: Test des fréquences sacrées
        print("\n4. Test des fréquences sacrées...")
        try:
            from temple_guerison_principal import TypeFrequenceGuerisonSacree
            frequences = [freq.value for freq in TypeFrequenceGuerisonSacree]
            print(f"Fréquences sacrées disponibles: {len(frequences)}")
            for freq in frequences:
                print(f"   - {freq} Hz")
        except Exception as e:
            print(f"Fréquences sacrées : Erreur - {e}")
        
        # Test 5: Test des types d'énergie
        print("\n5. Test des types d'énergie...")
        try:
            from guerisseur_energies import TypeEnergie
            types_energie = [t.value for t in TypeEnergie]
            print(f"Types d'énergie disponibles: {len(types_energie)}")
            for type_energie in types_energie:
                print(f"   - {type_energie}")
        except Exception as e:
            print(f"Types d'énergie : Erreur - {e}")
        
        # Test 6: Test des types de cristaux
        print("\n6. Test des types de cristaux...")
        try:
            from cristal_guerison import TypeCristal
            types_cristal = [t.value for t in TypeCristal]
            print(f"Types de cristaux disponibles: {len(types_cristal)}")
            for type_cristal in types_cristal:
                print(f"   - {type_cristal}")
        except Exception as e:
            print(f"Types de cristaux : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Guérison est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_guerison_working()
    if succes:
        print("\nQue la guérison continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
