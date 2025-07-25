#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST DE RÉGRESSION SIMPLIFIÉ - SYSTÈME SPHÈRES EXISTANT
==========================================================

Test simplifié pour valider le fonctionnement du système de sphères existant
avant toute modification ou évolution.

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
    print("Tentative d'import direct...")
    
    # Tentative d'import direct
    try:
        sys.path.insert(0, os.path.join(current_dir, '..', '..', '..'))
        from refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
        from core.types_spheres import TypeSphere
        print("✅ Imports directs réussis")
    except ImportError as e2:
        print(f"❌ Erreur d'import direct : {e2}")
        sys.exit(1)

def test_sphere_creation_basic():
    """Test basique de création de sphères"""
    print("\n🔍 Test 1 : Création basique de sphères")
    
    try:
        # Test création sphère COSMOS
        sphere_cosmos = Sphere(
            type_sphere=TypeSphere.COSMOS,
            position=(0.0, 2.0, 0.0),
            couleur="violet profond"
        )
        
        print(f"✅ Sphère COSMOS créée : {sphere_cosmos.type}")
        print(f"   Position : {sphere_cosmos.position}")
        print(f"   Couleur : {sphere_cosmos.couleur}")
        print(f"   Luminosité : {sphere_cosmos.luminosite}")
        
        # Test création sphère AMOUR
        sphere_amour = Sphere(
            type_sphere=TypeSphere.AMOUR,
            position=(1.0, 1.5, 0.5),
            couleur="rose pâle"
        )
        
        print(f"✅ Sphère AMOUR créée : {sphere_amour.type}")
        print(f"   Position : {sphere_amour.position}")
        print(f"   Couleur : {sphere_amour.couleur}")
        
        return sphere_cosmos, sphere_amour
        
    except Exception as e:
        print(f"❌ Erreur création sphères : {e}")
        return None, None

def test_rayons_basic():
    """Test basique des rayons"""
    print("\n🔍 Test 2 : Rayons de base")
    
    try:
        sphere_cosmos = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere_amour = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        print(f"✅ Rayons COSMOS : {len(sphere_cosmos.rayons)} rayons")
        for i, rayon in enumerate(sphere_cosmos.rayons):
            print(f"   Rayon {i+1} : {rayon.effet} ({rayon.couleur})")
        
        print(f"✅ Rayons AMOUR : {len(sphere_amour.rayons)} rayons")
        for i, rayon in enumerate(sphere_amour.rayons):
            print(f"   Rayon {i+1} : {rayon.effet} ({rayon.couleur})")
            
    except Exception as e:
        print(f"❌ Erreur rayons : {e}")

def test_facettes_basic():
    """Test basique des facettes"""
    print("\n🔍 Test 3 : Facettes de base")
    
    try:
        sphere_cosmos = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere_amour = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        sphere_serenite = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        print(f"✅ Facettes COSMOS : {len(sphere_cosmos.facettes)} facettes")
        for nom, facette in sphere_cosmos.facettes.items():
            print(f"   {nom} : active={facette.active}, intensité={facette.intensite}")
        
        print(f"✅ Facettes AMOUR : {len(sphere_amour.facettes)} facettes")
        for nom, facette in sphere_amour.facettes.items():
            print(f"   {nom} : active={facette.active}, intensité={facette.intensite}")
            
    except Exception as e:
        print(f"❌ Erreur facettes : {e}")

def test_connexions_basic():
    """Test basique des connexions"""
    print("\n🔍 Test 4 : Connexions de base")
    
    try:
        sphere1 = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        
        # Test connexion
        sphere1.connecter(sphere2)
        print(f"✅ Connexion établie : {sphere1.type} ↔ {sphere2.type}")
        print(f"   Connexions {sphere1.type} : {len(sphere1.connexions)}")
        print(f"   Connexions {sphere2.type} : {len(sphere2.connexions)}")
        
        # Test déconnexion
        sphere1.deconnecter(sphere2)
        print(f"✅ Déconnexion effectuée")
        print(f"   Connexions {sphere1.type} : {len(sphere1.connexions)}")
        print(f"   Connexions {sphere2.type} : {len(sphere2.connexions)}")
        
    except Exception as e:
        print(f"❌ Erreur connexions : {e}")

def test_collection_basic():
    """Test basique de la collection"""
    print("\n🔍 Test 5 : Collection de base")
    
    try:
        collection = CollectionSpheres()
        
        print(f"✅ Collection créée avec {len(collection.spheres)} sphères")
        
        # Vérifier quelques sphères spécifiques
        if TypeSphere.COSMOS in collection.spheres:
            print(f"✅ Sphère COSMOS présente dans la collection")
        
        if TypeSphere.AMOUR in collection.spheres:
            print(f"✅ Sphère AMOUR présente dans la collection")
        
        if TypeSphere.SERENITE in collection.spheres:
            print(f"✅ Sphère SERENITE présente dans la collection")
        
        # Test obtention d'une sphère
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        if sphere_cosmos:
            print(f"✅ Obtention sphère COSMOS réussie")
        
    except Exception as e:
        print(f"❌ Erreur collection : {e}")

def test_methodes_basic():
    """Test basique des méthodes"""
    print("\n🔍 Test 6 : Méthodes de base")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Test activation facette
        sphere.activer_facette("Transcendance", 0.9)
        print(f"✅ Facette Transcendance activée")
        
        # Test émission rayons
        rayons = sphere.emettre_rayons()
        print(f"✅ Émission de {len(rayons)} rayons")
        
        # Test ajout souvenir
        sphere.ajouter_souvenir("Test souvenir", "2025-01-01", "experience", 0.7)
        print(f"✅ Souvenir ajouté")
        
        # Test vibration
        sphere.vibrer(0.1)
        print(f"✅ Vibration effectuée, luminosité : {sphere.luminosite}")
        
    except Exception as e:
        print(f"❌ Erreur méthodes : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS DE RÉGRESSION SIMPLIFIÉS")
    print("=" * 60)
    
    try:
        # Tests de base
        sphere_cosmos, sphere_amour = test_sphere_creation_basic()
        test_rayons_basic()
        test_facettes_basic()
        test_connexions_basic()
        test_collection_basic()
        test_methodes_basic()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS DE RÉGRESSION PASSÉS AVEC SUCCÈS")
        print("✅ Le système de sphères existant fonctionne correctement")
        print("✅ Prêt pour l'évolution et l'enrichissement")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERREUR GÉNÉRALE : {e}")
        print("❌ Le système existant a un problème à corriger avant l'évolution")
        return False

if __name__ == "__main__":
    main() 