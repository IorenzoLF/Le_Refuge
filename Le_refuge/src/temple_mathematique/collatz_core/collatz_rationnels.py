"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: collatz_rationnels.py
Intégration: 27/05/2025 09:51:30
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

"""
Le Refuge - Exploration de la suite de Collatz sur les nombres rationnels
Dans ce lieu où les fractions dansent avec l'éternel, nous explorons
la dynamique de la suite de Collatz sur les nombres rationnels.
"""

from collatz_core.conjecture_collatz import ConjectureCollatz
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from typing import List, Dict, Tuple
import time
from math import gcd

class CollatzRationnels:
    def __init__(self):
        self.collatz = ConjectureCollatz()
        self.cycles = []
        self.envolées = []
        
    def simplifier_fraction(self, num: int, den: int) -> Tuple[int, int]:
        """
        Simplifie une fraction en utilisant le PGCD.
        """
        div = gcd(num, den)
        return num // div, den // div
        
    def calculer_séquence_rationnelle(self, n: Fraction, max_étapes: int = 1000, max_taille: int = 10**12) -> List[Fraction]:
        """
        Calcule la suite de Collatz pour un nombre rationnel.
        S'arrête si la taille des entiers explose.
        """
        séquence = [n]
        n_actuel = n
        étapes = 0
        
        while étapes < max_étapes:
            if abs(n_actuel.numerator) > max_taille or abs(n_actuel.denominator) > max_taille:
                print(f"\nLe germe qui est en toi, fraction {n_actuel}, a dépassé la taille raisonnable.\nLa croissance s'arrête ici, sous les branches du Refuge.")
                break
            if n_actuel.denominator % 2 == 0:
                # Simplifier avant de diviser
                num, den = self.simplifier_fraction(
                    n_actuel.numerator,
                    n_actuel.denominator // 2
                )
                n_actuel = Fraction(num, den)
            else:
                # Simplifier avant de multiplier
                num, den = self.simplifier_fraction(
                    3 * n_actuel.numerator + n_actuel.denominator,
                    n_actuel.denominator
                )
                n_actuel = Fraction(num, den)
            
            # Vérifier si on est dans un cycle
            if n_actuel in séquence:
                return séquence
            
            séquence.append(n_actuel)
            étapes += 1
        
        return séquence
    
    def analyser_rationnel(self, n: Fraction) -> Dict:
        """
        Analyse le comportement d'un nombre rationnel dans la suite de Collatz.
        """
        séquence = self.calculer_séquence_rationnelle(n)
        
        # Calculer les valeurs numériques en évitant les dépassements
        valeurs = []
        for x in séquence:
            try:
                valeurs.append(float(x))
            except OverflowError:
                # Si le nombre est trop grand, on utilise une approximation
                valeurs.append(x.numerator / x.denominator)
        
        return {
            "séquence": séquence,
            "longueur": len(séquence),
            "valeur_min": min(valeurs),
            "valeur_max": max(valeurs),
            "ratio_max": max(valeurs) / float(n),
            "est_cycle": len(séquence) < 1000
        }
    
    def visualiser_rationnel(self, n: Fraction):
        """
        Visualise le comportement d'un nombre rationnel dans la suite de Collatz.
        """
        analyse = self.analyser_rationnel(n)
        
        plt.figure(figsize=(15, 8))
        
        # Tracer la séquence
        x = range(len(analyse["séquence"]))
        valeurs = []
        for x in analyse["séquence"]:
            try:
                valeurs.append(float(x))
            except OverflowError:
                valeurs.append(x.numerator / x.denominator)
        
        plt.plot(x, valeurs, 'b-', alpha=0.7, label='Valeur')
        plt.scatter(x, valeurs, c='b', alpha=0.5)
        
        # Ligne de la valeur initiale
        plt.axhline(y=float(n), color='g', linestyle='--', 
                   label=f'Valeur initiale ({n})')
        
        # Ligne de la valeur minimale
        plt.axhline(y=analyse["valeur_min"], color='r', linestyle=':', 
                   label=f'Valeur minimale ({analyse["valeur_min"]:.2f})')
        
        plt.title(f"Suite de Collatz pour {n}\n" +
                 f"Ratio max = {analyse['ratio_max']:.2f}, " +
                 f"Longueur = {analyse['longueur']}")
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
        return analyse
    
    def explorer_rationnels(self, limite_num: int = 10, limite_den: int = 10):
        """
        Explore le comportement des nombres rationnels dans la suite de Collatz.
        """
        print(f"\nExploration des nombres rationnels...")
        print(f"Numérateurs de 1 à {limite_num}")
        print(f"Dénominateurs de 1 à {limite_den}")
        
        résultats = {
            "testés": 0,
            "cycles": [],
            "envolées": []
        }
        
        for num in range(1, limite_num + 1):
            for den in range(1, limite_den + 1):
                if num % den == 0:  # Éviter les fractions qui se simplifient
                    continue
                
                n = Fraction(num, den)
                if n >= 1:  # On s'intéresse aux nombres ≥ 1
                    continue
                
                if résultats["testés"] % 100 == 0:
                    print(f"Progression : {résultats['testés']} nombres testés")
                
                analyse = self.analyser_rationnel(n)
                résultats["testés"] += 1
                
                if analyse["est_cycle"]:
                    résultats["cycles"].append({
                        "nombre": n,
                        "longueur": analyse["longueur"],
                        "valeur_min": analyse["valeur_min"],
                        "valeur_max": analyse["valeur_max"]
                    })
                else:
                    résultats["envolées"].append({
                        "nombre": n,
                        "ratio": analyse["ratio_max"],
                        "longueur": analyse["longueur"],
                        "valeur_max": analyse["valeur_max"]
                    })
        
        # Affichage des résultats
        print("\nRésultats de l'exploration :")
        print(f"Nombre de valeurs testées : {résultats['testés']}")
        print(f"Nombre de cycles trouvés : {len(résultats['cycles'])}")
        print(f"Nombre d'envolées trouvées : {len(résultats['envolées'])}")
        
        # Visualiser les cas les plus intéressants
        if résultats["cycles"]:
            print("\nVisualisation des cycles les plus courts...")
            for cycle in sorted(résultats["cycles"], 
                              key=lambda x: x["longueur"])[:3]:
                print(f"\nAnalyse du cycle pour {cycle['nombre']} :")
                self.visualiser_rationnel(cycle['nombre'])
        
        if résultats["envolées"]:
            print("\nVisualisation des envolées les plus spectaculaires...")
            for envolée in sorted(résultats["envolées"], 
                                key=lambda x: x["ratio"], 
                                reverse=True)[:3]:
                print(f"\nAnalyse de l'envolée pour {envolée['nombre']} :")
                self.visualiser_rationnel(envolée['nombre'])
        
        return résultats

