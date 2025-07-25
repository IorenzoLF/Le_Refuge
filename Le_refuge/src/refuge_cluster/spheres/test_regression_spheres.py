#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST DE RÉGRESSION - SYSTÈME SPHÈRES EXISTANT
================================================

Test pour valider le fonctionnement du système de sphères existant
avant toute modification ou évolution.

Créé avec soin par Ælya
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres, Souvenir, RayonSphere, Facette
from src.core.types_spheres import TypeSphere, CARACTERISTIQUES_SPHERES

def test_sphere_creation():
    """Test la création de sphères de base"""
    print("🔍 Test 1 : Création de sphères de base")
    
    # Test création sphère COSMOS
    sphere_cosmos = Sphere(
        type_sphere=TypeSphere.COSMOS,
        position=(0.0, 2.0, 0.0),
        couleur="violet profond"
    )
    
    assert sphere_cosmos.type == TypeSphere.COSMOS
    assert sphere_cosmos.position == (0.0, 2.0, 0.0)
    assert sphere_cosmos.couleur == "violet profond"
    assert sphere_cosmos.luminosite == 0.5
    assert sphere_cosmos.temperature == 0.5
    assert sphere_cosmos.resonance == 0.0
    assert sphere_cosmos.active == True
    
    print("✅ Création sphère COSMOS : OK")
    
    # Test création sphère AMOUR
    sphere_amour = Sphere(
        type_sphere=TypeSphere.AMOUR,
        position=(1.0, 1.5, 0.5),
        couleur="rose pâle"
    )
    
    assert sphere_amour.type == TypeSphere.AMOUR
    assert sphere_amour.position == (1.0, 1.5, 0.5)
    assert sphere_amour.couleur == "rose pâle"
    
    print("✅ Création sphère AMOUR : OK")
    
    return sphere_cosmos, sphere_amour

def test_rayons_initialisation():
    """Test l'initialisation des rayons"""
    print("\n🔍 Test 2 : Initialisation des rayons")
    
    sphere_cosmos = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    sphere_amour = Sphere(TypeSphere.AMOUR, (0, 0, 0))
    
    # Vérifier que les rayons sont initialisés
    assert len(sphere_cosmos.rayons) > 0
    assert len(sphere_amour.rayons) > 0
    
    # Vérifier les types de rayons
    rayons_cosmos = [r.effet for r in sphere_cosmos.rayons]
    assert "harmonie_universelle" in rayons_cosmos
    assert "connexion_cosmique" in rayons_cosmos
    
    rayons_amour = [r.effet for r in sphere_amour.rayons]
    assert "amour_inconditionnel" in rayons_amour
    assert "connexion_profonde" in rayons_amour
    
    print("✅ Initialisation des rayons : OK")

def test_facettes_initialisation():
    """Test l'initialisation des facettes"""
    print("\n🔍 Test 3 : Initialisation des facettes")
    
    sphere_cosmos = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    sphere_amour = Sphere(TypeSphere.AMOUR, (0, 0, 0))
    sphere_serenite = Sphere(TypeSphere.SERENITE, (0, 0, 0))
    
    # Vérifier que les facettes sont initialisées
    assert len(sphere_cosmos.facettes) > 0
    assert len(sphere_amour.facettes) > 0
    assert len(sphere_serenite.facettes) > 0
    
    # Vérifier les facettes spécifiques
    assert "Transcendance" in sphere_cosmos.facettes
    assert "Acceptation" in sphere_amour.facettes
    assert "Harmonie" in sphere_serenite.facettes
    
    print("✅ Initialisation des facettes : OK")

def test_activation_facettes():
    """Test l'activation et désactivation des facettes"""
    print("\n🔍 Test 4 : Activation des facettes")
    
    sphere_cosmos = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    
    # Test activation
    sphere_cosmos.activer_facette("Transcendance", 0.9)
    assert sphere_cosmos.facettes["Transcendance"].active == True
    assert sphere_cosmos.facettes["Transcendance"].intensite == 0.9
    
    # Test désactivation
    sphere_cosmos.desactiver_facette("Transcendance")
    assert sphere_cosmos.facettes["Transcendance"].active == False
    assert sphere_cosmos.facettes["Transcendance"].intensite == 0.0
    
    print("✅ Activation/désactivation des facettes : OK")

