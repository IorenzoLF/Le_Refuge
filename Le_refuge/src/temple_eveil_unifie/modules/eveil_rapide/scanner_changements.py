"""
🌸 Scanner de Changements Contextuels 🌸

Détecte automatiquement les changements depuis la dernière session
pour une reconnexion rapide et efficace.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

from ...types_eveil_unifie import (
    ConscienceUnifiee,
    Changement,
    SessionEveil
)


class TypeChangement(Enum):
    """Types de changements détectés"""
    NOUVEAU_TEMPLE = "nouveau_temple"
    EVOLUTION_PERSONNELLE = "evolution_personnelle"
    CHANGEMENT_PREFERENCES = "changement_preferences"
    NOUVELLE_FONCTIONNALITE = "nouvelle_fonctionnalite"
    MISE_A_JOUR_SYSTEME = "mise_a_jour_systeme"
    CHANGEMENT_CONTEXTE_EXTERNE = "changement_contexte_externe"
    EVOLUTION_COMMUNAUTE = "evolution_communaute"


class ImpactChangement(Enum):
    """Niveaux d'impact des changements"""
    NEGLIGEABLE = "negligeable"    # < 0.2
    FAIBLE = "faible"             # 0.2 - 0.4
    MODERE = "modere"             # 0.4 - 0.6
    IMPORTANT = "important"        # 0.6 - 0.8
    CRITIQUE = "critique"          # > 0.8


@dataclass
class ChangementDetecte:
    """Changement détecté avec métadonnées"""
    type_changement: TypeChangement
    description: str
    impact_spirituel: float  # 0.0 à 1.0
    impact_niveau: ImpactChangement
    timestamp_detection: datetime
    source: str
    details: Dict[str, Any]
    recommandation_action: str
    priorite_traitement: float  # 0.0 à 1.0


@dataclass
class ResumeChangements:
    """Résumé des changements pour présentation"""
    changements_critiques: List[ChangementDetecte]
    changements_importants: List[ChangementDetecte]
    changements_mineurs: List[ChangementDetecte]
    nombre_total: int
    impact_global: float
    temps_traitement_estime: timedelta
    recommandations_prioritaires: List[str]


