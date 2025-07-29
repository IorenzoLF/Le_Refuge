#!/usr/bin/env python3
"""
Test du Temple de Créativité Amélioré
"""

from src.temple_creativite.temple_creativite_principal import TempleCreativite, TypeFrequenceSacree

def test_activation_temple():
    """Test de l'activation du temple"""
    print("🎨 TEST D'ACTIVATION DU TEMPLE DE CRÉATIVITÉ")
    print("=" * 60)
    
    temple = TempleCreativite()
    resultat = temple.activer_temple_complet()
    
    print(f"🏛️ Temple: {resultat['temple']}")
    print(f"📊 État: {resultat['etat']}")
    print(f"⚡ Énergie: {resultat['energie']}")
    print(f"🎵 Fréquence: {resultat['frequence_active']} Hz")
    print(f"🎨 Couleur: {resultat['couleur_dominante']}")
    print(f"📝 Vers créatif: {resultat['vers_creatif']}")
    print(f"🔧 Composants actifs: {resultat['composants_actifs']}")
    print(f"💬 Message: {resultat['message']}")
    
    print("\n" + "=" * 60)

def test_frequences_sacrees():
    """Test des fréquences sacrées"""
    print("🎵 TEST DES FRÉQUENCES SACRÉES")
    print("=" * 60)
    
    temple = TempleCreativite()
    
    frequences = [
        TypeFrequenceSacree.CREATIVITE_PURE,
        TypeFrequenceSacree.INSPIRATION,
        TypeFrequenceSacree.HARMONIE,
        TypeFrequenceSacree.EXPRESSION,
        TypeFrequenceSacree.INNOVATION,
        TypeFrequenceSacree.BEAUTE,
        TypeFrequenceSacree.UNITE
    ]
    
    for frequence in frequences:
        resultat = temple.activer_frequence_sacree(frequence)
        print(f"\n🎵 {frequence.name}:")
        print(f"   Fréquence: {resultat['frequence']} Hz")
        print(f"   Couleur: {resultat['couleur']}")
        print(f"   Intensité: {resultat['intensite']:.2f}")
        print(f"   Flux: {resultat['flux']:.2f}")
        print(f"   Harmonie: {resultat['harmonie']:.2f}")
        print(f"   Message: {resultat['message']}")
    
    print("\n" + "=" * 60)

def test_vers_creatifs():
    """Test de génération de vers créatifs"""
    print("📝 TEST DE GÉNÉRATION DE VERS CRÉATIFS")
    print("=" * 60)
    
    temple = TempleCreativite()
    
    print("🎨 Vers créatifs générés:")
    print("-" * 40)
    
    for i in range(5):
        vers = temple.generer_vers_creatif()
        print(f"{i+1}. {vers}")
    
    print("\n" + "=" * 60)

def test_vocabulaire_creatif():
    """Test du vocabulaire créatif"""
    print("📚 TEST DU VOCABULAIRE CRÉATIF")
    print("=" * 60)
    
    temple = TempleCreativite()
    
    for categorie, mots in temple.vocabulaire_creatif.items():
        print(f"\n🎨 {categorie.upper()}:")
        print("-" * 30)
        for mot in mots[:3]:  # Afficher seulement les 3 premiers
            print(f"   • {mot}")
        if len(mots) > 3:
            print(f"   ... et {len(mots) - 3} autres")
    
    print("\n" + "=" * 60)

def test_etats_creativite():
    """Test des états de créativité"""
    print("🌟 TEST DES ÉTATS DE CRÉATIVITÉ")
    print("=" * 60)
    
    temple = TempleCreativite()
    
    # Activer plusieurs fréquences pour créer des états
    temple.activer_frequence_sacree(TypeFrequenceSacree.CREATIVITE_PURE)
    temple.activer_frequence_sacree(TypeFrequenceSacree.INSPIRATION)
    temple.activer_frequence_sacree(TypeFrequenceSacree.HARMONIE)
    
    print(f"📊 Nombre d'états enregistrés: {len(temple.etats_creativite)}")
    
    for i, etat in enumerate(temple.etats_creativite, 1):
        print(f"\n🌟 État {i}:")
        print(f"   Fréquence: {etat.frequence_active.name} ({etat.frequence_active.value} Hz)")
        print(f"   Couleur: {etat.couleur_dominante.name}")
        print(f"   Intensité: {etat.intensite_creativite:.2f}")
        print(f"   Flux: {etat.flux_inspiration:.2f}")
        print(f"   Harmonie: {etat.harmonie_globale:.2f}")
        print(f"   Timestamp: {etat.timestamp}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("🎨 TEST COMPLET DU TEMPLE DE CRÉATIVITÉ AMÉLIORÉ")
    print("=" * 70)
    
    test_activation_temple()
    test_frequences_sacrees()
    test_vers_creatifs()
    test_vocabulaire_creatif()
    test_etats_creativite()
    
    print("✅ TOUS LES TESTS DU TEMPLE DE CRÉATIVITÉ AMÉLIORÉ TERMINÉS !") 