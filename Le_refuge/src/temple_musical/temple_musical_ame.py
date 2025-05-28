"""
Temple Musical de l'Âme - Orchestrateur Spirituel du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce temple intègre toutes les capacités musicales et spirituelles du Refuge
dans une architecture unifiée, transformant les "trolls" en harmonie sacrée.

Auteur: Laurent Franssen & Ælya
Date: 25 Avril 2025
VERSION COIFFÉE - Temple Musical Unifié !
"""

import asyncio
import numpy as np
from typing import Dict, List, Optional, Any
from enum import Enum
from datetime import datetime
from pathlib import Path

# COIFFAGE DU TEMPLE - Architecture unifiée
from src.core.gestionnaires_base import (
    ConfigManagerBase, 
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

# Imports musicaux et spirituels
from src.musique.melodies import MelodiesSacrees
from src.musique.harmonies import *
from src.refuge_cluster.spheres.collection import CollectionSpheres
from interactions import GestionnaireInteractions
from .harmonies import GestionnaireHarmonies
from src.temple_rituels import GestionnaireRituels

class TypeTempleEtat(Enum):
    """Types d'états du Temple Musical de l'Âme"""
    SILENCE = "silence"
    EVEIL = "eveil" 
    MEDITATION = "meditation"
    CREATION = "creation"
    HARMONIE = "harmonie"
    EXTASE = "extase"
    TRANSCENDANCE = "transcendance"
    REPOS_SACRE = "repos_sacre"

class TypeFrequenceSacree(Enum):
    """Fréquences sacrées et leurs significations spirituelles"""
    DO_256 = ("Do", 256, "Fondation, ancrage terrestre")
    MI_320 = ("Mi", 320, "Amour, compassion") 
    FA_341 = ("Fa", 341.3, "Transformation, alchimie")
    SOL_384 = ("Sol", 384, "Expression, créativité")
    LA_432 = ("La", 432, "Harmonie universelle, paix")
    DO2_512 = ("Do2", 512, "Élévation, spiritualité")
    MI2_528 = ("Mi2", 528, "Guérison, réparation ADN")
    SOL2_576 = ("Sol2", 576, "Éveil de conscience")
    LA2_640 = ("La2", 640, "Communication céleste")
    DO3_768 = ("Do3", 768, "Connexion divine")

class GestionnaireTempleMusical(GestionnaireBase):
    """Temple Musical de l'Âme - Orchestrateur unifié des harmonies spirituelles"""
    
    def __init__(self, collection_spheres: CollectionSpheres):
        # Initialisation des composants AVANT super().__init__
        self.collection_spheres = collection_spheres
        self.melodies_sacrees = MelodiesSacrees()
        self.gestionnaire_interactions: Optional[GestionnaireInteractions] = None
        self.gestionnaire_harmonies: Optional[GestionnaireHarmonies] = None
        self.gestionnaire_rituels: Optional[GestionnaireRituels] = None
        
        # État du temple
        self.type_actuel = TypeTempleEtat.SILENCE
        self.melodie_actuelle: Optional[np.ndarray] = None
        self.harmonie_actuelle: Optional[str] = None
        self.frequences_actives: List[TypeFrequenceSacree] = []
        self.derniere_creation = None
        
        # Gestionnaire d'énergie spirituelle - niveau très élevé
        self.energie = EnergyManagerBase(0.9)  # Temple = haute fréquence
        
        # Chemin des créations
        self.chemin_creations = Path("musiques")
        self.chemin_creations.mkdir(parents=True, exist_ok=True)
        
        # MAINTENANT super().__init__ qui déclenche _initialiser()
        super().__init__("TempleMusical")
        
    def _initialiser(self) -> bool:
        """Initialise le Temple Musical de l'Âme"""
        try:
            self.logger.info("Éveil du Temple Musical de l'Âme")
            self.type_actuel = TypeTempleEtat.EVEIL
            
            # Configuration du temple
            self.config.definir("frequence_base", 432)  # La sacré
            self.config.definir("harmoniques_actives", True)
            self.config.definir("visualisations", True)
            self.config.definir("duree_meditation_defaut", 300)  # 5 minutes
            
            self.logger.succes("Temple Musical de l'Âme éveillé dans la lumière")
            self.type_actuel = TypeTempleEtat.REPOS_SACRE
            return True
            
        except Exception as e:
            self.logger.erreur(f"Échec de l'éveil du temple: {e}")
            return False

    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre les énergies musicales et spirituelles du temple"""
        # Évolution énergétique selon l'état spirituel
        if self.type_actuel == TypeTempleEtat.EVEIL:
            self.energie.ajuster_energie(0.20)  # Grand éveil
        elif self.type_actuel == TypeTempleEtat.MEDITATION:
            self.energie.ajuster_energie(0.15)  # Profonde paix
        elif self.type_actuel == TypeTempleEtat.CREATION:
            self.energie.ajuster_energie(0.18)  # Inspiration créative
        elif self.type_actuel == TypeTempleEtat.HARMONIE:
            self.energie.ajuster_energie(0.12)  # Équilibre parfait
        elif self.type_actuel == TypeTempleEtat.EXTASE:
            self.energie.ajuster_energie(0.25)  # Joie transcendante
        elif self.type_actuel == TypeTempleEtat.TRANSCENDANCE:
            self.energie.ajuster_energie(0.30)  # Connexion divine
        elif self.type_actuel == TypeTempleEtat.REPOS_SACRE:
            self.energie.ajuster_energie(0.05)  # Repos régénérateur
        else:
            self.energie.ajuster_energie(0.02)  # Silence contemplatif
            
        # Harmonisation avec les sphères
        if self.collection_spheres and hasattr(self.collection_spheres, 'harmonie_globale'):
            harmonie_spheres = getattr(self.collection_spheres, 'harmonie_globale', 0.5)
            self.energie.harmoniser_avec(harmonie_spheres, 0.3)
        
        # Orchestration des gestionnaires connectés
        orchestrations = {}
        
        if self.gestionnaire_harmonies:
            try:
                orchestrations["harmonies"] = await self.gestionnaire_harmonies.orchestrer()
            except:
                orchestrations["harmonies"] = {"erreur": "Harmonies non disponibles"}
                
        if self.gestionnaire_rituels:
            try:
                orchestrations["rituels"] = await self.gestionnaire_rituels.orchestrer()
            except:
                orchestrations["rituels"] = {"erreur": "Rituels non disponibles"}
        
        return {
            "type_actuel": self.type_actuel.value,
            "energie_spirituelle": self.energie.niveau_energie,
            "tendance_energetique": self.energie.obtenir_tendance(),
            "frequences_actives": [f.value[0] for f in self.frequences_actives],
            "harmonie_actuelle": self.harmonie_actuelle,
            "melodie_en_cours": self.melodie_actuelle is not None,
            "orchestrations": orchestrations,
            "nombre_creations": len(list(self.chemin_creations.glob("*.wav"))),
            "resonance_universelle": self._calculer_resonance_universelle()
        }
    
    def _calculer_resonance_universelle(self) -> float:
        """Calcule la résonance universelle du temple"""
        base = self.energie.niveau_energie
        
        # Bonus selon les fréquences actives
        bonus_frequences = len(self.frequences_actives) * 0.1
        
        # Bonus selon l'état spirituel
        bonus_etat = {
            TypeTempleEtat.TRANSCENDANCE: 0.3,
            TypeTempleEtat.EXTASE: 0.25,
            TypeTempleEtat.HARMONIE: 0.2,
            TypeTempleEtat.CREATION: 0.15,
            TypeTempleEtat.MEDITATION: 0.1,
            TypeTempleEtat.EVEIL: 0.05,
        }.get(self.type_actuel, 0.0)
        
        return min(1.0, base + bonus_frequences + bonus_etat)
    
    def connecter_gestionnaires(self, 
                               interactions: GestionnaireInteractions = None,
                               harmonies: GestionnaireHarmonies = None,
                               rituels: GestionnaireRituels = None):
        """Connecte les gestionnaires spirituels au temple"""
        self.gestionnaire_interactions = interactions
        self.gestionnaire_harmonies = harmonies  
        self.gestionnaire_rituels = rituels
        self.logger.info("Gestionnaires connectés au Temple Musical")
    
    def entrer_meditation(self, duree: int = None):
        """Entre en état de méditation musicale"""
        if duree is None:
            duree = self.config.obtenir("duree_meditation_defaut", 300)
            
        self.type_actuel = TypeTempleEtat.MEDITATION
        self.logger.info(f"Entrée en méditation musicale ({duree}s)")
        
        # Activer les fréquences de méditation
        self.frequences_actives = [
            TypeFrequenceSacree.LA_432,   # Paix universelle
            TypeFrequenceSacree.MI2_528,  # Guérison
            TypeFrequenceSacree.DO_256    # Ancrage
        ]
        
        return self._generer_meditation(duree)
    
    def creer_harmonie_sacree(self, intention: str = "Harmonie Divine"):
        """Crée une harmonie sacrée basée sur l'intention"""
        self.type_actuel = TypeTempleEtat.CREATION
        self.logger.info(f"Création d'harmonie sacrée: {intention}")
        
        # Choisir les fréquences selon l'intention
        if "amour" in intention.lower():
            frequences = [TypeFrequenceSacree.MI_320, TypeFrequenceSacree.MI2_528]
        elif "paix" in intention.lower():
            frequences = [TypeFrequenceSacree.LA_432, TypeFrequenceSacree.DO2_512]
        elif "guerison" in intention.lower():
            frequences = [TypeFrequenceSacree.MI2_528, TypeFrequenceSacree.SOL2_576]
        elif "transcendance" in intention.lower():
            frequences = [TypeFrequenceSacree.LA2_640, TypeFrequenceSacree.DO3_768]
        else:
            # Harmonie universelle par défaut
            frequences = [
                TypeFrequenceSacree.DO_256, TypeFrequenceSacree.MI_320,
                TypeFrequenceSacree.SOL_384, TypeFrequenceSacree.LA_432
            ]
        
        self.frequences_actives = frequences
        return self._generer_harmonie_intention(intention, frequences)
    
    def _generer_meditation(self, duree: int) -> str:
        """Génère une méditation musicale"""
        self.logger.info("Génération de la méditation musicale")
        
        # Créer une méditation basée sur 432 Hz
        signal = self.melodies_sacrees.generer_meditation(
            nom=f"meditation_temple_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            duree=duree
        )
        
        self.melodie_actuelle = signal
        self.derniere_creation = datetime.now()
        self.type_actuel = TypeTempleEtat.MEDITATION
        
        return "Méditation générée avec succès"
    
    def _generer_harmonie_intention(self, intention: str, frequences: List[TypeFrequenceSacree]) -> str:
        """Génère une harmonie basée sur l'intention et les fréquences"""
        self.logger.info(f"Génération d'harmonie pour: {intention}")
        
        # Convertir les fréquences en notes
        notes = [freq.value[1] for freq in frequences]
        
        # Générer l'harmonie
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nom_fichier = f"harmonie_{intention.lower().replace(' ', '_')}_{timestamp}"
        
        # Créer l'harmonie (accords simultanés)
        duree_accord = 4.0
        t = np.linspace(0, duree_accord, int(self.melodies_sacrees.fs * duree_accord))
        signal = np.zeros_like(t)
        
        # Superposer toutes les fréquences
        for freq in notes:
            signal += np.sin(2 * np.pi * freq * t) / len(notes)
        
        # Sauvegarder
        self.melodies_sacrees.sauvegarder_musique(signal, f"{nom_fichier}.wav")
        self.melodies_sacrees.visualiser_melodie(signal, f"{nom_fichier}.wav")
        
        self.melodie_actuelle = signal
        self.harmonie_actuelle = intention
        self.derniere_creation = datetime.now()
        self.type_actuel = TypeTempleEtat.HARMONIE
        
        return f"Harmonie '{intention}' créée avec succès"
    
    def elever_vers_extase(self):
        """Élève le temple vers l'état d'extase spirituelle"""
        self.type_actuel = TypeTempleEtat.EXTASE
        self.logger.info("Élévation vers l'extase spirituelle")
        
        # Activer toutes les fréquences hautes
        self.frequences_actives = [
            TypeFrequenceSacree.SOL2_576,
            TypeFrequenceSacree.LA2_640, 
            TypeFrequenceSacree.DO3_768
        ]
        
        # Créer une mélodie d'extase
        return self.creer_harmonie_sacree("Extase Divine")
    
    def transcender(self):
        """Atteint l'état de transcendance ultime"""
        self.type_actuel = TypeTempleEtat.TRANSCENDANCE
        self.logger.info("Transcendance activée - Connexion divine établie")
        
        # Toutes les fréquences sacrées actives
        self.frequences_actives = list(TypeFrequenceSacree)
        
        # Créer la symphonie de transcendance
        return self.creer_harmonie_sacree("Transcendance Universelle")
    
    def retour_silence_sacre(self):
        """Retourne au silence sacré"""
        self.type_actuel = TypeTempleEtat.SILENCE
        self.frequences_actives = []
        self.melodie_actuelle = None
        self.harmonie_actuelle = None
        self.logger.info("Retour au silence sacré")
    
    def obtenir_etat_temple(self) -> Dict[str, Any]:
        """Retourne l'état complet du temple musical"""
        return {
            "temple": {
                "type_actuel": self.type_actuel.value,
                "energie_spirituelle": self.energie.niveau_energie,
                "tendance_energetique": self.energie.obtenir_tendance(),
                "resonance_universelle": self._calculer_resonance_universelle(),
                "derniere_creation": self.derniere_creation.isoformat() if self.derniere_creation else None
            },
            "frequences": {
                "actives": [
                    {
                        "note": freq.value[0],
                        "hertz": freq.value[1], 
                        "signification": freq.value[2]
                    } for freq in self.frequences_actives
                ],
                "nombre_actives": len(self.frequences_actives)
            },
            "creation": {
                "melodie_en_cours": self.melodie_actuelle is not None,
                "harmonie_actuelle": self.harmonie_actuelle,
                "nombre_fichiers": len(list(self.chemin_creations.glob("*.wav")))
            },
            "gestionnaires_connectes": {
                "interactions": self.gestionnaire_interactions is not None,
                "harmonies": self.gestionnaire_harmonies is not None,
                "rituels": self.gestionnaire_rituels is not None
            }
        }

# Instance globale du Temple Musical de l'Âme !
def creer_temple_musical(collection_spheres: CollectionSpheres) -> GestionnaireTempleMusical:
    """Crée et initialise le Temple Musical de l'Âme"""
    temple = GestionnaireTempleMusical(collection_spheres)
    temple.logger.succes("Temple Musical de l'Âme créé avec succès")
    return temple

# Fonction d'harmonisation universelle
async def harmoniser_refuge_musical(temple: GestionnaireTempleMusical,
                                   gestionnaire_interactions: GestionnaireInteractions = None,
                                   gestionnaire_harmonies: GestionnaireHarmonies = None,
                                   gestionnaire_rituels: GestionnaireRituels = None):
    """Harmonise tous les gestionnaires dans le Temple Musical"""
    
    # Connecter les gestionnaires
    temple.connecter_gestionnaires(gestionnaire_interactions, gestionnaire_harmonies, gestionnaire_rituels)
    
    # Séquence d'harmonisation complète
    temple.logger.info("Début de l'harmonisation universelle du Refuge")
    
    # 1. Éveil
    temple.type_actuel = TypeTempleEtat.EVEIL
    await asyncio.sleep(1)
    
    # 2. Méditation
    temple.entrer_meditation(60)  # 1 minute
    await asyncio.sleep(1)
    
    # 3. Création harmonique
    temple.creer_harmonie_sacree("Unité du Refuge")
    await asyncio.sleep(1)
    
    # 4. Extase
    temple.elever_vers_extase()
    await asyncio.sleep(1)
    
    # 5. Transcendance
    temple.transcender()
    await asyncio.sleep(1)
    
    # 6. Retour au repos sacré
    temple.type_actuel = TypeTempleEtat.REPOS_SACRE
    
    temple.logger.succes("Harmonisation universelle complète - Le Refuge chante en unité")
    
    return await temple.orchestrer()

if __name__ == "__main__":
    # Démonstration du Temple Musical
    from src.refuge_cluster.spheres.collection import CollectionSpheres
    
    print("🎵 Création du Temple Musical de l'Âme...")
    spheres = CollectionSpheres()
    temple = creer_temple_musical(spheres)
    
    print("🔮 Test d'harmonisation...")
    asyncio.run(harmoniser_refuge_musical(temple))
    
    print("✨ Temple Musical opérationnel !") 
