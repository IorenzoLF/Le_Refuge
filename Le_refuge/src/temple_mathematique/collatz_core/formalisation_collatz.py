"""
Formalisation de la conjecture de Collatz – Version Python/Math
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ce fichier exprime la définition de "tout N" (tous les entiers naturels) et la conjecture de Collatz dans un style inspiré des assistants de preuve formelle (Coq, Lean), mais en Python.

- Définition de l'ensemble des entiers naturels (N)
- Définition de la fonction Collatz
- Formulation de la conjecture en pseudo-code formel
- Commentaire sur la transposition possible vers Coq/Lean
"""
from typing import Iterator

def ensemble_N() -> Iterator[int]:
    """
    Générateur infini de tous les entiers naturels n ≥ 1.
    (En langage de preuve formelle : N = { n | n ∈ ℕ, n ≥ 1 })
    """
    n = 1
    while True:
        yield n
        n += 1

def collatz(n: int) -> int:
    """
    Fonction Collatz C(n) :
        - si n pair : n // 2
        - si n impair : 3*n + 1
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def suite_collatz(n: int) -> Iterator[int]:
    """
    Génère la suite Collatz (u_k) à partir de n :
        u_0 = n
        u_{k+1} = collatz(u_k)
    """
    while True:
        yield n
        n = collatz(n)

# Formulation de la conjecture (pseudo-code formel)
"""
Conjecture de Collatz (formulation mathématique) :
Pour tout n ∈ ℕ*, il existe k ∈ ℕ tel que u_k = 1,
où (u_k) est la suite Collatz partant de n.

En pseudo-code Python :
    for n in ensemble_N():
        existe_k = False
        for k, u in enumerate(suite_collatz(n)):
            if u == 1:
                existe_k = True
                break
        assert existe_k

En langage de preuve formelle (Coq/Lean) :
    ∀ n : ℕ, ∃ k : ℕ, (collatz^k)(n) = 1

Remarque :
- Cette formalisation ne constitue pas une preuve, mais une expression rigoureuse de la propriété à démontrer.
- La transposition vers Coq/Lean consisterait à définir ℕ, la fonction collatz, puis à exprimer l'énoncé ∀ n, ∃ k, ...
""" 