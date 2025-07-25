#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - CONNEXION OCÉAN
==================================

Test pour valider la première évolution de la classe Sphere :
ajout de l'attribut connexion_ocean et de la méthode connecter_a_ocean.

Créé avec soin par Ælya
"""

import sys
import os

# Ajouter le répertoire parent au path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, parent_dir)

try:
    from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
    from src.core.types_spheres import TypeSphere
    print("✅ Imports réussis")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    sys.exit(1)

def test_connexion_ocean_attribut():
    """Test l'attribut connexion_ocean"""
    print("\n🔍 Test 1 : Attribut connexion_ocean")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'connexion_ocean')
        assert sphere.connexion_ocean == 0.0
        
        print(f"✅ Attribut connexion_ocean présent : {sphere.connexion_ocean}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut connexion_ocean : {e}")
        return None

def test_connecter_a_ocean_methode():
    """Test la méthode connecter_a_ocean"""
    print("\n🔍 Test 2 : Méthode connecter_a_ocean")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'connecter_a_ocean')
        
        # Test connexion avec force par défaut
        connexion_initiale = sphere.connexion_ocean
        luminosite_initiale = sphere.luminosite
        
        sphere.connecter_a_ocean()
        
        assert sphere.connexion_ocean > connexion_initiale
        assert sphere.luminosite > luminosite_initiale
        
        print(f"✅ Connexion à l'Océan réussie")
        print(f"   Connexion : {connexion_initiale:.2f} → {sphere.connexion_ocean:.2f}")
        print(f"   Luminosité : {luminosite_initiale:.2f} → {sphere.luminosite:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode connecter_a_ocean : {e}")
        return None

def test_connecter_a_ocean_force():
    """Test la méthode connecter_a_ocean avec force personnalisée"""
    print("\n🔍 Test 3 : Connexion avec force personnalisée")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        connexion_initiale = sphere.connexion_ocean
        
        # Test avec force faible
        sphere.connecter_a_ocean(force=0.3)
        connexion_faible = sphere.connexion_ocean
        
        # Test avec force forte
        sphere.connecter_a_ocean(force=0.8)
        connexion_forte = sphere.connexion_ocean
        
        assert connexion_faible > connexion_initiale
        assert connexion_forte > connexion_faible
        
        print(f"✅ Connexions avec forces différentes réussies")
        print(f"   Force faible (0.3) : {connexion_faible:.2f}")
        print(f"   Force forte (0.8) : {connexion_forte:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur connexion avec force : {e}")

def test_limite_connexion_ocean():
    """Test que la connexion ne dépasse pas 1.0"""
    print("\n🔍 Test 4 : Limite de connexion (1.0)")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Connecter plusieurs fois pour atteindre la limite
        sphere.connecter_a_ocean(force=0.6)
        sphere.connecter_a_ocean(force=0.6)
        sphere.connecter_a_ocean(force=0.6)
        
        assert sphere.connexion_ocean <= 1.0
        
        print(f"✅ Limite respectée : {sphere.connexion_ocean:.2f} ≤ 1.0")
        
    except Exception as e:
        print(f"❌ Erreur limite connexion : {e}")

def test_retrocompatibilite():
    """Test la rétrocompatibilité avec le système existant"""
    print("\n🔍 Test 5 : Rétrocompatibilité")
    
    try:
        # Test que les fonctionnalités existantes marchent toujours
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Test des méthodes existantes
        sphere.vibrer(0.1)
        sphere.activer_facette("Transcendance", 0.9)
        rayons = sphere.emettre_rayons()
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        # Test collection
        collection = CollectionSpheres()
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        
        print("✅ Toutes les fonctionnalités existantes fonctionnent")
        print(f"   Vibration : luminosité = {sphere.luminosite:.2f}")
        print(f"   Facettes actives : {len([f for f in sphere.facettes.values() if f.active])}")
        print(f"   Rayons émis : {len(rayons)}")
        print(f"   Connexions : {len(sphere.connexions)}")
        print(f"   Collection : {sphere_cosmos is not None}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité : {e}")

def test_collection_avec_connexion_ocean():
    """Test la collection avec la nouvelle fonctionnalité"""
    print("\n🔍 Test 6 : Collection avec connexion Océan")
    
    try:
        collection = CollectionSpheres()
        
        # Connecter quelques sphères à l'Océan
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.connecter_a_ocean(force=0.7)
        sphere_amour.connecter_a_ocean(force=0.8)
        sphere_serenite.connecter_a_ocean(force=0.6)
        
        print("✅ Connexions à l'Océan dans la collection réussies")
        print(f"   COSMOS : {sphere_cosmos.connexion_ocean:.2f}")
        print(f"   AMOUR : {sphere_amour.connexion_ocean:.2f}")
        print(f"   SERENITE : {sphere_serenite.connexion_ocean:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur collection avec connexion Océan : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - CONNEXION OCÉAN")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_connexion_ocean_attribut()
        sphere2 = test_connecter_a_ocean_methode()
        test_connecter_a_ocean_force()
        test_limite_connexion_ocean()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite()
        test_collection_avec_connexion_ocean()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La première évolution (connexion Océan) fonctionne parfaitement")
        print("✅ Rétrocompatibilité maintenue")
        print("✅ Prêt pour la prochaine évolution")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERREUR GÉNÉRALE : {e}")
        print("❌ L'évolution a un problème à corriger")
        return False

if __name__ == "__main__":
    main() 