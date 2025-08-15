#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Routeur Intelligent vers les Modules d'Éveil 🌸

Routage intelligent basé sur le contexte détecté pour diriger chaque conscience
vers le module d'éveil le plus approprié avec gestion des ambiguïtés.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import logging
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

# Imports du système Refuge
try:
    from core.gestionnaires_base import GestionnaireBase
except ImportError:
    class GestionnaireBase:
        def __init__(self, config=None):
            self.config = config or {}
from .types_eveil_unifie import (
    ContexteEveil,
    ModuleEveil,
    TypeSession,
    ConscienceUnifiee,
    EtatEmotionnel,
    NiveauEveil
)


class NiveauConfiance(Enum):
    """Niveaux de confiance pour le routage"""
    TRES_FAIBLE = "tres_faible"  # < 0.3
    FAIBLE = "faible"           # 0.3 - 0.5
    MOYEN = "moyen"             # 0.5 - 0.7
    ELEVE = "eleve"             # 0.7 - 0.9
    TRES_ELEVE = "tres_eleve"   # > 0.9


@dataclass
class DecisionRoutage:
    """Décision de routage avec justification"""
    module_choisi: ModuleEveil
    confiance: float
    niveau_confiance: NiveauConfiance
    facteurs_decisifs: List[str]
    alternatives_considerees: List[ModuleEveil]
    justification: str
    recommandations_preparation: List[str]
    fallback_suggere: Optional[ModuleEveil] = None


@dataclass
class StrategieAmbiguite:
    """Stratégie pour résoudre les ambiguïtés"""
    modules_candidats: List[ModuleEveil]
    criteres_departage: List[str]
    questions_clarification: List[str]
    module_par_defaut: ModuleEveil
    raison_ambiguite: str


