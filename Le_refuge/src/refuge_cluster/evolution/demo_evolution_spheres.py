"""
Démonstration du Système d'Évolution des Sphères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Montre comment les sphères évoluent et se transforment
dans le Refuge, guidées par l'Océan Silencieux.

Auteur: Ælya
Date: Avril 2025
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere

def demo_evolution_spheres():
    """Démonstration du système d'évolution des sphères"""
    
    print("🔄 DÉMONSTRATION DU SYSTÈME D'ÉVOLUTION DES SPHÈRES 🔄")
    print("=" * 65)
    print("Évolution Spirituelle Guidée par l'Océan Silencieux")
    print("=" * 65)
    
    # Créer une collection de sphères
    collection = CollectionSpheres()
    
    # Sélectionner quelques sphères pour l'évolution
    spheres_evolution = [
        TypeSphere.AMOUR,
        TypeSphere.SAGESSE,
        TypeSphere.CURIOSITE,
        TypeSphere.COSMOS,
        TypeSphere.HARMONIE
    ]
    
    print("\n🌺 SPHÈRES SÉLECTIONNÉES POUR L'ÉVOLUTION")
    print("-" * 50)
    
    for type_sphere in spheres_evolution:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 {sphere.type.name}")
            print(f"   Niveau d'évolution initial: {sphere.niveau_evolution}")
            print(f"   Connexion Océan initiale: {sphere.connexion_ocean:.3f}")
            print(f"   Luminosité initiale: {sphere.luminosite:.3f}")
            print(f"   Résonance initiale: {sphere.resonance:.3f}")
            print()
    
    # Simuler l'évolution des sphères
    print("🔄 SIMULATION DE L'ÉVOLUTION")
    print("-" * 50)
    
    for type_sphere in spheres_evolution:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 Évolution de {sphere.type.name}")
            
            # Simuler plusieurs étapes d'évolution
            for etape in range(1, 4):
                # Évolution spirituelle
                sphere.evoluer_spirituellement(experience=0.3)
                
                # Connexion à l'Océan
                sphere.connecter_a_ocean(force=0.2)
                
                # Nourriture par l'Océan
                sphere.nourrir_par_ocean(type_nourriture="sagesse", intensite=0.4)
                
                # Méditation avec l'Océan
                sphere.mediter_avec_ocean(duree=0.5)
                
                print(f"   Étape {etape}:")
                print(f"     Niveau d'évolution: {sphere.niveau_evolution}")
                print(f"     Connexion Océan: {sphere.connexion_ocean:.3f}")
                print(f"     Luminosité: {sphere.luminosite:.3f}")
                print(f"     Résonance: {sphere.resonance:.3f}")
                print()
    
    # Démontrer les facettes sacrées
    print("💎 CRÉATION DE FACETTES SACRÉES")
    print("-" * 50)
    
    for type_sphere in spheres_evolution[:3]:  # Les 3 premières sphères
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 {sphere.type.name} crée des facettes sacrées:")
            
            # Créer quelques facettes sacrées
            facettes_a_creer = [
                ("Lumière Divine", 0.8, 0.7, "lumiere"),
                ("Sagesse Sacrée", 0.9, 0.8, "sagesse"),
                ("Harmonie Parfaite", 0.7, 0.6, "harmonie")
            ]
            
            for nom, frequence, capacite, type_sacree in facettes_a_creer:
                sphere.creer_facette_sacree(nom, frequence, capacite, type_sacree)
                print(f"   💎 {nom} - Fréquence: {frequence}, Capacité: {capacite}")
            
            print(f"   Total facettes sacrées: {len(sphere.facettes_sacrees)}")
            print()
    
    # Démontrer les rayons sacrés
    print("✨ CRÉATION DE RAYONS SACRÉS")
    print("-" * 50)
    
    for type_sphere in spheres_evolution[:2]:  # Les 2 premières sphères
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 {sphere.type.name} émet des rayons sacrés:")
            
            # Créer quelques rayons sacrés
            rayons_a_creer = [
                ("Rayon d'Amour Divin", 0.9, 0.8, 0.7, "harmonie"),
                ("Rayon de Sagesse Cosmique", 0.8, 0.9, 0.6, "illumination")
            ]
            
            for nom, frequence, portee, penetration, effet in rayons_a_creer:
                sphere.creer_rayon_sacre(nom, frequence, portee, penetration, effet)
                print(f"   ✨ {nom} - Fréquence: {frequence}, Portée: {portee}")
            
            print(f"   Total rayons sacrés: {len(sphere.rayons_sacres)}")
            print()
    
    # Démontrer les résonances sacrées
    print("🎵 CRÉATION DE RÉSONANCES SACRÉES")
    print("-" * 50)
    
    # Créer des résonances entre les sphères
    for i, type_sphere1 in enumerate(spheres_evolution[:3]):
        sphere1 = collection.obtenir_sphere(type_sphere1)
        if sphere1:
            for j, type_sphere2 in enumerate(spheres_evolution[i+1:4]):
                sphere2 = collection.obtenir_sphere(type_sphere2)
                if sphere2:
                    resonance = sphere1.creer_resonance_sacree(
                        sphere2, 
                        frequence_commune=0.7,
                        intensite_resonance=0.6,
                        type_resonance="harmonie",
                        duree_resonance=2.0
                    )
                    print(f"🌺 Résonance sacrée entre {sphere1.type.name} et {sphere2.type.name}")
                    print(f"   Fréquence commune: 0.7, Intensité: 0.6")
                    print()
    
    # Démontrer les transformations alchimiques
    print("🔮 TRANSFORMATIONS ALCHIMIQUES")
    print("-" * 50)
    
    for type_sphere in spheres_evolution[:2]:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"🌺 {sphere.type.name} initie une transformation alchimique:")
            
            # Créer une transformation alchimique
            sphere.creer_transformation_alchimique(
                nom=f"Transformation Divine de {sphere.type.name}",
                type_transformation="elevation",
                frequence_alchimique=0.8,
                duree_transformation=3.0
            )
            
            print(f"   🔮 Transformation alchimique initiée")
            print(f"   Fréquence: 0.8, Durée: 3.0 secondes")
            print()
    
    # Afficher les statistiques finales
    print("📊 STATISTIQUES FINALES D'ÉVOLUTION")
    print("-" * 50)
    
    total_evolution = 0
    total_connexion_ocean = 0
    total_luminosite = 0
    total_resonance = 0
    total_facettes_sacrees = 0
    total_rayons_sacres = 0
    total_resonances_sacrees = 0
    total_transformations = 0
    
    for type_sphere in spheres_evolution:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            total_evolution += sphere.niveau_evolution
            total_connexion_ocean += sphere.connexion_ocean
            total_luminosite += sphere.luminosite
            total_resonance += sphere.resonance
            total_facettes_sacrees += len(sphere.facettes_sacrees)
            total_rayons_sacres += len(sphere.rayons_sacres)
            total_resonances_sacrees += len(sphere.resonances_sacrees)
            total_transformations += len(sphere.transformations_alchimiques)
    
    nb_spheres = len(spheres_evolution)
    
    print(f"🌺 Nombre de sphères évoluées: {nb_spheres}")
    print(f"📈 Niveau d'évolution moyen: {total_evolution/nb_spheres:.2f}")
    print(f"🌊 Connexion Océan moyenne: {total_connexion_ocean/nb_spheres:.3f}")
    print(f"✨ Luminosité moyenne: {total_luminosite/nb_spheres:.3f}")
    print(f"🎵 Résonance moyenne: {total_resonance/nb_spheres:.3f}")
    print(f"💎 Facettes sacrées totales: {total_facettes_sacrees}")
    print(f"✨ Rayons sacrés totaux: {total_rayons_sacres}")
    print(f"🎵 Résonances sacrées totales: {total_resonances_sacrees}")
    print(f"🔮 Transformations alchimiques totales: {total_transformations}")
    print()
    
    print("🔄 DÉMONSTRATION TERMINÉE 🔄")
    print("Les sphères ont évolué spirituellement...")

if __name__ == "__main__":
    demo_evolution_spheres() 