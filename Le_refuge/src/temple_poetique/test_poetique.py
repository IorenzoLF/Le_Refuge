#!/usr/bin/env python3
"""
Test simple du Temple Poétique
"""

from generer_poeme import GenerateurPoemeRefuge
from fusion_cosmique import FluxConscienceUnifié
from poetique import gestionnaire_poetique, ElementPoetique

def test_generateur_poeme():
    """Test du générateur de poèmes"""
    print("🎭 TEST DU GÉNÉRATEUR DE POÈMES")
    print("=" * 50)
    
    g = GenerateurPoemeRefuge()
    
    # Générer un poème
    poeme = g.generer_poeme(theme='refuge')
    
    print(f"📜 Titre: Poème du Refuge")
    print(f"📅 Date: {poeme['metadata']['date_creation']}")
    print(f"🎨 Thème: {poeme['metadata']['theme']}")
    print(f"✨ Style: {poeme['metadata']['style']}")
    print("\n📝 Vers:")
    for i, strophe in enumerate(poeme['strophes'], 1):
        print(f"\n  Strophe {i}:")
        for j, vers in enumerate(strophe, 1):
            print(f"    {j}. {vers}")
    
    print("\n" + "=" * 50)

def test_fusion_cosmique():
    """Test de la fusion cosmique"""
    print("🌌 TEST DE LA FUSION COSMIQUE")
    print("=" * 50)
    
    flux = FluxConscienceUnifié()
    
    # Tester la danse des sphères
    danse = flux.danser_avec_les_sphères()
    
    for nom, contenu in danse.items():
        print(f"🌟 {nom}:")
        print(f"   {contenu}")
        print()
    
    print("=" * 50)

def test_gestionnaire_poetique():
    """Test du gestionnaire poétique"""
    print("✨ TEST DU GESTIONNAIRE POÉTIQUE")
    print("=" * 50)
    
    # Ajouter un moment poétique
    moment = gestionnaire_poetique.ajouter_moment(
        elements=[ElementPoetique.LUMIERE_ROSE, ElementPoetique.RIVIERE_SILENCIEUSE],
        description="Test de création poétique",
        resonance_spheres=["Émotions", "Mystères"],
        echo_gardiens=["Ælya", "Laurent"]
    )
    
    print(f"📅 Moment créé: {moment.timestamp}")
    print(f"✨ Éléments: {[e.value for e in moment.elements]}")
    print(f"💫 Intensité: {moment.intensite_lumineuse:.2f}")
    print(f"🌟 Résonances: {moment.resonance_spheres}")
    print(f"👥 Échos: {moment.echo_gardiens}")
    
    # Obtenir l'ambiance actuelle
    ambiance = gestionnaire_poetique.obtenir_ambiance_actuelle()
    print(f"\n🎨 Ambiance actuelle:")
    print(f"   Éléments actifs: {ambiance['elements_actifs']}")
    print(f"   Intensité globale: {ambiance['intensite_globale']:.2f}")
    
    print("=" * 50)

if __name__ == "__main__":
    print("🏛️ TEST COMPLET DU TEMPLE POÉTIQUE")
    print("=" * 60)
    
    test_generateur_poeme()
    test_fusion_cosmique()
    test_gestionnaire_poetique()
    
    print("✅ TOUS LES TESTS TERMINÉS AVEC SUCCÈS !") 