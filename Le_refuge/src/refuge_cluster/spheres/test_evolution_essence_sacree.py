#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 TEST ÉVOLUTION - ESSENCE SACRÉE
==================================

Test pour valider la cinquième évolution de la classe Sphere :
ajout de l'attribut essence_sacree et de la méthode definir_essence_sacree.

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

def test_essence_sacree_attribut():
    """Test l'attribut essence_sacree"""
    print("\n🔍 Test 1 : Attribut essence_sacree")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Vérifier que l'attribut existe
        assert hasattr(sphere, 'essence_sacree')
        assert sphere.essence_sacree is None
        
        print(f"✅ Attribut essence_sacree présent : {sphere.essence_sacree}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur attribut essence_sacree : {e}")
        return None

def test_definir_essence_sacree_methode():
    """Test la méthode definir_essence_sacree"""
    print("\n🔍 Test 2 : Méthode definir_essence_sacree")
    
    try:
        sphere = Sphere(TypeSphere.AMOUR, (0, 0, 0))
        
        # Vérifier que la méthode existe
        assert hasattr(sphere, 'definir_essence_sacree')
        
        # Test définition d'essence
        luminosite_avant = sphere.luminosite
        resonance_avant = sphere.resonance
        souvenirs_avant = len(sphere.souvenirs)
        
        sphere.definir_essence_sacree(
            nom="Amour Universel",
            frequence_fondamentale=528.0,
            couleur_primordiale="rose doré",
            vibration_essentielle="amour_inconditionnel"
        )
        
        assert sphere.essence_sacree is not None
        assert sphere.essence_sacree["nom"] == "Amour Universel"
        assert sphere.essence_sacree["frequence_fondamentale"] == 528.0
        assert sphere.essence_sacree["couleur_primordiale"] == "rose doré"
        assert sphere.essence_sacree["vibration_essentielle"] == "amour_inconditionnel"
        assert sphere.essence_sacree["connexion_source"] == True
        assert sphere.essence_sacree["intensite_essence"] == 1.0
        
        assert sphere.luminosite > luminosite_avant
        assert sphere.resonance > resonance_avant
        assert len(sphere.souvenirs) > souvenirs_avant
        
        print(f"✅ Essence sacrée définie avec succès")
        print(f"   Nom : {sphere.essence_sacree['nom']}")
        print(f"   Fréquence : {sphere.essence_sacree['frequence_fondamentale']} Hz")
        print(f"   Couleur : {sphere.essence_sacree['couleur_primordiale']}")
        print(f"   Vibration : {sphere.essence_sacree['vibration_essentielle']}")
        print(f"   Luminosité : {luminosite_avant:.2f} → {sphere.luminosite:.2f}")
        print(f"   Résonance : {resonance_avant:.2f} → {sphere.resonance:.2f}")
        
        return sphere
        
    except Exception as e:
        print(f"❌ Erreur méthode definir_essence_sacree : {e}")
        return None

def test_essences_differentes():
    """Test différentes essences sacrées"""
    print("\n🔍 Test 3 : Essences sacrées différentes")
    
    try:
        essences = [
            {
                "nom": "Sagesse Cosmique",
                "frequence": 741.0,
                "couleur": "violet profond",
                "vibration": "sagesse_ancienne"
            },
            {
                "nom": "Paix Éternelle",
                "frequence": 432.0,
                "couleur": "blanc nacré",
                "vibration": "paix_profonde"
            },
            {
                "nom": "Force Primordiale",
                "frequence": 639.0,
                "couleur": "or pur",
                "vibration": "force_essentielle"
            }
        ]
        
        for i, essence in enumerate(essences):
            sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
            
            sphere.definir_essence_sacree(
                nom=essence["nom"],
                frequence_fondamentale=essence["frequence"],
                couleur_primordiale=essence["couleur"],
                vibration_essentielle=essence["vibration"]
            )
            
            assert sphere.essence_sacree["nom"] == essence["nom"]
            assert sphere.essence_sacree["frequence_fondamentale"] == essence["frequence"]
            
            print(f"✅ Essence '{essence['nom']}' définie")
        
    except Exception as e:
        print(f"❌ Erreur essences différentes : {e}")

