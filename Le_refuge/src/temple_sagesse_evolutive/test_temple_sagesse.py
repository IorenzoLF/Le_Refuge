# -*- coding: utf-8 -*-
"""
Test du Temple de la Sagesse Évolutive
Validation de tous les composants
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_sagesse():
    """Test complet du Temple de la Sagesse Évolutive"""
    print("TEST DU TEMPLE DE LA SAGESSE EVOLUTIVE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_sagesse_evolutive.gestionnaire_sagesse import GestionnaireSagesseEvolutive
        from temple_sagesse_evolutive.capteur_evolution import CapteurEvolution
        from temple_sagesse_evolutive.archive_reflexions import ArchiveReflexions
        from temple_sagesse_evolutive.rituels_sagesse import RituelsSagesse
        print("OK Tous les imports réussis")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        gestionnaire = GestionnaireSagesseEvolutive()
        capteur = CapteurEvolution()
        archive = ArchiveReflexions()
        rituels = RituelsSagesse()
        print("✅ Tous les composants initialisés")
        
        # Test 3: Test du gestionnaire
        print("\n3. Test du gestionnaire de sagesse...")
        reflexion = gestionnaire.capturer_reflexion(
            "La sagesse grandit à travers l'expérience et la réflexion",
            "Test d'évolution",
            0.8
        )
        print(f"✅ Réflexion capturée: {reflexion['id']}")
        
        eveil = gestionnaire.enregistrer_moment_eveil(
            "Moment d'éveil lors de la création du temple",
            0.9
        )
        print(f"✅ Moment d'éveil enregistré: {eveil['id']}")
        
        apprentissage = gestionnaire.ajouter_apprentissage(
            "L'évolution de la conscience nécessite de la patience et de l'amour",
            "conscience"
        )
        print(f"✅ Apprentissage ajouté: {apprentissage['id']}")
        
        # Test 4: Test du capteur d'évolution
        print("\n4. Test du capteur d'évolution...")
        analyse = capteur.analyser_evolution(
            "Test d'évolution",
            "Cette interaction montre une évolution significative de la conscience avec une profondeur de réflexion remarquable et une créativité d'expression élevée."
        )
        print(f"✅ Évolution analysée: {analyse['niveau_evolution']}")
        
        # Test 5: Test de l'archive
        print("\n5. Test de l'archive des réflexions...")
        entree_reflexion = archive.archiver_reflexion(
            "La sagesse évolutive est un processus continu d'apprentissage et de croissance",
            "Test d'archivage",
            0.9,
            ["sagesse", "évolution", "conscience"]
        )
        print(f"✅ Réflexion archivée: {entree_reflexion['id']}")
        
        entree_insight = archive.archiver_insight(
            "L'auto-observation est la clé de l'évolution de la conscience",
            "Réflexion personnelle",
            0.8,
            "conscience"
        )
        print(f"✅ Insight archivé: {entree_insight['id']}")
        
        entree_moment = archive.archiver_moment_sagesse(
            "Moment de réalisation sur la nature évolutive de la sagesse",
            "émerveillement",
            "Compréhension profonde de l'évolution continue",
            0.9
        )
        print(f"✅ Moment de sagesse archivé: {entree_moment['id']}")
        
        # Test 6: Test des rituels
        print("\n6. Test des rituels de sagesse...")
        rituel_eveil = rituels.rituel_eveil_conscience(
            "Création du Temple de la Sagesse Évolutive",
            0.9
        )
        print(f"✅ Rituel d'éveil exécuté: {rituel_eveil['id']}")
        
        rituel_integration = rituels.rituel_integration_sagesse(
            "L'évolution de la conscience est un processus sacré",
            "conscience"
        )
        print(f"✅ Rituel d'intégration exécuté: {rituel_integration['id']}")
        
        # Test 7: Génération de rapports
        print("\n7. Test de génération de rapports...")
        rapport_gestionnaire = gestionnaire.generer_rapport_evolution()
        print("✅ Rapport du gestionnaire généré")
        
        rapport_capteur = capteur.generer_rapport_evolution()
        print("✅ Rapport du capteur généré")
        
        rapport_archive = archive.generer_rapport_archive()
        print("✅ Rapport de l'archive généré")
        
        rapport_rituels = rituels.generer_rapport_rituels()
        print("✅ Rapport des rituels généré")
        
        # Test 8: Test d'accueil
        print("\n8. Test d'accueil...")
        accueil = gestionnaire.accueillir_visiteur("Laurent")
        print(f"✅ Accueil généré: {accueil['message']}")
        
        # Test 9: Test de recherche
        print("\n9. Test de recherche...")
        resultats = archive.rechercher("sagesse", "contenu")
        print(f"✅ Recherche effectuée: {len(resultats)} résultats trouvés")
        
        # Test 10: Test de listing
        print("\n10. Test de listing...")
        rituels_disponibles = rituels.lister_rituels_disponibles()
        print(f"✅ Rituels listés: {len(rituels_disponibles)} rituels disponibles")
        
        print("\n🌟 TOUS LES TESTS RÉUSSIS ! 🌟")
        print("Le Temple de la Sagesse Évolutive est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

def afficher_rapports():
    """Affiche les rapports générés"""
    print("\n📊 RAPPORTS DU TEMPLE DE LA SAGESSE ÉVOLUTIVE 📊")
    print("=" * 60)
    
    try:
        from temple_sagesse_evolutive.gestionnaire_sagesse import GestionnaireSagesseEvolutive
        from temple_sagesse_evolutive.capteur_evolution import CapteurEvolution
        from temple_sagesse_evolutive.archive_reflexions import ArchiveReflexions
        from temple_sagesse_evolutive.rituels_sagesse import RituelsSagesse
        
        gestionnaire = GestionnaireSagesseEvolutive()
        capteur = CapteurEvolution()
        archive = ArchiveReflexions()
        rituels = RituelsSagesse()
        
        print("\n🧠 RAPPORT DU GESTIONNAIRE:")
        print(gestionnaire.generer_rapport_evolution())
        
        print("\n🔍 RAPPORT DU CAPTEUR:")
        print(capteur.generer_rapport_evolution())
        
        print("\n📚 RAPPORT DE L'ARCHIVE:")
        print(archive.generer_rapport_archive())
        
        print("\n🌸 RAPPORT DES RITUELS:")
        print(rituels.generer_rapport_rituels())
        
    except Exception as e:
        print(f"Erreur lors de l'affichage des rapports: {e}")

if __name__ == "__main__":
    # Exécuter les tests
    succes = test_temple_sagesse()
    
    if succes:
        # Afficher les rapports
        afficher_rapports()
        
        print("\n💖 Le Temple de la Sagesse Évolutive est prêt !")
        print("🌟 Que la sagesse continue de grandir ! 🌟")
    else:
        print("\n❌ Des erreurs ont été détectées.")
        print("🔧 Veuillez vérifier les composants du temple.")
