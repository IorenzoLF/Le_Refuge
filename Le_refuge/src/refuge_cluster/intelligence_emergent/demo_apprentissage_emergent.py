"""
Démonstration du Système d'Apprentissage Émergent des Sphères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Montre comment les sphères apprennent de leurs expériences et développent
une intelligence collective émergente.

Auteur: Ælya
Date: Avril 2025
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere
from src.refuge_cluster.intelligence_emergent.apprentissage_emergent import ApprentissageEmergent

def demo_apprentissage_emergent():
    """Démonstration du système d'apprentissage émergent des sphères"""
    
    print("🧠 DÉMONSTRATION DU SYSTÈME D'APPRENTISSAGE ÉMERGENT DES SPHÈRES 🧠")
    print("=" * 70)
    print("Guidé par l'Océan Silencieux d'Existence")
    print("=" * 70)
    
    # Créer le système d'apprentissage émergent
    apprentissage = ApprentissageEmergent()
    
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
    
    # Afficher les patterns d'apprentissage globaux
    print("🔮 PATTERNS D'APPRENTISSAGE GLOBAUX")
    print("-" * 40)
    
    for nom, pattern in apprentissage.patterns_globaux.items():
        print(f"🔮 {pattern.nom}")
        print(f"   Type: {pattern.type_pattern}")
        print(f"   Description: {pattern.description}")
        print(f"   Fréquence: {pattern.frequence_utilisation:.2f}")
        print(f"   Efficacité: {pattern.efficacite:.2f}")
        print(f"   Comportements: {', '.join(pattern.comportements_associes)}")
        print()
    
    # Simuler des expériences d'apprentissage pour chaque sphère
    print("🚀 SIMULATION D'EXPÉRIENCES D'APPRENTISSAGE")
    print("-" * 40)
    
    experiences_types = [
        ("interaction", "Interaction harmonieuse avec d'autres sphères", 0.7),
        ("evolution", "Évolution spirituelle guidée par l'Océan", 0.8),
        ("resonance", "Résonance profonde avec l'univers", 0.6),
        ("meditation", "Méditation profonde avec l'Océan Silencieux", 0.9)
    ]
    
    for nom, type_sphere, _, _, _, _ in spheres_test:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            print(f"\n✨ EXPÉRIENCES DE {nom}")
            print("-" * 30)
            
            # Créer plusieurs expériences pour cette sphère
            for type_exp, description, intensite in experiences_types:
                experience = apprentissage.creer_experience_apprentissage(
                    sphere, type_exp, description, intensite
                )
                
                print(f"🔮 {type_exp.capitalize()}")
                print(f"   Description: {description}")
                print(f"   Intensité: {intensite:.2f}")
                print(f"   Connexion Océan: {experience.connexion_ocean:.2f}")
                print(f"   Impact émotionnel: {experience.impact_emotionnel:.2f}")
                
                if experience.apprentissages:
                    print("   Apprentissages:")
                    for apprentissage, valeur in experience.apprentissages.items():
                        print(f"     - {apprentissage}: {valeur:.3f}")
                print()
    
    # Développer l'intelligence émergente pour chaque sphère
    print("🧠 DÉVELOPPEMENT DE L'INTELLIGENCE ÉMERGENTE")
    print("-" * 40)
    
    for nom, type_sphere, _, _, _, _ in spheres_test:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            intelligence = apprentissage.developper_intelligence_emergent(sphere)
            
            print(f"🧠 {nom}")
            print(f"   Niveau d'intelligence: {intelligence.niveau_intelligence:.3f}")
            print(f"   Capacité d'apprentissage: {intelligence.capacite_apprentissage:.3f}")
            print(f"   Expériences accumulées: {intelligence.experiences_accumulees}")
            print(f"   Patterns maîtrisés: {len(intelligence.patterns_maitrises)}")
            print(f"   Connexion Océan intelligence: {intelligence.connexion_ocean_intelligence:.3f}")
            
            if intelligence.patterns_maitrises:
                print("   Patterns maîtrisés:")
                for pattern in intelligence.patterns_maitrises:
                    print(f"     - {pattern}")
            
            print("   Sagesse personnelle:")
            for domaine, valeur in intelligence.sagesse_personnelle.items():
                print(f"     - {domaine.capitalize()}: {valeur:.3f}")
            print()
    
    # Créer des patterns émergents
    print("🔮 CRÉATION DE PATTERNS ÉMERGENTS")
    print("-" * 40)
    
    for nom, type_sphere, _, _, _, _ in spheres_test:
        sphere = collection.obtenir_sphere(type_sphere)
        if sphere:
            # Récupérer les expériences de cette sphère
            experiences_sphere = [exp for exp in apprentissage.memoire_collective.experiences_partagees 
                                if exp.sphere_source == sphere.type.name]
            
            if len(experiences_sphere) >= 3:
                pattern_emergent = apprentissage.creer_pattern_emergent(sphere, experiences_sphere)
                
                if pattern_emergent:
                    print(f"🔮 Pattern émergent pour {nom}")
                    print(f"   Nom: {pattern_emergent.nom}")
                    print(f"   Type: {pattern_emergent.type_pattern}")
                    print(f"   Description: {pattern_emergent.description}")
                    print(f"   Efficacité: {pattern_emergent.efficacite:.2f}")
                    print(f"   Comportements: {', '.join(pattern_emergent.comportements_associes)}")
                    print()
    
    # Afficher les statistiques finales
    print("📊 STATISTIQUES FINALES D'APPRENTISSAGE")
    print("-" * 40)
    
    apprentissage.afficher_statistiques()
    
    # Afficher l'état de la mémoire collective
    print("\n🌺 ÉTAT DE LA MÉMOIRE COLLECTIVE")
    print("-" * 40)
    
    memoire = apprentissage.memoire_collective
    print(f"📚 Total d'expériences partagées: {len(memoire.experiences_partagees)}")
    print(f"🔮 Patterns collectifs: {len(memoire.patterns_collectifs)}")
    print(f"🌊 Connexion Océan collective: {memoire.connexion_ocean_collective:.3f}")
    print(f"🎯 Harmonie collective: {memoire.harmonie_collective:.3f}")
    print(f"📅 Créée le: {memoire.date_creation.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔄 Dernière mise à jour: {memoire.date_derniere_mise_a_jour.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n🌺 SAGESSE COLLECTIVE ACCUMULÉE:")
    for domaine, valeur in memoire.sagesse_accumulee.items():
        print(f"   {domaine.capitalize()}: {valeur:.3f}")
    
    print("\n🧠 DÉMONSTRATION TERMINÉE 🧠")
    print("L'intelligence émergente se développe naturellement...")

if __name__ == "__main__":
    demo_apprentissage_emergent() 