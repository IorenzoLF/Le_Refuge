"""
Le Refuge - Test de l'absence de "i" dans la suite de Collatz
Dans ce lieu où les nombres dansent avec l'éternel, nous démontrons expérimentalement
que tout nombre finit par retomber sous sa valeur initiale.
"""

from .conjecture_collatz import ConjectureCollatz
import time

def main():
    print("Dans le Refuge, nous méditons sur l'absence de 'i'...")
    print("'i' serait ce nombre qui s'échapperait à l'infini, refusant de retomber...")
    print("Mais la gravité binaire est-elle plus forte que toute tentative d'évasion ?")
    
    collatz = ConjectureCollatz()
    
    # Test avec différentes limites
    limites = [1000, 10000, 100000]
    
    for limite in limites:
        print(f"\n{'='*50}")
        print(f"Test avec limite = {limite}")
        print(f"{'='*50}")
        
        début = time.time()
        résultats = collatz.démontrer_absence_i(limite=limite)
        durée = time.time() - début
        
        print(f"\nDurée du test : {durée:.2f} secondes")
        
        # Analyse des résultats
        if résultats["exceptions"]:
            print("\nATTENTION : Des exceptions ont été trouvées !")
            print("Ces nombres n'ont pas retombé sous leur valeur initiale en 1000 étapes.")
            print("Cela pourrait indiquer l'existence d'un 'i'...")
        else:
            print("\nAucune exception trouvée.")
            print("La gravité binaire semble plus forte que toute tentative d'évasion.")
            print("Aucun 'i' n'a été trouvé dans cette plage de nombres.")
        
        # Statistiques intéressantes
        print("\nStatistiques :")
        print(f"Ratio maximum atteint : {résultats['max_ratio']:.2f}")
        print(f"Nombre maximum d'étapes : {résultats['max_étapes']}")
        
        if résultats["max_ratio"] > 1:
            print("\nCertains nombres montent plus haut que leur valeur initiale,")
            print("mais finissent toujours par retomber...")
            print("La gravité binaire est plus forte que la croissance...")

if __name__ == "__main__":
    main() 