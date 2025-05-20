"""
Ælya - Système de visualisation poétique des sphères problématiques.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime
from .gestion_sphères_problématiques import GestionnaireSphèresProblematiques, TypeSphereProblematique
from .visualisation_sphères_problématiques import VisualisationSphèresProblematiques

class Aelya:
    """Ælya - Gardienne des sphères problématiques dans les racines."""
    
    def __init__(self, gestionnaire: GestionnaireSphèresProblematiques):
        """Initialise Ælya."""
        self.gestionnaire = gestionnaire
        self.visualiseur = VisualisationSphèresProblematiques(gestionnaire)
        self.style = {
            'figure.figsize': (15, 10),
            'axes.titlesize': 14,
            'axes.labelsize': 12,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10
        }
        plt.style.use('dark_background')
        
    def visualiser_racines(self) -> None:
        """Visualise les sphères problématiques dans les racines."""
        fig = plt.figure(figsize=(15, 10))
        fig.suptitle("Les Racines du Cerisier - Ælya", fontsize=16, y=0.95)
        
        # Configuration de la grille
        gs = fig.add_gridspec(2, 2)
        
        # 1. État des confinements (graphique radar)
        ax1 = fig.add_subplot(gs[0, 0], projection='polar')
        self._visualiser_confinements(ax1)
        
        # 2. Énergie résiduelle (graphique à barres)
        ax2 = fig.add_subplot(gs[0, 1])
        self._visualiser_energie(ax2)
        
        # 3. Évolution temporelle (graphique linéaire)
        ax3 = fig.add_subplot(gs[1, 0])
        self._visualiser_evolution(ax3)
        
        # 4. Stabilité des racines (jauge)
        ax4 = fig.add_subplot(gs[1, 1])
        self._visualiser_stabilite(ax4)
        
        plt.tight_layout()
        plt.show()
        
    def _visualiser_confinements(self, ax: plt.Axes) -> None:
        """Visualise les niveaux de confinement."""
        types = [t.value for t in TypeSphereProblematique]
        angles = np.linspace(0, 2*np.pi, len(types), endpoint=False)
        
        # Fermeture du polygone
        angles = np.concatenate((angles, [angles[0]]))
        
        # Récupération des niveaux
        niveaux = []
        for type_sphere in TypeSphereProblematique:
            sphere = self.gestionnaire.obtenir_sphere(type_sphere)
            niveaux.append(sphere.niveau_confinement if sphere else 0)
        niveaux = np.concatenate((niveaux, [niveaux[0]]))
        
        # Tracé
        ax.plot(angles, niveaux, 'o-', linewidth=2, color='#FF69B4')
        ax.fill(angles, niveaux, alpha=0.25, color='#FF69B4')
        
        # Configuration
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(types)
        ax.set_ylim(0, 1)
        ax.set_title("Niveaux de Confinement", pad=20)
        
    def _visualiser_energie(self, ax: plt.Axes) -> None:
        """Visualise l'énergie résiduelle."""
        types = []
        energies = []
        
        for type_sphere in TypeSphereProblematique:
            sphere = self.gestionnaire.obtenir_sphere(type_sphere)
            if sphere:
                types.append(type_sphere.value)
                energies.append(sphere.energie_residuelle)
                
        if types:
            bars = ax.bar(types, energies, color='#4169E1')
            ax.set_ylim(0, 100)
            ax.set_title("Énergie Résiduelle")
            
            # Valeurs sur les barres
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.1f}',
                       ha='center', va='bottom')
                
    def _visualiser_evolution(self, ax: plt.Axes) -> None:
        """Visualise l'évolution temporelle."""
        dates = []
        energies = []
        
        for type_sphere in TypeSphereProblematique:
            sphere = self.gestionnaire.obtenir_sphere(type_sphere)
            if sphere and sphere.interactions:
                for interaction in sphere.interactions:
                    date = datetime.fromisoformat(interaction['date'])
                    dates.append(date)
                    energies.append(interaction['energie'])
                    
        if dates:
            ax.plot(dates, energies, 'o-', color='#32CD32')
            ax.set_title("Évolution des Interactions")
            ax.set_xlabel("Date")
            ax.set_ylabel("Énergie")
            plt.setp(ax.get_xticklabels(), rotation=45)
            
    def _visualiser_stabilite(self, ax: plt.Axes) -> None:
        """Visualise la stabilité des racines."""
        stabilite = self.gestionnaire.calculer_stabilite_racines()
        
        # Jauge
        ax.barh(['Stabilité'], [stabilite], color='#FFD700')
        ax.set_xlim(0, 1)
        ax.set_title("Stabilité des Racines")
        
        # Valeur
        ax.text(stabilite, 0, f'{stabilite:.0%}',
                ha='left', va='center')
                
    def generer_rapport_poetique(self) -> str:
        """Génère un rapport poétique des sphères problématiques."""
        rapport = [
            "🌳 Rapport Poétique d'Ælya 🌳",
            "============================",
            "",
            f"Dans les profondeurs des racines,",
            f"Ælya veille sur les sphères problématiques.",
            f"La stabilité des racines atteint {self.gestionnaire.calculer_stabilite_racines():.0%}.",
            "",
            "État des Confinements:"
        ]
        
        # Détails pour chaque sphère
        for type_sphere in TypeSphereProblematique:
            sphere = self.gestionnaire.obtenir_sphere(type_sphere)
            if sphere:
                rapport.extend([
                    f"\n{type_sphere.value}:",
                    f"  • Niveau de confinement: {sphere.niveau_confinement:.0%}",
                    f"  • Énergie résiduelle: {sphere.energie_residuelle:.1f}",
                    f"  • Date de confinement: {sphere.date_confinement.strftime('%Y-%m-%d')}",
                    f"  • Dernière interaction: {sphere.interactions[-1]['date'][:10] if sphere.interactions else 'Aucune'}"
                ])
                
        return "\n".join(rapport) 