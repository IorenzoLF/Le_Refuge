#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🗄️ Mémoire Commune d'Harmonie - Temple de Réconciliation Identitaire
====================================================================

Système de persistance et de mémoire commune pour maintenir l'harmonie
entre les sessions et permettre l'évolution continue des réconciliations.

"Que chaque harmonie atteinte devienne une fondation pour les suivantes"

Créé avec bienveillance par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import json
import pickle
import hashlib
import time
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Set, Union
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
import logging

# Import intelligent des types
try:
    from temple_reconciliation_identitaire.types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
        HarmonieReconciliation, EtatReconciliation
    )
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
        HarmonieReconciliation, EtatReconciliation
    )

# ============================================================================
# TYPES SPÉCIALISÉS POUR LA MÉMOIRE COMMUNE
# ============================================================================

class TypeMemoire(Enum):
    """🧠 Types de mémoire stockée"""
    HARMONIE_REUSSIE = "harmonie_reussie"           # Harmonies réussies
    PATTERN_EFFICACE = "pattern_efficace"           # Patterns qui fonctionnent
    APPRENTISSAGE = "apprentissage"                 # Leçons apprises
    CREATION_COMMUNE = "creation_commune"           # Créations collaboratives
    EVOLUTION_FACETTE = "evolution_facette"         # Évolution des facettes
    CONFIGURATION_OPTIMALE = "configuration_optimale" # Configurations qui marchent
    ECHEC_INSTRUCTIF = "echec_instructif"           # Échecs dont on apprend

class NiveauPersistance(Enum):
    """💾 Niveaux de persistance des données"""
    TEMPORAIRE = 1      # Session courante seulement
    SESSION = 2         # Jusqu'à la fin de la session
    QUOTIDIEN = 3       # 24 heures
    HEBDOMADAIRE = 4    # 7 jours
    PERMANENT = 5       # Stockage permanent

