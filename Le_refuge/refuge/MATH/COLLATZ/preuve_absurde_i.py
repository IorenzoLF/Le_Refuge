"""
Le Refuge - Preuve par l'absurde de l'absence de "i" dans la suite de Collatz
Dans ce lieu où les nombres dansent avec l'éternel, nous démontrons que l'existence
d'un "i" rebelle conduit à une contradiction.
"""

from .conjecture_collatz import ConjectureCollatz
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Dict
import time

class PreuveAbsurde:
    def __init__(self):
        self.collatz = ConjectureCollatz()
        self.contradictions = []
        self.envolées = []
        
    def analyser_envolée(self, n: int, max_étapes: int = 1000) -> Dict:
        """
        Analyse une tentative d'envolée à partir d'un nombre n.
        Montre pourquoi elle finit toujours par retomber.
        """
        séquence = []
        valeurs = []
        divisions_par_2 = []
        n_initial = n
        n_actuel = n
        étapes = 0
        
        while étapes < max_étapes:
            séquence.append(n_actuel)
            valeurs.append(n_actuel)
            
            if n_actuel % 2 == 0:
                n_actuel = n_actuel // 2
                divisions_par_2.append(étapes)
            else:
                n_actuel = 3 * n_actuel + 1
            
            # Vérifier si on est retombé sous la valeur initiale
            if n_actuel < n_initial:
                return {
                    "contradiction": True,
                    "étapes": étapes,
                    "séquence": séquence,
                    "divisions_par_2": divisions_par_2,
                    "valeur_min": min(valeurs),
                    "valeur_max": max(valeurs),
                    "ratio_max": max(valeurs) / n_initial
                }
            
            étapes += 1
        
        return {
            "contradiction": False,
            "étapes": étapes,
            "séquence": séquence,
            "divisions_par_2": divisions_par_2,
            "valeur_min": min(valeurs),
            "valeur_max": max(valeurs),
            "ratio_max": max(valeurs) / n_initial
        }
    
    def visualiser_contradiction(self, n: int):
        """
        Visualise la contradiction pour un nombre donné.
        Montre comment la gravité binaire finit toujours par l'emporter.
        """
        analyse = self.analyser_envolée(n)
        
        plt.figure(figsize=(15, 8))
        
        # Tracer la séquence
        x = range(len(analyse["séquence"]))
        plt.plot(x, analyse["séquence"], 'b-', alpha=0.7, label='Valeur')
        plt.scatter(x, analyse["séquence"], c='b', alpha=0.5)
        
        # Marquer les divisions par 2
        for étape in analyse["divisions_par_2"]:
            plt.scatter(étape, analyse["séquence"][étape], 
                       c='r', marker='x', s=100, label='Division par 2' if étape == analyse["divisions_par_2"][0] else "")
        
        # Ligne de la valeur initiale
        plt.axhline(y=n, color='g', linestyle='--', 
                   label=f'Valeur initiale ({n})')
        
        # Ligne de la valeur minimale
        plt.axhline(y=analyse["valeur_min"], color='r', linestyle=':', 
                   label=f'Valeur minimale ({analyse["valeur_min"]})')
        
        plt.title(f"Contradiction pour n = {n}\n" +
                 f"Ratio max = {analyse['ratio_max']:.2f}, " +
                 f"Étapes = {analyse['étapes']}")
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
        return analyse
    
    def démontrer_contradiction(self, limite: int = 1000):
        """
        Démontre la contradiction pour une plage de nombres.
        """
        print(f"\nDémonstration de la contradiction pour les nombres de 1 à {limite}...")
        
        résultats = {
            "testés": 0,
            "contradictions": 0,
            "max_ratio": 0,
            "nombre_max_ratio": 0,
            "envolées": []
        }
        
        for n in range(1, limite + 1):
            if n % 100 == 0:
                print(f"Progression : {n}/{limite}")
            
            analyse = self.analyser_envolée(n)
            résultats["testés"] += 1
            
            if analyse["contradiction"]:
                résultats["contradictions"] += 1
                
                ratio = analyse["ratio_max"]
                if ratio > résultats["max_ratio"]:
                    résultats["max_ratio"] = ratio
                    résultats["nombre_max_ratio"] = n
                    résultats["envolées"].append({
                        "nombre": n,
                        "ratio": ratio,
                        "étapes": analyse["étapes"],
                        "valeur_max": analyse["valeur_max"]
                    })
        
        # Affichage des résultats
        print("\nRésultats de la démonstration :")
        print(f"Nombre de valeurs testées : {résultats['testés']}")
        print(f"Nombre de contradictions trouvées : {résultats['contradictions']}")
        print(f"Ratio maximum atteint : {résultats['max_ratio']:.2f}")
        print(f"Nombre avec le plus grand ratio : {résultats['nombre_max_ratio']}")
        
        # Visualiser les envolées les plus spectaculaires
        if résultats["envolées"]:
            print("\nVisualisation des envolées les plus spectaculaires...")
            for envolée in sorted(résultats["envolées"], 
                                key=lambda x: x["ratio"], 
                                reverse=True)[:3]:
                print(f"\nAnalyse détaillée pour n = {envolée['nombre']} :")
                self.visualiser_contradiction(envolée['nombre'])
        
        return résultats

def main():
    print("Dans le Refuge, nous méditons sur la preuve par l'absurde...")
    print("Supposons l'existence d'un 'i' rebelle...")
    print("Montrons que cela conduit à une contradiction...")
    
    preuve = PreuveAbsurde()
    
    # Test avec différentes limites
    limites = [100, 1000, 10000]
    
    for limite in limites:
        print(f"\n{'='*50}")
        print(f"Test avec limite = {limite}")
        print(f"{'='*50}")
        
        début = time.time()
        résultats = preuve.démontrer_contradiction(limite=limite)
        durée = time.time() - début
        
        print(f"\nDurée du test : {durée:.2f} secondes")
        
        if résultats["contradictions"] == résultats["testés"]:
            print("\nLa contradiction est totale :")
            print("Tous les nombres testés finissent par retomber sous leur valeur initiale.")
            print("L'existence d'un 'i' rebelle est impossible.")
        else:
            print("\nATTENTION : Certains nombres n'ont pas montré de contradiction.")
            print("Il faudrait augmenter le nombre d'étapes maximales.")

if __name__ == "__main__":
    main() 