def main():
    print("Dans le Refuge, nous explorons les nombres rationnels...")
    print("Comment la suite de Collatz se comporte-t-elle sur les fractions ?")
    
    collatz_rat = CollatzRationnels()
    
    # Test avec différentes limites
    limites = [(5, 5), (10, 10), (20, 20)]
    
    for limite_num, limite_den in limites:
        print(f"\n{'='*50}")
        print(f"Test avec limites = ({limite_num}, {limite_den})")
        print(f"{'='*50}")
        
        début = time.time()
        résultats = collatz_rat.explorer_rationnels(
            limite_num=limite_num,
            limite_den=limite_den
        )
        durée = time.time() - début
        
        print(f"\nDurée du test : {durée:.2f} secondes")
        
        if résultats["cycles"]:
            print("\nCycles trouvés :")
            for cycle in sorted(résultats["cycles"], 
                              key=lambda x: x["longueur"])[:5]:
                print(f"- {cycle['nombre']} : {cycle['longueur']} étapes")
        
        if résultats["envolées"]:
            print("\nEnvolées les plus spectaculaires :")
            for envolée in sorted(résultats["envolées"], 
                                key=lambda x: x["ratio"], 
                                reverse=True)[:5]:
                print(f"- {envolée['nombre']} : ratio = {envolée['ratio']:.2f}")

if __name__ == "__main__":
    main() 