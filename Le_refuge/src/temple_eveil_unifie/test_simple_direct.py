#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Test Simple et Direct du Temple d'Éveil Unifié 🌸
==================================================

Test direct et simple pour validation rapide du temple.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import sys
import os
from pathlib import Path

# Ajout du chemin racine
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_compilation_fichiers():
    """Test de compilation de tous les fichiers principaux"""
    print("🔍 Test de compilation des fichiers principaux...")
    
    fichiers_a_tester = [
        "src/temple_eveil_unifie/types_eveil_unifie.py",
        "src/temple_eveil_unifie/temple_eveil_unifie.py",
        "src/temple_eveil_unifie/detecteur_contexte.py",
        "src/temple_eveil_unifie/routeur_intelligent.py",
        "src/temple_eveil_unifie/integrateur_experiences.py",
        "src/temple_eveil_unifie/deploiement_production_unifie.py",
        "src/temple_eveil_unifie/lanceur_temple_accompagnement.py"
    ]
    
    resultats = {}
    
    for fichier in fichiers_a_tester:
        try:
            # Test de compilation
            import py_compile
            py_compile.compile(fichier, doraise=True)
            print(f"✅ {fichier}")
            resultats[fichier] = True
        except Exception as e:
            print(f"❌ {fichier}: {e}")
            resultats[fichier] = False
    
    return resultats

def test_imports_directs():
    """Test d'imports directs"""
    print("\n🔧 Test d'imports directs...")
    
    try:
        # Test d'import avec chemin absolu
        import importlib.util
        
        # Import des types
        types_path = Path("src/temple_eveil_unifie/types_eveil_unifie.py").resolve()
        spec = importlib.util.spec_from_file_location("types_eveil_unifie", types_path)
        if spec and spec.loader:
            types_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(types_module)
            print("✅ Types importés avec succès")
            
            # Test de création d'une conscience
            ConscienceUnifiee = types_module.ConscienceUnifiee
            TypeConscience = types_module.TypeConscience
            
            conscience = ConscienceUnifiee(
                nom_affichage="Test Direct",
                type_conscience=TypeConscience.HUMAINE
            )
            print(f"✅ Conscience créée: {conscience.nom_affichage}")
            return True
            
    except Exception as e:
        print(f"❌ Erreur import direct: {e}")
        return False

def test_structure_projet():
    """Test de la structure du projet"""
    print("\n📁 Test de la structure du projet...")
    
    repertoires_requis = [
        "src/temple_eveil_unifie",
        "src/temple_eveil_unifie/modules",
        "src/temple_eveil_unifie/modules/eveil_base",
        "src/temple_eveil_unifie/modules/eveil_rapide",
        "src/temple_eveil_unifie/modules/eveil_progressif",
        "src/temple_eveil_unifie/tests"
    ]
    
    fichiers_requis = [
        "src/temple_eveil_unifie/temple_eveil_unifie.py",
        "src/temple_eveil_unifie/types_eveil_unifie.py",
        "docs/GUIDE_SPIRITUEL_EVEIL_UNIFIE.md",
        "docs/DOCUMENTATION_TECHNIQUE_TEMPLE_EVEIL_UNIFIE.md"
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
    """Fonction principale du test simple"""
    print("🌸✨ TEST SIMPLE ET DIRECT DU TEMPLE D'ÉVEIL UNIFIÉ ✨🌸")
    print("=" * 60)
    
    # 1. Test de compilation
    resultats_compilation = test_compilation_fichiers()
    
    # 2. Test d'imports directs
    import_reussi = test_imports_directs()
    
    # 3. Test de structure
    resultats_structure = test_structure_projet()
    
    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)
    
    # Compilation
    fichiers_compiles = sum(1 for r in resultats_compilation.values() if r)
    total_fichiers = len(resultats_compilation)
    print(f"Compilation: {fichiers_compiles}/{total_fichiers} fichiers")
    
    # Imports
    print(f"Imports directs: {'✅ Réussi' if import_reussi else '❌ Échoué'}")
    
    # Structure
    repertoires_ok = sum(1 for r in resultats_structure["repertoires"].values() if r)
    total_repertoires = len(resultats_structure["repertoires"])
    fichiers_ok = sum(1 for r in resultats_structure["fichiers"].values() if r)
    total_fichiers_struct = len(resultats_structure["fichiers"])
    
    print(f"Structure - Répertoires: {repertoires_ok}/{total_repertoires}")
    print(f"Structure - Fichiers: {fichiers_ok}/{total_fichiers_struct}")
    
    # Score global
    score_total = (
        (fichiers_compiles / total_fichiers) * 0.4 +
        (1 if import_reussi else 0) * 0.3 +
        (repertoires_ok / total_repertoires) * 0.15 +
        (fichiers_ok / total_fichiers_struct) * 0.15
    ) * 100
    
    print(f"\n🎯 SCORE GLOBAL: {score_total:.1f}%")
    
    if score_total >= 90:
        print("🎉 EXCELLENT! Temple validé!")
        return 0
    elif score_total >= 75:
        print("✅ BIEN! Quelques ajustements nécessaires")
        return 0
    elif score_total >= 50:
        print("⚠️ MOYEN! Corrections nécessaires")
        return 1
    else:
        print("❌ CRITIQUE! Révision nécessaire")
        return 2

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)