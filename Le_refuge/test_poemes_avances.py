#!/usr/bin/env python3
"""
Test de Génération de Poèmes Avancés
"""

from src.temple_poetique.generer_poeme import GenerateurPoemeRefuge

def test_poemes_themes():
    """Test de poèmes avec différents thèmes"""
    print("🎭 TEST DE POÈMES AVEC DIFFÉRENTS THÈMES")
    print("=" * 60)
    
    g = GenerateurPoemeRefuge()
    
    themes = ['refuge', 'conscience', 'amour', 'mystere', 'harmonie']
    
    for theme in themes:
        print(f"\n🌙 THÈME: {theme.upper()}")
        print("-" * 40)
        
        poeme = g.generer_poeme(theme=theme, nb_strophes=2)
        
        for i, strophe in enumerate(poeme['strophes'], 1):
            print(f"\n  Strophe {i}:")
            for j, vers in enumerate(strophe, 1):
                print(f"    {j}. {vers}")
    
    print("\n" + "=" * 60)

def test_structures_personnalisees():
    """Test avec des schémas de rimes personnalisés"""
    print("🎨 TEST DE STRUCTURES PERSONNALISÉES")
    print("=" * 60)
    
    g = GenerateurPoemeRefuge()
    
    # Schémas personnalisés
    schemas = [
        ["A", "B", "A"],           # Tercet
        ["A", "B", "B", "A"],      # Quatrain ABBA
        ["A", "A", "B", "B"],      # Quatrain AABB
        ["A", "B", "C", "B"],      # Quatrain ABCB
        ["A", "B", "A", "B", "A"]  # Quintain
    ]
    
    print("📝 Poème avec structures personnalisées:")
    print("-" * 40)
    
    poeme = g.generer_poeme(schemas_personnalises=schemas, theme='refuge')
    
    for i, strophe in enumerate(poeme['strophes'], 1):
        print(f"\n  Strophe {i} (Schéma {schemas[i-1]}):")
        for j, vers in enumerate(strophe, 1):
            print(f"    {j}. {vers}")
    
    print("\n" + "=" * 60)

def test_collection_poemes():
    """Test de génération d'une collection de poèmes"""
    print("📚 TEST DE COLLECTION DE POÈMES")
    print("=" * 60)
    
    g = GenerateurPoemeRefuge()
    
    collection = g.generer_collection(nb_poemes=3, theme='refuge')
    
    for i, poeme in enumerate(collection, 1):
        print(f"\n📜 POÈME {i}:")
        print("-" * 30)
        
        for j, strophe in enumerate(poeme['strophes'], 1):
            print(f"\n  Strophe {j}:")
            for k, vers in enumerate(strophe, 1):
                print(f"    {k}. {vers}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_poemes_themes()
    test_structures_personnalisees()
    test_collection_poemes()
    
    print("✅ TOUS LES TESTS DE POÉSIE AVANCÉE TERMINÉS !") 