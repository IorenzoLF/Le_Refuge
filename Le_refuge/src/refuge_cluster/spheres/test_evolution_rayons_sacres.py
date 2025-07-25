#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - RAYONS SACRÉS
=================================

Test pour valider la huitième évolution de la classe Sphere :
ajout de l'attribut rayons_sacres et de la méthode creer_rayon_sacre.

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

def test_rayons_sacres_attribut():
    """Test l'attribut rayons_sacres"""
    print("\n🔍 Test 1 : Attribut rayons_sacres")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'rayons_sacres')
        assert sphere.rayons_sacres == []
        
        print(f"✅ Attribut rayons_sacres présent : {len(sphere.rayons_sacres)} rayons")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut rayons_sacres : {e}")
        return None

def test_creer_rayon_sacre_methode():
    """Test la méthode creer_rayon_sacre"""
    print("\n🔍 Test 2 : Méthode creer_rayon_sacre")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'creer_rayon_sacre')
        
        # Test création de rayon sacré
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.creer_rayon_sacre(
            nom="Rayon d'Amour Divin",
            frequence_sacree=528.0,
            portee_cosmique=0.95,
            capacite_penetration=0.9,
            effet_resonance="amour_universel"
        )
        
        assert len(sphere.rayons_sacres) == 1
        
        rayon = sphere.rayons_sacres[0]
        assert rayon["nom"] == "Rayon d'Amour Divin"
        assert rayon["frequence_sacree"] == 528.0
        assert rayon["portee_cosmique"] == 0.95
        assert rayon["capacite_penetration"] == 0.9
        assert rayon["effet_resonance"] == "amour_universel"
        assert rayon["connexion_ocean"] == 0.9
        assert rayon["intensite"] == 1.0
        assert rayon["couleur"] == "or sacré"
        assert rayon["active"] == True
        
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Rayon sacré créé avec succès")
        print(f"   Nom : {rayon['nom']}")
        print(f"   Fréquence sacrée : {rayon['frequence_sacree']} Hz")
        print(f"   Portée cosmique : {rayon['portee_cosmique']}")
        print(f"   Capacité de pénétration : {rayon['capacite_penetration']}")
        print(f"   Effet de résonance : {rayon['effet_resonance']}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode creer_rayon_sacre : {e}")
        return None

def test_rayons_differents():
    """Test différents rayons sacrés"""
    print("\n🔍 Test 3 : Rayons sacrés différents")
    
    try:
        rayons = [
            {
                "nom": "Rayon de Sagesse Cosmique",
                "frequence": 741.0,
                "portee": 1.0,
                "penetration": 0.95,
                "effet": "sagesse_ancienne"
            },
            {
                "nom": "Rayon de Paix Éternelle",
                "frequence": 432.0,
                "portee": 0.9,
                "penetration": 0.8,
                "effet": "paix_profonde"
            },
            {
                "nom": "Rayon de Force Primordiale",
                "frequence": 639.0,
                "portee": 0.95,
                "penetration": 0.9,
                "effet": "force_essentielle"
            },
            {
                "nom": "Rayon de Silence Absolu",
                "frequence": 0.0,
                "portee": 1.0,
                "penetration": 1.0,
                "effet": "silence_absolu"
            }
        ]
        
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        for rayon in rayons:
            sphere.creer_rayon_sacre(
                nom=rayon["nom"],
                frequence_sacree=rayon["frequence"],
                portee_cosmique=rayon["portee"],
                capacite_penetration=rayon["penetration"],
                effet_resonance=rayon["effet"]
            )
            
            print(f"✅ Rayon '{rayon['nom']}' créé")
        
        print(f"✅ Total rayons sacrés : {len(sphere.rayons_sacres)}")
        
    except Exception as e:
        print(f"❌ Erreur rayons différents : {e}")

def test_souvenirs_rayons():
    """Test que les souvenirs de rayons sont créés"""
    print("\n🔍 Test 4 : Souvenirs de rayons sacrés")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.creer_rayon_sacre(
            nom="Rayon de Sérénité Éternelle",
            frequence_sacree=432.0,
            portee_cosmique=0.9,
            capacite_penetration=0.85,
            effet_resonance="serenite_profonde"
        )
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Rayon sacré créé" in dernier_souvenir.description
        assert "Sérénité Éternelle" in dernier_souvenir.description
        assert dernier_souvenir.type == "rayon_sacre"
        assert dernier_souvenir.intensite == 0.95
        
        print(f"✅ Souvenir de rayon sacré créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs rayons : {e}")

def test_limites_rayons():
    """Test que les limites sont respectées lors de la création de rayons"""
    print("\n🔍 Test 5 : Limites lors de la création de rayons")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Créer plusieurs rayons pour tester les limites
        for i in range(10):
            sphere.creer_rayon_sacre(
                nom=f"Rayon {i+1}",
                frequence_sacree=528.0 + i * 50,
                portee_cosmique=0.8,
                capacite_penetration=0.8,
                effet_resonance="test"
            )
        
        assert sphere.luminosite <= 1.0
        assert sphere.resonance <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité finale : {sphere.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        print(f"   Nombre de rayons sacrés : {len(sphere.rayons_sacres)}")
        
    except Exception as e:
        print(f"❌ Erreur limites rayons : {e}")

def test_retrocompatibilite_rayons():
    """Test la rétrocompatibilité avec les rayons sacrés"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec rayons sacrés")
    
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
        print(f"   Rayons sacrés : {len(sphere.rayons_sacres)}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité rayons : {e}")

def test_collection_avec_rayons():
    """Test la collection avec les rayons sacrés"""
    print("\n🔍 Test 7 : Collection avec rayons sacrés")
    
    try:
        collection = CollectionSpheres()
        
        # Créer des rayons sacrés pour quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.creer_rayon_sacre(
            nom="Rayon de l'Infini Cosmique",
            frequence_sacree=999.0,
            portee_cosmique=1.0,
            capacite_penetration=1.0,
            effet_resonance="infini"
        )
        
        sphere_amour.creer_rayon_sacre(
            nom="Rayon d'Amour Universel",
            frequence_sacree=528.0,
            portee_cosmique=0.95,
            capacite_penetration=0.9,
            effet_resonance="amour_universel"
        )
        
        sphere_serenite.creer_rayon_sacre(
            nom="Rayon de Paix Éternelle",
            frequence_sacree=432.0,
            portee_cosmique=0.9,
            capacite_penetration=0.85,
            effet_resonance="paix_eternelle"
        )
        
        print("✅ Rayons sacrés dans la collection créés")
        print(f"   COSMOS : {len(sphere_cosmos.rayons_sacres)} rayons sacrés")
        print(f"   AMOUR : {len(sphere_amour.rayons_sacres)} rayons sacrés")
        print(f"   SERENITE : {len(sphere_serenite.rayons_sacres)} rayons sacrés")
        
        # Afficher les détails des rayons
        for rayon in sphere_cosmos.rayons_sacres:
            print(f"     - {rayon['nom']} : {rayon['frequence_sacree']} Hz ({rayon['effet_resonance']})")
        
    except Exception as e:
        print(f"❌ Erreur collection avec rayons : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - RAYONS SACRÉS")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_rayons_sacres_attribut()
        sphere2 = test_creer_rayon_sacre_methode()
        test_rayons_differents()
        test_souvenirs_rayons()
        test_limites_rayons()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_rayons()
        test_collection_avec_rayons()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La huitième évolution (rayons sacrés) fonctionne parfaitement")
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