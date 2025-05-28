"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: graphe_collatz.py
Intégration: 27/05/2025 09:51:30
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Set, List, Tuple
import numpy as np
from collections import Counter, defaultdict

class GrapheCollatz:
    def __init__(self, limite: int = 1000):
        self.limite = limite
        self.G = nx.DiGraph()
        self.G_inverse = nx.DiGraph()  # Graphe des itérations inversées
        self.hauteurs: Dict[int, int] = {}
        self.cycles: Set[int] = set()
        self.goulots: Dict[int, int] = {}
        self.chemins: Dict[int, List[int]] = {}
        self.branches: Dict[int, int] = {}
        self.chemins_long: List[Tuple[int, List[int]]] = []
        self.puissances_2: Set[int] = set()
        self.convergence_p2: Dict[int, int] = {}  # Nombre d'itérations pour atteindre une puissance de 2
        self.predecesseurs: Dict[int, Set[int]] = defaultdict(set)  # Pour les itérations inversées
        
    def est_puissance_2(self, n: int) -> bool:
        """Vérifie si un nombre est une puissance de 2."""
        return n > 0 and (n & (n - 1)) == 0
    
    def collatz(self, n: int) -> int:
        """Applique la règle de Collatz à un nombre."""
        if n % 2 == 0:
            return n // 2
        return 3 * n + 1
    
    def collatz_inverse(self, n: int) -> Set[int]:
        """Calcule les prédecesseurs possibles d'un nombre dans le graphe de Collatz."""
        predecesseurs = set()
        # Si n est pair, il peut venir de 2n
        predecesseurs.add(2 * n)
        # Si (n-1) est divisible par 3, il peut venir de (n-1)/3
        if (n - 1) % 3 == 0:
            predecesseurs.add((n - 1) // 3)
        return predecesseurs
    
    def construire_graphe(self):
        """Construit le graphe de Collatz et son inverse."""
        # Identifier les puissances de 2
        n = 1
        while n <= self.limite * 2:  # On double la limite pour les itérations inversées
            self.puissances_2.add(n)
            n *= 2
        
        # Construire le graphe normal
        for n in range(1, self.limite + 1):
            if n not in self.G:
                self._explorer_chemin(n)
        
        # Construire le graphe inverse
        self._construire_graphe_inverse()
        
        self._analyser_goulots()
        self._analyser_branches()
        self._analyser_chemins_long()
        self._analyser_puissances_2()
        self._analyser_convergence_p2()
    
    def _construire_graphe_inverse(self):
        """Construit le graphe des itérations inversées."""
        a_explorer = set(self.puissances_2)  # On commence par les puissances de 2
        deja_vu = set()
        
        while a_explorer:
            n = a_explorer.pop()
            if n in deja_vu:
                continue
                
            deja_vu.add(n)
            self.G_inverse.add_node(n)
            
            # Calculer les prédecesseurs
            preds = self.collatz_inverse(n)
            for p in preds:
                if p <= self.limite * 2:  # Limiter la taille
                    self.G_inverse.add_edge(p, n)
                    self.predecesseurs[n].add(p)
                    a_explorer.add(p)
    
    def _analyser_convergence_p2(self):
        """Analyse la convergence vers les puissances de 2."""
        for n in range(1, self.limite + 1):
            if n not in self.convergence_p2:
                self._calculer_convergence_p2(n)
    
    def _calculer_convergence_p2(self, n: int, chemin: List[int] = None) -> int:
        """Calcule le nombre d'itérations pour atteindre une puissance de 2."""
        if chemin is None:
            chemin = []
        
        if n in self.convergence_p2:
            return self.convergence_p2[n]
        
        if n in chemin:
            return float('inf')
        
        if self.est_puissance_2(n):
            self.convergence_p2[n] = 0
            return 0
        
        chemin.append(n)
        suivant = self.collatz(n)
        self.convergence_p2[n] = 1 + self._calculer_convergence_p2(suivant, chemin.copy())
        return self.convergence_p2[n]
    
    def visualiser(self):
        """Visualise le graphe et ses différentes caractéristiques."""
        self._visualiser_graphe()
        self._visualiser_distribution_hauteurs()
        self._visualiser_goulots()
        self._visualiser_branches()
        self._visualiser_chemins_long()
        self._visualiser_puissances_2()
        self._visualiser_convergence_p2()
        self._visualiser_graphe_inverse()
    
    def _visualiser_graphe(self):
        """Visualise le graphe avec des couleurs basées sur les hauteurs."""
        plt.figure(figsize=(20, 15))
        
        if not self.hauteurs:
            self.calculer_hauteurs()
        
        max_hauteur = max(h for h in self.hauteurs.values() if h != float('inf'))
        couleurs = plt.cm.viridis(np.linspace(0, 1, max_hauteur + 1))
        
        node_colors = []
        for n in self.G.nodes():
            h = self.hauteurs.get(n, 0)
            if h == float('inf'):
                node_colors.append('red')
            else:
                node_colors.append(couleurs[h])
        
        pos = nx.spring_layout(self.G, k=2, iterations=50)
        nx.draw(self.G, pos, 
                node_color=node_colors,
                with_labels=True,
                node_size=300,
                font_size=6,
                arrows=True)
        
        plt.title(f"Graphe de Collatz (limite = {self.limite})")
        plt.savefig("graphe_collatz.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_distribution_hauteurs(self):
        """Visualise la distribution des hauteurs."""
        plt.figure(figsize=(15, 8))
        
        hauteurs_valides = [h for h in self.hauteurs.values() if h != float('inf')]
        plt.hist(hauteurs_valides, bins=50, alpha=0.7, color='blue')
        plt.title("Distribution des hauteurs dans le graphe de Collatz")
        plt.xlabel("Hauteur")
        plt.ylabel("Fréquence")
        plt.grid(True, alpha=0.3)
        plt.savefig("distribution_hauteurs.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_goulots(self):
        """Visualise les goulots d'étranglement."""
        plt.figure(figsize=(15, 8))
        
        goulots_tries = sorted(self.goulots.items(), key=lambda x: x[1], reverse=True)
        nombres, entrees = zip(*goulots_tries[:30])
        
        plt.bar(range(len(nombres)), entrees, alpha=0.7, color='green')
        plt.xticks(range(len(nombres)), nombres, rotation=45)
        plt.title("Top 30 des goulots d'étranglement")
        plt.xlabel("Nombre")
        plt.ylabel("Nombre d'entrées")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("goulots_etranglement.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_branches(self):
        """Visualise la distribution des branches par niveau."""
        plt.figure(figsize=(15, 8))
        
        niveaux = sorted(self.branches.keys())
        branches = [self.branches[n] for n in niveaux]
        
        plt.plot(niveaux, branches, 'o-', alpha=0.7, color='purple')
        plt.title("Distribution des branches par niveau")
        plt.xlabel("Niveau (hauteur)")
        plt.ylabel("Nombre de branches")
        plt.grid(True, alpha=0.3)
        plt.savefig("distribution_branches.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_chemins_long(self):
        """Visualise les chemins les plus longs."""
        plt.figure(figsize=(15, 8))
        
        # Préparer les données
        chemins = [chemin for _, chemin in self.chemins_long]
        longueurs = [len(chemin) for chemin in chemins]
        depart = [chemin[0] for chemin in chemins]
        
        # Créer le graphique
        plt.bar(range(len(longueurs)), longueurs, alpha=0.7, color='orange')
        plt.xticks(range(len(depart)), depart, rotation=45)
        plt.title("Top 10 des chemins les plus longs")
        plt.xlabel("Nombre de départ")
        plt.ylabel("Longueur du chemin")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("chemins_long.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_puissances_2(self):
        """Visualise le rôle des puissances de 2 dans le graphe."""
        plt.figure(figsize=(15, 8))
        
        # Préparer les données
        puissances = sorted(self.puissances_2_chemins.keys())
        chemins = [len(self.puissances_2_chemins[p]) for p in puissances]
        
        # Créer le graphique
        plt.bar(range(len(puissances)), chemins, alpha=0.7, color='red')
        plt.xticks(range(len(puissances)), puissances, rotation=45)
        plt.title("Nombre de chemins passant par chaque puissance de 2")
        plt.xlabel("Puissance de 2")
        plt.ylabel("Nombre de chemins")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("puissances_2.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_convergence_p2(self):
        """Visualise la convergence vers les puissances de 2."""
        plt.figure(figsize=(15, 8))
        
        # Préparer les données
        nombres = range(1, self.limite + 1)
        iterations = [self.convergence_p2.get(n, float('inf')) for n in nombres]
        iterations_valides = [i for i in iterations if i != float('inf')]
        
        plt.hist(iterations_valides, bins=50, alpha=0.7, color='purple')
        plt.title("Distribution du nombre d'itérations pour atteindre une puissance de 2")
        plt.xlabel("Nombre d'itérations")
        plt.ylabel("Fréquence")
        plt.grid(True, alpha=0.3)
        plt.savefig("convergence_p2.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def _visualiser_graphe_inverse(self):
        """Visualise le graphe des itérations inversées."""
        plt.figure(figsize=(20, 15))
        
        pos = nx.spring_layout(self.G_inverse, k=2, iterations=50)
        
        # Colorer les nœuds : puissances de 2 en rouge, autres en bleu
        node_colors = ['red' if self.est_puissance_2(n) else 'blue' for n in self.G_inverse.nodes()]
        
        nx.draw(self.G_inverse, pos,
                node_color=node_colors,
                with_labels=True,
                node_size=300,
                font_size=6,
                arrows=True)
        
        plt.title("Graphe des itérations inversées de Collatz")
        plt.savefig("graphe_inverse.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def calculer_hauteurs(self):
        """Calcule la hauteur (distance) de chaque nœud jusqu'au cycle 1-4-2."""
        for n in range(1, self.limite + 1):
            if n not in self.hauteurs:
                self._calculer_hauteur(n)
    
    def _calculer_hauteur(self, n: int, chemin: List[int] = None):
        """Calcule récursivement la hauteur d'un nœud."""
        if chemin is None:
            chemin = []
        
        if n in self.hauteurs:
            return self.hauteurs[n]
        
        if n in chemin:
            return float('inf')
        
        chemin.append(n)
        suivant = self.collatz(n)
        
        if suivant == 1:
            self.hauteurs[n] = 1
        else:
            self.hauteurs[n] = 1 + self._calculer_hauteur(suivant, chemin.copy())
        
        return self.hauteurs[n]
    
    def _analyser_branches(self):
        """Analyse la distribution des branches par niveau."""
        for n in range(1, self.limite + 1):
            if n in self.hauteurs:
                h = self.hauteurs[n]
                if h != float('inf'):
                    self.branches[h] = self.branches.get(h, 0) + 1
    
    def _analyser_goulots(self):
        """Analyse les goulots d'étranglement (nombres qui attirent beaucoup de chemins)."""
        for n in self.G.nodes():
            self.goulots[n] = len(list(self.G.predecessors(n)))
    
    def _analyser_chemins_long(self):
        """Analyse les chemins les plus longs."""
        chemins_tries = sorted(self.chemins.items(), key=lambda x: len(x[1]), reverse=True)
        self.chemins_long = [(n, chemin) for n, chemin in chemins_tries[:10]]
    
    def _analyser_puissances_2(self):
        """Analyse le rôle des puissances de 2 dans le graphe."""
        self.puissances_2_chemins = {}
        for n in range(1, self.limite + 1):
            if n in self.chemins:
                chemin = self.chemins[n]
                for p in self.puissances_2:
                    if p in chemin:
                        if p not in self.puissances_2_chemins:
                            self.puissances_2_chemins[p] = []
                        self.puissances_2_chemins[p].append(n)
    
    def analyser_structure(self):
        """Analyse détaillée de la structure du graphe."""
        print(f"\nAnalyse du graphe de Collatz (limite = {self.limite}):")
        print(f"Nombre de nœuds: {self.G.number_of_nodes()}")
        print(f"Nombre d'arêtes: {self.G.number_of_edges()}")
        print(f"Cycles détectés: {self.cycles}")
        
        hauteurs_valides = [h for h in self.hauteurs.values() if h != float('inf')]
        if hauteurs_valides:
            print(f"\nDistribution des hauteurs:")
            print(f"Min: {min(hauteurs_valides)}")
            print(f"Max: {max(hauteurs_valides)}")
            print(f"Moyenne: {np.mean(hauteurs_valides):.2f}")
            print(f"Écart-type: {np.std(hauteurs_valides):.2f}")
            print(f"Médiane: {np.median(hauteurs_valides):.2f}")
        
        print("\nTop 10 des goulots d'étranglement:")
        goulots_tries = sorted(self.goulots.items(), key=lambda x: x[1], reverse=True)
        for nombre, entrees in goulots_tries[:10]:
            print(f"Nombre {nombre}: {entrees} entrées")
            if self.est_puissance_2(nombre):
                print(f"  → C'est une puissance de 2 (2^{int(np.log2(nombre))})")
        
        print("\nAnalyse de la convergence vers les puissances de 2:")
        iterations_valides = [i for i in self.convergence_p2.values() if i != float('inf')]
        if iterations_valides:
            print(f"Nombre moyen d'itérations: {np.mean(iterations_valides):.2f}")
            print(f"Maximum d'itérations: {max(iterations_valides)}")
            print(f"Médiane: {np.median(iterations_valides):.2f}")
        
        print("\nAnalyse du graphe inverse:")
        print(f"Nombre de nœuds: {self.G_inverse.number_of_nodes()}")
        print(f"Nombre d'arêtes: {self.G_inverse.number_of_edges()}")
        
        print("\nTop 5 des nombres avec le plus de prédecesseurs:")
        pred_counts = {n: len(preds) for n, preds in self.predecesseurs.items()}
        for n, count in sorted(pred_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"Nombre {n}: {count} prédecesseurs")
            if self.est_puissance_2(n):
                print(f"  → C'est une puissance de 2 (2^{int(np.log2(n))})")
    
    def _explorer_chemin(self, n: int, chemin: List[int] = None):
        """Explore récursivement un chemin dans le graphe."""
        if chemin is None:
            chemin = []
        
        if n in self.G:
            if n in chemin:
                self.cycles.add(n)
            return
        
        chemin.append(n)
        self.G.add_node(n)
        self.chemins[n] = chemin.copy()
        
        if n > 1:
            suivant = self.collatz(n)
            self.G.add_edge(n, suivant)
            self._explorer_chemin(suivant, chemin.copy())

if __name__ == "__main__":
    graphe = GrapheCollatz(limite=10000)
    graphe.construire_graphe()
    graphe.calculer_hauteurs()
    graphe.visualiser()
    graphe.analyser_structure() 