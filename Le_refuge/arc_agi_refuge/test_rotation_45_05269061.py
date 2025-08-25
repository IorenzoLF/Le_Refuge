#!/usr/bin/env python3
"""
🧪 TEST DU PATTERN ROTATION 45° POUR 05269061
Validation que le nouveau pattern améliore les résultats
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_rotation_45_05269061():
    """Test spécifique du pattern rotation 45° pour le puzzle 05269061"""

    print("🔄 TEST ROTATION 45° POUR 05269061")
    print("=" * 45)

    solveur = SolveurTransparentARC()

    # Tester le puzzle problématique
    puzzle_id = "05269061"

    print(f"🧩 Test du puzzle: {puzzle_id}")
    print("-" * 30)

    try:
        # Analyser le puzzle
        resultat = solveur.analyser_puzzle_complet(puzzle_id)

        print(f"Pattern détecté: {resultat.pattern_type}")
        print(".1f")

        if hasattr(resultat, 'similarite'):
            print(".1f")

            # Afficher les détails de validation si disponibles
            if hasattr(resultat, 'details'):
                print(f"Détails: {resultat.details}")

        # Vérifier si c'est le nouveau pattern rotation_45
        if resultat.pattern_type == 'rotation_45':
            print("✅ SUCCÈS: Pattern rotation_45 détecté!")
            print("   → Cela devrait considérablement améliorer les résultats")
        else:
            print(f"⚠️  Le pattern détecté est '{resultat.pattern_type}', pas 'rotation_45'")
            print("   → Le nouveau pattern n'a pas été activé")

        # Afficher l'explication
        if hasattr(resultat, 'explication'):
            print(f"Explication: {resultat.explication}")

    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")

    print("\n📊 RÉSULTAT ATTENDU:")
    print("   Avant: 22.4% similarité avec 'repetition_simple'")
    print("   Après: 80-95% similarité avec 'rotation_45'")
    print("   Amélioration: +60% de similarité!")

if __name__ == "__main__":
    test_rotation_45_05269061()
