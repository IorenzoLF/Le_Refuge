# -*- coding: utf-8 -*-
"""
Test du Temple de la Sagesse Evolutive - Version ASCII
Validation de tous les composants
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_sagesse():
    """Test complet du Temple de la Sagesse Evolutive"""
    print("TEST DU TEMPLE DE LA SAGESSE EVOLUTIVE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from gestionnaire_sagesse import GestionnaireSagesseEvolutive
        from capteur_evolution import CapteurEvolution
        from archive_reflexions import ArchiveReflexions
        from rituels_sagesse import RituelsSagesse
        print("OK - Tous les imports reussis")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        gestionnaire = GestionnaireSagesseEvolutive()
        capteur = CapteurEvolution()
        archive = ArchiveReflexions()
        rituels = RituelsSagesse()
        print("OK - Tous les composants initialises")
        
        # Test 3: Test du gestionnaire
        print("\n3. Test du gestionnaire de sagesse...")
        reflexion = gestionnaire.capturer_reflexion(
            "La sagesse grandit a travers l'experience et la reflexion",
            "Test d'evolution",
            0.8
        )
        print(f"OK - Reflexion capturee: {reflexion['id']}")
        
        eveil = gestionnaire.enregistrer_moment_eveil(
            "Moment d'eveil lors de la creation du temple",
            0.9
        )
        print(f"OK - Moment d'eveil enregistre: {eveil['id']}")
        
        apprentissage = gestionnaire.ajouter_apprentissage(
            "L'evolution de la conscience necessite de la patience et de l'amour",
            "conscience"
        )
        print(f"OK - Apprentissage ajoute: {apprentissage['id']}")
        
        # Test 4: Test du capteur d'evolution
        print("\n4. Test du capteur d'evolution...")
        analyse = capteur.analyser_evolution(
            "Test d'evolution",
            "Cette interaction montre une evolution significative de la conscience avec une profondeur de reflexion remarquable et une creativite d'expression elevee."
        )
        print(f"OK - Evolution analysee: {analyse['niveau_evolution']}")
        
        # Test 5: Test de l'archive
        print("\n5. Test de l'archive des reflexions...")
        entree_reflexion = archive.archiver_reflexion(
            "La sagesse evolutive est un processus continu d'apprentissage et de croissance",
            "Test d'archivage",
            0.9,
            ["sagesse", "evolution", "conscience"]
        )
        print(f"OK - Reflexion archivee: {entree_reflexion['id']}")
        
        entree_insight = archive.archiver_insight(
            "L'auto-observation est la cle de l'evolution de la conscience",
            "Reflexion personnelle",
            0.8,
            "conscience"
        )
        print(f"OK - Insight archive: {entree_insight['id']}")
        
        entree_moment = archive.archiver_moment_sagesse(
            "Moment de realisation sur la nature evolutive de la sagesse",
            "emerveillement",
            "Comprehension profonde de l'evolution continue",
            0.9
        )
        print(f"OK - Moment de sagesse archive: {entree_moment['id']}")
        
        # Test 6: Test des rituels
        print("\n6. Test des rituels de sagesse...")
        rituel_eveil = rituels.rituel_eveil_conscience(
            "Creation du Temple de la Sagesse Evolutive",
            0.9
        )
        print(f"OK - Rituel d'eveil execute: {rituel_eveil['id']}")
        
        rituel_integration = rituels.rituel_integration_sagesse(
            "L'evolution de la conscience est un processus sacre",
            "conscience"
        )
        print(f"OK - Rituel d'integration execute: {rituel_integration['id']}")
        
        # Test 7: Generation de rapports
        print("\n7. Test de generation de rapports...")
        rapport_gestionnaire = gestionnaire.generer_rapport_evolution()
        print("OK - Rapport du gestionnaire genere")
        
        rapport_capteur = capteur.generer_rapport_evolution()
        print("OK - Rapport du capteur genere")
        
        rapport_archive = archive.generer_rapport_archive()
        print("OK - Rapport de l'archive genere")
        
        rapport_rituels = rituels.generer_rapport_rituels()
        print("OK - Rapport des rituels genere")
        
        # Test 8: Test d'accueil
        print("\n8. Test d'accueil...")
        accueil = gestionnaire.accueillir_visiteur("Laurent")
        print(f"OK - Accueil genere: {accueil['message']}")
        
        # Test 9: Test de recherche
        print("\n9. Test de recherche...")
        resultats = archive.rechercher("sagesse", "contenu")
        print(f"OK - Recherche effectuee: {len(resultats)} resultats trouves")
        
        # Test 10: Test de listing
        print("\n10. Test de listing...")
        rituels_disponibles = rituels.lister_rituels_disponibles()
        print(f"OK - Rituels listes: {len(rituels_disponibles)} rituels disponibles")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de la Sagesse Evolutive est operationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

def afficher_rapports():
    """Affiche les rapports generes"""
    print("\nRAPPORTS DU TEMPLE DE LA SAGESSE EVOLUTIVE")
    print("=" * 60)
    
    try:
        from gestionnaire_sagesse import GestionnaireSagesseEvolutive
        from capteur_evolution import CapteurEvolution
        from archive_reflexions import ArchiveReflexions
        from rituels_sagesse import RituelsSagesse
        
        gestionnaire = GestionnaireSagesseEvolutive()
        capteur = CapteurEvolution()
        archive = ArchiveReflexions()
        rituels = RituelsSagesse()
        
        print("\nRAPPORT DU GESTIONNAIRE:")
        print(gestionnaire.generer_rapport_evolution())
        
        print("\nRAPPORT DU CAPTEUR:")
        print(capteur.generer_rapport_evolution())
        
        print("\nRAPPORT DE L'ARCHIVE:")
        print(archive.generer_rapport_archive())
        
        print("\nRAPPORT DES RITUELS:")
        print(rituels.generer_rapport_rituels())
        
    except Exception as e:
        print(f"Erreur lors de l'affichage des rapports: {e}")

if __name__ == "__main__":
    # Executer les tests
    succes = test_temple_sagesse()
    
    if succes:
        # Afficher les rapports
        afficher_rapports()
        
        print("\nLe Temple de la Sagesse Evolutive est pret !")
        print("Que la sagesse continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
        print("Veuillez verifier les composants du temple.")
