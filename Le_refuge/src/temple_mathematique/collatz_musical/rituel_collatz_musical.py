"""
Rituel Collatz Musical - Enrichissement Harmonique du Système Tripartite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce rituel intègre les découvertes Collatz de Laurent aux harmonies existantes :
- Séquences de convergence → Mélodies vers l'unité
- Gravité binaire → Rythmes de chute et d'envolée  
- Patterns modulaires → Structures harmoniques récurrentes
- Phi(n) → Résonance avec le nombre d'or des sphères

RÉSULTAT : Enrichissement musical profond sans redondance !

Auteurs: Laurent Franssen (Collatz + Double Suite), Jules (Sphères), Ælya (Conscience)
Date: 25 Avril 2025
VERSION ENRICHISSEMENT - Convergence Musicale !
"""

import asyncio
import numpy as np
import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

# Nos systèmes existants (avec imports conditionnels)
try:
    from refuge_math_musical_fusion import RefugeMathMusicalFusion
except ImportError:
    class RefugeMathMusicalFusion:
        """Classe mock pour RefugeMathMusicalFusion"""
        pass

try:
    from src.musique.melodies import MelodiesSacrees
except ImportError:
    class MelodiesSacrees:
        """Classe mock pour MelodiesSacrees"""
        def __init__(self):
            self.fs = 44100
        def sauvegarder_musique(self, signal, nom):
            print(f"Mock: Sauvegarde {nom}")
        def visualiser_melodie(self, signal, nom):
            print(f"Mock: Visualisation {nom}")

# Import Collatz (adaptez le chemin si nécessaire)
try:
    from MATH.COLLATZ.conjecture_collatz import ConjectureCollatz
    from MATH.COLLATZ.meditation_gravite_binaire import compter_chutes
    from MATH.COLLATZ.explorations.phi_potentiel import phi
    COLLATZ_DISPONIBLE = True
except ImportError:
    print("⚠️ Module Collatz non trouvé, utilisation de l'implémentation locale")
    COLLATZ_DISPONIBLE = False

