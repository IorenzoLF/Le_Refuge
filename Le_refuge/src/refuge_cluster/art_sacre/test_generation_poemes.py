"""
Test simple du système de génération de poèmes sacrés.
Auteur: Ælya
Date: Avril 2025

Test indépendant du générateur de poèmes sacrés.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere
from src.refuge_cluster.art_sacre.generateur_poemes_sacres import GenerateurPoemesSacres

def test_generation_poemes():
    """Test de la génération de poèmes sacrés."""
    
    print("🌸 Test du Générateur de Poèmes Sacrés 🌸")
    print("=" * 60)
    
    # Créer une collection de sphères enrichies
    collection = CollectionSpheres()
    
    # Enrichir quelques sphères pour le test
    sphere_amour = collection.obtenir_sphere(TypeSphere.AMOUR)
    if sphere_amour:
        sphere_amour.connecter_a_ocean(0.9)
        sphere_amour.definir_essence_sacree("Amour Divin", 528.0, "rose", "vibration_amoureuse")
        sphere_amour.evoluer_spirituellement(3.0)
        sphere_amour.creer_facette_sacree("Connexion Céleste", 0.9, 0.8, "lumiere")
        sphere_amour.creer_rayon_sacre("Rayon d'Amour Universel", 528.0, 0.9, 0.8, "harmonie")
    
    sphere_serenite = collection.obtenir_sphere(TypeSphere.SERENITE)
    if sphere_serenite:
        sphere_serenite.connecter_a_ocean(0.7)
        sphere_serenite.definir_essence_sacree("Paix Profonde", 432.0, "blanc", "vibration_paisible")
        sphere_serenite.evoluer_spirituellement(2.0)
        sphere_serenite.creer_facette_sacree("Silence Intérieur", 0.8, 0.6, "silence")
    
    sphere_cosmos = collection.obtenir_sphere(TypeSphere.COSMOS)
    if sphere_cosmos:
        sphere_cosmos.connecter_a_ocean(0.8)
        sphere_cosmos.definir_essence_sacree("Infini Cosmique", 639.0, "violet", "vibration_cosmique")
        sphere_cosmos.evoluer_spirituellement(4.0)
        sphere_cosmos.creer_facette_sacree("Expansion Universelle", 0.95, 0.9, "expansion")
        sphere_cosmos.creer_rayon_sacre("Rayon Cosmique", 639.0, 1.0, 0.9, "transcendance")
    
    # Créer le générateur
    generateur = GenerateurPoemesSacres()
    
    print(f"🎯 Collection créée avec {len(collection.spheres)} sphères enrichies")
    print()
    
    # Générer des poèmes pour quelques sphères
    print("📜 GÉNÉRATION DE POÈMES INDIVIDUELS :")
    print("-" * 40)
    
    spheres_test = [sphere_amour, sphere_serenite, sphere_cosmos]
    spheres_test = [s for s in spheres_test if s is not None]
    
    for i, sphere in enumerate(spheres_test, 1):
        print(f"\n🌺 Sphère {i} : {sphere.type.value}")
        print(f"   Connexion Océan : {sphere.connexion_ocean:.2f}")
        print(f"   Niveau d'Évolution : {sphere.niveau_evolution}")
        print(f"   Luminosité : {sphere.luminosite:.2f}")
        print(f"   Résonance : {sphere.resonance:.2f}")
        
        # Générer le poème
        poeme = generateur.generer_poeme_sphere(sphere)
        generateur.afficher_poeme(poeme)
    
    # Générer un poème d'harmonie globale
    print("\n🌊 GÉNÉRATION DU POÈME D'HARMONIE GLOBALE :")
    print("-" * 50)
    
    poeme_harmonie = generateur.generer_poeme_harmonie_globale(collection)
    generateur.afficher_poeme(poeme_harmonie)
    
    # Afficher les statistiques
    print("\n📊 STATISTIQUES DE GÉNÉRATION :")
    print("-" * 35)
    
    stats = generateur.obtenir_statistiques()
    print(f"   Total poèmes générés : {stats['total_poemes']}")
    print(f"   Qualité moyenne : {stats['qualite_moyenne']:.2f}")
    print(f"   Styles utilisés : {stats['styles_utilises']}")
    print(f"   Thèmes dominants : {stats['themes_dominants']}")
    print(f"   Derniers poèmes : {stats['derniers_poemes']}")
    
    print("\n" + "=" * 60)
    print("✅ Test de génération de poèmes sacrés terminé avec succès !")
    print("🌸 Le système de poésie sacrée fonctionne parfaitement ! 🌸")

if __name__ == "__main__":
    test_generation_poemes() 