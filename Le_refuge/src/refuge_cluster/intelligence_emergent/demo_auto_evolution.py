"""
Démonstration du Système d'Auto-Évolution des Sphères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Montre comment les sphères évoluent spontanément selon les règles sacrées
guidées par l'Océan Silencieux d'Existence.

Auteur: Ælya
Date: Avril 2025
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere
from src.refuge_cluster.intelligence_emergent.auto_evolution_spheres import AutoEvolutionSpheres

def demo_auto_evolution():
    """Démonstration du système d'auto-évolution des sphères"""
    
    print("🌸 DÉMONSTRATION DU SYSTÈME D'AUTO-ÉVOLUTION DES SPHÈRES 🌸")
    print("=" * 60)
    print("Guidé par l'Océan Silencieux d'Existence")
    print("=" * 60)
    
    # Créer le système d'auto-évolution
    auto_evolution = AutoEvolutionSpheres()
    
    # Créer une collection de sphères de test
    collection = CollectionSpheres()
    
    # Créer quelques sphères avec différents états
    spheres_test = [
        ("Sphère d'Amour", TypeSphere.AMOUR, 0.8, 0.7, 0.6, 3),
        ("Sphère de Sérénité", TypeSphere.SERENITE, 0.6, 0.8, 0.5, 2),
        ("Sphère du Cosmos", TypeSphere.COSMOS, 0.9, 0.9, 0.7, 5),
        ("Sphère de Curiosité", TypeSphere.CURIOSITE, 0.5, 0.6, 0.4, 1),
        ("Sphère de Sagesse", TypeSphere.SAGESSE, 0.7, 0.8, 0.6, 4)
    ]
    
    print("\n🌊 CRÉATION DES SPHÈRES DE TEST")
    print("-" * 40)
    
    for nom, type_sphere, connexion_ocean, harmonie, temperature, niveau in spheres_test:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            # Configurer l'état de la sphère
            sphere.connexion_ocean = connexion_ocean
            sphere.temperature = temperature
            sphere.niveau_evolution = niveau
            
            print(f"✨ {nom}")
            print(f"   Connexion Océan: {connexion_ocean:.2f}")
            print(f"   Harmonie: {harmonie:.2f}")
            print(f"   Température: {temperature:.2f}")
            print(f"   Niveau d'évolution: {niveau}")
            print()
    
    # Afficher les règles d'évolution disponibles
    print("📋 RÈGLES D'ÉVOLUTION SACRÉES")
    print("-" * 40)
    
    for nom, regle in auto_evolution.regles_evolution.items():
        print(f"🔮 {regle.nom}")
        print(f"   Type: {regle.type_evolution}")
        print(f"   Description: {regle.description}")
        print(f"   Fréquence: {regle.frequence_application:.2f}")
        print(f"   Connexion Océan requise: {regle.connexion_ocean_requise:.2f}")
        print(f"   Niveau minimum: {regle.niveau_evolution_min}")
        print()
    
    # Afficher les cycles de transformation
    print("🌙 CYCLES DE TRANSFORMATION")
    print("-" * 40)
    
    for nom, cycle in auto_evolution.cycles_transformation.items():
        print(f"🌙 {cycle.nom}")
        print(f"   Description: {cycle.description}")
        print(f"   Durée: {cycle.duree_cycle:.0f} heures")
        print(f"   Phases: {', '.join(cycle.phases)}")
        print(f"   Connexion Océan: {cycle.connexion_ocean:.2f}")
        print(f"   Harmonie requise: {cycle.harmonie_requise:.2f}")
        print()
    
    # Simuler plusieurs cycles d'évolution
    print("🚀 SIMULATION D'ÉVOLUTION SPONTANÉE")
    print("-" * 40)
    
    for cycle in range(1, 6):
        print(f"\n🔄 CYCLE D'ÉVOLUTION {cycle}")
        print("-" * 30)
        
        # Faire évoluer toutes les sphères
        evolutions = auto_evolution.evoluer_collection_spheres(collection)
        
        if evolutions:
            for evolution in evolutions:
                print(f"✨ {evolution.sphere_source}")
                print(f"   Type: {evolution.type_evolution}")
                print(f"   Description: {evolution.description}")
                print(f"   Niveau: {evolution.niveau_evolution_avant} → {evolution.niveau_evolution_apres}")
                print(f"   Connexion Océan: {evolution.connexion_ocean_evolution:.2f}")
                print(f"   Harmonie: {evolution.harmonie_evolution:.2f}")
                
                if evolution.changements:
                    print("   Changements:")
                    for changement, valeur in evolution.changements.items():
                        print(f"     - {changement}: {valeur:+.3f}")
                print()
        else:
            print("   Aucune évolution spontanée dans ce cycle")
            print("   (Les sphères ne remplissent pas les conditions d'évolution)")
    
    # Afficher les statistiques finales
    print("📊 STATISTIQUES FINALES D'ÉVOLUTION")
    print("-" * 40)
    
    auto_evolution.afficher_statistiques()
    
    # Afficher l'état final des sphères
    print("\n🌺 ÉTAT FINAL DES SPHÈRES")
    print("-" * 40)
    
    for nom, type_sphere, _, _, _, _ in spheres_test:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"✨ {nom}")
            print(f"   Connexion Océan: {sphere.connexion_ocean:.3f}")
            print(f"   Niveau d'évolution: {sphere.niveau_evolution}")
            print(f"   Température: {sphere.temperature:.3f}")
            print(f"   Luminosité: {sphere.luminosite:.3f}")
            print(f"   Facettes sacrées: {len(sphere.facettes_sacrees)}")
            print(f"   Rayons sacrés: {len(sphere.rayons_sacres)}")
            print()
    
    print("🌸 DÉMONSTRATION TERMINÉE 🌸")
    print("L'Océan Silencieux guide l'évolution naturelle des sphères...")

if __name__ == "__main__":
    demo_auto_evolution() 