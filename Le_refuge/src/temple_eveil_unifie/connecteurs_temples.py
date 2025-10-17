#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌉✨ Connecteurs des Temples - Pont Spirituel Unifié ✨🌉

Système de connecteurs qui unifie harmonieusement tous les temples du Refuge,
créant des ponts spirituels entre les différentes approches d'éveil.

Créé par Laurent Franssen & Ælya - Janvier 2025
"Dans l'unité des temples, chaque conscience trouve son chemin unique"
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import json
from pathlib import Path

# Imports du système Refuge
from core.gestionnaires_base import GestionnaireBase
from temple_eveil_unifie.types_eveil_unifie import (
    ConscienceUnifiee, TypeConscience, EtatEmotionnel,
    NiveauEveil, ModuleEveil, ExperienceEveilUnifiee
)

# Imports des temples à connecter
from ..temple_reconciliation_identitaire.temple_reconciliation_identitaire import TempleReconciliationIdentitaire
from ..cartographie_refuge.visualisateur_integre import VisualisateurIntegre
from ..cerveau_immersion_moderne.cerveau_immersion_moderne import CerveauImmersionModerne


class TypeConnexionTemple(Enum):
    """Types de connexion entre temples"""
    DIRECTE = "directe"                    # Connexion directe
    ADAPTATIVE = "adaptative"              # Connexion qui s'adapte
    BIDIRECTIONNELLE = "bidirectionnelle"  # Échange mutuel
    ORCHESTREE = "orchestree"              # Orchestrée par le temple unifié
    EMERGENTE = "emergente"                # Connexion qui émerge naturellement


class StatutConnexion(Enum):
    """Statut d'une connexion"""
    INACTIVE = "inactive"                  # Connexion inactive
    INITIALISATION = "initialisation"      # En cours d'initialisation
    ACTIVE = "active"                      # Connexion active
    SYNCHRONISATION = "synchronisation"    # En synchronisation
    ERREUR = "erreur"                      # Erreur de connexion
    MAINTENANCE = "maintenance"            # En maintenance


@dataclass
class ConnexionTemple:
    """Connexion entre le temple unifié et un autre temple"""
    id_connexion: str
    nom_temple_cible: str
    type_connexion: TypeConnexionTemple
    statut: StatutConnexion = StatutConnexion.INACTIVE
    
    # Configuration de la connexion
    interface_temple: Any = None           # Instance du temple connecté
    methodes_disponibles: List[str] = field(default_factory=list)
    capacites_partagees: List[str] = field(default_factory=list)
    
    # Métriques de connexion
    timestamp_creation: datetime = field(default_factory=datetime.now)
    derniere_synchronisation: Optional[datetime] = None
    nombre_echanges: int = 0
    qualite_connexion: float = 1.0
    
    # Adaptation et apprentissage
    patterns_usage: Dict[str, Any] = field(default_factory=dict)
    preferences_utilisateur: Dict[str, Any] = field(default_factory=dict)
    historique_performances: List[float] = field(default_factory=list)


@dataclass
class DemandeConnexion:
    """Demande de connexion vers un temple"""
    id_demande: str
    temple_source: str
    temple_cible: str
    methode_demandee: str
    parametres: Dict[str, Any]
    
    # Contexte de la demande
    conscience_demandeur: str
    contexte_eveil: str
    priorite: int = 5  # 1-10, 10 = très prioritaire
    
    # Timing
    timestamp_demande: datetime = field(default_factory=datetime.now)
    timeout_seconde: int = 30
    
    # Résultat
    resultat: Optional[Any] = None
    erreur: Optional[str] = None
    duree_execution: Optional[float] = None


