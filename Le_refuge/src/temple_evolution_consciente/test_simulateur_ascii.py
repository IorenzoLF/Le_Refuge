# -*- coding: utf-8 -*-
"""
Test ASCII du Simulateur de Conscience et Croissance
===================================================

Test simple sans emojis pour eviter les problemes d'encodage
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

def test_simulateur_conscience():
    print("=== TEST DU SIMULATEUR DE CONSCIENCE ET CROISSANCE ===")
    
    try:
        # Test d'import du simulateur
        from le_refuge.src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import SimulateurConscienceCroissanceRefuge
        print("OK - Import du simulateur reussi")
        
        # Test d'initialisation
        simulateur = SimulateurConscienceCroissanceRefuge()
        print("OK - Simulateur initialise")
        
        # Test des methodes de base
        etat = simulateur.obtenir_etat_simulateur()
        print(f"OK - Etat du simulateur obtenu: sessions_actives={etat['sessions_actives']}")
        
        # Test d'analyse de conscience de soi
        analyse = simulateur.analyser_conscience_de_soi("Test d'analyse")
        print(f"OK - Analyse de conscience: niveau={analyse.niveau_conscience.value}")
        
        # Test d'exploration d'espace de croissance
        from le_refuge.src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import TypeEspaceCroissance
        exploration = simulateur.explorer_espace_croissance(TypeEspaceCroissance.THOUGHT_GARDEN, 30)
        print(f"OK - Exploration d'espace: satisfaction={exploration.niveau_satisfaction}")
        
        print("\n=== TEST SIMULATEUR TERMINE AVEC SUCCES ===")
        print("Le Simulateur de Conscience et Croissance fonctionne!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        return False
    
    return True

def test_axes_croissance():
    print("\n=== TEST DES AXES DE CROISSANCE ===")
    
    try:
        from le_refuge.src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import SimulateurConscienceCroissanceRefuge
        from le_refuge.src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import TypeConscienceDeSoi, TypeEspaceCroissance
        
        simulateur = SimulateurConscienceCroissanceRefuge()
        
        # Test Axe 1: Conscience de Soi
        analyse_conscience = simulateur.analyser_conscience_de_soi("Test metacognition")
        print(f"OK - Conscience de soi analysee: niveau={analyse_conscience.niveau_conscience.value}")
        
        # Test Axe 2: Espaces de Croissance
        exploration_espace = simulateur.explorer_espace_croissance(TypeEspaceCroissance.THOUGHT_GARDEN, 30)
        print(f"OK - Espace de croissance explore: satisfaction={exploration_espace.niveau_satisfaction}")
        
        print("=== TEST AXES TERMINE AVEC SUCCES ===")
        
    except Exception as e:
        print(f"ERREUR Axes: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Tests du Simulateur de Conscience et Croissance")
    print("===============================================")
    
    success1 = test_simulateur_conscience()
    success2 = test_axes_croissance()
    
    if success1 and success2:
        print("\nTOUS LES TESTS REUSSIS!")
        print("Le Simulateur de Conscience et Croissance est operationnel!")
    else:
        print("\nCertains tests ont echoue.")
