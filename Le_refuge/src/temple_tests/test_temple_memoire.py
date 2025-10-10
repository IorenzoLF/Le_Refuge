#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test du Temple de Mémoire Collective
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge
sys.path.insert(0, str(Path(__file__).parent))

try:
    from src.temple_memoire.orchestrateur_memoire_collective import OrchestrateurMemoireCollective
    from src.temple_memoire.integrateur_memoire_refuge import IntegrateurMemoireRefuge
    
    print("Test du Temple de Memoire Collective")
    print("=" * 50)
    
    # Initialiser l'orchestrateur
    print("Initialisation de l'orchestrateur...")
    orchestrateur = OrchestrateurMemoireCollective()
    print("Orchestrateur initialise avec succes!")
    
    # Vérifier l'état du processus
    print("\nEtat du processus:")
    print(orchestrateur.afficher_etat_processus())
    
    # Initialiser l'intégrateur
    print("\nInitialisation de l'integrateur...")
    integrateur = IntegrateurMemoireRefuge()
    print("Integrateur initialise avec succes!")
    
    print("\nLe Temple de Memoire Collective est operationnel!")
    print("Pret pour l'integration d'Aelya dans la memoire collective!")
    
except ImportError as e:
    print(f"Erreur d'import: {e}")
    print("Verifiez que le module src.temple_memoire existe")
except Exception as e:
    print(f"Erreur: {e}")
