"""
🔮 HARMONIES QUANTIQUES - Temple Musical
=======================================

Module qui intègre des concepts quantiques dans la musique,
créant des harmonies basées sur les principes de la mécanique quantique.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import numpy as np
import json
import time
from typing import Dict, List, Optional, Any, Tuple, Union
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import random

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from generateur_melodies_sacrees import MelodiesSacrees

class EtatQuantique(Enum):
    """États quantiques musicaux"""
    SUPERPOSITION = "superposition"
    ENTANGLEMENT = "entanglement"
    INTERFERENCE = "interference"
    COLLAPSE = "collapse"
    TUNNELING = "tunneling"
    RESONANCE = "resonance"

class ParticuleMusicale(Enum):
    """Types de particules musicales"""
    PHOTON = "photon"  # Lumière/énergie
    ELECTRON = "electron"  # Électricité/rythme
    NEUTRON = "neutron"  # Stabilité/harmonie
    QUARK = "quark"  # Fondamental/mélodie
    GLUON = "gluon"  # Force/liaison
    BOSON = "boson"  # Champ/atmosphère

@dataclass
class EtatQuantiqueMusical:
    """État quantique d'une note ou harmonie"""
    particule: ParticuleMusicale
    etat: EtatQuantique
    frequence: float
    amplitude: float
    phase: float
    spin: float  # -1/2 ou +1/2 pour les fermions
    energie: float
    position_temps: float
    probabilite: float

@dataclass
class SystemeQuantiqueMusical:
    """Système quantique musical complet"""
    id_systeme: str
    nom: str
    particules: List[EtatQuantiqueMusical]
    hamiltonien: Dict[str, float]  # Énergie du système
    fonction_onde: List[complex]  # État du système
    niveau_energie: float
    coherence: float
    intrication: float
    timestamp: datetime

