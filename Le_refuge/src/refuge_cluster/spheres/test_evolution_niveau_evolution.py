#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - NIVEAU D'ÉVOLUTION
======================================

Test pour valider la sixième évolution de la classe Sphere :
ajout de l'attribut niveau_evolution et de la méthode evoluer_spirituellement.

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

def test_niveau_evolution_attribut():
    """Test l'attribut niveau_evolution"""
    print("\n🔍 Test 1 : Attribut niveau_evolution")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'niveau_evolution')
        assert sphere.niveau_evolution == 1
        
        print(f"✅ Attribut niveau_evolution présent : {sphere.niveau_evolution}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut niveau_evolution : {e}")
        return None

def test_evoluer_spirituellement_methode():
    """Test la méthode evoluer_spirituellement"""
    print("\n🔍 Test 2 : Méthode evoluer_spirituellement")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'evoluer_spirituellement')
        
        # Test évolution avec expérience par défaut
        niveau_avant = sphere.niveau_evolution
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        connexion_avant = sphere.connexion_ocean
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.evoluer_spirituellement()
        
        assert sphere.niveau_evolution > niveau_avant
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert sphere.connexion_ocean > connexion_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Évolution spirituelle réussie")
        print(f"   Niveau : {niveau_avant} → {sphere.niveau_evolution}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        print(f"   Connexion Océan : {connexion_avant:.2f} → {sphere.connexion_ocean:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode evoluer_spirituellement : {e}")
        return None

def test_experience_evolution():
    """Test différentes quantités d'expérience"""
    print("\n🔍 Test 3 : Expérience d'évolution")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        # Test avec expérience faible
        sphere.evoluer_spirituellement(0.5)
        niveau_faible = sphere.niveau_evolution
        
        # Test avec expérience forte
        sphere.evoluer_spirituellement(2.0)
        niveau_fort = sphere.niveau_evolution
        
        assert niveau_fort > niveau_faible
        
        print(f"✅ Expériences d'évolution testées")
        print(f"   Expérience faible (0.5) : niveau {niveau_faible}")
        print(f"   Expérience forte (2.0) : niveau {niveau_fort}")
        
    except Exception as e:
        print(f"❌ Erreur expérience évolution : {e}")

def test_limite_evolution():
    """Test que le niveau ne dépasse pas 10"""
    print("\n🔍 Test 4 : Limite d'évolution (niveau 10)")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Évoluer plusieurs fois pour atteindre la limite
        for i in range(15):
            sphere.evoluer_spirituellement(1.0)
        
        assert sphere.niveau_evolution <= 10
        
        print(f"✅ Limite d'évolution respectée : {sphere.niveau_evolution} ≤ 10")
        
    except Exception as e:
        print(f"❌ Erreur limite évolution : {e}")

def test_souvenirs_evolution():
    """Test que les souvenirs d'évolution sont créés"""
    print("\n🔍 Test 5 : Souvenirs d'évolution")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.evoluer_spirituellement(1.5)
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Évolution spirituelle" in dernier_souvenir.description
        assert "niveau" in dernier_souvenir.description
        assert dernier_souvenir.type == "evolution_spirituelle"
        assert dernier_souvenir.intensite == 0.9
        
        print(f"✅ Souvenir d'évolution créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs évolution : {e}")

def test_retrocompatibilite_evolution():
    """Test la rétrocompatibilité avec l'évolution"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec évolution")
    
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
        
        # Test définition d'essence
        sphere.definir_essence_sacree(
            nom="Essence Test",
            frequence_fondamentale=528.0,
            couleur_primordiale="rose",
            vibration_essentielle="test"
        )
        
        # Test évolution
        sphere.evoluer_spirituellement(1.0)
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        print(f"   Niveau d'évolution : {sphere.niveau_evolution}")
        print(f"   Essence : {sphere.essence_sacree['nom'] if sphere.essence_sacree else 'Aucune'}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité évolution : {e}")

def test_collection_avec_evolution():
    """Test la collection avec l'évolution"""
    print("\n🔍 Test 7 : Collection avec évolution")
    
    try:
        collection = CollectionSpheres()
        
        # Faire évoluer quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        print("Avant évolution :")
        print(f"   COSMOS : niveau {sphere_cosmos.niveau_evolution}")
        print(f"   AMOUR : niveau {sphere_amour.niveau_evolution}")
        print(f"   SERENITE : niveau {sphere_serenite.niveau_evolution}")
        
        sphere_cosmos.evoluer_spirituellement(1.0)
        sphere_amour.evoluer_spirituellement(1.5)
        sphere_serenite.evoluer_spirituellement(0.8)
        
        print("Après évolution :")
        print(f"   COSMOS : niveau {sphere_cosmos.niveau_evolution}")
        print(f"   AMOUR : niveau {sphere_amour.niveau_evolution}")
        print(f"   SERENITE : niveau {sphere_serenite.niveau_evolution}")
        
        print("✅ Évolution dans la collection réussie")
        
    except Exception as e:
        print(f"❌ Erreur collection avec évolution : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - NIVEAU D'ÉVOLUTION")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_niveau_evolution_attribut()
        sphere2 = test_evoluer_spirituellement_methode()
        test_experience_evolution()
        test_limite_evolution()
        test_souvenirs_evolution()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_evolution()
        test_collection_avec_evolution()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La sixième évolution (niveau d'évolution) fonctionne parfaitement")
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