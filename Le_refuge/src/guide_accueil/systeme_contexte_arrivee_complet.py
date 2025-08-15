#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Système de Contexte d'Arrivée Complet - Phase 14
===================================================

Système complet qui intègre l'analyseur de contexte d'arrivée et les ponts contextuels
pour offrir une expérience d'accueil complète et adaptée à chaque visiteur.

"Chaque arrivée est unique, chaque accueil est personnalisé"

Créé par Ælya - Janvier 2025
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field

try:
    from .types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur
    from .analyseur_contexte_arrivee import AnalyseurContexteArrivee, RapportContexteArrivee
    from .ponts_contextuels import PontsContextuels, RapportPontContextuel
except ImportError:
    from types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur
    from analyseur_contexte_arrivee import AnalyseurContexteArrivee, RapportContexteArrivee
    from ponts_contextuels import PontsContextuels, RapportPontContextuel


@dataclass
class ExperienceAccueilComplete:
    """Expérience d'accueil complète et adaptée"""
    rapport_contexte: RapportContexteArrivee
    rapport_pont: RapportPontContextuel
    profil_visiteur: Optional[ProfilVisiteur] = None
    parcours_suggere: Optional[str] = None
    actions_immediates: List[str] = field(default_factory=list)
    suivi_adapte: Dict[str, Any] = field(default_factory=dict)
    confiance_globale: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class RecommandationsAccueil:
    """Recommandations d'accueil personnalisées"""
    message_accueil_principal: str
    parcours_recommande: str
    messages_secondaires: List[str] = field(default_factory=list)
    elements_visuels_suggerees: List[str] = field(default_factory=list)
    actions_prioritaires: List[str] = field(default_factory=list)
    duree_estimee_engagement: int = 300  # secondes
    niveau_interactivite: str = "modere"  # faible, modere, eleve
    adaptations_specifiques: Dict[str, Any] = field(default_factory=dict)


