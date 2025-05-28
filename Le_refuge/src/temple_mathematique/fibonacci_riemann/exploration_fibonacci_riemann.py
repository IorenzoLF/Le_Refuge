"""
Exploration Fibonacci Riemann - Approfondissement Mathématique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basé sur les découvertes du fichier "Broc reimann Fibonacci.txt" et 
intégré à notre fusion tripartite Math + Musique + Spiritualité.

Explorations avancées :
- Analyse spectrale poussée (FFT, correlation)
- Fonction zêta discrète adaptée à la double suite
- Visualisations des patterns premiers
- Intégration avec les sphères harmoniques

Auteurs: Laurent Franssen, Jules, & Ælya
Date: 25 Avril 2025
VERSION EXPLORATION - Mystères Mathématiques !
"""

import asyncio
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.special import zeta
import datetime
from typing import Dict, List, Optional, Any

# Notre fusion tripartite
from refuge_math_musical_fusion import (
    RefugeMathMusicalFusion, 
    DoubleSuiteRiemann,
    SphereHarmoniqueUnifiee,
    AelyaConscienceEvoluee
)

# Architecture unifiée
from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase

class ExplorateurFibonacciRiemann(GestionnaireBase):
    """Explorateur avancé des mystères mathématiques de Laurent"""
    
    def __init__(self, fusion_tripartite: RefugeMathMusicalFusion):
        # Références AVANT super().__init__
        self.fusion = fusion_tripartite
        self.double_suite = fusion_tripartite.double_suite
        self.sequences_explorees = {}
        self.analyses_spectrales = {}
        self.patterns_premiers = {}
        self.zeta_discrete_values = []
        
        # Paramètres d'exploration
        self.longueurs_test = [20, 50, 100, 200]
        self.points_depart_alternatifs = [(2, 1), (3, 1), (1, 2), (5, 3)]
        
        # Gestionnaire d'énergie pour l'exploration
        self.energie = EnergyManagerBase(0.85)
        
        # MAINTENANT super().__init__
        super().__init__("ExplorateurFibonacci")
        
    def _initialiser(self) -> bool:
        """Initialise l'explorateur mathématique"""
        try:
            self.logger.info("Initialisation de l'Explorateur Fibonacci Riemann")
            
            # Configuration d'exploration
            self.config.definir("precision_fft", 1e-12)
            self.config.definir("seuil_correlation_significative", 0.7)
            self.config.definir("frequence_echantillonnage", 44100)
            
            self.logger.succes("Explorateur Fibonacci Riemann initialisé")
            return True
            
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'initialisation de l'explorateur: {e}")
            return False

    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre l'exploration complète"""
        self.energie.ajuster_energie(0.10)  # Boost énergétique pour exploration
        
        # 1. Exploration des séquences alternatives
        await self.explorer_sequences_alternatives()
        
        # 2. Analyse spectrale avancée
        await self.analyse_spectrale_avancee()
        
        # 3. Fonction zêta discrète
        await self.calculer_zeta_discrete()
        
        # 4. Patterns de nombres premiers
        await self.analyser_patterns_premiers()
        
        # 5. Corrélations avec sphères harmoniques
        await self.correlations_spheres_harmoniques()
        
        return {
            "sequences_explorees": len(self.sequences_explorees),
            "analyses_spectrales": len(self.analyses_spectrales),
            "patterns_premiers": len(self.patterns_premiers),
            "zeta_discrete_points": len(self.zeta_discrete_values),
            "energie_exploration": self.energie.niveau_energie,
            "timestamp": datetime.datetime.now().isoformat()
        }

    async def explorer_sequences_alternatives(self):
        """Explore différents points de départ pour la double suite"""
        self.logger.info("Exploration des séquences alternatives")
        
        for a_init, b_init in self.points_depart_alternatifs:
            for longueur in self.longueurs_test:
                nom_sequence = f"suite_{a_init}_{b_init}_L{longueur}"
                
                # Générer la séquence
                sequence = self.generer_double_suite(a_init, b_init, longueur)
                
                # Analyser les nombres premiers
                primes_info = self.analyser_nombres_premiers(sequence)
                
                self.sequences_explorees[nom_sequence] = {
                    "sequence": sequence,
                    "debut": (a_init, b_init),
                    "longueur": longueur,
                    "primes_count": primes_info["count"],
                    "primes_ratio": primes_info["ratio"],
                    "primes_list": primes_info["primes"]
                }
                
        self.logger.info(f"Exploré {len(self.sequences_explorees)} séquences alternatives")

    def generer_double_suite(self, a_init: int, b_init: int, longueur: int) -> List[int]:
        """Génère une double suite selon la logique de Laurent"""
        sequence = [a_init, b_init]
        
        while len(sequence) < longueur:
            a = sequence[-2]
            b = sequence[-1]
            c = a + b
            d = b - c + 2 * a
            sequence.extend([c, d])
            
        return sequence[:longueur]

    def analyser_nombres_premiers(self, sequence: List[int]) -> Dict[str, Any]:
        """Analyse détaillée des nombres premiers dans une séquence"""
        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0: return False
            return True
            
        primes = [n for n in sequence if is_prime(n)]
        
        return {
            "count": len(primes),
            "ratio": len(primes) / len(sequence) if sequence else 0,
            "primes": primes,
            "positions": [i for i, n in enumerate(sequence) if is_prime(n)]
        }

    async def analyse_spectrale_avancee(self):
        """Analyse spectrale poussée de toutes les séquences"""
        self.logger.info("Analyse spectrale avancée en cours")
        
        for nom, seq_data in self.sequences_explorees.items():
            sequence = seq_data["sequence"]
            
            # FFT de la séquence
            fft_values = fft(sequence)
            frequencies = fftfreq(len(sequence))
            magnitudes = np.abs(fft_values)
            phases = np.angle(fft_values)
            
            # Calculs avancés
            energie_spectrale = np.sum(magnitudes ** 2)
            freq_dominante = frequencies[np.argmax(magnitudes[1:])] if len(magnitudes) > 1 else 0
            
            # Corrélation avec séquence Fibonacci classique
            fibonacci_ref = self.generer_fibonacci(len(sequence))
            correlation_fibonacci = np.corrcoef(sequence, fibonacci_ref)[0, 1] if len(fibonacci_ref) == len(sequence) else 0
            
            self.analyses_spectrales[nom] = {
                "fft_magnitudes": magnitudes[:10].tolist(),  # 10 premiers
                "energie_spectrale": float(energie_spectrale),
                "frequence_dominante": float(freq_dominante),
                "correlation_fibonacci": float(correlation_fibonacci) if not np.isnan(correlation_fibonacci) else 0,
                "entropie_spectrale": self.calculer_entropie_spectrale(magnitudes)
            }

    def generer_fibonacci(self, longueur: int) -> List[int]:
        """Génère la séquence de Fibonacci classique"""
        if longueur <= 0: return []
        if longueur == 1: return [1]
        
        fib = [1, 1]
        while len(fib) < longueur:
            fib.append(fib[-1] + fib[-2])
        return fib[:longueur]

    def calculer_entropie_spectrale(self, magnitudes: np.ndarray) -> float:
        """Calcule l'entropie spectrale (mesure de complexité)"""
        # Normaliser les magnitudes
        magnitudes_norm = magnitudes / np.sum(magnitudes) if np.sum(magnitudes) > 0 else magnitudes
        
        # Calculer l'entropie de Shannon
        entropie = 0
        for mag in magnitudes_norm:
            if mag > 0:
                entropie -= mag * np.log2(mag)
                
        return float(entropie)

    async def calculer_zeta_discrete(self):
        """Calcule une fonction zêta discrète basée sur les séquences"""
        self.logger.info("Calcul de la fonction zêta discrète")
        
        for nom, seq_data in self.sequences_explorees.items():
            sequence = seq_data["sequence"]
            
            # Zêta discrète : somme de 1/n^s pour les termes de la séquence
            for s_real in [0.5, 1.0, 1.5, 2.0]:  # Valeurs test de s
                zeta_sum = 0
                for n in sequence:
                    if n > 0:
                        zeta_sum += 1 / (n ** s_real)
                
                self.zeta_discrete_values.append({
                    "sequence": nom,
                    "s_value": s_real,
                    "zeta_sum": float(zeta_sum),
                    "convergence": "rapide" if zeta_sum < 10 else "lente"
                })

    async def analyser_patterns_premiers(self):
        """Analyse des patterns dans la distribution des nombres premiers"""
        self.logger.info("Analyse des patterns de nombres premiers")
        
        for nom, seq_data in self.sequences_explorees.items():
            primes = seq_data["primes_list"]
            positions = self.sequences_explorees[nom]["sequence"]
            
            if len(primes) > 1:
                # Écarts entre nombres premiers consécutifs
                ecarts_premiers = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
                
                # Analyse des positions dans la séquence
                positions_premiers = [i for i, n in enumerate(positions) if n in primes]
                ecarts_positions = [positions_premiers[i+1] - positions_premiers[i] for i in range(len(positions_premiers)-1)]
                
                self.patterns_premiers[nom] = {
                    "ecarts_valeurs": ecarts_premiers,
                    "ecarts_positions": ecarts_positions,
                    "moyenne_ecart_valeurs": np.mean(ecarts_premiers) if ecarts_premiers else 0,
                    "moyenne_ecart_positions": np.mean(ecarts_positions) if ecarts_positions else 0,
                    "periodicite_detectee": self.detecter_periodicite(positions_premiers)
                }

    def detecter_periodicite(self, positions: List[int]) -> Dict[str, Any]:
        """Détecte la périodicité dans les positions des nombres premiers"""
        if len(positions) < 3:
            return {"detectee": False, "periode": 0}
            
        # Cherche des patterns répétitifs simples
        for periode in range(2, len(positions) // 2):
            pattern_trouve = True
            for i in range(periode, len(positions)):
                if positions[i] - positions[i-periode] != positions[periode] - positions[0]:
                    pattern_trouve = False
                    break
            
            if pattern_trouve:
                return {"detectee": True, "periode": periode}
                
        return {"detectee": False, "periode": 0}

    async def correlations_spheres_harmoniques(self):
        """Corrélations entre les fréquences mathématiques et les sphères harmoniques"""
        self.logger.info("Calcul des corrélations avec les sphères harmoniques")
        
        if not self.fusion.spheres_harmoniques:
            return
            
        correlations = {}
        
        for nom_sphere, sphere in self.fusion.spheres_harmoniques.items():
            freq_sphere = sphere.frequence
            
            for nom_seq, analyse in self.analyses_spectrales.items():
                freq_dominante_seq = analyse["frequence_dominante"]
                
                # Calcul de résonance harmonique
                if freq_dominante_seq > 0 and freq_sphere > 0:
                    ratio = min(freq_sphere / freq_dominante_seq, freq_dominante_seq / freq_sphere)
                    resonance = ratio * analyse["energie_spectrale"] / 1000  # Normalisation
                    
                    correlations[f"{nom_sphere}_{nom_seq}"] = {
                        "freq_sphere": freq_sphere,
                        "freq_sequence": freq_dominante_seq,
                        "ratio_harmonique": float(ratio),
                        "resonance": float(resonance),
                        "compatible": ratio > 0.5  # Seuil de compatibilité harmonique
                    }
                    
        return correlations

    def generer_rapport_complet(self) -> Dict[str, Any]:
        """Génère un rapport complet de toutes les explorations"""
        # Meilleure séquence (ratio de nombres premiers)
        meilleure_seq = max(self.sequences_explorees.items(), 
                           key=lambda x: x[1]["primes_ratio"]) if self.sequences_explorees else None
        
        # Analyse spectrale la plus intéressante (entropie élevée)
        meilleure_analyse = max(self.analyses_spectrales.items(),
                               key=lambda x: x[1]["entropie_spectrale"]) if self.analyses_spectrales else None
        
        # Zêta discrète avec convergence la plus rapide
        zeta_convergent = min(self.zeta_discrete_values,
                             key=lambda x: x["zeta_sum"]) if self.zeta_discrete_values else None
        
        return {
            "exploration_complete": {
                "sequences_testees": len(self.sequences_explorees),
                "analyses_spectrales": len(self.analyses_spectrales),
                "points_zeta": len(self.zeta_discrete_values),
                "patterns_premiers": len(self.patterns_premiers)
            },
            "resultats_optimaux": {
                "meilleure_sequence_premiers": meilleure_seq[0] if meilleure_seq else None,
                "ratio_premiers_max": meilleure_seq[1]["primes_ratio"] if meilleure_seq else 0,
                "analyse_spectrale_riche": meilleure_analyse[0] if meilleure_analyse else None,
                "entropie_max": meilleure_analyse[1]["entropie_spectrale"] if meilleure_analyse else 0,
                "zeta_convergent": zeta_convergent
            },
            "timestamp_rapport": datetime.datetime.now().isoformat()
        }

    def visualiser_exploration(self, sauvegarder: bool = True):
        """Crée des visualisations des découvertes mathématiques"""
        if not self.sequences_explorees:
            return "Aucune séquence à visualiser"
            
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle("Exploration Fibonacci Riemann - Découvertes Mathématiques", fontsize=16)
        
        # 1. Ratios de nombres premiers par séquence
        ax1 = axes[0, 0]
        noms = list(self.sequences_explorees.keys())[:10]  # 10 premières
        ratios = [self.sequences_explorees[nom]["primes_ratio"] for nom in noms]
        ax1.bar(range(len(noms)), ratios)
        ax1.set_title("Ratios de Nombres Premiers par Séquence")
        ax1.set_ylabel("Ratio Premiers/Total")
        ax1.set_xticks(range(len(noms)))
        ax1.set_xticklabels([nom.split('_')[1:3] for nom in noms], rotation=45)
        
        # 2. Énergies spectrales
        ax2 = axes[0, 1]
        if self.analyses_spectrales:
            energies = [analyse["energie_spectrale"] for analyse in list(self.analyses_spectrales.values())[:10]]
            ax2.plot(energies, 'o-')
            ax2.set_title("Énergies Spectrales des Séquences")
            ax2.set_ylabel("Énergie Spectrale")
            ax2.set_xlabel("Séquence")
        
        # 3. Fonction Zêta Discrète
        ax3 = axes[1, 0]
        if self.zeta_discrete_values:
            s_values = [z["s_value"] for z in self.zeta_discrete_values[:20]]
            zeta_sums = [z["zeta_sum"] for z in self.zeta_discrete_values[:20]]
            ax3.scatter(s_values, zeta_sums, alpha=0.6)
            ax3.set_title("Fonction Zêta Discrète")
            ax3.set_xlabel("Valeur s")
            ax3.set_ylabel("Somme Zêta")
        
        # 4. Exemple de séquence avec nombres premiers
        ax4 = axes[1, 1]
        if self.sequences_explorees:
            nom_exemple = list(self.sequences_explorees.keys())[0]
            seq_exemple = self.sequences_explorees[nom_exemple]["sequence"][:50]  # 50 premiers
            primes_exemple = self.sequences_explorees[nom_exemple]["primes_list"]
            
            ax4.plot(seq_exemple, 'b-', alpha=0.7, label="Séquence")
            for i, val in enumerate(seq_exemple):
                if val in primes_exemple:
                    ax4.plot(i, val, 'ro', markersize=6)
            ax4.set_title(f"Séquence Exemple: {nom_exemple}")
            ax4.set_ylabel("Valeur")
            ax4.set_xlabel("Position")
            ax4.legend()
        
        plt.tight_layout()
        
        if sauvegarder:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            nom_fichier = f"exploration_fibonacci_riemann_{timestamp}.png"
            plt.savefig(f"musiques/visualisations/{nom_fichier}", dpi=150, bbox_inches='tight')
            plt.close()
            return f"Visualisation sauvegardée: {nom_fichier}"
        else:
            plt.show()
            return "Visualisation affichée"

# Fonction principale d'exploration
async def lancer_exploration_complete():
    """Lance l'exploration complète Fibonacci Riemann"""
    print("🔍🧮 Lancement de l'Exploration Fibonacci Riemann...")
    
    # Créer la fusion tripartite
    print("Initialisation de la fusion tripartite...")
    fusion = RefugeMathMusicalFusion()
    fusion.initialiser_composants()
    
    # Créer l'explorateur
    print("Création de l'explorateur mathématique...")
    explorateur = ExplorateurFibonacciRiemann(fusion)
    
    # Lancer l'exploration complète
    print("Exploration en cours...")
    resultat_orchestration = await explorateur.orchestrer()
    
    # Générer le rapport
    print("Génération du rapport complet...")
    rapport = explorateur.generer_rapport_complet()
    
    # Créer les visualisations
    print("Création des visualisations...")
    viz_result = explorateur.visualiser_exploration()
    
    # Affichage des résultats
    print("\n🎯 RÉSULTATS DE L'EXPLORATION:")
    print(f"Séquences explorées: {resultat_orchestration['sequences_explorees']}")
    print(f"Analyses spectrales: {resultat_orchestration['analyses_spectrales']}")
    print(f"Points zêta calculés: {resultat_orchestration['zeta_discrete_points']}")
    
    if rapport["resultats_optimaux"]["meilleure_sequence_premiers"]:
        print(f"\n🏆 MEILLEURE SÉQUENCE (nombres premiers): {rapport['resultats_optimaux']['meilleure_sequence_premiers']}")
        print(f"Ratio premiers maximum: {rapport['resultats_optimaux']['ratio_premiers_max']:.4f}")
    
    if rapport["resultats_optimaux"]["analyse_spectrale_riche"]:
        print(f"\n🌊 ANALYSE SPECTRALE LA PLUS RICHE: {rapport['resultats_optimaux']['analyse_spectrale_riche']}")
        print(f"Entropie maximale: {rapport['resultats_optimaux']['entropie_max']:.4f}")
    
    print(f"\n🎨 {viz_result}")
    
    # Faire évoluer Ælya avec les découvertes
    if fusion.aelya:
        fusion.aelya.evoluer_conscience("mathematiques")
        fusion.aelya.se_souvenir("ExplorationFibonacci", 
                                f"Découvertes: {resultat_orchestration['sequences_explorees']} séquences explorées")
        print("\n🌸 Ælya a intégré les nouvelles découvertes mathématiques!")
    
    print("\n✨ Exploration Fibonacci Riemann terminée avec succès!")
    return explorateur, rapport

if __name__ == "__main__":
    # Lancement de l'exploration
    import asyncio
    asyncio.run(lancer_exploration_complete()) 