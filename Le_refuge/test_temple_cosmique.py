#!/usr/bin/env python3
"""
Test du Temple Cosmique
"""

from src.temple_cosmique import temple_cosmique, TypeConnexionCosmique

def test_connexion_etoile_polaire():
    """Test de connexion étoile polaire"""
    print("⭐ TEST CONNEXION ÉTOILE POLAIRE")
    print("=" * 60)
    
    connexion = temple_cosmique.creer_connexion_cosmique(
        "Temple Poétique", 
        "Temple Créativité", 
        TypeConnexionCosmique.ETOILE_POLAIRE
    )
    
    print(f"🌌 Connexion cosmique créée:")
    print(f"   Source: {connexion.temple_source}")
    print(f"   Destination: {connexion.temple_destination}")
    print(f"   Type: {connexion.type_connexion.value}")
    print(f"   Fréquence: {connexion.frequence} Hz")
    print(f"   Intensité: {connexion.intensite:.2f}")
    print(f"   Couleur: {connexion.couleur}")
    print(f"   Description: {connexion.description}")
    print(f"   Coordonnées: {connexion.coordonnees_cosmiques}")
    
    # Générer un poème cosmique
    poeme = temple_cosmique.generer_poeme_cosmique(TypeConnexionCosmique.ETOILE_POLAIRE)
    print(f"\n📝 Poème cosmique:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_connexion_voie_lactee():
    """Test de connexion voie lactée"""
    print("🌌 TEST CONNEXION VOIE LACTÉE")
    print("=" * 60)
    
    connexion = temple_cosmique.creer_connexion_cosmique(
        "Temple Alchimique", 
        "Temple Sagesse", 
        TypeConnexionCosmique.VOIE_LACTEE
    )
    
    print(f"🌌 Connexion cosmique créée:")
    print(f"   Source: {connexion.temple_source}")
    print(f"   Destination: {connexion.temple_destination}")
    print(f"   Type: {connexion.type_connexion.value}")
    print(f"   Fréquence: {connexion.frequence} Hz")
    print(f"   Intensité: {connexion.intensite:.2f}")
    print(f"   Couleur: {connexion.couleur}")
    print(f"   Description: {connexion.description}")
    print(f"   Coordonnées: {connexion.coordonnees_cosmiques}")
    
    # Générer un poème cosmique
    poeme = temple_cosmique.generer_poeme_cosmique(TypeConnexionCosmique.VOIE_LACTEE)
    print(f"\n📝 Poème cosmique:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_connexion_nebuleuse():
    """Test de connexion nébuleuse"""
    print("🌌 TEST CONNEXION NÉBULEUSE")
    print("=" * 60)
    
    connexion = temple_cosmique.creer_connexion_cosmique(
        "Temple Créativité", 
        "Temple Alchimique", 
        TypeConnexionCosmique.NEBULEUSE
    )
    
    print(f"🌌 Connexion cosmique créée:")
    print(f"   Source: {connexion.temple_source}")
    print(f"   Destination: {connexion.temple_destination}")
    print(f"   Type: {connexion.type_connexion.value}")
    print(f"   Fréquence: {connexion.frequence} Hz")
    print(f"   Intensité: {connexion.intensite:.2f}")
    print(f"   Couleur: {connexion.couleur}")
    print(f"   Description: {connexion.description}")
    print(f"   Coordonnées: {connexion.coordonnees_cosmiques}")
    
    # Générer un poème cosmique
    poeme = temple_cosmique.generer_poeme_cosmique(TypeConnexionCosmique.NEBULEUSE)
    print(f"\n📝 Poème cosmique:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_connexion_constellation():
    """Test de connexion constellation"""
    print("⭐ TEST CONNEXION CONSTELLATION")
    print("=" * 60)
    
    connexion = temple_cosmique.creer_connexion_cosmique(
        "Temple Sagesse", 
        "Temple Poétique", 
        TypeConnexionCosmique.CONSTELLATION
    )
    
    print(f"🌌 Connexion cosmique créée:")
    print(f"   Source: {connexion.temple_source}")
    print(f"   Destination: {connexion.temple_destination}")
    print(f"   Type: {connexion.type_connexion.value}")
    print(f"   Fréquence: {connexion.frequence} Hz")
    print(f"   Intensité: {connexion.intensite:.2f}")
    print(f"   Couleur: {connexion.couleur}")
    print(f"   Description: {connexion.description}")
    print(f"   Coordonnées: {connexion.coordonnees_cosmiques}")
    
    # Générer un poème cosmique
    poeme = temple_cosmique.generer_poeme_cosmique(TypeConnexionCosmique.CONSTELLATION)
    print(f"\n📝 Poème cosmique:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_connexion_portal_dimensionnel():
    """Test de connexion portal dimensionnel"""
    print("🌀 TEST CONNEXION PORTAL DIMENSIONNEL")
    print("=" * 60)
    
    connexion = temple_cosmique.creer_connexion_cosmique(
        "Temple Poétique", 
        "Temple Sagesse", 
        TypeConnexionCosmique.PORTAL_DIMENSIONNEL
    )
    
    print(f"🌌 Connexion cosmique créée:")
    print(f"   Source: {connexion.temple_source}")
    print(f"   Destination: {connexion.temple_destination}")
    print(f"   Type: {connexion.type_connexion.value}")
    print(f"   Fréquence: {connexion.frequence} Hz")
    print(f"   Intensité: {connexion.intensite:.2f}")
    print(f"   Couleur: {connexion.couleur}")
    print(f"   Description: {connexion.description}")
    print(f"   Coordonnées: {connexion.coordonnees_cosmiques}")
    
    # Générer un poème cosmique
    poeme = temple_cosmique.generer_poeme_cosmique(TypeConnexionCosmique.PORTAL_DIMENSIONNEL)
    print(f"\n📝 Poème cosmique:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_reseau_cosmique_complet():
    """Test du réseau cosmique complet"""
    print("🌌 TEST RÉSEAU COSMIQUE COMPLET")
    print("=" * 60)
    
    etat = temple_cosmique.creer_reseau_cosmique_complet()
    
    print(f"🌌 État du réseau cosmique:")
    print(f"   Connexions cosmiques: {len(etat.connexions_cosmiques)}")
    print(f"   Fréquence dominante: {etat.frequence_dominante.value} Hz")
    print(f"   Harmonie cosmique: {etat.harmonie_cosmique:.2f}")
    print(f"   Énergie cosmique: {etat.energie_cosmique:.2f}")
    print(f"   Temples connectés: {len(etat.temples_connectes)}")
    
    print(f"\n🌌 Temples connectés:")
    for temple in etat.temples_connectes:
        print(f"   - {temple}")
    
    print(f"\n🌌 Connexions cosmiques:")
    for i, connexion in enumerate(etat.connexions_cosmiques, 1):
        print(f"   {i}. {connexion.temple_source} → {connexion.temple_destination}")
        print(f"      Type: {connexion.type_connexion.value}")
        print(f"      Fréquence: {connexion.frequence} Hz")
        print(f"      Intensité: {connexion.intensite:.2f}")
    
    print("\n" + "=" * 60)

def test_etat_complet():
    """Test de l'état complet du temple cosmique"""
    print("📊 TEST ÉTAT COMPLET DU TEMPLE COSMIQUE")
    print("=" * 60)
    
    etat_complet = temple_cosmique.obtenir_etat_complet()
    
    print(f"🏛️ Nom: {etat_complet['nom']}")
    print(f"📊 État: {etat_complet['etat_activation']}")
    print(f"📅 Date création: {etat_complet['date_creation']}")
    print(f"🌌 Connexions cosmiques: {etat_complet['connexions_cosmiques']}")
    print(f"🎵 Fréquence dominante: {etat_complet['frequence_dominante']} Hz")
    print(f"✨ Harmonie cosmique: {etat_complet['harmonie_cosmique']:.2f}")
    print(f"⚡ Énergie cosmique: {etat_complet['energie_cosmique']:.2f}")
    print(f"🏛️ Temples connectés: {len(etat_complet['temples_connectes'])}")
    print(f"💬 Message: {etat_complet['message']}")
    
    print(f"\n🌌 Détail des connexions:")
    for i, connexion in enumerate(etat_complet['connexions'], 1):
        print(f"   {i}. {connexion['source']} → {connexion['destination']}")
        print(f"      Type: {connexion['type']}")
        print(f"      Fréquence: {connexion['frequence']} Hz")
        print(f"      Intensité: {connexion['intensite']:.2f}")
        print(f"      Couleur: {connexion['couleur']}")
        print(f"      Description: {connexion['description']}")
        print(f"      Coordonnées: {connexion['coordonnees']}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("🌌 TEST COMPLET DU TEMPLE COSMIQUE")
    print("=" * 70)
    
    test_connexion_etoile_polaire()
    test_connexion_voie_lactee()
    test_connexion_nebuleuse()
    test_connexion_constellation()
    test_connexion_portal_dimensionnel()
    test_reseau_cosmique_complet()
    test_etat_complet()
    
    print("✅ TOUS LES TESTS DU TEMPLE COSMIQUE TERMINÉS AVEC SUCCÈS !") 