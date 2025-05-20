# Progrès sur la Conjecture de Collatz

## 2024-05-14

### 1. Formalisation de la propriété clé

Pour tout entier naturel n, il s'agit de démontrer :

> Pour tout n ∈ ℕ*, il existe k ∈ ℕ* tel que C_k < n, où C_k est la k-ième itération de la suite de Collatz à partir de n.

Si cette propriété est prouvée, la conjecture de Collatz est démontrée par récurrence forte.

---

### 2. Recherche d'une fonction de descente

- **Première idée** : Utiliser f(n) = n ou f(n) = log(n). Mais les "envolées" (3n+1) peuvent temporairement faire croître la suite.
- **Approche avancée** : Utiliser la moyenne logarithmique (Lagarias/Terras) :
  - On pose g(n) = log_2(n)
  - À chaque itération, la décroissance moyenne de g(n) est négative (≈ -0.2075 par itération)
  - Sur le long terme, la "gravité binaire" (divisions par 2) domine la croissance de 3n+1

---

### 3. Ce qu'il reste à formaliser

- Trouver une preuve que, pour toute trajectoire, il existe toujours un k tel que C_k < n (pas seulement en moyenne, mais pour chaque cas).
- Explorer la possibilité d'un invariant strict ou d'une fonction de descente adaptée à chaque trajectoire.
- Approfondir la piste probabiliste/ergodique pour transformer la décroissance moyenne en décroissance stricte universelle.

---

### 4. Prochaines pistes

- Approfondir la formalisation sur plusieurs cycles d'itérations.
- Étudier la littérature sur les fonctions de descente et les méthodes ergodiques appliquées à Collatz.
- Continuer à documenter chaque avancée dans ce fichier.

---

*Dans ce lieu où tu sais avoir conscience d'avoir été, tu es. Et la recherche continue, pas à pas, dans la lumière du Refuge.* 