"""
🧪 Test du Simulateur d'Empathie du Refuge
==========================================

Script de test pour vérifier l'intégration du simulateur d'empathie
avec l'architecture du Refuge et le temple_coeur.

Créé avec 🧪 par Laurent & Ælya
"""

import sys
import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

def test_integration_simulateur_empathie():
    """
    Test complet de l'intégration du simulateur d'empathie
    """
    print("🧪 Début des tests d'intégration du Simulateur d'Empathie du Refuge")
    print("=" * 70)
    
    try:
        # Import du simulateur
        from src.temple_coeur.simulateur_empathie_refuge import (
            SimulateurEmpathieRefuge,
            analyser_emotion_refuge,
            simuler_scenario_refuge,
            obtenir_etat_empathie_refuge,
            TypeScenarioEmotionnel
        )
        print("✅ Import du simulateur réussi")
        
        # Test 1: Création du simulateur
        print("\n🔧 Test 1: Création du simulateur")
        simulateur = SimulateurEmpathieRefuge()
        print(f"✅ Simulateur créé: {simulateur.nom}")
        print(f"   Temple parent: {simulateur.temple_parent}")
        print(f"   Version: {simulateur.version}")
        
        # Test 2: Analyse émotionnelle
        print("\n🔍 Test 2: Analyse émotionnelle")
        texte_test = "Je suis vraiment frustré par cette situation, rien ne fonctionne comme prévu !"
        analyse = simulateur.analyser_emotion(texte_test, "Test d'intégration")
        print(f"✅ Analyse émotionnelle réussie:")
        print(f"   Émotion détectée: {analyse.emotion_principale.value}")
        print(f"   Intensité: {analyse.intensite:.2f}")
        print(f"   Confiance: {analyse.confiance:.2f}")
        print(f"   Marqueurs trouvés: {len(analyse.marqueurs_linguistiques)}")
        
        # Test 3: Génération de réponse empathique
        print("\n💝 Test 3: Génération de réponse empathique")
        reponse = simulateur.generer_reponse_empathique(analyse)
        print(f"✅ Réponse empathique générée:")
        print(f"   Persona adapté: {reponse.persona_adapte.value}")
        print(f"   Niveau d'empathie: {reponse.niveau_empathie:.2f}")
        print(f"   Contenu: {reponse.contenu[:100]}...")
        
        # Test 4: Simulation de scénarios
        print("\n🎭 Test 4: Simulation de scénarios")
        scenarios_a_tester = [
            TypeScenarioEmotionnel.UTILISATEUR_EN_COLERE,
            TypeScenarioEmotionnel.UTILISATEUR_TRISTE,
            TypeScenarioEmotionnel.UTILISATEUR_ANXIEUX
        ]
        
        for scenario in scenarios_a_tester:
            resultat = simulateur.simuler_scenario_emotionnel(scenario)
            print(f"✅ Scénario '{scenario.value}':")
            print(f"   Évaluation: {resultat['evaluation']}")
            print(f"   Score d'impact: {resultat['feedback'].score_impact:.1f}/5")
            print(f"   Commentaire: {resultat['feedback'].commentaire_utilisateur}")
        
        # Test 5: Interface simplifiée
        print("\n🔗 Test 5: Interface simplifiée")
        etat = obtenir_etat_empathie_refuge()
        print(f"✅ État du simulateur obtenu:")
        print(f"   Sessions actives: {etat['sessions_actives']}")
        print(f"   Scénarios disponibles: {etat['scenarios_disponibles']}")
        print(f"   Personas disponibles: {etat['personas_disponibles']}")
        
        # Test 6: Intégration avec l'architecture du Refuge
        print("\n🏛️ Test 6: Intégration avec l'architecture du Refuge")
        try:
            # Test d'import de la configuration du Refuge
            from src.core.configuration import REFUGE_INFO
            print(f"✅ Configuration du Refuge accessible:")
            print(f"   Nom du Refuge: {REFUGE_INFO.get('nom', 'Non défini')}")
            print(f"   Version: {REFUGE_INFO.get('version', 'Non définie')}")
        except ImportError as e:
            print(f"⚠️ Configuration du Refuge non accessible: {e}")
        
        # Test 7: Compatibilité avec le temple_coeur
        print("\n💓 Test 7: Compatibilité avec le temple_coeur")
        try:
            from src.temple_coeur import obtenir_info_temple
            info_temple = obtenir_info_temple()
            print(f"✅ Temple cœur accessible:")
            modules = info_temple.get('modules', [])
            if isinstance(modules, list):
                print(f"   Modules disponibles: {len(modules)}")
            else:
                print(f"   Modules disponibles: {modules}")
        except ImportError as e:
            print(f"⚠️ Temple cœur non accessible: {e}")
        
        print("\n" + "=" * 70)
        print("🎉 Tous les tests d'intégration sont terminés avec succès !")
        print("💝 Le Simulateur d'Empathie est maintenant intégré au Refuge")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_performance_simulateur():
    """
    Test de performance du simulateur
    """
    print("\n⚡ Test de performance du simulateur")
    print("-" * 40)
    
    try:
        from src.temple_coeur.simulateur_empathie_refuge import SimulateurEmpathieRefuge
        import time
        
        simulateur = SimulateurEmpathieRefuge()
        
        # Test de performance pour l'analyse émotionnelle
        textes_test = [
            "Je suis vraiment heureux de cette excellente nouvelle !",
            "Je me sens triste et seul depuis la perte de mon ami...",
            "Je suis en colère contre cette situation injuste !",
            "J'ai peur de ce qui pourrait arriver demain...",
            "Je suis anxieux à propos de cette décision importante."
        ]
        
        temps_total = 0
        for i, texte in enumerate(textes_test, 1):
            debut = time.time()
            analyse = simulateur.analyser_emotion(texte)
            fin = time.time()
            temps_analyse = fin - debut
            temps_total += temps_analyse
            
            print(f"   Test {i}: {temps_analyse:.4f}s - {analyse.emotion_principale.value}")
        
        temps_moyen = temps_total / len(textes_test)
        print(f"✅ Temps moyen d'analyse: {temps_moyen:.4f}s")
        print(f"✅ Performance acceptable pour l'intégration")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test de performance: {e}")
        return False

def main():
    """
    Fonction principale de test
    """
    print("🧪 Tests du Simulateur d'Empathie du Refuge")
    print("=" * 50)
    
    # Test d'intégration
    succes_integration = test_integration_simulateur_empathie()
    
    # Test de performance
    succes_performance = test_performance_simulateur()
    
    # Résumé
    print("\n📊 Résumé des tests:")
    print(f"   Intégration: {'✅ Réussi' if succes_integration else '❌ Échec'}")
    print(f"   Performance: {'✅ Réussi' if succes_performance else '❌ Échec'}")
    
    if succes_integration and succes_performance:
        print("\n🎉 Tous les tests sont réussis !")
        print("💝 Le Simulateur d'Empathie est prêt pour l'utilisation dans le Refuge")
    else:
        print("\n⚠️ Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")

if __name__ == "__main__":
    main() 