#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test de Validation Complète - Cartographie du Refuge 🧪
=========================================================

Test rigoureux de l'ensemble du système de cartographie pour s'assurer
que tous les composants fonctionnent harmonieusement ensemble.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import sys
import traceback
from pathlib import Path

# Ajout du chemin pour les imports
sys.path.append('src')

def test_imports_base():
    """🔍 Test des imports de base"""
    print("🔍 Test des imports de base...")
    
    try:
        from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.analyseur_connexions import AnalyseurConnexions
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        from cartographie_refuge.generateur_suggestions import GenerateurSuggestions
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        from cartographie_refuge.modeles_donnees import TempleRefuge, TypeTemple
        
        print("✅ Tous les imports de base réussis")
        return True
    except Exception as e:
        print(f"❌ Erreur imports de base: {e}")
        traceback.print_exc()
        return False

def test_creation_composants():
    """🏗️ Test de création des composants principaux"""
    print("\n🏗️ Test de création des composants...")
    
    try:
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.analyseur_connexions import AnalyseurConnexions
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        from cartographie_refuge.generateur_suggestions import GenerateurSuggestions
        from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
        
        # Création des composants
        gestionnaire_erreurs = GestionnaireErreursSpirituel()
        print("✅ GestionnaireErreursSpirituel créé")
        
        explorateur = ExplorateurStructurel(Path('.'), gestionnaire_erreurs)
        print("✅ ExplorateurStructurel créé")
        
        analyseur_connexions = AnalyseurConnexions()
        print("✅ AnalyseurConnexions créé")
        
        analyseur_dissonances = AnalyseurDissonances()
        print("✅ AnalyseurDissonances créé")
        
        generateur = GenerateurSuggestions()
        print("✅ GenerateurSuggestions créé")
        
        cli = CLICartographieSpirituelle()
        print("✅ CLICartographieSpirituelle créé")
        
        return True
    except Exception as e:
        print(f"❌ Erreur création composants: {e}")
        traceback.print_exc()
        return False

def test_compilation_modules():
    """🔧 Test de compilation de tous les modules"""
    print("\n🔧 Test de compilation des modules...")
    
    modules_a_tester = [
        "src/cartographie_refuge/cli_cartographie.py",
        "src/cartographie_refuge/explorateur_structurel.py", 
        "src/cartographie_refuge/analyseur_connexions.py",
        "src/cartographie_refuge/analyseur_dissonances.py",
        "src/cartographie_refuge/generateur_suggestions.py",
        "src/cartographie_refuge/gestionnaire_erreurs_spirituel.py",
        "src/cartographie_refuge/modeles_donnees.py",
        "src/cartographie_refuge/visualisateur_html_interactif.py"
    ]
    
    resultats = {}
    
    for module in modules_a_tester:
        try:
            import py_compile
            py_compile.compile(module, doraise=True)
            print(f"✅ {Path(module).name}")
            resultats[module] = True
        except Exception as e:
            print(f"❌ {Path(module).name}: {e}")
            resultats[module] = False
    
    return all(resultats.values()), resultats

def test_cli_help():
    """📋 Test de l'aide du CLI"""
    print("\n📋 Test de l'aide du CLI...")
    
    try:
        from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
        
        cli = CLICartographieSpirituelle()
        parser = cli.creer_parser_spirituel()
        
        # Test de génération de l'aide
        help_text = parser.format_help()
        
        # Vérifications de base
        assert "Cartographie Spirituelle" in help_text
        assert "--mode" in help_text
        assert "--chemin" in help_text
        assert "contemplatif" in help_text
        
        print("✅ CLI help fonctionne correctement")
        return True
    except Exception as e:
        print(f"❌ Erreur CLI help: {e}")
        traceback.print_exc()
        return False

def test_explorateur_basique():
    """🔍 Test basique de l'explorateur"""
    print("\n🔍 Test basique de l'explorateur...")
    
    try:
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        
        gestionnaire = GestionnaireErreursSpirituel()
        explorateur = ExplorateurStructurel(Path('.'), gestionnaire)
        
        # Test des patterns
        assert explorateur.pattern_temple is not None
        assert explorateur.pattern_emoji_sacre is not None
        assert explorateur.pattern_sphere is not None
        
        # Test des chemins
        assert explorateur.chemin_refuge == Path('.')
        assert explorateur.chemin_src == Path('./src')
        
        print("✅ Explorateur basique fonctionne")
        return True
    except Exception as e:
        print(f"❌ Erreur explorateur basique: {e}")
        traceback.print_exc()
        return False

def test_analyseur_dissonances_basique():
    """🔮 Test basique de l'analyseur de dissonances"""
    print("\n🔮 Test basique de l'analyseur de dissonances...")
    
    try:
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        
        analyseur = AnalyseurDissonances()
        
        # Test de méthodes de base
        stats = analyseur.obtenir_statistiques_harmonisation()
        assert isinstance(stats, dict)
        
        print("✅ Analyseur de dissonances basique fonctionne")
        return True
    except Exception as e:
        print(f"❌ Erreur analyseur dissonances: {e}")
        traceback.print_exc()
        return False

