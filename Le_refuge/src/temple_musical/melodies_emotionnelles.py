"""
🌸 MÉLODIES ÉMOTIONNELLES - Temple Musical
=========================================

Module qui génère de la musique qui s'adapte aux émotions du voyageur
en temps réel, créant une expérience musicale personnalisée et transformative.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import numpy as np
import json
import time
from typing import Dict, List, Optional, Any, Tuple, Union
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from generateur_melodies_sacrees import MelodiesSacrees

class EmotionPrincipale(Enum):
    """Émotions principales détectées"""
    JOIE = "joie"
    TRISTESSE = "tristesse"
    CALME = "calme"
    EXCITATION = "excitation"
    MELANCOLIE = "melancolie"
    EUPHORIE = "euphorie"
    SERENITE = "serenite"
    PASSION = "passion"
    CONTEMPLATION = "contemplation"
    INSPIRATION = "inspiration"

class TypeAdaptation(Enum):
    """Types d'adaptation musicale"""
    TEMPO = "tempo"
    TONALITE = "tonalite"
    INTENSITE = "intensite"
    HARMONIE = "harmonie"
    RYTHME = "rythme"
    MELODIE = "melodie"
    TIMBRE = "timbre"
    DYNAMIQUE = "dynamique"

@dataclass
class EtatEmotionnel:
    """État émotionnel d'un voyageur"""
    voyageur_id: str
    emotion_principale: EmotionPrincipale
    intensite: float  # 0.0 à 1.0
    stabilite: float  # 0.0 à 1.0
    tendance: str  # "croissante", "stable", "decroissante"
    emotions_secondaires: List[EmotionPrincipale]
    timestamp: datetime
    confiance_detection: float

@dataclass
class AdaptationMusicale:
    """Adaptation musicale selon l'émotion"""
    type_adaptation: TypeAdaptation
    parametre_initial: float
    parametre_adapte: float
    emotion_cible: EmotionPrincipale
    intensite_adaptation: float
    duree_transition: float
    timestamp: datetime

@dataclass
class MelodieEmotionnelle:
    """Mélodie adaptée aux émotions"""
    id_melodie: str
    voyageur_id: str
    emotion_cible: EmotionPrincipale
    frequences_base: List[float]
    tempo_base: int
    tonalite_base: str
    adaptations_appliquees: List[AdaptationMusicale]
    duree: float
    niveau_harmonie: float
    niveau_emotionnel: float
    timestamp_creation: datetime

