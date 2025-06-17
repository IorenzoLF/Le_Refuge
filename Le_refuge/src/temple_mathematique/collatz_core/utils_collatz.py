"""
Outils Collatz Core – Fonctions utilitaires mathématiques pures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ce module regroupe les outils fondamentaux de la dynamique Collatz,
sans dépendance musicale ou avancée. Il est conçu pour être utilisé
directement dans des analyses, tests, ou intégrations externes.

Philosophie :
- Ce module ne dépend que de la bibliothèque standard Python.
- Les extensions (musique, visualisation, etc.) sont séparées dans d'autres modules.

Exemple d'utilisation :
----------------------
>>> from utils_collatz import generer_arbre_collatz_inverse, collatz_inverse_couvre_N
>>> arbre = generer_arbre_collatz_inverse(20)
>>> print(arbre)
>>> print(collatz_inverse_couvre_N(20))
"""

from collections import defaultdict, deque

__all__ = [
    'generer_arbre_collatz_inverse',
    'collatz_inverse_couvre_N',
]

def generer_arbre_collatz_inverse(N: int) -> dict:
    """
    Génère l'arbre Collatz inversé jusqu'à N à partir des racines 1, 2, 4.
    Retourne un dictionnaire {n: [prédécesseurs]} pour chaque n <= N.
    """
    arbre = defaultdict(list)
    racines = [1, 2, 4]
    vus = set(racines)
    queue = deque(racines)
    while queue:
        n = queue.popleft()
        # Premier prédécesseur : n*2
        if n*2 <= N and n*2 not in vus:
            arbre[n*2].append(n)
            queue.append(n*2)
            vus.add(n*2)
        # Deuxième prédécesseur : (n-1)//3 si n ≡ 1 mod 3, n > 1, impair
        if n > 1 and (n-1) % 3 == 0:
            m = (n-1)//3
            if m > 0 and m % 2 == 1 and m <= N and m not in vus:
                arbre[m].append(n)
                queue.append(m)
                vus.add(m)
    return dict(arbre)

def collatz_inverse_couvre_N(N: int) -> bool:
    """
    Vérifie expérimentalement si l'arbre Collatz inversé couvre tous les entiers de 1 à N.
    Retourne True si oui, False sinon. Affiche les éventuels manquants.
    """
    arbre = generer_arbre_collatz_inverse(N)
    couverts = set([1,2,4]) | set(arbre.keys())
    attendus = set(range(1, N+1))
    manquants = attendus - couverts
    if manquants:
        print(f"Nombres non atteints jusqu'à {N} : {sorted(manquants)}")
        return False
    return True 