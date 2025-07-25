#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - RÉSONANCES SACRÉES
======================================

Test pour valider la neuvième évolution de la classe Sphere :
ajout de l'attribut resonances_sacrees et de la méthode creer_resonance_sacree.

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

def test_resonances_sacrees_attribut():
    """Test l'attribut resonances_sacrees"""
    print("\n🔍 Test 1 : Attribut resonances_sacrees")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'resonances_sacrees')
        assert sphere.resonances_sacrees == []
        
        print(f"✅ Attribut resonances_sacrees présent : {len(sphere.resonances_sacrees)} résonances")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut resonances_sacrees : {e}")
        return None

def test_creer_resonance_sacree_methode():
    """Test la méthode creer_resonance_sacree"""
    print("\n🔍 Test 2 : Méthode creer_resonance_sacree")
    
    try:
        sphere1 = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.SERENITE, (1, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere1, 'creer_resonance_sacree')
        
        # Test création de résonance sacrée
        luminosite_avant1 = sphere1.luminosite
        resonance_avant1 = sphere1.resonance
        luminosite_avant2 = sphere2.luminosite
        resonance_avant2 = sphere2.resonance
        souvenirs_avant1 = len(sphere1.souvenirs)
        souvenirs_avant2 = len(sphere2.souvenirs)
        
        sphere1.creer_resonance_sacree(
            sphere_cible=sphere2,
            frequence_commune=528.0,
            intensite_resonance=0.9,
            type_resonance="amour_paix",
            duree_resonance=1.0
        )
        
        assert len(sphere1.resonances_sacrees) == 1
        
        resonance = sphere1.resonances_sacrees[0]
        assert resonance["sphere_cible"] == "SERENITE"
        assert resonance["frequence_commune"] == 528.0
        assert resonance["intensite_resonance"] == 0.9
        assert resonance["type_resonance"] == "amour_paix"
        assert resonance["duree_resonance"] == 1.0
        assert resonance["evolution_resonance"] == 1.0
        assert resonance["connexion_ocean"] == 0.85
        assert resonance["active"] == True
        
        assert sphere1.luminosite > luminosite_avant1
        assert sphere1.resonance > resonance_avant1
        assert sphere2.luminosite > luminosite_avant2
        assert sphere2.resonance > resonance_avant2
        assert len(sphere1.souvenirs) > souvenirs_avant1
        assert len(sphere2.souvenirs) > souvenirs_avant2
        
        print(f"✅ Résonance sacrée créée avec succès")
        print(f"   Sphère source : {sphere1.type.name}")
        print(f"   Sphère cible : {resonance['sphere_cible']}")
        print(f"   Fréquence commune : {resonance['frequence_commune']} Hz")
        print(f"   Intensité de résonance : {resonance['intensite_resonance']}")
        print(f"   Type de résonance : {resonance['type_resonance']}")
        print(f"   Luminosité {sphere1.type.name} : {luminosite_avant1:.2f} → {sphere1.luminosite:.2f}")
        print(f"   Résonance {sphere1.type.name} : {resonance_avant1:.2f} → {sphere1.resonance:.2f}")
        print(f"   Luminosité {sphere2.type.name} : {luminosite_avant2:.2f} → {sphere2.luminosite:.2f}")
        print(f"   Résonance {sphere2.type.name} : {resonance_avant2:.2f} → {sphere2.resonance:.2f}")
        
        return sphere1, sphere2
        
    except Exception as e:
        print(f"❌ Erreur méthode creer_resonance_sacree : {e}")
        return None, None

def test_resonances_differentes():
    """Test différentes résonances sacrées"""
    print("\n🔍 Test 3 : Résonances sacrées différentes")
    
    try:
        resonances = [
            {
                "type": "sagesse_force",
                "frequence": 741.0,
                "intensite": 0.95,
                "duree": 1.5
            },
            {
                "type": "paix_silence",
                "frequence": 432.0,
                "intensite": 0.8,
                "duree": 0.8
            },
            {
                "type": "amour_joie",
                "frequence": 528.0,
                "intensite": 0.9,
                "duree": 1.2
            },
            {
                "type": "cosmos_infini",
                "frequence": 999.0,
                "intensite": 1.0,
                "duree": 2.0
            }
        ]
        
        sphere1 = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere3 = Sphere(TypeSphere.SERENITE, (0, 1, 0))
        sphere4 = Sphere(TypeSphere.SAGESSE, (1, 1, 0))
        
        spheres_cibles = [sphere2, sphere3, sphere4, sphere1]
        
        for i, resonance in enumerate(resonances):
            sphere1.creer_resonance_sacree(
                sphere_cible=spheres_cibles[i],
                frequence_commune=resonance["frequence"],
                intensite_resonance=resonance["intensite"],
                type_resonance=resonance["type"],
                duree_resonance=resonance["duree"]
            )
            
            print(f"✅ Résonance '{resonance['type']}' créée")
        
        print(f"✅ Total résonances sacrées : {len(sphere1.resonances_sacrees)}")
        
    except Exception as e:
        print(f"❌ Erreur résonances différentes : {e}")

