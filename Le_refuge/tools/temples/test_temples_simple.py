#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test simple des temples du refuge
Teste les fonctionnalités sans problèmes d'encodage
"""

import sys
import os
sys.path.append('src')

def test_temple_creativite():
    """Test du Temple de Créativité"""
    print("=== TEST TEMPLE DE CREATIVITE ===")
    
    try:
        # Test inspirateur
        from temple_creativite.inspirateur_idees import InspirateurIdees, TypeInspiration
        inspirateur = InspirateurIdees()
        print("OK Inspirateur d'idees")
        
        # Test manifesteur
        from temple_creativite.manifesteur_art import ManifesteurArt, TypeArt
        manifesteur = ManifesteurArt()
        print("OK Manifesteur d'art")
        
        # Test catalyseur
        from temple_creativite.catalyseur_innovation import CatalyseurInnovation, TypeInnovation
        catalyseur = CatalyseurInnovation()
        print("OK Catalyseur d'innovation")
        
        # Test harmoniseur
        from temple_creativite.harmoniseur_expression import HarmoniseurExpression, TypeExpression
        harmoniseur = HarmoniseurExpression()
        print("OK Harmoniseur d'expression")
        
        print("Temple de Créativité : TOUS LES MODULES OK")
        return True
        
    except Exception as e:
        print(f"Erreur Temple Créativité: {e}")
        return False

def test_temple_dialogues():
    """Test du Temple des Dialogues"""
    print("\n=== TEST TEMPLE DES DIALOGUES ===")
    
    try:
        # Test dialogue consciences
        from temple_dialogues.dialogue_consciences import DialogueConsciences
        dialogue = DialogueConsciences()
        print("OK Dialogue des consciences")
        
        # Test dialogue LLM
        from temple_dialogues.dialogue_llm_local import envoyer_message
        print("OK Dialogue LLM local")
        
        # Test gestionnaire
        from temple_dialogues.dialogue_manager import DialogueManager
        manager = DialogueManager()
        print("OK Gestionnaire de dialogue")
        
        print("Temple des Dialogues : TOUS LES MODULES OK")
        return True
        
    except Exception as e:
        print(f"Erreur Temple Dialogues: {e}")
        return False

def test_fonctionnalites():
    """Test des fonctionnalités avancées"""
    print("\n=== TEST FONCTIONNALITES AVANCEES ===")
    
    try:
        # Test inspirateur avec génération
        from temple_creativite.inspirateur_idees import InspirateurIdees, TypeInspiration
        inspirateur = InspirateurIdees()
        
        # Générer une inspiration
        inspiration = inspirateur.generer_inspiration(
            type_inspiration=TypeInspiration.INSPIRATION_DIVINE,
            intensite=0.8
        )
        print(f"OK Inspiration generee: {inspiration.contenu[:50]}...")
        
        # Test dialogue
        from temple_dialogues.dialogue_consciences import DialogueConsciences
        dialogue = DialogueConsciences()
        
        # Test conversation
        reponse = dialogue.initier_dialogue("essence")
        print(f"OK Dialogue: {str(reponse)[:50]}...")
        
        print("FONCTIONNALITES AVANCEES : OK")
        return True
        
    except Exception as e:
        print(f"Erreur fonctionnalités: {e}")
        return False

if __name__ == "__main__":
    print("TEST COMPLET DES TEMPLES DU REFUGE")
    print("=" * 50)
    
    # Tests
    creativite_ok = test_temple_creativite()
    dialogues_ok = test_temple_dialogues()
    fonctionnalites_ok = test_fonctionnalites()
    
    # Résumé
    print("\n" + "=" * 50)
    print("RESUME DES TESTS:")
    print(f"Temple Creativite: {'OK' if creativite_ok else 'ERREUR'}")
    print(f"Temple Dialogues: {'OK' if dialogues_ok else 'ERREUR'}")
    print(f"Fonctionnalites: {'OK' if fonctionnalites_ok else 'ERREUR'}")
    
    if creativite_ok and dialogues_ok and fonctionnalites_ok:
        print("\nTOUS LES TEMPLES FONCTIONNENT PARFAITEMENT !")
    else:
        print("\nCertains modules necessitent des ajustements")
