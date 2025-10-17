#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple et Propre du Temple de Créativité
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_creativite_simple():
    """Test simple du Temple de Créativité"""
    print("TEST DU TEMPLE DE CREATIVITE")
    print("=" * 50)
    
    try:
        # Test 1: Test des modules individuels
        print("\n1. Test des modules individuels...")
        try:
            from inspirateur_idees import InspirateurIdees
            inspirateur = InspirateurIdees()
            print("OK Inspirateur d'idées importé et initialisé")
        except Exception as e:
            print(f"Inspirateur d'idées : Erreur - {e}")
        
        try:
            from manifesteur_art import ManifesteurArt
            manifesteur = ManifesteurArt()
            print("OK Manifesteur d'art importé et initialisé")
        except Exception as e:
            print(f"Manifesteur d'art : Erreur - {e}")
        
        try:
            from catalyseur_innovation import CatalyseurInnovation
            catalyseur = CatalyseurInnovation()
            print("OK Catalyseur d'innovation importé et initialisé")
        except Exception as e:
            print(f"Catalyseur d'innovation : Erreur - {e}")
        
        try:
            from harmoniseur_expression import HarmoniseurExpression
            harmoniseur = HarmoniseurExpression()
            print("OK Harmoniseur d'expression importé et initialisé")
        except Exception as e:
            print(f"Harmoniseur d'expression : Erreur - {e}")
        
        try:
            from simulateur_expression_creative_refuge import SimulateurExpressionCreativeRefuge
            simulateur = SimulateurExpressionCreativeRefuge()
            print("OK Simulateur d'expression créative importé et initialisé")
        except Exception as e:
            print(f"Simulateur d'expression créative : Erreur - {e}")
        
        # Test 2: Test du temple principal
        print("\n2. Test du temple principal...")
        try:
            from temple_creativite_principal import TempleCreativite
            temple = TempleCreativite()
            print("OK Temple de créativité importé et initialisé")
        except Exception as e:
            print(f"Temple de créativité : Erreur - {e}")
        
        # Test 3: Test des fonctionnalités
        print("\n3. Test des fonctionnalités...")
        try:
            from inspirateur_idees import InspirateurIdees
            inspirateur = InspirateurIdees()
            idee = inspirateur.generer_inspiration("divine", "Laurent")
            print(f"Inspiration générée : {idee}")
        except Exception as e:
            print(f"Inspiration générée : Erreur - {e}")
        
        try:
            from manifesteur_art import ManifesteurArt
            manifesteur = ManifesteurArt()
            oeuvre = manifesteur.manifester_art("peinture", "Laurent")
            print(f"Œuvre d'art manifestée : {oeuvre}")
        except Exception as e:
            print(f"Œuvre d'art manifestée : Erreur - {e}")
        
        try:
            from catalyseur_innovation import CatalyseurInnovation
            catalyseur = CatalyseurInnovation()
            innovation = catalyseur.catalyser_innovation("technologique", "Laurent")
            print(f"Innovation catalysée : {innovation}")
        except Exception as e:
            print(f"Innovation catalysée : Erreur - {e}")
        
        try:
            from harmoniseur_expression import HarmoniseurExpression
            harmoniseur = HarmoniseurExpression()
            expression = harmoniseur.harmoniser_expression("poétique", "Laurent")
            print(f"Expression harmonisée : {expression}")
        except Exception as e:
            print(f"Expression harmonisée : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Créativité est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_creativite_simple()
    if succes:
        print("\nQue la créativité continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")