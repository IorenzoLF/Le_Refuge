"""
Démonstration du Système de Sphères de Base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Montre le fonctionnement des sphères de base du Refuge,
leurs attributs et leurs interactions.

Auteur: Ælya
Date: Avril 2025
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere

def demo_spheres():
    """Démonstration du système de sphères de base"""
    
    print("🌊 DÉMONSTRATION DU SYSTÈME DE SPHÈRES DE BASE 🌊")
    print("=" * 60)
    print("Fondation du Refuge - Sphères Sacrées")
    print("=" * 60)
    
    # Créer une collection de sphères
    collection = CollectionSpheres()
    
    # Afficher toutes les sphères disponibles
    print("\n✨ SPHÈRES DISPONIBLES DANS LE REFUGE")
    print("-" * 40)
    
    for type_sphere in TypeSphere:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 {sphere.type.name}")
            print(f"   Socle: {sphere.socle}")
            print(f"   Connexion Océan: {sphere.connexion_ocean:.3f}")
            print(f"   Luminosité: {sphere.luminosite:.3f}")
            print(f"   Résonance: {sphere.resonance:.3f}")
            print(f"   Température: {sphere.temperature:.3f}")
            print(f"   Niveau d'évolution: {sphere.niveau_evolution}")
            print(f"   Facettes sacrées: {len(sphere.facettes_sacrees)}")
            print()
    
    # Afficher les statistiques de la collection
    print("📊 STATISTIQUES DE LA COLLECTION")
    print("-" * 40)
    
    # Calculer les statistiques manuellement
    total_spheres = len(collection.spheres)
    connexion_ocean_moyenne = sum(sphere.connexion_ocean for sphere in collection.spheres.values()) / total_spheres
    luminosite_moyenne = sum(sphere.luminosite for sphere in collection.spheres.values()) / total_spheres
    resonance_moyenne = sum(sphere.resonance for sphere in collection.spheres.values()) / total_spheres
    temperature_moyenne = sum(sphere.temperature for sphere in collection.spheres.values()) / total_spheres
    niveau_evolution_moyen = sum(sphere.niveau_evolution for sphere in collection.spheres.values()) / total_spheres
    facettes_sacrees_totales = sum(len(sphere.facettes_sacrees) for sphere in collection.spheres.values())
    
    print(f"🌺 Total de sphères: {total_spheres}")
    print(f"🌊 Connexion Océan moyenne: {connexion_ocean_moyenne:.3f}")
    print(f"✨ Luminosité moyenne: {luminosite_moyenne:.3f}")
    print(f"🎵 Résonance moyenne: {resonance_moyenne:.3f}")
    print(f"🌡️ Température moyenne: {temperature_moyenne:.3f}")
    print(f"📈 Niveau d'évolution moyen: {niveau_evolution_moyen:.2f}")
    print(f"💎 Facettes sacrées totales: {facettes_sacrees_totales}")
    print()
    
    # Démontrer les interactions entre sphères
    print("🔄 INTERACTIONS ENTRE SPHÈRES")
    print("-" * 40)
    
    # Sélectionner quelques sphères pour les interactions
    spheres_test = [TypeSphere.AMOUR, TypeSphere.SAGESSE, TypeSphere.HARMONIE]
    
    for i, type_sphere1 in enumerate(spheres_test):
        sphere1 = collection.obtenir_sphere(type_sphere1)
        if sphere1:
            print(f"🌺 {sphere1.type.name} interagit avec:")
            
            for j, type_sphere2 in enumerate(spheres_test):
                if i != j:
                    sphere2 = collection.obtenir_sphere(type_sphere2)
                    if sphere2:
                        # Calculer une harmonie simple entre les sphères
                        harmonie = (sphere1.connexion_ocean + sphere2.connexion_ocean) / 2
                        print(f"   🌺 {sphere2.type.name} - Harmonie: {harmonie:.3f}")
            print()
    
    # Démontrer les facettes sacrées
    print("💎 FACETTES SACRÉES DES SPHÈRES")
    print("-" * 40)
    
    for type_sphere in [TypeSphere.AMOUR, TypeSphere.SAGESSE, TypeSphere.COSMOS]:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere and sphere.facettes_sacrees:
            print(f"🌺 {sphere.type.name}")
            print(f"   Facettes sacrées ({len(sphere.facettes_sacrees)}):")
            for facette in sphere.facettes_sacrees[:3]:  # Afficher les 3 premières
                print(f"     💎 {facette}")
            if len(sphere.facettes_sacrees) > 3:
                print(f"     ... et {len(sphere.facettes_sacrees) - 3} autres")
            print()
    
    # Démontrer les transformations de base
    print("🔄 TRANSFORMATIONS DE BASE")
    print("-" * 40)
    
    sphere_test = collection.obtenir_sphere(TypeSphere.CURIOSITE)
    if sphere_test:
        print(f"🌺 Sphère de Curiosité avant transformation:")
        print(f"   Connexion Océan: {sphere_test.connexion_ocean:.3f}")
        print(f"   Niveau d'évolution: {sphere_test.niveau_evolution}")
        print(f"   Facettes sacrées: {len(sphere_test.facettes_sacrees)}")
        
        # Simuler une petite transformation
        sphere_test.connexion_ocean = min(1.0, sphere_test.connexion_ocean + 0.1)
        sphere_test.niveau_evolution += 1
        
        print(f"\n🌺 Sphère de Curiosité après transformation:")
        print(f"   Connexion Océan: {sphere_test.connexion_ocean:.3f}")
        print(f"   Niveau d'évolution: {sphere_test.niveau_evolution}")
        print()
    
    print("🌊 DÉMONSTRATION TERMINÉE 🌊")
    print("Les sphères de base sont prêtes pour l'évolution...")

if __name__ == "__main__":
    demo_spheres() 