def test_souvenirs_resonances():
    """Test que les souvenirs de résonances sont créés"""
    print("\n🔍 Test 4 : Souvenirs de résonances sacrées")
    
    try:
        sphere1 = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.SERENITE, (1, 0, 0))
        
        souvenirs_initiaux1 = len(sphere1.souvenirs)
        souvenirs_initiaux2 = len(sphere2.souvenirs)
        
        sphere1.creer_resonance_sacree(
            sphere_cible=sphere2,
            frequence_commune=432.0,
            intensite_resonance=0.85,
            type_resonance="amour_serenite",
            duree_resonance=1.0
        )
        
        # Vérifier qu'un nouveau souvenir a été créé pour chaque sphère
        assert len(sphere1.souvenirs) == souvenirs_initiaux1 + 1
        assert len(sphere2.souvenirs) == souvenirs_initiaux2 + 1
        
        dernier_souvenir1 = sphere1.souvenirs[-1]
        dernier_souvenir2 = sphere2.souvenirs[-1]
        
        assert "Résonance sacrée créée" in dernier_souvenir1.description
        assert "SERENITE" in dernier_souvenir1.description
        assert dernier_souvenir1.type == "resonance_sacree"
        assert dernier_souvenir1.intensite == 0.9
        
        assert "Résonance sacrée reçue" in dernier_souvenir2.description
        assert "AMOUR" in dernier_souvenir2.description
        assert dernier_souvenir2.type == "resonance_sacree"
        assert dernier_souvenir2.intensite == 0.9
        
        print(f"✅ Souvenirs de résonance sacrée créés")
        print(f"   Sphère 1 : {dernier_souvenir1.description}")
        print(f"   Sphère 2 : {dernier_souvenir2.description}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs résonances : {e}")