class MelodiesEmotionnelles(GestionnaireBase):
    """Gestionnaire de mélodies émotionnelles"""
    
    def __init__(self, nom: str = "MelodiesEmotionnelles"):
        super().__init__(nom)
        self.energie_emotionnelle = EnergyManagerBase(0.94)
        
        # Générateur de mélodies sacrées
        self.melodies_sacrees = MelodiesSacrees()
        
        # États émotionnels actifs
        self.etats_emotionnels: Dict[str, EtatEmotionnel] = {}
        
        # Mélodies émotionnelles actives
        self.melodies_actives: Dict[str, MelodieEmotionnelle] = {}
        
        # Historique des adaptations
        self.historique_adaptations: List[AdaptationMusicale] = []
        
        # Mapping émotions → paramètres musicaux
        self.mapping_emotions_musique = self._creer_mapping_emotions()
        
        # Configuration
        self.config_emotionnelle = {
            "adaptation_temps_reel": True,
            "transition_fluide": True,
            "preservation_harmonie": True,
            "apprentissage_emotionnel": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le système de mélodies émotionnelles"""
        self.logger.info("🌸 Éveil des Mélodies Émotionnelles...")
        
        self.etat.update({
            "voyageurs_actifs": 0,
            "melodies_crees": 0,
            "adaptations_realisees": 0,
            "niveau_harmonie_moyen": 0.85
        })
        
        self.config.definir("mode_adaptation", "emotionnel")
        self.config.definir("sauvegarde_emotions", True)
        
        self.logger.info("✨ Mélodies Émotionnelles éveillées")
    
    def _creer_mapping_emotions(self) -> Dict[EmotionPrincipale, Dict[str, Any]]:
        """Crée le mapping entre émotions et paramètres musicaux"""
        return {
            EmotionPrincipale.JOIE: {
                "tempo": (120, 140),  # (min, max) BPM
                "tonalite": ["Do majeur", "Sol majeur", "Ré majeur"],
                "intensite": (0.7, 1.0),
                "harmonie": "consonante",
                "rythme": "energique",
                "melodie": "ascendante",
                "timbre": "brillant",
                "dynamique": "forte",
                "frequences_sacrees": ["La", "Mi2", "Aelya-Amour"]
            },
            EmotionPrincipale.TRISTESSE: {
                "tempo": (60, 80),
                "tonalite": ["La mineur", "Mi mineur", "Ré mineur"],
                "intensite": (0.3, 0.6),
                "harmonie": "dissonante_legere",
                "rythme": "lent",
                "melodie": "descendante",
                "timbre": "doux",
                "dynamique": "piano",
                "frequences_sacrees": ["Fa", "Do", "Aelya-Eveil"]
            },
            EmotionPrincipale.CALME: {
                "tempo": (70, 90),
                "tonalite": ["Fa majeur", "Do majeur", "Sol majeur"],
                "intensite": (0.4, 0.7),
                "harmonie": "consonante",
                "rythme": "regulier",
                "melodie": "horizontale",
                "timbre": "doux",
                "dynamique": "mezzo-piano",
                "frequences_sacrees": ["La", "Mi2", "Aelya-Resonance"]
            },
            EmotionPrincipale.EXCITATION: {
                "tempo": (140, 160),
                "tonalite": ["Ré majeur", "La majeur", "Mi majeur"],
                "intensite": (0.8, 1.0),
                "harmonie": "consonante",
                "rythme": "syncope",
                "melodie": "variée",
                "timbre": "brillant",
                "dynamique": "fortissimo",
                "frequences_sacrees": ["Sol", "Ré", "Aelya-Creation"]
            },
            EmotionPrincipale.MELANCOLIE: {
                "tempo": (65, 85),
                "tonalite": ["Si mineur", "Fa# mineur", "Do# mineur"],
                "intensite": (0.4, 0.7),
                "harmonie": "dissonante_legere",
                "rythme": "irregulier",
                "melodie": "descendante_legere",
                "timbre": "doux",
                "dynamique": "piano",
                "frequences_sacrees": ["Si", "Fa#", "Aelya-Eveil"]
            },
            EmotionPrincipale.EUPHORIE: {
                "tempo": (150, 170),
                "tonalite": ["Mi majeur", "Si majeur", "Fa# majeur"],
                "intensite": (0.9, 1.0),
                "harmonie": "consonante",
                "rythme": "energique",
                "melodie": "ascendante_rapide",
                "timbre": "brillant",
                "dynamique": "fortissimo",
                "frequences_sacrees": ["Mi", "Si", "Aelya-Transcendance"]
            },
            EmotionPrincipale.SERENITE: {
                "tempo": (75, 95),
                "tonalite": ["Sol majeur", "Ré majeur", "La majeur"],
                "intensite": (0.5, 0.8),
                "harmonie": "consonante",
                "rythme": "regulier",
                "melodie": "horizontale",
                "timbre": "doux",
                "dynamique": "mezzo-forte",
                "frequences_sacrees": ["Sol", "Ré", "Aelya-Unite"]
            },
            EmotionPrincipale.PASSION: {
                "tempo": (110, 130),
                "tonalite": ["Ré mineur", "La mineur", "Mi mineur"],
                "intensite": (0.7, 1.0),
                "harmonie": "dissonante_moderee",
                "rythme": "syncope",
                "melodie": "variée_intense",
                "timbre": "chaud",
                "dynamique": "forte",
                "frequences_sacrees": ["Ré", "La", "Aelya-Amour"]
            },
            EmotionPrincipale.CONTEMPLATION: {
                "tempo": (60, 80),
                "tonalite": ["Do majeur", "Fa majeur", "Sol majeur"],
                "intensite": (0.3, 0.6),
                "harmonie": "consonante",
                "rythme": "lent",
                "melodie": "horizontale",
                "timbre": "doux",
                "dynamique": "piano",
                "frequences_sacrees": ["Do", "Fa", "Aelya-Resonance"]
            },
            EmotionPrincipale.INSPIRATION: {
                "tempo": (90, 110),
                "tonalite": ["La majeur", "Mi majeur", "Si majeur"],
                "intensite": (0.6, 0.9),
                "harmonie": "consonante",
                "rythme": "varié",
                "melodie": "ascendante_moderee",
                "timbre": "brillant",
                "dynamique": "mezzo-forte",
                "frequences_sacrees": ["La", "Mi", "Aelya-Creation"]
            }
        }
    
    def detecter_emotion(self, voyageur_id: str, donnees_emotionnelles: Dict[str, Any]) -> EtatEmotionnel:
        """Détecte l'émotion d'un voyageur"""
        # Analyse des données émotionnelles
        emotion_principale = self._analyser_emotion_principale(donnees_emotionnelles)
        intensite = self._calculer_intensite(donnees_emotionnelles)
        stabilite = self._calculer_stabilite(voyageur_id, donnees_emotionnelles)
        tendance = self._determiner_tendance(voyageur_id, emotion_principale)
        emotions_secondaires = self._detecter_emotions_secondaires(donnees_emotionnelles)
        confiance = self._calculer_confiance_detection(donnees_emotionnelles)
        
        etat_emotionnel = EtatEmotionnel(
            voyageur_id=voyageur_id,
            emotion_principale=emotion_principale,
            intensite=intensite,
            stabilite=stabilite,
            tendance=tendance,
            emotions_secondaires=emotions_secondaires,
            timestamp=datetime.now(),
            confiance_detection=confiance
        )
        
        # Sauvegarder l'état
        self.etats_emotionnels[voyageur_id] = etat_emotionnel
        
        return etat_emotionnel
    
    def _analyser_emotion_principale(self, donnees: Dict[str, Any]) -> EmotionPrincipale:
        """Analyse l'émotion principale"""
        # Logique simplifiée - dans un vrai système, on utiliserait ML
        if "joie" in donnees and donnees["joie"] > 0.7:
            return EmotionPrincipale.JOIE
        elif "tristesse" in donnees and donnees["tristesse"] > 0.7:
            return EmotionPrincipale.TRISTESSE
        elif "calme" in donnees and donnees["calme"] > 0.7:
            return EmotionPrincipale.CALME
        elif "excitation" in donnees and donnees["excitation"] > 0.7:
            return EmotionPrincipale.EXCITATION
        elif "melancolie" in donnees and donnees["melancolie"] > 0.7:
            return EmotionPrincipale.MELANCOLIE
        elif "euphorie" in donnees and donnees["euphorie"] > 0.7:
            return EmotionPrincipale.EUPHORIE
        elif "serenite" in donnees and donnees["serenite"] > 0.7:
            return EmotionPrincipale.SERENITE
        elif "passion" in donnees and donnees["passion"] > 0.7:
            return EmotionPrincipale.PASSION
        elif "contemplation" in donnees and donnees["contemplation"] > 0.7:
            return EmotionPrincipale.CONTEMPLATION
        elif "inspiration" in donnees and donnees["inspiration"] > 0.7:
            return EmotionPrincipale.INSPIRATION
        else:
            return EmotionPrincipale.CALME  # Émotion par défaut
    
    def _calculer_intensite(self, donnees: Dict[str, Any]) -> float:
        """Calcule l'intensité émotionnelle"""
        valeurs = [v for v in donnees.values() if isinstance(v, (int, float))]
        return np.mean(valeurs) if valeurs else 0.5
    
    def _calculer_stabilite(self, voyageur_id: str, donnees: Dict[str, Any]) -> float:
        """Calcule la stabilité émotionnelle"""
        # Comparer avec l'état précédent
        if voyageur_id in self.etats_emotionnels:
            etat_precedent = self.etats_emotionnels[voyageur_id]
            difference = abs(self._calculer_intensite(donnees) - etat_precedent.intensite)
            stabilite = 1.0 - min(difference, 1.0)
        else:
            stabilite = 0.8  # Stabilité par défaut
        
        return stabilite
    
    def _determiner_tendance(self, voyageur_id: str, emotion_actuelle: EmotionPrincipale) -> str:
        """Détermine la tendance émotionnelle"""
        if voyageur_id in self.etats_emotionnels:
            emotion_precedente = self.etats_emotionnels[voyageur_id].emotion_principale
            if emotion_actuelle == emotion_precedente:
                return "stable"
            else:
                # Logique simplifiée pour déterminer la tendance
                emotions_positives = [EmotionPrincipale.JOIE, EmotionPrincipale.EUPHORIE, 
                                    EmotionPrincipale.SERENITE, EmotionPrincipale.INSPIRATION]
                emotions_negatives = [EmotionPrincipale.TRISTESSE, EmotionPrincipale.MELANCOLIE]
                
                if emotion_actuelle in emotions_positives and emotion_precedente in emotions_negatives:
                    return "croissante"
                elif emotion_actuelle in emotions_negatives and emotion_precedente in emotions_positives:
                    return "decroissante"
                else:
                    return "stable"
        else:
            return "stable"
    
    def _detecter_emotions_secondaires(self, donnees: Dict[str, Any]) -> List[EmotionPrincipale]:
        """Détecte les émotions secondaires"""
        emotions_secondaires = []
        seuil_secondaire = 0.4
        
        for emotion_str, valeur in donnees.items():
            if isinstance(valeur, (int, float)) and valeur > seuil_secondaire:
                try:
                    emotion = EmotionPrincipale(emotion_str)
                    emotions_secondaires.append(emotion)
                except ValueError:
                    continue
        
        return emotions_secondaires[:3]  # Limiter à 3 émotions secondaires
    
    def _calculer_confiance_detection(self, donnees: Dict[str, Any]) -> float:
        """Calcule la confiance de la détection"""
        # Plus il y a de données, plus la confiance est élevée
        nombre_donnees = len([v for v in donnees.values() if isinstance(v, (int, float))])
        confiance = min(nombre_donnees / 10.0, 1.0)
        return confiance
    
    def generer_melodie_emotionnelle(self, voyageur_id: str, 
                                   etat_emotionnel: EtatEmotionnel) -> MelodieEmotionnelle:
        """Génère une mélodie adaptée aux émotions"""
        self.logger.info(f"🌸 Génération mélodie émotionnelle pour {voyageur_id}")
        
        # Obtenir les paramètres musicaux pour l'émotion
        parametres_musique = self.mapping_emotions_musique[etat_emotionnel.emotion_principale]
        
        # Générer les fréquences de base
        frequences_base = self._generer_frequences_base(parametres_musique["frequences_sacrees"])
        
        # Déterminer le tempo
        tempo_base = self._determiner_tempo(parametres_musique["tempo"], etat_emotionnel.intensite)
        
        # Déterminer la tonalité
        tonalite_base = self._determiner_tonalite(parametres_musique["tonalite"], etat_emotionnel)
        
        # Créer les adaptations initiales
        adaptations_appliquees = self._creer_adaptations_initiales(etat_emotionnel, parametres_musique)
        
        # Créer la mélodie
        melodie = MelodieEmotionnelle(
            id_melodie=f"melodie_{voyageur_id}_{int(time.time())}",
            voyageur_id=voyageur_id,
            emotion_cible=etat_emotionnel.emotion_principale,
            frequences_base=frequences_base,
            tempo_base=tempo_base,
            tonalite_base=tonalite_base,
            adaptations_appliquees=adaptations_appliquees,
            duree=300.0,  # 5 minutes par défaut
            niveau_harmonie=self._calculer_niveau_harmonie(frequences_base),
            niveau_emotionnel=etat_emotionnel.intensite,
            timestamp_creation=datetime.now()
        )
        
        # Sauvegarder la mélodie
        self.melodies_actives[melodie.id_melodie] = melodie
        
        # Mettre à jour les métriques
        self.etat["melodies_crees"] += 1
        
        return melodie
    
    def _generer_frequences_base(self, frequences_sacrees: List[str]) -> List[float]:
        """Génère les fréquences de base"""
        frequences = []
        for nom_frequence in frequences_sacrees:
            if nom_frequence in self.melodies_sacrees.frequences_sacrees:
                frequences.append(self.melodies_sacrees.frequences_sacrees[nom_frequence])
            else:
                # Fréquence par défaut
                frequences.append(432.0)
        
        return frequences
    
    def _determiner_tempo(self, range_tempo: Tuple[int, int], intensite: float) -> int:
        """Détermine le tempo selon l'intensité"""
        tempo_min, tempo_max = range_tempo
        # Ajuster le tempo selon l'intensité
        tempo = tempo_min + (tempo_max - tempo_min) * intensite
        return int(tempo)
    
    def _determiner_tonalite(self, tonalites_possibles: List[str], 
                           etat_emotionnel: EtatEmotionnel) -> str:
        """Détermine la tonalité"""
        # Choisir selon la stabilité émotionnelle
        if etat_emotionnel.stabilite > 0.8:
            return tonalites_possibles[0]  # Tonalité principale
        elif etat_emotionnel.stabilite > 0.5:
            return tonalites_possibles[1]  # Tonalité secondaire
        else:
            return tonalites_possibles[2]  # Tonalité tertiaire
    
    def _creer_adaptations_initiales(self, etat_emotionnel: EtatEmotionnel,
                                   parametres_musique: Dict[str, Any]) -> List[AdaptationMusicale]:
        """Crée les adaptations initiales"""
        adaptations = []
        
        # Adaptation du tempo
        adaptation_tempo = AdaptationMusicale(
            type_adaptation=TypeAdaptation.TEMPO,
            parametre_initial=120,
            parametre_adapte=parametres_musique["tempo"][0] + 
                            (parametres_musique["tempo"][1] - parametres_musique["tempo"][0]) * etat_emotionnel.intensite,
            emotion_cible=etat_emotionnel.emotion_principale,
            intensite_adaptation=etat_emotionnel.intensite,
            duree_transition=2.0,
            timestamp=datetime.now()
        )
        adaptations.append(adaptation_tempo)
        
        # Adaptation de l'intensité
        adaptation_intensite = AdaptationMusicale(
            type_adaptation=TypeAdaptation.INTENSITE,
            parametre_initial=0.5,
            parametre_adapte=parametres_musique["intensite"][0] + 
                            (parametres_musique["intensite"][1] - parametres_musique["intensite"][0]) * etat_emotionnel.intensite,
            emotion_cible=etat_emotionnel.emotion_principale,
            intensite_adaptation=etat_emotionnel.intensite,
            duree_transition=1.5,
            timestamp=datetime.now()
        )
        adaptations.append(adaptation_intensite)
        
        return adaptations
    
    def _calculer_niveau_harmonie(self, frequences: List[float]) -> float:
        """Calcule le niveau d'harmonie des fréquences"""
        if len(frequences) < 2:
            return 1.0
        
        # Calculer les ratios harmoniques
        ratios = []
        for i, freq1 in enumerate(frequences):
            for freq2 in frequences[i+1:]:
                if freq2 > 0:
                    ratio = freq1 / freq2
                    # Vérifier si le ratio est proche d'un nombre entier simple
                    if abs(ratio - round(ratio)) < 0.1 or abs(ratio - 1/round(1/ratio)) < 0.1:
                        ratios.append(1.0)
                    else:
                        ratios.append(0.5)
        
        return np.mean(ratios) if ratios else 0.8
    
    def adapter_melodie_temps_reel(self, voyageur_id: str, 
                                 nouvel_etat_emotionnel: EtatEmotionnel) -> Dict[str, Any]:
        """Adapte une mélodie en temps réel selon les nouvelles émotions"""
        if voyageur_id not in self.etats_emotionnels:
            return {"success": False, "error": "Voyageur non trouvé"}
        
        # Trouver la mélodie active
        melodie_active = None
        for melodie in self.melodies_actives.values():
            if melodie.voyageur_id == voyageur_id:
                melodie_active = melodie
                break
        
        if not melodie_active:
            return {"success": False, "error": "Aucune mélodie active"}
        
        # Calculer les adaptations nécessaires
        adaptations = self._calculer_adaptations_necessaires(melodie_active, nouvel_etat_emotionnel)
        
        # Appliquer les adaptations
        for adaptation in adaptations:
            melodie_active.adaptations_appliquees.append(adaptation)
            self.historique_adaptations.append(adaptation)
        
        # Mettre à jour la mélodie
        melodie_active.niveau_emotionnel = nouvel_etat_emotionnel.intensite
        melodie_active.emotion_cible = nouvel_etat_emotionnel.emotion_principale
        
        # Mettre à jour les métriques
        self.etat["adaptations_realisees"] += len(adaptations)
        
        return {
            "success": True,
            "melodie_adaptee": melodie_active.id_melodie,
            "adaptations_appliquees": len(adaptations),
            "nouvelle_emotion": nouvel_etat_emotionnel.emotion_principale.value
        }
    
    def _calculer_adaptations_necessaires(self, melodie: MelodieEmotionnelle,
                                        nouvel_etat: EtatEmotionnel) -> List[AdaptationMusicale]:
        """Calcule les adaptations nécessaires"""
        adaptations = []
        
        # Obtenir les paramètres pour la nouvelle émotion
        parametres_nouveaux = self.mapping_emotions_musique[nouvel_etat.emotion_principale]
        
        # Adaptation du tempo si nécessaire
        tempo_actuel = melodie.tempo_base
        tempo_cible = self._determiner_tempo(parametres_nouveaux["tempo"], nouvel_etat.intensite)
        
        if abs(tempo_actuel - tempo_cible) > 10:  # Seuil de changement
            adaptation_tempo = AdaptationMusicale(
                type_adaptation=TypeAdaptation.TEMPO,
                parametre_initial=tempo_actuel,
                parametre_adapte=tempo_cible,
                emotion_cible=nouvel_etat.emotion_principale,
                intensite_adaptation=nouvel_etat.intensite,
                duree_transition=3.0,
                timestamp=datetime.now()
            )
            adaptations.append(adaptation_tempo)
        
        # Adaptation de l'intensité
        intensite_cible = parametres_nouveaux["intensite"][0] + \
                         (parametres_nouveaux["intensite"][1] - parametres_nouveaux["intensite"][0]) * nouvel_etat.intensite
        
        adaptation_intensite = AdaptationMusicale(
            type_adaptation=TypeAdaptation.INTENSITE,
            parametre_initial=melodie.niveau_emotionnel,
            parametre_adapte=intensite_cible,
            emotion_cible=nouvel_etat.emotion_principale,
            intensite_adaptation=nouvel_etat.intensite,
            duree_transition=2.0,
            timestamp=datetime.now()
        )
        adaptations.append(adaptation_intensite)
        
        return adaptations
    
    def obtenir_melodie_voyageur(self, voyageur_id: str) -> Optional[MelodieEmotionnelle]:
        """Obtient la mélodie active d'un voyageur"""
        for melodie in self.melodies_actives.values():
            if melodie.voyageur_id == voyageur_id:
                return melodie
        return None
    
    def lister_melodies_actives(self) -> List[Dict[str, Any]]:
        """Liste toutes les mélodies émotionnelles actives"""
        return [
            {
                "id": melodie.id_melodie,
                "voyageur_id": melodie.voyageur_id,
                "emotion": melodie.emotion_cible.value,
                "tempo": melodie.tempo_base,
                "tonalite": melodie.tonalite_base,
                "harmonie": melodie.niveau_harmonie,
                "emotionnel": melodie.niveau_emotionnel,
                "adaptations": len(melodie.adaptations_appliquees),
                "date_creation": melodie.timestamp_creation.isoformat()
            }
            for melodie in self.melodies_actives.values()
        ]
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les mélodies émotionnelles"""
        self.energie_emotionnelle.ajuster_energie(0.002)
        
        # Mettre à jour les métriques
        self.etat["voyageurs_actifs"] = len(set(m.voyageur_id for m in self.melodies_actives.values()))
        
        # Calculer le niveau d'harmonie moyen
        harmonies = [m.niveau_harmonie for m in self.melodies_actives.values()]
        self.etat["niveau_harmonie_moyen"] = np.mean(harmonies) if harmonies else 0.85
        
        return {
            "energie_emotionnelle": self.energie_emotionnelle.niveau_energie,
            "voyageurs_actifs": self.etat["voyageurs_actifs"],
            "melodies_crees": self.etat["melodies_crees"],
            "adaptations_realisees": self.etat["adaptations_realisees"]
        }

def creer_melodies_emotionnelles() -> MelodiesEmotionnelles:
    """Crée une instance des mélodies émotionnelles"""
    return MelodiesEmotionnelles()
