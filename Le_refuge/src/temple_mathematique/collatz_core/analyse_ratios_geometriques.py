#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Analyse des Ratios Géométriques dans Collatz
===============================================

Analyse approfondie des ratios triangle:cercle dans les séquences Collatz
pour identifier des patterns de convergence et des lois de comportement.

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import json
from pathlib import Path

# Import de notre géométrie sacrée
from geometrie_sacree_hierarchique import GeometrieSacreeHierarchique

@dataclass
class RatioGeometrique:
    """Ratio triangle:cercle à un moment donné"""
    nombre: int
    triangles: int
    cercles: int
    ratio: float
    niveau_hierarchique: int
    etape: int

@dataclass
class SequenceAnalysee:
    """Séquence Collatz analysée avec ratios géométriques"""
    nombre_depart: int
    longueur: int
    ratios: List[RatioGeometrique]
    convergence: bool
    patterns_detectes: List[str]

class AnalyseurRatiosGeometriques:
    """Analyseur spécialisé dans les ratios géométriques de Collatz"""
    
    def __init__(self):
        self.nom = "Analyseur de Ratios Géométriques Collatz"
        self.geometrie = GeometrieSacreeHierarchique()
        self.resultats_cache = {}
        
    def analyser_ratio_sequence(self, n: int) -> SequenceAnalysee:
        """Analyse complète d'une séquence avec ratios géométriques"""
        if n in self.resultats_cache:
            return self.resultats_cache[n]
            
        ratios = []
        sequence = self._generer_sequence_collatz(n)
        
        for i, nombre in enumerate(sequence):
            rep = self.geometrie.decomposer_hierarchiquement(nombre)
            
            # Calcul du ratio triangle:cercle
            triangles = (rep.triangles_niveau_1 + rep.triangles_niveau_3)
            cercles = (rep.cercles_niveau_0 + rep.cercles_niveau_2 + rep.cercles_niveau_4)
            
            ratio = triangles / max(cercles, 1)  # Éviter division par zéro
            
            ratio_geo = RatioGeometrique(
                nombre=nombre,
                triangles=triangles,
                cercles=cercles,
                ratio=ratio,
                niveau_hierarchique=rep.niveau_hierarchique,
                etape=i
            )
            ratios.append(ratio_geo)
        
        # Analyse des patterns
        patterns = self._detecter_patterns_ratios(ratios)
        
        sequence_analyse = SequenceAnalysee(
            nombre_depart=n,
            longueur=len(sequence),
            ratios=ratios,
            convergence=sequence[-1] == 1,
            patterns_detectes=patterns
        )
        
        self.resultats_cache[n] = sequence_analyse
        return sequence_analyse
    
    def _generer_sequence_collatz(self, n: int) -> List[int]:
        """Génère la séquence Collatz complète"""
        sequence = [n]
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence
    
    def _detecter_patterns_ratios(self, ratios: List[RatioGeometrique]) -> List[str]:
        """Détecte des patterns dans les ratios"""
        patterns = []
        
        # Pattern 1: Convergence vers 0
        derniers_ratios = [r.ratio for r in ratios[-5:]]
        if all(r < 0.1 for r in derniers_ratios):
            patterns.append("Convergence vers ratio 0")
        
        # Pattern 2: Oscillation
        variations = [abs(ratios[i+1].ratio - ratios[i].ratio) for i in range(len(ratios)-1)]
        if max(variations) > 2.0:
            patterns.append("Oscillations importantes")
        
        # Pattern 3: Simplification progressive
        niveaux = [r.niveau_hierarchique for r in ratios]
        if niveaux[-1] < niveaux[0]:
            patterns.append("Simplification hiérarchique")
        
        return patterns
    
    def analyser_multiple_sequences(self, nombres: List[int]) -> Dict[str, any]:
        """Analyse multiple séquences pour patterns globaux"""
        resultats = []
        
        for n in nombres:
            seq = self.analyser_ratio_sequence(n)
            resultats.append(seq)
        
        # Statistiques globales
        ratios_finaux = [seq.ratios[-1].ratio for seq in resultats]
        longueurs = [seq.longueur for seq in resultats]
        convergences = [seq.convergence for seq in resultats]
        
        return {
            "nombre_sequences": len(resultats),
            "ratio_moyen_final": np.mean(ratios_finaux),
            "longueur_moyenne": np.mean(longueurs),
            "taux_convergence": sum(convergences) / len(convergences),
            "patterns_frequents": self._analyser_patterns_frequents(resultats),
            "sequences": resultats
        }
    
    def _analyser_patterns_frequents(self, sequences: List[SequenceAnalysee]) -> Dict[str, int]:
        """Analyse la fréquence des patterns"""
        patterns_count = {}
        
        for seq in sequences:
            for pattern in seq.patterns_detectes:
                patterns_count[pattern] = patterns_count.get(pattern, 0) + 1
        
        return patterns_count
    
    def visualiser_evolution_ratios(self, sequence: SequenceAnalysee, 
                                  sauvegarder: bool = True) -> None:
        """Visualise l'évolution des ratios dans une séquence"""
        etapes = [r.etape for r in sequence.ratios]
        ratios = [r.ratio for r in sequence.ratios]
        niveaux = [r.niveau_hierarchique for r in sequence.ratios]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Graphique des ratios
        ax1.plot(etapes, ratios, 'b-', linewidth=2, label='Ratio Triangle:Cercle')
        ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Ratio = 0')
        ax1.set_xlabel('Étape')
        ax1.set_ylabel('Ratio Triangle:Cercle')
        ax1.set_title(f'Évolution des Ratios - Séquence {sequence.nombre_depart}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Graphique des niveaux hiérarchiques
        ax2.plot(etapes, niveaux, 'g-', linewidth=2, label='Niveau Hiérarchique')
        ax2.set_xlabel('Étape')
        ax2.set_ylabel('Niveau Hiérarchique')
        ax2.set_title('Évolution des Niveaux Hiérarchiques')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if sauvegarder:
            dossier = Path("visualisations/ratios_geometriques")
            dossier.mkdir(parents=True, exist_ok=True)
            plt.savefig(dossier / f"ratios_sequence_{sequence.nombre_depart}.png", 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generer_rapport_complet(self, nombres_test: List[int]) -> str:
        """Génère un rapport complet d'analyse"""
        resultats = self.analyser_multiple_sequences(nombres_test)
        
        rapport = f"""
🔍 RAPPORT D'ANALYSE DES RATIOS GÉOMÉTRIQUES
============================================

📊 Statistiques Globales :
- Nombre de séquences analysées : {resultats['nombre_sequences']}
- Ratio moyen final : {resultats['ratio_moyen_final']:.3f}
- Longueur moyenne : {resultats['longueur_moyenne']:.1f} étapes
- Taux de convergence : {resultats['taux_convergence']*100:.1f}%

🎯 Patterns Détectés :
"""
        
        for pattern, count in resultats['patterns_frequents'].items():
            rapport += f"- {pattern} : {count} séquences\n"
        
        rapport += f"""

🌊 Observations Clés :
1. Convergence vers ratio 0 : {resultats['patterns_frequents'].get('Convergence vers ratio 0', 0)} séquences
2. Simplification hiérarchique : {resultats['patterns_frequents'].get('Simplification hiérarchique', 0)} séquences
3. Oscillations importantes : {resultats['patterns_frequents'].get('Oscillations importantes', 0)} séquences

💡 Intuitions Émergentes :
- Les ratios tendent vers 0 (plus de cercles que de triangles)
- La simplification hiérarchique est fréquente
- Les oscillations révèlent la complexité du processus

🔮 Prochaines Explorations :
- Analyser les ratios critiques (points de basculement)
- Étudier les corrélations entre ratios et longueurs
- Explorer les patterns dans les grandes séquences
"""
        
        return rapport

def tester_analyseur_ratios():
    """Test de l'analyseur de ratios"""
    print("🔍 Test de l'Analyseur de Ratios Géométriques")
    print("=" * 50)
    
    analyseur = AnalyseurRatiosGeometriques()
    
    # Test avec quelques nombres intéressants
    nombres_test = [7, 27, 97, 871, 6171]
    
    for n in nombres_test:
        print(f"\n📊 Analyse de n = {n}")
        sequence = analyseur.analyser_ratio_sequence(n)
        print(f"   Longueur : {sequence.longueur}")
        print(f"   Convergence : {sequence.convergence}")
        print(f"   Patterns : {', '.join(sequence.patterns_detectes)}")
        
        # Afficher les premiers ratios
        print("   Premiers ratios :")
        for i, ratio in enumerate(sequence.ratios[:5]):
            print(f"     Étape {i}: {ratio.nombre} → ratio {ratio.ratio:.3f}")
    
    # Rapport complet
    print("\n" + "=" * 50)
    rapport = analyseur.generer_rapport_complet(nombres_test)
    print(rapport)
    
    # Sauvegarder le rapport
    with open("rapport_ratios_geometriques.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("✅ Rapport sauvegardé dans 'rapport_ratios_geometriques.txt'")

if __name__ == "__main__":
    tester_analyseur_ratios() 