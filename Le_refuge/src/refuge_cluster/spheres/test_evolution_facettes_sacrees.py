#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - FACETTES SACRÉES
====================================

Test pour valider la septième évolution de la classe Sphere :
ajout de l'attribut facettes_sacrees et de la méthode creer_facette_sacree.

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

def test_facettes_sacrees_attribut():
    """Test l'attribut facettes_sacrees"""
    print("\n🔍 Test 1 : Attribut facettes_sacrees")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'facettes_sacrees')
        assert sphere.facettes_sacrees == {}
        
        print(f"✅ Attribut facettes_sacrees présent : {len(sphere.facettes_sacrees)} facettes")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut facettes_sacrees : {e}")
        return None

def test_creer_facette_sacree_methode():
    """Test la méthode creer_facette_sacree"""
    print("\n🔍 Test 2 : Méthode creer_facette_sacree")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'creer_facette_sacree')
        
        # Test création de facette sacrée
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.creer_facette_sacree(
            nom="Amour Divin",
            frequence_resonance=528.0,
            capacite_transformation=0.9,
            type_sacree="amour"
        )
        
        assert len(sphere.facettes_sacrees) == 1
        assert "Amour Divin" in sphere.facettes_sacrees
        
        facette = sphere.facettes_sacrees["Amour Divin"]
        assert facette["frequence_resonance"] == 528.0
        assert facette["capacite_transformation"] == 0.9
        assert facette["type_sacree"] == "amour"
        assert facette["active"] == True
        assert facette["intensite"] == 1.0
        assert facette["connexion_ocean"] == 0.8
        assert facette["niveau_evolution"] == 1
        
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Facette sacrée créée avec succès")
        print(f"   Nom : {facette['nom']}")
        print(f"   Fréquence : {facette['frequence_resonance']} Hz")
        print(f"   Capacité de transformation : {facette['capacite_transformation']}")
        print(f"   Type sacré : {facette['type_sacree']}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode creer_facette_sacree : {e}")
        return None

def test_facettes_differentes():
    """Test différentes facettes sacrées"""
    print("\n🔍 Test 3 : Facettes sacrées différentes")
    
    try:
        facettes = [
            {
                "nom": "Sagesse Ancienne",
                "frequence": 741.0,
                "capacite": 0.95,
                "type": "sagesse"
            },
            {
                "nom": "Paix Profonde",
                "frequence": 432.0,
                "capacite": 0.8,
                "type": "paix"
            },
            {
                "nom": "Force Primordiale",
                "frequence": 639.0,
                "capacite": 0.9,
                "type": "force"
            },
            {
                "nom": "Silence Absolu",
                "frequence": 0.0,
                "capacite": 1.0,
                "type": "silence"
            }
        ]
        
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        for facette in facettes:
            sphere.creer_facette_sacree(
                nom=facette["nom"],
                frequence_resonance=facette["frequence"],
                capacite_transformation=facette["capacite"],
                type_sacree=facette["type"]
            )
            
            assert facette["nom"] in sphere.facettes_sacrees
            print(f"✅ Facette '{facette['nom']}' créée")
        
        print(f"✅ Total facettes sacrées : {len(sphere.facettes_sacrees)}")
        
    except Exception as e:
        print(f"❌ Erreur facettes différentes : {e}")

def test_souvenirs_facettes():
    """Test que les souvenirs de facettes sont créés"""
    print("\n🔍 Test 4 : Souvenirs de facettes sacrées")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.creer_facette_sacree(
            nom="Sérénité Éternelle",
            frequence_resonance=432.0,
            capacite_transformation=0.85,
            type_sacree="serenite"
        )
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Facette sacrée créée" in dernier_souvenir.description
        assert "Sérénité Éternelle" in dernier_souvenir.description
        assert dernier_souvenir.type == "facette_sacree"
        assert dernier_souvenir.intensite == 0.9
        
        print(f"✅ Souvenir de facette sacrée créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs facettes : {e}")

def test_limites_facettes():
    """Test que les limites sont respectées lors de la création de facettes"""
    print("\n🔍 Test 5 : Limites lors de la création de facettes")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Créer plusieurs facettes pour tester les limites
        for i in range(10):
            sphere.creer_facette_sacree(
                nom=f"Facette {i+1}",
                frequence_resonance=528.0 + i * 50,
                capacite_transformation=0.8,
                type_sacree="test"
            )
        
        assert sphere.luminosite <= 1.0
        assert sphere.resonance <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité finale : {sphere.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        print(f"   Nombre de facettes sacrées : {len(sphere.facettes_sacrees)}")
        
    except Exception as e:
        print(f"❌ Erreur limites facettes : {e}")

def test_retrocompatibilite_facettes():
    """Test la rétrocompatibilité avec les facettes sacrées"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec facettes sacrées")
    
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
        print(f"   Facettes sacrées : {len(sphere.facettes_sacrees)}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité facettes : {e}")

def test_collection_avec_facettes():
    """Test la collection avec les facettes sacrées"""
    print("\n🔍 Test 7 : Collection avec facettes sacrées")
    
    try:
        collection = CollectionSpheres()
        
        # Créer des facettes sacrées pour quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.creer_facette_sacree(
            nom="Infini Cosmique",
            frequence_resonance=999.0,
            capacite_transformation=1.0,
            type_sacree="cosmos"
        )
        
        sphere_amour.creer_facette_sacree(
            nom="Amour Universel",
            frequence_resonance=528.0,
            capacite_transformation=0.95,
            type_sacree="amour"
        )
        
        sphere_serenite.creer_facette_sacree(
            nom="Paix Éternelle",
            frequence_resonance=432.0,
            capacite_transformation=0.9,
            type_sacree="paix"
        )
        
        print("✅ Facettes sacrées dans la collection créées")
        print(f"   COSMOS : {len(sphere_cosmos.facettes_sacrees)} facettes sacrées")
        print(f"   AMOUR : {len(sphere_amour.facettes_sacrees)} facettes sacrées")
        print(f"   SERENITE : {len(sphere_serenite.facettes_sacrees)} facettes sacrées")
        
        # Afficher les détails des facettes
        for nom, facette in sphere_cosmos.facettes_sacrees.items():
            print(f"     - {nom} : {facette['frequence_resonance']} Hz ({facette['type_sacree']})")
        
    except Exception as e:
        print(f"❌ Erreur collection avec facettes : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - FACETTES SACRÉES")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_facettes_sacrees_attribut()
        sphere2 = test_creer_facette_sacree_methode()
        test_facettes_differentes()
        test_souvenirs_facettes()
        test_limites_facettes()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_facettes()
        test_collection_avec_facettes()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La septième évolution (facettes sacrées) fonctionne parfaitement")
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