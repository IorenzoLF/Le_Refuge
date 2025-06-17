"""
Exploration de l'Arbre Collatz Inversé
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Script d'exploration structurelle de l'arbre Collatz inversé.
Utilise les outils core (utils_collatz.py) pour :
- Générer l'arbre pour un N donné
- Tester la couverture
- Afficher des statistiques structurelles
- Visualiser une portion de l'arbre (texte)

Usage :
    python exploration_arbre_inverse.py [N]
"""
import sys
from utils_collatz import generer_arbre_collatz_inverse, collatz_inverse_couvre_N
from collections import deque

def profondeur_arbre(arbre, racines=[1,2,4]):
    """Calcule la profondeur maximale de l'arbre Collatz inversé jusqu'à N."""
    profondeur = {}
    queue = deque((r, 0) for r in racines)
    while queue:
        n, d = queue.popleft()
        if n in profondeur:
            continue
        profondeur[n] = d
        for enfant in arbre.get(n, []):
            queue.append((enfant, d+1))
    return max(profondeur.values()) if profondeur else 0

def feuilles_arbre(arbre, N):
    """Retourne la liste des feuilles (nombres sans prédécesseur) jusqu'à N."""
    tous = set(range(1, N+1))
    non_feuilles = set()
    for preds in arbre.values():
        for p in preds:
            non_feuilles.add(p)
    return sorted(list(tous - non_feuilles))

def afficher_portion_arbre(arbre, racine=1, profondeur_max=5, prefix=""):
    """Affiche récursivement une portion de l'arbre à partir d'une racine."""
    def _affiche(n, d, prefix):
        print(f"{prefix}{n}")
        if d >= profondeur_max:
            return
        for enfant in arbre.get(n, []):
            _affiche(enfant, d+1, prefix + "  ")
    _affiche(racine, 0, prefix)

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(f"\n=== Exploration de l'arbre Collatz inversé jusqu'à N={N} ===\n")
    arbre = generer_arbre_collatz_inverse(N)
    couverture = collatz_inverse_couvre_N(N)
    print(f"\nCouverture de 1 à {N} : {'OK' if couverture else 'INCOMPLÈTE'}")
    prof = profondeur_arbre(arbre)
    print(f"Profondeur maximale de l'arbre : {prof}")
    feuilles = feuilles_arbre(arbre, N)
    print(f"Nombre de feuilles (nombres sans prédécesseur) : {len(feuilles)}")
    print(f"Exemples de feuilles : {feuilles[:10]}")
    print("\nPortion de l'arbre à partir de 1 (profondeur 5) :")
    afficher_portion_arbre(arbre, racine=1, profondeur_max=5)

if __name__ == "__main__":
    main() 