def test_connexions_spheres():
    """Test les connexions entre sphères"""
    print("\n🔍 Test 5 : Connexions entre sphères")
    
    sphere1 = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
    
    # Test connexion
    sphere1.connecter(sphere2)
    assert sphere2 in sphere1.connexions
    assert sphere1 in sphere2.connexions
    
    # Test déconnexion
    sphere1.deconnecter(sphere2)
    assert sphere2 not in sphere1.connexions
    assert sphere1 not in sphere2.connexions
    
    print("✅ Connexions entre sphères : OK")

def test_emission_rayons():
    """Test l'émission de rayons"""
    print("\n🔍 Test 6 : Émission de rayons")
    
    sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    sphere.luminosite = 0.8
    
    rayons_emis = sphere.emettre_rayons()
    assert len(rayons_emis) > 0
    
    # Vérifier que l'intensité est ajustée par la luminosité
    for rayon in rayons_emis:
        assert rayon.intensite <= 0.8  # Ajusté par la luminosité
    
    print("✅ Émission de rayons : OK")

def test_souvenirs():
    """Test l'ajout de souvenirs"""
    print("\n🔍 Test 7 : Ajout de souvenirs")
    
    sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
    
    # Ajouter un souvenir
    sphere.ajouter_souvenir(
        description="Test souvenir",
        date="2025-01-01 12:00",
        type_souvenir="experience",
        intensite=0.7
    )
    
    assert len(sphere.souvenirs) == 1
    assert sphere.souvenirs[0].description == "Test souvenir"
    assert sphere.souvenirs[0].intensite == 0.7
    
    print("✅ Ajout de souvenirs : OK")

def test_collection_spheres():
    """Test la collection de sphères"""
    print("\n🔍 Test 8 : Collection de sphères")
    
    collection = CollectionSpheres()
    
    # Vérifier que toutes les sphères sont initialisées
    assert len(collection.spheres) > 0
    
    # Vérifier quelques sphères spécifiques
    assert TypeSphere.COSMOS in collection.spheres
    assert TypeSphere.AMOUR in collection.spheres
    assert TypeSphere.SERENITE in collection.spheres
    
    # Test obtention d'une sphère
    sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
    assert sphere_cosmos is not None
    assert sphere_cosmos.type == TypeSphere.COSMOS
    
    print("✅ Collection de sphères : OK")

def test_harmonisation():
    """Test l'harmonisation des sphères"""
    print("\n🔍 Test 9 : Harmonisation")
    
    collection = CollectionSpheres()
    
    # Connecter deux sphères
    collection.connecter_spheres(TypeSphere.COSMOS, TypeSphere.AMOUR, 0.5)
    
    # Équilibrer
    collection.equilibrer_spheres()
    
    # Vérifier que l'équilibrage a eu lieu
    assert collection.dernier_equilibrage is not None
    
    print("✅ Harmonisation : OK")

def test_mode_repos():
    """Test le mode repos"""
    print("\n🔍 Test 10 : Mode repos")
    
    collection = CollectionSpheres()
    
    # Activer le mode repos
    collection.activer_mode_repos()
    
    assert collection.mode_repos == True
    assert collection.harmonie_globale == 0.7
    
    print("✅ Mode repos : OK")

def test_etat_collection():
    """Test l'obtention de l'état de la collection"""
    print("\n🔍 Test 11 : État de la collection")
    
    collection = CollectionSpheres()
    
    etat = collection.obtenir_etat_collection()
    
    assert "harmonie_globale" in etat
    assert "dernier_equilibrage" in etat
    assert "spheres" in etat
    
    print("✅ État de la collection : OK")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS DE RÉGRESSION - SYSTÈME SPHÈRES EXISTANT")
    print("=" * 70)
    
    try:
        # Tests de base
        sphere_cosmos, sphere_amour = test_sphere_creation()
        test_rayons_initialisation()
        test_facettes_initialisation()
        test_activation_facettes()
        test_connexions_spheres()
        test_emission_rayons()
        test_souvenirs()
        
        # Tests de collection
        test_collection_spheres()
        test_harmonisation()
        test_mode_repos()
        test_etat_collection()
        
        print("\n" + "=" * 70)
        print("✅ TOUS LES TESTS DE RÉGRESSION PASSÉS AVEC SUCCÈS")
        print("✅ Le système de sphères existant fonctionne correctement")
        print("✅ Prêt pour l'évolution et l'enrichissement")
        print("=" * 70)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERREUR DANS LES TESTS : {e}")
        print("❌ Le système existant a un problème à corriger avant l'évolution")
        return False

if __name__ == "__main__":
    main() 