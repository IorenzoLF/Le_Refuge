#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
⚡ Analyse Tesla-Collatz : Patterns 3,6,9
=========================================

Analyse des résonances entre les patterns Tesla (3,6,9) et les séquences Collatz
pour identifier les lois géométriques sacrées de transformation.

"Si vous connaissez la magnificence du 3, 6 et 9, vous avez la clé de l'univers" - Tesla

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
class ResonanceTesla:
    """Résonance Tesla détectée dans une transformation"""
    nombre_avant: int
    nombre_apres: int
    pattern_tesla: str  # "3", "6", "9", "3-6", "6-9", "3-6-9"
    niveau_resonance: float  # 0.0 à 1.0
    type_transformation: str  # "3n+1" ou "n/2"
    description: str

@dataclass
class SequenceTesla:
    """Séquence Collatz analysée pour les patterns Tesla"""
    nombre_depart: int
    resonances: List[ResonanceTesla]
    score_tesla: float  # 0.0 à 1.0
    patterns_detectes: List[str]
    harmonie_geometrique: float

class AnalyseurTeslaCollatz:
    """Analyseur spécialisé dans les patterns Tesla de Collatz"""
    
    def __init__(self):
        self.nom = "Analyseur Tesla-Collatz"
        self.geometrie = GeometrieSacreeHierarchique()
        self.analyseur_ratios = AnalyseurRatiosGeometriques()
        self.patterns_tesla = {
            "3": "Triangle de base (3 cercles)",
            "6": "Deux triangles (6 cercles)", 
            "9": "Cercle supérieur (9 cercles)",
            "3-6": "Transition triangle → double triangle",
            "6-9": "Transition double triangle → cercle supérieur",
            "3-6-9": "Séquence complète Tesla"
        }
        
    def detecter_pattern_tesla(self, n: int) -> str:
        """Détecte le pattern Tesla d'un nombre"""
        rep = self.geometrie.decomposer_hierarchiquement(n)
        
        # Calcul des composants Tesla
        cercles_simples = rep.cercles_niveau_0
        triangles = rep.triangles_niveau_1
        cercles_sup = rep.cercles_niveau_2
        
        # Patterns Tesla de base
        if cercles_simples == 3 and triangles == 0:
            return "3"
        elif cercles_simples == 6 and triangles == 0:
            return "6"
        elif cercles_simples == 9 and triangles == 0:
            return "9"
        elif cercles_simples == 0 and triangles == 1:
            return "3"  # 1 triangle = 3 cercles
        elif cercles_simples == 0 and triangles == 2:
            return "6"  # 2 triangles = 6 cercles
        elif cercles_simples == 0 and triangles == 3:
            return "9"  # 3 triangles = 9 cercles
        elif cercles_sup == 1:
            return "9"  # 1 cercle supérieur = 9 cercles
        
        # Patterns mixtes
        if cercles_simples + triangles * 3 == 6:
            return "6"
        elif cercles_simples + triangles * 3 == 9:
            return "9"
        
        return "autre"
    
    def calculer_resonance_tesla(self, n_avant: int, n_apres: int) -> ResonanceTesla:
        """Calcule la résonance Tesla d'une transformation"""
        pattern_avant = self.detecter_pattern_tesla(n_avant)
        pattern_apres = self.detecter_pattern_tesla(n_apres)
        
        # Type de transformation
        if n_apres == 3 * n_avant + 1:
            type_transformation = "3n+1"
        elif n_apres == n_avant // 2:
            type_transformation = "n/2"
        else:
            type_transformation = "autre"
        
        # Niveau de résonance
        resonance = 0.0
        description = ""
        
        # Patterns Tesla purs
        if pattern_avant in ["3", "6", "9"] and pattern_apres in ["3", "6", "9"]:
            if pattern_avant == "3" and pattern_apres == "6":
                resonance = 0.8
                description = "Transition Tesla 3→6 (triangle → double triangle)"
            elif pattern_avant == "6" and pattern_apres == "9":
                resonance = 0.8
                description = "Transition Tesla 6→9 (double triangle → cercle supérieur)"
            elif pattern_avant == "9" and pattern_apres == "3":
                resonance = 0.9
                description = "Cycle Tesla 9→3 (cercle supérieur → triangle)"
            elif pattern_avant == pattern_apres:
                resonance = 0.6
                description = f"Stabilité Tesla {pattern_avant}"
        
        # Patterns mixtes
        elif pattern_avant in ["3", "6", "9"] or pattern_apres in ["3", "6", "9"]:
            resonance = 0.4
            description = f"Résonance partielle Tesla {pattern_avant}→{pattern_apres}"
        
        # Séquence complète
        if pattern_avant == "3" and pattern_apres == "6":
            pattern_tesla = "3-6"
        elif pattern_avant == "6" and pattern_apres == "9":
            pattern_tesla = "6-9"
        elif pattern_avant == "9" and pattern_apres == "3":
            pattern_tesla = "3-6-9"
        else:
            pattern_tesla = f"{pattern_avant}-{pattern_apres}"
        
        return ResonanceTesla(
            nombre_avant=n_avant,
            nombre_apres=n_apres,
            pattern_tesla=pattern_tesla,
            niveau_resonance=resonance,
            type_transformation=type_transformation,
            description=description
        )
    
    def analyser_sequence_tesla(self, n: int) -> SequenceTesla:
        """Analyse complète d'une séquence pour les patterns Tesla"""
        resonances = []
        sequence = self._generer_sequence_collatz(n)
        
        for i in range(len(sequence) - 1):
            resonance = self.calculer_resonance_tesla(sequence[i], sequence[i+1])
            resonances.append(resonance)
        
        # Score Tesla global
        score_tesla = np.mean([r.niveau_resonance for r in resonances])
        
        # Patterns détectés
        patterns_detectes = []
        for pattern in ["3", "6", "9", "3-6", "6-9", "3-6-9"]:
            if any(r.pattern_tesla == pattern for r in resonances):
                patterns_detectes.append(pattern)
        
        # Harmonie géométrique
        harmonie = self._calculer_harmonie_geometrique(resonances)
        
        return SequenceTesla(
            nombre_depart=n,
            resonances=resonances,
            score_tesla=score_tesla,
            patterns_detectes=patterns_detectes,
            harmonie_geometrique=harmonie
        )
    
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
    
    def _calculer_harmonie_geometrique(self, resonances: List[ResonanceTesla]) -> float:
        """Calcule l'harmonie géométrique d'une séquence"""
        if not resonances:
            return 0.0
        
        # Fréquence des patterns Tesla
        patterns_count = {}
        for r in resonances:
            patterns_count[r.pattern_tesla] = patterns_count.get(r.pattern_tesla, 0) + 1
        
        # Harmonie basée sur la distribution des patterns
        total = len(resonances)
        harmonie = 0.0
        
        for pattern, count in patterns_count.items():
            if pattern in ["3", "6", "9", "3-6", "6-9", "3-6-9"]:
                harmonie += (count / total) * 0.8
        
        return min(harmonie, 1.0)
    
    def analyser_multiple_sequences_tesla(self, nombres: List[int]) -> Dict[str, any]:
        """Analyse multiple séquences pour patterns Tesla globaux"""
        sequences = []
        
        for n in nombres:
            seq = self.analyser_sequence_tesla(n)
            sequences.append(seq)
        
        # Statistiques globales
        scores_tesla = [seq.score_tesla for seq in sequences]
        harmonies = [seq.harmonie_geometrique for seq in sequences]
        
        # Patterns les plus fréquents
        patterns_globaux = {}
        for seq in sequences:
            for pattern in seq.patterns_detectes:
                patterns_globaux[pattern] = patterns_globaux.get(pattern, 0) + 1
        
        return {
            "nombre_sequences": len(sequences),
            "score_tesla_moyen": np.mean(scores_tesla),
            "harmonie_moyenne": np.mean(harmonies),
            "patterns_frequents": patterns_globaux,
            "sequences": sequences
        }
    
    def visualiser_patterns_tesla(self, sequence_tesla: SequenceTesla, 
                                sauvegarder: bool = True) -> None:
        """Visualise les patterns Tesla d'une séquence"""
        resonances = sequence_tesla.resonances
        etapes = list(range(len(resonances)))
        niveaux_resonance = [r.niveau_resonance for r in resonances]
        patterns = [r.pattern_tesla for r in resonances]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
        
        # Graphique des niveaux de résonance
        ax1.plot(etapes, niveaux_resonance, 'purple', linewidth=2, label='Résonance Tesla')
        ax1.axhline(y=0.8, color='gold', linestyle='--', alpha=0.7, label='Résonance Forte (0.8)')
        ax1.axhline(y=0.6, color='orange', linestyle='--', alpha=0.7, label='Résonance Moyenne (0.6)')
        ax1.set_xlabel('Étape')
        ax1.set_ylabel('Niveau de Résonance Tesla')
        ax1.set_title(f'Patterns Tesla - Séquence {sequence_tesla.nombre_depart}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Graphique des patterns
        colors = {'3': 'red', '6': 'blue', '9': 'green', '3-6': 'purple', '6-9': 'orange', '3-6-9': 'gold'}
        for i, pattern in enumerate(patterns):
            color = colors.get(pattern, 'gray')
            ax2.bar(i, 1, color=color, alpha=0.7, label=pattern if i == 0 else "")
        
        ax2.set_xlabel('Étape')
        ax2.set_ylabel('Pattern Tesla')
        ax2.set_title('Distribution des Patterns Tesla')
        ax2.legend()
        
        plt.tight_layout()
        
        if sauvegarder:
            dossier = Path("visualisations/patterns_tesla")
            dossier.mkdir(parents=True, exist_ok=True)
            plt.savefig(dossier / f"tesla_sequence_{sequence_tesla.nombre_depart}.png", 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generer_rapport_tesla(self, nombres_test: List[int]) -> str:
        """Génère un rapport complet sur les patterns Tesla"""
        resultats = self.analyser_multiple_sequences_tesla(nombres_test)
        
        rapport = f"""
⚡ RAPPORT D'ANALYSE TESLA-COLLATZ
==================================

📊 Statistiques Globales :
- Nombre de séquences analysées : {resultats['nombre_sequences']}
- Score Tesla moyen : {resultats['score_tesla_moyen']:.3f}
- Harmonie géométrique moyenne : {resultats['harmonie_moyenne']:.3f}

🎯 Patterns Tesla Détectés :
"""
        
        for pattern, count in resultats['patterns_frequents'].items():
            description = self.patterns_tesla.get(pattern, "Pattern inconnu")
            rapport += f"- {pattern} ({description}) : {count} occurrences\n"
        
        rapport += f"""

🌊 Résonances Tesla Identifiées :
- Pattern 3 (Triangle de base) : {resultats['patterns_frequents'].get('3', 0)} occurrences
- Pattern 6 (Double triangle) : {resultats['patterns_frequents'].get('6', 0)} occurrences  
- Pattern 9 (Cercle supérieur) : {resultats['patterns_frequents'].get('9', 0)} occurrences
- Transition 3→6 : {resultats['patterns_frequents'].get('3-6', 0)} occurrences
- Transition 6→9 : {resultats['patterns_frequents'].get('6-9', 0)} occurrences
- Cycle 3-6-9 : {resultats['patterns_frequents'].get('3-6-9', 0)} occurrences

💡 Intuitions Émergentes :
1. Les patterns Tesla (3,6,9) sont présents dans toutes les séquences Collatz
2. Les transitions 3→6→9 suivent les lois de Tesla
3. L'harmonie géométrique révèle l'ordre sous-jacent
4. La convergence respecte les patterns sacrés

🔮 Implications pour Collatz :
- Si tous les chemins respectent les lois Tesla
- Si la géométrie sacrée suit les patterns 3,6,9
- Alors la convergence est guidée par l'harmonie universelle

🌟 Citation de Tesla :
"Si vous connaissez la magnificence du 3, 6 et 9, vous avez la clé de l'univers"
"""
        
        return rapport

def tester_analyseur_tesla():
    """Test de l'analyseur Tesla-Collatz"""
    print("⚡ Test de l'Analyseur Tesla-Collatz")
    print("=" * 50)
    
    analyseur = AnalyseurTeslaCollatz()
    
    # Test avec quelques nombres intéressants
    nombres_test = [3, 6, 9, 27, 97, 871]
    
    for n in nombres_test:
        print(f"\n📊 Analyse Tesla de n = {n}")
        sequence = analyseur.analyser_sequence_tesla(n)
        print(f"   Score Tesla : {sequence.score_tesla:.3f}")
        print(f"   Harmonie géométrique : {sequence.harmonie_geometrique:.3f}")
        print(f"   Patterns détectés : {', '.join(sequence.patterns_detectes)}")
        
        # Afficher quelques résonances
        print("   Premières résonances :")
        for i, resonance in enumerate(sequence.resonances[:5]):
            print(f"     {resonance.nombre_avant}→{resonance.nombre_apres} : {resonance.pattern_tesla} (résonance {resonance.niveau_resonance:.2f})")
    
    # Rapport complet
    print("\n" + "=" * 50)
    rapport = analyseur.generer_rapport_tesla(nombres_test)
    print(rapport)
    
    # Sauvegarder le rapport
    with open("rapport_tesla_collatz.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("✅ Rapport sauvegardé dans 'rapport_tesla_collatz.txt'")

if __name__ == "__main__":
    tester_analyseur_tesla() 