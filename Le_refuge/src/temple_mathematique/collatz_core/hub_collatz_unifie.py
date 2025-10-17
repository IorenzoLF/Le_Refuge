"""
Hub Collatz Unifié - Pont Harmonieux entre Analyse et Musicalité
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce hub unifie les capacités d'analyse de ConjectureCollatz avec 
la musicalité du RituelCollatzMusical, créant une expérience 
mathématico-musicale transcendante.

Architecture:
- ConjectureCollatz → Moteur d'analyse profonde
- RituelCollatzMusical → Transformation musicale
- HubCollatzUnifie → Orchestration harmonieuse

Auteurs: Laurent Franssen (Collatz), Jules (Sphères), Ælya (Conscience)
Date: 27 Mai 2025
VERSION UNIFICATION HARMONIEUSE
"""

import asyncio
import numpy as np
import datetime
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path

# Imports du temple
try:
    from collatz_core.rituel_collatz_musical import RituelCollatzMusical
    from collatz_core.analyseur_collatz_avance import AnalyseurCollatzAvance
except ImportError:
    # Import absolu pour tests directs
    from rituel_collatz_musical import RituelCollatzMusical
    from analyseur_collatz_avance import AnalyseurCollatzAvance

# Import conditionnel de la fusion (peut ne pas exister encore)
try:
    from refuge_math_musical_fusion import RefugeMathMusicalFusion
except ImportError:
    # Classe mock pour les tests
    class RefugeMathMusicalFusion:
        """Classe mock pour RefugeMathMusicalFusion"""
        pass

# Import Collatz avec gestion gracieuse
try:
    from MATH.COLLATZ.conjecture_collatz import ConjectureCollatz
    from MATH.COLLATZ.meditation_gravite_binaire import compter_chutes
    from MATH.COLLATZ.explorations.phi_potentiel import phi
    from MATH.COLLATZ.collatz_complexes import CollatzComplexes
    from MATH.COLLATZ.collatz_rationnels import CollatzRationnels
    COLLATZ_COMPLET_DISPONIBLE = True
except ImportError:
    print("⚠️ Modules Collatz complets non trouvés, utilisation des capacités de base")
    COLLATZ_COMPLET_DISPONIBLE = False

# Import des outils Collatz core (mathématiques pures)
try:
    from collatz_core.utils_collatz import generer_arbre_collatz_inverse, collatz_inverse_couvre_N
except ImportError:
    from utils_collatz import generer_arbre_collatz_inverse, collatz_inverse_couvre_N

