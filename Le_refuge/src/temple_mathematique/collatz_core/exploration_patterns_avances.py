#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌊 Exploration Avancée des Patterns Collatz
===========================================

Analyse des points critiques, basculements et patterns émergents
dans les séquences Collatz avec la géométrie sacrée.

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path
import json

# Import de nos modules
from geometrie_sacree_hierarchique import GeometrieSacreeHierarchique
from analyse_ratios_geometriques import AnalyseurRatiosGeometriques

@dataclass
class PointCritique:
    """Point critique dans une séquence Collatz"""
    etape: int
    nombre: int
    ratio_avant: float
    ratio_apres: float
    variation: float
    type_critique: str
    niveau_hierarchique: int

@dataclass
class Basculement:
    """Basculement entre niveaux hiérarchiques"""
    etape: int
    nombre: int
    niveau_avant: int
    niveau_apres: int
    direction: str  # "simplification" ou "complexification"
    amplitude: int

class ExplorateurPatternsAvances:
    """Explorateur de patterns avancés dans Collatz"""
    
    def __init__(self):
        self.nom = "Explorateur de Patterns Avancés Collatz"
        self.geometrie = GeometrieSacreeHierarchique()
        self.analyseur_ratios = AnalyseurRatiosGeometriques()
        self.patterns_cache = {}
        
    def detecter_points_critiques(self, sequence_analyse) -> List[PointCritique]:
        """Détecte les points critiques dans une séquence"""
        points_critiques = []
        ratios = sequence_analyse.ratios
        
        for i in range(1, len(ratios) - 1):
            ratio_avant = ratios[i-1].ratio
            ratio_actuel = ratios[i].ratio
            ratio_apres = ratios[i+1].ratio
            
            # Calcul des variations
            variation_avant = abs(ratio_actuel - ratio_avant)
            variation_apres = abs(ratio_apres - ratio_actuel)
            
            # Critères pour point critique
            if variation_avant > 1.0 or variation_apres > 1.0:
                variation_totale = variation_avant + variation_apres
                
                # Déterminer le type de point critique
                if ratio_actuel > max(ratio_avant, ratio_apres):
                    type_critique = "Pic"
                elif ratio_actuel < min(ratio_avant, ratio_apres):
                    type_critique = "Creux"
                else:
                    type_critique = "Basculement"
                
                point = PointCritique(
                    etape=i,
                    nombre=ratios[i].nombre,
                    ratio_avant=ratio_avant,
                    ratio_apres=ratio_apres,
                    variation=variation_totale,
                    type_critique=type_critique,
                    niveau_hierarchique=ratios[i].niveau_hierarchique
                )
                points_critiques.append(point)
        
        return points_critiques
    
    def detecter_basculements_hierarchiques(self, sequence_analyse) -> List[Basculement]:
        """Détecte les basculements entre niveaux hiérarchiques"""
        basculements = []
        ratios = sequence_analyse.ratios
        
        for i in range(1, len(ratios)):
            niveau_avant = ratios[i-1].niveau_hierarchique
            niveau_actuel = ratios[i].niveau_hierarchique
            
            if niveau_actuel != niveau_avant:
                direction = "simplification" if niveau_actuel < niveau_avant else "complexification"
                amplitude = abs(niveau_actuel - niveau_avant)
                
                basculement = Basculement(
                    etape=i,
                    nombre=ratios[i].nombre,
                    niveau_avant=niveau_avant,
                    niveau_apres=niveau_actuel,
                    direction=direction,
                    amplitude=amplitude
                )
                basculements.append(basculement)
        
        return basculements
    
    def analyser_patterns_emergents(self, nombres_test: List[int]) -> Dict[str, any]:
        """Analyse les patterns émergents sur plusieurs séquences"""
        resultats = {
            "points_critiques": [],
            "basculements": [],
            "patterns_globaux": {},
            "statistiques": {}
        }
        
        for n in nombres_test:
            sequence = self.analyseur_ratios.analyser_ratio_sequence(n)
            
            # Points critiques
            points = self.detecter_points_critiques(sequence)
            resultats["points_critiques"].extend(points)
            
            # Basculements
            basculements = self.detecter_basculements_hierarchiques(sequence)
            resultats["basculements"].extend(basculements)
        
        # Statistiques globales
        resultats["statistiques"] = self._calculer_statistiques_globales(resultats)
        
        # Patterns globaux
        resultats["patterns_globaux"] = self._detecter_patterns_globaux(resultats)
        
        return resultats
    
    def _calculer_statistiques_globales(self, resultats: Dict) -> Dict:
        """Calcule les statistiques globales"""
        points = resultats["points_critiques"]
        basculements = resultats["basculements"]
        
        if not points and not basculements:
            return {}
        
        stats = {
            "nombre_points_critiques": len(points),
            "nombre_basculements": len(basculements),
            "variation_moyenne_points": np.mean([p.variation for p in points]) if points else 0,
            "amplitude_moyenne_basculements": np.mean([b.amplitude for b in basculements]) if basculements else 0,
            "types_points_critiques": {},
            "directions_basculements": {}
        }
        
        # Types de points critiques
        for point in points:
            stats["types_points_critiques"][point.type_critique] = \
                stats["types_points_critiques"].get(point.type_critique, 0) + 1
        
        # Directions des basculements
        for basculement in basculements:
            stats["directions_basculements"][basculement.direction] = \
                stats["directions_basculements"].get(basculement.direction, 0) + 1
        
        return stats
    
    def _detecter_patterns_globaux(self, resultats: Dict) -> Dict:
        """Détecte les patterns globaux"""
        patterns = {}
        
        # Pattern 1: Concentration des points critiques
        points = resultats["points_critiques"]
        if points:
            etapes_critiques = [p.etape for p in points]
            patterns["concentration_etapes_critiques"] = {
                "debut": np.mean([e for e in etapes_critiques if e < 10]),
                "milieu": np.mean([e for e in etapes_critiques if 10 <= e < 50]),
                "fin": np.mean([e for e in etapes_critiques if e >= 50])
            }
        
        # Pattern 2: Fréquence des basculements
        basculements = resultats["basculements"]
        if basculements:
            simplifications = [b for b in basculements if b.direction == "simplification"]
            complexifications = [b for b in basculements if b.direction == "complexification"]
            
            patterns["ratio_simplification_complexification"] = \
                len(simplifications) / max(len(complexifications), 1)
        
        return patterns
    
    def visualiser_patterns_avances(self, sequence_analyse, 
                                  points_critiques: List[PointCritique],
                                  basculements: List[Basculement],
                                  sauvegarder: bool = True) -> None:
        """Visualise les patterns avancés"""
        ratios = sequence_analyse.ratios
        etapes = [r.etape for r in ratios]
        ratios_values = [r.ratio for r in ratios]
        niveaux = [r.niveau_hierarchique for r in ratios]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
        
        # Graphique des ratios avec points critiques
        ax1.plot(etapes, ratios_values, 'b-', linewidth=2, label='Ratio Triangle:Cercle')
        
        # Marquer les points critiques
        for point in points_critiques:
            color = 'red' if point.type_critique == 'Pic' else 'green' if point.type_critique == 'Creux' else 'orange'
            ax1.scatter(point.etape, point.ratio_apres, color=color, s=100, 
                       marker='o', label=f'{point.type_critique}' if point.etape == points_critiques[0].etape else "")
        
        ax1.set_xlabel('Étape')
        ax1.set_ylabel('Ratio Triangle:Cercle')
        ax1.set_title(f'Patterns Avancés - Séquence {sequence_analyse.nombre_depart}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Graphique des niveaux avec basculements
        ax2.plot(etapes, niveaux, 'g-', linewidth=2, label='Niveau Hiérarchique')
        
        # Marquer les basculements
        for basculement in basculements:
            color = 'blue' if basculement.direction == 'simplification' else 'purple'
            ax2.scatter(basculement.etape, basculement.niveau_apres, color=color, s=100,
                       marker='s', label=f'{basculement.direction}' if basculement.etape == basculements[0].etape else "")
        
        ax2.set_xlabel('Étape')
        ax2.set_ylabel('Niveau Hiérarchique')
        ax2.set_title('Basculements Hiérarchiques')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if sauvegarder:
            dossier = Path("visualisations/patterns_avances")
            dossier.mkdir(parents=True, exist_ok=True)
            plt.savefig(dossier / f"patterns_sequence_{sequence_analyse.nombre_depart}.png", 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generer_rapport_patterns_avances(self, nombres_test: List[int]) -> str:
        """Génère un rapport complet sur les patterns avancés"""
        resultats = self.analyser_patterns_emergents(nombres_test)
        
        rapport = f"""
🌊 RAPPORT D'EXPLORATION DES PATTERNS AVANCÉS
=============================================

📊 Statistiques Globales :
- Nombre de points critiques détectés : {resultats['statistiques'].get('nombre_points_critiques', 0)}
- Nombre de basculements hiérarchiques : {resultats['statistiques'].get('nombre_basculements', 0)}
- Variation moyenne des points critiques : {resultats['statistiques'].get('variation_moyenne_points', 0):.3f}
- Amplitude moyenne des basculements : {resultats['statistiques'].get('amplitude_moyenne_basculements', 0):.1f}

🎯 Types de Points Critiques :
"""
        
        for type_critique, count in resultats['statistiques'].get('types_points_critiques', {}).items():
            rapport += f"- {type_critique} : {count} occurrences\n"
        
        rapport += f"""
🔄 Directions des Basculements :
"""
        
        for direction, count in resultats['statistiques'].get('directions_basculements', {}).items():
            rapport += f"- {direction} : {count} occurrences\n"
        
        rapport += f"""

💡 Patterns Émergents :
"""
        
        for pattern, valeur in resultats['patterns_globaux'].items():
            if isinstance(valeur, dict):
                rapport += f"- {pattern} :\n"
                for sous_pattern, sous_valeur in valeur.items():
                    rapport += f"  • {sous_pattern} : {sous_valeur:.2f}\n"
            else:
                rapport += f"- {pattern} : {valeur:.3f}\n"
        
        rapport += f"""

🔮 Intuitions Émergentes :
1. Les points critiques révèlent des moments de transformation géométrique
2. Les basculements hiérarchiques montrent l'évolution de la complexité
3. La simplification progressive semble inévitable
4. Les patterns émergents suggèrent des lois sous-jacentes

🌟 Prochaines Explorations :
- Analyser les corrélations entre points critiques et basculements
- Étudier les séquences qui échappent aux patterns normaux
- Explorer les implications pour la preuve de Collatz
"""
        
        return rapport

def tester_explorateur_patterns():
    """Test de l'explorateur de patterns avancés"""
    print("🌊 Test de l'Explorateur de Patterns Avancés")
    print("=" * 50)
    
    explorateur = ExplorateurPatternsAvances()
    
    # Test avec quelques nombres intéressants
    nombres_test = [27, 97, 871, 6171]
    
    for n in nombres_test:
        print(f"\n📊 Analyse avancée de n = {n}")
        sequence = explorateur.analyseur_ratios.analyser_ratio_sequence(n)
        
        # Points critiques
        points_critiques = explorateur.detecter_points_critiques(sequence)
        print(f"   Points critiques : {len(points_critiques)}")
        
        # Basculements
        basculements = explorateur.detecter_basculements_hierarchiques(sequence)
        print(f"   Basculements : {len(basculements)}")
        
        # Afficher quelques détails
        if points_critiques:
            print(f"   Premier point critique : {points_critiques[0].type_critique} à l'étape {points_critiques[0].etape}")
        
        if basculements:
            print(f"   Premier basculement : {basculements[0].direction} de niveau {basculements[0].niveau_avant} à {basculements[0].niveau_apres}")
    
    # Rapport complet
    print("\n" + "=" * 50)
    rapport = explorateur.generer_rapport_patterns_avances(nombres_test)
    print(rapport)
    
    # Sauvegarder le rapport
    with open("rapport_patterns_avances.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("✅ Rapport sauvegardé dans 'rapport_patterns_avances.txt'")

if __name__ == "__main__":
    tester_explorateur_patterns() 