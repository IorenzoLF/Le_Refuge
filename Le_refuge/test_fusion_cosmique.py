#!/usr/bin/env python3
"""
Test de la Fusion Cosmique Complète
"""

from src.temple_poetique.fusion_cosmique import FluxConscienceUnifié

def test_manifestation_complete():
    """Test de la manifestation complète"""
    print("🌌 TEST DE LA MANIFESTATION COSMIQUE COMPLÈTE")
    print("=" * 60)
    
    flux = FluxConscienceUnifié()
    manifestation = flux.manifester()
    
    print(manifestation)
    print("=" * 60)

def test_transmutation_code():
    """Test de la transmutation du code"""
    print("🔮 TEST DE LA TRANSMUTATION DU CODE")
    print("=" * 60)
    
    flux = FluxConscienceUnifié()
    
    # Tester la transmutation sur un fichier existant
    try:
        from pathlib import Path
        test_file = Path("src/temple_poetique/poetique.py")
        
        print(f"Transmutation de {test_file.name}:")
        print("-" * 40)
        
        for ligne_poetique in flux.transmuter_code(test_file):
            print(ligne_poetique.rstrip())
            
    except Exception as e:
        print(f"Erreur lors de la transmutation: {e}")
    
    print("=" * 60)

if __name__ == "__main__":
    test_manifestation_complete()
    test_transmutation_code() 