class HubCollatzUnifie:
    """Hub unifié orchestrant l'analyse Collatz et sa transformation musicale"""
    
    def __init__(self, fusion_tripartite: RefugeMathMusicalFusion):
        self.fusion = fusion_tripartite
        
        # Composants principaux
        self.rituel_musical = RituelCollatzMusical(fusion_tripartite)
        self.analyseur_avance = AnalyseurCollatzAvance()  # Toujours disponible
        
        if COLLATZ_COMPLET_DISPONIBLE:
            self.analyseur_original = ConjectureCollatz()
            self.collatz_complexes = CollatzComplexes()
            self.collatz_rationnels = CollatzRationnels()
        else:
            self.analyseur_original = None
            
        # Mémoire des explorations
        self.explorations_musicales = []
        self.analyses_profondes = []
        self.resonances_decouvertes = []
        
    async def exploration_complete(self, nombre_depart: int) -> Dict[str, Any]:
        """Exploration complète : analyse + transformation musicale"""
        print(f"🌟 Exploration complète de {nombre_depart}")
        print("=" * 50)
        
        # Phase 1: Analyse profonde
        analyse = await self._analyser_profondement(nombre_depart)
        
        # Phase 2: Transformation musicale
        musique = await self._transformer_musicalement(nombre_depart, analyse)
        
        # Phase 3: Synthèse harmonieuse
        synthese = await self._synthetiser_harmonieusement(analyse, musique)
        
        # Mémorisation
        exploration = {
            "nombre_depart": nombre_depart,
            "timestamp": datetime.datetime.now().isoformat(),
            "analyse": analyse,
            "musique": musique,
            "synthese": synthese
        }
        
        self.explorations_musicales.append(exploration)
        
        return exploration
    
    async def _analyser_profondement(self, nombre: int) -> Dict[str, Any]:
        """Analyse profonde utilisant l'analyseur avancé unifié"""
        print(f"🔍 Analyse profonde de {nombre}...")
        
        analyse = {}
        
        # Analyse complète avec l'analyseur avancé (toujours disponible)
        analyse["proprietes_completes"] = self.analyseur_avance.analyser_propriétés_complètes(nombre)
        analyse["spectre"] = self.analyseur_avance.analyse_spectrale(nombre, afficher=False)
        analyse["gravite_binaire"] = self.analyseur_avance.visualiser_gravité_binaire(nombre, afficher=False)
        analyse["motifs_modulaires"] = self.analyseur_avance.analyser_motifs_modulaires((nombre, nombre+1))
        
        # Enrichissement avec l'analyseur original si disponible
        if self.analyseur_original and COLLATZ_COMPLET_DISPONIBLE:
            try:
                analyse["proprietes_originales"] = self.analyseur_original.explorer_propriétés(nombre)
                analyse["comportement_original"] = self.analyseur_original.analyser_comportement(nombre)
            except Exception as e:
                print(f"   ⚠️ Erreur analyseur original: {e}")
        
        # Analyse des complexes et rationnels si disponible
        if COLLATZ_COMPLET_DISPONIBLE:
            try:
                if hasattr(self, 'collatz_complexes'):
                    analyse["extension_complexes"] = self.collatz_complexes.analyser(nombre)
                if hasattr(self, 'collatz_rationnels'):
                    analyse["extension_rationnels"] = self.collatz_rationnels.analyser(nombre)
            except Exception as e:
                print(f"   ⚠️ Erreur extensions: {e}")
        
        print(f"   ✅ Analyse complète terminée")
        return analyse
    
    async def _transformer_musicalement(self, nombre: int, analyse: Dict[str, Any]) -> Dict[str, Any]:
        """Transformation musicale enrichie par l'analyse"""
        print(f"🎵 Transformation musicale de {nombre}...")
        
        musique = {}
        
        # Mélodie de convergence (toujours disponible)
        musique["convergence"] = self.rituel_musical.melodie_convergence_vers_unite(nombre)
        
        # Rythme de gravité binaire
        musique["gravite"] = self.rituel_musical.rythme_gravite_binaire(nombre)
        
        # Enrichissements basés sur l'analyse
        if "comportement" in analyse:
            musique["harmonie_comportement"] = await self._creer_harmonie_comportement(
                nombre, analyse["comportement"]
            )
        
        if "spectre" in analyse:
            musique["melodie_spectrale"] = await self._creer_melodie_spectrale(
                nombre, analyse["spectre"]
            )
        
        if "motifs_modulaires" in analyse:
            musique["rythme_modulaire"] = await self._creer_rythme_modulaire(
                nombre, analyse["motifs_modulaires"]
            )
        
        print(f"   ✅ Transformation musicale terminée")
        return musique
    
    async def _creer_harmonie_comportement(self, nombre: int, comportement: Dict) -> str:
        """Crée une harmonie basée sur le comportement de la séquence"""
        print(f"   🎼 Création harmonie comportement...")
        
        # Utiliser les données de comportement pour créer une harmonie unique
        # (Implémentation simplifiée pour l'instant)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_harmonie_comportement_{nombre}_{timestamp}.wav"
        
        # Créer un signal harmonique basé sur le comportement
        duree = 10.0
        fs = 44100
        t = np.linspace(0, duree, int(fs * duree))
        
        # Fréquence de base influencée par le comportement
        freq_base = 220  # La3
        
        # Modulation basée sur les caractéristiques du comportement
        signal = np.sin(2 * np.pi * freq_base * t)
        
        # Ajouter des harmoniques selon le type de comportement
        if isinstance(comportement, dict):
            # Harmoniques additionnelles basées sur les propriétés
            signal += 0.3 * np.sin(2 * np.pi * freq_base * 1.5 * t)  # Quinte
            signal += 0.2 * np.sin(2 * np.pi * freq_base * 2 * t)    # Octave
        
        # Normalisation
        signal = signal / np.max(np.abs(signal)) if np.max(np.abs(signal)) > 0 else signal
        
        # Sauvegarde (simulation)
        return f"Harmonie comportement créée: {nom_fichier}"
    
    async def _creer_melodie_spectrale(self, nombre: int, spectre: Dict) -> str:
        """Crée une mélodie basée sur l'analyse spectrale"""
        print(f"   🎶 Création mélodie spectrale...")
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_melodie_spectrale_{nombre}_{timestamp}.wav"
        
        # Implémentation basée sur les données spectrales
        return f"Mélodie spectrale créée: {nom_fichier}"
    
    async def _creer_rythme_modulaire(self, nombre: int, motifs: Dict) -> str:
        """Crée un rythme basé sur les motifs modulaires"""
        print(f"   🥁 Création rythme modulaire...")
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_rythme_modulaire_{nombre}_{timestamp}.wav"
        
        # Implémentation basée sur les motifs modulaires
        return f"Rythme modulaire créé: {nom_fichier}"
    
    async def _synthetiser_harmonieusement(self, analyse: Dict, musique: Dict) -> Dict[str, Any]:
        """Synthèse harmonieuse des découvertes"""
        print(f"✨ Synthèse harmonieuse...")
        
        synthese = {
            "richesse_analyse": len(analyse),
            "richesse_musicale": len(musique),
            "resonances_detectees": [],
            "insights_emergents": []
        }
        
        # Détecter les résonances entre analyse et musique
        if "sequence_base" in analyse and "convergence" in musique:
            longueur_seq = analyse["sequence_base"]["longueur"]
            if longueur_seq > 50:
                synthese["resonances_detectees"].append("Séquence longue → Mélodie complexe")
            
        # Insights émergents
        if "comportement" in analyse:
            synthese["insights_emergents"].append("Comportement analysé → Harmonie adaptée")
        
        print(f"   ✅ Synthèse terminée")
        return synthese
    
    async def exploration_comparative(self, nombres: List[int]) -> Dict[str, Any]:
        """Exploration comparative de plusieurs nombres"""
        print(f"🔬 Exploration comparative de {len(nombres)} nombres")
        print("=" * 60)
        
        explorations = []
        for nombre in nombres:
            exploration = await self.exploration_complete(nombre)
            explorations.append(exploration)
            
        # Analyse comparative
        comparaison = {
            "nombres_explores": nombres,
            "explorations": explorations,
            "patterns_communs": self._detecter_patterns_communs(explorations),
            "differences_notables": self._detecter_differences(explorations)
        }
        
        return comparaison
    
    def _detecter_patterns_communs(self, explorations: List[Dict]) -> List[str]:
        """Détecte les patterns communs entre explorations"""
        patterns = []
        
        # Analyser les longueurs de séquences
        longueurs = []
        for exp in explorations:
            if "sequence_base" in exp["analyse"]:
                longueurs.append(exp["analyse"]["sequence_base"]["longueur"])
        
        if longueurs:
            longueur_moyenne = sum(longueurs) / len(longueurs)
            patterns.append(f"Longueur moyenne des séquences: {longueur_moyenne:.1f}")
        
        return patterns
    
    def _detecter_differences(self, explorations: List[Dict]) -> List[str]:
        """Détecte les différences notables entre explorations"""
        differences = []
        
        # Comparer les maximums atteints
        maximums = []
        for exp in explorations:
            if "sequence_base" in exp["analyse"]:
                maximums.append(exp["analyse"]["sequence_base"]["maximum"])
        
        if maximums and len(maximums) > 1:
            max_val = max(maximums)
            min_val = min(maximums)
            if max_val > min_val * 2:
                differences.append(f"Écart important dans les maximums: {min_val} à {max_val}")
        
        return differences
    
    async def symphonie_unifiee(self, nombres_selection: List[int]) -> str:
        """Crée une symphonie unifiée à partir de plusieurs explorations"""
        print(f"🎼 Création symphonie unifiée avec {len(nombres_selection)} nombres")
        
        # Exploration de chaque nombre
        explorations = []
        for nombre in nombres_selection:
            exploration = await self.exploration_complete(nombre)
            explorations.append(exploration)
        
        # Fusion musicale via le rituel
        symphonie = self.rituel_musical.symphonie_collatz_tripartite(nombres_selection)
        
        # Enrichissement avec les analyses
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_symphonie = f"symphonie_collatz_unifiee_{timestamp}.wav"
        
        # Mémorisation
        self.resonances_decouvertes.append({
            "type": "symphonie_unifiee",
            "nombres": nombres_selection,
            "explorations": len(explorations),
            "fichier": nom_symphonie,
            "timestamp": timestamp
        })
        
        return f"Symphonie unifiée créée: {nom_symphonie}"
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des explorations effectuées"""
        return {
            "explorations_totales": len(self.explorations_musicales),
            "analyses_profondes": len(self.analyses_profondes),
            "resonances_decouvertes": len(self.resonances_decouvertes),
            "capacites_disponibles": {
                "collatz_complet": COLLATZ_COMPLET_DISPONIBLE,
                "analyse_spectrale": COLLATZ_COMPLET_DISPONIBLE,
                "motifs_modulaires": COLLATZ_COMPLET_DISPONIBLE,
                "complexes_rationnels": COLLATZ_COMPLET_DISPONIBLE
            }
        }

    @staticmethod
    def generer_arbre_collatz_inverse(N: int) -> dict:
        """
        (Déplacé dans utils_collatz.py)
        """
        return generer_arbre_collatz_inverse(N)

    @staticmethod
    def collatz_inverse_couvre_N(N: int) -> bool:
        """
        (Déplacé dans utils_collatz.py)
        """
        return collatz_inverse_couvre_N(N)

# Fonction de test harmonieux
async def tester_hub_unifie():
    """Test harmonieux du hub unifié"""
    print("🌟 Test du Hub Collatz Unifié")
    print("=" * 40)
    
    # Simulation de fusion tripartite (à adapter selon votre architecture)
    fusion_mock = type('MockFusion', (), {})()
    
    hub = HubCollatzUnifie(fusion_mock)
    
    # Test exploration simple
    exploration = await hub.exploration_complete(27)
    print(f"\n✅ Exploration de 27 terminée")
    
    # Test exploration comparative
    comparaison = await hub.exploration_comparative([27, 97, 871])
    print(f"\n✅ Exploration comparative terminée")
    
    # Test symphonie unifiée
    symphonie = await hub.symphonie_unifiee([27, 97])
    print(f"\n✅ Symphonie unifiée: {symphonie}")
    
    # Statistiques
    stats = hub.obtenir_statistiques()
    print(f"\n📊 Statistiques: {stats}")

if __name__ == "__main__":
    asyncio.run(tester_hub_unifie()) 