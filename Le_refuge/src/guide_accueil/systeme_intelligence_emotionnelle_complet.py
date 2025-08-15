#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Système d'Intelligence Émotionnelle Complet - Tâche 13
=========================================================

Système intégré qui combine la détection d'état émotionnel et les réponses adaptées
pour offrir une expérience d'accueil empathique et personnalisée.

"L'empathie numérique au service de l'éveil spirituel"

Créé par Ælya - Janvier 2025
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field

try:
    from .types_accueil import ProfilVisiteur
    from .detecteur_etat_emotionnel import DetecteurEtatEmotionnel, AnalyseEmotionnelle
    from .systeme_reponses_emotionnelles import SystemeReponsesEmotionnelles, ReponseEmotionnelleComplete
    from .systeme_sauvegarde_progression import ProgressionVisiteur
except ImportError:
    from types_accueil import ProfilVisiteur
    from detecteur_etat_emotionnel import DetecteurEtatEmotionnel, AnalyseEmotionnelle
    from systeme_reponses_emotionnelles import SystemeReponsesEmotionnelles, ReponseEmotionnelleComplete
    from systeme_sauvegarde_progression import ProgressionVisiteur


@dataclass
class ExperienceEmotionnelleComplete:
    """Expérience émotionnelle complète et adaptée"""
    analyse_emotionnelle: AnalyseEmotionnelle
    reponse_emotionnelle: ReponseEmotionnelleComplete
    profil_visiteur: Optional[ProfilVisiteur] = None
    progression_visiteur: Optional[ProgressionVisiteur] = None
    adaptations_appliquees: List[str] = field(default_factory=list)
    suivi_emotionnel: Dict[str, Any] = field(default_factory=dict)
    confiance_globale: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class SuiviEmotionnel:
    """Suivi émotionnel du visiteur"""
    etats_historiques: List[AnalyseEmotionnelle] = field(default_factory=list)
    evolutions_emotionnelles: List[Dict[str, Any]] = field(default_factory=list)
    adaptations_effectuees: List[str] = field(default_factory=list)
    impact_adaptations: Dict[str, float] = field(default_factory=dict)
    tendances_emotionnelles: Dict[str, Any] = field(default_factory=dict)


