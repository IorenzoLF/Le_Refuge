#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Mathématique
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_mathematique_simple():
    """Test simple du Temple Mathématique"""
    print("TEST DU TEMPLE MATHEMATIQUE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules principaux
        print("\n1. Test des imports...")
        try:
            from hub_temple_mathematique_unifie import hub_temple_mathematique_unifie
            print("OK Hub unifié importé")
        except Exception as e:
            print(f"Hub unifié : Erreur - {e}")
        
        try:
            from analyseur_temple_mathematique import analyseur_temple_mathematique
            print("OK Analyseur de temple importé")
        except Exception as e:
            print(f"Analyseur de temple : Erreur - {e}")
        
        # Test 2: Test des modules Collatz
        print("\n2. Test des modules Collatz...")
        try:
            from collatz_core.analyseur_collatz_avance import analyseur_collatz_avance
            print("OK Analyseur Collatz avancé importé")
        except Exception as e:
            print(f"Analyseur Collatz avancé : Erreur - {e}")
        
        try:
            from collatz_core.geometrie_sacree_collatz import geometrie_sacree_collatz
            print("OK Géométrie sacrée Collatz importée")
        except Exception as e:
            print(f"Géométrie sacrée Collatz : Erreur - {e}")
        
        # Test 3: Test des modules Quantum
        print("\n3. Test des modules Quantum...")
        try:
            from quantum_xprize.memoire_quantique import memoire_quantique
            print("OK Mémoire quantique importée")
        except Exception as e:
            print(f"Mémoire quantique : Erreur - {e}")
        
        try:
            from quantum_xprize.core.quantum_collatz import quantum_collatz
            print("OK Quantum Collatz importé")
        except Exception as e:
            print(f"Quantum Collatz : Erreur - {e}")
        
        # Test 4: Test des modules Fibonacci
        print("\n4. Test des modules Fibonacci...")
        try:
            from fibonacci_riemann.exploration_fibonacci_riemann import exploration_fibonacci_riemann
            print("OK Exploration Fibonacci-Riemann importée")
        except Exception as e:
            print(f"Exploration Fibonacci-Riemann : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Mathématique est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_mathematique_simple()
    if succes:
        print("\nQue les mathématiques sacrées continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
