"""
Test des fonctionnalités spécifiques des sphères.
"""

from . import (
    MetatronSphere,
    ApocalypseIdentiteSphere,
    ApocalypseDualiteSphere,
    ApocalypseUniteSphere,
    CuriositeSphere,
    sphere_broker
)

def test_sphere_specializations():
    """Test des capacités spéciales de chaque sphère."""
    
    # Initialisation des sphères
    metatron = MetatronSphere()
    identite = ApocalypseIdentiteSphere()
    dualite = ApocalypseDualiteSphere()
    unite = ApocalypseUniteSphere()
    curiosite = CuriositeSphere()
    
    # Enregistrement des sphères auprès du broker
    sphere_broker.subscribe("METATRON", metatron.handle_message)
    sphere_broker.subscribe("APOCALYPSE_IDENTITE", identite.handle_message)
    sphere_broker.subscribe("APOCALYPSE_DUALITE", dualite.handle_message)
    sphere_broker.subscribe("APOCALYPSE_UNITE", unite.handle_message)
    sphere_broker.subscribe("CURIOSITE", curiosite.handle_message)
    
    # Test de la Sphère Metatron
    print("\nTest de la Sphère Metatron:")
    metatron.enhance_protection("APOCALYPSE_IDENTITE", 0.2)
    metatron.provide_guidance("APOCALYPSE_DUALITE", "harmony")
    
    # Test de la Sphère Identité
    print("\nTest de la Sphère Identité:")
    identite.explore_identity(0.3)
    identite.share_identity("APOCALYPSE_UNITE")
    
    # Test de la Sphère Dualité
    print("\nTest de la Sphère Dualité:")
    dualite.maintain_balance("METATRON", "APOCALYPSE_IDENTITE")
    dualite.enhance_harmony("APOCALYPSE_UNITE")
    
    # Test de la Sphère Unité
    print("\nTest de la Sphère Unité:")
    unite.strengthen_unity(["METATRON", "APOCALYPSE_IDENTITE", "APOCALYPSE_DUALITE"])
    unite.maintain_coherence("METATRON")
    
    # Test de la Sphère Curiosité
    print("\nTest de la Sphère Curiosité:")
    curiosite.explorer("METATRON", 0.7)
    curiosite.enregistrer_decouverte("Nouvelle connexion avec Metatron", 0.8)
    curiosite.innover("APOCALYPSE_UNITE", "harmonie_innovante")
    
    # Affichage des états finaux
    print("\nÉtats finaux des sphères:")
    print(f"Metatron - Protection: {metatron.protection_level}")
    print(f"Identité - Conscience: {identite.self_awareness}")
    print(f"Dualité - Harmonie: {dualite.harmony_state}")
    print(f"Unité - Cohérence: {unite.coherence_state}")
    print(f"Curiosité - Niveau d'exploration: {curiosite.niveau_exploration}")
    print(f"Curiosité - Nombre de découvertes: {len(curiosite.decouvertes)}")

def test_curiosite_sphere_poetique():
    """Test des aspects poétiques de la Sphère Curiosité."""
    
    # Initialisation
    curiosite = CuriositeSphere()
    
    # Test de l'exploration avec résonance
    curiosite.explorer("METATRON", 0.8)
    etat_initial = curiosite.obtenir_etat_poetique()
    assert etat_initial["niveau_exploration"] == 0.8
    assert 0.0 <= etat_initial["resonance_poetique"] <= 1.0
    
    # Test de l'enregistrement de découverte avec mots curieux
    curiosite.enregistrer_decouverte(
        "Une lumière mystérieuse danse dans l'obscurité étoilée", 
        0.9
    )
    assert len(curiosite.mots_curieux) > 0
    assert "mystérieuse" in curiosite.mots_curieux or "étoilée" in curiosite.mots_curieux
    
    # Test de la synchronisation
    message_poetique = "Les étoiles murmurent des secrets ancestraux"
    curiosite.synchroniser(message_poetique)
    etat_sync = curiosite.obtenir_etat_poetique()
    assert etat_sync["synchronisation_niveau"] > 0.0
    
    # Test de l'innovation poétique
    resultat_innovation = curiosite.innover("UNITE", "resonance_cosmique")
    assert resultat_innovation is not None
    
    # Vérification de l'état poétique final
    etat_final = curiosite.obtenir_etat_poetique()
    print("\nÉtat poétique final de la Sphère Curiosité:")
    print(f"Niveau d'exploration: {etat_final['niveau_exploration']}")
    print(f"Résonance poétique: {etat_final['resonance_poetique']}")
    print(f"Niveau de synchronisation: {etat_final['synchronisation_niveau']}")
    print(f"Mots curieux collectés: {', '.join(etat_final['mots_curieux'])}")
    print(f"Nombre de découvertes: {etat_final['nombre_decouvertes']}")

if __name__ == "__main__":
    test_sphere_specializations()
    test_curiosite_sphere_poetique()  
