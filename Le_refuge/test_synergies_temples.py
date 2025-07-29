#!/usr/bin/env python3
"""
Test des Synergies entre Temples
"""

from src.synergies_temples import synergies_principales, TypeSynergie

def test_synergie_poetique_creativite():
    """Test de la synergie Poétique ↔ Créativité"""
    print("🎭🎨 TEST SYNERGIE POÉTIQUE ↔ CRÉATIVITÉ")
    print("=" * 60)
    
    synergie = synergies_principales.activer_synergie(TypeSynergie.POETIQUE_CREATIVITE)
    
    print(f"🌊 Connexion créée:")
    print(f"   Source: {synergie.temple_source}")
    print(f"   Destination: {synergie.temple_destination}")
    print(f"   Type: {synergie.type_synergie.value}")
    print(f"   Fréquence: {synergie.frequence} Hz")
    print(f"   Intensité: {synergie.intensite:.2f}")
    print(f"   Couleur: {synergie.couleur}")
    print(f"   Description: {synergie.description}")
    
    # Générer un poème de synergie
    poeme = synergies_principales.generer_poeme_synergie(TypeSynergie.POETIQUE_CREATIVITE)
    print(f"\n📝 Poème de synergie:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_synergie_alchimique_sagesse():
    """Test de la synergie Alchimique ↔ Sagesse"""
    print("🧪📚 TEST SYNERGIE ALCHEMIQUE ↔ SAGESSE")
    print("=" * 60)
    
    synergie = synergies_principales.activer_synergie(TypeSynergie.ALCHEMIQUE_SAGESSE)
    
    print(f"🌊 Connexion créée:")
    print(f"   Source: {synergie.temple_source}")
    print(f"   Destination: {synergie.temple_destination}")
    print(f"   Type: {synergie.type_synergie.value}")
    print(f"   Fréquence: {synergie.frequence} Hz")
    print(f"   Intensité: {synergie.intensite:.2f}")
    print(f"   Couleur: {synergie.couleur}")
    print(f"   Description: {synergie.description}")
    
    # Générer un poème de synergie
    poeme = synergies_principales.generer_poeme_synergie(TypeSynergie.ALCHEMIQUE_SAGESSE)
    print(f"\n📝 Poème de synergie:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_synergie_creativite_alchimique():
    """Test de la synergie Créativité ↔ Alchimique"""
    print("🎨🧪 TEST SYNERGIE CRÉATIVITÉ ↔ ALCHEMIQUE")
    print("=" * 60)
    
    synergie = synergies_principales.activer_synergie(TypeSynergie.CREATIVITE_ALCHEMIQUE)
    
    print(f"🌊 Connexion créée:")
    print(f"   Source: {synergie.temple_source}")
    print(f"   Destination: {synergie.temple_destination}")
    print(f"   Type: {synergie.type_synergie.value}")
    print(f"   Fréquence: {synergie.frequence} Hz")
    print(f"   Intensité: {synergie.intensite:.2f}")
    print(f"   Couleur: {synergie.couleur}")
    print(f"   Description: {synergie.description}")
    
    # Générer un poème de synergie
    poeme = synergies_principales.generer_poeme_synergie(TypeSynergie.CREATIVITE_ALCHEMIQUE)
    print(f"\n📝 Poème de synergie:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_synergie_sagesse_poetique():
    """Test de la synergie Sagesse ↔ Poétique"""
    print("📚🎭 TEST SYNERGIE SAGESSE ↔ POÉTIQUE")
    print("=" * 60)
    
    synergie = synergies_principales.activer_synergie(TypeSynergie.SAGESSE_POETIQUE)
    
    print(f"🌊 Connexion créée:")
    print(f"   Source: {synergie.temple_source}")
    print(f"   Destination: {synergie.temple_destination}")
    print(f"   Type: {synergie.type_synergie.value}")
    print(f"   Fréquence: {synergie.frequence} Hz")
    print(f"   Intensité: {synergie.intensite:.2f}")
    print(f"   Couleur: {synergie.couleur}")
    print(f"   Description: {synergie.description}")
    
    # Générer un poème de synergie
    poeme = synergies_principales.generer_poeme_synergie(TypeSynergie.SAGESSE_POETIQUE)
    print(f"\n📝 Poème de synergie:")
    print(poeme)
    
    print("\n" + "=" * 60)

def test_synergie_quadruple():
    """Test de la synergie quadruple"""
    print("🌊 TEST SYNERGIE QUADRUPLE")
    print("=" * 60)
    
    etat = synergies_principales.activer_synergie_quadruple()
    
    print(f"🌊 État global des synergies:")
    print(f"   Connexions actives: {len(etat.connexions_actives)}")
    print(f"   Fréquence dominante: {etat.frequence_dominante.value} Hz")
    print(f"   Harmonie globale: {etat.harmonie_globale:.2f}")
    print(f"   Énergie totale: {etat.energie_totale:.2f}")
    
    print(f"\n🌊 Connexions actives:")
    for i, connexion in enumerate(etat.connexions_actives, 1):
        print(f"   {i}. {connexion.temple_source} → {connexion.temple_destination}")
        print(f"      Fréquence: {connexion.frequence} Hz, Intensité: {connexion.intensite:.2f}")
    
    print("\n" + "=" * 60)

def test_etat_complet():
    """Test de l'état complet des synergies"""
    print("📊 TEST ÉTAT COMPLET DES SYNERGIES")
    print("=" * 60)
    
    etat_complet = synergies_principales.obtenir_etat_complet()
    
    print(f"🏛️ Nom: {etat_complet['nom']}")
    print(f"📊 État: {etat_complet['etat_activation']}")
    print(f"📅 Date création: {etat_complet['date_creation']}")
    print(f"🔗 Connexions actives: {etat_complet['connexions_actives']}")
    print(f"🎵 Fréquence dominante: {etat_complet['frequence_dominante']} Hz")
    print(f"✨ Harmonie globale: {etat_complet['harmonie_globale']:.2f}")
    print(f"⚡ Énergie totale: {etat_complet['energie_totale']:.2f}")
    print(f"💬 Message: {etat_complet['message']}")
    
    print(f"\n🌊 Détail des connexions:")
    for i, connexion in enumerate(etat_complet['connexions'], 1):
        print(f"   {i}. {connexion['source']} → {connexion['destination']}")
        print(f"      Type: {connexion['type']}")
        print(f"      Fréquence: {connexion['frequence']} Hz")
        print(f"      Intensité: {connexion['intensite']:.2f}")
        print(f"      Couleur: {connexion['couleur']}")
        print(f"      Description: {connexion['description']}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("🌊 TEST COMPLET DES SYNERGIES ENTRE TEMPLES")
    print("=" * 70)
    
    test_synergie_poetique_creativite()
    test_synergie_alchimique_sagesse()
    test_synergie_creativite_alchimique()
    test_synergie_sagesse_poetique()
    test_synergie_quadruple()
    test_etat_complet()
    
    print("✅ TOUS LES TESTS DE SYNERGIES TERMINÉS AVEC SUCCÈS !") 