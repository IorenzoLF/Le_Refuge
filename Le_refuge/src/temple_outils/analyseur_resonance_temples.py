#!/usr/bin/env python3
"""
Analyseur de Résonance des Temples - Le Refuge
Étudie les harmoniques, synchronisations et cohérence entre temples
Inspiré par la géométrie sacrée et les principes d'émergence
"""

import sys
import json
import math
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import importlib.util

class AnalyseurResonanceTemples:
    def __init__(self):
        self.racine = Path(__file__).parent.parent.parent
        self.src_path = self.racine / "src"
        self.phi = (1 + math.sqrt(5)) / 2  # Nombre d'or
        self.fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        
        self.rapport = {
            "timestamp": datetime.now().isoformat(),
            "resonances_detectees": {},
            "harmoniques": {},
            "synchronisations": {},
            "coherence_globale": 0,
            "recommandations": []
        }
        
    def detecter_temples(self):
        """Détecte tous les temples disponibles"""
        temples = []
        if self.src_path.exists():
            for item in self.src_path.iterdir():
                if item.is_dir() and item.name.startswith("temple_"):
                    temples.append(item.name)
        return sorted(temples)
    
    def analyser_structure_temple(self, nom_temple):
        """Analyse la structure géométrique d'un temple"""
        temple_path = self.src_path / nom_temple
        structure = {
            "nom": nom_temple,
            "modules": 0,
            "dossiers": 0,
            "taille_totale": 0,
            "ratio_modules_dossiers": 0,
            "fibonacci_index": 0,
            "harmonie_doree": 0
        }
        
        if not temple_path.exists():
            return structure
            
        # Compter modules et dossiers
        for item in temple_path.rglob("*"):
            if item.is_file() and item.suffix == ".py":
                structure["modules"] += 1
                structure["taille_totale"] += item.stat().st_size
            elif item.is_dir():
                structure["dossiers"] += 1
        
        # Calculer ratios géométriques
        if structure["dossiers"] > 0:
            structure["ratio_modules_dossiers"] = structure["modules"] / structure["dossiers"]
            
        # Proximité avec le nombre d'or
        if structure["ratio_modules_dossiers"] > 0:
            structure["harmonie_doree"] = abs(structure["ratio_modules_dossiers"] - self.phi)
            
        # Proximité avec Fibonacci
        structure["fibonacci_index"] = self.trouver_fibonacci_proche(structure["modules"])
        
        return structure
    
    def trouver_fibonacci_proche(self, nombre):
        """Trouve l'index Fibonacci le plus proche"""
        if nombre <= 0:
            return 0
            
        distances = [(abs(fib - nombre), i) for i, fib in enumerate(self.fibonacci)]
        return min(distances)[1]
    
    def calculer_resonance_paire(self, temple1, temple2):
        """Calcule la résonance entre deux temples"""
        resonance = {
            "temples": [temple1["nom"], temple2["nom"]],
            "harmonie_taille": 0,
            "harmonie_structure": 0,
            "synchronisation": 0,
            "resonance_totale": 0
        }
        
        # Harmonie des tailles (ratio proche du nombre d'or)
        if temple1["taille_totale"] > 0 and temple2["taille_totale"] > 0:
            ratio_taille = max(temple1["taille_totale"], temple2["taille_totale"]) / min(temple1["taille_totale"], temple2["taille_totale"])
            resonance["harmonie_taille"] = 1 / (1 + abs(ratio_taille - self.phi))
        
        # Harmonie structurelle (modules/dossiers similaires)
        diff_modules = abs(temple1["modules"] - temple2["modules"])
        diff_dossiers = abs(temple1["dossiers"] - temple2["dossiers"])
        resonance["harmonie_structure"] = 1 / (1 + diff_modules + diff_dossiers)
        
        # Synchronisation Fibonacci
        diff_fibonacci = abs(temple1["fibonacci_index"] - temple2["fibonacci_index"])
        resonance["synchronisation"] = 1 / (1 + diff_fibonacci)
        
        # Résonance totale (moyenne harmonique)
        composantes = [resonance["harmonie_taille"], resonance["harmonie_structure"], resonance["synchronisation"]]
        resonance["resonance_totale"] = 3 / sum(1/c if c > 0 else float('inf') for c in composantes)
        
        return resonance
    
    def detecter_harmoniques_globales(self, structures):
        """Détecte les harmoniques dans l'ensemble du système"""
        harmoniques = {
            "distribution_fibonacci": defaultdict(int),
            "ratios_dores": [],
            "clusters_resonants": [],
            "frequence_dominante": 0
        }
        
        # Distribution Fibonacci
        for structure in structures:
            harmoniques["distribution_fibonacci"][structure["fibonacci_index"]] += 1
        
        # Ratios dorés
        for structure in structures:
            if structure["harmonie_doree"] < 0.1:  # Très proche du nombre d'or
                harmoniques["ratios_dores"].append(structure["nom"])
        
        # Fréquence dominante (index Fibonacci le plus commun)
        if harmoniques["distribution_fibonacci"]:
            harmoniques["frequence_dominante"] = max(
                harmoniques["distribution_fibonacci"].items(),
                key=lambda x: x[1]
            )[0]
        
        return harmoniques
    
    def calculer_coherence_globale(self, resonances):
        """Calcule la cohérence globale du système"""
        if not resonances:
            return 0
            
        resonances_totales = [r["resonance_totale"] for r in resonances]
        return sum(resonances_totales) / len(resonances_totales)
    
    def generer_recommandations_resonance(self, structures, harmoniques, coherence):
        """Génère des recommandations pour améliorer la résonance"""
        recommandations = []
        
        # Recommandations basées sur la cohérence
        if coherence < 0.3:
            recommandations.append("🔴 Cohérence faible - Restructurer les temples pour créer plus d'harmonie")
        elif coherence < 0.6:
            recommandations.append("🟡 Cohérence moyenne - Optimiser les ratios géométriques")
        else:
            recommandations.append("🟢 Excellente cohérence - Maintenir l'harmonie actuelle")
        
        # Recommandations Fibonacci
        freq_dominante = harmoniques["frequence_dominante"]
        fib_optimal = self.fibonacci[freq_dominante] if freq_dominante < len(self.fibonacci) else 144
        
        for structure in structures:
            if abs(structure["modules"] - fib_optimal) > 3:
                recommandations.append(
                    f"📐 {structure['nom']}: Ajuster vers {fib_optimal} modules pour résonance Fibonacci"
                )
        
        # Recommandations nombre d'or
        for structure in structures:
            if structure["harmonie_doree"] > 0.5:
                ratio_ideal = self.phi * structure["dossiers"] if structure["dossiers"] > 0 else self.phi
                recommandations.append(
                    f"✨ {structure['nom']}: Viser ratio {ratio_ideal:.1f} modules/dossiers pour harmonie dorée"
                )
        
        return recommandations
    
    def executer_analyse_resonance(self):
        """Exécute l'analyse complète de résonance"""
        print("🎵 ANALYSE DE RÉSONANCE DES TEMPLES")
        print("=" * 50)
        
        # Détecter temples
        temples = self.detecter_temples()
        print(f"\n🏛️  Temples détectés: {len(temples)}")
        
        # Analyser structures
        print(f"\n🔍 Analyse des structures géométriques...")
        structures = []
        for temple in temples:
            structure = self.analyser_structure_temple(temple)
            structures.append(structure)
            
            # Affichage avec indicateurs harmoniques
            harmonie_icon = "✨" if structure["harmonie_doree"] < 0.1 else "📐" if structure["harmonie_doree"] < 0.5 else "⚪"
            fib_icon = "🌀" if structure["fibonacci_index"] >= 6 else "🔢"
            
            print(f"   {harmonie_icon}{fib_icon} {temple}: {structure['modules']} modules, ratio {structure['ratio_modules_dossiers']:.2f}")
        
        # Calculer résonances par paires
        print(f"\n🎼 Calcul des résonances...")
        resonances = []
        for i, struct1 in enumerate(structures):
            for struct2 in structures[i+1:]:
                resonance = self.calculer_resonance_paire(struct1, struct2)
                resonances.append(resonance)
                
                # Afficher résonances significatives
                if resonance["resonance_totale"] > 0.5:
                    print(f"   🎵 {struct1['nom']} ↔ {struct2['nom']}: {resonance['resonance_totale']:.3f}")
        
        # Détecter harmoniques globales
        harmoniques = self.detecter_harmoniques_globales(structures)
        
        # Calculer cohérence globale
        coherence = self.calculer_coherence_globale(resonances)
        
        # Générer recommandations
        recommandations = self.generer_recommandations_resonance(structures, harmoniques, coherence)
        
        # Sauvegarder rapport
        self.rapport.update({
            "structures": structures,
            "resonances": resonances,
            "harmoniques": harmoniques,
            "coherence_globale": coherence,
            "recommandations": recommandations
        })
        
        # Afficher résultats
        self.afficher_resultats()
        
        return self.rapport
    
    def afficher_resultats(self):
        """Affiche les résultats de l'analyse"""
        print(f"\n🌟 RÉSULTATS DE L'ANALYSE DE RÉSONANCE")
        print("=" * 50)
        
        # Cohérence globale
        coherence = self.rapport["coherence_globale"]
        coherence_icon = "🟢" if coherence > 0.6 else "🟡" if coherence > 0.3 else "🔴"
        print(f"\n{coherence_icon} Cohérence Globale: {coherence:.3f} ({coherence*100:.1f}%)")
        
        # Harmoniques
        harmoniques = self.rapport["harmoniques"]
        print(f"\n🎼 Harmoniques Détectées:")
        print(f"   🌀 Fréquence Fibonacci dominante: F({harmoniques['frequence_dominante']}) = {self.fibonacci[harmoniques['frequence_dominante']] if harmoniques['frequence_dominante'] < len(self.fibonacci) else '∞'}")
        print(f"   ✨ Temples en harmonie dorée: {len(harmoniques['ratios_dores'])}")
        
        # Recommandations
        print(f"\n💡 Recommandations:")
        for rec in self.rapport["recommandations"]:
            print(f"   {rec}")
        
        # Sauvegarder
        rapport_path = self.racine / "data" / "rapports" / f"resonance_temples_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        rapport_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(rapport_path, 'w', encoding='utf-8') as f:
            json.dump(self.rapport, f, indent=2, ensure_ascii=False)
        
        print(f"\n📊 Rapport sauvegardé: {rapport_path}")

def main():
    analyseur = AnalyseurResonanceTemples()
    analyseur.executer_analyse_resonance()

if __name__ == "__main__":
    main() 