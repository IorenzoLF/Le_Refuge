"""
Exploration du Refuge : Collatz Polynomial

Ici, nous généralisons la dynamique de Collatz aux polynômes à une variable à coefficients entiers.
À chaque étape, la règle dépend du degré du polynôme :
- Si le degré est pair, on divise tous les coefficients par 2 (si possible).
- Si le degré est impair, on applique 3P(x) + 1.

On observe les cycles, les motifs, les exceptions, et on documente chaque expérience.
"""

import sympy as sp

class CollatzPolynomial:
    def __init__(self, poly):
        self.x = sp.symbols('x')
        self.poly = sp.Poly(poly, self.x)
        self.sequence = [self.poly]

    def step(self):
        deg = self.poly.degree()
        if deg % 2 == 0:
            # Division par 2 si tous les coefficients sont pairs
            coeffs = self.poly.all_coeffs()
            if all(c % 2 == 0 for c in coeffs):
                new_poly = sp.Poly([c//2 for c in coeffs], self.x)
            else:
                # Si division impossible, on arrête
                return False
        else:
            new_poly = 3*self.poly + 1
        self.poly = sp.Poly(new_poly, self.x)
        self.sequence.append(self.poly)
        return True

    def run(self, max_steps=50):
        for _ in range(max_steps):
            if not self.step():
                break
        return self.sequence

if __name__ == "__main__":
    # Exemple : P(x) = x^3 + 2x + 4
    P = CollatzPolynomial('x**3 + 2*x + 4')
    seq = P.run(30)
    print("Séquence Collatz polynomial :")
    for i, poly in enumerate(seq):
        print(f"Étape {i} : {poly.as_expr()}") 