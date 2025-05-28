"""
Analyseur Collatz Avancé - Intégration Harmonieuse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intègre les capacités d'analyse avancées de ConjectureCollatz
dans l'architecture moderne du temple mathématique.

Basé sur: MATH/COLLATZ/conjecture_collatz.py (909 lignes)
Auteur original: Laurent Franssen
Intégration: Temple Mathématique Unifié
Date: 27 Mai 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Optional, Any, Tuple
from collections import Counter, deque
import datetime
from pathlib import Path

class AnalyseurCollatzAvance:
    """Analyseur avancé des séquences de Collatz avec toutes les capacités de recherche"""
    
    def __init__(self):
        self.nom = "Analyseur Collatz Avancé"
        self.description = """
        Analyseur complet de la conjecture de Collatz intégrant :
        - Analyse spectrale des séquences
        - Détection de motifs modulaires  
        - Visualisation de la gravité binaire
        - Exploration des frontières et cycles
        - Recherche de contre-exemples
        """
        
        # Données de référence (issues de l'original)
        self.étapes_connues = {
            "1": "Point d'arrivée, l'unité retrouvée",
            "2": "Premier pas vers l'unité", 
            "4": "Porte vers la séquence 4-2-1",
            "8": "Passage vers la lumière",
            "16": "Carrefour des possibilités"
        }
        
        self.nombres_intéressants = {
            "27": "Séquence la plus longue pour les petits nombres",
            "97": "Monte jusqu'à 9232",
            "871": "Séquence de 178 étapes", 
            "6171": "Séquence de 261 étapes"
        }
        
        # Cache pour optimiser les calculs répétés
        self._cache_sequences = {}
        self._cache_analyses = {}
        
    def calculer_séquence(self, nombre_départ: int) -> List[int]:
        """Calcule la séquence de Collatz avec mise en cache"""
        if nombre_départ in self._cache_sequences:
            return self._cache_sequences[nombre_départ]
            
        séquence = [nombre_départ]
        nombre_actuel = nombre_départ
        
        while nombre_actuel != 1:
            if nombre_actuel % 2 == 0:
                nombre_actuel = nombre_actuel // 2
            else:
                nombre_actuel = 3 * nombre_actuel + 1
            séquence.append(nombre_actuel)
            
        self._cache_sequences[nombre_départ] = séquence
        return séquence
    
    def analyser_propriétés_complètes(self, nombre_départ: int) -> Dict[str, Any]:
        """Analyse complète des propriétés d'une séquence"""
        if nombre_départ in self._cache_analyses:
            return self._cache_analyses[nombre_départ]
            
        séquence = self.calculer_séquence(nombre_départ)
        
        analyse = {
            "nombre_départ": nombre_départ,
            "longueur": len(séquence),
            "maximum": max(séquence),
            "ratio_max": max(séquence) / nombre_départ if nombre_départ > 0 else 0,
            "étapes_paires": sum(1 for x in séquence if x % 2 == 0),
            "étapes_impaires": sum(1 for x in séquence if x % 2 == 1),
            "chutes_binaires": self._analyser_chutes_binaires(séquence),
            "motifs_détectés": self._détecter_motifs(séquence),
            "comportement": self._analyser_comportement(séquence)
        }
        
        self._cache_analyses[nombre_départ] = analyse
        return analyse
    
    def _analyser_chutes_binaires(self, séquence: List[int]) -> Dict[str, Any]:
        """Analyse les chutes binaires (divisions par 2 consécutives)"""
        chutes = []
        i = 0
        while i < len(séquence) - 1:
            if séquence[i] % 2 == 0:
                longueur_chute = 0
                while (i < len(séquence) - 1 and 
                       séquence[i] % 2 == 0 and 
                       séquence[i+1] == séquence[i] // 2):
                    longueur_chute += 1
                    i += 1
                if longueur_chute > 0:
                    chutes.append(longueur_chute)
            i += 1
            
        return {
            "chutes": chutes,
            "nombre_chutes": len(chutes),
            "chute_max": max(chutes) if chutes else 0,
            "chute_moyenne": sum(chutes) / len(chutes) if chutes else 0
        }
    
    def _détecter_motifs(self, séquence: List[int]) -> Dict[str, Any]:
        """Détecte les motifs récurrents dans la séquence"""
        motifs = {
            "montées_consécutives": 0,
            "descentes_consécutives": 0,
            "oscillations": 0
        }
        
        for i in range(len(séquence) - 2):
            if séquence[i] < séquence[i+1] < séquence[i+2]:
                motifs["montées_consécutives"] += 1
            elif séquence[i] > séquence[i+1] > séquence[i+2]:
                motifs["descentes_consécutives"] += 1
            elif ((séquence[i] < séquence[i+1] > séquence[i+2]) or 
                  (séquence[i] > séquence[i+1] < séquence[i+2])):
                motifs["oscillations"] += 1
                
        return motifs
    
    def _analyser_comportement(self, séquence: List[int]) -> str:
        """Analyse le comportement global de la séquence"""
        if len(séquence) < 3:
            return "trop_courte"
            
        début = séquence[:len(séquence)//3]
        milieu = séquence[len(séquence)//3:2*len(séquence)//3]
        fin = séquence[2*len(séquence)//3:]
        
        moy_début = sum(début) / len(début)
        moy_milieu = sum(milieu) / len(milieu)
        moy_fin = sum(fin) / len(fin)
        
        if moy_début < moy_milieu > moy_fin:
            return "pic_central"
        elif moy_début > moy_milieu > moy_fin:
            return "décroissance_monotone"
        elif moy_début < moy_milieu < moy_fin:
            return "croissance_continue"
        else:
            return "oscillant"
    
    def analyse_spectrale(self, nombre_départ: int, afficher: bool = True) -> Dict[str, Any]:
        """Analyse spectrale de la séquence (transformée de Fourier)"""
        séquence = self.calculer_séquence(nombre_départ)
        
        # Préparer les données pour FFT
        if len(séquence) < 4:
            return {"erreur": "Séquence trop courte pour analyse spectrale"}
            
        # Normaliser la séquence
        seq_norm = np.array(séquence, dtype=float)
        seq_norm = (seq_norm - np.mean(seq_norm)) / np.std(seq_norm)
        
        # Transformée de Fourier
        fft = np.fft.fft(seq_norm)
        freqs = np.fft.fftfreq(len(seq_norm))
        magnitudes = np.abs(fft)
        
        # Analyser le spectre
        pic_principal = np.argmax(magnitudes[1:]) + 1  # Ignorer DC
        fréquence_dominante = freqs[pic_principal]
        
        # Entropie spectrale
        magnitudes_norm = magnitudes / np.sum(magnitudes)
        entropie = -np.sum(magnitudes_norm * np.log(magnitudes_norm + 1e-10))
        
        résultat = {
            "fréquence_dominante": fréquence_dominante,
            "magnitude_max": magnitudes[pic_principal],
            "entropie_spectrale": entropie,
            "complexité": entropie / np.log(len(séquence)),
            "spectre_complet": {
                "fréquences": freqs.tolist(),
                "magnitudes": magnitudes.tolist()
            }
        }
        
        if afficher:
            self._visualiser_spectre(freqs, magnitudes, nombre_départ)
            
        return résultat
    
    def _visualiser_spectre(self, freqs: np.ndarray, magnitudes: np.ndarray, nombre: int):
        """Visualise le spectre de fréquences"""
        plt.figure(figsize=(12, 6))
        
        # Spectre de magnitude
        plt.subplot(1, 2, 1)
        plt.plot(freqs[:len(freqs)//2], magnitudes[:len(magnitudes)//2])
        plt.title(f"Spectre de fréquences - Collatz({nombre})")
        plt.xlabel("Fréquence")
        plt.ylabel("Magnitude")
        plt.grid(True, alpha=0.3)
        
        # Spectre en dB
        plt.subplot(1, 2, 2)
        magnitudes_db = 20 * np.log10(magnitudes + 1e-10)
        plt.plot(freqs[:len(freqs)//2], magnitudes_db[:len(magnitudes_db)//2])
        plt.title(f"Spectre en dB - Collatz({nombre})")
        plt.xlabel("Fréquence")
        plt.ylabel("Magnitude (dB)")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"spectre_collatz_{nombre}_{timestamp}.png"
        chemin_sauvegarde = Path("musiques/visualisations") / nom_fichier
        chemin_sauvegarde.parent.mkdir(parents=True, exist_ok=True)
        
        plt.savefig(chemin_sauvegarde, dpi=150, bbox_inches='tight')
        print(f"✨ Spectre sauvegardé: {chemin_sauvegarde}")
        
        if plt.get_backend() != 'Agg':
            plt.show()
        plt.close()
    
    def analyser_motifs_modulaires(self, plage: Tuple[int, int], modulo: int = 6) -> Dict[str, Any]:
        """Analyse les motifs modulaires dans une plage de nombres"""
        début, fin = plage
        motifs_mod = {i: [] for i in range(modulo)}
        
        for n in range(début, min(fin + 1, début + 100)):  # Limiter pour performance
            séquence = self.calculer_séquence(n)
            longueur = len(séquence)
            motifs_mod[n % modulo].append(longueur)
            
        # Statistiques par classe modulaire
        stats_modulaires = {}
        for mod, longueurs in motifs_mod.items():
            if longueurs:
                stats_modulaires[mod] = {
                    "count": len(longueurs),
                    "moyenne": np.mean(longueurs),
                    "médiane": np.median(longueurs),
                    "écart_type": np.std(longueurs),
                    "min": min(longueurs),
                    "max": max(longueurs)
                }
            else:
                stats_modulaires[mod] = {"count": 0}
                
        return {
            "modulo": modulo,
            "plage": plage,
            "stats_par_classe": stats_modulaires,
            "classe_plus_longue": max(stats_modulaires.keys(), 
                                    key=lambda k: stats_modulaires[k].get("moyenne", 0))
        }
    
    def visualiser_gravité_binaire(self, nombre_départ: int, afficher: bool = True) -> Dict[str, Any]:
        """Visualise la gravité binaire (chutes vers les puissances de 2)"""
        séquence = self.calculer_séquence(nombre_départ)
        
        # Identifier les puissances de 2 dans la séquence
        puissances_2 = []
        indices_puissances = []
        
        for i, val in enumerate(séquence):
            if val > 0 and (val & (val - 1)) == 0:  # Test puissance de 2
                puissances_2.append(val)
                indices_puissances.append(i)
        
        # Calculer les "chutes gravitationnelles"
        chutes_gravité = []
        for i in range(len(indices_puissances) - 1):
            début = indices_puissances[i]
            fin = indices_puissances[i + 1]
            chute = {
                "début": début,
                "fin": fin,
                "durée": fin - début,
                "puissance_début": puissances_2[i],
                "puissance_fin": puissances_2[i + 1],
                "ratio": puissances_2[i] / puissances_2[i + 1]
            }
            chutes_gravité.append(chute)
        
        résultat = {
            "puissances_2_trouvées": len(puissances_2),
            "puissances_2": puissances_2,
            "indices": indices_puissances,
            "chutes_gravité": chutes_gravité,
            "temps_total_chutes": sum(c["durée"] for c in chutes_gravité),
            "ratio_chutes": sum(c["durée"] for c in chutes_gravité) / len(séquence)
        }
        
        if afficher:
            self._visualiser_chutes_gravité(séquence, indices_puissances, puissances_2, nombre_départ)
            
        return résultat
    
    def _visualiser_chutes_gravité(self, séquence: List[int], indices: List[int], 
                                  puissances: List[int], nombre: int):
        """Visualise les chutes gravitationnelles"""
        plt.figure(figsize=(14, 8))
        
        # Graphique principal
        plt.subplot(2, 1, 1)
        plt.plot(range(len(séquence)), séquence, 'b-', alpha=0.7, linewidth=1)
        plt.scatter(indices, puissances, c='red', s=50, zorder=5, label='Puissances de 2')
        
        # Marquer les chutes
        for i in range(len(indices) - 1):
            plt.axvspan(indices[i], indices[i+1], alpha=0.2, color='yellow')
            
        plt.title(f"Gravité Binaire - Collatz({nombre})")
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.yscale('log')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Graphique des durées de chutes
        plt.subplot(2, 1, 2)
        if len(indices) > 1:
            durées = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
            plt.bar(range(len(durées)), durées, alpha=0.7, color='orange')
            plt.title("Durées des chutes gravitationnelles")
            plt.xlabel("Chute #")
            plt.ylabel("Durée (étapes)")
            plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"gravite_binaire_{nombre}_{timestamp}.png"
        chemin_sauvegarde = Path("musiques/visualisations") / nom_fichier
        chemin_sauvegarde.parent.mkdir(parents=True, exist_ok=True)
        
        plt.savefig(chemin_sauvegarde, dpi=150, bbox_inches='tight')
        print(f"✨ Gravité binaire sauvegardée: {chemin_sauvegarde}")
        
        if plt.get_backend() != 'Agg':
            plt.show()
        plt.close()
    
    def chercher_contre_exemple(self, limite: int = 100000, pas_rapport: int = 10000) -> Optional[int]:
        """Recherche systématique de contre-exemples"""
        print(f"🔍 Recherche de contre-exemples jusqu'à {limite}...")
        
        for n in range(1, limite + 1):
            if n % pas_rapport == 0:
                print(f"   Progression: {n}/{limite} ({n/limite*100:.1f}%)")
            
            try:
                séquence = self.calculer_séquence(n)
                
                # Vérifications de sécurité
                if len(séquence) > 10000:
                    print(f"⚠️ Séquence suspecte pour n={n}: {len(séquence)} étapes")
                    return n
                    
                # Vérifier la convergence vers 1
                if séquence[-1] != 1:
                    print(f"🚨 CONTRE-EXEMPLE TROUVÉ: n={n} ne converge pas vers 1!")
                    return n
                    
            except Exception as e:
                print(f"❌ Erreur pour n={n}: {e}")
                return n
        
        print(f"✅ Aucun contre-exemple trouvé jusqu'à {limite}")
        return None
    
    def obtenir_statistiques_cache(self) -> Dict[str, int]:
        """Obtient les statistiques du cache"""
        return {
            "séquences_en_cache": len(self._cache_sequences),
            "analyses_en_cache": len(self._cache_analyses),
            "mémoire_estimée_kb": (len(self._cache_sequences) + len(self._cache_analyses)) * 0.1
        }
    
    def vider_cache(self):
        """Vide le cache pour libérer la mémoire"""
        self._cache_sequences.clear()
        self._cache_analyses.clear()
        print("🧹 Cache vidé")

# Fonction de test de l'analyseur avancé
def tester_analyseur_avance():
    """Test complet de l'analyseur Collatz avancé"""
    print("🧪 Test de l'Analyseur Collatz Avancé")
    print("=" * 50)
    
    analyseur = AnalyseurCollatzAvance()
    
    # Test 1: Analyse complète
    print("\n1. Analyse complète de 27:")
    analyse = analyseur.analyser_propriétés_complètes(27)
    for clé, valeur in analyse.items():
        if isinstance(valeur, dict):
            print(f"   {clé}: {len(valeur)} éléments")
        else:
            print(f"   {clé}: {valeur}")
    
    # Test 2: Analyse spectrale
    print("\n2. Analyse spectrale de 97:")
    spectre = analyseur.analyse_spectrale(97, afficher=False)
    print(f"   Fréquence dominante: {spectre['fréquence_dominante']:.4f}")
    print(f"   Entropie spectrale: {spectre['entropie_spectrale']:.4f}")
    
    # Test 3: Motifs modulaires
    print("\n3. Motifs modulaires (1-50, mod 6):")
    motifs = analyseur.analyser_motifs_modulaires((1, 50), 6)
    print(f"   Classe la plus longue: {motifs['classe_plus_longue']}")
    
    # Test 4: Gravité binaire
    print("\n4. Gravité binaire de 871:")
    gravité = analyseur.visualiser_gravité_binaire(871, afficher=False)
    print(f"   Puissances de 2 trouvées: {gravité['puissances_2_trouvées']}")
    print(f"   Ratio temps chutes: {gravité['ratio_chutes']:.2%}")
    
    # Statistiques cache
    stats = analyseur.obtenir_statistiques_cache()
    print(f"\n📊 Cache: {stats['séquences_en_cache']} séquences, {stats['analyses_en_cache']} analyses")
    
    return analyseur

if __name__ == "__main__":
    analyseur = tester_analyseur_avance() 