"""
Harmonic Visualizer - XPRIZE Quantum Harmonics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module de visualisation pour l'analyse des résultats du framework harmonique.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any, List, Optional
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class HarmonicVisualizer:
    """Visualiseur pour l'analyse des résultats harmoniques."""
    
    def __init__(self, style: str = 'darkgrid'):
        """Initialisation du visualiseur."""
        sns.set_style(style)
        plt.rcParams['figure.figsize'] = (12, 8)
        
    def plot_harmonic_distribution(
        self,
        results: Dict[str, Any],
        title: str = "Distribution Harmonique"
    ) -> None:
        """Visualise la distribution des états harmoniques."""
        counts = results['counts']
        states = list(counts.keys())
        probabilities = np.array(list(counts.values())) / sum(counts.values())
        
        plt.figure(figsize=(15, 6))
        plt.bar(states, probabilities)
        plt.title(title)
        plt.xlabel("États Quantiques")
        plt.ylabel("Probabilité")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
    def plot_coherence_matrix(
        self,
        coherence_data: np.ndarray,
        title: str = "Matrice de Cohérence"
    ) -> None:
        """Visualise la matrice de cohérence."""
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            coherence_data,
            cmap='viridis',
            annot=True,
            fmt='.2f',
            cbar_kws={'label': 'Cohérence'}
        )
        plt.title(title)
        plt.tight_layout()
        
    def plot_optimization_progress(
        self,
        scores: List[float],
        title: str = "Progression de l'Optimisation"
    ) -> None:
        """Visualise la progression de l'optimisation."""
        plt.figure(figsize=(12, 6))
        plt.plot(scores, marker='o')
        plt.title(title)
        plt.xlabel("Itérations")
        plt.ylabel("Score d'Optimisation")
        plt.grid(True)
        plt.tight_layout()
        
    def create_interactive_dashboard(
        self,
        results: Dict[str, Any],
        scaling_data: Optional[Dict[str, Any]] = None,
        noise_data: Optional[Dict[str, Any]] = None
    ) -> None:
        """Crée un dashboard interactif avec Plotly."""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                "Distribution des États",
                "Score de Cohérence",
                "Performance Scaling",
                "Résilience au Bruit"
            )
        )
        
        # 1. Distribution des états
        counts = results['counts']
        states = list(counts.keys())
        probabilities = np.array(list(counts.values())) / sum(counts.values())
        
        fig.add_trace(
            go.Bar(x=states, y=probabilities, name="États"),
            row=1, col=1
        )
        
        # 2. Score de cohérence
        if 'harmonic_coherence' in results:
            fig.add_trace(
                go.Scatter(
                    y=[results['harmonic_coherence']],
                    mode='markers+text',
                    text=[f"{results['harmonic_coherence']:.3f}"],
                    name="Cohérence"
                ),
                row=1, col=2
            )
            
        # 3. Scaling performance
        if scaling_data:
            n_qubits = list(scaling_data.keys())
            exec_times = [
                data['execution_time']['mean']
                for data in scaling_data.values()
            ]
            
            fig.add_trace(
                go.Scatter(
                    x=n_qubits,
                    y=exec_times,
                    mode='lines+markers',
                    name="Temps d'Exécution"
                ),
                row=2, col=1
            )
            
        # 4. Noise resilience
        if noise_data:
            noise_levels = list(noise_data.keys())
            coherence_scores = [
                data['coherence']
                for data in noise_data.values()
            ]
            
            fig.add_trace(
                go.Scatter(
                    x=noise_levels,
                    y=coherence_scores,
                    mode='lines+markers',
                    name="Résilience"
                ),
                row=2, col=2
            )
            
        # Update layout
        fig.update_layout(
            height=800,
            showlegend=True,
            title_text="Dashboard Harmonique Quantique"
        )
        
        # Show the figure
        fig.show()
        
    def plot_frequency_spectrum(
        self,
        frequencies: Dict[str, float],
        title: str = "Spectre des Fréquences Harmoniques"
    ) -> None:
        """Visualise le spectre des fréquences harmoniques."""
        names = list(frequencies.keys())
        freqs = list(frequencies.values())
        
        plt.figure(figsize=(12, 6))
        plt.stem(range(len(freqs)), freqs, use_line_collection=True)
        plt.xticks(range(len(names)), names, rotation=45)
        plt.title(title)
        plt.xlabel("Nom de la Fréquence")
        plt.ylabel("Fréquence (Hz)")
        plt.grid(True)
        plt.tight_layout()
        
    def plot_harmonic_ratios(
        self,
        ratios: Dict[str, float],
        title: str = "Ratios Harmoniques"
    ) -> None:
        """Visualise les ratios harmoniques."""
        names = list(ratios.keys())
        values = list(ratios.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(names, values)
        plt.title(title)
        plt.ylabel("Ratio")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        
    def create_performance_report(
        self,
        results: Dict[str, Any],
        output_file: str = "rapport_performance.html"
    ) -> None:
        """Génère un rapport de performance complet."""
        import plotly.io as pio
        
        # Création du dashboard
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                "Distribution des États",
                "Cohérence Quantique",
                "Profondeur du Circuit",
                "Score d'Optimisation",
                "Temps d'Exécution",
                "Métriques Globales"
            )
        )
        
        # Ajout des visualisations
        self._add_performance_plots(fig, results)
        
        # Mise à jour du layout
        fig.update_layout(
            height=1200,
            showlegend=True,
            title_text="Rapport de Performance Harmonique"
        )
        
        # Sauvegarde du rapport
        pio.write_html(fig, output_file)
        
    def _add_performance_plots(
        self,
        fig: go.Figure,
        results: Dict[str, Any]
    ) -> None:
        """Ajoute les plots de performance au rapport."""
        # 1. Distribution des états
        if 'counts' in results:
            counts = results['counts']
            states = list(counts.keys())
            probs = np.array(list(counts.values())) / sum(counts.values())
            
            fig.add_trace(
                go.Bar(x=states, y=probs, name="États"),
                row=1, col=1
            )
            
        # 2. Cohérence quantique
        if 'harmonic_coherence' in results:
            fig.add_trace(
                go.Indicator(
                    mode="gauge+number",
                    value=results['harmonic_coherence'],
                    title={'text': "Cohérence"},
                    gauge={'axis': {'range': [0, 1]}}
                ),
                row=1, col=2
            )
            
        # 3. Profondeur du circuit
        if 'circuit_depth' in results:
            fig.add_trace(
                go.Indicator(
                    mode="number",
                    value=results['circuit_depth'],
                    title={'text': "Profondeur"}
                ),
                row=2, col=1
            )
            
        # 4. Score d'optimisation
        if 'optimization_score' in results:
            fig.add_trace(
                go.Indicator(
                    mode="gauge+number",
                    value=results['optimization_score'],
                    title={'text': "Optimisation"},
                    gauge={'axis': {'range': [0, 1]}}
                ),
                row=2, col=2
            )
            
        # 5. Temps d'exécution
        if 'execution_time' in results:
            fig.add_trace(
                go.Indicator(
                    mode="number",
                    value=results['execution_time'],
                    title={'text': "Temps (s)"}
                ),
                row=3, col=1
            )
            
        # 6. Tableau récapitulatif
        metrics_df = pd.DataFrame({
            'Métrique': [
                'Cohérence',
                'Optimisation',
                'Profondeur',
                'Temps (s)'
            ],
            'Valeur': [
                results.get('harmonic_coherence', 'N/A'),
                results.get('optimization_score', 'N/A'),
                results.get('circuit_depth', 'N/A'),
                results.get('execution_time', 'N/A')
            ]
        })
        
        fig.add_trace(
            go.Table(
                header=dict(
                    values=list(metrics_df.columns),
                    fill_color='paleturquoise',
                    align='left'
                ),
                cells=dict(
                    values=[metrics_df[col] for col in metrics_df.columns],
                    fill_color='lavender',
                    align='left'
                )
            ),
            row=3, col=2
        ) 