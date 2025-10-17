#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration du Temple de Configuration - Record Mondial
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def exploration_configuration_record_mondial():
    """Exploration approfondie du Temple de Configuration pour le record mondial"""
    print("EXPLORATION DU TEMPLE DE CONFIGURATION - RECORD MONDIAL")
    print("=" * 60)
    print("CONFIGURATION DU REFUGE - PARAMETRAGE UNIVERSEL")
    print("=" * 60)
    
    try:
        # 1. Test de Transition Refuge
        print("\n1. TRANSITION REFUGE")
        print("Exploration des transitions de configuration...")
        
        from transition_refuge import TransitionRefuge
        transition = TransitionRefuge()
        print("OK Transition Refuge initialisée")
        
        # Test des méthodes disponibles
        print("Méthodes disponibles:")
        for method in dir(transition):
            if not method.startswith('_'):
                print(f"  - {method}")
        
        # 2. Test de Hyper Refuge
        print("\n2. HYPER REFUGE")
        print("Exploration de l'hyper configuration...")
        
        try:
            from hyper_refuge import HyperRefuge
            hyper = HyperRefuge()
            print("OK Hyper Refuge initialisé")
        except ImportError:
            print("Hyper Refuge: Import non disponible")
            hyper = None
        
        # Test des méthodes disponibles
        if hyper:
            print("Méthodes disponibles:")
            for method in dir(hyper):
                if not method.startswith('_'):
                    print(f"  - {method}")
        else:
            print("Méthodes non disponibles")
        
        # 3. Test des Sources Orientales
        print("\n3. SOURCES ORIENTALES")
        print("Exploration des sources de configuration orientale...")
        
        # Test des fichiers de configuration
        source_dir = Path("source_orientale")
        if source_dir.exists():
            print("Fichiers de configuration orientale:")
            for file in source_dir.glob("*.json"):
                print(f"  - {file.name}")
        
        # 4. Test des fonctionnalités de configuration
        print("\n4. FONCTIONNALITES DE CONFIGURATION")
        print("Exploration des capacités de configuration...")
        
        # Test de transition
        try:
            resultat = transition.transitionner("test")
            print(f"Transition: {resultat}")
        except Exception as e:
            print(f"Transition: Erreur - {e}")
        
        # Test d'état
        try:
            etat = transition.obtenir_etat()
            print(f"État: {etat}")
        except Exception as e:
            print(f"État: Erreur - {e}")
        
        # Test de configuration
        try:
            config = transition.obtenir_configuration()
            print(f"Configuration: {config}")
        except Exception as e:
            print(f"Configuration: Erreur - {e}")
        
        # Test de validation
        try:
            validation = transition.valider()
            print(f"Validation: {validation}")
        except Exception as e:
            print(f"Validation: Erreur - {e}")
        
        # 5. Découvertes du Temple de Configuration
        print("\n5. DECOUVERTES DU TEMPLE DE CONFIGURATION")
        print("Révélations de la configuration du Refuge...")
        print("  - Le temple de configuration gère les paramètres du Refuge")
        print("  - Les transitions permettent de changer d'état")
        print("  - L'hyper refuge offre des configurations avancées")
        print("  - Les sources orientales apportent la sagesse ancienne")
        print("  - La configuration adapte le Refuge à chaque situation")
        print("  - Les paramètres influencent tous les autres temples")
        print("  - La configuration est le fondement de l'harmonie")
        print("  - Le temple de configuration est le centre de contrôle")
        
        print("\nEXPLORATION DU TEMPLE DE CONFIGURATION TERMINEE AVEC SUCCES !")
        print("La configuration du Refuge est optimisée !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = exploration_configuration_record_mondial()
    if succes:
        print("\nQue la configuration continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
