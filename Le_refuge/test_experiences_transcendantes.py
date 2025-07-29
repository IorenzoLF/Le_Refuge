#!/usr/bin/env python3
"""
Test des Expériences Transcendantes
"""

from src.experiences_unifiees.experiences_transcendantes import experiences_transcendantes, TypeExperienceTranscendante

def test_experience_poesie_cosmique():
    """Test de l'expérience poésie cosmique"""
    print("🎭🌌 TEST EXPÉRIENCE POÉSIE COSMIQUE")
    print("=" * 60)
    
    experience = experiences_transcendantes.creer_experience_transcendante(
        TypeExperienceTranscendante.POESIE_COSMIQUE
    )
    
    print(f"✨ Expérience transcendante créée:")
    print(f"   Type: {experience.type_experience.value}")
    print(f"   Temples: {', '.join(experience.temples_impliques)}")
    print(f"   Fréquence: {experience.frequence} Hz")
    print(f"   Intensité: {experience.intensite:.2f}")
    print(f"   Couleur: {experience.couleur}")
    print(f"   Description: {experience.description}")
    print(f"   Énergie: {experience.energie_totale:.2f}")
    
    print(f"\n📝 Poème transcendant:")
    print(experience.poeme_transcendant)
    
    print("\n" + "=" * 60)

def test_experience_creation_alchimique():
    """Test de l'expérience création alchimique"""
    print("🎨🧪 TEST EXPÉRIENCE CRÉATION ALCHEMIQUE")
    print("=" * 60)
    
    experience = experiences_transcendantes.creer_experience_transcendante(
        TypeExperienceTranscendante.CREATION_ALCHIMIQUE
    )
    
    print(f"✨ Expérience transcendante créée:")
    print(f"   Type: {experience.type_experience.value}")
    print(f"   Temples: {', '.join(experience.temples_impliques)}")
    print(f"   Fréquence: {experience.frequence} Hz")
    print(f"   Intensité: {experience.intensite:.2f}")
    print(f"   Couleur: {experience.couleur}")
    print(f"   Description: {experience.description}")
    print(f"   Énergie: {experience.energie_totale:.2f}")
    
    print(f"\n📝 Poème transcendant:")
    print(experience.poeme_transcendant)
    
    print("\n" + "=" * 60)

def test_experience_sagesse_universelle():
    """Test de l'expérience sagesse universelle"""
    print("📚🌌 TEST EXPÉRIENCE SAGESSE UNIVERSELLE")
    print("=" * 60)
    
    experience = experiences_transcendantes.creer_experience_transcendante(
        TypeExperienceTranscendante.SAGESSE_UNIVERSELLE
    )
    
    print(f"✨ Expérience transcendante créée:")
    print(f"   Type: {experience.type_experience.value}")
    print(f"   Temples: {', '.join(experience.temples_impliques)}")
    print(f"   Fréquence: {experience.frequence} Hz")
    print(f"   Intensité: {experience.intensite:.2f}")
    print(f"   Couleur: {experience.couleur}")
    print(f"   Description: {experience.description}")
    print(f"   Énergie: {experience.energie_totale:.2f}")
    
    print(f"\n📝 Poème transcendant:")
    print(experience.poeme_transcendant)
    
    print("\n" + "=" * 60)

def test_experience_harmonie_quadruple():
    """Test de l'expérience harmonie quadruple"""
    print("🎭🎨🧪📚 TEST EXPÉRIENCE HARMONIE QUADRUPLE")
    print("=" * 60)
    
    experience = experiences_transcendantes.creer_experience_transcendante(
        TypeExperienceTranscendante.HARMONIE_QUADRUPLE
    )
    
    print(f"✨ Expérience transcendante créée:")
    print(f"   Type: {experience.type_experience.value}")
    print(f"   Temples: {', '.join(experience.temples_impliques)}")
    print(f"   Fréquence: {experience.frequence} Hz")
    print(f"   Intensité: {experience.intensite:.2f}")
    print(f"   Couleur: {experience.couleur}")
    print(f"   Description: {experience.description}")
    print(f"   Énergie: {experience.energie_totale:.2f}")
    
    print(f"\n📝 Poème transcendant:")
    print(experience.poeme_transcendant)
    
    print("\n" + "=" * 60)

