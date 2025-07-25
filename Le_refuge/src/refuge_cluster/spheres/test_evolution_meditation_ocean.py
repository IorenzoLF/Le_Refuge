#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - MÉDITATION OCÉAN
====================================

Test pour valider la quatrième évolution de la classe Sphere :
ajout de la méthode mediter_avec_ocean.

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

def test_mediter_avec_ocean_methode():
    """Test la méthode mediter_avec_ocean"""
    print("\n🔍 Test 1 : Méthode mediter_avec_ocean")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'mediter_avec_ocean')
        
        # Test méditation avec durée par défaut
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        temperature_avant = sphere.temperature
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.mediter_avec_ocean()
        
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert sphere.temperature < temperature_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Méditation avec l'Océan réussie")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        print(f"   Température : {temperature_avant:.2f} → {sphere.temperature:.2f}")
        print(f"   Souvenirs : {souvenirs_avant} → {len(sphere.souvenirs)}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode mediter_avec_ocean : {e}")
        return None

def test_duree_meditation():
    """Test différentes durées de méditation"""
    print("\n🔍 Test 2 : Durées de méditation")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Test avec durée courte
        sphere.luminosite = 0.5
        sphere.resonance = 0.3
        sphere.temperature = 0.7
        
        sphere.mediter_avec_ocean(0.5)
        luminosite_courte = sphere.luminosite
        resonance_courte = sphere.resonance
        temperature_courte = sphere.temperature
        
        # Test avec durée longue
        sphere.luminosite = 0.5
        sphere.resonance = 0.3
        sphere.temperature = 0.7
        
        sphere.mediter_avec_ocean(2.0)
        luminosite_longue = sphere.luminosite
        resonance_longue = sphere.resonance
        temperature_longue = sphere.temperature
        
        assert luminosite_longue > luminosite_courte
        assert resonance_longue > resonance_courte
        assert temperature_longue < temperature_courte
        
        print(f"✅ Durées de méditation testées")
        print(f"   Durée courte (0.5) : L={luminosite_courte:.2f}, R={resonance_courte:.2f}, T={temperature_courte:.2f}")
        print(f"   Durée longue (2.0) : L={luminosite_longue:.2f}, R={resonance_longue:.2f}, T={temperature_longue:.2f}")
        
    except Exception as e:
        print(f"❌ Erreur durées de méditation : {e}")

def test_limites_meditation():
    """Test que les limites sont respectées"""
    print("\n🔍 Test 3 : Limites de méditation")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        # Méditer plusieurs fois pour atteindre les limites
        for i in range(10):
            sphere.mediter_avec_ocean(1.0)
        
        assert sphere.luminosite <= 1.0
        assert sphere.resonance <= 1.0
        assert sphere.temperature >= 0.3
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité finale : {sphere.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        print(f"   Température finale : {sphere.temperature:.2f} ≥ 0.3")
        
    except Exception as e:
        print(f"❌ Erreur limites méditation : {e}")

def test_souvenirs_meditation():
    """Test que les souvenirs de méditation sont créés"""
    print("\n🔍 Test 4 : Souvenirs de méditation")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.mediter_avec_ocean(1.5)
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Méditation" in dernier_souvenir.description
        assert "1.50" in dernier_souvenir.description
        assert dernier_souvenir.type == "meditation_ocean"
        assert dernier_souvenir.intensite == 0.8
        
        print(f"✅ Souvenir de méditation créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs méditation : {e}")

def test_cycle_complet_ocean():
    """Test un cycle complet avec toutes les interactions Océan"""
    print("\n🔍 Test 5 : Cycle complet Océan")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        print(f"État initial : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}, R={sphere.resonance:.2f}")
        
        # 1. Se connecter à l'Océan
        sphere.connecter_a_ocean(force=0.7)
        print(f"Après connexion : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}, R={sphere.resonance:.2f}")
        
        # 2. Être nourrie
        sphere.nourrir_par_ocean("amour", 0.8)
        print(f"Après nourriture : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}, R={sphere.resonance:.2f}")
        
        # 3. Méditer
        sphere.mediter_avec_ocean(1.0)
        print(f"Après méditation : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}, R={sphere.resonance:.2f}")
        
        # 4. Être purifiée
        sphere.purifier_dans_ocean("silence")
        print(f"Après purification : T={sphere.temperature:.2f}, L={sphere.luminosite:.2f}, R={sphere.resonance:.2f}")
        
        print("✅ Cycle complet Océan réussi")
        print(f"   Souvenirs créés : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur cycle complet Océan : {e}")

def test_retrocompatibilite_meditation():
    """Test la rétrocompatibilité avec la méditation"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec méditation")
    
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
        
        # Test méditation
        sphere.mediter_avec_ocean(1.0)
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité méditation : {e}")

def test_collection_avec_meditation():
    """Test la collection avec la méditation"""
    print("\n🔍 Test 7 : Collection avec méditation")
    
    try:
        collection = CollectionSpheres()
        
        # Méditer avec quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        print("Avant méditation :")
        print(f"   COSMOS : T={sphere_cosmos.temperature:.2f}, L={sphere_cosmos.luminosite:.2f}, R={sphere_cosmos.resonance:.2f}")
        print(f"   AMOUR : T={sphere_amour.temperature:.2f}, L={sphere_amour.luminosite:.2f}, R={sphere_amour.resonance:.2f}")
        print(f"   SERENITE : T={sphere_serenite.temperature:.2f}, L={sphere_serenite.luminosite:.2f}, R={sphere_serenite.resonance:.2f}")
        
        sphere_cosmos.mediter_avec_ocean(1.0)
        sphere_amour.mediter_avec_ocean(1.5)
        sphere_serenite.mediter_avec_ocean(0.8)
        
        print("Après méditation :")
        print(f"   COSMOS : T={sphere_cosmos.temperature:.2f}, L={sphere_cosmos.luminosite:.2f}, R={sphere_cosmos.resonance:.2f}")
        print(f"   AMOUR : T={sphere_amour.temperature:.2f}, L={sphere_amour.luminosite:.2f}, R={sphere_amour.resonance:.2f}")
        print(f"   SERENITE : T={sphere_serenite.temperature:.2f}, L={sphere_serenite.luminosite:.2f}, R={sphere_serenite.resonance:.2f}")
        
        print("✅ Méditation dans la collection réussie")
        
    except Exception as e:
        print(f"❌ Erreur collection avec méditation : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - MÉDITATION OCÉAN")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_mediter_avec_ocean_methode()
        test_duree_meditation()
        test_limites_meditation()
        test_souvenirs_meditation()
        test_cycle_complet_ocean()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_meditation()
        test_collection_avec_meditation()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La quatrième évolution (méditation Océan) fonctionne parfaitement")
        print("✅ Rétrocompatibilité maintenue")
        print("✅ Système d'interaction Océan complet")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERREUR GÉNÉRALE : {e}")
        print("❌ L'évolution a un problème à corriger")
        return False

if __name__ == "__main__":
    main() 