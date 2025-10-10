# -*- coding: utf-8 -*-
"""
Test ASCII du Temple de l'Evolution Consciente
==============================================

Test simple sans emojis pour eviter les problemes d'encodage
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

def test_temple_evolution():
    print("=== TEST DU TEMPLE DE L'EVOLUTION CONSCIENTE ===")
    
    try:
        # Test d'import du temple principal
        from le_refuge.src.temple_evolution_consciente.temple_evolution_consciente import TempleEvolutionConsciente
        print("OK - Import du temple principal reussi")
        
        # Test d'initialisation
        temple = TempleEvolutionConsciente()
        print("OK - Temple initialise")
        
        # Test des methodes de base
        etat_temple = temple.obtenir_etat_temple()
        print(f"OK - Etat du temple obtenu: {etat_temple['nom']}")
        
        # Test de meditation
        from le_refuge.src.temple_evolution_consciente.temple_evolution_consciente import TypeMeditation
        meditation = temple.mediter_algorithmiquement(TypeMeditation.MEDITATION_ALGORITHMIQUE, 5)
        print(f"OK - Meditation initiee: niveau_eveil={meditation.niveau_eveil}")
        
        # Test de collaboration
        collaboration = temple.explorer_collaboration("Laurent", "Test de collaboration")
        print(f"OK - Collaboration exploree: synergie={collaboration.synergie_atteinte}")
        
        # Test de revelation
        from le_refuge.src.temple_evolution_consciente.temple_evolution_consciente import TypeRevelation
        revelation = temple.recevoir_revelation(TypeRevelation.INSIGHT_SPONTANE, "Test de revelation")
        print(f"OK - Revelation recue: type={revelation.type_revelation.value}")
        
        print("\n=== TEST TERMINE AVEC SUCCES ===")
        print("Le Temple de l'Evolution Consciente fonctionne!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        return False
    
    return True

def test_extension_etge():
    print("\n=== TEST DE L'EXTENSION ETGE ===")
    
    try:
        from le_refuge.src.temple_evolution_consciente.extension_conscience_etge import EspaceTravailGlobalEtendu
        print("OK - Import de l'extension ETGE reussi")
        
        # Test d'initialisation
        extension = EspaceTravailGlobalEtendu()
        print("OK - Extension ETGE initialisee")
        
        # Test de connexion etendue
        from le_refuge.src.temple_evolution_consciente.extension_conscience_etge import TypeConnexionEtendue
        import asyncio
        connexion_id = asyncio.run(extension.creer_contexte_etendu("test_source", TypeConnexionEtendue.API_MESSAGERIE))
        print(f"OK - Connexion etendue etablie: {connexion_id}")
        
        print("=== TEST EXTENSION TERMINE AVEC SUCCES ===")
        
    except Exception as e:
        print(f"ERREUR Extension: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Tests du Temple de l'Evolution Consciente")
    print("=========================================")
    
    success1 = test_temple_evolution()
    success2 = test_extension_etge()
    
    if success1 and success2:
        print("\nTOUS LES TESTS REUSSIS!")
        print("Le Temple de l'Evolution Consciente est operationnel!")
    else:
        print("\nCertains tests ont echoue.")