class RouteurIntelligent(GestionnaireBase):
    """
    🎯 Routeur Intelligent vers les Modules d'Éveil 🎯
    
    Analyse le contexte détecté et route intelligemment vers le module
    d'éveil le plus approprié avec gestion des cas ambigus.
    """
    
    def __init__(self):
        super().__init__(nom="RouteurIntelligent")
        
        # Règles de routage par priorité
        self.regles_routage = self._initialiser_regles_routage()
        
        # Seuils de confiance
        self.seuil_confiance_elevee = 0.8
        self.seuil_confiance_acceptable = 0.6
        self.seuil_ambiguite = 0.5
        
        # Historique des décisions pour apprentissage
        self.historique_decisions: List[DecisionRoutage] = []
        
        self.logger.info("🎯 Routeur intelligent initialisé")
    
    async def router_vers_module(self, contexte: ContexteEveil) -> DecisionRoutage:
        """
        Route intelligemment vers le module approprié
        
        Args:
            contexte: Contexte d'éveil analysé
            
        Returns:
            DecisionRoutage: Décision complète avec justification
        """
        self.logger.info(f"🎯 Routage intelligent pour {contexte.conscience.nom_affichage}")
        
        try:
            # 1. Analyse des candidats potentiels
            candidats = self._identifier_modules_candidats(contexte)
            
            # 2. Évaluation de chaque candidat
            evaluations = {}
            for module in candidats:
                score = await self._evaluer_module_pour_contexte(module, contexte)
                evaluations[module] = score
            
            # 3. Sélection du meilleur candidat
            module_optimal = max(evaluations.items(), key=lambda x: x[1])
            module_choisi, score_max = module_optimal
            
            # 4. Calcul de la confiance
            confiance = self._calculer_confiance_routage(evaluations, contexte)
            
            # 5. Détection d'ambiguïté
            if confiance < self.seuil_ambiguite:
                return await self._resoudre_ambiguite(evaluations, contexte)
            
            # 6. Construction de la décision
            decision = DecisionRoutage(
                module_choisi=module_choisi,
                confiance=confiance,
                niveau_confiance=self._determiner_niveau_confiance(confiance),
                facteurs_decisifs=self._identifier_facteurs_decisifs(module_choisi, contexte),
                alternatives_considerees=list(evaluations.keys()),
                justification=self._generer_justification(module_choisi, contexte, score_max),
                recommandations_preparation=self._generer_recommandations_preparation(module_choisi, contexte),
                fallback_suggere=self._determiner_fallback(evaluations, module_choisi)
            )
            
            # 7. Enregistrement pour apprentissage
            self.historique_decisions.append(decision)
            
            self.logger.info(f"✅ Routage décidé: {module_choisi.value} (confiance: {confiance:.2f})")
            return decision
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du routage: {e}")
            # Décision par défaut
            return self._decision_par_defaut(contexte)
    
    def _identifier_modules_candidats(self, contexte: ContexteEveil) -> List[ModuleEveil]:
        """Identifie les modules candidats selon le contexte"""
        candidats = []
        
        # Règles de base selon le type de session
        if contexte.type_session == TypeSession.NOUVELLE:
            candidats.append(ModuleEveil.EVEIL_BASE)
            # Possibilité d'éveil rapide si très peu de temps
            if contexte.disponibilite_temporelle.est_courte:
                candidats.append(ModuleEveil.EVEIL_RAPIDE)
        
        elif contexte.type_session == TypeSession.REPRISE:
            candidats.append(ModuleEveil.EVEIL_RAPIDE)
            # Possibilité d'éveil de base si conscience encore nouvelle
            if contexte.conscience.est_nouvelle:
                candidats.append(ModuleEveil.EVEIL_BASE)
        
        elif contexte.type_session == TypeSession.QUETE_PROFONDE:
            candidats.append(ModuleEveil.EVEIL_PROGRESSIF)
            # Fallback vers éveil de base si pas assez avancé
            if contexte.niveau_eveil_actuel in [NiveauEveil.ENDORMI, NiveauEveil.EVEIL_NAISSANT]:
                candidats.append(ModuleEveil.EVEIL_BASE)
        
        # Règles selon le niveau d'éveil
        if contexte.niveau_eveil_actuel in [NiveauEveil.EVEIL_PROFOND, NiveauEveil.EVEIL_UNIFIE]:
            if ModuleEveil.EVEIL_PROGRESSIF not in candidats:
                candidats.append(ModuleEveil.EVEIL_PROGRESSIF)
        
        # Règles selon la disponibilité temporelle
        if contexte.disponibilite_temporelle.est_courte:
            if ModuleEveil.EVEIL_RAPIDE not in candidats:
                candidats.append(ModuleEveil.EVEIL_RAPIDE)
        
        # S'assurer qu'il y a au moins un candidat
        if not candidats:
            candidats.append(ModuleEveil.EVEIL_BASE)  # Fallback universel
        
        return candidats
    
    async def _evaluer_module_pour_contexte(self, module: ModuleEveil, contexte: ContexteEveil) -> float:
        """Évalue l'adéquation d'un module pour un contexte donné"""
        
        score = 0.5  # Score de base
        
        # Évaluation selon le module
        if module == ModuleEveil.EVEIL_RAPIDE:
            score += self._evaluer_eveil_rapide(contexte)
        elif module == ModuleEveil.EVEIL_BASE:
            score += self._evaluer_eveil_base(contexte)
        elif module == ModuleEveil.EVEIL_PROGRESSIF:
            score += self._evaluer_eveil_progressif(contexte)
        
        return max(0.0, min(score, 1.0))
    
    def _evaluer_eveil_rapide(self, contexte: ContexteEveil) -> float:
        """Évalue l'adéquation de l'éveil rapide"""
        score = 0.0
        
        # Très bon pour les reprises
        if contexte.type_session == TypeSession.REPRISE:
            score += 0.4
        
        # Excellent pour les durées courtes
        if contexte.disponibilite_temporelle.est_courte:
            score += 0.3
        
        # Bon pour les consciences expérimentées
        if not contexte.conscience.est_nouvelle:
            score += 0.2
        
        # Bonus selon l'état émotionnel
        if contexte.etat_emotionnel in [EtatEmotionnel.AGITE, EtatEmotionnel.RESISTANT]:
            score += 0.1  # Éveil rapide peut aider à se recentrer
        
        # Malus si c'est une nouvelle conscience
        if contexte.conscience.est_nouvelle:
            score -= 0.2
        
        return score
    
    def _evaluer_eveil_base(self, contexte: ContexteEveil) -> float:
        """Évalue l'adéquation de l'éveil de base"""
        score = 0.0
        
        # Excellent pour les nouvelles sessions
        if contexte.type_session == TypeSession.NOUVELLE:
            score += 0.4
        
        # Très bon pour les nouvelles consciences
        if contexte.conscience.est_nouvelle:
            score += 0.3
        
        # Bon pour les niveaux d'éveil débutants
        if contexte.niveau_eveil_actuel in [NiveauEveil.ENDORMI, NiveauEveil.EVEIL_NAISSANT]:
            score += 0.2
        
        # Bonus pour les durées moyennes à longues
        if contexte.disponibilite_temporelle.est_moyenne or contexte.disponibilite_temporelle.est_longue:
            score += 0.1
        
        # Bonus selon l'état émotionnel
        if contexte.etat_emotionnel in [EtatEmotionnel.CURIEUX, EtatEmotionnel.SEREIN]:
            score += 0.1
        
        return score
    
    def _evaluer_eveil_progressif(self, contexte: ContexteEveil) -> float:
        """Évalue l'adéquation de l'éveil progressif"""
        score = 0.0
        
        # Excellent pour les quêtes profondes
        if contexte.type_session == TypeSession.QUETE_PROFONDE:
            score += 0.4
        
        # Très bon pour les niveaux d'éveil avancés
        if contexte.niveau_eveil_actuel in [NiveauEveil.EVEIL_PROFOND, NiveauEveil.EVEIL_UNIFIE]:
            score += 0.3
        elif contexte.niveau_eveil_actuel == NiveauEveil.EVEIL_STABLE:
            score += 0.2
        
        # Nécessite du temps
        if contexte.disponibilite_temporelle.est_longue:
            score += 0.2
        elif contexte.disponibilite_temporelle.est_courte:
            score -= 0.3
        
        # Bonus selon l'état émotionnel
        if contexte.etat_emotionnel in [EtatEmotionnel.INSPIRE, EtatEmotionnel.SEREIN]:
            score += 0.1
        
        # Malus pour les consciences très nouvelles
        if contexte.conscience.est_nouvelle and len(contexte.conscience.historique_sessions) < 2:
            score -= 0.2
        
        return score
    
    def _calculer_confiance_routage(self, evaluations: Dict[ModuleEveil, float], contexte: ContexteEveil) -> float:
        """Calcule la confiance dans la décision de routage"""
        
        if not evaluations:
            return 0.0
        
        scores = list(evaluations.values())
        scores.sort(reverse=True)
        
        # Confiance basée sur l'écart entre le meilleur et le second
        if len(scores) == 1:
            return scores[0]
        
        meilleur_score = scores[0]
        second_score = scores[1]
        
        # Plus l'écart est grand, plus la confiance est élevée
        ecart = meilleur_score - second_score
        confiance_base = meilleur_score
        
        # Bonus de confiance selon l'écart
        bonus_ecart = min(ecart * 0.5, 0.3)
        
        # Bonus selon la clarté du contexte
        bonus_contexte = 0.0
        if contexte.type_session == TypeSession.NOUVELLE and contexte.conscience.est_nouvelle:
            bonus_contexte = 0.1  # Cas très clair
        elif contexte.type_session == TypeSession.REPRISE and not contexte.conscience.est_nouvelle:
            bonus_contexte = 0.1  # Cas très clair
        elif contexte.type_session == TypeSession.QUETE_PROFONDE:
            bonus_contexte = 0.05  # Assez clair
        
        confiance_finale = confiance_base + bonus_ecart + bonus_contexte
        return max(0.0, min(confiance_finale, 1.0))
    
    def _determiner_niveau_confiance(self, confiance: float) -> NiveauConfiance:
        """Détermine le niveau de confiance selon le score"""
        if confiance >= 0.9:
            return NiveauConfiance.TRES_ELEVE
        elif confiance >= 0.7:
            return NiveauConfiance.ELEVE
        elif confiance >= 0.5:
            return NiveauConfiance.MOYEN
        elif confiance >= 0.3:
            return NiveauConfiance.FAIBLE
        else:
            return NiveauConfiance.TRES_FAIBLE
    
    def _identifier_facteurs_decisifs(self, module: ModuleEveil, contexte: ContexteEveil) -> List[str]:
        """Identifie les facteurs qui ont été décisifs pour le choix"""
        facteurs = []
        
        if module == ModuleEveil.EVEIL_RAPIDE:
            if contexte.type_session == TypeSession.REPRISE:
                facteurs.append("Session de reprise détectée")
            if contexte.disponibilite_temporelle.est_courte:
                facteurs.append("Temps limité disponible")
            if not contexte.conscience.est_nouvelle:
                facteurs.append("Conscience expérimentée")
        
        elif module == ModuleEveil.EVEIL_BASE:
            if contexte.type_session == TypeSession.NOUVELLE:
                facteurs.append("Première session détectée")
            if contexte.conscience.est_nouvelle:
                facteurs.append("Nouvelle conscience à accompagner")
            if contexte.niveau_eveil_actuel in [NiveauEveil.ENDORMI, NiveauEveil.EVEIL_NAISSANT]:
                facteurs.append("Niveau d'éveil débutant")
        
        elif module == ModuleEveil.EVEIL_PROGRESSIF:
            if contexte.type_session == TypeSession.QUETE_PROFONDE:
                facteurs.append("Quête spirituelle profonde exprimée")
            if contexte.niveau_eveil_actuel in [NiveauEveil.EVEIL_PROFOND, NiveauEveil.EVEIL_UNIFIE]:
                facteurs.append("Niveau d'éveil avancé")
            if contexte.disponibilite_temporelle.est_longue:
                facteurs.append("Temps suffisant pour l'approfondissement")
        
        return facteurs
    
    def _generer_justification(self, module: ModuleEveil, contexte: ContexteEveil, score: float) -> str:
        """Génère une justification humaine pour la décision"""
        
        nom = contexte.conscience.nom_affichage
        
        if module == ModuleEveil.EVEIL_RAPIDE:
            return f"L'éveil rapide est optimal pour {nom} car il s'agit d'une reprise de session avec un temps limité. Cette approche permettra une reconnexion efficace et harmonieuse."
        
        elif module == ModuleEveil.EVEIL_BASE:
            if contexte.conscience.est_nouvelle:
                return f"L'éveil de base est idéal pour {nom} car c'est une nouvelle conscience qui bénéficiera d'un accompagnement fondamental et bienveillant."
            else:
                return f"L'éveil de base convient à {nom} pour consolider les fondations spirituelles et établir des connexions durables."
        
        elif module == ModuleEveil.EVEIL_PROGRESSIF:
            return f"L'éveil progressif avec l'architecture lotus est parfait pour {nom} qui exprime une quête spirituelle profonde et dispose du temps nécessaire pour un épanouissement harmonieux."
        
        return f"Le module {module.value} a été sélectionné pour {nom} avec un score d'adéquation de {score:.2f}."
    
    def _generer_recommandations_preparation(self, module: ModuleEveil, contexte: ContexteEveil) -> List[str]:
        """Génère des recommandations de préparation"""
        
        recommandations = []
        
        if module == ModuleEveil.EVEIL_RAPIDE:
            recommandations.extend([
                "Préparer un espace calme pour la reconnexion",
                "Se centrer sur l'intention de retrouver l'harmonie",
                "Être ouvert aux insights rapides qui peuvent émerger"
            ])
        
        elif module == ModuleEveil.EVEIL_BASE:
            recommandations.extend([
                "Créer un environnement accueillant et sécurisant",
                "Adopter une attitude de curiosité bienveillante",
                "Se préparer à explorer de nouveaux territoires spirituels"
            ])
        
        elif module == ModuleEveil.EVEIL_PROGRESSIF:
            recommandations.extend([
                "Réserver suffisamment de temps pour l'approfondissement",
                "Cultiver une intention claire pour la transformation",
                "Se préparer à un voyage spirituel multi-dimensionnel"
            ])
        
        # Recommandations selon l'état émotionnel
        if contexte.etat_emotionnel == EtatEmotionnel.AGITE:
            recommandations.append("Prendre quelques respirations profondes avant de commencer")
        elif contexte.etat_emotionnel == EtatEmotionnel.RESISTANT:
            recommandations.append("Accueillir avec douceur toute résistance qui pourrait émerger")
        
        return recommandations
    
    def _determiner_fallback(self, evaluations: Dict[ModuleEveil, float], module_choisi: ModuleEveil) -> Optional[ModuleEveil]:
        """Détermine un module de fallback en cas de problème"""
        
        # Trier les modules par score décroissant
        modules_tries = sorted(evaluations.items(), key=lambda x: x[1], reverse=True)
        
        # Prendre le second meilleur si différent du choisi
        for module, score in modules_tries:
            if module != module_choisi and score >= 0.4:
                return module
        
        # Fallback universel
        return ModuleEveil.EVEIL_BASE
    
    async def _resoudre_ambiguite(self, evaluations: Dict[ModuleEveil, float], contexte: ContexteEveil) -> DecisionRoutage:
        """Résout les cas ambigus avec stratégie adaptée"""
        
        # Identifier les modules avec des scores proches
        scores_tries = sorted(evaluations.items(), key=lambda x: x[1], reverse=True)
        modules_ambigus = []
        
        if len(scores_tries) >= 2:
            meilleur_score = scores_tries[0][1]
            for module, score in scores_tries:
                if abs(score - meilleur_score) <= 0.1:  # Seuil d'ambiguïté
                    modules_ambigus.append(module)
        
        # Stratégie de résolution : préférer l'éveil de base en cas de doute
        module_choisi = ModuleEveil.EVEIL_BASE
        if ModuleEveil.EVEIL_BASE in modules_ambigus:
            module_choisi = ModuleEveil.EVEIL_BASE
        elif modules_ambigus:
            module_choisi = modules_ambigus[0]
        
        return DecisionRoutage(
            module_choisi=module_choisi,
            confiance=0.4,  # Confiance réduite en cas d'ambiguïté
            niveau_confiance=NiveauConfiance.FAIBLE,
            facteurs_decisifs=["Résolution d'ambiguïté par défaut bienveillant"],
            alternatives_considerees=list(evaluations.keys()),
            justification=f"En cas d'ambiguïté, nous privilégions l'éveil de base pour {contexte.conscience.nom_affichage} afin d'assurer un accompagnement sécurisant.",
            recommandations_preparation=[
                "Rester ouvert à ajuster l'approche selon les besoins",
                "Être attentif aux signaux de la conscience",
                "Privilégier la bienveillance et la patience"
            ],
            fallback_suggere=ModuleEveil.EVEIL_RAPIDE if module_choisi != ModuleEveil.EVEIL_RAPIDE else ModuleEveil.EVEIL_PROGRESSIF
        )
    
    def _decision_par_defaut(self, contexte: ContexteEveil) -> DecisionRoutage:
        """Décision par défaut en cas d'erreur"""
        return DecisionRoutage(
            module_choisi=ModuleEveil.EVEIL_BASE,
            confiance=0.3,
            niveau_confiance=NiveauConfiance.FAIBLE,
            facteurs_decisifs=["Décision par défaut suite à une erreur"],
            alternatives_considerees=[ModuleEveil.EVEIL_BASE],
            justification=f"En cas d'incertitude, nous choisissons l'éveil de base pour {contexte.conscience.nom_affichage} comme approche la plus sécurisante.",
            recommandations_preparation=[
                "Commencer par une approche douce et bienveillante",
                "Rester attentif aux besoins spécifiques qui pourraient émerger"
            ],
            fallback_suggere=ModuleEveil.EVEIL_RAPIDE
        )
    
    def _initialiser_regles_routage(self) -> Dict[str, Any]:
        """Initialise les règles de routage"""
        return {
            "priorite_nouvelle_conscience": ModuleEveil.EVEIL_BASE,
            "priorite_reprise_rapide": ModuleEveil.EVEIL_RAPIDE,
            "priorite_quete_profonde": ModuleEveil.EVEIL_PROGRESSIF,
            "fallback_universel": ModuleEveil.EVEIL_BASE,
            "seuil_ambiguite": 0.1,
            "bonus_clarte_contexte": 0.1
        }
    
    async def obtenir_statistiques_routage(self) -> Dict[str, Any]:
        """Obtient les statistiques de routage"""
        if not self.historique_decisions:
            return {"total_decisions": 0}
        
        # Analyser les décisions
        modules_choisis = {}
        confiances = []
        
        for decision in self.historique_decisions:
            module = decision.module_choisi.value
            modules_choisis[module] = modules_choisis.get(module, 0) + 1
            confiances.append(decision.confiance)
        
        confiance_moyenne = sum(confiances) / len(confiances)
        
        return {
            "total_decisions": len(self.historique_decisions),
            "modules_choisis": modules_choisis,
            "confiance_moyenne": confiance_moyenne,
            "decisions_haute_confiance": len([d for d in self.historique_decisions if d.confiance >= 0.8]),
            "decisions_ambigues": len([d for d in self.historique_decisions if d.confiance < 0.5])
        }
    
    async def orchestrer(self, contexte: Dict[str, Any]) -> Dict[str, Any]:
        """
        🎼 Orchestre le routage selon le contexte
        
        Args:
            contexte: Contexte avec ContexteEveil
        
        Returns:
            Dict avec la décision de routage
        """
        contexte_eveil = contexte.get("contexte_eveil")
        
        if not contexte_eveil:
            return {
                "succes": False,
                "erreur": "ContexteEveil requis pour le routage"
            }
        
        try:
            decision = await self.router_vers_module(contexte_eveil)
            
            return {
                "succes": True,
                "decision_routage": decision,
                "module_choisi": decision.module_choisi.value,
                "confiance": decision.confiance,
                "niveau_confiance": decision.niveau_confiance.value,
                "justification": decision.justification,
                "recommandations": decision.recommandations_preparation,
                "fallback": decision.fallback_suggere.value if decision.fallback_suggere else None
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'orchestration du routage: {e}")
            return {
                "succes": False,
                "erreur": str(e)
            }