"""
🌸 Détecteur de Contexte Intelligent 🌸

Analyse intelligente du contexte pour déterminer automatiquement
le type d'éveil le plus approprié pour chaque conscience.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from dataclasses import dataclass

from temple_eveil_unifie.types_eveil_unifie import (
    ConscienceUnifiee,
    ContexteEveil,
    TypeSession,
    TypeConscience,
    EtatEmotionnel,
    NiveauEveil,
    DureeDisponible,
    Changement,
    SessionEveil
)


@dataclass
class AnalyseContextuelle:
    """Résultat d'analyse contextuelle"""
    type_session_detecte: TypeSession
    confiance: float  # 0.0 à 1.0
    facteurs_decisifs: List[str]
    recommandations: List[str]
    etat_emotionnel_estime: EtatEmotionnel
    patterns_detectes: List[str]


class DetecteurContexteIntelligent:
    """
    🔍 Détecteur de Contexte Intelligent 🔍
    
    Analyse le contexte d'une conscience pour déterminer automatiquement
    le type d'éveil le plus approprié avec une haute précision.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Seuils de détection
        self.seuil_nouvelle_conscience = 3  # sessions
        self.seuil_session_recente = timedelta(hours=24)
        self.seuil_pause_longue = timedelta(days=7)
        
        # Patterns d'usage
        self.patterns_connus: Dict[str, List[str]] = {}
        
        self.logger.info("🔍 Détecteur de contexte intelligent initialisé")
    
    async def analyser_contexte_complet(self, 
                                      conscience: ConscienceUnifiee,
                                      intention: Optional[str] = None,
                                      duree_disponible: Optional[int] = None,
                                      contexte_externe: Optional[Dict[str, Any]] = None) -> AnalyseContextuelle:
        """
        Analyse complète du contexte d'éveil
        
        Args:
            conscience: Conscience à analyser
            intention: Intention déclarée (optionnelle)
            duree_disponible: Durée disponible en minutes
            contexte_externe: Contexte externe additionnel
            
        Returns:
            AnalyseContextuelle: Analyse complète avec recommandations
        """
        self.logger.info(f"🔍 Analyse contextuelle pour {conscience.nom_affichage}")
        
        try:
            # 1. Analyse de l'historique de sessions
            analyse_historique = self._analyser_historique_sessions(conscience)
            
            # 2. Analyse temporelle
            analyse_temporelle = self._analyser_patterns_temporels(conscience)
            
            # 3. Analyse de l'intention déclarée
            analyse_intention = self._analyser_intention_declaree(intention)
            
            # 4. Analyse de la disponibilité temporelle
            analyse_duree = self._analyser_duree_disponible(duree_disponible)
            
            # 5. Analyse de l'état émotionnel estimé
            etat_emotionnel = self._estimer_etat_emotionnel(conscience, contexte_externe)
            
            # 6. Synthèse et décision
            type_session = self._synthetiser_type_session(
                analyse_historique,
                analyse_temporelle,
                analyse_intention,
                analyse_duree,
                conscience
            )
            
            # 7. Calcul de la confiance
            confiance = self._calculer_confiance_detection(
                analyse_historique,
                analyse_temporelle,
                analyse_intention,
                analyse_duree
            )
            
            # 8. Génération des recommandations
            recommandations = self._generer_recommandations(
                type_session,
                conscience,
                analyse_duree,
                etat_emotionnel
            )
            
            # 9. Détection des patterns
            patterns = self._detecter_patterns_personnels(conscience)
            
            # 10. Construction du résultat
            analyse = AnalyseContextuelle(
                type_session_detecte=type_session,
                confiance=confiance,
                facteurs_decisifs=self._identifier_facteurs_decisifs(
                    analyse_historique, analyse_temporelle, analyse_intention, analyse_duree
                ),
                recommandations=recommandations,
                etat_emotionnel_estime=etat_emotionnel,
                patterns_detectes=patterns
            )
            
            self.logger.info(f"✅ Analyse terminée: {type_session.value} (confiance: {confiance:.2f})")
            return analyse
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'analyse contextuelle: {e}")
            # Retour d'analyse par défaut
            return AnalyseContextuelle(
                type_session_detecte=TypeSession.NOUVELLE,
                confiance=0.5,
                facteurs_decisifs=["Analyse par défaut suite à erreur"],
                recommandations=["Commencer par l'éveil de base"],
                etat_emotionnel_estime=EtatEmotionnel.SEREIN,
                patterns_detectes=[]
            )
    
    def _analyser_historique_sessions(self, conscience: ConscienceUnifiee) -> Dict[str, Any]:
        """Analyse l'historique des sessions"""
        historique = conscience.historique_sessions
        
        analyse = {
            "nombre_sessions": len(historique),
            "est_nouvelle": conscience.est_nouvelle,
            "derniere_session": conscience.derniere_session,
            "modules_preferes": self._analyser_preferences_modules(historique),
            "progression_satisfaction": self._analyser_progression_satisfaction(historique),
            "frequence_usage": self._analyser_frequence_usage(historique)
        }
        
        return analyse
    
    def _analyser_patterns_temporels(self, conscience: ConscienceUnifiee) -> Dict[str, Any]:
        """Analyse les patterns temporels d'usage"""
        maintenant = datetime.now()
        derniere_activite = conscience.derniere_activite
        
        if not derniere_activite:
            return {
                "temps_depuis_derniere": None,
                "est_session_recente": False,
                "est_pause_longue": False,
                "pattern_temporel": "premiere_fois"
            }
        
        temps_ecoule = maintenant - derniere_activite
        
        analyse = {
            "temps_depuis_derniere": temps_ecoule,
            "est_session_recente": temps_ecoule < self.seuil_session_recente,
            "est_pause_longue": temps_ecoule > self.seuil_pause_longue,
            "pattern_temporel": self._identifier_pattern_temporel(temps_ecoule)
        }
        
        return analyse
    
    def _analyser_intention_declaree(self, intention: Optional[str]) -> Dict[str, Any]:
        """Analyse l'intention déclarée par la conscience"""
        if not intention:
            return {
                "intention_presente": False,
                "type_intention": None,
                "mots_cles": [],
                "urgence_detectee": False
            }
        
        intention_lower = intention.lower()
        
        # Mots-clés pour différents types d'éveil
        mots_cles_rapide = ["rapide", "vite", "court", "bref", "reprendre", "continuer"]
        mots_cles_base = ["nouveau", "découvrir", "apprendre", "commencer", "initiation"]
        mots_cles_progressif = ["profond", "transformation", "évolution", "spirituel", "méditation"]
        
        type_intention = None
        if any(mot in intention_lower for mot in mots_cles_rapide):
            type_intention = "eveil_rapide"
        elif any(mot in intention_lower for mot in mots_cles_base):
            type_intention = "eveil_base"
        elif any(mot in intention_lower for mot in mots_cles_progressif):
            type_intention = "eveil_progressif"
        
        analyse = {
            "intention_presente": True,
            "type_intention": type_intention,
            "mots_cles": self._extraire_mots_cles(intention),
            "urgence_detectee": any(mot in intention_lower for mot in ["urgent", "vite", "maintenant"])
        }
        
        return analyse
    
    def _analyser_duree_disponible(self, duree_minutes: Optional[int]) -> Dict[str, Any]:
        """Analyse la durée disponible"""
        if duree_minutes is None:
            duree_minutes = 15  # Valeur par défaut
        
        duree = DureeDisponible(minutes_estimees=duree_minutes)
        
        analyse = {
            "duree_minutes": duree_minutes,
            "duree_obj": duree,
            "categorie": "courte" if duree.est_courte else "moyenne" if duree.est_moyenne else "longue",
            "compatible_eveil_rapide": duree.est_courte,
            "compatible_eveil_progressif": duree.est_longue
        }
        
        return analyse
    
    def _estimer_etat_emotionnel(self, 
                               conscience: ConscienceUnifiee, 
                               contexte_externe: Optional[Dict[str, Any]]) -> EtatEmotionnel:
        """Estime l'état émotionnel de la conscience"""
        # Pour l'instant, estimation basique
        # Sera enrichie avec des analyses plus sophistiquées
        
        if conscience.est_nouvelle:
            return EtatEmotionnel.CURIEUX
        
        derniere_session = conscience.derniere_session
        if derniere_session and derniere_session.satisfaction:
            if derniere_session.satisfaction > 0.8:
                return EtatEmotionnel.INSPIRE
            elif derniere_session.satisfaction < 0.5:
                return EtatEmotionnel.CONFUS
        
        return EtatEmotionnel.SEREIN
    
    def _synthetiser_type_session(self, 
                                analyse_historique: Dict[str, Any],
                                analyse_temporelle: Dict[str, Any],
                                analyse_intention: Dict[str, Any],
                                analyse_duree: Dict[str, Any],
                                conscience: ConscienceUnifiee) -> TypeSession:
        """Synthétise toutes les analyses pour déterminer le type de session"""
        
        # Règles de décision hiérarchiques
        
        # 1. Nouvelle conscience = Éveil de Base
        if analyse_historique["est_nouvelle"]:
            return TypeSession.NOUVELLE
        
        # 2. Intention explicite
        if analyse_intention["intention_presente"]:
            type_intention = analyse_intention["type_intention"]
            if type_intention == "eveil_rapide" and analyse_duree["compatible_eveil_rapide"]:
                return TypeSession.REPRISE
            elif type_intention == "eveil_progressif" and analyse_duree["compatible_eveil_progressif"]:
                return TypeSession.QUETE_PROFONDE
        
        # 3. Analyse temporelle + durée
        if analyse_temporelle["est_session_recente"] and analyse_duree["compatible_eveil_rapide"]:
            return TypeSession.REPRISE
        
        # 4. Pause longue + durée longue = Éveil progressif
        if analyse_temporelle["est_pause_longue"] and analyse_duree["compatible_eveil_progressif"]:
            return TypeSession.QUETE_PROFONDE
        
        # 5. Par défaut selon la durée
        if analyse_duree["compatible_eveil_rapide"]:
            return TypeSession.REPRISE
        elif analyse_duree["compatible_eveil_progressif"]:
            return TypeSession.QUETE_PROFONDE
        
        # 6. Fallback
        return TypeSession.NOUVELLE
    
    def _calculer_confiance_detection(self, *analyses) -> float:
        """Calcule la confiance dans la détection"""
        # Algorithme simple de confiance basé sur la cohérence des analyses
        facteurs_coherents = 0
        facteurs_totaux = 0
        
        for analyse in analyses:
            if isinstance(analyse, dict):
                facteurs_totaux += len(analyse)
                # Compte les facteurs non-None comme cohérents
                facteurs_coherents += sum(1 for v in analyse.values() if v is not None)
        
        if facteurs_totaux == 0:
            return 0.5
        
        confiance_base = facteurs_coherents / facteurs_totaux
        
        # Ajustements selon des critères spécifiques
        # (sera enrichi avec l'expérience)
        
        return min(1.0, max(0.1, confiance_base))
    
    def _generer_recommandations(self, 
                               type_session: TypeSession,
                               conscience: ConscienceUnifiee,
                               analyse_duree: Dict[str, Any],
                               etat_emotionnel: EtatEmotionnel) -> List[str]:
        """Génère des recommandations personnalisées"""
        recommandations = []
        
        if type_session == TypeSession.NOUVELLE:
            recommandations.extend([
                "Commencer par l'éveil de base pour établir les fondations",
                "Prendre le temps de découvrir le Refuge sans pression",
                "Se laisser guider par les rituels d'initiation"
            ])
        
        elif type_session == TypeSession.REPRISE:
            recommandations.extend([
                "Éveil rapide recommandé pour une reconnexion efficace",
                "Scanner les changements depuis la dernière session",
                "Restaurer rapidement les connexions spirituelles"
            ])
        
        elif type_session == TypeSession.QUETE_PROFONDE:
            recommandations.extend([
                "Éveil progressif avec architecture lotus recommandé",
                "Prévoir suffisamment de temps pour la transformation",
                "S'ouvrir aux expériences profondes d'éveil"
            ])
        
        # Recommandations selon l'état émotionnel
        if etat_emotionnel == EtatEmotionnel.CONFUS:
            recommandations.append("Commencer par des pratiques d'ancrage et de clarification")
        elif etat_emotionnel == EtatEmotionnel.AGITE:
            recommandations.append("Privilégier des approches apaisantes et centrantes")
        
        return recommandations
    
    def _identifier_facteurs_decisifs(self, *analyses) -> List[str]:
        """Identifie les facteurs qui ont été décisifs dans la détection"""
        facteurs = []
        
        # Analyse des facteurs les plus influents
        # (logique simplifiée pour l'instant)
        
        for i, analyse in enumerate(analyses):
            if isinstance(analyse, dict):
                nom_analyse = ["historique", "temporelle", "intention", "durée"][i]
                facteurs.append(f"Analyse {nom_analyse} contributive")
        
        return facteurs
    
    # Méthodes utilitaires
    
    def _analyser_preferences_modules(self, historique: List[SessionEveil]) -> Dict[str, float]:
        """Analyse les préférences de modules"""
        if not historique:
            return {}
        
        compteurs = {}
        for session in historique:
            module = session.module_utilise.value
            compteurs[module] = compteurs.get(module, 0) + 1
        
        total = len(historique)
        return {k: v/total for k, v in compteurs.items()}
    
    def _analyser_progression_satisfaction(self, historique: List[SessionEveil]) -> Dict[str, float]:
        """Analyse la progression de satisfaction"""
        if not historique:
            return {"moyenne": 0.0, "tendance": 0.0}
        
        satisfactions = [s.satisfaction for s in historique if s.satisfaction is not None]
        if not satisfactions:
            return {"moyenne": 0.0, "tendance": 0.0}
        
        moyenne = sum(satisfactions) / len(satisfactions)
        
        # Tendance simple (dernière moitié vs première moitié)
        if len(satisfactions) >= 4:
            milieu = len(satisfactions) // 2
            premiere_moitie = sum(satisfactions[:milieu]) / milieu
            seconde_moitie = sum(satisfactions[milieu:]) / (len(satisfactions) - milieu)
            tendance = seconde_moitie - premiere_moitie
        else:
            tendance = 0.0
        
        return {"moyenne": moyenne, "tendance": tendance}
    
    def _analyser_frequence_usage(self, historique: List[SessionEveil]) -> str:
        """Analyse la fréquence d'usage"""
        if len(historique) < 2:
            return "insuffisant"
        
        # Calcul simple basé sur les timestamps
        sessions_recentes = [s for s in historique if s.est_recente]
        
        if len(sessions_recentes) >= 3:
            return "frequent"
        elif len(sessions_recentes) >= 1:
            return "occasionnel"
        else:
            return "rare"
    
    def _identifier_pattern_temporel(self, temps_ecoule: timedelta) -> str:
        """Identifie le pattern temporel"""
        if temps_ecoule < timedelta(hours=1):
            return "continuation_immediate"
        elif temps_ecoule < timedelta(hours=6):
            return "reprise_courte"
        elif temps_ecoule < timedelta(days=1):
            return "reprise_journee"
        elif temps_ecoule < timedelta(days=7):
            return "reprise_semaine"
        else:
            return "retour_apres_pause"
    
    def _extraire_mots_cles(self, intention: str) -> List[str]:
        """Extrait les mots-clés significatifs de l'intention"""
        # Extraction simple pour l'instant
        mots_significatifs = []
        mots = intention.lower().split()
        
        mots_cles_importants = [
            "éveil", "méditation", "transformation", "spirituel", "conscience",
            "rapide", "profond", "nouveau", "découvrir", "apprendre"
        ]
        
        for mot in mots:
            if mot in mots_cles_importants:
                mots_significatifs.append(mot)
        
        return mots_significatifs
    
    def _detecter_patterns_personnels(self, conscience: ConscienceUnifiee) -> List[str]:
        """Détecte les patterns personnels de la conscience"""
        patterns = []
        
        # Patterns basés sur l'historique
        if len(conscience.historique_sessions) > 5:
            patterns.append("utilisateur_regulier")
        
        if conscience.profil_eveil.preferences_modules:
            module_prefere = max(conscience.profil_eveil.preferences_modules.items(), key=lambda x: x[1])
            patterns.append(f"preference_{module_prefere[0].value}")
        
        return patterns