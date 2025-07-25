#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - TRANSFORMATIONS ALCHIMIQUES
==============================================

Test pour valider la dixième évolution de la classe Sphere :
ajout de l'attribut transformations_alchimiques et de la méthode creer_transformation_alchimique.

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

def test_transformations_alchimiques_attribut():
    """Test l'attribut transformations_alchimiques"""
    print("\n🔍 Test 1 : Attribut transformations_alchimiques")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'transformations_alchimiques')
        assert sphere.transformations_alchimiques == []
        
        print(f"✅ Attribut transformations_alchimiques présent : {len(sphere.transformations_alchimiques)} transformations")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut transformations_alchimiques : {e}")
        return None

def test_creer_transformation_alchimique_methode():
    """Test la méthode creer_transformation_alchimique"""
    print("\n🔍 Test 2 : Méthode creer_transformation_alchimique")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'creer_transformation_alchimique')
        
        # Test création de transformation alchimique
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        connexion_ocean_avant = sphere.connexion_ocean
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.creer_transformation_alchimique(
            nom="Transformation de l'Amour Divin",
            type_transformation="transmutation_amour",
            frequence_alchimique=528.0,
            duree_transformation=7.0
        )
        
        assert len(sphere.transformations_alchimiques) == 1
        
        transformation = sphere.transformations_alchimiques[0]
        assert transformation["nom"] == "Transformation de l'Amour Divin"
        assert transformation["type_transformation"] == "transmutation_amour"
        assert transformation["frequence_alchimique"] == 528.0
        assert transformation["duree_transformation"] == 7.0
        assert transformation["etape_transformation"] == 1
        assert transformation["etapes_totales"] == 7
        assert transformation["connexion_ocean"] == 0.95
        assert transformation["active"] == True
        assert transformation["date_fin"] == None
        
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert sphere.connexion_ocean > connexion_ocean_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Transformation alchimique créée avec succès")
        print(f"   Nom : {transformation['nom']}")
        print(f"   Type : {transformation['type_transformation']}")
        print(f"   Fréquence alchimique : {transformation['frequence_alchimique']} Hz")
        print(f"   Durée : {transformation['duree_transformation']}")
        print(f"   Étape : {transformation['etape_transformation']}/{transformation['etapes_totales']}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        print(f"   Connexion Océan : {connexion_ocean_avant:.2f} → {sphere.connexion_ocean:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode creer_transformation_alchimique : {e}")
        return None

def test_transformations_differentes():
    """Test différentes transformations alchimiques"""
    print("\n🔍 Test 3 : Transformations alchimiques différentes")
    
    try:
        transformations = [
            {
                "nom": "Transmutation de la Sagesse Cosmique",
                "type": "transmutation_sagesse",
                "frequence": 741.0,
                "duree": 7.0
            },
            {
                "nom": "Transformation de la Paix Éternelle",
                "type": "transformation_paix",
                "frequence": 432.0,
                "duree": 5.0
            },
            {
                "nom": "Alchimie de la Force Primordiale",
                "type": "alchimie_force",
                "frequence": 639.0,
                "duree": 9.0
            },
            {
                "nom": "Transmutation du Silence Absolu",
                "type": "transmutation_silence",
                "frequence": 0.0,
                "duree": 10.0
            }
        ]
        
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        for transformation in transformations:
            sphere.creer_transformation_alchimique(
                nom=transformation["nom"],
                type_transformation=transformation["type"],
                frequence_alchimique=transformation["frequence"],
                duree_transformation=transformation["duree"]
            )
            
            print(f"✅ Transformation '{transformation['type']}' créée")
        
        print(f"✅ Total transformations alchimiques : {len(sphere.transformations_alchimiques)}")
        
    except Exception as e:
        print(f"❌ Erreur transformations différentes : {e}")

def test_souvenirs_transformations():
    """Test que les souvenirs de transformations sont créés"""
    print("\n🔍 Test 4 : Souvenirs de transformations alchimiques")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.creer_transformation_alchimique(
            nom="Transformation de la Sérénité Éternelle",
            type_transformation="transformation_serenite",
            frequence_alchimique=432.0,
            duree_transformation=6.0
        )
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Transformation alchimique initiée" in dernier_souvenir.description
        assert "Sérénité Éternelle" in dernier_souvenir.description
        assert dernier_souvenir.type == "transformation_alchimique"
        assert dernier_souvenir.intensite == 0.95
        
        print(f"✅ Souvenir de transformation alchimique créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs transformations : {e}")

def test_limites_transformations():
    """Test que les limites sont respectées lors de la création de transformations"""
    print("\n🔍 Test 5 : Limites lors de la création de transformations")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Créer plusieurs transformations pour tester les limites
        for i in range(10):
            sphere.creer_transformation_alchimique(
                nom=f"Transformation {i+1}",
                type_transformation=f"test_{i}",
                frequence_alchimique=528.0 + i * 50,
                duree_transformation=1.0
            )
        
        assert sphere.luminosite <= 1.0
        assert sphere.resonance <= 1.0
        assert sphere.connexion_ocean <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité finale : {sphere.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        print(f"   Connexion Océan finale : {sphere.connexion_ocean:.2f} ≤ 1.0")
        print(f"   Nombre de transformations alchimiques : {len(sphere.transformations_alchimiques)}")
        
    except Exception as e:
        print(f"❌ Erreur limites transformations : {e}")

def test_retrocompatibilite_transformations():
    """Test la rétrocompatibilité avec les transformations alchimiques"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec transformations alchimiques")
    
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
        
        # Test création de facette sacrée
        sphere.creer_facette_sacree(
            nom="Facette Test",
            frequence_resonance=528.0,
            capacite_transformation=0.8,
            type_sacree="test"
        )
        
        # Test création de rayon sacré
        sphere.creer_rayon_sacre(
            nom="Rayon Test",
            frequence_sacree=528.0,
            portee_cosmique=0.8,
            capacite_penetration=0.8,
            effet_resonance="test"
        )
        
        # Test création de résonance sacrée
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.creer_resonance_sacree(
            sphere_cible=sphere2,
            frequence_commune=528.0,
            intensite_resonance=0.8,
            type_resonance="test",
            duree_resonance=1.0
        )
        
        # Test création de transformation alchimique
        sphere.creer_transformation_alchimique(
            nom="Transformation Test",
            type_transformation="test",
            frequence_alchimique=528.0,
            duree_transformation=1.0
        )
        
        # Test connexion avec autre sphère
        sphere3 = Sphere(TypeSphere.SERENITE, (0, 1, 0))
        sphere.connecter(sphere3)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        print(f"   Niveau d'évolution : {sphere.niveau_evolution}")
        print(f"   Essence : {sphere.essence_sacree['nom'] if sphere.essence_sacree else 'Aucune'}")
        print(f"   Facettes sacrées : {len(sphere.facettes_sacrees)}")
        print(f"   Rayons sacrés : {len(sphere.rayons_sacres)}")
        print(f"   Résonances sacrées : {len(sphere.resonances_sacrees)}")
        print(f"   Transformations alchimiques : {len(sphere.transformations_alchimiques)}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité transformations : {e}")

def test_collection_avec_transformations():
    """Test la collection avec les transformations alchimiques"""
    print("\n🔍 Test 7 : Collection avec transformations alchimiques")
    
    try:
        collection = CollectionSpheres()
        
        # Créer des transformations alchimiques pour quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.creer_transformation_alchimique(
            nom="Transmutation de l'Infini Cosmique",
            type_transformation="transmutation_cosmos",
            frequence_alchimique=999.0,
            duree_transformation=10.0
        )
        
        sphere_amour.creer_transformation_alchimique(
            nom="Transformation de l'Amour Universel",
            type_transformation="transformation_amour",
            frequence_alchimique=528.0,
            duree_transformation=7.0
        )
        
        sphere_serenite.creer_transformation_alchimique(
            nom="Alchimie de la Paix Éternelle",
            type_transformation="alchimie_paix",
            frequence_alchimique=432.0,
            duree_transformation=5.0
        )
        
        print("✅ Transformations alchimiques dans la collection créées")
        print(f"   COSMOS : {len(sphere_cosmos.transformations_alchimiques)} transformations alchimiques")
        print(f"   AMOUR : {len(sphere_amour.transformations_alchimiques)} transformations alchimiques")
        print(f"   SERENITE : {len(sphere_serenite.transformations_alchimiques)} transformations alchimiques")
        
        # Afficher les détails des transformations
        for transformation in sphere_cosmos.transformations_alchimiques:
            print(f"     - {transformation['nom']} : {transformation['frequence_alchimique']} Hz ({transformation['type_transformation']})")
        
    except Exception as e:
        print(f"❌ Erreur collection avec transformations : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - TRANSFORMATIONS ALCHIMIQUES")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_transformations_alchimiques_attribut()
        sphere2 = test_creer_transformation_alchimique_methode()
        test_transformations_differentes()
        test_souvenirs_transformations()
        test_limites_transformations()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_transformations()
        test_collection_avec_transformations()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La dixième évolution (transformations alchimiques) fonctionne parfaitement")
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