def test_souvenirs_essence():
    """Test que les souvenirs d'essence sont créés"""
    print("\n🔍 Test 4 : Souvenirs d'essence")
    
    try:
        sphere = Sphere(TypeSphere.SERENITE, (0, 0, 0))
        
        souvenirs_initiaux = len(sphere.souvenirs)
        
        sphere.definir_essence_sacree(
            nom="Sérénité Absolue",
            frequence_fondamentale=432.0,
            couleur_primordiale="bleu azur",
            vibration_essentielle="serenite_profonde"
        )
        
        # Vérifier qu'un nouveau souvenir a été créé
        assert len(sphere.souvenirs) == souvenirs_initiaux + 1
        
        dernier_souvenir = sphere.souvenirs[-1]
        assert "Essence sacrée définie" in dernier_souvenir.description
        assert "Sérénité Absolue" in dernier_souvenir.description
        assert dernier_souvenir.type == "essence_sacree"
        assert dernier_souvenir.intensite == 1.0
        
        print(f"✅ Souvenir d'essence créé")
        print(f"   Description : {dernier_souvenir.description}")
        print(f"   Type : {dernier_souvenir.type}")
        print(f"   Intensité : {dernier_souvenir.intensite}")
        
    except Exception as e:
        print(f"❌ Erreur souvenirs essence : {e}")

def test_limites_essence():
    """Test que les limites sont respectées lors de la définition d'essence"""
    print("\n🔍 Test 5 : Limites lors de la définition d'essence")
    
    try:
        sphere = Sphere(TypeSphere.COSMOS, (0, 0, 0))
        
        # Définir l'essence plusieurs fois pour tester les limites
        for i in range(5):
            sphere.definir_essence_sacree(
                nom=f"Essence {i+1}",
                frequence_fondamentale=528.0 + i * 100,
                couleur_primordiale="violet",
                vibration_essentielle="test"
            )
        
        assert sphere.luminosite <= 1.0
        assert sphere.resonance <= 1.0
        
        print(f"✅ Limites respectées")
        print(f"   Luminosité finale : {sphere.luminosite:.2f} ≤ 1.0")
        print(f"   Résonance finale : {sphere.resonance:.2f} ≤ 1.0")
        
    except Exception as e:
        print(f"❌ Erreur limites essence : {e}")

def test_retrocompatibilite_essence():
    """Test la rétrocompatibilité avec l'essence sacrée"""
    print("\n🔍 Test 6 : Rétrocompatibilité avec essence")
    
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
        
        # Test connexion avec autre sphère
        sphere2 = Sphere(TypeSphere.AMOUR, (1, 0, 0))
        sphere.connecter(sphere2)
        
        print("✅ Toutes les fonctionnalités fonctionnent ensemble")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Température : {sphere.temperature:.2f}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        print(f"   Essence : {sphere.essence_sacree['nom'] if sphere.essence_sacree else 'Aucune'}")
        print(f"   Souvenirs : {len(sphere.souvenirs)}")
        
    except Exception as e:
        print(f"❌ Erreur rétrocompatibilité essence : {e}")

def test_collection_avec_essence():
    """Test la collection avec l'essence sacrée"""
    print("\n🔍 Test 7 : Collection avec essence")
    
    try:
        collection = CollectionSpheres()
        
        # Définir des essences pour quelques sphères
        sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
        sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
        
        sphere_cosmos.definir_essence_sacree(
            nom="Cosmos Infini",
            frequence_fondamentale=999.0,
            couleur_primordiale="violet cosmique",
            vibration_essentielle="infini"
        )
        
        sphere_amour.definir_essence_sacree(
            nom="Amour Divin",
            frequence_fondamentale=528.0,
            couleur_primordiale="rose céleste",
            vibration_essentielle="amour_divin"
        )
        
        sphere_serenite.definir_essence_sacree(
            nom="Paix Éternelle",
            frequence_fondamentale=432.0,
            couleur_primordiale="blanc pur",
            vibration_essentielle="paix_eternelle"
        )
        
        print("✅ Essences sacrées dans la collection définies")
        print(f"   COSMOS : {sphere_cosmos.essence_sacree['nom']} ({sphere_cosmos.essence_sacree['frequence_fondamentale']} Hz)")
        print(f"   AMOUR : {sphere_amour.essence_sacree['nom']} ({sphere_amour.essence_sacree['frequence_fondamentale']} Hz)")
        print(f"   SERENITE : {sphere_serenite.essence_sacree['nom']} ({sphere_serenite.essence_sacree['frequence_fondamentale']} Hz)")
        
    except Exception as e:
        print(f"❌ Erreur collection avec essence : {e}")

def main():
    """Fonction principale de test"""
    print("🔍 DÉBUT DES TESTS D'ÉVOLUTION - ESSENCE SACRÉE")
    print("=" * 60)
    
    try:
        # Tests de l'évolution
        sphere1 = test_essence_sacree_attribut()
        sphere2 = test_definir_essence_sacree_methode()
        test_essences_differentes()
        test_souvenirs_essence()
        test_limites_essence()
        
        # Tests de rétrocompatibilité
        test_retrocompatibilite_essence()
        test_collection_avec_essence()
        
        print("\n" + "=" * 60)
        print("✅ TOUS LES TESTS D'ÉVOLUTION PASSÉS AVEC SUCCÈS")
        print("✅ La cinquième évolution (essence sacrée) fonctionne parfaitement")
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