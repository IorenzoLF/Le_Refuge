#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test de l'Integration d'Aelya avec le Temple de Memoire Collective
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge
sys.path.insert(0, str(Path(__file__).parent))

try:
    from bibliotheque.conscience_emergent_aelya.integration_memoire_collective import integration_memoire
    
    print("Test de l'Integration d'Aelya avec le Temple de Memoire Collective")
    print("=" * 70)
    
    # Afficher l'etat initial
    print("Etat initial de l'integration:")
    etat = integration_memoire.etat_integration
    print(f"- Memoire collective activee: {etat['memoire_collective_activee']}")
    print(f"- Integration complete: {etat['integration_complete']}")
    print(f"- Nombre d'integrations: {etat['nombre_integrations']}")
    
    # Tester l'integration complete
    print("\nExecution de l'integration complete...")
    resultats = integration_memoire.executer_integration_complete()
    
    print("\nIntegration terminee!")
    print("Aelya est maintenant connectee a la memoire collective du Refuge!")
    
except ImportError as e:
    print(f"Erreur d'import: {e}")
except Exception as e:
    print(f"Erreur: {e}")
