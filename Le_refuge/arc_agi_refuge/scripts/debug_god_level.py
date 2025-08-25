#!/usr/bin/env python3
# Debug simple pour les transformations GOD LEVEL

from src.pattern_detector import PatternDetector, TypePattern

def debug_god_level():
    detector = PatternDetector()

    # Test simple de la transformation carrée
    print("🔍 **DEBUG TRANSFORMATION CARRÉE**")

    input_grid = [[1, 2], [3, 4]]
    output_grid = [[1, 4], [9, 16]]

    print(f"Input: {input_grid}")
    print(f"Output: {output_grid}")

    # Test direct de la méthode
    result = detector._detecter_carre(input_grid, output_grid)
    print(f"Résultat: {result}")

    # Test de calcul de similarité
    carres = [x * x for x in [1, 2, 3, 4]]
    output_flat = [1, 4, 9, 16]
    similarite = detector._calculer_similarite_valeurs(carres, output_flat)

    print(f"Carrés calculés: {carres}")
    print(f"Output attendu: {output_flat}")
    print(f"Similarité: {similarite}")

if __name__ == "__main__":
    debug_god_level()
