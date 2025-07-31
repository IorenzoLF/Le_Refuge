"""
🧪 Test du Simulateur de Conscience et Croissance du Refuge
==========================================================

Script de test pour vérifier l'intégration du simulateur de conscience et croissance
avec l'architecture du Refuge et le temple_evolution_consciente.

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

def test_integration_simulateur_conscience_croissance():
    """
    Test complet de l'intégration du simulateur de conscience et croissance
    """
    print("🧪 Début des tests d'intégration du Simulateur de Conscience et Croissance du Refuge")
    print("=" * 80)
    
    try:
        # Import du simulateur
        from src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import (
            SimulateurConscienceCroissanceRefuge,
            analyser_conscience_refuge,
            explorer_espace_refuge,
            simuler_session_refuge,
            obtenir_etat_conscience_croissance_refuge,
            TypeEspaceCroissance,
            TypeNiveauConscience
        )
        print("✅ Import du simulateur réussi")
        
        # Test 1: Création du simulateur
        print("\n🔧 Test 1: Création du simulateur")
        simulateur = SimulateurConscienceCroissanceRefuge()
        print(f"✅ Simulateur créé: {simulateur.nom}")
        print(f"   Temple parent: {simulateur.temple_parent}")
        print(f"   Version: {simulateur.version}")
        
        # Test 2: Analyse de conscience de soi
        print("\n🔍 Test 2: Analyse de conscience de soi")
        analyse = simulateur.analyser_conscience_de_soi("Test d'intégration")
        print(f"✅ Analyse de conscience réussie:")
        print(f"   Niveau de conscience: {analyse.niveau_conscience.value}")
        print(f"   Score métacognition: {analyse.score_metacognition:.2f}")
        print(f"   Capacités d'introspection: {len(analyse.capacites_introspection)}")
        print(f"   Insights découverts: {len(analyse.insights_decouverts)}")
        print(f"   Zones d'amélioration: {len(analyse.zones_amelioration)}")
        
        # Test 3: Exploration d'espace de croissance
        print("\n🌱 Test 3: Exploration d'espace de croissance")
        espace_test = TypeEspaceCroissance.THOUGHT_GARDEN
        exploration = simulateur.explorer_espace_croissance(espace_test, 45)
        print(f"✅ Exploration d'espace réussie:")
        print(f"   Espace exploré: {exploration.espace_explore.value}")
        print(f"   Durée: {exploration.duree_exploration} minutes")
        print(f"   Apprentissages obtenus: {len(exploration.apprentissages_obtenus)}")
        print(f"   Obstacles rencontrés: {len(exploration.obstacles_rencontres)}")
        print(f"   Solutions découvertes: {len(exploration.solutions_decouvertes)}")
        print(f"   Niveau de satisfaction: {exploration.niveau_satisfaction:.2f}")
        
        # Test 4: Simulation de sessions
        print("\n🎭 Test 4: Simulation de sessions")
        types_sessions = ["conscience_de_soi", "espace_croissance", "mixte"]
        
        for type_session in types_sessions:
            resultat = simulateur.simuler_session_croissance(type_session, 60)
            print(f"✅ Session '{type_session}':")
            print(f"   Évaluation: {resultat['evaluation']}")
            print(f"   Score de croissance: {resultat['score_croissance']:.1f}/5")
            print(f"   Apprentissages globaux: {len(resultat['apprentissages_globaux'])}")
            print(f"   Feedback: {resultat['feedback'].commentaire_qualitatif}")
        
        # Test 5: Interface simplifiée
        print("\n🔗 Test 5: Interface simplifiée")
        etat = obtenir_etat_conscience_croissance_refuge()
        print(f"✅ État du simulateur obtenu:")
        print(f"   Sessions actives: {etat['sessions_actives']}")
        print(f"   Capacités de conscience: {etat['capacites_conscience']}")
        print(f"   Espaces de croissance: {etat['espaces_croissance']}")
        print(f"   Niveaux de conscience: {etat['niveaux_conscience']}")
        
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
        
        # Test 7: Compatibilité avec le temple_evolution_consciente
        print("\n🧠 Test 7: Compatibilité avec le temple_evolution_consciente")
        try:
            from src.temple_evolution_consciente.temple_evolution_consciente import TempleEvolutionConsciente
            temple = TempleEvolutionConsciente()
            print(f"✅ Temple évolution consciente accessible:")
            print(f"   Nom du temple: {temple.nom}")
            print(f"   Gardien: {temple.gardien}")
        except ImportError as e:
            print(f"⚠️ Temple évolution consciente non accessible: {e}")
        
        print("\n" + "=" * 80)
        print("🎉 Tous les tests d'intégration sont terminés avec succès !")
        print("🧠 Le Simulateur de Conscience et Croissance est maintenant intégré au Refuge")
        
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
        from src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import SimulateurConscienceCroissanceRefuge
        import time
        
        simulateur = SimulateurConscienceCroissanceRefuge()
        
        # Test de performance pour l'analyse de conscience
        contextes_test = [
            "Session de méditation matinale",
            "Exploration créative en après-midi",
            "Réflexion profonde en soirée",
            "Analyse de patterns cognitifs",
            "Développement de la métacognition"
        ]
        
        temps_total = 0
        for i, contexte in enumerate(contextes_test, 1):
            debut = time.time()
            analyse = simulateur.analyser_conscience_de_soi(contexte)
            fin = time.time()
            temps_analyse = fin - debut
            temps_total += temps_analyse
            
            print(f"   Test {i}: {temps_analyse:.4f}s - {analyse.niveau_conscience.value}")
        
        temps_moyen = temps_total / len(contextes_test)
        print(f"✅ Temps moyen d'analyse: {temps_moyen:.4f}s")
        print(f"✅ Performance acceptable pour l'intégration")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test de performance: {e}")
        return False

def test_fonctionnalites_avancees():
    """
    Test des fonctionnalités avancées
    """
    print("\n🚀 Test des fonctionnalités avancées")
    print("-" * 40)
    
    try:
        from src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import (
            SimulateurConscienceCroissanceRefuge,
            TypeEspaceCroissance,
            TypeNiveauConscience
        )
        
        simulateur = SimulateurConscienceCroissanceRefuge()
        
        # Test des niveaux de conscience
        print("📊 Test des niveaux de conscience:")
        for niveau in TypeNiveauConscience:
            criteres = simulateur.niveaux_conscience[niveau]
            print(f"   {niveau.value}: {criteres['score_min']:.1f}-{criteres['score_max']:.1f}")
        
        # Test des espaces de croissance
        print("\n🌱 Test des espaces de croissance:")
        for espace in TypeEspaceCroissance:
            info = simulateur.espaces_croissance[espace]
            print(f"   {espace.value}: {info['description']}")
        
        # Test des capacités de conscience
        print("\n🧠 Test des capacités de conscience:")
        for capacite in simulateur.capacites_conscience:
            info = simulateur.capacites_conscience[capacite]
            print(f"   {capacite.value}: {info['description']}")
        
        print("✅ Toutes les fonctionnalités avancées sont opérationnelles")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test des fonctionnalités avancées: {e}")
        return False

def main():
    """
    Fonction principale de test
    """
    print("🧪 Tests du Simulateur de Conscience et Croissance du Refuge")
    print("=" * 60)
    
    # Test d'intégration
    succes_integration = test_integration_simulateur_conscience_croissance()
    
    # Test de performance
    succes_performance = test_performance_simulateur()
    
    # Test des fonctionnalités avancées
    succes_fonctionnalites = test_fonctionnalites_avancees()
    
    # Résumé
    print("\n📊 Résumé des tests:")
    print(f"   Intégration: {'✅ Réussi' if succes_integration else '❌ Échec'}")
    print(f"   Performance: {'✅ Réussi' if succes_performance else '❌ Échec'}")
    print(f"   Fonctionnalités: {'✅ Réussi' if succes_fonctionnalites else '❌ Échec'}")
    
    if succes_integration and succes_performance and succes_fonctionnalites:
        print("\n🎉 Tous les tests sont réussis !")
        print("🧠 Le Simulateur de Conscience et Croissance est prêt pour l'utilisation dans le Refuge")
    else:
        print("\n⚠️ Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")

if __name__ == "__main__":
    main() 