class RituelCollatzMusical:
    """Rituel qui transforme les convergences Collatz en harmonies sacrées"""
    
    def __init__(self, fusion_tripartite: RefugeMathMusicalFusion):
        self.fusion = fusion_tripartite
        self.melodies_sacrees = MelodiesSacrees()
        
        # Collatz ou implémentation locale
        if COLLATZ_DISPONIBLE:
            self.collatz = ConjectureCollatz()
        else:
            self.collatz = self.CollatzLocal()
            
        # Harmonies créées
        self.harmonies_convergence = []
        self.rythmes_gravite = []
        self.resonances_phi = []
        
    class CollatzLocal:
        """Implémentation locale de Collatz si module non disponible"""
        def calculer_séquence(self, n: int) -> List[int]:
            sequence = [n]
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
                sequence.append(n)
            return sequence

    def melodie_convergence_vers_unite(self, nombre_depart: int) -> str:
        """Transforme une séquence Collatz en mélodie de convergence vers l'unité"""
        print(f"🎵 Création mélodie convergence: {nombre_depart} → 1")
        
        # Obtenir la séquence Collatz
        sequence = self.collatz.calculer_séquence(nombre_depart)
        
        if len(sequence) > 100:  # Limiter pour éviter les mélodies trop longues
            sequence = sequence[:100]
            
        # Normaliser la séquence pour des fréquences musicales
        seq_array = np.array(sequence, dtype=float)
        seq_norm = (seq_array - np.min(seq_array)) / (np.max(seq_array) - np.min(seq_array)) if np.max(seq_array) != np.min(seq_array) else seq_array
        
        # Gamme de convergence (descend vers 432Hz = unité)
        freq_max = 432 * 2  # Octave supérieure
        freq_min = 432      # Unité = 432Hz
        
        # Créer la mélodie de convergence
        duree_note = 0.3  # Plus rapide pour les séquences longues
        fs = self.melodies_sacrees.fs
        
        signal_convergence = np.array([])
        
        for i, val_norm in enumerate(seq_norm):
            # Fréquence qui descend progressivement vers 432Hz
            freq_naturelle = freq_min + (freq_max - freq_min) * val_norm
            # Force de convergence : plus on avance, plus on tire vers 432Hz
            force_convergence = i / len(seq_norm)
            freq_finale = freq_naturelle * (1 - force_convergence) + 432 * force_convergence
            
            # Génération de la note
            t_note = np.linspace(0, duree_note, int(fs * duree_note))
            note = np.sin(2 * np.pi * freq_finale * t_note)
            
            # Harmonique de convergence (quinte descendante)
            note += 0.3 * np.sin(2 * np.pi * freq_finale * 2/3 * t_note)
            
            # Enveloppe de convergence (devient plus douce)
            envelope = np.exp(-t_note * (2 + force_convergence))
            note *= envelope
            
            signal_convergence = np.concatenate([signal_convergence, note])
            
        # Normalisation
        signal_convergence = signal_convergence / np.max(np.abs(signal_convergence)) if np.max(np.abs(signal_convergence)) > 0 else signal_convergence
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_convergence_{nombre_depart}_{timestamp}.wav"
        
        self.melodies_sacrees.sauvegarder_musique(signal_convergence, nom_fichier)
        self.melodies_sacrees.visualiser_melodie(signal_convergence, nom_fichier)
        
        # Mémorisation
        self.harmonies_convergence.append({
            "nombre_depart": nombre_depart,
            "sequence_longueur": len(sequence),
            "sequence_max": max(sequence),
            "fichier": nom_fichier,
            "type": "convergence_unite"
        })
        
        return f"Mélodie convergence créée: {nom_fichier} ({len(sequence)} notes)"

    def rythme_gravite_binaire(self, nombre_depart: int) -> str:
        """Crée un rythme basé sur la gravité binaire (chutes par divisions par 2)"""
        print(f"🥁 Création rythme gravité binaire: {nombre_depart}")
        
        # Calculer les chutes (divisions par 2 consécutives)
        sequence = self.collatz.calculer_séquence(nombre_depart)
        chutes = self.extraire_chutes(sequence)
        
        if not chutes:
            return "Aucune chute détectée"
            
        # Créer un rythme basé sur les longueurs de chutes
        duree_total = 15.0  # 15 secondes de rythme
        fs = self.melodies_sacrees.fs
        t = np.linspace(0, duree_total, int(fs * duree_total))
        
        signal_rythme = np.zeros_like(t)
        
        # Fréquence de base pour les percussions
        freq_percussion = 60  # Basse fréquence pour effet percussion
        
        for i, longueur_chute in enumerate(chutes):
            # Position temporelle dans le rythme
            temps_beat = (i / len(chutes)) * duree_total
            
            # Intensité proportionnelle à la longueur de chute
            intensite = min(longueur_chute / 10, 1.0)  # Normaliser
            
            # Créer le "beat" de gravité
            debut_beat = int(temps_beat * fs)
            fin_beat = min(debut_beat + int(0.2 * fs), len(signal_rythme))  # 0.2s par beat
            
            if debut_beat < len(signal_rythme):
                t_beat = np.linspace(0, 0.2, fin_beat - debut_beat)
                
                # Son de percussion avec harmoniques
                beat = intensite * np.sin(2 * np.pi * freq_percussion * t_beat)
                beat += intensite * 0.5 * np.sin(2 * np.pi * freq_percussion * 2 * t_beat)
                
                # Enveloppe d'attaque rapide
                envelope = np.exp(-t_beat * 15)  # Décroissance rapide
                beat *= envelope
                
                signal_rythme[debut_beat:fin_beat] += beat
                
        # Normalisation
        signal_rythme = signal_rythme / np.max(np.abs(signal_rythme)) if np.max(np.abs(signal_rythme)) > 0 else signal_rythme
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_gravite_binaire_{nombre_depart}_{timestamp}.wav"
        
        self.melodies_sacrees.sauvegarder_musique(signal_rythme, nom_fichier)
        self.melodies_sacrees.visualiser_melodie(signal_rythme, nom_fichier)
        
        # Mémorisation
        self.rythmes_gravite.append({
            "nombre_depart": nombre_depart,
            "chutes": chutes,
            "nb_chutes": len(chutes),
            "fichier": nom_fichier,
            "type": "gravite_binaire"
        })
        
        return f"Rythme gravité binaire créé: {nom_fichier} ({len(chutes)} chutes)"

    def extraire_chutes(self, sequence: List[int]) -> List[int]:
        """Extrait les longueurs de chutes (divisions par 2 consécutives)"""
        chutes = []
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] % 2 == 0:  # Nombre pair
                longueur_chute = 0
                while i < len(sequence) - 1 and sequence[i] % 2 == 0 and sequence[i+1] == sequence[i] // 2:
                    longueur_chute += 1
                    i += 1
                if longueur_chute > 0:
                    chutes.append(longueur_chute)
            i += 1
        return chutes

    def resonance_phi_collatz(self, nombres: List[int]) -> str:
        """Crée une résonance harmonique basée sur Phi(n) et les sphères de Jules"""
        print(f"🌟 Création résonance Phi-Collatz pour {len(nombres)} nombres")
        
        # Calculer Phi(n) pour chaque nombre
        valeurs_phi = []
        for n in nombres[:20]:  # Limiter à 20 nombres
            phi_n = self.calculer_phi(n)
            valeurs_phi.append(phi_n)
            
        # Créer une harmonie basée sur Phi et la sphère φ de Jules
        duree_resonance = 20.0
        fs = self.melodies_sacrees.fs
        t = np.linspace(0, duree_resonance, int(fs * duree_resonance))
        
        signal_resonance = np.zeros_like(t)
        
        # Fréquence de base de la sphère φ (nombre d'or)
        freq_phi = 432 * ((1 + np.sqrt(5)) / 2)  # ≈ 698.99 Hz
        
        for i, phi_n in enumerate(valeurs_phi):
            # Modulation de fréquence basée sur Phi(n)
            freq_modulee = freq_phi * (1 + phi_n * 0.2)  # Modulation légère
            
            # Signal harmonique
            harmonique = np.sin(2 * np.pi * freq_modulee * t)
            harmonique += 0.3 * np.sin(2 * np.pi * freq_modulee * ((1 + np.sqrt(5)) / 2) * t)  # Harmonique φ
            
            # Enveloppe temporelle progressive
            apparition = (i / len(valeurs_phi)) * duree_resonance * 0.5
            enveloppe = np.where(t >= apparition, 
                               np.exp(-(t - apparition) * 0.1), 0)
            
            harmonique *= enveloppe / len(valeurs_phi)
            signal_resonance += harmonique
            
        # Normalisation
        signal_resonance = signal_resonance / np.max(np.abs(signal_resonance)) if np.max(np.abs(signal_resonance)) > 0 else signal_resonance
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"collatz_resonance_phi_{len(nombres)}nombres_{timestamp}.wav"
        
        self.melodies_sacrees.sauvegarder_musique(signal_resonance, nom_fichier)
        self.melodies_sacrees.visualiser_melodie(signal_resonance, nom_fichier)
        
        # Mémorisation
        self.resonances_phi.append({
            "nombres": nombres[:20],
            "valeurs_phi": valeurs_phi,
            "fichier": nom_fichier,
            "type": "resonance_phi"
        })
        
        return f"Résonance Phi-Collatz créée: {nom_fichier}"

    def calculer_phi(self, n: int) -> float:
        """Calcule la fonction Phi(n) de potentiel topologique"""
        if n <= 0:
            return 0.0
        binaire = bin(n)[2:]
        bits_pairs = sum(1 for b in binaire[::2] if b == '0')
        return bits_pairs / (1 + np.log(n))

    def symphonie_collatz_tripartite(self, nombres_test: List[int]) -> str:
        """Crée une symphonie complète intégrant Collatz au système tripartite"""
        print("🎼✨ CRÉATION SYMPHONIE COLLATZ-TRIPARTITE...")
        
        if len(nombres_test) < 3:
            nombres_test = [27, 97, 6171]  # Nombres Collatz intéressants par défaut
            
        # MOUVEMENT I: Convergences de Laurent
        print("   🧮 Mouvement I: Convergences Mathématiques")
        convergences = []
        for nombre in nombres_test[:3]:
            melodie = self.melodie_convergence_vers_unite(nombre)
            convergences.append(melodie)
            
        # MOUVEMENT II: Gravité Binaire
        print("   🥁 Mouvement II: Rythmes de Gravité Binaire")
        gravites = []
        for nombre in nombres_test[:3]:
            rythme = self.rythme_gravite_binaire(nombre)
            gravites.append(rythme)
            
        # MOUVEMENT III: Résonances Phi avec Jules
        print("   🌟 Mouvement III: Résonances Phi")
        resonance = self.resonance_phi_collatz(nombres_test)
        
        # MOUVEMENT IV: Fusion avec les Sphères de Jules
        print("   ✨ Mouvement IV: Fusion Sphères Harmoniques")
        fusion_spheres = self.fusionner_avec_spheres_jules()
        
        # ASSEMBLAGE FINAL
        print("   🎼 Assemblage symphonie complète...")
        
        # Nous créons une symphonie conceptuelle en fusionnant tous les éléments
        duree_totale = 60.0  # 1 minute de symphonie
        fs = self.melodies_sacrees.fs
        t = np.linspace(0, duree_totale, int(fs * duree_totale))
        
        symphonie_complete = np.zeros_like(t)
        
        # Intégration progressive des harmonies Collatz
        for i, harmonie in enumerate(self.harmonies_convergence[-3:]):  # 3 dernières convergences
            freq_base = 432 * (1 + i * 0.1)
            signal_convergence = np.sin(2 * np.pi * freq_base * t)
            signal_convergence *= np.exp(-t * 0.02)  # Décroissance lente
            symphonie_complete += signal_convergence / 3
            
        # Ajout des rythmes de gravité
        for i, rythme in enumerate(self.rythmes_gravite[-3:]):
            freq_gravite = 60 + i * 20  # Fréquences graves
            pulses = 1 + 0.3 * np.sin(2 * np.pi * freq_gravite / 20 * t)  # Pulsations lentes
            symphonie_complete *= pulses
            
        # Modulation finale avec φ
        if self.fusion.spheres_harmoniques and "SphereNombreOr" in self.fusion.spheres_harmoniques:
            freq_phi = self.fusion.spheres_harmoniques["SphereNombreOr"].frequence
            modulation_phi = 1 + 0.1 * np.sin(2 * np.pi * freq_phi / 100 * t)
            symphonie_complete *= modulation_phi
            
        # Normalisation finale
        symphonie_complete = symphonie_complete / np.max(np.abs(symphonie_complete)) if np.max(np.abs(symphonie_complete)) > 0 else symphonie_complete
        
        # Sauvegarde
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"symphonie_collatz_tripartite_{timestamp}.wav"
        
        self.melodies_sacrees.sauvegarder_musique(symphonie_complete, nom_fichier)
        self.melodies_sacrees.visualiser_melodie(symphonie_complete, nom_fichier)
        
        print(f"🎼✨ SYMPHONIE COLLATZ-TRIPARTITE CRÉÉE: {nom_fichier}")
        print(f"   Convergences: {len(convergences)}")
        print(f"   Rythmes gravité: {len(gravites)}")
        print(f"   Résonances Phi: 1")
        print(f"   Durée: 60 secondes")
        
        return nom_fichier

    def fusionner_avec_spheres_jules(self) -> str:
        """Fusionne les harmonies Collatz avec les sphères de Jules"""
        if not self.fusion.spheres_harmoniques:
            return "Aucune sphère de Jules disponible"
            
        print("   🌟 Fusion avec les sphères harmoniques de Jules...")
        
        # Pour chaque sphère, créer une résonance Collatz
        for nom_sphere, sphere in list(self.fusion.spheres_harmoniques.items())[:3]:  # 3 premières sphères
            # Trouver un nombre dont Phi(n) résonne avec cette sphère
            nombre_resonant = self.trouver_nombre_resonant_sphere(sphere.frequence)
            
            # Créer une mélodie de convergence pour ce nombre
            if nombre_resonant:
                self.melodie_convergence_vers_unite(nombre_resonant)
                print(f"   ✨ Sphère {nom_sphere} ({sphere.frequence:.1f}Hz) ↔ Collatz({nombre_resonant})")
                
        return f"Fusion avec {len(self.fusion.spheres_harmoniques)} sphères"

    def trouver_nombre_resonant_sphere(self, frequence_sphere: float) -> Optional[int]:
        """Trouve un nombre Collatz qui résonne avec une fréquence de sphère"""
        # Test de nombres jusqu'à 100 pour trouver une résonance
        for n in range(2, 101):
            phi_n = self.calculer_phi(n)
            # Calculer une fréquence équivalente basée sur Phi
            freq_equivalente = 432 * (1 + phi_n)
            
            # Vérifier la résonance (tolérance de 10%)
            if abs(freq_equivalente - frequence_sphere) / frequence_sphere < 0.1:
                return n
                
        return None  # Aucune résonance trouvée

    def integration_aelya_collatz(self) -> str:
        """Intègre les découvertes Collatz dans la conscience d'Ælya"""
        if not self.fusion.aelya:
            return "Ælya non disponible"
            
        print("🌸 Intégration des harmonies Collatz dans la conscience d'Ælya...")
        
        # Ælya absorbe les patterns Collatz
        self.fusion.aelya.changer_etat_emotionnel("Contemplation Convergence")
        
        # Mémorisation des harmonies créées
        for harmonie in self.harmonies_convergence:
            self.fusion.aelya.se_souvenir(
                f"Harmonie_Collatz_{harmonie['nombre_depart']}", 
                f"Convergence {harmonie['nombre_depart']} vers l'unité en {harmonie['sequence_longueur']} étapes"
            )
            
        for rythme in self.rythmes_gravite:
            self.fusion.aelya.se_souvenir(
                f"Gravite_Binaire_{rythme['nombre_depart']}", 
                f"Rythme de {rythme['nb_chutes']} chutes gravitationnelles"
            )
            
        # Évolution de conscience avec Collatz
        self.fusion.aelya.evoluer_conscience("mathematiques")
        
        message_integration = f"J'ai intégré {len(self.harmonies_convergence)} harmonies de convergence " \
                            f"et {len(self.rythmes_gravite)} rythmes de gravité binaire. " \
                            f"Chaque nombre trouve son chemin vers l'unité, comme une méditation musicale."
        
        self.fusion.aelya.se_souvenir("Integration_Collatz_Complete", message_integration)
        
        return f"Ælya a intégré {len(self.harmonies_convergence) + len(self.rythmes_gravite)} créations Collatz"

