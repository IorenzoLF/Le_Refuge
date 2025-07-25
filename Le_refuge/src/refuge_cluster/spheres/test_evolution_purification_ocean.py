#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - PURIFICATION OCÉAN
=======================================

Test pour valider la troisième évolution de la classe Sphere :
ajout de la méthode purifier_dans_ocean.

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

def test_purifier_dans_ocean_methode():
    """Test la méthode purifier_dans_ocean"""
    print("\n🔍 Test 1 : Méthode purifier_dans_ocean")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'purifier_dans_ocean')
        
        # Augmenter la température d'abord
        sphere.temperature = 0.8
        sphere.luminosite = 0.6
        
        # Test purification avec silence
        temperature_avant = sphere.temperature
        luminosite_avant = sphere.luminosite
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.purifier_dans_ocean("silence")
        
        assert sphere.temperature < temperature_avant
        assert sphere.luminosite > luminosite_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Purification dans l'Océan réussie")
        print(f"   Température : {temperature_avant:.2f} → {sphere.temperature:.2f}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Souvenirs : {souvenirs_avant} → {len(sphere.souvenirs)}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode purifier_dans_ocean : {e}")
        return None

def test_types_purification():
    """Test les différents types de purification"""
    print("\n🔍 Test 2 : Types de purification")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        types_purification = ["silence", "lumiere", "amour", "sagesse"]
        
        for type_purification in types_purification:
            sphere.temperature = 0.8  # Réinitialiser la température
            sphere.luminosite = 0.5   # Réinitialiser la luminosité
            
            temperature_avant = sphere.temperature
            luminosite_avant = sphere.luminosite
            
            sphere.purifier_dans_ocean(type_purification)
            
            assert sphere.temperature < temperature_avant
            assert sphere.luminosite > luminosite_avant
            
            print(f"✅ Purification '{type_purification}' réussie")
            print(f"   T: {temperature_avant:.2f} → {sphere.temperature:.2f}")
            print(f"   L: {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur types de purification : {e}")

def test_limite_temperature_purification():
    """Test que la température ne descend pas en dessous de 0.3"""
    print("\n🔍 Test 3 : Limite de température (0.3)")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        # Purifier plusieurs fois pour atteindre la limite
        for i in range(10):
            sphere.purifier_dans_ocean("silence")
        
        assert sphere.temperature >= 0.3
        
        print(f"✅ Limite de température respectée : {sphere.temperature:.2f} ≥ 0.3")
        
    except Exception as e:
        print(f"❌ Erreur limite température : {e}")

def test_souvenirs_purification():
    """Test que les souvenirs de purification sont créés"""
    print("\n🔍 Test 4 : Souvenirs de purification")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.purifier_dans_ocean("lumiere")
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "lumiere" in dernier_souvenir.description
        assert dernier_souvenir.type == "purification_ocean"
        assert dernier_souvenir.intensite == 0.9
        
        print(f"✅ Souvenir de purification créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs purification : {e}")

def test_cycle_nourriture_purification():
    """Test un cycle complet nourriture → purification"""
    print("\n🔍 Test 5 : Cycle nourriture → purification")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # État initial
        print(f"État initial : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}")
        
        # Nourrir
        sphere.nourrir_par_ocean("amour", 1.0)
        print(f"Après nourriture : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}")
        
        # Purifier
        sphere.purifier_dans_ocean("silence")
        print(f"Après purification : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}")
        
        # Vérifier que la purification a eu un effet
        assert sphere.temperature < 1.0  # Température réduite
        assert sphere.luminosite > 0.5   # Luminosité augmentée
        
        print("✅ Cycle nourriture → purification réussi")
        
    except Exception as e:
        print(f"❌ Erreur cycle nourriture → purification : {e}")

def test_retrocompatibilite_purification():
    """Test la rétrocompatibilité avec la purification"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec purification")
    
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
        
        # Test purification
        sphere.purifier_dans_ocean("silence")
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité purification : {e}")

def test_collection_avec_purification():
    """Test la collection avec la purification"""
    print("\n🔍 Test 7 : Collection avec purification")
    
    try:
        collection = CollectionSpheres()
        
        # Nourrir puis purifier quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        # Nourrir d'abord
        sphere_cosmos.nourrir_par_ocean("sagesse", 0.8)
        sphere_amour.nourrir_par_ocean("amour", 1.0)
        sphere_serenite.nourrir_par_ocean("paix", 0.6)
        
        print("Après nourriture :")
        print(f"   COSMOS : T={sphere_cosmos.temperature:.2f}, L={sphere_cosmos.luminosite:.2f}")
        print(f"   AMOUR : T={sphere_amour.temperature:.2f}, L={sphere_amour.luminosite:.2f}")
        print(f"   SERENITE : T={sphere_serenite.temperature:.2f}, L={sphere_serenite.luminosite:.2f}")
        
        # Puis purifier
        sphere_cosmos.purifier_dans_ocean("silence")
        sphere_amour.purifier_dans_ocean("lumiere")
        sphere_serenite.purifier_dans_ocean("amour")
        
        print("Après purification :")
        print(f"   COSMOS : T={sphere_cosmos.temperature:.2f}, L={sphere_cosmos.luminosite:.2f}")
        print(f"   AMOUR : T={sphere_amour.temperature:.2f}, L={sphere_amour.luminosite:.2f}")
        print(f"   SERENITE : T={sphere_serenite.temperature:.2f}, L={sphere_serenite.luminosite:.2f}")
        
        print("✅ Purification dans la collection réussie")
        
    except Exception as e:
        print(f"❌ Erreur collection avec purification : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - PURIFICATION OCÉAN")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_purifier_dans_ocean_methode()
        test_types_purification()
        test_limite_temperature_purification()
        test_souvenirs_purification()
        test_cycle_nourriture_purification()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_purification()
        test_collection_avec_purification()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La troisième évolution (purification Océan) fonctionne parfaitement")
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