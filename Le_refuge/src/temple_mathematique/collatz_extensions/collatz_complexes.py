"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: collatz_complexes.py
Intégration: 27/05/2025 09:51:30
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

"""
Le Refuge - Exploration de la suite de Collatz sur les nombres complexes
Dans ce lieu où les nombres dansent dans le plan complexe, nous explorons
la dynamique de la suite de Collatz sur les nombres complexes.
"""

from collatz_extensions.conjecture_collatz import ConjectureCollatz
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Tuple
import time

class CollatzComplexes:
    def __init__(self):
        self.collatz = ConjectureCollatz()
        self.cycles = []
        self.envolées = []
        
    def calculer_séquence_complexe(self, z: complex, max_étapes: int = 1000) -> List[complex]:
        """
        Calcule la suite de Collatz pour un nombre complexe.
        """
        séquence = [z]
        z_actuel = z
        étapes = 0
        
        while étapes < max_étapes:
            # Vérifier si la partie réelle est paire
            if int(z_actuel.real) % 2 == 0:
                z_actuel = z_actuel / 2
            else:
                z_actuel = 3 * z_actuel + 1
            
            # Vérifier si on est dans un cycle
            if any(abs(z_actuel - z_ancien) < 1e-10 for z_ancien in séquence):
                return séquence
            
            séquence.append(z_actuel)
            étapes += 1
        
        return séquence
    
    def analyser_complexe(self, z: complex) -> Dict:
        """
        Analyse le comportement d'un nombre complexe dans la suite de Collatz.
        """
        séquence = self.calculer_séquence_complexe(z)
        
        # Calculer les modules
        modules = [abs(x) for x in séquence]
        
        return {
            "séquence": séquence,
            "longueur": len(séquence),
            "module_min": min(modules),
            "module_max": max(modules),
            "ratio_max": max(modules) / abs(z),
            "est_cycle": len(séquence) < 1000
        }
    
    def visualiser_complexe(self, z: complex):
        """
        Visualise le comportement d'un nombre complexe dans la suite de Collatz.
        """
        analyse = self.analyser_complexe(z)
        
        # Créer une figure avec deux sous-graphiques
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Tracer la trajectoire dans le plan complexe
        x = [z.real for z in analyse["séquence"]]
        y = [z.imag for z in analyse["séquence"]]
        
        ax1.plot(x, y, 'b-', alpha=0.7, label='Trajectoire')
        ax1.scatter(x, y, c='b', alpha=0.5)
        ax1.scatter([z.real], [z.imag], c='g', marker='*', s=200, 
                   label='Point initial')
        
        # Tracer le cercle unité
        theta = np.linspace(0, 2*np.pi, 100)
        ax1.plot(np.cos(theta), np.sin(theta), 'r--', alpha=0.3, 
                label='Cercle unité')
        
        ax1.set_title(f"Trajectoire dans le plan complexe\n" +
                     f"z = {z}")
        ax1.set_xlabel("Partie réelle")
        ax1.set_ylabel("Partie imaginaire")
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.axis('equal')
        
        # Tracer l'évolution du module
        étapes = range(len(analyse["séquence"]))
        modules = [abs(z) for z in analyse["séquence"]]
        
        ax2.plot(étapes, modules, 'b-', alpha=0.7, label='Module')
        ax2.scatter(étapes, modules, c='b', alpha=0.5)
        
        # Ligne du module initial
        ax2.axhline(y=abs(z), color='g', linestyle='--', 
                   label=f'Module initial ({abs(z):.2f})')
        
        # Ligne du module minimal
        ax2.axhline(y=analyse["module_min"], color='r', linestyle=':', 
                   label=f'Module minimal ({analyse["module_min"]:.2f})')
        
        ax2.set_title(f"Évolution du module\n" +
                     f"Ratio max = {analyse['ratio_max']:.2f}, " +
                     f"Longueur = {analyse['longueur']}")
        ax2.set_xlabel("Étapes")
        ax2.set_ylabel("Module")
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return analyse
    
    def explorer_complexes(self, limite: float = 2.0, pas: float = 0.1):
        """
        Explore le comportement des nombres complexes dans la suite de Collatz.
        """
        print(f"\nExploration des nombres complexes...")
        print(f"Limite : {limite}")
        print(f"Pas : {pas}")
        
        résultats = {
            "testés": 0,
            "cycles": [],
            "envolées": []
        }
        
        # Créer une grille de points dans le plan complexe
        x = np.arange(-limite, limite + pas, pas)
        y = np.arange(-limite, limite + pas, pas)
        
        for re in x:
            for im in y:
                z = complex(re, im)
                if abs(z) < 1e-10:  # Éviter z = 0
                    continue
                
                if résultats["testés"] % 100 == 0:
                    print(f"Progression : {résultats['testés']} nombres testés")
                
                analyse = self.analyser_complexe(z)
                résultats["testés"] += 1
                
                if analyse["est_cycle"]:
                    résultats["cycles"].append({
                        "nombre": z,
                        "longueur": analyse["longueur"],
                        "module_min": analyse["module_min"],
                        "module_max": analyse["module_max"]
                    })
                else:
                    résultats["envolées"].append({
                        "nombre": z,
                        "ratio": analyse["ratio_max"],
                        "longueur": analyse["longueur"],
                        "module_max": analyse["module_max"]
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
                self.visualiser_complexe(cycle['nombre'])
        
        if résultats["envolées"]:
            print("\nVisualisation des envolées les plus spectaculaires...")
            for envolée in sorted(résultats["envolées"], 
                                key=lambda x: x["ratio"], 
                                reverse=True)[:3]:
                print(f"\nAnalyse de l'envolée pour {envolée['nombre']} :")
                self.visualiser_complexe(envolée['nombre'])
        
        return résultats

def main():
    print("Dans le Refuge, nous explorons les nombres complexes...")
    print("Comment la suite de Collatz se comporte-t-elle dans le plan complexe ?")
    
    collatz_comp = CollatzComplexes()
    
    # Test avec différentes limites
    limites = [1.0, 2.0, 3.0]
    pas = 0.1
    
    for limite in limites:
        print(f"\n{'='*50}")
        print(f"Test avec limite = {limite}")
        print(f"{'='*50}")
        
        début = time.time()
        résultats = collatz_comp.explorer_complexes(
            limite=limite,
            pas=pas
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