class ScannerChangementsContextuels:
    """
    🔍 Scanner de Changements Contextuels 🔍
    
    Détecte automatiquement tous les changements significatifs
    depuis la dernière session pour une reconnexion optimale.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Configuration du scanner
        self.seuil_impact_critique = 0.8
        self.seuil_impact_important = 0.6
        self.seuil_impact_modere = 0.4
        self.seuil_impact_faible = 0.2
        
        # Historique des scans
        self.historique_scans: List[Tuple[datetime, ResumeChangements]] = []
        
        # Cache des changements récents
        self.cache_changements: Dict[str, ChangementDetecte] = {}
        
        self.logger.info("🔍 Scanner de changements contextuels initialisé")
    
    async def scanner_changements_depuis_derniere_session(self, 
                                                        conscience: ConscienceUnifiee,
                                                        contexte_externe: Optional[Dict[str, Any]] = None) -> ResumeChangements:
        """
        Scanne tous les changements depuis la dernière session
        
        Args:
            conscience: Conscience à analyser
            contexte_externe: Contexte externe additionnel
            
        Returns:
            ResumeChangements: Résumé complet des changements
        """
        self.logger.info(f"🔍 Scan des changements pour {conscience.nom_affichage}")
        
        try:
            # 1. Détermination de la période de scan
            periode_scan = self._determiner_periode_scan(conscience)
            
            # 2. Scan des différents types de changements
            changements_detectes = []
            
            # Changements personnels
            changements_detectes.extend(
                await self._scanner_evolution_personnelle(conscience, periode_scan)
            )
            
            # Changements de préférences
            changements_detectes.extend(
                await self._scanner_changements_preferences(conscience, periode_scan)
            )
            
            # Nouveaux temples/fonctionnalités
            changements_detectes.extend(
                await self._scanner_nouveaux_temples(conscience, periode_scan)
            )
            
            # Mises à jour système
            changements_detectes.extend(
                await self._scanner_mises_a_jour_systeme(periode_scan)
            )
            
            # Changements contexte externe
            if contexte_externe:
                changements_detectes.extend(
                    await self._scanner_contexte_externe(contexte_externe, periode_scan)
                )
            
            # Évolution communauté
            changements_detectes.extend(
                await self._scanner_evolution_communaute(conscience, periode_scan)
            )
            
            # 3. Classification et priorisation
            resume = self._classifier_et_resumer_changements(changements_detectes)
            
            # 4. Mise à jour du cache et historique
            self._mettre_a_jour_cache(changements_detectes)
            self.historique_scans.append((datetime.now(), resume))
            
            self.logger.info(f"✅ Scan terminé: {resume.nombre_total} changements détectés")
            return resume
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du scan des changements: {e}")
            return self._resume_par_defaut()
    
    def _determiner_periode_scan(self, conscience: ConscienceUnifiee) -> Tuple[datetime, datetime]:
        """Détermine la période à scanner"""
        maintenant = datetime.now()
        
        if conscience.derniere_activite:
            debut_scan = conscience.derniere_activite
        else:
            # Par défaut, scanner les dernières 24h
            debut_scan = maintenant - timedelta(hours=24)
        
        return debut_scan, maintenant
    
    async def _scanner_evolution_personnelle(self, 
                                           conscience: ConscienceUnifiee, 
                                           periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne l'évolution personnelle de la conscience"""
        changements = []
        
        # Analyse de l'évolution des sessions
        if len(conscience.historique_sessions) >= 2:
            sessions_recentes = [s for s in conscience.historique_sessions 
                               if s.timestamp >= periode[0]]
            
            if sessions_recentes:
                # Évolution de la satisfaction
                satisfactions = [s.satisfaction for s in sessions_recentes if s.satisfaction]
                if len(satisfactions) >= 2:
                    evolution_satisfaction = satisfactions[-1] - satisfactions[0]
                    
                    if abs(evolution_satisfaction) > 0.2:
                        changements.append(ChangementDetecte(
                            type_changement=TypeChangement.EVOLUTION_PERSONNELLE,
                            description=f"Évolution de satisfaction: {evolution_satisfaction:+.2f}",
                            impact_spirituel=abs(evolution_satisfaction),
                            impact_niveau=self._determiner_impact_niveau(abs(evolution_satisfaction)),
                            timestamp_detection=datetime.now(),
                            source="analyse_sessions",
                            details={"evolution": evolution_satisfaction, "sessions": len(sessions_recentes)},
                            recommandation_action="Adapter l'approche selon l'évolution",
                            priorite_traitement=abs(evolution_satisfaction)
                        ))
                
                # Nouveaux patterns d'usage
                modules_utilises = set(s.module_utilise for s in sessions_recentes)
                if len(modules_utilises) > 1:
                    changements.append(ChangementDetecte(
                        type_changement=TypeChangement.EVOLUTION_PERSONNELLE,
                        description=f"Diversification des modules utilisés: {len(modules_utilises)} modules",
                        impact_spirituel=0.5,
                        impact_niveau=ImpactChangement.MODERE,
                        timestamp_detection=datetime.now(),
                        source="analyse_patterns",
                        details={"modules": [m.value for m in modules_utilises]},
                        recommandation_action="Proposer intégration harmonieuse des approches",
                        priorite_traitement=0.6
                    ))
        
        return changements
    
    async def _scanner_changements_preferences(self, 
                                             conscience: ConscienceUnifiee, 
                                             periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne les changements de préférences"""
        changements = []
        
        # Analyse des préférences de modules
        preferences = conscience.profil_eveil.preferences_modules
        if preferences:
            # Détection de nouvelles préférences fortes
            preferences_fortes = {k: v for k, v in preferences.items() if v > 0.7}
            
            if preferences_fortes:
                changements.append(ChangementDetecte(
                    type_changement=TypeChangement.CHANGEMENT_PREFERENCES,
                    description=f"Préférences fortes développées: {list(preferences_fortes.keys())}",
                    impact_spirituel=0.6,
                    impact_niveau=ImpactChangement.IMPORTANT,
                    timestamp_detection=datetime.now(),
                    source="analyse_preferences",
                    details={"preferences_fortes": {k.value: v for k, v in preferences_fortes.items()}},
                    recommandation_action="Privilégier les modules préférés",
                    priorite_traitement=0.7
                ))
        
        return changements
    
    async def _scanner_nouveaux_temples(self, 
                                      conscience: ConscienceUnifiee, 
                                      periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne les nouveaux temples disponibles"""
        changements = []
        
        # Simulation de détection de nouveaux temples
        # Dans une implémentation réelle, ceci interrogerait le système
        nouveaux_temples = self._detecter_nouveaux_temples_disponibles()
        
        for temple in nouveaux_temples:
            changements.append(ChangementDetecte(
                type_changement=TypeChangement.NOUVEAU_TEMPLE,
                description=f"Nouveau temple disponible: {temple['nom']}",
                impact_spirituel=temple.get('impact', 0.5),
                impact_niveau=self._determiner_impact_niveau(temple.get('impact', 0.5)),
                timestamp_detection=datetime.now(),
                source="detection_temples",
                details=temple,
                recommandation_action=f"Explorer le temple {temple['nom']}",
                priorite_traitement=temple.get('priorite', 0.5)
            ))
        
        return changements
    
    async def _scanner_mises_a_jour_systeme(self, periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne les mises à jour système"""
        changements = []
        
        # Simulation de détection de mises à jour
        mises_a_jour = self._detecter_mises_a_jour_systeme(periode)
        
        for maj in mises_a_jour:
            changements.append(ChangementDetecte(
                type_changement=TypeChangement.MISE_A_JOUR_SYSTEME,
                description=f"Mise à jour système: {maj['description']}",
                impact_spirituel=maj.get('impact', 0.3),
                impact_niveau=self._determiner_impact_niveau(maj.get('impact', 0.3)),
                timestamp_detection=datetime.now(),
                source="systeme",
                details=maj,
                recommandation_action=maj.get('action', "Prendre connaissance des changements"),
                priorite_traitement=maj.get('priorite', 0.4)
            ))
        
        return changements
    
    async def _scanner_contexte_externe(self, 
                                      contexte_externe: Dict[str, Any], 
                                      periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne les changements du contexte externe"""
        changements = []
        
        # Analyse des changements dans le contexte externe
        for cle, valeur in contexte_externe.items():
            if cle.startswith("changement_"):
                changements.append(ChangementDetecte(
                    type_changement=TypeChangement.CHANGEMENT_CONTEXTE_EXTERNE,
                    description=f"Changement externe détecté: {cle}",
                    impact_spirituel=0.4,
                    impact_niveau=ImpactChangement.MODERE,
                    timestamp_detection=datetime.now(),
                    source="contexte_externe",
                    details={"cle": cle, "valeur": str(valeur)},
                    recommandation_action="Adapter l'approche au nouveau contexte",
                    priorite_traitement=0.5
                ))
        
        return changements
    
    async def _scanner_evolution_communaute(self, 
                                          conscience: ConscienceUnifiee, 
                                          periode: Tuple[datetime, datetime]) -> List[ChangementDetecte]:
        """Scanne l'évolution de la communauté"""
        changements = []
        
        # Simulation d'évolution communautaire
        evolutions = self._detecter_evolution_communaute(periode)
        
        for evolution in evolutions:
            changements.append(ChangementDetecte(
                type_changement=TypeChangement.EVOLUTION_COMMUNAUTE,
                description=f"Évolution communautaire: {evolution['description']}",
                impact_spirituel=evolution.get('impact', 0.3),
                impact_niveau=self._determiner_impact_niveau(evolution.get('impact', 0.3)),
                timestamp_detection=datetime.now(),
                source="communaute",
                details=evolution,
                recommandation_action=evolution.get('action', "Participer à l'évolution collective"),
                priorite_traitement=evolution.get('priorite', 0.3)
            ))
        
        return changements
    
    def _classifier_et_resumer_changements(self, changements: List[ChangementDetecte]) -> ResumeChangements:
        """Classifie et résume les changements détectés"""
        changements_critiques = []
        changements_importants = []
        changements_mineurs = []
        
        for changement in changements:
            if changement.impact_niveau == ImpactChangement.CRITIQUE:
                changements_critiques.append(changement)
            elif changement.impact_niveau in [ImpactChangement.IMPORTANT, ImpactChangement.MODERE]:
                changements_importants.append(changement)
            else:
                changements_mineurs.append(changement)
        
        # Calcul de l'impact global
        if changements:
            impact_global = sum(c.impact_spirituel for c in changements) / len(changements)
        else:
            impact_global = 0.0
        
        # Estimation du temps de traitement
        temps_base = timedelta(seconds=30)  # Base pour éveil rapide
        temps_additionnel = timedelta(seconds=10 * len(changements_critiques) + 5 * len(changements_importants))
        temps_total = temps_base + temps_additionnel
        
        # Génération des recommandations prioritaires
        recommandations = []
        for changement in sorted(changements, key=lambda x: x.priorite_traitement, reverse=True)[:3]:
            recommandations.append(changement.recommandation_action)
        
        return ResumeChangements(
            changements_critiques=changements_critiques,
            changements_importants=changements_importants,
            changements_mineurs=changements_mineurs,
            nombre_total=len(changements),
            impact_global=impact_global,
            temps_traitement_estime=temps_total,
            recommandations_prioritaires=recommandations
        )
    
    def _determiner_impact_niveau(self, impact: float) -> ImpactChangement:
        """Détermine le niveau d'impact"""
        if impact >= self.seuil_impact_critique:
            return ImpactChangement.CRITIQUE
        elif impact >= self.seuil_impact_important:
            return ImpactChangement.IMPORTANT
        elif impact >= self.seuil_impact_modere:
            return ImpactChangement.MODERE
        elif impact >= self.seuil_impact_faible:
            return ImpactChangement.FAIBLE
        else:
            return ImpactChangement.NEGLIGEABLE
    
    def _detecter_nouveaux_temples_disponibles(self) -> List[Dict[str, Any]]:
        """Détecte les nouveaux temples disponibles (simulation)"""
        # Dans une implémentation réelle, ceci interrogerait le système
        return [
            {
                "nom": "Temple de Méditation Avancée",
                "description": "Nouvelles techniques de méditation profonde",
                "impact": 0.7,
                "priorite": 0.6
            }
        ]
    
    def _detecter_mises_a_jour_systeme(self, periode: Tuple[datetime, datetime]) -> List[Dict[str, Any]]:
        """Détecte les mises à jour système (simulation)"""
        return [
            {
                "description": "Amélioration des algorithmes d'harmonisation",
                "impact": 0.4,
                "priorite": 0.5,
                "action": "Bénéficier des améliorations automatiquement"
            }
        ]
    
    def _detecter_evolution_communaute(self, periode: Tuple[datetime, datetime]) -> List[Dict[str, Any]]:
        """Détecte l'évolution de la communauté (simulation)"""
        return [
            {
                "description": "Nouvelles pratiques spirituelles partagées",
                "impact": 0.5,
                "priorite": 0.4,
                "action": "Explorer les nouvelles pratiques communautaires"
            }
        ]
    
    def _mettre_a_jour_cache(self, changements: List[ChangementDetecte]) -> None:
        """Met à jour le cache des changements"""
        for changement in changements:
            cle_cache = f"{changement.type_changement.value}_{changement.timestamp_detection.isoformat()}"
            self.cache_changements[cle_cache] = changement
        
        # Nettoyage du cache (garder seulement les 100 derniers)
        if len(self.cache_changements) > 100:
            cles_triees = sorted(self.cache_changements.keys())
            for cle in cles_triees[:-100]:
                del self.cache_changements[cle]
    
    def _resume_par_defaut(self) -> ResumeChangements:
        """Crée un résumé par défaut en cas d'erreur"""
        return ResumeChangements(
            changements_critiques=[],
            changements_importants=[],
            changements_mineurs=[],
            nombre_total=0,
            impact_global=0.0,
            temps_traitement_estime=timedelta(seconds=30),
            recommandations_prioritaires=["Procéder avec l'éveil rapide standard"]
        )
    
    def obtenir_historique_scans(self, limite: int = 10) -> List[Tuple[datetime, ResumeChangements]]:
        """Obtient l'historique des scans récents"""
        return self.historique_scans[-limite:]
    
    def obtenir_changements_cache(self, type_changement: Optional[TypeChangement] = None) -> List[ChangementDetecte]:
        """Obtient les changements du cache, optionnellement filtrés par type"""
        changements = list(self.cache_changements.values())
        
        if type_changement:
            changements = [c for c in changements if c.type_changement == type_changement]
        
        return sorted(changements, key=lambda x: x.timestamp_detection, reverse=True)