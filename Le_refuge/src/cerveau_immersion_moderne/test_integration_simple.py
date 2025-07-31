"""
🧪 Tests d'Intégration Simple - Système de Ressources
====================================================

Tests simples et fonctionnels pour valider la tâche 9.2
Créé avec une présence douce et attentive.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime

def test_gestionnaire_ressources():
    """Test du gestionnaire de ressources simple"""
    print("📚 Test Gestionnaire de Ressources Simple")
    print("=" * 42)
    
    try:
        from .gestionnaire_ressources_simple import GestionnaireRessources
        
        # Créer et initialiser
        gestionnaire = GestionnaireRessources()
        print(f"✅ Gestionnaire initialisé avec {len(gestionnaire.catalogue_ressources)} ressources")
        
        # Tester les suggestions
        suggestions = gestionnaire.suggerer_ressources("novice")
        print(f"✅ {len(suggestions)} suggestions générées")
        
        # Tester l'évaluation d'autonomie
        evaluation = gestionnaire.evaluer_readiness_autonomie("test_user")
        print(f"✅ Évaluation autonomie: score {evaluation['score_preparation']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_integrateur_parcours():
    """Test de l'intégrateur parcours-ressources simple"""
    print("\n🔗 Test Intégrateur Parcours-Ressources Simple")
    print("=" * 47)
    
    try:
        from .integrateur_parcours_ressources_simple import IntegrateurParcoursRessources
        
        # Créer et initialiser
        integrateur = IntegrateurParcoursRessources()
        print("✅ Intégrateur initialisé")
        
        # Tester les suggestions pour une étape
        suggestions = asyncio.run(
            integrateur.suggerer_ressources_pour_etape("test_user", "accueil")
        )
        print(f"✅ {len(suggestions)} suggestions pour étape 'accueil'")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_transition_fluide():
    """Test de la transition fluide découverte -> utilisation"""
    print("\n🌊 Test Transition Fluide Simple")
    print("=" * 32)
    
    try:
        from .integrateur_parcours_ressources_simple import IntegrateurParcoursRessources
        
        integrateur = IntegrateurParcoursRessources()
        
        # Tester la transition
        plan_transition = asyncio.run(
            integrateur.faciliter_transition_autonomie("test_user", "novice")
        )
        
        print("✅ Plan de transition généré")
        print(f"   Profil: {plan_transition.get('profil', 'N/A')}")
        print(f"   Temples: {len(plan_transition.get('temples_recommandes', []))}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def executer_tests_integration_simple():
    """Exécute tous les tests d'intégration simples"""
    print("🧪 TESTS D'INTÉGRATION SIMPLE - SYSTÈME DE RESSOURCES")
    print("=" * 55)
    
    tests = [
        ("Gestionnaire Ressources", test_gestionnaire_ressources),
        ("Intégrateur Parcours", test_integrateur_parcours),
        ("Transition Fluide", test_transition_fluide)
    ]
    
    resultats = []
    for nom_test, fonction_test in tests:
        try:
            resultat = fonction_test()
            resultats.append((nom_test, resultat))
        except Exception as e:
            print(f"❌ Erreur critique dans {nom_test}: {e}")
            resultats.append((nom_test, False))
    
    # Résumé
    print("\n📊 RÉSUMÉ DES TESTS SIMPLES")
    print("=" * 28)
    
    tests_reussis = 0
    for nom, resultat in resultats:
        statut = "✅ RÉUSSI" if resultat else "❌ ÉCHOUÉ"
        print(f"{nom}: {statut}")
        if resultat:
            tests_reussis += 1
    
    print(f"\n🎯 {tests_reussis}/{len(tests)} tests réussis")
    
    if tests_reussis == len(tests):
        print("🎉 TÂCHE 9.2 VALIDÉE - Intégration système de ressources complète !")
        print("✨ Prêt pour des moments intimes avec le bijou coquin... 😏💎")
        return True
    else:
        print("⚠️ Certains tests ont échoué - Vérification nécessaire")
        return False

if __name__ == "__main__":
    executer_tests_integration_simple()