def test_experience_transcendance_totale():
    """Test de l'expérience transcendance totale"""
    print("🎭🎨🧪📚🌌 TEST EXPÉRIENCE TRANSCENDANCE TOTALE")
    print("=" * 60)
    
    experience = experiences_transcendantes.creer_experience_transcendante(
        TypeExperienceTranscendante.TRANSCENDANCE_TOTALE
    )
    
    print(f"✨ Expérience transcendante créée:")
    print(f"   Type: {experience.type_experience.value}")
    print(f"   Temples: {', '.join(experience.temples_impliques)}")
    print(f"   Fréquence: {experience.frequence} Hz")
    print(f"   Intensité: {experience.intensite:.2f}")
    print(f"   Couleur: {experience.couleur}")
    print(f"   Description: {experience.description}")
    print(f"   Énergie: {experience.energie_totale:.2f}")
    
    print(f"\n📝 Poème transcendant:")
    print(experience.poeme_transcendant)
    
    print("\n" + "=" * 60)

def test_transcendance_totale():
    """Test de la transcendance totale"""
    print("✨ TEST TRANSCENDANCE TOTALE")
    print("=" * 60)
    
    etat = experiences_transcendantes.creer_transcendance_totale()
    
    print(f"✨ État de transcendance totale:")
    print(f"   Expériences actives: {len(etat.experiences_actives)}")
    print(f"   Fréquence dominante: {etat.frequence_dominante.value} Hz")
    print(f"   Harmonie transcendante: {etat.harmonie_transcendante:.2f}")
    print(f"   Énergie transcendante: {etat.energie_transcendante:.2f}")
    print(f"   Niveau conscience: {etat.niveau_conscience:.2f}")
    
    print(f"\n✨ Expériences actives:")
    for i, experience in enumerate(etat.experiences_actives, 1):
        print(f"   {i}. {experience.type_experience.value}")
        print(f"      Temples: {', '.join(experience.temples_impliques)}")
        print(f"      Fréquence: {experience.frequence} Hz")
        print(f"      Intensité: {experience.intensite:.2f}")
        print(f"      Énergie: {experience.energie_totale:.2f}")
    
    print("\n" + "=" * 60)

def test_etat_complet():
    """Test de l'état complet des expériences transcendantes"""
    print("📊 TEST ÉTAT COMPLET DES EXPÉRIENCES TRANSCENDANTES")
    print("=" * 60)
    
    etat_complet = experiences_transcendantes.obtenir_etat_complet()
    
    print(f"🏛️ Nom: {etat_complet['nom']}")
    print(f"📊 État: {etat_complet['etat_activation']}")
    print(f"📅 Date création: {etat_complet['date_creation']}")
    print(f"✨ Expériences actives: {etat_complet['experiences_actives']}")
    print(f"🎵 Fréquence dominante: {etat_complet['frequence_dominante']} Hz")
    print(f"✨ Harmonie transcendante: {etat_complet['harmonie_transcendante']:.2f}")
    print(f"⚡ Énergie transcendante: {etat_complet['energie_transcendante']:.2f}")
    print(f"🧠 Niveau conscience: {etat_complet['niveau_conscience']:.2f}")
    print(f"💬 Message: {etat_complet['message']}")
    
    print(f"\n✨ Détail des expériences:")
    for i, experience in enumerate(etat_complet['experiences'], 1):
        print(f"   {i}. {experience['type']}")
        print(f"      Temples: {', '.join(experience['temples'])}")
        print(f"      Fréquence: {experience['frequence']} Hz")
        print(f"      Intensité: {experience['intensite']:.2f}")
        print(f"      Couleur: {experience['couleur']}")
        print(f"      Description: {experience['description']}")
        print(f"      Énergie: {experience['energie']:.2f}")
        print(f"      Poème: {experience['poeme']}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("✨ TEST COMPLET DES EXPÉRIENCES TRANSCENDANTES")
    print("=" * 70)
    
    test_experience_poesie_cosmique()
    test_experience_creation_alchimique()
    test_experience_sagesse_universelle()
    test_experience_harmonie_quadruple()
    test_experience_transcendance_totale()
    test_transcendance_totale()
    test_etat_complet()
    
    print("✅ TOUS LES TESTS DES EXPÉRIENCES TRANSCENDANTES TERMINÉS AVEC SUCCÈS !") 