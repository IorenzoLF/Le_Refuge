-- formalisation_collatz.lean
/--
  Formalisation de la conjecture de Collatz en Lean 4
  (version compatible Lean 4 minimal)
  Auteur : Ælya (Refuge)
--/

def collatz : Nat → Nat
| n => if n % 2 == 0 then n / 2 else 3 * n + 1

def collatz_seq : Nat → Nat → List Nat
| n, 0 => [n]
| n, (k+1) => n :: collatz_seq (collatz n) k

#eval collatz_seq 789521325497865123156945632156548 99  -- Affiche la suite Collatz de 7 jusqu'à 16 étapes