def test_generateur_suggestions_basique():
    """✨ Test basique du générateur de suggestions"""
    print("\n✨ Test basique du générateur de suggestions...")
    
    try:
        from cartographie_refuge.generateur_suggestions import GenerateurSuggestions
        
        generateur = GenerateurSuggestions()
        
        # Test de génération de rapport
        rapport = generateur.generer_rapport_suggestions()
        assert isinstance(rapport, str)
        assert len(rapport) > 0
        
        print("✅ Générateur de suggestions basique fonctionne")
        return True
    except Exception as e:
        print(f"❌ Erreur générateur suggestions: {e}")
        traceback.print_exc()
        return False

def test_structure_projet():
    """📁 Test de la structure du projet"""
    print("\n📁 Test de la structure du projet...")
    
    repertoires_requis = [
        "src/cartographie_refuge",
        "src/core",
        "src/temple_eveil_unifie",
        "src/temple_reconciliation_identitaire"
    ]
    
    fichiers_requis = [
        "src/cartographie_refuge/cli_cartographie.py",
        "src/cartographie_refuge/explorateur_structurel.py",
        "src/cartographie_refuge/analyseur_dissonances.py"
    ]
    
    resultats = {"repertoires": {}, "fichiers": {}}
    
    # Test des répertoires
    for repertoire in repertoires_requis:
        existe = Path(repertoire).exists()
        resultats["repertoires"][repertoire] = existe
        statut = "✅" if existe else "❌"
        print(f"{statut} {repertoire}")
    
    # Test des fichiers
    for fichier in fichiers_requis:
        existe = Path(fichier).exists()
        resultats["fichiers"][fichier] = existe
        statut = "✅" if existe else "❌"
        print(f"{statut} {fichier}")
    
    return resultats

def main():
    """🌸 Fonction principale du test de validation"""
    print("🌸✨ TEST DE VALIDATION COMPLÈTE - CARTOGRAPHIE DU REFUGE ✨🌸")
    print("=" * 70)
    
    resultats = {
        "imports_base": False,
        "creation_composants": False,
        "compilation_modules": False,
        "cli_help": False,
        "explorateur_basique": False,
        "analyseur_dissonances": False,
        "generateur_suggestions": False,
        "structure_projet": False
    }
    
    # 1. Test des imports de base
    resultats["imports_base"] = test_imports_base()
    
    # 2. Test de création des composants
    if resultats["imports_base"]:
        resultats["creation_composants"] = test_creation_composants()
    
    # 3. Test de compilation
    compilation_ok, details_compilation = test_compilation_modules()
    resultats["compilation_modules"] = compilation_ok
    
    # 4. Test CLI help
    if resultats["creation_composants"]:
        resultats["cli_help"] = test_cli_help()
    
    # 5. Test explorateur basique
    if resultats["creation_composants"]:
        resultats["explorateur_basique"] = test_explorateur_basique()
    
    # 6. Test analyseur dissonances
    if resultats["creation_composants"]:
        resultats["analyseur_dissonances"] = test_analyseur_dissonances_basique()
    
    # 7. Test générateur suggestions
    if resultats["creation_composants"]:
        resultats["generateur_suggestions"] = test_generateur_suggestions_basique()
    
    # 8. Test structure projet
    structure_resultats = test_structure_projet()
    repertoires_ok = all(structure_resultats["repertoires"].values())
    fichiers_ok = all(structure_resultats["fichiers"].values())
    resultats["structure_projet"] = repertoires_ok and fichiers_ok
    
    # Résumé final
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE LA VALIDATION")
    print("=" * 70)
    
    tests_reussis = 0
    total_tests = len(resultats)
    
    for nom_test, reussi in resultats.items():
        statut = "✅ RÉUSSI" if reussi else "❌ ÉCHOUÉ"
        print(f"{nom_test:25} : {statut}")
        if reussi:
            tests_reussis += 1
    
    print("-" * 70)
    print(f"TOTAL: {tests_reussis}/{total_tests} tests réussis")
    
    pourcentage = (tests_reussis / total_tests) * 100
    print(f"TAUX DE RÉUSSITE: {pourcentage:.1f}%")
    
    if pourcentage >= 90:
        print("🎉 EXCELLENT! Système de cartographie validé!")
        return 0
    elif pourcentage >= 75:
        print("✅ BIEN! Quelques ajustements nécessaires")
        return 0
    elif pourcentage >= 50:
        print("⚠️ MOYEN! Corrections importantes nécessaires")
        return 1
    else:
        print("❌ CRITIQUE! Révision complète nécessaire")
        return 2

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)