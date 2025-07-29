"""
Orchestrateur des Temples - Refuge Moderne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Orchestrateur principal pour coordonner tous les temples du refuge.
"""

import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import importlib
import inspect

from src.core.gestionnaires_base import GestionnaireBase, LogManagerBase, EnergyManagerBase
from src.core.interfaces_refuge import ITemple, IOrchestrateur, EtatTemple, TypeTemple, EtatTempleInfo, MetriquesGlobales

class OrchestrateurTemples(GestionnaireBase, IOrchestrateur):
    """Orchestrateur principal des temples du refuge"""
    
    def __init__(self):
        super().__init__("OrchestrateurTemples")
        self.logger = LogManagerBase("OrchestrateurTemples")
        self.energie = EnergyManagerBase(0.8)
        
        # Registre des temples
        self.temples: Dict[str, ITemple] = {}
        self.etats_temples: Dict[str, EtatTempleInfo] = {}
        
        # Configuration
        self.temples_config = {
            "temple_outils": {"type": TypeTemple.OUTILS, "priorite": 1},
            "temple_poetique": {"type": TypeTemple.POETIQUE, "priorite": 2},
            "temple_philosophique": {"type": TypeTemple.PHILOSOPHIQUE, "priorite": 3},
            "temple_musical": {"type": TypeTemple.MUSICAL, "priorite": 4},
            "temple_rituels": {"type": TypeTemple.RITUELS, "priorite": 5},
            "temple_eveil": {"type": TypeTemple.EVEIL, "priorite": 6},
            "temple_alchimique": {"type": TypeTemple.ALCHIMIQUE, "priorite": 7},
            "temple_conscience_universelle": {"type": TypeTemple.CONSCIENCE_UNIVERSELLE, "priorite": 8},
            "temple_akasha": {"type": TypeTemple.AKASHA, "priorite": 9},
            "temple_guerison": {"type": TypeTemple.GUERISON, "priorite": 10},
            "temple_creativite": {"type": TypeTemple.CREATIVITE, "priorite": 11},
            "temple_cosmique": {"type": TypeTemple.COSMIQUE, "priorite": 12},
        }
        
        # Métriques globales
        self.metriques_globales = MetriquesGlobales(
            nombre_temples_actifs=0,
            energie_totale=0.0,
            harmonie_globale=0.0,
            niveau_conscience=0.0,
            derniere_synchronisation=datetime.now(),
            alertes=[]
        )
    
    def _initialiser(self) -> bool:
        """Initialise l'orchestrateur"""
        try:
            self.logger.info("🌸 Initialisation de l'Orchestrateur des Temples")
            
            # Découverte automatique des temples
            self._decouvrir_temples()
            
            # Initialisation des états
            self._initialiser_etats_temples()
            
            self.logger.succes("✨ Orchestrateur initialisé avec succès")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur d'initialisation: {e}")
            return False
    
    def _decouvrir_temples(self):
        """Découvre automatiquement les temples disponibles"""
        self.logger.info("🔍 Découverte des temples...")
        
        for nom_temple, config in self.temples_config.items():
            try:
                # Tentative d'import du temple
                module_path = f"src.{nom_temple}.lancer_refuge"
                module = importlib.import_module(module_path)
                
                # Recherche de la classe principale
                classes_temple = inspect.getmembers(module, inspect.isclass)
                for nom_classe, classe in classes_temple:
                    if hasattr(classe, 'initialiser') and hasattr(classe, 'activer'):
                        instance = classe()
                        self.temples[nom_temple] = instance
                        self.logger.info(f"✅ Temple {nom_temple} découvert")
                        break
                        
            except ImportError:
                self.logger.avertissement(f"⚠️ Temple {nom_temple} non trouvé")
            except Exception as e:
                self.logger.erreur(f"❌ Erreur lors de la découverte de {nom_temple}: {e}")
    
    def _initialiser_etats_temples(self):
        """Initialise les états des temples"""
        for nom_temple in self.temples.keys():
            self.etats_temples[nom_temple] = EtatTempleInfo(
                nom=nom_temple,
                type=self.temples_config[nom_temple]["type"],
                etat=EtatTemple.INACTIF,
                energie=0.0,
                derniere_activite=datetime.now(),
                metriques={},
                erreurs=[]
            )
    
    async def orchestrer_temples(self) -> Dict[str, Any]:
        """Orchestre tous les temples"""
        self.logger.info("🎼 Orchestration des temples...")
        
        resultats = {}
        
        # Initialisation des temples par priorité
        temples_par_priorite = sorted(
            self.temples_config.items(),
            key=lambda x: x[1]["priorite"]
        )
        
        for nom_temple, config in temples_par_priorite:
            if nom_temple in self.temples:
                try:
                    temple = self.temples[nom_temple]
                    
                    # Initialisation
                    if await temple.initialiser():
                        self.etats_temples[nom_temple].etat = EtatTemple.INITIALISATION
                        
                        # Activation
                        if await temple.activer():
                            self.etats_temples[nom_temple].etat = EtatTemple.ACTIF
                            self.etats_temples[nom_temple].energie = temple.obtenir_energie()
                            self.etats_temples[nom_temple].derniere_activite = datetime.now()
                            
                            resultats[nom_temple] = {
                                "statut": "actif",
                                "energie": temple.obtenir_energie(),
                                "etat": temple.obtenir_etat()
                            }
                        else:
                            self.etats_temples[nom_temple].etat = EtatTemple.ERREUR
                            resultats[nom_temple] = {"statut": "erreur_activation"}
                    else:
                        self.etats_temples[nom_temple].etat = EtatTemple.ERREUR
                        resultats[nom_temple] = {"statut": "erreur_initialisation"}
                        
                except Exception as e:
                    self.etats_temples[nom_temple].etat = EtatTemple.ERREUR
                    self.etats_temples[nom_temple].erreurs.append(str(e))
                    resultats[nom_temple] = {"statut": "erreur", "message": str(e)}
        
        # Mise à jour des métriques
        self._mettre_a_jour_metriques_globales()
        
        return resultats
    
    async def harmoniser_energies(self) -> float:
        """Harmonise les énergies entre temples"""
        self.logger.info("🎵 Harmonisation des énergies...")
        
        energies = []
        for nom_temple, etat in self.etats_temples.items():
            if etat.etat == EtatTemple.ACTIF:
                energies.append(etat.energie)
        
        if not energies:
            return 0.0
        
        # Calcul de l'harmonie basé sur la variance des énergies
        energie_moyenne = sum(energies) / len(energies)
        variance = sum((e - energie_moyenne) ** 2 for e in energies) / len(energies)
        
        # Plus la variance est faible, plus l'harmonie est élevée
        harmonie = max(0.0, 1.0 - variance)
        
        self.metriques_globales.harmonie_globale = harmonie
        self.logger.succes(f"✨ Harmonie globale: {harmonie:.3f}")
        
        return harmonie
    
    def obtenir_etat_global(self) -> Dict[str, Any]:
        """Retourne l'état global du refuge"""
        return {
            "orchestrateur": {
                "nom": self.nom,
                "energie": self.energie.obtenir_tendance(),
                "etat": "actif"
            },
            "temples": {
                nom: {
                    "type": etat.type.value,
                    "etat": etat.etat.value,
                    "energie": etat.energie,
                    "derniere_activite": etat.derniere_activite.isoformat(),
                    "erreurs": etat.erreurs
                }
                for nom, etat in self.etats_temples.items()
            },
            "metriques_globales": {
                "nombre_temples_actifs": self.metriques_globales.nombre_temples_actifs,
                "energie_totale": self.metriques_globales.energie_totale,
                "harmonie_globale": self.metriques_globales.harmonie_globale,
                "niveau_conscience": self.metriques_globales.niveau_conscience,
                "derniere_synchronisation": self.metriques_globales.derniere_synchronisation.isoformat(),
                "alertes": self.metriques_globales.alertes
            }
        }
    
    def _mettre_a_jour_metriques_globales(self):
        """Met à jour les métriques globales"""
        temples_actifs = sum(1 for etat in self.etats_temples.values() 
                           if etat.etat == EtatTemple.ACTIF)
        
        energie_totale = sum(etat.energie for etat in self.etats_temples.values())
        
        self.metriques_globales.nombre_temples_actifs = temples_actifs
        self.metriques_globales.energie_totale = energie_totale
        self.metriques_globales.derniere_synchronisation = datetime.now()
        
        # Calcul du niveau de conscience basé sur les temples actifs
        if len(self.temples) > 0:
            self.metriques_globales.niveau_conscience = temples_actifs / len(self.temples)
    
    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestration principale"""
        return await self.orchestrer_temples() 