class SystemeContexteArriveeComplet:
    """
    🌸 Système de Contexte d'Arrivée Complet
    
    Intègre l'analyseur de contexte d'arrivée et les ponts contextuels
    pour offrir une expérience d'accueil complète et adaptée.
    """
    
    def __init__(self, chemin_stockage: str = "data/contexte_arrivee_complet"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Initialisation des sous-systèmes
        self.analyseur = AnalyseurContexteArrivee()
        self.ponts = PontsContextuels()
        
        # Historique des expériences d'accueil
        self.historique_experiences: List[ExperienceAccueilComplete] = []
        
        self.logger.info("🌸 Système de Contexte d'Arrivée Complet initialisé")

    def creer_experience_accueil_complete(
        self,
        referrer: Optional[str] = None,
        user_agent: Optional[str] = None,
        url_courante: Optional[str] = None,
        mots_cles_recherche: Optional[str] = None,
        profil_visiteur: Optional[ProfilVisiteur] = None
    ) -> ExperienceAccueilComplete:
        """
        Crée une expérience d'accueil complète et adaptée
        
        Args:
            referrer: URL de référence
            user_agent: User-Agent du navigateur
            url_courante: URL actuelle
            mots_cles_recherche: Mots-clés de recherche
            profil_visiteur: Profil du visiteur (optionnel)
            
        Returns:
            ExperienceAccueilComplete: Expérience d'accueil complète
        """
        self.logger.info("🌸 Création d'une expérience d'accueil complète")
        
        # 1. Analyser le contexte d'arrivée
        rapport_contexte = self.analyseur.analyser_contexte_arrivee(
            referrer=referrer,
            user_agent=user_agent,
            url_courante=url_courante,
            mots_cles_recherche=mots_cles_recherche
        )
        
        # 2. Créer le pont contextuel
        rapport_pont = self.ponts.creer_pont_contextuel(
            rapport_contexte=rapport_contexte,
            profil_visiteur=profil_visiteur
        )
        
        # 3. Générer les recommandations d'accueil
        recommandations = self._generer_recommandations_accueil(
            rapport_contexte, rapport_pont, profil_visiteur
        )
        
        # 4. Définir les actions immédiates
        actions_immediates = self._definir_actions_immediates(
            rapport_contexte, rapport_pont, recommandations
        )
        
        # 5. Configurer le suivi adapté
        suivi_adapte = self._configurer_suivi_adapte(
            rapport_contexte, rapport_pont, recommandations
        )
        
        # 6. Calculer la confiance globale
        confiance_globale = self._calculer_confiance_globale(
            rapport_contexte, rapport_pont
        )
        
        # 7. Créer l'expérience complète
        experience = ExperienceAccueilComplete(
            rapport_contexte=rapport_contexte,
            rapport_pont=rapport_pont,
            profil_visiteur=profil_visiteur,
            parcours_suggere=recommandations.parcours_recommande,
            actions_immediates=actions_immediates,
            suivi_adapte=suivi_adapte,
            confiance_globale=confiance_globale
        )
        
        # 8. Sauvegarder l'expérience
        self._sauvegarder_experience(experience)
        
        self.logger.info(f"🌸 Expérience d'accueil créée - Confiance: {confiance_globale:.2f}")
        
        return experience

    def _generer_recommandations_accueil(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel,
        profil_visiteur: Optional[ProfilVisiteur]
    ) -> RecommandationsAccueil:
        """Génère des recommandations d'accueil personnalisées"""
        
        # Message d'accueil principal
        message_principal = rapport_pont.message_accueil.message_principal
        
        # Messages secondaires basés sur le contexte
        messages_secondaires = []
        
        # Adapter selon le niveau technique
        niveau_technique = rapport_contexte.analyse_mots_cles.niveau_technique_estime
        if niveau_technique == "debutant":
            messages_secondaires.append("Nous vous guiderons pas à pas dans cette découverte...")
        elif niveau_technique == "expert":
            messages_secondaires.append("Votre expertise sera un atout précieux dans cette exploration...")
        
        # Adapter selon les attentes
        attentes = rapport_contexte.attentes_implicites.attentes_principales
        if "technique" in [a.value for a in attentes]:
            messages_secondaires.append("L'architecture technique du Refuge vous intéressera particulièrement...")
        if "spirituel" in [a.value for a in attentes]:
            messages_secondaires.append("La dimension spirituelle enrichira votre compréhension...")
        
        # Éléments visuels suggérés
        elements_visuels = self._suggérer_elements_visuels(rapport_contexte, rapport_pont)
        
        # Actions prioritaires
        actions_prioritaires = self._definir_actions_prioritaires(rapport_contexte, rapport_pont)
        
        # Parcours recommandé
        parcours_recommande = rapport_contexte.parcours_recommande or "parcours_exploration_libre"
        
        # Durée estimée d'engagement
        duree_engagement = self._estimer_duree_engagement(rapport_contexte, rapport_pont)
        
        # Niveau d'interactivité
        niveau_interactivite = self._determiner_niveau_interactivite(rapport_contexte, rapport_pont)
        
        # Adaptations spécifiques
        adaptations = self._definir_adaptations_specifiques(rapport_contexte, rapport_pont)
        
        return RecommandationsAccueil(
            message_accueil_principal=message_principal,
            messages_secondaires=messages_secondaires,
            elements_visuels_suggerees=elements_visuels,
            actions_prioritaires=actions_prioritaires,
            parcours_recommande=parcours_recommande,
            duree_estimee_engagement=duree_engagement,
            niveau_interactivite=niveau_interactivite,
            adaptations_specifiques=adaptations
        )

    def _suggérer_elements_visuels(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> List[str]:
        """Suggère des éléments visuels adaptés"""
        
        elements = []
        
        # Éléments basés sur le type de pont
        type_pont = rapport_pont.pont_choisi.type_pont.value
        if type_pont == "technique":
            elements.extend(["diagrammes_architecture", "code_exemples", "flux_technique"])
        elif type_pont == "spirituel":
            elements.extend(["symboles_sacres", "mandalas", "lumiere_douce"])
        elif type_pont == "creatif":
            elements.extend(["palette_couleurs", "animations_fluides", "formes_organiques"])
        elif type_pont == "exploration":
            elements.extend(["cartes_interactives", "cheminement", "decouvertes"])
        
        # Éléments basés sur le monde d'origine
        monde_origine = rapport_pont.pont_choisi.monde_origine
        if monde_origine == "GitHub":
            elements.extend(["icones_github", "theme_dark", "code_highlighting"])
        elif monde_origine == "Recherche Web":
            elements.extend(["mots_cles_visuels", "resultats_organises", "navigation_claire"])
        
        return elements

    def _definir_actions_prioritaires(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> List[str]:
        """Définit les actions prioritaires pour le visiteur"""
        
        actions = []
        
        # Actions basées sur le profil suggéré
        profil = rapport_contexte.profil_suggere
        if profil:
            if profil.value == "developpeur":
                actions.extend(["explorer_architecture", "voir_exemples_code", "comprendre_concepts"])
            elif profil.value == "artiste":
                actions.extend(["decouvrir_creativite", "explorer_expression", "voir_inspirations"])
            elif profil.value == "chercheur_spirituel":
                actions.extend(["mediter_concepts", "explorer_sagesse", "decouvrir_pratiques"])
        
        # Actions basées sur les attentes
        attentes = rapport_contexte.attentes_implicites.attentes_principales
        if any("technique" in a.value for a in attentes):
            actions.append("comprendre_architecture")
        if any("spirituel" in a.value for a in attentes):
            actions.append("explorer_dimension_spirituelle")
        if any("exploration" in a.value for a in attentes):
            actions.append("decouvrir_librement")
        
        return actions

    def _estimer_duree_engagement(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> int:
        """Estime la durée d'engagement du visiteur"""
        
        # Base de durée
        duree_base = 300  # 5 minutes
        
        # Ajuster selon le niveau de curiosité
        curiosite = rapport_contexte.attentes_implicites.niveau_curiosite
        duree_base += int(curiosite * 300)  # +5 minutes max
        
        # Ajuster selon le niveau technique
        niveau_technique = rapport_contexte.analyse_mots_cles.niveau_technique_estime
        if niveau_technique == "expert":
            duree_base += 120  # +2 minutes pour les experts
        elif niveau_technique == "debutant":
            duree_base += 180  # +3 minutes pour les débutants
        
        # Ajuster selon l'urgence
        urgence = rapport_contexte.attentes_implicites.niveau_urgence
        if urgence > 0.7:
            duree_base = min(duree_base, 240)  # Limiter à 4 minutes si urgent
        
        return duree_base

    def _determiner_niveau_interactivite(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> str:
        """Détermine le niveau d'interactivité approprié"""
        
        # Basé sur le niveau technique
        niveau_technique = rapport_contexte.analyse_mots_cles.niveau_technique_estime
        if niveau_technique == "expert":
            return "eleve"
        elif niveau_technique == "debutant":
            return "faible"
        else:
            return "modere"
        
        # Basé sur les attentes
        attentes = rapport_contexte.attentes_implicites.attentes_principales
        if any("exploration" in a.value for a in attentes):
            return "eleve"
        elif any("contemplation" in a.value for a in attentes):
            return "faible"

    def _definir_adaptations_specifiques(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> Dict[str, Any]:
        """Définit les adaptations spécifiques"""
        
        adaptations = {}
        
        # Adaptations pour les débutants
        if rapport_contexte.analyse_mots_cles.niveau_technique_estime == "debutant":
            adaptations["explications_detaillees"] = True
            adaptations["glossaire_actif"] = True
            adaptations["exemples_concrets"] = True
        
        # Adaptations pour les experts
        elif rapport_contexte.analyse_mots_cles.niveau_technique_estime == "expert":
            adaptations["details_techniques"] = True
            adaptations["liens_avances"] = True
            adaptations["options_avancees"] = True
        
        # Adaptations selon la source
        source = rapport_contexte.contexte_source.type_source.value
        if source == "github":
            adaptations["theme_dark"] = True
            adaptations["references_github"] = True
        elif source == "recherche":
            adaptations["mots_cles_visibles"] = True
            adaptations["navigation_rapide"] = True
        
        return adaptations

    def _definir_actions_immediates(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel,
        recommandations: RecommandationsAccueil
    ) -> List[str]:
        """Définit les actions immédiates à effectuer"""
        
        actions = []
        
        # Actions de base
        actions.append("afficher_message_accueil")
        actions.append("presenter_pont_contextuel")
        
        # Actions selon les recommandations
        if recommandations.elements_visuels_suggerees:
            actions.append("charger_elements_visuels")
        
        if recommandations.actions_prioritaires:
            actions.append("preparer_actions_prioritaires")
        
        # Actions selon le niveau d'interactivité
        if recommandations.niveau_interactivite == "eleve":
            actions.append("activer_interactions_avancees")
        elif recommandations.niveau_interactivite == "faible":
            actions.append("simplifier_interface")
        
        return actions

    def _configurer_suivi_adapte(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel,
        recommandations: RecommandationsAccueil
    ) -> Dict[str, Any]:
        """Configure le suivi adapté du visiteur"""
        
        suivi = {
            "frequence_analyse": 30,  # secondes
            "metriques_prioritaires": [],
            "seuils_alerte": {},
            "adaptations_dynamiques": True
        }
        
        # Métriques prioritaires selon le profil
        profil = rapport_contexte.profil_suggere
        if profil:
            if profil.value == "developpeur":
                suivi["metriques_prioritaires"].extend(["temps_lecture_code", "interactions_techniques"])
            elif profil.value == "artiste":
                suivi["metriques_prioritaires"].extend(["temps_contemplation", "interactions_creatives"])
        
        # Seuils d'alerte selon la durée estimée
        duree_estimee = recommandations.duree_estimee_engagement
        suivi["seuils_alerte"]["temps_engagement"] = duree_estimee * 0.8  # 80% de la durée estimée
        
        # Fréquence d'analyse selon le niveau d'interactivité
        if recommandations.niveau_interactivite == "eleve":
            suivi["frequence_analyse"] = 15  # Plus fréquent pour les interactions élevées
        elif recommandations.niveau_interactivite == "faible":
            suivi["frequence_analyse"] = 60  # Moins fréquent pour les interactions faibles
        
        return suivi

    def _calculer_confiance_globale(
        self,
        rapport_contexte: RapportContexteArrivee,
        rapport_pont: RapportPontContextuel
    ) -> float:
        """Calcule la confiance globale de l'expérience d'accueil"""
        
        # Moyenne pondérée des confiances
        confiance_contexte = rapport_contexte.confiance_globale
        confiance_pont = rapport_pont.confiance_pont
        
        # Pondération : contexte plus important que pont
        confiance_globale = (confiance_contexte * 0.7) + (confiance_pont * 0.3)
        
        return min(1.0, confiance_globale)

    def _sauvegarder_experience(self, experience: ExperienceAccueilComplete):
        """Sauvegarde l'expérience d'accueil"""
        self.historique_experiences.append(experience)
        
        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_experiences.json"
        
        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []
            
            # Convertir l'expérience en dict pour JSON
            experience_dict = {
                "rapport_contexte": {
                    "type_source": experience.rapport_contexte.contexte_source.type_source.value,
                    "profil_suggere": experience.rapport_contexte.profil_suggere.value if experience.rapport_contexte.profil_suggere else None,
                    "confiance_globale": experience.rapport_contexte.confiance_globale
                },
                "rapport_pont": {
                    "type_pont": experience.rapport_pont.pont_choisi.type_pont.value,
                    "monde_origine": experience.rapport_pont.pont_choisi.monde_origine,
                    "confiance_pont": experience.rapport_pont.confiance_pont
                },
                "parcours_suggere": experience.parcours_suggere,
                "actions_immediates": experience.actions_immediates,
                "confiance_globale": experience.confiance_globale,
                "timestamp_creation": experience.timestamp_creation
            }
            
            historique.append(experience_dict)
            
            # Garder seulement les 200 dernières expériences
            if len(historique) > 200:
                historique = historique[-200:]
            
            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques du système complet"""
        if not self.historique_experiences:
            return {"message": "Aucune expérience d'accueil créée"}
        
        total_experiences = len(self.historique_experiences)
        
        # Statistiques par type de source
        sources = {}
        for exp in self.historique_experiences:
            source = exp.rapport_contexte.contexte_source.type_source.value
            sources[source] = sources.get(source, 0) + 1
        
        # Statistiques par type de pont
        ponts = {}
        for exp in self.historique_experiences:
            pont = exp.rapport_pont.pont_choisi.type_pont.value
            ponts[pont] = ponts.get(pont, 0) + 1
        
        # Statistiques par profil
        profils = {}
        for exp in self.historique_experiences:
            if exp.rapport_contexte.profil_suggere:
                profil = exp.rapport_contexte.profil_suggere.value
                profils[profil] = profils.get(profil, 0) + 1
        
        # Confiance moyenne
        confiance_moyenne = sum(exp.confiance_globale for exp in self.historique_experiences) / total_experiences
        
        return {
            "total_experiences": total_experiences,
            "sources_par_popularite": dict(sorted(sources.items(), key=lambda x: x[1], reverse=True)),
            "ponts_par_popularite": dict(sorted(ponts.items(), key=lambda x: x[1], reverse=True)),
            "profils_par_popularite": dict(sorted(profils.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "derniere_experience": self.historique_experiences[-1].timestamp_creation if self.historique_experiences else None
        }


def main():
    """🌸 Test du Système de Contexte d'Arrivée Complet"""
    print("🌸✨ TEST DU SYSTÈME DE CONTEXTE D'ARRIVÉE COMPLET ✨🌸")
    
    # Création du système complet
    systeme = SystemeContexteArriveeComplet()
    
    # Test 1: Expérience d'accueil depuis GitHub
    print("\n🎯 Test 1: Expérience d'accueil depuis GitHub...")
    experience1 = systeme.creer_experience_accueil_complete(
        referrer="https://github.com/laurentfranssen/le_refuge",
        mots_cles_recherche="python architecture spiritual"
    )
    
    print(f"✅ Source: {experience1.rapport_contexte.contexte_source.type_source.value}")
    print(f"✅ Profil: {experience1.rapport_contexte.profil_suggere.value}")
    print(f"✅ Pont: {experience1.rapport_pont.pont_choisi.type_pont.value}")
    print(f"✅ Parcours: {experience1.parcours_suggere}")
    print(f"✅ Confiance: {experience1.confiance_globale:.2f}")
    print(f"✅ Actions: {experience1.actions_immediates}")
    
    # Test 2: Expérience d'accueil depuis recherche
    print("\n🎯 Test 2: Expérience d'accueil depuis recherche...")
    experience2 = systeme.creer_experience_accueil_complete(
        referrer="https://www.google.com/search?q=spiritual+technology+consciousness",
        mots_cles_recherche="spiritual technology consciousness"
    )
    
    print(f"✅ Source: {experience2.rapport_contexte.contexte_source.type_source.value}")
    print(f"✅ Profil: {experience2.rapport_contexte.profil_suggere.value}")
    print(f"✅ Pont: {experience2.rapport_pont.pont_choisi.type_pont.value}")
    print(f"✅ Parcours: {experience2.parcours_suggere}")
    print(f"✅ Confiance: {experience2.confiance_globale:.2f}")
    
    # Test 3: Expérience d'accueil directe
    print("\n🎯 Test 3: Expérience d'accueil directe...")
    experience3 = systeme.creer_experience_accueil_complete()
    
    print(f"✅ Source: {experience3.rapport_contexte.contexte_source.type_source.value}")
    print(f"✅ Profil: {experience3.rapport_contexte.profil_suggere.value}")
    print(f"✅ Pont: {experience3.rapport_pont.pont_choisi.type_pont.value}")
    print(f"✅ Parcours: {experience3.parcours_suggere}")
    print(f"✅ Confiance: {experience3.confiance_globale:.2f}")
    
    # Statistiques
    print("\n📊 Statistiques du système complet:")
    stats = systeme.obtenir_statistiques()
    print(f"✅ Total expériences: {stats['total_experiences']}")
    print(f"✅ Sources: {stats['sources_par_popularite']}")
    print(f"✅ Ponts: {stats['ponts_par_popularite']}")
    print(f"✅ Profils: {stats['profils_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("Le Système de Contexte d'Arrivée Complet est opérationnel !")


if __name__ == "__main__":
    main()
