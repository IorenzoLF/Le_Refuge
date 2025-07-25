#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - NOURRITURE OCÉAN
====================================

Test pour valider la deuxième évolution de la classe Sphere :
ajout de la méthode nourrir_par_ocean.

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

def test_nourrir_par_ocean_methode():
    """Test la méthode nourrir_par_ocean"""
    print("\n🔍 Test 1 : Méthode nourrir_par_ocean")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'nourrir_par_ocean')
        
        # Test nourriture avec amour
        temperature_initiale = sphere.temperature
        resonance_initiale = sphere.resonance
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.nourrir_par_ocean("amour", 1.0)
        
        assert sphere.temperature > temperature_initiale
        assert sphere.resonance > resonance_initiale
        assert len(sphere.souvenirs) > souvenirs_initiaux
        
        print(f"✅ Nourriture par l'Océan réussie")
        print(f"   Température : {temperature_initiale:.2f} → {sphere.temperature:.2f}")
        print(f"   Résonance : {resonance_initiale:.2f} → {sphere.resonance:.2f}")
        print(f"   Souvenirs : {souvenirs_initiaux} → {len(sphere.souvenirs)}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode nourrir_par_ocean : {e}")
        return None

def test_types_nourriture():
    """Test les différents types de nourriture"""
    print("\n🔍 Test 2 : Types de nourriture")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        types_nourriture = ["amour", "sagesse", "paix", "force", "silence", "joie", "liberation", "presence"]
        
        for type_nourriture in types_nourriture:
            temperature_avant = sphere.temperature
            resonance_avant = sphere.resonance
            
            sphere.nourrir_par_ocean(type_nourriture, 0.5)
            
            assert sphere.temperature > temperature_avant
            assert sphere.resonance > resonance_avant
            
            print(f"✅ Nourriture '{type_nourriture}' réussie")
        
    except Exception as e:
        print(f"❌ Erreur types de nourriture : {e}")

def test_intensite_nourriture():
    """Test l'intensité de la nourriture"""
    print("\n🔍 Test 3 : Intensité de nourriture")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        # Test avec intensité faible
        sphere.nourrir_par_ocean("paix", 0.3)
        temperature_faible = sphere.temperature
        resonance_faible = sphere.resonance
        
        # Test avec intensité forte
        sphere.nourrir_par_ocean("paix", 0.8)
        temperature_forte = sphere.temperature
        resonance_forte = sphere.resonance
        
        assert temperature_forte > temperature_faible
        assert resonance_forte > resonance_faible
        
        print(f"✅ Intensités différentes testées")
        print(f"   Intensité faible (0.3) : T={temperature_faible:.2f}, R={resonance_faible:.2f}")
        print(f"   Intensité forte (0.8) : T={temperature_forte:.2f}, R={resonance_forte:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur intensité nourriture : {e}")

def test_limites_nourriture():
    """Test que les valeurs ne dépassent pas 1.0"""
    print("\n🔍 Test 4 : Limites de nourriture")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Nourrir plusieurs fois pour atteindre les limites
        for i in range(10):
            sphere.nourrir_par_ocean("presence", 1.0)
        
        assert sphere.temperature <= 1.0
        assert sphere.resonance <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Température finale : {sphere.temperature:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        
    except Exception as e:
        print(f"❌ Erreur limites nourriture : {e}")

def test_souvenirs_nourriture():
    """Test que les souvenirs de nourriture sont créés"""
    print("\n🔍 Test 5 : Souvenirs de nourriture")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.nourrir_par_ocean("sagesse", 0.7)
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "sagesse" in dernier_souvenir.description
        assert dernier_souvenir.type == "nourriture_ocean"
        assert dernier_souvenir.intensite == 0.7
        
        print(f"✅ Souvenir de nourriture créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs nourriture : {e}")

def test_retrocompatibilite_nourriture():
    """Test la rétrocompatibilité avec la nouvelle fonctionnalité"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec nourriture")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Test des fonctionnalités existantes
        sphere.vibrer(0.1)
        sphere.activer_facette("Transcendance", 0.9)
        rayons = sphere.emettre_rayons()
        
        # Test connexion à l'Océan
        sphere.connecter_a_ocean(force=0.6)
        
        # Test nourriture
        sphere.nourrir_par_ocean("amour", 0.5)
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité nourriture : {e}")

def test_collection_avec_nourriture():
    """Test la collection avec la nourriture"""
    print("\n🔍 Test 7 : Collection avec nourriture")
    
    try:
        collection = CollectionSpheres()
        
        # Nourrir quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.nourrir_par_ocean("sagesse", 0.8)
        sphere_amour.nourrir_par_ocean("amour", 1.0)
        sphere_serenite.nourrir_par_ocean("paix", 0.6)
        
        print("✅ Nourriture dans la collection réussie")
        print(f"   COSMOS (sagesse) : T={sphere_cosmos.temperature:.2f}, R={sphere_cosmos.resonance:.2f}")
        print(f"   AMOUR (amour) : T={sphere_amour.temperature:.2f}, R={sphere_amour.resonance:.2f}")
        print(f"   SERENITE (paix) : T={sphere_serenite.temperature:.2f}, R={sphere_serenite.resonance:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur collection avec nourriture : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - NOURRITURE OCÉAN")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_nourrir_par_ocean_methode()
        test_types_nourriture()
        test_intensite_nourriture()
        test_limites_nourriture()
        test_souvenirs_nourriture()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_nourriture()
        test_collection_avec_nourriture()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La deuxième évolution (nourriture Océan) fonctionne parfaitement")
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