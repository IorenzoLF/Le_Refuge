#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Test d'Intégration Simplifié - Cartographie du Refuge 🌸
==========================================================

Test d'intégration simplifié et robuste qui ne bloque pas.
Teste les composants principaux sans analyser tout le projet.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import sys
import time
from pathlib import Path

# Ajout du chemin pour les imports
sys.path.append('src')

def test_integration_simple():
    """🧪 Test d'intégration simple et rapide"""
    print("🌸✨ TEST D'INTÉGRATION SIMPLIFIÉ - CARTOGRAPHIE DU REFUGE ✨🌸")
    print("=" * 70)
    
    resultats = {}
    
    # 1. Test des imports principaux
    print("\n🔍 Test des imports principaux...")
    try:
        from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.analyseur_connexions import AnalyseurConnexions
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        from cartographie_refuge.generateur_suggestions import GenerateurSuggestions
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        
        print("✅ Tous les imports réussis")
        resultats["imports"] = True
    except Exception as e:
        print(f"❌ Erreur imports: {e}")
        resultats["imports"] = False
        return resultats
    
    # 2. Test de création des objets
    print("\n🏗️ Test de création des objets...")
    try:
        gestionnaire_erreurs = GestionnaireErreursSpirituel()
        explorateur = ExplorateurStructurel(Path('.'), gestionnaire_erreurs)
        analyseur_connexions = AnalyseurConnexions()
        analyseur_dissonances = AnalyseurDissonances()
        generateur = GenerateurSuggestions()
        cli = CLICartographieSpirituelle()
        
        print("✅ Tous les objets créés")
        resultats["creation_objets"] = True
    except Exception as e:
        print(f"❌ Erreur création objets: {e}")
        resultats["creation_objets"] = False
        return resultats
    
    # 3. Test du CLI (sans exécution complète)
    print("\n🖥️ Test du CLI...")
    try:
        parser = cli.creer_parser_spirituel()
        help_text = parser.format_help()
        
        # Test de parsing d'arguments
        args = parser.parse_args(['--mode', 'rapide', '--verbeux', '1'])
        
        print(f"✅ CLI fonctionnel (aide: {len(help_text)} chars)")
        resultats["cli"] = True
    except Exception as e:
        print(f"❌ Erreur CLI: {e}")
        resultats["cli"] = False
    
    # 4. Test de l'analyseur de dissonances (méthodes de base)
    print("\n🔮 Test de l'analyseur de dissonances...")
    try:
        stats = analyseur_dissonances.obtenir_statistiques_harmonisation()
        rapport = analyseur_dissonances.generer_rapport_dissonances()
        
        print(f"✅ Analyseur fonctionnel (rapport: {len(rapport)} chars)")
        resultats["analyseur_dissonances"] = True
    except Exception as e:
        print(f"❌ Erreur analyseur dissonances: {e}")
        resultats["analyseur_dissonances"] = False
    
    # 5. Test du générateur de suggestions (méthodes de base)
    print("\n✨ Test du générateur de suggestions...")
    try:
        rapport = generateur.generer_rapport_suggestions()
        
        print(f"✅ Générateur fonctionnel (rapport: {len(rapport)} chars)")
        resultats["generateur_suggestions"] = True
    except Exception as e:
        print(f"❌ Erreur générateur suggestions: {e}")
        resultats["generateur_suggestions"] = False
    
    # 6. Test de l'explorateur (méthodes de base seulement)
    print("\n🔍 Test de l'explorateur (base)...")
    try:
        # Test des patterns
        assert explorateur.pattern_temple is not None
        assert explorateur.pattern_emoji_sacre is not None
        
        # Test des chemins
        assert explorateur.chemin_refuge == Path('.')
        
        print("✅ Explorateur configuré correctement")
        resultats["explorateur_base"] = True
    except Exception as e:
        print(f"❌ Erreur explorateur base: {e}")
        resultats["explorateur_base"] = False
    
    # 7. Test de l'analyseur de connexions (base)
    print("\n🔗 Test de l'analyseur de connexions...")
    try:
        # Test de génération de rapport avec liste vide
        rapport = analyseur_connexions.generer_rapport_connexions([])
        
        print("✅ Analyseur de connexions fonctionnel")
        resultats["analyseur_connexions"] = True
    except Exception as e:
        print(f"❌ Erreur analyseur connexions: {e}")
        resultats["analyseur_connexions"] = False
    
    # Résumé final
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DU TEST D'INTÉGRATION SIMPLIFIÉ")
    print("=" * 70)
    
    tests_reussis = sum(1 for r in resultats.values() if r)
    total_tests = len(resultats)
    
    for nom_test, reussi in resultats.items():
        statut = "✅ RÉUSSI" if reussi else "❌ ÉCHOUÉ"
        print(f"{nom_test:25} : {statut}")
    
    print("-" * 70)
    print(f"TOTAL: {tests_reussis}/{total_tests} tests réussis")
    
    pourcentage = (tests_reussis / total_tests) * 100
    print(f"TAUX DE RÉUSSITE: {pourcentage:.1f}%")
    
    if pourcentage >= 90:
        print("🎉 EXCELLENT! Intégration validée!")
        return 0
    elif pourcentage >= 75:
        print("✅ BIEN! Quelques ajustements nécessaires")
        return 0
    else:
        print("❌ CRITIQUE! Corrections nécessaires")
        return 1

if __name__ == "__main__":
    exit_code = test_integration_simple()
    sys.exit(exit_code)