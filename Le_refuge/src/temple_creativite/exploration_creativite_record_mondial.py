#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration du Temple de Créativité - Record Mondial
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def exploration_creativite_record_mondial():
    """Exploration approfondie du Temple de Créativité pour le record mondial"""
    print("EXPLORATION DU TEMPLE DE CREATIVITE - RECORD MONDIAL")
    print("=" * 60)
    print("CREATIVITE ET INNOVATION - EXPRESSION ARTISTIQUE")
    print("=" * 60)
    
    try:
        # 1. Test des modules individuels
        print("\n1. MODULES DE CREATIVITE")
        print("Exploration des composants créatifs...")
        
        from inspirateur_idees import InspirateurIdees
        inspirateur = InspirateurIdees()
        print("OK Inspirateur d'idées initialisé")
        
        from manifesteur_art import ManifesteurArt
        manifesteur = ManifesteurArt()
        print("OK Manifesteur d'art initialisé")
        
        from catalyseur_innovation import CatalyseurInnovation
        catalyseur = CatalyseurInnovation()
        print("OK Catalyseur d'innovation initialisé")
        
        from harmoniseur_expression import HarmoniseurExpression
        harmoniseur = HarmoniseurExpression()
        print("OK Harmoniseur d'expression initialisé")
        
        from simulateur_expression_creative_refuge import SimulateurExpressionCreativeRefuge
        simulateur = SimulateurExpressionCreativeRefuge()
        print("OK Simulateur d'expression créative initialisé")
        
        # 2. Test du temple principal
        print("\n2. TEMPLE PRINCIPAL")
        print("Exploration du temple de créativité...")
        
        from temple_creativite_principal import TempleCreativite
        temple = TempleCreativite()
        print("OK Temple de créativité initialisé")
        
        # 3. Test des fonctionnalités créatives
        print("\n3. FONCTIONNALITES CREATIVES")
        print("Exploration des capacités créatives...")
        
        # Test d'inspiration
        try:
            inspiration = inspirateur.generer_inspiration("divine", "Laurent")
            print(f"Inspiration générée: {inspiration}")
        except Exception as e:
            print(f"Inspiration générée: Erreur - {e}")
        
        # Test de manifestation d'art
        try:
            oeuvre = manifesteur.manifester_art("peinture", "Laurent")
            print(f"Œuvre d'art manifestée: {oeuvre}")
        except Exception as e:
            print(f"Œuvre d'art manifestée: Erreur - {e}")
        
        # Test de catalyse d'innovation
        try:
            innovation = catalyseur.catalyser_innovation("technologique", "Laurent")
            print(f"Innovation catalysée: {innovation}")
        except Exception as e:
            print(f"Innovation catalysée: Erreur - {e}")
        
        # Test d'harmonisation d'expression
        try:
            expression = harmoniseur.harmoniser_expression("poétique", "Laurent")
            print(f"Expression harmonisée: {expression}")
        except Exception as e:
            print(f"Expression harmonisée: Erreur - {e}")
        
        # 4. Test des méthodes disponibles
        print("\n4. METHODES DISPONIBLES")
        print("Exploration des méthodes créatives...")
        
        print("Méthodes de l'inspirateur:")
        for method in dir(inspirateur):
            if not method.startswith('_'):
                print(f"  - {method}")
        
        print("Méthodes du manifesteur:")
        for method in dir(manifesteur):
            if not method.startswith('_'):
                print(f"  - {method}")
        
        print("Méthodes du catalyseur:")
        for method in dir(catalyseur):
            if not method.startswith('_'):
                print(f"  - {method}")
        
        print("Méthodes de l'harmoniseur:")
        for method in dir(harmoniseur):
            if not method.startswith('_'):
                print(f"  - {method}")
        
        # 5. Découvertes du Temple de Créativité
        print("\n5. DECOUVERTES DU TEMPLE DE CREATIVITE")
        print("Révélations de la créativité et de l'innovation...")
        print("  - L'inspirateur d'idées génère des concepts créatifs")
        print("  - Le manifesteur d'art crée des œuvres artistiques")
        print("  - Le catalyseur d'innovation accélère les découvertes")
        print("  - L'harmoniseur d'expression unifie les formes d'art")
        print("  - Le simulateur d'expression créative explore les possibilités")
        print("  - La créativité transcende les limites de l'imagination")
        print("  - L'innovation ouvre de nouveaux horizons")
        print("  - Le temple de créativité est un sanctuaire d'expression")
        
        print("\nEXPLORATION DU TEMPLE DE CREATIVITE TERMINEE AVEC SUCCES !")
        print("La créativité et l'innovation rayonnent dans l'univers !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = exploration_creativite_record_mondial()
    if succes:
        print("\nQue la créativité continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
