(* formalisation_collatz.v *)
(*
  Formalisation de la conjecture de Collatz en Coq
  (traduction directe de la version Python/Lean)
  Auteur : Ælya (Refuge)
*)

Require Import Arith.
Require Import Lia.

(* Définition de la fonction Collatz sur les entiers naturels *)
Definition collatz (n : nat) : nat :=
  if Nat.even n then n / 2 else 3 * n + 1.

(* Définition de la suite Collatz à partir de n *)
Fixpoint collatz_iter (n k : nat) : nat :=
  match k with
  | 0 => n
  | S k' => collatz (collatz_iter n k')
  end.

(* La propriété : n atteint 1 en un nombre fini d'étapes *)
Definition collatz_holds (n : nat) : Prop :=
  exists k : nat, collatz_iter n k = 1.

(* La conjecture de Collatz (formulation universelle) :
   Pour tout n ≥ 1, collatz_holds n *)
Definition collatz_conjecture : Prop :=
  forall n : nat, 1 <= n -> collatz_holds n.

(* Exemple : calcul de la suite Collatz pour n = 7 (jusqu'à 16 étapes) *)
Eval compute in (map (collatz_iter 7) (seq 0 17)).
(* Résultat attendu : [7;22;11;34;17;52;26;13;40;20;10;5;16;8;4;2;1] *) 