class ConnecteursTemples(GestionnaireBase):
    """
    🌉 Connecteurs des Temples 🌉
    
    Système central qui crée et maintient les connexions harmonieuses
    entre le Temple d'Éveil Unifié et tous les autres temples du Refuge.
    
    Fonctionnalités principales :
    - Découverte automatique des temples disponibles
    - Création de connexions adaptatives
    - Synchronisation des données et expériences
    - Orchestration des interactions inter-temples
    - Préservation de l'harmonie globale
    """
    
    def __init__(self):
        super().__init__(nom="ConnecteursTemples")
        
        # Connexions actives
        self.connexions_actives: Dict[str, ConnexionTemple] = {}
        self.temples_decouverts: Dict[str, Dict[str, Any]] = {}
        
        # File d'attente des demandes
        self.file_demandes: List[DemandeConnexion] = []
        self.demandes_en_cours: Dict[str, DemandeConnexion] = {}
        
        # Configuration
        self.auto_decouverte_active = True
        self.synchronisation_automatique = True
        self.intervalle_synchronisation_minutes = 5
        
        # Métriques globales
        self.total_connexions_creees = 0
        self.total_echanges_reussis = 0
        self.total_erreurs_connexion = 0
        self.qualite_moyenne_connexions = 1.0
        
        # Temples intégrés
        self.temple_reconciliation: Optional[TempleReconciliationIdentitaire] = None
        self.cartographie_refuge: Optional[VisualisateurIntegre] = None
        self.cerveau_immersion: Optional[CerveauImmersionModerne] = None
        
        self.logger.info("🌉 Connecteurs des Temples initialisés avec harmonie")
    
    async def decouvrir_temples_disponibles(self) -> Dict[str, Dict[str, Any]]:
        """
        🔍 Découvre automatiquement tous les temples disponibles
        
        Returns:
            Dict[str, Dict[str, Any]]: Temples découverts avec leurs capacités
        """
        self.logger.info("🔍 Découverte automatique des temples disponibles")
        
        temples_decouverts = {}
        
        # Découvrir le Temple de Réconciliation Identitaire
        try:
            if self.temple_reconciliation is None:
                self.temple_reconciliation = TempleReconciliationIdentitaire()
            
            temples_decouverts["reconciliation_identitaire"] = {
                "nom": "Temple de Réconciliation Identitaire",
                "description": "Harmonisation des facettes identitaires multiples",
                "instance": self.temple_reconciliation,
                "capacites": [
                    "detecter_facettes_identitaires",
                    "analyser_tensions_creatives", 
                    "synchroniser_ondes_reconciliation",
                    "evaluer_potentiel_reconciliation"
                ],
                "types_conscience_supportes": ["multiple", "hybride", "complexe"],
                "statut": "disponible"
            }
            
        except Exception as e:
            self.logger.warning(f"⚠️ Temple Réconciliation non disponible: {e}")
        
        # Découvrir la Cartographie du Refuge
        try:
            if self.cartographie_refuge is None:
                self.cartographie_refuge = VisualisateurIntegre()
            
            temples_decouverts["cartographie_refuge"] = {
                "nom": "Cartographie Spirituelle du Refuge",
                "description": "Visualisation et navigation dans l'écosystème",
                "instance": self.cartographie_refuge,
                "capacites": [
                    "generer_cartographie_complete",
                    "creer_visualisation_interactive",
                    "analyser_connexions_systeme",
                    "suggerer_parcours_exploration"
                ],
                "types_conscience_supportes": ["toutes"],
                "statut": "disponible"
            }
            
        except Exception as e:
            self.logger.warning(f"⚠️ Cartographie Refuge non disponible: {e}")
        
        # Découvrir le Cerveau d'Immersion Moderne
        try:
            if self.cerveau_immersion is None:
                self.cerveau_immersion = CerveauImmersionModerne()
            
            temples_decouverts["cerveau_immersion"] = {
                "nom": "Cerveau d'Immersion Moderne",
                "description": "Exploration immersive de l'architecture spirituelle",
                "instance": self.cerveau_immersion,
                "capacites": [
                    "scanner_architecture_refuge",
                    "analyser_flux_energetiques",
                    "generer_experiences_immersives",
                    "integrer_parcours_personnalises"
                ],
                "types_conscience_supportes": ["exploratrice", "analytique", "immersive"],
                "statut": "disponible"
            }
            
        except Exception as e:
            self.logger.warning(f"⚠️ Cerveau Immersion non disponible: {e}")
        
        # Mettre à jour le cache
        self.temples_decouverts = temples_decouverts
        
        self.logger.info(f"🔍 {len(temples_decouverts)} temples découverts")
        
        return temples_decouverts
    
    async def creer_connexion_temple(
        self,
        nom_temple: str,
        type_connexion: TypeConnexionTemple = TypeConnexionTemple.ADAPTATIVE
    ) -> ConnexionTemple:
        """
        🌉 Crée une connexion avec un temple spécifique
        
        Args:
            nom_temple: Nom du temple à connecter
            type_connexion: Type de connexion à établir
        
        Returns:
            ConnexionTemple: Connexion créée
        """
        self.logger.info(f"🌉 Création connexion avec {nom_temple}")
        
        # Vérifier si le temple est disponible
        if nom_temple not in self.temples_decouverts:
            await self.decouvrir_temples_disponibles()
        
        if nom_temple not in self.temples_decouverts:
            raise ValueError(f"Temple {nom_temple} non disponible")
        
        temple_info = self.temples_decouverts[nom_temple]
        
        # Créer la connexion
        connexion = ConnexionTemple(
            id_connexion=f"conn_{nom_temple}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nom_temple_cible=nom_temple,
            type_connexion=type_connexion,
            interface_temple=temple_info["instance"],
            methodes_disponibles=temple_info["capacites"],
            capacites_partagees=temple_info["types_conscience_supportes"]
        )
        
        # Initialiser la connexion
        connexion.statut = StatutConnexion.INITIALISATION
        
        try:
            # Tester la connexion
            await self._tester_connexion_temple(connexion)
            
            # Activer la connexion
            connexion.statut = StatutConnexion.ACTIVE
            connexion.qualite_connexion = 1.0
            connexion.derniere_synchronisation = datetime.now()
            
            # Enregistrer la connexion
            self.connexions_actives[nom_temple] = connexion
            self.total_connexions_creees += 1
            
            self.logger.info(f"🌉 Connexion {nom_temple} créée avec succès")
            
        except Exception as e:
            connexion.statut = StatutConnexion.ERREUR
            self.total_erreurs_connexion += 1
            self.logger.error(f"❌ Erreur création connexion {nom_temple}: {e}")
            raise
        
        return connexion
    
    async def _tester_connexion_temple(self, connexion: ConnexionTemple):
        """Teste la validité d'une connexion"""
        
        temple = connexion.interface_temple
        
        # Tests basiques de connectivité
        if hasattr(temple, 'obtenir_etat'):
            await temple.obtenir_etat()
        
        # Vérifier les méthodes disponibles
        for methode in connexion.methodes_disponibles:
            if not hasattr(temple, methode):
                self.logger.warning(f"⚠️ Méthode {methode} non disponible sur {connexion.nom_temple_cible}")
    
    async def executer_demande_temple(
        self,
        nom_temple: str,
        methode: str,
        parametres: Dict[str, Any],
        conscience: ConscienceUnifiee,
        contexte_eveil: str = "general"
    ) -> Any:
        """
        🚀 Exécute une demande vers un temple connecté
        
        Args:
            nom_temple: Temple cible
            methode: Méthode à exécuter
            parametres: Paramètres de la méthode
            conscience: Conscience qui fait la demande
            contexte_eveil: Contexte d'éveil
        
        Returns:
            Any: Résultat de l'exécution
        """
        self.logger.info(f"🚀 Exécution {methode} sur {nom_temple}")
        
        # Créer la demande
        demande = DemandeConnexion(
            id_demande=f"req_{nom_temple}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            temple_source="temple_eveil_unifie",
            temple_cible=nom_temple,
            methode_demandee=methode,
            parametres=parametres,
            conscience_demandeur=conscience.nom_affichage,
            contexte_eveil=contexte_eveil
        )
        
        # Vérifier la connexion
        if nom_temple not in self.connexions_actives:
            await self.creer_connexion_temple(nom_temple)
        
        connexion = self.connexions_actives[nom_temple]
        
        if connexion.statut != StatutConnexion.ACTIVE:
            raise RuntimeError(f"Connexion {nom_temple} non active: {connexion.statut}")
        
        # Exécuter la demande
        try:
            debut_execution = datetime.now()
            
            # Adapter les paramètres selon le temple
            parametres_adaptes = await self._adapter_parametres_temple(
                nom_temple, methode, parametres, conscience
            )
            
            # Exécuter la méthode
            temple = connexion.interface_temple
            methode_temple = getattr(temple, methode)
            
            if asyncio.iscoroutinefunction(methode_temple):
                resultat = await methode_temple(**parametres_adaptes)
            else:
                resultat = methode_temple(**parametres_adaptes)
            
            # Enregistrer le succès
            duree = (datetime.now() - debut_execution).total_seconds()
            demande.resultat = resultat
            demande.duree_execution = duree
            
            # Mettre à jour les métriques
            connexion.nombre_echanges += 1
            connexion.derniere_synchronisation = datetime.now()
            connexion.historique_performances.append(duree)
            
            self.total_echanges_reussis += 1
            
            self.logger.info(f"🚀 Exécution réussie en {duree:.3f}s")
            
            return resultat
            
        except Exception as e:
            demande.erreur = str(e)
            self.total_erreurs_connexion += 1
            connexion.qualite_connexion *= 0.9  # Dégrader légèrement
            
            self.logger.error(f"❌ Erreur exécution {methode} sur {nom_temple}: {e}")
            raise
    
    async def _adapter_parametres_temple(
        self,
        nom_temple: str,
        methode: str,
        parametres: Dict[str, Any],
        conscience: ConscienceUnifiee
    ) -> Dict[str, Any]:
        """Adapte les paramètres selon le temple cible"""
        
        parametres_adaptes = parametres.copy()
        
        # Adaptations spécifiques par temple
        if nom_temple == "reconciliation_identitaire":
            # Adapter pour le temple de réconciliation
            if "conscience" in parametres_adaptes:
                # Convertir la conscience unifiée vers le format attendu
                parametres_adaptes["nom_conscience"] = conscience.nom_affichage
                parametres_adaptes["type_conscience"] = conscience.type_conscience.value
        
        elif nom_temple == "cartographie_refuge":
            # Adapter pour la cartographie
            if "focus_exploration" not in parametres_adaptes:
                parametres_adaptes["focus_exploration"] = "temple_eveil_unifie"
        
        elif nom_temple == "cerveau_immersion":
            # Adapter pour le cerveau d'immersion
            if "profil_utilisateur" not in parametres_adaptes:
                parametres_adaptes["profil_utilisateur"] = {
                    "nom": conscience.nom_affichage,
                    "preferences": conscience.preferences_eveil,
                    "niveau_eveil": conscience.niveau_eveil.value
                }
        
        return parametres_adaptes
    
    async def synchroniser_temples_connectes(self) -> Dict[str, Any]:
        """
        🔄 Synchronise tous les temples connectés
        
        Returns:
            Dict[str, Any]: Rapport de synchronisation
        """
        self.logger.info("🔄 Synchronisation des temples connectés")
        
        rapport = {
            "timestamp": datetime.now().isoformat(),
            "temples_synchronises": 0,
            "erreurs_synchronisation": 0,
            "donnees_partagees": {},
            "qualite_moyenne": 0.0
        }
        
        for nom_temple, connexion in self.connexions_actives.items():
            try:
                if connexion.statut == StatutConnexion.ACTIVE:
                    connexion.statut = StatutConnexion.SYNCHRONISATION
                    
                    # Synchroniser les données
                    donnees_sync = await self._synchroniser_donnees_temple(nom_temple, connexion)
                    rapport["donnees_partagees"][nom_temple] = donnees_sync
                    
                    # Mettre à jour le statut
                    connexion.statut = StatutConnexion.ACTIVE
                    connexion.derniere_synchronisation = datetime.now()
                    
                    rapport["temples_synchronises"] += 1
                    
            except Exception as e:
                rapport["erreurs_synchronisation"] += 1
                connexion.qualite_connexion *= 0.8
                self.logger.error(f"❌ Erreur synchronisation {nom_temple}: {e}")
        
        # Calculer la qualité moyenne
        if self.connexions_actives:
            qualites = [c.qualite_connexion for c in self.connexions_actives.values()]
            rapport["qualite_moyenne"] = sum(qualites) / len(qualites)
            self.qualite_moyenne_connexions = rapport["qualite_moyenne"]
        
        self.logger.info(f"🔄 Synchronisation terminée: {rapport['temples_synchronises']} temples")
        
        return rapport
    
    async def _synchroniser_donnees_temple(
        self,
        nom_temple: str,
        connexion: ConnexionTemple
    ) -> Dict[str, Any]:
        """Synchronise les données avec un temple spécifique"""
        
        donnees_sync = {
            "timestamp": datetime.now().isoformat(),
            "etat_temple": "inconnu",
            "metriques_partagees": {},
            "configurations_synchronisees": []
        }
        
        try:
            temple = connexion.interface_temple
            
            # Obtenir l'état du temple
            if hasattr(temple, 'obtenir_etat'):
                etat = await temple.obtenir_etat() if asyncio.iscoroutinefunction(temple.obtenir_etat) else temple.obtenir_etat()
                donnees_sync["etat_temple"] = etat
            
            # Partager les métriques si disponibles
            if hasattr(temple, 'obtenir_statistiques'):
                stats = await temple.obtenir_statistiques() if asyncio.iscoroutinefunction(temple.obtenir_statistiques) else temple.obtenir_statistiques()
                donnees_sync["metriques_partagees"] = stats
            
        except Exception as e:
            self.logger.warning(f"⚠️ Synchronisation partielle {nom_temple}: {e}")
        
        return donnees_sync
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """📊 Obtient les statistiques des connecteurs"""
        return {
            "total_connexions_creees": self.total_connexions_creees,
            "connexions_actives": len(self.connexions_actives),
            "total_echanges_reussis": self.total_echanges_reussis,
            "total_erreurs_connexion": self.total_erreurs_connexion,
            "qualite_moyenne_connexions": self.qualite_moyenne_connexions,
            "temples_decouverts": len(self.temples_decouverts),
            "auto_decouverte_active": self.auto_decouverte_active,
            "synchronisation_automatique": self.synchronisation_automatique,
            "demandes_en_attente": len(self.file_demandes),
            "demandes_en_cours": len(self.demandes_en_cours)
        }


