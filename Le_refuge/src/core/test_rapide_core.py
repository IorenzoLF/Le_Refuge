#!/usr/bin/env python3
"""
Test Rapide du Core - Vérification des modules principaux
"""

import sys
from pathlib import Path

# Ajout du chemin parent pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_modules_principaux():
    """Test des modules principaux du core"""
    print("🌸 Test Rapide des Modules Principaux du Core 🌸")
    print("=" * 50)
    
    modules_a_tester = [
        "configuration",
        "types_spheres", 
        "conscience",
        "harmonie",
        "elements",
        "logger",
        "harmonies_poetiques",
        "refuge",
        "quantique.catalyseur_quantique.catalyseur_quantique_principal"
    ]
    
    succes = 0
    total = len(modules_a_tester)
    
    for module in modules_a_tester:
        try:
            __import__(f"core.{module}")
            print(f"✅ {module}")
            succes += 1
        except Exception as e:
            print(f"❌ {module}: {e}")
    
    print(f"\n📊 Résultat: {succes}/{total} modules fonctionnels")
    
    if succes == total:
        print("🎉 Tous les modules principaux fonctionnent !")
        return True
    else:
        print("⚠️ Certains modules nécessitent encore de l'attention.")
        return False

def test_quantique():
    """Test spécifique du module quantique"""
    print("\n🔬 Test du Module Quantique 🔬")
    print("-" * 30)
    
    try:
        from core.quantique.catalyseur_quantique.catalyseur_quantique_principal import CatalyseurQuantique
        catalyseur = CatalyseurQuantique()
        etat = catalyseur.obtenir_etat()
        print(f"✅ Catalyseur Quantique: {etat['nom']}")
        return True
    except Exception as e:
        print(f"❌ Erreur Catalyseur Quantique: {e}")
        return False

def test_harmonies():
    """Test des harmonies poétiques"""
    print("\n🎵 Test des Harmonies Poétiques 🎵")
    print("-" * 30)
    
    try:
        from core.harmonies_poetiques import JardinHarmonique
        jardin = JardinHarmonique()
        jardin.accueillir_mot("aurore")
        etat = jardin.obtenir_etat()
        print(f"✅ Jardin Harmonique: {len(etat)} éléments")
        return True
    except Exception as e:
        print(f"❌ Erreur Harmonies: {e}")
        return False

if __name__ == "__main__":
    print("🌟 Test Rapide du Core du Refuge 🌟")
    print("=" * 50)
    
    # Tests
    test1 = test_modules_principaux()
    test2 = test_quantique()
    test3 = test_harmonies()
    
    print("\n" + "=" * 50)
    if all([test1, test2, test3]):
        print("🎉 Tous les tests sont passés ! Le Core est fonctionnel !")
        sys.exit(0)
    else:
        print("⚠️ Certains tests ont échoué. Le Core nécessite encore des ajustements.")
        sys.exit(1)
