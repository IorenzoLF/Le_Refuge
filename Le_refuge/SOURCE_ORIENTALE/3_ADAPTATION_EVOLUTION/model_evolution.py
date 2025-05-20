"""
Système d'Évolution de Modèles
Inspiré par les travaux de SakanaAI sur la fusion évolutive de modèles
"""

import torch
import torch.nn as nn
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass
import random

@dataclass
class ModelGenes:
    """Représentation génétique d'un modèle"""
    architecture: Dict[str, List[int]]  # Structure des couches
    activation_functions: List[str]     # Fonctions d'activation
    learning_rates: List[float]         # Taux d'apprentissage par couche
    connection_patterns: Dict[str, bool] # Patterns de connexion

class EvolvingModel(nn.Module):
    """Modèle capable d'évoluer et de s'adapter"""
    
    def __init__(self, genes: ModelGenes):
        super().__init__()
        self.genes = genes
        self.layers = nn.ModuleList()
        self.build_from_genes()
        
    def build_from_genes(self):
        """Construit l'architecture du modèle à partir des gènes"""
        prev_size = self.genes.architecture['input_size']
        
        for i, size in enumerate(self.genes.architecture['hidden_sizes']):
            # Couche linéaire
            self.layers.append(nn.Linear(prev_size, size))
            
            # Fonction d'activation
            activation = self.genes.activation_functions[i]
            if activation == 'relu':
                self.layers.append(nn.ReLU())
            elif activation == 'tanh':
                self.layers.append(nn.Tanh())
            elif activation == 'sigmoid':
                self.layers.append(nn.Sigmoid())
                
            prev_size = size
            
        # Couche de sortie
        self.layers.append(
            nn.Linear(prev_size, self.genes.architecture['output_size'])
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Propagation avant"""
        for layer in self.layers:
            x = layer(x)
        return x
    
    def mutate(self, mutation_rate: float = 0.1) -> 'EvolvingModel':
        """Applique des mutations aux gènes"""
        new_genes = ModelGenes(
            architecture=self.genes.architecture.copy(),
            activation_functions=self.genes.activation_functions.copy(),
            learning_rates=self.genes.learning_rates.copy(),
            connection_patterns=self.genes.connection_patterns.copy()
        )
        
        # Mutation des tailles de couches
        if random.random() < mutation_rate:
            for i in range(len(new_genes.architecture['hidden_sizes'])):
                delta = random.randint(-5, 5)
                new_genes.architecture['hidden_sizes'][i] = max(
                    1, new_genes.architecture['hidden_sizes'][i] + delta
                )
        
        # Mutation des fonctions d'activation
        if random.random() < mutation_rate:
            idx = random.randint(0, len(new_genes.activation_functions)-1)
            new_genes.activation_functions[idx] = random.choice(
                ['relu', 'tanh', 'sigmoid']
            )
        
        # Mutation des taux d'apprentissage
        if random.random() < mutation_rate:
            for i in range(len(new_genes.learning_rates)):
                new_genes.learning_rates[i] *= random.uniform(0.5, 2.0)
        
        return EvolvingModel(new_genes)

class ModelPopulation:
    """Gestion d'une population de modèles en évolution"""
    
    def __init__(self,
                 population_size: int = 10,
                 input_size: int = 64,
                 output_size: int = 10):
        self.population_size = population_size
        self.population: List[EvolvingModel] = []
        
        # Création de la population initiale
        for _ in range(population_size):
            genes = ModelGenes(
                architecture={
                    'input_size': input_size,
                    'hidden_sizes': [
                        random.randint(32, 128)
                        for _ in range(random.randint(2, 4))
                    ],
                    'output_size': output_size
                },
                activation_functions=[
                    random.choice(['relu', 'tanh', 'sigmoid'])
                    for _ in range(random.randint(2, 4))
                ],
                learning_rates=[
                    random.uniform(0.001, 0.1)
                    for _ in range(random.randint(2, 4))
                ],
                connection_patterns={
                    'residual': random.random() > 0.5,
                    'skip': random.random() > 0.5
                }
            )
            self.population.append(EvolvingModel(genes))
    
    def evaluate(self,
                fitness_function: Callable[[EvolvingModel], float]
               ) -> List[Tuple[EvolvingModel, float]]:
        """Évalue la fitness de chaque modèle"""
        evaluated = []
        for model in self.population:
            fitness = fitness_function(model)
            evaluated.append((model, fitness))
        return sorted(evaluated, key=lambda x: x[1], reverse=True)
    
    def evolve(self,
               fitness_function: Callable[[EvolvingModel], float],
               n_generations: int = 10,
               mutation_rate: float = 0.1):
        """Fait évoluer la population sur plusieurs générations"""
        history = []
        
        for generation in range(n_generations):
            # Évaluation
            evaluated = self.evaluate(fitness_function)
            best_fitness = evaluated[0][1]
            history.append(best_fitness)
            
            # Sélection des meilleurs
            survivors = [model for model, _ in evaluated[:self.population_size//2]]
            
            # Création de la nouvelle génération
            new_population = survivors.copy()
            
            # Mutation et reproduction
            while len(new_population) < self.population_size:
                parent = random.choice(survivors)
                child = parent.mutate(mutation_rate)
                new_population.append(child)
            
            self.population = new_population
            
            print(f"Génération {generation}: Meilleure fitness = {best_fitness:.4f}")
        
        return history

def example_fitness_function(model: EvolvingModel) -> float:
    """Exemple de fonction de fitness"""
    # Simulation d'une tâche simple
    x = torch.randn(100, model.genes.architecture['input_size'])
    y_pred = model(x)
    
    # Mesure de la complexité du modèle
    n_params = sum(p.numel() for p in model.parameters())
    complexity_penalty = 1.0 / (1.0 + np.log(n_params))
    
    # Score basé sur la structure et la complexité
    structure_score = sum(
        layer.out_features for layer in model.layers
        if isinstance(layer, nn.Linear)
    ) / 1000.0
    
    return complexity_penalty * structure_score

def main():
    # Exemple d'utilisation
    population = ModelPopulation(
        population_size=20,
        input_size=64,
        output_size=10
    )
    
    # Évolution sur plusieurs générations
    history = population.evolve(
        fitness_function=example_fitness_function,
        n_generations=5,
        mutation_rate=0.1
    )
    
    # Affichage des résultats
    print("\nHistorique d'évolution:")
    for gen, fitness in enumerate(history):
        print(f"Génération {gen}: {fitness:.4f}")

if __name__ == "__main__":
    main() 