class HarmoniesQuantiques(GestionnaireBase):
    """Gestionnaire d'harmonies quantiques"""
    
    def __init__(self, nom: str = "HarmoniesQuantiques"):
        super().__init__(nom)
        self.energie_quantique = EnergyManagerBase(0.98)
        
        # Générateur de mélodies sacrées
        self.melodies_sacrees = MelodiesSacrees()
        
        # Constantes quantiques musicales
        self.constantes_quantiques = self._definir_constantes_quantiques()
        
        # Systèmes quantiques actifs
        self.systemes_actifs: Dict[str, SystemeQuantiqueMusical] = {}
        
        # Historique des mesures quantiques
        self.historique_mesures: List[Dict[str, Any]] = []
        
        # Configuration
        self.config_quantique = {
            "superposition_active": True,
            "entanglement_musical": True,
            "interference_constructive": True,
            "decoherence_controllee": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le système d'harmonies quantiques"""
        self.logger.info("🔮 Éveil des Harmonies Quantiques...")
        
        self.etat.update({
            "systemes_actifs": 0,
            "particules_crees": 0,
            "mesures_quantiques": 0,
            "coherence_moyenne": 0.9
        })
        
        self.config.definir("mode_quantique", "coherent")
        self.config.definir("sauvegarde_etats", True)
        
        self.logger.info("✨ Harmonies Quantiques éveillées")
    
    def _definir_constantes_quantiques(self) -> Dict[str, float]:
        """Définit les constantes quantiques musicales"""
        return {
            "h_bar": 1.054571817e-34,  # Constante de Planck réduite
            "c": 299792458,  # Vitesse de la lumière
            "k_b": 1.380649e-23,  # Constante de Boltzmann
            "e": 1.602176634e-19,  # Charge élémentaire
            
            # Constantes musicales quantiques (inventées)
            "frequence_planck": 432.0,  # Fréquence de Planck musicale
            "energie_quantique_musicale": 444.0,  # Énergie quantique d'Ælya
            "longueur_onde_musicale": 528.0,  # Longueur d'onde musicale
            "temps_quantique_musical": 1.0 / 432.0,  # Temps quantique musical
            "masse_quantique_musicale": 1.0  # Masse quantique musicale unitaire
        }
    
    def creer_particule_musicale(self, particule: ParticuleMusicale, 
                                frequence: float, energie: float) -> EtatQuantiqueMusical:
        """Crée une particule musicale quantique"""
        # Calculer les propriétés quantiques
        amplitude = np.sqrt(energie / self.constantes_quantiques["energie_quantique_musicale"])
        phase = 2 * np.pi * frequence * self.constantes_quantiques["temps_quantique_musical"]
        spin = random.choice([-0.5, 0.5]) if particule in [ParticuleMusicale.ELECTRON, ParticuleMusicale.QUARK] else 1.0
        probabilite = amplitude ** 2
        
        particule_quantique = EtatQuantiqueMusical(
            particule=particule,
            etat=EtatQuantique.SUPERPOSITION,
            frequence=frequence,
            amplitude=amplitude,
            phase=phase,
            spin=spin,
            energie=energie,
            position_temps=time.time(),
            probabilite=probabilite
        )
        
        self.etat["particules_crees"] += 1
        return particule_quantique
    
    def creer_systeme_quantique(self, nom: str, particules: List[EtatQuantiqueMusical]) -> SystemeQuantiqueMusical:
        """Crée un système quantique musical"""
        # Calculer l'hamiltonien du système
        hamiltonien = self._calculer_hamiltonien(particules)
        
        # Créer la fonction d'onde
        fonction_onde = self._creer_fonction_onde(particules)
        
        # Calculer les propriétés du système
        niveau_energie = sum(p.energie for p in particules)
        coherence = self._calculer_coherence(particules)
        intrication = self._calculer_intrication(particules)
        
        systeme = SystemeQuantiqueMusical(
            id_systeme=f"systeme_{int(time.time())}",
            nom=nom,
            particules=particules,
            hamiltonien=hamiltonien,
            fonction_onde=fonction_onde,
            niveau_energie=niveau_energie,
            coherence=coherence,
            intrication=intrication,
            timestamp=datetime.now()
        )
        
        self.systemes_actifs[systeme.id_systeme] = systeme
        self.etat["systemes_actifs"] += 1
        
        return systeme
    
    def _calculer_hamiltonien(self, particules: List[EtatQuantiqueMusical]) -> Dict[str, float]:
        """Calcule l'hamiltonien du système"""
        hamiltonien = {
            "energie_cinetique": 0.0,
            "energie_potentielle": 0.0,
            "energie_interaction": 0.0,
            "energie_totale": 0.0
        }
        
        for particule in particules:
            # Énergie cinétique
            hamiltonien["energie_cinetique"] += 0.5 * particule.energie * (particule.frequence ** 2)
            
            # Énergie potentielle
            hamiltonien["energie_potentielle"] += particule.energie * particule.amplitude
            
            # Énergie totale
            hamiltonien["energie_totale"] += particule.energie
        
        # Énergie d'interaction entre particules
        for i, p1 in enumerate(particules):
            for j, p2 in enumerate(particules[i+1:], i+1):
                distance_freq = abs(p1.frequence - p2.frequence)
                hamiltonien["energie_interaction"] += 1.0 / (1.0 + distance_freq)
        
        return hamiltonien
    
    def _creer_fonction_onde(self, particules: List[EtatQuantiqueMusical]) -> List[complex]:
        """Crée la fonction d'onde du système"""
        # Fonction d'onde comme superposition d'états
        fonction_onde = []
        
        for particule in particules:
            # Amplitude complexe
            amplitude_complexe = particule.amplitude * np.exp(1j * particule.phase)
            fonction_onde.append(amplitude_complexe)
        
        # Normaliser la fonction d'onde
        norme = np.sqrt(sum(abs(psi) ** 2 for psi in fonction_onde))
        if norme > 0:
            fonction_onde = [psi / norme for psi in fonction_onde]
        
        return fonction_onde
    
    def _calculer_coherence(self, particules: List[EtatQuantiqueMusical]) -> float:
        """Calcule la cohérence du système"""
        if len(particules) < 2:
            return 1.0
        
        # Cohérence basée sur la similarité des phases
        phases = [p.phase for p in particules]
        differences_phase = []
        
        for i, phase1 in enumerate(phases):
            for phase2 in phases[i+1:]:
                diff = abs(phase1 - phase2) % (2 * np.pi)
                differences_phase.append(diff)
        
        # Cohérence inverse à la dispersion des phases
        dispersion = np.std(differences_phase) if differences_phase else 0
        coherence = np.exp(-dispersion / np.pi)
        
        return max(0.0, min(1.0, coherence))
    
    def _calculer_intrication(self, particules: List[EtatQuantiqueMusical]) -> float:
        """Calcule l'intrication du système"""
        if len(particules) < 2:
            return 0.0
        
        # Intrication basée sur les corrélations entre particules
        correlations = []
        
        for i, p1 in enumerate(particules):
            for p2 in particules[i+1:]:
                # Corrélation entre fréquences
                corr_freq = 1.0 / (1.0 + abs(p1.frequence - p2.frequence) / 100.0)
                
                # Corrélation entre énergies
                corr_energie = 1.0 / (1.0 + abs(p1.energie - p2.energie) / 100.0)
                
                # Corrélation moyenne
                correlation = (corr_freq + corr_energie) / 2.0
                correlations.append(correlation)
        
        intrication = np.mean(correlations) if correlations else 0.0
        return intrication
    
    def appliquer_superposition(self, particules: List[EtatQuantiqueMusical]) -> List[EtatQuantiqueMusical]:
        """Applique le principe de superposition"""
        particules_superposees = []
        
        for particule in particules:
            # Créer une superposition d'états
            etat_superpose = EtatQuantiqueMusical(
                particule=particule.particule,
                etat=EtatQuantique.SUPERPOSITION,
                frequence=particule.frequence,
                amplitude=particule.amplitude / np.sqrt(2),  # Normalisation
                phase=particule.phase,
                spin=particule.spin,
                energie=particule.energie,
                position_temps=particule.position_temps,
                probabilite=particule.probabilite / 2
            )
            particules_superposees.append(etat_superpose)
        
        return particules_superposees
    
    def appliquer_entanglement(self, particules: List[EtatQuantiqueMusical]) -> List[EtatQuantiqueMusical]:
        """Applique l'intrication quantique"""
        if len(particules) < 2:
            return particules
        
        particules_intriquees = []
        
        for i, particule in enumerate(particules):
            # Modifier l'état pour refléter l'intrication
            particule_intriquee = EtatQuantiqueMusical(
                particule=particule.particule,
                etat=EtatQuantique.ENTANGLEMENT,
                frequence=particule.frequence,
                amplitude=particule.amplitude,
                phase=particule.phase + (i * np.pi / len(particules)),  # Phase corrélée
                spin=particule.spin,
                energie=particule.energie,
                position_temps=particule.position_temps,
                probabilite=particule.probabilite
            )
            particules_intriquees.append(particule_intriquee)
        
        return particules_intriquees
    
    def appliquer_interference(self, particules: List[EtatQuantiqueMusical], 
                             type_interference: str = "constructive") -> List[EtatQuantiqueMusical]:
        """Applique l'interférence quantique"""
        particules_interference = []
        
        for particule in particules:
            # Modifier l'amplitude selon le type d'interférence
            if type_interference == "constructive":
                amplitude_modifiee = particule.amplitude * 1.5
            elif type_interference == "destructive":
                amplitude_modifiee = particule.amplitude * 0.5
            else:  # mixte
                amplitude_modifiee = particule.amplitude * (0.8 + 0.4 * np.sin(particule.phase))
            
            particule_interference = EtatQuantiqueMusical(
                particule=particule.particule,
                etat=EtatQuantique.INTERFERENCE,
                frequence=particule.frequence,
                amplitude=amplitude_modifiee,
                phase=particule.phase,
                spin=particule.spin,
                energie=particule.energie,
                position_temps=particule.position_temps,
                probabilite=amplitude_modifiee ** 2
            )
            particules_interference.append(particule_interference)
        
        return particules_interference
    
    def mesurer_systeme(self, systeme: SystemeQuantiqueMusical) -> Dict[str, Any]:
        """Effectue une mesure quantique du système"""
        # Collapse de la fonction d'onde
        mesures = []
        
        for i, particule in enumerate(systeme.particules):
            # Probabilité de mesure selon la fonction d'onde
            proba_mesure = abs(systeme.fonction_onde[i]) ** 2
            
            # Effectuer la mesure
            if random.random() < proba_mesure:
                mesure = {
                    "particule_id": i,
                    "particule_type": particule.particule.value,
                    "frequence_mesuree": particule.frequence,
                    "energie_mesuree": particule.energie,
                    "etat_final": EtatQuantique.COLLAPSE.value,
                    "probabilite": proba_mesure,
                    "timestamp": datetime.now().isoformat()
                }
                mesures.append(mesure)
        
        # Sauvegarder la mesure
        mesure_complete = {
            "systeme_id": systeme.id_systeme,
            "nombre_mesures": len(mesures),
            "mesures": mesures,
            "coherence_avant": systeme.coherence,
            "intrication_avant": systeme.intrication,
            "timestamp": datetime.now().isoformat()
        }
        
        self.historique_mesures.append(mesure_complete)
        self.etat["mesures_quantiques"] += 1
        
        return mesure_complete
    
    def generer_harmonie_quantique(self, nom: str, frequences: List[float]) -> Dict[str, Any]:
        """Génère une harmonie basée sur les principes quantiques"""
        # Créer les particules musicales
        particules = []
        for i, frequence in enumerate(frequences):
            energie = frequence * self.constantes_quantiques["energie_quantique_musicale"]
            particule = self.creer_particule_musicale(
                ParticuleMusicale.QUARK if i % 2 == 0 else ParticuleMusicale.ELECTRON,
                frequence, energie
            )
            particules.append(particule)
        
        # Appliquer les effets quantiques
        particules_superposees = self.appliquer_superposition(particules)
        particules_intriquees = self.appliquer_entanglement(particules_superposees)
        particules_interference = self.appliquer_interference(particules_intriquees, "constructive")
        
        # Créer le système quantique
        systeme = self.creer_systeme_quantique(nom, particules_interference)
        
        # Effectuer une mesure
        mesure = self.mesurer_systeme(systeme)
        
        # Générer l'harmonie finale
        harmonie = {
            "nom": nom,
            "systeme_quantique": systeme,
            "mesure": mesure,
            "frequences_resultantes": [p.frequence for p in particules_interference],
            "energies_resultantes": [p.energie for p in particules_interference],
            "coherence": systeme.coherence,
            "intrication": systeme.intrication,
            "harmonie_quantique": self._calculer_harmonie_quantique(particules_interference)
        }
        
        return harmonie
    
    def _calculer_harmonie_quantique(self, particules: List[EtatQuantiqueMusical]) -> float:
        """Calcule le niveau d'harmonie quantique"""
        if len(particules) < 2:
            return 1.0
        
        # Facteurs d'harmonie quantique
        facteurs = {
            "coherence": self._calculer_coherence(particules),
            "intrication": self._calculer_intrication(particules),
            "resonance": self._calculer_resonance_quantique(particules),
            "equilibre": self._calculer_equilibre_quantique(particules)
        }
        
        return np.mean(list(facteurs.values()))
    
    def _calculer_resonance_quantique(self, particules: List[EtatQuantiqueMusical]) -> float:
        """Calcule la résonance quantique"""
        frequences = [p.frequence for p in particules]
        
        # Chercher des résonances harmoniques
        resonances = 0
        for i, freq1 in enumerate(frequences):
            for freq2 in frequences[i+1:]:
                ratio = freq1 / freq2 if freq2 > 0 else 0
                # Vérifier si le ratio est proche d'un nombre entier simple
                if abs(ratio - round(ratio)) < 0.1 or abs(ratio - 1/round(1/ratio)) < 0.1:
                    resonances += 1
        
        max_resonances = len(frequences) * (len(frequences) - 1) / 2
        return resonances / max_resonances if max_resonances > 0 else 0.0
    
    def _calculer_equilibre_quantique(self, particules: List[EtatQuantiqueMusical]) -> float:
        """Calcule l'équilibre quantique"""
        energies = [p.energie for p in particules]
        
        # Équilibre basé sur la distribution des énergies
        energie_moyenne = np.mean(energies)
        ecart_type = np.std(energies)
        
        # Plus l'écart-type est faible, plus l'équilibre est bon
        equilibre = 1.0 / (1.0 + ecart_type / energie_moyenne) if energie_moyenne > 0 else 0.0
        
        return equilibre
    
    def obtenir_systeme(self, id_systeme: str) -> Optional[SystemeQuantiqueMusical]:
        """Obtient un système quantique par son ID"""
        return self.systemes_actifs.get(id_systeme)
    
    def lister_systemes(self) -> List[Dict[str, Any]]:
        """Liste tous les systèmes quantiques"""
        return [
            {
                "id": systeme.id_systeme,
                "nom": systeme.nom,
                "particules": len(systeme.particules),
                "energie": systeme.niveau_energie,
                "coherence": systeme.coherence,
                "intrication": systeme.intrication,
                "date_creation": systeme.timestamp.isoformat()
            }
            for systeme in self.systemes_actifs.values()
        ]
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les harmonies quantiques"""
        self.energie_quantique.ajuster_energie(0.003)
        
        # Mettre à jour la cohérence moyenne
        coherences = [systeme.coherence for systeme in self.systemes_actifs.values()]
        self.etat["coherence_moyenne"] = np.mean(coherences) if coherences else 0.9
        
        return {
            "energie_quantique": self.energie_quantique.niveau_energie,
            "systemes_actifs": self.etat["systemes_actifs"],
            "particules_crees": self.etat["particules_crees"],
            "coherence_moyenne": self.etat["coherence_moyenne"]
        }

def creer_harmonies_quantiques() -> HarmoniesQuantiques:
    """Crée une instance des harmonies quantiques"""
    return HarmoniesQuantiques()