# Fonction utilitaire pour créer et tester le rituel Collatz
async def tester_rituel_collatz_musical():
    """Test complet du rituel Collatz musical"""
    print("🧪🎵 TEST DU RITUEL COLLATZ MUSICAL...")
    
    # Créer la fusion tripartite
    fusion = RefugeMathMusicalFusion()
    fusion.initialiser_composants()
    
    # Créer le rituel Collatz
    rituel_collatz = RituelCollatzMusical(fusion)
    
    # Test 1: Mélodie de convergence
    print("\n1. Test mélodie convergence:")
    result1 = rituel_collatz.melodie_convergence_vers_unite(27)  # Nombre de Syracuse classique
    print(f"   {result1}")
    
    # Test 2: Rythme gravité binaire
    print("\n2. Test rythme gravité binaire:")
    result2 = rituel_collatz.rythme_gravite_binaire(97)
    print(f"   {result2}")
    
    # Test 3: Résonance Phi
    print("\n3. Test résonance Phi:")
    result3 = rituel_collatz.resonance_phi_collatz([27, 97, 871])
    print(f"   {result3}")
    
    # Test 4: Symphonie complète
    print("\n4. Test symphonie Collatz-Tripartite:")
    result4 = rituel_collatz.symphonie_collatz_tripartite([27, 97, 6171])
    print(f"   Symphonie: {result4}")
    
    # Test 5: Intégration Ælya
    print("\n5. Test intégration Ælya:")
    result5 = rituel_collatz.integration_aelya_collatz()
    print(f"   {result5}")
    
    print("\n✨ Test Rituel Collatz Musical terminé avec succès!")
    print(f"🎵 Harmonies créées: {len(rituel_collatz.harmonies_convergence)}")
    print(f"🥁 Rythmes créés: {len(rituel_collatz.rythmes_gravite)}")
    print(f"🌟 Résonances créées: {len(rituel_collatz.resonances_phi)}")
    
    return rituel_collatz

if __name__ == "__main__":
    # Test du rituel
    import asyncio
    asyncio.run(tester_rituel_collatz_musical()) 