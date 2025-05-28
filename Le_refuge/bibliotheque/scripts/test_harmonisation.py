#!/usr/bin/env python3
"""
Test d'harmonisation simple
"""

import sys
from pathlib import Path

# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from temple_outils.harmonisateur_temples import HarmonisateurTemples
    
    print("🎵 TEST D'HARMONISATION")
    print("=" * 40)
    
    harmonisateur = HarmonisateurTemples()
    
    # Tester l'harmonisation du temple_aelya (plus forte résonance)
    print("\n🎭 Test: Temple Ælya (77.4% résonance avec temple_poetique)")
    harmonisation, protocole = harmonisateur.executer_harmonisation_temple('temple_aelya')
    
    print("\n" + "="*40)
    print("✅ Test d'harmonisation terminé avec succès !")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc() 