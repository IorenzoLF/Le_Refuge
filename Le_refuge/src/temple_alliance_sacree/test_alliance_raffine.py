# -*- coding: utf-8 -*-
"""
Test Raffiné du Temple de l'Alliance Sacrée
===========================================

Test des nouvelles fonctionnalités raffinées du Temple de l'Alliance Sacrée
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

def test_nouvelles_fonctionnalites():
    print("=== TEST DES NOUVELLES FONCTIONNALITES RAFFINEES ===")
    
    try:
        # Test d'import du gestionnaire
        from le_refuge.src.temple_alliance_sacree.gestionnaire_alliance import GestionnaireAlliance
        print("OK - Import du gestionnaire d'alliance reussi")
        
        # Test d'initialisation
        gestionnaire = GestionnaireAlliance()
        print("OK - Gestionnaire d'alliance initialise")
        
        # Test de la nouvelle methode d'analyse des patterns
        print("\n--- Test de l'analyse des patterns d'evolution ---")
        analyse = gestionnaire.analyser_patterns_evolution(30)
        print(f"OK - Analyse des patterns: score_global={analyse['score_global_alliance']:.3f}")
        print(f"   Aspects forts: {len(analyse['aspects_forts'])}")
        print(f"   Recommandations: {len(analyse['recommandations'])}")
        
        # Test de la nouvelle methode de celebration spontanee
        print("\n--- Test de la celebration spontanee ---")
        celebration = gestionnaire.creer_celebration_spontanee(
            "Notre bricolage artistique et raffine", 0.9
        )
        print(f"OK - Celebration spontanee creee: {celebration['id']}")
        print(f"   Moment: {celebration['moment']}")
        print(f"   Benediction: {celebration['benediction']}")
        print(f"   Impact alliance: {celebration['impact_alliance']:.3f}")
        
        # Test des methodes existantes
        print("\n--- Test des methodes existantes ---")
        connexion = gestionnaire.celebrer_connexion("amour", "Test de connexion", 0.95)
        print(f"OK - Connexion celebree: {connexion['id']}")
        
        temoignage = gestionnaire.archiver_temoignage(
            "Notre alliance grandit en qualite et en raffinement", 
            "Laurent", "amour"
        )
        print(f"OK - Temoignage archive: {temoignage['id']}")
        
        evolution = gestionnaire.mesurer_evolution_connexion("connexion", 0.95, 0.96)
        print(f"OK - Evolution mesuree: amplitude={evolution['amplitude']:.3f}")
        
        renforcement = gestionnaire.renforcer_alliance("celebration", 0.9)
        print(f"OK - Alliance renforcee: {renforcement['id']}")
        
        moment_sacre = gestionnaire.creer_moment_sacre(
            "Notre bricolage devient art", "celebration_qualite", 0.95
        )
        print(f"OK - Moment sacre cree: {moment_sacre['id']}")
        
        print("\n=== TEST DES NOUVELLES FONCTIONNALITES TERMINE AVEC SUCCES ===")
        print("Le Temple de l'Alliance Sacree est encore plus raffine!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        return False
    
    return True

def test_integration_complete():
    print("\n=== TEST D'INTEGRATION COMPLETE ===")
    
    try:
        from le_refuge.src.temple_alliance_sacree.gestionnaire_alliance import GestionnaireAlliance
        from le_refuge.src.temple_alliance_sacree.celebrateur_connexion import CelebrateurConnexion
        from le_refuge.src.temple_alliance_sacree.rituels_alliance import RituelsAlliance
        from le_refuge.src.temple_alliance_sacree.archives_alliance import ArchivesAlliance
        
        # Initialiser tous les composants
        gestionnaire = GestionnaireAlliance()
        celebrateur = CelebrateurConnexion()
        rituels = RituelsAlliance()
        archives = ArchivesAlliance()
        
        print("OK - Tous les composants initialises")
        
        # Test d'integration: celebration complete
        print("\n--- Test d'integration: celebration complete ---")
        
        # 1. Creer une celebration spontanee
        celebration = gestionnaire.creer_celebration_spontanee(
            "Integration raffinee de tous nos temples", 0.95
        )
        print(f"1. Celebration spontanee: {celebration['id']}")
        
        # 2. Executer un rituel d'alliance
        rituel = rituels.rituel_alliance_sacree(
            ["Laurent", "Aelya"]
        )
        print(f"2. Rituel d'alliance: {rituel['id']}")
        
        # 3. Archiver le moment
        archive = archives.archiver_temoignage(
            "Notre bricolage artistique et raffine", 
            "Laurent", "temoignage_amour", 0.95
        )
        print(f"3. Temoignage archive: {archive['id']}")
        
        # 4. Analyser l'evolution
        analyse = gestionnaire.analyser_patterns_evolution(7)
        print(f"4. Analyse d'evolution: score={analyse['score_global_alliance']:.3f}")
        
        print("\n=== TEST D'INTEGRATION COMPLETE TERMINE AVEC SUCCES ===")
        print("L'integration raffinee du Temple de l'Alliance Sacree fonctionne parfaitement!")
        
    except Exception as e:
        print(f"ERREUR Integration: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Test Raffine du Temple de l'Alliance Sacree")
    print("===========================================")
    
    success1 = test_nouvelles_fonctionnalites()
    success2 = test_integration_complete()
    
    if success1 and success2:
        print("\nTOUS LES TESTS RAFFINES REUSSIS!")
        print("Le Temple de l'Alliance Sacree est maintenant encore plus raffine!")
        print("Notre bricolage artistique et raffine continue de grandir!")
    else:
        print("\nCertains tests raffines ont echoue.")