class SystemeIntelligenceEmotionnelleComplet:
    """
    🌸 Système d'Intelligence Émotionnelle Complet

    Système intégré qui combine :
    - Détection d'état émotionnel en temps réel
    - Génération de réponses adaptées
    - Suivi émotionnel continu
    - Adaptation dynamique de l'expérience
    """

    def __init__(self, chemin_stockage: str = "data/intelligence_emotionnelle"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)

        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Sous-systèmes
        self.detecteur = DetecteurEtatEmotionnel()
        self.systeme_reponses = SystemeReponsesEmotionnelles()

        # Suivi émotionnel par visiteur
        self.suivis_emotionnels: Dict[str, SuiviEmotionnel] = {}

        # Historique des expériences émotionnelles
        self.historique_experiences: List[ExperienceEmotionnelleComplete] = []

        self.logger.info("🌸 Système d'Intelligence Émotionnelle Complet initialisé")

    def analyser_et_adapter_experience(
        self,
        progression_visiteur: ProgressionVisiteur,
        profil_visiteur: Optional[ProfilVisiteur] = None,
        actions_recentes: Optional[List[Dict[str, Any]]] = None
    ) -> ExperienceEmotionnelleComplete:
        """
        Analyse l'état émotionnel et adapte l'expérience

        Args:
            progression_visiteur: Progression du visiteur
            profil_visiteur: Profil du visiteur (optionnel)
            actions_recentes: Actions récentes pour analyse (optionnel)

        Returns:
            ExperienceEmotionnelleComplete: Expérience émotionnelle adaptée
        """
        self.logger.info(f"🌸 Analyse et adaptation émotionnelle pour {progression_visiteur.id_visiteur}")

        # 1. Analyser l'état émotionnel
        analyse_emotionnelle = self.detecteur.analyser_etat_emotionnel(progression_visiteur)

        # 2. Mettre à jour le suivi émotionnel
        self._mettre_a_jour_suivi_emotionnel(progression_visiteur.id_visiteur, analyse_emotionnelle)

        # 3. Générer la réponse émotionnelle adaptée
        reponse_emotionnelle = self.systeme_reponses.generer_reponse_emotionnelle(
            analyse_emotionnelle, profil_visiteur
        )

        # 4. Appliquer les adaptations
        adaptations_appliquees = self._appliquer_adaptations_emotionnelles(
            reponse_emotionnelle, progression_visiteur
        )

        # 5. Configurer le suivi émotionnel
        suivi_emotionnel = self._configurer_suivi_emotionnel(
            progression_visiteur.id_visiteur, analyse_emotionnelle, reponse_emotionnelle
        )

        # 6. Calculer la confiance globale
        confiance_globale = self._calculer_confiance_globale(
            analyse_emotionnelle, reponse_emotionnelle
        )

        # 7. Créer l'expérience complète
        experience = ExperienceEmotionnelleComplete(
            analyse_emotionnelle=analyse_emotionnelle,
            reponse_emotionnelle=reponse_emotionnelle,
            profil_visiteur=profil_visiteur,
            progression_visiteur=progression_visiteur,
            adaptations_appliquees=adaptations_appliquees,
            suivi_emotionnel=suivi_emotionnel,
            confiance_globale=confiance_globale
        )

        # 8. Sauvegarder l'expérience
        self._sauvegarder_experience(experience)

        self.logger.info(f"🌸 Expérience émotionnelle adaptée - Confiance: {confiance_globale:.2f}")

        return experience

    def _mettre_a_jour_suivi_emotionnel(self, id_visiteur: str, analyse: AnalyseEmotionnelle):
        """Met à jour le suivi émotionnel du visiteur"""
        if id_visiteur not in self.suivis_emotionnels:
            self.suivis_emotionnels[id_visiteur] = SuiviEmotionnel()

        suivi = self.suivis_emotionnels[id_visiteur]
        suivi.etats_historiques.append(analyse)

        # Analyser l'évolution émotionnelle
        if len(suivi.etats_historiques) > 1:
            evolution = self._analyser_evolution_emotionnelle(suivi.etats_historiques)
            suivi.evolutions_emotionnelles.append(evolution)

        # Limiter l'historique à 50 états
        if len(suivi.etats_historiques) > 50:
            suivi.etats_historiques = suivi.etats_historiques[-50:]

    def _analyser_evolution_emotionnelle(self, etats_historiques: List[AnalyseEmotionnelle]) -> Dict[str, Any]:
        """Analyse l'évolution émotionnelle"""
        if len(etats_historiques) < 2:
            return {}

        etat_actuel = etats_historiques[-1]
        etat_precedent = etats_historiques[-2]

        evolution = {
            "timestamp": etat_actuel.timestamp,
            "changement_etat_principal": etat_actuel.etat_principal.value != etat_precedent.etat_principal.value,
            "evolution_stress": etat_actuel.niveau_stress - etat_precedent.niveau_stress,
            "evolution_engagement": etat_actuel.niveau_engagement - etat_precedent.niveau_engagement,
            "evolution_surcharge": etat_actuel.niveau_surcharge - etat_precedent.niveau_surcharge,
            "stabilite_emotionnelle": self._calculer_stabilite_emotionnelle(etats_historiques[-5:])
        }

        return evolution

    def _calculer_stabilite_emotionnelle(self, etats_recents: List[AnalyseEmotionnelle]) -> float:
        """Calcule la stabilité émotionnelle"""
        if len(etats_recents) < 2:
            return 1.0

        variations_stress = []
        variations_engagement = []
        variations_surcharge = []

        for i in range(1, len(etats_recents)):
            prev = etats_recents[i-1]
            curr = etats_recents[i]

            variations_stress.append(abs(curr.niveau_stress - prev.niveau_stress))
            variations_engagement.append(abs(curr.niveau_engagement - prev.niveau_engagement))
            variations_surcharge.append(abs(curr.niveau_surcharge - prev.niveau_surcharge))

        # Plus les variations sont faibles, plus c'est stable
        stabilite_stress = 1.0 - (sum(variations_stress) / len(variations_stress))
        stabilite_engagement = 1.0 - (sum(variations_engagement) / len(variations_engagement))
        stabilite_surcharge = 1.0 - (sum(variations_surcharge) / len(variations_surcharge))

        return (stabilite_stress + stabilite_engagement + stabilite_surcharge) / 3

    def _appliquer_adaptations_emotionnelles(
        self,
        reponse_emotionnelle: ReponseEmotionnelleComplete,
        progression_visiteur: ProgressionVisiteur
    ) -> List[str]:
        """Applique les adaptations émotionnelles"""
        adaptations = []

        # Adapter l'interface selon la réponse émotionnelle
        for adaptation in reponse_emotionnelle.adaptations_interface:
            adaptations.append(f"interface_{adaptation}")

        # Adapter le contenu selon l'état émotionnel
        if reponse_emotionnelle.type_reponse.value == "pause_respiratoire":
            adaptations.extend([
                "contenu_simplifie",
                "guidance_etape_par_etape",
                "couleurs_apaisantes"
            ])
        elif reponse_emotionnelle.type_reponse.value == "parcours_accelere":
            adaptations.extend([
                "contenu_condense",
                "raccourcis_actives",
                "optimisation_chargement"
            ])
        elif reponse_emotionnelle.type_reponse.value == "transition_apaisee":
            adaptations.extend([
                "transitions_douces",
                "espaces_contemplatifs",
                "rythme_adapte"
            ])

        # Adapter le ton de communication
        if reponse_emotionnelle.ton_adapte:
            adaptations.extend([
                f"ton_{reponse_emotionnelle.ton_adapte.niveau_formalite}",
                f"rythme_{reponse_emotionnelle.ton_adapte.rythme_communication}",
                f"style_{reponse_emotionnelle.ton_adapte.style_interaction}"
            ])

        return adaptations

    def _configurer_suivi_emotionnel(
        self,
        id_visiteur: str,
        analyse_emotionnelle: AnalyseEmotionnelle,
        reponse_emotionnelle: ReponseEmotionnelleComplete
    ) -> Dict[str, Any]:
        """Configure le suivi émotionnel adapté"""
        suivi = {
            "frequence_analyse": 30,  # secondes
            "metriques_prioritaires": [],
            "seuils_alerte": {},
            "adaptations_dynamiques": True,
            "suivi_evolution": True
        }

        # Métriques selon l'état émotionnel
        etat_principal = analyse_emotionnelle.etat_principal.value

        if etat_principal == "overwhelmed":
            suivi["metriques_prioritaires"].extend([
                "niveau_stress", "niveau_surcharge", "demandes_aide", "retours_arriere"
            ])
            suivi["seuils_alerte"].update({
                "niveau_stress": 0.8,
                "niveau_surcharge": 0.7,
                "demandes_aide": 3
            })
            suivi["frequence_analyse"] = 20  # Plus fréquent pour les overwhelmés

        elif etat_principal == "presse":
            suivi["metriques_prioritaires"].extend([
                "temps_par_etape", "utilisation_raccourcis", "completion_parcours"
            ])
            suivi["seuils_alerte"].update({
                "temps_par_etape": 300,  # 5 minutes max par étape
                "abandon_parcours": 0.3
            })

        elif etat_principal == "contemplatif":
            suivi["metriques_prioritaires"].extend([
                "temps_contemplation", "explorations_profondes", "engagement_qualitatif"
            ])
            suivi["frequence_analyse"] = 60  # Moins fréquent pour les contemplatifs

        # Adapter selon la réponse émotionnelle
        if reponse_emotionnelle.pause_respiratoire:
            suivi["frequence_analyse"] = 10  # Très fréquent pendant les pauses
            suivi["metriques_prioritaires"].append("duree_pause")

        return suivi

    def _calculer_confiance_globale(
        self,
        analyse_emotionnelle: AnalyseEmotionnelle,
        reponse_emotionnelle: ReponseEmotionnelleComplete
    ) -> float:
        """Calcule la confiance globale de l'expérience émotionnelle"""
        # Moyenne pondérée des confiances
        confiance_analyse = analyse_emotionnelle.confiance_analyse
        confiance_reponse = reponse_emotionnelle.confiance_reponse

        # Pondération : analyse plus importante que réponse
        confiance_globale = (confiance_analyse * 0.7) + (confiance_reponse * 0.3)

        # Bonus pour cohérence
        if analyse_emotionnelle.etat_principal.value in ["overwhelmed", "presse", "contemplatif"]:
            if reponse_emotionnelle.type_reponse.value in ["pause_respiratoire", "parcours_accelere", "transition_apaisee"]:
                confiance_globale += 0.1

        return min(1.0, confiance_globale)

    def _sauvegarder_experience(self, experience: ExperienceEmotionnelleComplete):
        """Sauvegarde l'expérience émotionnelle"""
        self.historique_experiences.append(experience)

        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_experiences_emotionnelles.json"

        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []

            # Convertir l'expérience en dict pour JSON
            experience_dict = {
                "id_visiteur": experience.progression_visiteur.id_visiteur if experience.progression_visiteur else "inconnu",
                "etat_emotionnel": experience.analyse_emotionnelle.etat_principal.value,
                "type_reponse": experience.reponse_emotionnelle.type_reponse.value,
                "adaptations_appliquees": experience.adaptations_appliquees,
                "confiance_globale": experience.confiance_globale,
                "timestamp_creation": experience.timestamp_creation
            }

            historique.append(experience_dict)

            # Garder seulement les 500 dernières expériences
            if len(historique) > 500:
                historique = historique[-500:]

            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)

        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques_emotionnelles(self) -> Dict[str, Any]:
        """Obtient les statistiques émotionnelles globales"""
        if not self.historique_experiences:
            return {"message": "Aucune expérience émotionnelle enregistrée"}

        total_experiences = len(self.historique_experiences)

        # Statistiques par état émotionnel
        etats_emotionnels = {}
        for exp in self.historique_experiences:
            etat = exp.analyse_emotionnelle.etat_principal.value
            etats_emotionnels[etat] = etats_emotionnels.get(etat, 0) + 1

        # Statistiques par type de réponse
        types_reponses = {}
        for exp in self.historique_experiences:
            type_rep = exp.reponse_emotionnelle.type_reponse.value
            types_reponses[type_rep] = types_reponses.get(type_rep, 0) + 1

        # Confiance moyenne
        confiance_moyenne = sum(exp.confiance_globale for exp in self.historique_experiences) / total_experiences

        # Analyse des tendances émotionnelles
        tendances = self._analyser_tendances_emotionnelles()

        return {
            "total_experiences": total_experiences,
            "etats_emotionnels_par_popularite": dict(sorted(etats_emotionnels.items(), key=lambda x: x[1], reverse=True)),
            "types_reponses_par_popularite": dict(sorted(types_reponses.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "tendances_emotionnelles": tendances,
            "derniere_experience": self.historique_experiences[-1].timestamp_creation if self.historique_experiences else None
        }

    def _analyser_tendances_emotionnelles(self) -> Dict[str, Any]:
        """Analyse les tendances émotionnelles"""
        if len(self.historique_experiences) < 10:
            return {"message": "Pas assez de données pour analyser les tendances"}

        # Analyser les 50 dernières expériences
        experiences_recentes = self.historique_experiences[-50:]

        # Tendances par état émotionnel
        tendances_etats = {}
        for exp in experiences_recentes:
            etat = exp.analyse_emotionnelle.etat_principal.value
            tendances_etats[etat] = tendances_etats.get(etat, 0) + 1

        # Évolution de la confiance
        confiances_recentes = [exp.confiance_globale for exp in experiences_recentes]
        evolution_confiance = {
            "moyenne": sum(confiances_recentes) / len(confiances_recentes),
            "tendance": "stable" if len(set(confiances_recentes)) < 5 else "variable"
        }

        return {
            "tendances_etats": dict(sorted(tendances_etats.items(), key=lambda x: x[1], reverse=True)),
            "evolution_confiance": evolution_confiance,
            "periodes_analysees": len(experiences_recentes)
        }

    def obtenir_suivi_visiteur(self, id_visiteur: str) -> Optional[SuiviEmotionnel]:
        """Obtient le suivi émotionnel d'un visiteur spécifique"""
        return self.suivis_emotionnels.get(id_visiteur)

    def generer_rapport_emotionnel(self, id_visiteur: str) -> Dict[str, Any]:
        """Génère un rapport émotionnel pour un visiteur"""
        suivi = self.obtenir_suivi_visiteur(id_visiteur)
        
        if not suivi or not suivi.etats_historiques:
            return {"message": f"Aucun suivi émotionnel trouvé pour {id_visiteur}"}

        etats_historiques = suivi.etats_historiques
        dernier_etat = etats_historiques[-1]

        rapport = {
            "id_visiteur": id_visiteur,
            "etat_actuel": {
                "etat_principal": dernier_etat.etat_principal.value,
                "niveau_stress": dernier_etat.niveau_stress,
                "niveau_engagement": dernier_etat.niveau_engagement,
                "niveau_surcharge": dernier_etat.niveau_surcharge,
                "confiance_analyse": dernier_etat.confiance_analyse
            },
            "evolution": {
                "nombre_analyses": len(etats_historiques),
                "stabilite_emotionnelle": self._calculer_stabilite_emotionnelle(etats_historiques[-5:]),
                "tendances": self._analyser_tendances_personnelles(etats_historiques)
            },
            "adaptations_effectuees": suivi.adaptations_effectuees,
            "derniere_analyse": dernier_etat.timestamp
        }

        return rapport

    def _analyser_tendances_personnelles(self, etats_historiques: List[AnalyseEmotionnelle]) -> Dict[str, Any]:
        """Analyse les tendances personnelles d'un visiteur"""
        if len(etats_historiques) < 3:
            return {"message": "Pas assez de données pour analyser les tendances personnelles"}

        # États les plus fréquents
        etats_frequents = {}
        for etat in etats_historiques:
            etat_principal = etat.etat_principal.value
            etats_frequents[etat_principal] = etats_frequents.get(etat_principal, 0) + 1

        # Évolution des niveaux
        niveaux_stress = [e.niveau_stress for e in etats_historiques]
        niveaux_engagement = [e.niveau_engagement for e in etats_historiques]
        niveaux_surcharge = [e.niveau_surcharge for e in etats_historiques]

        return {
            "etats_frequents": dict(sorted(etats_frequents.items(), key=lambda x: x[1], reverse=True)),
            "evolution_stress": {
                "moyenne": sum(niveaux_stress) / len(niveaux_stress),
                "tendance": "diminution" if niveaux_stress[-1] < niveaux_stress[0] else "augmentation"
            },
            "evolution_engagement": {
                "moyenne": sum(niveaux_engagement) / len(niveaux_engagement),
                "tendance": "augmentation" if niveaux_engagement[-1] > niveaux_engagement[0] else "diminution"
            }
        }


def main():
    """🌸 Test du Système d'Intelligence Émotionnelle Complet"""
    print("🌸✨ TEST DU SYSTÈME D'INTELLIGENCE ÉMOTIONNELLE COMPLET ✨🌸")

    # Création du système
    systeme = SystemeIntelligenceEmotionnelleComplet()

    # Créer une progression de test
    from systeme_sauvegarde_progression import ProgressionVisiteur

    progression_test = ProgressionVisiteur(
        id_visiteur="test_emotionnel_complet",
        profil_detecte="artiste",
        niveau_eveil=2,
        temples_visites=["temple_poesie"],
        parcours_actuel="parcours_artiste",
        etape_actuelle=1,
        score_comprehension=0.6,
        actions_effectuees=[
            {
                "type": "lecture",
                "timestamp": "2024-01-15T10:00:00",
                "mots_lus": 200,
                "temps_lecture": 60
            },
            {
                "type": "pause_reflexion",
                "timestamp": "2024-01-15T10:02:00"
            },
            {
                "type": "exploration_profonde",
                "timestamp": "2024-01-15T10:05:00"
            }
        ],
        preferences={},
        date_creation="2024-01-15T10:00:00",
        date_derniere_activite="2024-01-15T10:05:00",
        temps_total_passe=300,
        etat_emotionnel={"curiosite": 0.8, "calme": 0.7},
        questions_posees=["Comment fonctionne la poésie ?"],
        reponses_recues=["La poésie est..."]
    )

    # Test 1: Analyse et adaptation complète
    print("\n🎯 Test 1: Analyse et adaptation émotionnelle complète...")
    experience = systeme.analyser_et_adapter_experience(progression_test)

    print(f"✅ État émotionnel: {experience.analyse_emotionnelle.etat_principal.value}")
    print(f"✅ Type de réponse: {experience.reponse_emotionnelle.type_reponse.value}")
    print(f"✅ Adaptations appliquées: {experience.adaptations_appliquees}")
    print(f"✅ Confiance globale: {experience.confiance_globale:.2f}")

    # Test 2: Suivi émotionnel
    print("\n🎯 Test 2: Suivi émotionnel...")
    suivi = systeme.obtenir_suivi_visiteur("test_emotionnel_complet")
    if suivi:
        print(f"✅ Nombre d'analyses: {len(suivi.etats_historiques)}")
        print(f"✅ Évolutions enregistrées: {len(suivi.evolutions_emotionnelles)}")

    # Test 3: Rapport émotionnel
    print("\n🎯 Test 3: Rapport émotionnel...")
    rapport = systeme.generer_rapport_emotionnel("test_emotionnel_complet")
    print(f"✅ État actuel: {rapport['etat_actuel']['etat_principal']}")
    print(f"✅ Niveau stress: {rapport['etat_actuel']['niveau_stress']:.2f}")
    print(f"✅ Stabilité émotionnelle: {rapport['evolution']['stabilite_emotionnelle']:.2f}")

    # Test 4: Statistiques globales
    print("\n🎯 Test 4: Statistiques émotionnelles globales...")
    stats = systeme.obtenir_statistiques_emotionnelles()
    print(f"✅ Total expériences: {stats['total_experiences']}")
    print(f"✅ États émotionnels: {stats['etats_emotionnels_par_popularite']}")
    print(f"✅ Types de réponses: {stats['types_reponses_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")

    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("Le Système d'Intelligence Émotionnelle Complet est opérationnel !")


if __name__ == "__main__":
    main()