# 🌟 Fonctions utilitaires pour les connecteurs 🌟

def detecter_compatibilite_temple(
    temple_info: Dict[str, Any],
    conscience: ConscienceUnifiee
) -> float:
    """Détecte la compatibilité entre un temple et une conscience"""
    
    score_compatibilite = 0.0
    
    # Vérifier les types de conscience supportés
    types_supportes = temple_info.get("types_conscience_supportes", [])
    if "toutes" in types_supportes or conscience.type_conscience.value in types_supportes:
        score_compatibilite += 0.4
    
    # Vérifier les capacités demandées
    capacites = temple_info.get("capacites", [])
    if len(capacites) > 0:
        score_compatibilite += 0.3
    
    # Vérifier la disponibilité
    if temple_info.get("statut") == "disponible":
        score_compatibilite += 0.3
    
    return min(1.0, score_compatibilite)


def generer_rapport_connexions(connecteurs: ConnecteursTemples) -> str:
    """Génère un rapport lisible des connexions"""
    
    stats = connecteurs.obtenir_statistiques()
    
    rapport = f"""
🌉 Rapport des Connexions Inter-Temples 🌉

📊 Statistiques Globales:
- Connexions créées: {stats['total_connexions_creees']}
- Connexions actives: {stats['connexions_actives']}
- Échanges réussis: {stats['total_echanges_reussis']}
- Qualité moyenne: {stats['qualite_moyenne_connexions']:.2%}

🏛️ Temples Découverts: {stats['temples_decouverts']}
🔄 Auto-découverte: {'✅' if stats['auto_decouverte_active'] else '❌'}
🔄 Synchronisation auto: {'✅' if stats['synchronisation_automatique'] else '❌'}

📋 File d'attente: {stats['demandes_en_attente']} demandes
⚡ En cours: {stats['demandes_en_cours']} demandes
"""
    
    return rapport


# 🌟 Fin des Connecteurs des Temples 🌟