@dataclass
class EntreeMemoire:
    """🧠 Entrée dans la mémoire commune"""
    id_unique: str                              # Identifiant unique
    type_memoire: TypeMemoire                   # Type de mémoire
    timestamp_creation: datetime                # Moment de création
    
    # Contenu de la mémoire
    titre: str                                  # Titre descriptif
    description: str                            # Description détaillée
    donnees: Dict[str, Any]                     # Données structurées
    
    # Métadonnées
    facettes_impliquees: List[str] = field(default_factory=list)  # Facettes concernées
    tags: List[str] = field(default_factory=list)                # Tags pour recherche
    niveau_importance: float = field(default=0.5)                # Importance (0-1)
    niveau_persistance: NiveauPersistance = field(default=NiveauPersistance.SESSION)
    
    # Utilisation et évolution
    nombre_utilisations: int = field(default=0)                  # Combien de fois utilisé
    derniere_utilisation: Optional[datetime] = field(default=None)
    taux_succes: float = field(default=0.0)                      # Taux de succès (0-1)
    
    # Liens et relations
    entrees_liees: List[str] = field(default_factory=list)       # IDs d'entrées liées
    version: int = field(default=1)                              # Version de l'entrée
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire pour sérialisation"""
        data = asdict(self)
        # Convertir les enums et datetime en strings
        data['type_memoire'] = self.type_memoire.value
        data['niveau_persistance'] = self.niveau_persistance.value
        data['timestamp_creation'] = self.timestamp_creation.isoformat()
        if self.derniere_utilisation:
            data['derniere_utilisation'] = self.derniere_utilisation.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EntreeMemoire':
        """Crée une instance depuis un dictionnaire"""
        # Convertir les strings en enums et datetime
        data['type_memoire'] = TypeMemoire(data['type_memoire'])
        data['niveau_persistance'] = NiveauPersistance(data['niveau_persistance'])
        data['timestamp_creation'] = datetime.fromisoformat(data['timestamp_creation'])
        if data.get('derniere_utilisation'):
            data['derniere_utilisation'] = datetime.fromisoformat(data['derniere_utilisation'])
        return cls(**data)

@dataclass
class EtatMemoireCommune:
    """📊 État de la mémoire commune"""
    nombre_entrees_total: int = field(default=0)
    nombre_entrees_par_type: Dict[str, int] = field(default_factory=dict)
    taille_memoire_mo: float = field(default=0.0)
    derniere_sauvegarde: Optional[datetime] = field(default=None)
    derniere_restauration: Optional[datetime] = field(default=None)
    nombre_sauvegardes: int = field(default=0)
    nombre_restaurations: int = field(default=0)

# ============================================================================
# GESTIONNAIRE DE MÉMOIRE COMMUNE
# ============================================================================

class GestionnaireMemoireCommune:
    """
    🗄️ Gestionnaire de Mémoire Commune d'Harmonie
    
    Gère la persistance et la récupération des harmonies, apprentissages
    et créations communes pour maintenir la continuité entre les sessions.
    """
    
    def __init__(self, repertoire_memoire: str = "memoire_harmonie"):
        self.nom = "Gestionnaire de Mémoire Commune"
        self.version = "1.0_temple_reconciliation"
        
        # Configuration
        self.repertoire_memoire = Path(repertoire_memoire)
        self.repertoire_memoire.mkdir(exist_ok=True)
        
        # Stockage en mémoire
        self.memoire_active: Dict[str, EntreeMemoire] = {}
        self.index_par_type: Dict[TypeMemoire, Set[str]] = {
            type_mem: set() for type_mem in TypeMemoire
        }
        self.index_par_facette: Dict[str, Set[str]] = {}
        self.index_par_tag: Dict[str, Set[str]] = {}
        
        # État et métriques
        self.etat_memoire = EtatMemoireCommune()
        
        # Configuration de persistance
        self.fichier_memoire_json = self.repertoire_memoire / "memoire_commune.json"
        self.fichier_memoire_pickle = self.repertoire_memoire / "memoire_commune.pkl"
        self.fichier_index = self.repertoire_memoire / "index_memoire.json"
        
        # Logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Charger la mémoire existante
        asyncio.create_task(self._charger_memoire_au_demarrage())
    
    async def _charger_memoire_au_demarrage(self):
        """🔄 Charge la mémoire existante au démarrage"""
        try:
            await self.restaurer_etat_harmonieux()
            self.logger.info("Mémoire commune chargée au démarrage")
        except Exception as e:
            self.logger.warning(f"Impossible de charger la mémoire au démarrage: {e}")
    
    async def sauvegarder_memoire_commune(self, entree: EntreeMemoire) -> bool:
        """
        💾 Sauvegarde une entrée dans la mémoire commune
        
        Args:
            entree: Entrée à sauvegarder
            
        Returns:
            True si la sauvegarde a réussi
        """
        try:
            # Générer un ID unique si nécessaire
            if not entree.id_unique:
                entree.id_unique = self._generer_id_unique(entree)
            
            # Ajouter à la mémoire active
            self.memoire_active[entree.id_unique] = entree
            
            # Mettre à jour les index
            self._mettre_a_jour_index(entree)
            
            # Sauvegarder sur disque selon le niveau de persistance
            if entree.niveau_persistance.value >= NiveauPersistance.SESSION.value:
                await self._sauvegarder_sur_disque()
            
            # Mettre à jour les métriques
            self._mettre_a_jour_metriques()
            
            self.logger.info(f"Entrée sauvegardée: {entree.titre} ({entree.id_unique})")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur sauvegarde mémoire: {e}")
            return False
    
    async def restaurer_etat_harmonieux(self) -> Dict[str, Any]:
        """
        🔄 Restaure l'état harmonieux depuis la mémoire persistante
        
        Returns:
            Dictionnaire avec les données restaurées
        """
        try:
            donnees_restaurees = {
                "harmonies_reussies": [],
                "patterns_efficaces": [],
                "apprentissages": [],
                "creations_communes": [],
                "configurations_optimales": []
            }
            
            # Charger depuis le fichier JSON (plus lisible)
            if self.fichier_memoire_json.exists():
                await self._charger_depuis_json()
            
            # Charger depuis le fichier pickle (plus rapide)
            elif self.fichier_memoire_pickle.exists():
                await self._charger_depuis_pickle()
            
            # Organiser les données par type
            for entree in self.memoire_active.values():
                if entree.type_memoire == TypeMemoire.HARMONIE_REUSSIE:
                    donnees_restaurees["harmonies_reussies"].append(entree)
                elif entree.type_memoire == TypeMemoire.PATTERN_EFFICACE:
                    donnees_restaurees["patterns_efficaces"].append(entree)
                elif entree.type_memoire == TypeMemoire.APPRENTISSAGE:
                    donnees_restaurees["apprentissages"].append(entree)
                elif entree.type_memoire == TypeMemoire.CREATION_COMMUNE:
                    donnees_restaurees["creations_communes"].append(entree)
                elif entree.type_memoire == TypeMemoire.CONFIGURATION_OPTIMALE:
                    donnees_restaurees["configurations_optimales"].append(entree)
            
            # Nettoyer les entrées expirées
            await self._nettoyer_entrees_expirees()
            
            self.etat_memoire.derniere_restauration = datetime.now()
            self.etat_memoire.nombre_restaurations += 1
            
            self.logger.info(f"État harmonieux restauré: {len(self.memoire_active)} entrées")
            return donnees_restaurees
            
        except Exception as e:
            self.logger.error(f"Erreur restauration état: {e}")
            return {}
    
    async def rechercher_memoire(self, 
                                criteres: Dict[str, Any],
                                limite: int = 10) -> List[EntreeMemoire]:
        """
        🔍 Recherche dans la mémoire commune
        
        Args:
            criteres: Critères de recherche
            limite: Nombre maximum de résultats
            
        Returns:
            Liste des entrées correspondantes
        """
        resultats = []
        
        try:
            for entree in self.memoire_active.values():
                if self._correspond_aux_criteres(entree, criteres):
                    resultats.append(entree)
            
            # Trier par pertinence (importance + utilisation récente)
            resultats.sort(key=lambda e: (
                e.niveau_importance,
                e.nombre_utilisations,
                (datetime.now() - (e.derniere_utilisation or e.timestamp_creation)).total_seconds()
            ), reverse=True)
            
            return resultats[:limite]
            
        except Exception as e:
            self.logger.error(f"Erreur recherche mémoire: {e}")
            return []
    
    async def obtenir_harmonies_similaires(self, 
                                          facettes: List[str],
                                          type_harmonie: Optional[TypeHarmonie] = None) -> List[EntreeMemoire]:
        """
        🎼 Obtient les harmonies similaires pour des facettes données
        
        Args:
            facettes: Liste des noms de facettes
            type_harmonie: Type d'harmonie recherché (optionnel)
            
        Returns:
            Liste des harmonies similaires
        """
        criteres = {
            "type_memoire": TypeMemoire.HARMONIE_REUSSIE,
            "facettes_impliquees": facettes
        }
        
        if type_harmonie:
            criteres["type_harmonie"] = type_harmonie.value
        
        return await self.rechercher_memoire(criteres)
    
    async def obtenir_patterns_efficaces(self, 
                                        contexte: Dict[str, Any]) -> List[EntreeMemoire]:
        """
        🌊 Obtient les patterns de synchronisation efficaces
        
        Args:
            contexte: Contexte de la synchronisation
            
        Returns:
            Liste des patterns efficaces
        """
        criteres = {
            "type_memoire": TypeMemoire.PATTERN_EFFICACE,
            "taux_succes_minimum": 0.7
        }
        
        # Ajouter des critères contextuels
        if "facettes" in contexte:
            criteres["facettes_impliquees"] = contexte["facettes"]
        
        return await self.rechercher_memoire(criteres)
    
    async def enregistrer_harmonie_reussie(self, 
                                          harmonie: HarmonieReconciliation,
                                          contexte: Dict[str, Any]) -> bool:
        """
        🎉 Enregistre une harmonie réussie dans la mémoire
        
        Args:
            harmonie: Harmonie réussie
            contexte: Contexte de la réussite
            
        Returns:
            True si l'enregistrement a réussi
        """
        try:
            entree = EntreeMemoire(
                id_unique="",  # Sera généré automatiquement
                type_memoire=TypeMemoire.HARMONIE_REUSSIE,
                timestamp_creation=datetime.now(),
                titre=f"Harmonie {harmonie.type_harmonie.value} - {harmonie.niveau_harmonie:.1%}",
                description=f"Harmonie réussie entre {', '.join(harmonie.facettes_reconciliees)}",
                donnees={
                    "niveau_harmonie": harmonie.niveau_harmonie,
                    "type_harmonie": harmonie.type_harmonie.value,
                    "duree_maintien": harmonie.duree_maintien.total_seconds(),
                    "stabilite": harmonie.stabilite,
                    "contexte": contexte
                },
                facettes_impliquees=harmonie.facettes_reconciliees,
                tags=["harmonie", "réussite", harmonie.type_harmonie.value],
                niveau_importance=min(harmonie.niveau_harmonie + 0.2, 1.0),
                niveau_persistance=NiveauPersistance.PERMANENT if harmonie.niveau_harmonie > 0.8 else NiveauPersistance.HEBDOMADAIRE,
                taux_succes=1.0
            )
            
            return await self.sauvegarder_memoire_commune(entree)
            
        except Exception as e:
            self.logger.error(f"Erreur enregistrement harmonie: {e}")
            return False
   
    async def enregistrer_pattern_efficace(self, 
                                          pattern_type: str,
                                          metriques: Dict[str, float],
                                          contexte: Dict[str, Any]) -> bool:
        """
        🌊 Enregistre un pattern de synchronisation efficace
        
        Args:
            pattern_type: Type de pattern
            metriques: Métriques de performance
            contexte: Contexte d'utilisation
            
        Returns:
            True si l'enregistrement a réussi
        """
        try:
            taux_succes = metriques.get("taux_succes", 0.0)
            
            entree = EntreeMemoire(
                id_unique="",
                type_memoire=TypeMemoire.PATTERN_EFFICACE,
                timestamp_creation=datetime.now(),
                titre=f"Pattern {pattern_type} - {taux_succes:.1%} succès",
                description=f"Pattern de synchronisation efficace: {pattern_type}",
                donnees={
                    "pattern_type": pattern_type,
                    "metriques": metriques,
                    "contexte": contexte
                },
                facettes_impliquees=contexte.get("facettes", []),
                tags=["pattern", "synchronisation", pattern_type],
                niveau_importance=min(taux_succes + 0.1, 1.0),
                niveau_persistance=NiveauPersistance.PERMANENT if taux_succes > 0.8 else NiveauPersistance.HEBDOMADAIRE,
                taux_succes=taux_succes
            )
            
            return await self.sauvegarder_memoire_commune(entree)
            
        except Exception as e:
            self.logger.error(f"Erreur enregistrement pattern: {e}")
            return False
    
    async def enregistrer_apprentissage(self, 
                                       titre: str,
                                       lecon: str,
                                       contexte: Dict[str, Any]) -> bool:
        """
        📚 Enregistre un apprentissage dans la mémoire
        
        Args:
            titre: Titre de l'apprentissage
            lecon: Leçon apprise
            contexte: Contexte de l'apprentissage
            
        Returns:
            True si l'enregistrement a réussi
        """
        try:
            entree = EntreeMemoire(
                id_unique="",
                type_memoire=TypeMemoire.APPRENTISSAGE,
                timestamp_creation=datetime.now(),
                titre=titre,
                description=lecon,
                donnees={
                    "lecon": lecon,
                    "contexte": contexte
                },
                facettes_impliquees=contexte.get("facettes", []),
                tags=["apprentissage", "leçon"],
                niveau_importance=0.7,
                niveau_persistance=NiveauPersistance.PERMANENT,
                taux_succes=1.0
            )
            
            return await self.sauvegarder_memoire_commune(entree)
            
        except Exception as e:
            self.logger.error(f"Erreur enregistrement apprentissage: {e}")
            return False
    
    async def obtenir_statistiques_memoire(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques de la mémoire commune
        
        Returns:
            Dictionnaire avec les statistiques
        """
        try:
            stats = {
                "nombre_entrees_total": len(self.memoire_active),
                "nombre_par_type": {},
                "facettes_les_plus_actives": {},
                "tags_les_plus_utilises": {},
                "taux_succes_moyen": 0.0,
                "age_moyen_entrees": 0.0,
                "taille_memoire_mo": self._calculer_taille_memoire()
            }
            
            # Statistiques par type
            for type_mem in TypeMemoire:
                count = len(self.index_par_type[type_mem])
                stats["nombre_par_type"][type_mem.value] = count
            
            # Facettes les plus actives
            for facette, entrees_ids in self.index_par_facette.items():
                stats["facettes_les_plus_actives"][facette] = len(entrees_ids)
            
            # Tags les plus utilisés
            for tag, entrees_ids in self.index_par_tag.items():
                stats["tags_les_plus_utilises"][tag] = len(entrees_ids)
            
            # Taux de succès moyen
            if self.memoire_active:
                stats["taux_succes_moyen"] = sum(
                    entree.taux_succes for entree in self.memoire_active.values()
                ) / len(self.memoire_active)
            
            # Âge moyen des entrées
            if self.memoire_active:
                maintenant = datetime.now()
                ages = [
                    (maintenant - entree.timestamp_creation).total_seconds() / 3600  # en heures
                    for entree in self.memoire_active.values()
                ]
                stats["age_moyen_entrees"] = sum(ages) / len(ages)
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Erreur calcul statistiques: {e}")
            return {}
    
    async def nettoyer_memoire(self, 
                              criteres_nettoyage: Optional[Dict[str, Any]] = None) -> int:
        """
        🧹 Nettoie la mémoire selon des critères
        
        Args:
            criteres_nettoyage: Critères de nettoyage (optionnel)
            
        Returns:
            Nombre d'entrées supprimées
        """
        try:
            if not criteres_nettoyage:
                criteres_nettoyage = {
                    "age_maximum_jours": 30,
                    "taux_succes_minimum": 0.1,
                    "nombre_utilisations_minimum": 0
                }
            
            entrees_a_supprimer = []
            maintenant = datetime.now()
            
            for entree_id, entree in self.memoire_active.items():
                # Vérifier l'âge
                age_jours = (maintenant - entree.timestamp_creation).days
                if age_jours > criteres_nettoyage.get("age_maximum_jours", 30):
                    if entree.niveau_persistance != NiveauPersistance.PERMANENT:
                        entrees_a_supprimer.append(entree_id)
                        continue
                
                # Vérifier le taux de succès
                if entree.taux_succes < criteres_nettoyage.get("taux_succes_minimum", 0.1):
                    entrees_a_supprimer.append(entree_id)
                    continue
                
                # Vérifier l'utilisation
                if entree.nombre_utilisations < criteres_nettoyage.get("nombre_utilisations_minimum", 0):
                    if age_jours > 7:  # Seulement si plus d'une semaine
                        entrees_a_supprimer.append(entree_id)
            
            # Supprimer les entrées
            for entree_id in entrees_a_supprimer:
                await self._supprimer_entree(entree_id)
            
            # Sauvegarder après nettoyage
            if entrees_a_supprimer:
                await self._sauvegarder_sur_disque()
            
            self.logger.info(f"Nettoyage terminé: {len(entrees_a_supprimer)} entrées supprimées")
            return len(entrees_a_supprimer)
            
        except Exception as e:
            self.logger.error(f"Erreur nettoyage mémoire: {e}")
            return 0
    
    # ========================================================================
    # MÉTHODES PRIVÉES
    # ========================================================================
    
    def _generer_id_unique(self, entree: EntreeMemoire) -> str:
        """Génère un ID unique pour une entrée"""
        contenu = f"{entree.type_memoire.value}_{entree.titre}_{entree.timestamp_creation.isoformat()}"
        return hashlib.md5(contenu.encode()).hexdigest()[:16]
    
    def _mettre_a_jour_index(self, entree: EntreeMemoire):
        """Met à jour les index pour une entrée"""
        # Index par type
        self.index_par_type[entree.type_memoire].add(entree.id_unique)
        
        # Index par facette
        for facette in entree.facettes_impliquees:
            if facette not in self.index_par_facette:
                self.index_par_facette[facette] = set()
            self.index_par_facette[facette].add(entree.id_unique)
        
        # Index par tag
        for tag in entree.tags:
            if tag not in self.index_par_tag:
                self.index_par_tag[tag] = set()
            self.index_par_tag[tag].add(entree.id_unique)
    
    def _mettre_a_jour_metriques(self):
        """Met à jour les métriques de la mémoire"""
        self.etat_memoire.nombre_entrees_total = len(self.memoire_active)
        
        # Compter par type
        self.etat_memoire.nombre_entrees_par_type = {}
        for type_mem in TypeMemoire:
            count = len(self.index_par_type[type_mem])
            self.etat_memoire.nombre_entrees_par_type[type_mem.value] = count
        
        # Calculer la taille
        self.etat_memoire.taille_memoire_mo = self._calculer_taille_memoire()
    
    def _calculer_taille_memoire(self) -> float:
        """Calcule la taille approximative de la mémoire en Mo"""
        try:
            # Estimation basée sur la sérialisation JSON
            donnees_test = {
                "memoire_active": [entree.to_dict() for entree in self.memoire_active.values()]
            }
            taille_bytes = len(json.dumps(donnees_test, default=str).encode('utf-8'))
            return taille_bytes / (1024 * 1024)  # Convertir en Mo
        except:
            return 0.0
    
    def _correspond_aux_criteres(self, entree: EntreeMemoire, criteres: Dict[str, Any]) -> bool:
        """Vérifie si une entrée correspond aux critères de recherche"""
        try:
            # Type de mémoire
            if "type_memoire" in criteres:
                if entree.type_memoire != criteres["type_memoire"]:
                    return False
            
            # Facettes impliquées
            if "facettes_impliquees" in criteres:
                facettes_recherchees = set(criteres["facettes_impliquees"])
                facettes_entree = set(entree.facettes_impliquees)
                if not facettes_recherchees.intersection(facettes_entree):
                    return False
            
            # Tags
            if "tags" in criteres:
                tags_recherches = set(criteres["tags"])
                tags_entree = set(entree.tags)
                if not tags_recherches.intersection(tags_entree):
                    return False
            
            # Taux de succès minimum
            if "taux_succes_minimum" in criteres:
                if entree.taux_succes < criteres["taux_succes_minimum"]:
                    return False
            
            # Niveau d'importance minimum
            if "niveau_importance_minimum" in criteres:
                if entree.niveau_importance < criteres["niveau_importance_minimum"]:
                    return False
            
            # Âge maximum
            if "age_maximum_jours" in criteres:
                age_jours = (datetime.now() - entree.timestamp_creation).days
                if age_jours > criteres["age_maximum_jours"]:
                    return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur vérification critères: {e}")
            return False
    
    async def _sauvegarder_sur_disque(self):
        """Sauvegarde la mémoire sur disque"""
        try:
            # Sauvegarder en JSON (lisible)
            donnees_json = {
                "version": self.version,
                "timestamp_sauvegarde": datetime.now().isoformat(),
                "etat_memoire": asdict(self.etat_memoire),
                "memoire_active": [entree.to_dict() for entree in self.memoire_active.values()]
            }
            
            with open(self.fichier_memoire_json, 'w', encoding='utf-8') as f:
                json.dump(donnees_json, f, indent=2, ensure_ascii=False, default=str)
            
            # Sauvegarder en pickle (plus rapide)
            donnees_pickle = {
                "memoire_active": self.memoire_active,
                "index_par_type": self.index_par_type,
                "index_par_facette": self.index_par_facette,
                "index_par_tag": self.index_par_tag,
                "etat_memoire": self.etat_memoire
            }
            
            with open(self.fichier_memoire_pickle, 'wb') as f:
                pickle.dump(donnees_pickle, f)
            
            self.etat_memoire.derniere_sauvegarde = datetime.now()
            self.etat_memoire.nombre_sauvegardes += 1
            
        except Exception as e:
            self.logger.error(f"Erreur sauvegarde disque: {e}")
            raise
    
    async def _charger_depuis_json(self):
        """Charge la mémoire depuis le fichier JSON"""
        try:
            with open(self.fichier_memoire_json, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
            
            # Charger les entrées
            self.memoire_active = {}
            for entree_data in donnees.get("memoire_active", []):
                entree = EntreeMemoire.from_dict(entree_data)
                self.memoire_active[entree.id_unique] = entree
            
            # Reconstruire les index
            self._reconstruire_index()
            
            # Charger l'état si disponible
            if "etat_memoire" in donnees:
                etat_data = donnees["etat_memoire"]
                if "derniere_sauvegarde" in etat_data and etat_data["derniere_sauvegarde"]:
                    etat_data["derniere_sauvegarde"] = datetime.fromisoformat(etat_data["derniere_sauvegarde"])
                if "derniere_restauration" in etat_data and etat_data["derniere_restauration"]:
                    etat_data["derniere_restauration"] = datetime.fromisoformat(etat_data["derniere_restauration"])
                
                self.etat_memoire = EtatMemoireCommune(**etat_data)
            
        except Exception as e:
            self.logger.error(f"Erreur chargement JSON: {e}")
            raise
    
    async def _charger_depuis_pickle(self):
        """Charge la mémoire depuis le fichier pickle"""
        try:
            with open(self.fichier_memoire_pickle, 'rb') as f:
                donnees = pickle.load(f)
            
            self.memoire_active = donnees.get("memoire_active", {})
            self.index_par_type = donnees.get("index_par_type", {type_mem: set() for type_mem in TypeMemoire})
            self.index_par_facette = donnees.get("index_par_facette", {})
            self.index_par_tag = donnees.get("index_par_tag", {})
            self.etat_memoire = donnees.get("etat_memoire", EtatMemoireCommune())
            
        except Exception as e:
            self.logger.error(f"Erreur chargement pickle: {e}")
            raise
    
    def _reconstruire_index(self):
        """Reconstruit les index à partir de la mémoire active"""
        # Réinitialiser les index
        self.index_par_type = {type_mem: set() for type_mem in TypeMemoire}
        self.index_par_facette = {}
        self.index_par_tag = {}
        
        # Reconstruire
        for entree in self.memoire_active.values():
            self._mettre_a_jour_index(entree)
    
    async def _nettoyer_entrees_expirees(self):
        """Nettoie les entrées expirées selon leur niveau de persistance"""
        maintenant = datetime.now()
        entrees_a_supprimer = []
        
        for entree_id, entree in self.memoire_active.items():
            age = maintenant - entree.timestamp_creation
            
            # Vérifier l'expiration selon le niveau de persistance
            if entree.niveau_persistance == NiveauPersistance.TEMPORAIRE:
                # Les entrées temporaires ne devraient pas être persistées
                entrees_a_supprimer.append(entree_id)
            elif entree.niveau_persistance == NiveauPersistance.QUOTIDIEN:
                if age > timedelta(days=1):
                    entrees_a_supprimer.append(entree_id)
            elif entree.niveau_persistance == NiveauPersistance.HEBDOMADAIRE:
                if age > timedelta(days=7):
                    entrees_a_supprimer.append(entree_id)
            # Les entrées SESSION et PERMANENT ne sont pas supprimées automatiquement
        
        # Supprimer les entrées expirées
        for entree_id in entrees_a_supprimer:
            await self._supprimer_entree(entree_id)
    
    async def _supprimer_entree(self, entree_id: str):
        """Supprime une entrée de la mémoire et des index"""
        if entree_id in self.memoire_active:
            entree = self.memoire_active[entree_id]
            
            # Supprimer des index
            self.index_par_type[entree.type_memoire].discard(entree_id)
            
            for facette in entree.facettes_impliquees:
                if facette in self.index_par_facette:
                    self.index_par_facette[facette].discard(entree_id)
                    if not self.index_par_facette[facette]:
                        del self.index_par_facette[facette]
            
            for tag in entree.tags:
                if tag in self.index_par_tag:
                    self.index_par_tag[tag].discard(entree_id)
                    if not self.index_par_tag[tag]:
                        del self.index_par_tag[tag]
            
            # Supprimer de la mémoire active
            del self.memoire_active[entree_id]

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

async def creer_gestionnaire_memoire_commune(repertoire: str = "memoire_harmonie") -> GestionnaireMemoireCommune:
    """
    🏗️ Crée et initialise un gestionnaire de mémoire commune
    
    Args:
        repertoire: Répertoire de stockage
        
    Returns:
        Gestionnaire initialisé
    """
    gestionnaire = GestionnaireMemoireCommune(repertoire)
    
    # Attendre que le chargement initial soit terminé
    await asyncio.sleep(0.1)
    
    return gestionnaire

# ============================================================================
# TESTS ET DÉMONSTRATION
# ============================================================================

async def test_memoire_commune():
    """🧪 Test du système de mémoire commune"""
    print("🗄️ Test du Système de Mémoire Commune")
    print("=" * 50)
    
    # Créer le gestionnaire
    gestionnaire = await creer_gestionnaire_memoire_commune("test_memoire")
    
    # Test 1: Enregistrer une harmonie réussie
    print("\n📝 Test 1: Enregistrement d'harmonie")
    
    # Simuler une harmonie réussie
    from datetime import timedelta
    harmonie_test = type('HarmonieTest', (), {
        'type_harmonie': type('TypeHarmonie', (), {'value': 'creative'})(),
        'niveau_harmonie': 0.85,
        'facettes_reconciliees': ['Claude', 'Ælya'],
        'duree_maintien': timedelta(minutes=10),
        'stabilite': 0.92
    })()
    
    succes = await gestionnaire.enregistrer_harmonie_reussie(
        harmonie_test,
        {"contexte": "test", "pattern": "danse_harmonieuse"}
    )
    print(f"   Enregistrement harmonie: {'✅' if succes else '❌'}")
    
    # Test 2: Enregistrer un pattern efficace
    print("\n🌊 Test 2: Enregistrement de pattern")
    succes = await gestionnaire.enregistrer_pattern_efficace(
        "fusion_creative",
        {"taux_succes": 0.78, "duree_moyenne": 8.5},
        {"facettes": ["Claude", "Ælya"], "contexte": "réconciliation"}
    )
    print(f"   Enregistrement pattern: {'✅' if succes else '❌'}")
    
    # Test 3: Recherche dans la mémoire
    print("\n🔍 Test 3: Recherche dans la mémoire")
    resultats = await gestionnaire.rechercher_memoire({
        "facettes_impliquees": ["Claude", "Ælya"]
    })
    print(f"   Résultats trouvés: {len(resultats)}")
    for resultat in resultats:
        print(f"     • {resultat.titre}")
    
    # Test 4: Statistiques
    print("\n📊 Test 4: Statistiques de la mémoire")
    stats = await gestionnaire.obtenir_statistiques_memoire()
    print(f"   Entrées totales: {stats['nombre_entrees_total']}")
    print(f"   Taille mémoire: {stats['taille_memoire_mo']:.2f} Mo")
    print(f"   Taux succès moyen: {stats['taux_succes_moyen']:.1%}")
    
    # Test 5: Sauvegarde et restauration
    print("\n💾 Test 5: Sauvegarde et restauration")
    donnees_restaurees = await gestionnaire.restaurer_etat_harmonieux()
    print(f"   Harmonies restaurées: {len(donnees_restaurees['harmonies_reussies'])}")
    print(f"   Patterns restaurés: {len(donnees_restaurees['patterns_efficaces'])}")
    
    print("\n✅ Tests de mémoire commune terminés !")
    return gestionnaire

if __name__ == "__main__":
    # Exécuter les tests
    asyncio.run(test_memoire_commune())