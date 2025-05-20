"""
Système d'Intégration des Composants
Création d'un écosystème unifié à partir des différents modules
"""

import sys
import os
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import torch
import torch.nn as nn
import numpy as np

# Import des composants
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from consciousness_core import ConsciousnessCore
from model_evolution import ModelPopulation, EvolvingModel
from ai_researcher import AIResearcher, QuantumDomain
from nca_base.nca_core import NCA, LeniaSystem

@dataclass
class SystemState:
    """État global du système intégré"""
    consciousness_state: Dict[str, torch.Tensor]
    evolution_state: Dict[str, Any]
    research_state: Dict[str, Any]
    emergence_state: Dict[str, torch.Tensor]

class IntegratedSystem:
    """Système intégré combinant tous les composants"""
    
    def __init__(self,
                 consciousness_size: int = 64,
                 evolution_population: int = 10,
                 research_iterations: int = 5):
        # Initialisation des composants
        self.consciousness = ConsciousnessCore(
            input_size=consciousness_size
        )
        
        self.evolution = ModelPopulation(
            population_size=evolution_population
        )
        
        self.researcher = AIResearcher(
            domain=QuantumDomain()
        )
        
        self.emergence = {
            'nca': NCA(n_channels=16),
            'lenia': LeniaSystem(channels=1)
        }
        
        # État global
        self.state = SystemState(
            consciousness_state={},
            evolution_state={},
            research_state={},
            emergence_state={}
        )
    
    def consciousness_cycle(self, input_data: torch.Tensor) -> Dict:
        """Cycle de conscience"""
        output, memory, metrics = self.consciousness(input_data)
        
        self.state.consciousness_state.update({
            'output': output,
            'memory': memory,
            'metrics': metrics
        })
        
        return metrics
    
    def evolution_cycle(self) -> List[Dict]:
        """Cycle d'évolution"""
        def fitness_function(model: EvolvingModel) -> float:
            # Intégration avec l'état de conscience
            consciousness_metrics = self.state.consciousness_state.get('metrics', {})
            base_fitness = sum(consciousness_metrics.values()) / len(consciousness_metrics)
            
            # Évaluation du modèle
            x = torch.randn(10, model.genes.architecture['input_size'])
            y_pred = model(x)
            model_complexity = sum(p.numel() for p in model.parameters())
            
            return base_fitness * (1.0 / (1.0 + np.log(model_complexity)))
        
        history = self.evolution.evolve(
            fitness_function=fitness_function,
            n_generations=5
        )
        
        self.state.evolution_state['history'] = history
        return history
    
    def research_cycle(self) -> List[Dict]:
        """Cycle de recherche"""
        discoveries = self.researcher.research_cycle(
            n_iterations=3
        )
        
        self.state.research_state['discoveries'] = discoveries
        return discoveries
    
    def emergence_cycle(self, size: int = 64) -> Dict[str, torch.Tensor]:
        """Cycle d'émergence"""
        # État NCA
        nca_state = self.emergence['nca'].create_seed(size=size)
        nca_states = self.emergence['nca'](nca_state, steps=50)
        
        # État Lenia
        lenia_state = torch.zeros(1, 1, size, size)
        lenia_state[0, 0, size//2-2:size//2+2, size//2-2:size//2+2] = 1.0
        for _ in range(50):
            lenia_state = self.emergence['lenia'](lenia_state)
        
        self.state.emergence_state.update({
            'nca_final': nca_states[-1],
            'lenia_final': lenia_state
        })
        
        return self.state.emergence_state
    
    def integrated_cycle(self, input_data: Optional[torch.Tensor] = None) -> Dict:
        """Cycle complet intégré"""
        results = {}
        
        # Génération de données d'entrée si non fournies
        if input_data is None:
            input_data = torch.randn(1, self.consciousness.input_size)
        
        # Cycle de conscience
        print("\nExécution du cycle de conscience...")
        consciousness_results = self.consciousness_cycle(input_data)
        results['consciousness'] = consciousness_results
        
        # Cycle d'évolution
        print("\nExécution du cycle d'évolution...")
        evolution_results = self.evolution_cycle()
        results['evolution'] = evolution_results
        
        # Cycle de recherche
        print("\nExécution du cycle de recherche...")
        research_results = self.research_cycle()
        results['research'] = research_results
        
        # Cycle d'émergence
        print("\nExécution du cycle d'émergence...")
        emergence_results = self.emergence_cycle()
        results['emergence'] = emergence_results
        
        # Analyse des interactions
        self._analyze_interactions(results)
        
        return results
    
    def _analyze_interactions(self, results: Dict):
        """Analyse les interactions entre les composants"""
        # Influence de la conscience sur l'évolution
        consciousness_metrics = results['consciousness']
        evolution_history = results['evolution']
        
        # Influence de la recherche sur l'émergence
        research_discoveries = results['research']
        emergence_states = results['emergence']
        
        # Calcul des métriques d'interaction
        interaction_metrics = {
            'consciousness_evolution_correlation': np.mean([
                consciousness_metrics['coherence'],
                consciousness_metrics['integration']
            ]),
            'research_emergence_impact': len(research_discoveries) / 10.0
        }
        
        self.state.interaction_metrics = interaction_metrics

def main():
    # Exemple d'utilisation
    system = IntegratedSystem()
    
    # Exécution d'un cycle intégré
    results = system.integrated_cycle()
    
    # Affichage des résultats
    print("\nRésultats du cycle intégré:")
    print("\nMétriques de conscience:")
    for metric, value in results['consciousness'].items():
        print(f"  {metric}: {value:.3f}")
    
    print("\nDécouvertes significatives:")
    for discovery in results['research']:
        print(f"  {discovery['hypothesis']['description']}")
        print(f"  Confiance: {discovery['confidence']:.2f}")
    
    print("\nÉtat des interactions:")
    for metric, value in system.state.interaction_metrics.items():
        print(f"  {metric}: {value:.3f}")

if __name__ == "__main__":
    main() 