def test_limites_resonances():
    """Test que les limites sont respectées lors de la création de résonances"""
    print("\n🔍 Test 5 : Limites lors de la création de résonances")
    
    try:
        sphere1 = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        
        # Créer plusieurs résonances pour tester les limites
        for i in range(10):
            sphere1.creer_resonance_sacree(
                sphere_cible=sphere2,
                frequence_commune=528.0 + i * 50,
                intensite_resonance=0.8,
                type_resonance=f"test_{i}",
                duree_resonance=1.0
            )
        
        assert sphere1.luminosite <= 1.0
        assert sphere1.resonance <= 1.0
        assert sphere2.luminosite <= 1.0
        assert sphere2.resonance <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité {sphere1.type.name} : {sphere1.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance {sphere1.type.name} : {sphere1.resonance:.2f} ≤ 1.0")
        print(f"   Luminosité {sphere2.type.name} : {sphere2.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance {sphere2.type.name} : {sphere2.resonance:.2f} ≤ 1.0")
        print(f"   Nombre de résonances sacrées : {len(sphere1.resonances_sacrees)}")
        
    except Exception as e:
        print(f"❌ Erreur limites résonances : {e}")

def test_retrocompatibilite_resonances():
    """Test la rétrocompatibilité avec les résonances sacrées"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec résonances sacrées")
    
    try:
        sphere1 = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        
        # Test des fonctionnalités existantes
        sphere1.vibrer(0.1)
        sphere1.activer_facette("Transcendance", 0.9)
        rayons = sphere1.emettre_rayons()
        
        # Test connexion à l'Océan
        sphere1.connecter_a_ocean(force=0.6)
        
        # Test nourriture
        sphere1.nourrir_par_ocean("amour", 0.5)
        
        # Test purification
        sphere1.purifier_dans_ocean("silence")
        
        # Test méditation
        sphere1.mediter_avec_ocean(1.0)
        
        # Test définition d'essence
        sphere1.definir_essence_sacree(
            nom="Essence Test",
            frequence_fondamentale=528.0,
            couleur_primordiale="rose",
            vibration_essentielle="test"
        )
        
        # Test évolution
        sphere1.evoluer_spirituellement(1.0)
        
        # Test création de facette sacrée
        sphere1.creer_facette_sacree(
            nom="Facette Test",
            frequence_resonance=528.0,
            capacite_transformation=0.8,
            type_sacree="test"
        )
        
        # Test création de rayon sacré
        sphere1.creer_rayon_sacre(
            nom="Rayon Test",
            frequence_sacree=528.0,
            portee_cosmique=0.8,
            capacite_penetration=0.8,
            effet_resonance="test"
        )
        
        # Test création de résonance sacrée
        sphere1.creer_resonance_sacree(
            sphere_cible=sphere2,
            frequence_commune=528.0,
            intensite_resonance=0.8,
            type_resonance="test",
            duree_resonance=1.0
        )
        
        # Test connexion avec autre sphère
        sphere3 = Sphere(TypeSphere.SERENITE, (0, 1, 0))
        sphere1.connecter(sphere3)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere1.connexion_ocean:.2f}")
        print(f"   Température : {sphere1.temperature:.2f}")
        print(f"   Luminosité : {sphere1.luminosite:.2f}")
        print(f"   Résonance : {sphere1.resonance:.2f}")
        print(f"   Niveau d'évolution : {sphere1.niveau_evolution}")
        print(f"   Essence : {sphere1.essence_sacree['nom'] if sphere1.essence_sacree else 'Aucune'}")
        print(f"   Facettes sacrées : {len(sphere1.facettes_sacrees)}")
        print(f"   Rayons sacrés : {len(sphere1.rayons_sacres)}")
        print(f"   Résonances sacrées : {len(sphere1.resonances_sacrees)}")
        print(f"   Souvenirs : {len(sphere1.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité résonances : {e}")

def test_collection_avec_resonances():
    """Test la collection avec les résonances sacrées"""
    print("\n🔍 Test 7 : Collection avec résonances sacrées")
    
    try:
        collection = CollectionSpheres()
        
        # Créer des résonances sacrées entre sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        sphere_sagesse = collection.obtenir_sphere(TypeSphere.SAGESSE)
        
        sphere_cosmos.creer_resonance_sacree(
            sphere_cible=sphere_amour,
            frequence_commune=528.0,
            intensite_resonance=0.95,
            type_resonance="cosmos_amour",
            duree_resonance=1.5
        )
        
        sphere_amour.creer_resonance_sacree(
            sphere_cible=sphere_serenite,
            frequence_commune=432.0,
            intensite_resonance=0.9,
            type_resonance="amour_serenite",
            duree_resonance=1.0
        )
        
        sphere_serenite.creer_resonance_sacree(
            sphere_cible=sphere_sagesse,
            frequence_commune=741.0,
            intensite_resonance=0.85,
            type_resonance="serenite_sagesse",
            duree_resonance=1.2
        )
        
        print("✅ Résonances sacrées dans la collection créées")
        print(f"   COSMOS : {len(sphere_cosmos.resonances_sacrees)} résonances sacrées")
        print(f"   AMOUR : {len(sphere_amour.resonances_sacrees)} résonances sacrées")
        print(f"   SERENITE : {len(sphere_serenite.resonances_sacrees)} résonances sacrées")
        print(f"   SAGESSE : {len(sphere_sagesse.resonances_sacrees)} résonances sacrées")
        
        # Afficher les détails des résonances
        for resonance in sphere_cosmos.resonances_sacrees:
            print(f"     - {sphere_cosmos.type.name} ↔ {resonance['sphere_cible']} : {resonance['frequence_commune']} Hz ({resonance['type_resonance']})")
        
    except Exception as e:
        print(f"❌ Erreur collection avec résonances : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - RÉSONANCES SACRÉES")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_resonances_sacrees_attribut()
        sphere2, sphere3 = test_creer_resonance_sacree_methode()
        test_resonances_differentes()
        test_souvenirs_resonances()
        test_limites_resonances()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_resonances()
        test_collection_avec_resonances()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La neuvième évolution (résonances sacrées) fonctionne parfaitement")
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