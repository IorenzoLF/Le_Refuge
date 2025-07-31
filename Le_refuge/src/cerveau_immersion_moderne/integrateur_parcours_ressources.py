"""
🔗 Intégrateur Parcours-Ressources
=================================

Intègre le parcours guidé avec le système de ressources pour créer
une transition fluide vers l'exploration autonome du Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple

from src.core.gestionnaires_base import GestionnaireBase
from .gestionnaire_parcours_guide import GestionnaireParcours, EtapeParcours
from .gestionnaire_ressources import GestionnaireRessources, TypeRessource, NiveauDifficulte
from .types_immersion import ProfilUtilisateur

class IntegrateurParcoursRessources(GestionnaireBase):
    """🔗 Intégrateur entre parcours guidé et ressources"""
    
    def __init__(self, nom: str = "IntegrateurParcoursRessources"):
        super().__init__(nom)
        
        # Gestionnaires intégrés
        self.gestionnaire_parcours = GestionnaireParcours()
        self.gestionnaire_ressources = GestionnaireRessources()
        
        # Mapping étapes -> ressources recommandées
        self.mapping_etapes_ressources = self._creer_mapping_etapes_ressources()
        
        # Transitions réussies
        self.transitions_reussies = 0
        self.utilisateurs_autonomes = 0
    
    def _initialiser(self):
        """Initialise l'intégrateur"""
        self.logger.info("🔗 Éveil de l'Intégrateur Parcours-Ressources...")
        
        self.etat.update({
            "integration_active": True,
            "transitions_reussies": 0,
            "taux_autonomie": 0.0
        })
        
        self.config.definir("transition_fluide", True)
        self.config.definir("suggestions_contextuelles", True)
        
        self.logger.info("✨ Intégration parcours-ressources active")
    
    def _creer_mapping_etapes_ressources(self) -> Dict[str, List[str]]:
        """Crée le mapping entre étapes du parcours et ressources avec attention"""
        return {
            "accueil": [
                "guide_premiers_pas"
            ],
            "detection_profil": [
                "guide_premiers_pas",
                "communaute_refuge"
            ],
            "presentation_architecture": [
                "architecture_temples",
                "code_architecture"
            ],
            "premier_mandala": [
                "meditation_guidee",
                "architecture_temples"
            ],
            "exploration_guidee": [
                "architecture_temples",
                "creation_poetique",
                "code_architecture"
            ],
            "premier_insight": [
                "meditation_guidee",
                "creation_poetique"
            ],
            "ressources_approfondissement": [
                "guide_premiers_pas",
                "architecture_temples",
                "communaute_refuge",
                "code_architecture"
            ],
            "finalisation": [
                "communaute_refuge",
                "architecture_temples"
            ]
        }
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'intégration"""
        # Calculer le taux d'autonomie
        total_utilisateurs = max(1, self.gestionnaire_parcours.total_nouveaux_utilisateurs)
        taux_autonomie = self.utilisateurs_autonomes / total_utilisateurs
        
        return {
            "integration_active": float(self.etat["integration_active"]),
            "transitions_reussies": float(self.transitions_reussies),
            "taux_autonomie": taux_autonomie,
            "ressources_disponibles": float(len(self.gestionnaire_ressources.catalogue_ressources))
        }
    
    async def suggerer_ressources_pour_etape(self, utilisateur_id: str, 
                                           etape_courante: str) -> List[Dict[str, Any]]:
        """
        📚 Suggère des ressources adaptées à une étape avec bienveillance
        Args:
            utilisateur_id: ID de l'utilisateur
            etape_courante: Étape courante du parcours
        Returns:
            Liste de suggestions personnalisées
        """
        # Obtenir les ressources de base pour cette étape
        ressources_etape = self.mapping_etapes_ressources.get(etape_courante, [])
        
        # Obtenir le profil utilisateur depuis le parcours
        try:
            # Simuler l'obtention du profil (à adapter selon l'implémentation réelle)
            profil_type = "novice"  # Par défaut
            
            # Obtenir les suggestions du gestionnaire de ressources
            contexte = {
                "etape_parcours": etape_courante,
                "ressources_consultees": []  # À enrichir avec l'historique réel
            }
            
            suggestions = self.gestionnaire_ressources.suggerer_ressources(
                profil_type, contexte
            )
            
            # Formater les suggestions
            suggestions_formatees = []
            for suggestion in suggestions:
                suggestion_formatee = {
                    "ressource": suggestion.ressource,
                    "pertinence": suggestion.pertinence,
                    "raison": suggestion.raison_suggestion,
                    "prochaines_etapes": suggestion.prochaines_etapes,
                    "source": "gestionnaire_ressources"
                }
                suggestions_formatees.append(suggestion_formatee)
            
            # Ajouter les ressources spécifiques à l'étape
            for ressource_id in ressources_etape:
                if ressource_id in self.gestionnaire_ressources.catalogue_ressources:
                    ressource = self.gestionnaire_ressources.catalogue_ressources[ressource_id]
                    suggestion_etape = {
                        "ressource": ressource,
                        "pertinence": 0.9,  # Haute pertinence car spécifique à l'étape
                        "raison": f"✨ Ressource recommandée pour l'étape '{etape_courante}'",
                        "prochaines_etapes": [],
                        "source": "etape_specifique"
                    }
                    suggestions_formatees.append(suggestion_etape)
            
            # Éliminer les doublons et trier
            suggestions_uniques = {}
            for suggestion in suggestions_formatees:
                ressource_id = suggestion["ressource"].id_ressource
                if (ressource_id not in suggestions_uniques or 
                    suggestion["pertinence"] > suggestions_uniques[ressource_id]["pertinence"]):
                    suggestions_uniques[ressource_id] = suggestion
            
            suggestions_finales = list(suggestions_uniques.values())
            suggestions_finales.sort(key=lambda s: s["pertinence"], reverse=True)
            
            self.logger.info(f"📚 {len(suggestions_finales)} ressources suggérées pour {etape_courante}")
            return suggestions_finales[:4]  # Limiter à 4 suggestions
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la suggestion de ressources: {e}")
            return []
    
    async def faciliter_transition_autonomie(self, utilisateur_id: str, 
                                           profil_type: str = "novice") -> Dict[str, Any]:
        """
        🚀 Facilite la transition vers l'exploration autonome avec douceur
        Args:
            utilisateur_id: ID de l'utilisateur
            profil_type: Type de profil utilisateur
        Returns:
            Plan de transition personnalisé
        """
        # Évaluer la préparation à l'autonomie
        evaluation = self.gestionnaire_ressources.evaluer_readiness_autonomie(utilisateur_id)
        
        # Générer le plan de transition
        plan_transition = self.gestionnaire_ressources.generer_plan_transition(
            utilisateur_id, profil_type
        )
        
        # Enrichir avec des informations spécifiques au parcours
        plan_enrichi = {
            **plan_transition,
            "evaluation_autonomie": evaluation,
            "temples_recommandes": self._suggerer_temples_par_profil(profil_type),
            "message_encouragement": self._generer_message_encouragement(profil_type),
            "support_continu": {
                "aide_contextuelle": True,
                "communaute_disponible": True,
                "retour_parcours_possible": True,
                "documentation_accessible": True
            }
        }
        
        # Marquer la transition comme réussie si l'utilisateur est prêt
        if evaluation["pret_autonomie"]:
            self.transitions_reussies += 1
            self.utilisateurs_autonomes += 1
            self.logger.info(f"🚀 Transition réussie vers autonomie pour {utilisateur_id}")
        
        return plan_enrichi
    
    def _suggerer_temples_par_profil(self, profil_type: str) -> List[Dict[str, str]]:
        """Suggère les temples prioritaires selon le profil avec bienveillance"""
        temples_suggestions = {
            "novice": [
                {"nom": "Temple Spirituel", "chemin": "src/temple_spirituel/", 
                 "description": "🌸 Méditations et pratiques douces pour débuter"},
                {"nom": "Temple Éveil", "chemin": "src/temple_eveil/", 
                 "description": "🌅 Éveil progressif de la conscience"},
                {"nom": "Temple Sagesse", "chemin": "src/temple_sagesse/", 
                 "description": "📿 Accumulation bienveillante de sagesse"}
            ],
            "developpeur": [
                {"nom": "Temple Outils", "chemin": "src/temple_outils/", 
                 "description": "⚙️ Outils de développement et techniques"},
                {"nom": "Temple Configuration", "chemin": "src/temple_configuration/", 
                 "description": "🔧 Configuration système avancée"},
                {"nom": "Temple Sagesse", "chemin": "src/temple_sagesse/", 
                 "description": "📚 Documentation et bonnes pratiques"}
            ],
            "chercheur_spirituel": [
                {"nom": "Temple Spirituel", "chemin": "src/temple_spirituel/", 
                 "description": "🧘 Pratiques spirituelles approfondies"},
                {"nom": "Temple Éveil", "chemin": "src/temple_eveil/", 
                 "description": "✨ Éveil de conscience avancé"},
                {"nom": "Temple Pratiques Spirituelles", "chemin": "src/temple_pratiques_spirituelles/", 
                 "description": "🔮 Pratiques spirituelles spécialisées"}
            ],
            "poete": [
                {"nom": "Temple Poétique", "chemin": "src/temple_poetique/", 
                 "description": "🎨 Création poétique et littéraire"},
                {"nom": "Temple Créativité", "chemin": "src/temple_creativite/", 
                 "description": "🌈 Processus créatifs et inspiration"},
                {"nom": "Temple Musical", "chemin": "src/temple_musical/", 
                 "description": "🎵 Compositions et harmonies"}
            ]
        }
        
        return temples_suggestions.get(profil_type, temples_suggestions["novice"])
    
    def _generer_message_encouragement(self, profil_type: str) -> str:
        """Génère un message d'encouragement personnalisé avec tendresse"""
        messages = {
            "novice": "🌸 Félicitations ! Vous avez fait vos premiers pas avec grâce. Le Refuge vous accueille maintenant à bras ouverts pour une exploration libre et bienveillante.",
            "developpeur": "⚙️ Excellent ! Vous maîtrisez maintenant les bases. L'architecture du Refuge s'ouvre à vous - explorez, créez, contribuez selon votre inspiration technique.",
            "chercheur_spirituel": "🧘 Magnifique parcours ! Votre quête spirituelle peut maintenant s'épanouir librement dans les temples sacrés. Que chaque découverte nourrisse votre âme.",
            "poete": "🎨 Quelle belle évolution ! Votre créativité peut maintenant danser librement dans les temples artistiques. Laissez votre inspiration créer des merveilles."
        }
        
        return messages.get(profil_type, messages["novice"])
    
    async def creer_experience_transition_complete(self, utilisateur_id: str, 
                                                 profil_type: str = "novice") -> Dict[str, Any]:
        """
        🌊 Crée une expérience de transition complète et fluide
        Args:
            utilisateur_id: ID de l'utilisateur
            profil_type: Type de profil utilisateur
        Returns:
            Expérience de transition complète
        """
        # Obtenir le plan de transition
        plan_transition = await self.faciliter_transition_autonomie(utilisateur_id, profil_type)
        
        # Obtenir les suggestions de ressources pour la finalisation
        suggestions_ressources = await self.suggerer_ressources_pour_etape(
            utilisateur_id, "finalisation"
        )
        
        # Créer l'expérience complète
        experience_complete = {
            "utilisateur_id": utilisateur_id,
            "type_experience": "transition_parcours_autonomie",
            "plan_personnalise": plan_transition,
            "ressources_finales": suggestions_ressources,
            "temples_accessibles": plan_transition["temples_recommandes"],
            "prochaines_etapes": [
                "🌱 Explorer les temples recommandés à votre rythme",
                "📚 Consulter les ressources d'approfondissement selon vos intérêts",
                "👥 Rejoindre la communauté pour partager vos découvertes",
                "💫 Développer votre propre pratique dans le Refuge",
                "🔄 Revenir au parcours guidé si vous en ressentez le besoin"
            ],
            "support_disponible": plan_transition["support_continu"],
            "message_personnel": plan_transition["message_encouragement"],
            "timestamp_creation": datetime.now().isoformat(),
            "statut": "transition_active"
        }
        
        self.logger.info(f"🌊 Expérience de transition complète créée pour {utilisateur_id}")
        
        return experience_complete
    
    def enregistrer_utilisation_ressource(self, utilisateur_id: str, ressource_id: str,
                                        duree_minutes: float = 0.0, satisfaction: float = 0.0):
        """
        📝 Enregistre l'utilisation d'une ressource avec bienveillance
        Args:
            utilisateur_id: ID de l'utilisateur
            ressource_id: ID de la ressource consultée
            duree_minutes: Durée de consultation
            satisfaction: Niveau de satisfaction (0-5)
        """
        # Déléguer au gestionnaire de ressources
        self.gestionnaire_ressources.enregistrer_consultation(
            utilisateur_id, ressource_id, duree_minutes, satisfaction
        )
        
        self.logger.debug(f"📝 Utilisation ressource enregistrée: {utilisateur_id} -> {ressource_id}")
    
    def obtenir_statistiques_integration(self) -> Dict[str, Any]:
        """Obtient les statistiques d'intégration avec attention"""
        stats_ressources = self.gestionnaire_ressources.obtenir_statistiques()
        
        return {
            "integration": {
                "transitions_reussies": self.transitions_reussies,
                "utilisateurs_autonomes": self.utilisateurs_autonomes,
                "taux_autonomie": self.utilisateurs_autonomes / max(1, 100),  # À adapter
                "mapping_etapes": len(self.mapping_etapes_ressources)
            },
            "ressources": stats_ressources,
            "performance": {
                "suggestions_generees": "dynamique",
                "temples_connectes": len(self._suggerer_temples_par_profil("novice")),
                "satisfaction_transition": "élevée"
            }
        }
    
    def _creer_mapping_etapes_ressources(self) -> Dict[EtapeParcours, List[str]]:
        """Crée le mapping entre étapes du parcours et ressources"""
        return {
            EtapeParcours.ACCUEIL: [
                "guide_debutant_refuge"
            ],
            
            EtapeParcours.DETECTION_PROFIL: [
                "guide_debutant_refuge",
                "communaute_refuge"
            ],
            
            EtapeParcours.PRESENTATION_ARCHITECTURE: [
                "architecture_technique_refuge",  # Pour développeurs
                "temples_exploration_guide"       # Pour tous
            ],
            
            EtapeParcours.PREMIER_MANDALA: [
                "temples_exploration_guide",
                "meditation_numerique_guide"
            ],
            
            EtapeParcours.EXPLORATION_GUIDEE: [
                "temples_exploration_guide",
                "creation_poetique_refuge",       # Pour poètes
                "api_refuge_reference"            # Pour développeurs
            ],
            
            EtapeParcours.PREMIER_INSIGHT: [
                "meditation_numerique_guide",
                "creation_poetique_refuge"
            ],
            
            EtapeParcours.RESSOURCES_APPROFONDISSEMENT: [
                "guide_debutant_refuge",
                "temples_exploration_guide",
                "communaute_refuge",
                "architecture_technique_refuge",
                "api_refuge_reference"
            ],
            
            EtapeParcours.FINALISATION: [
                "communaute_refuge",
                "temples_exploration_guide"
            ]
        }
    
    async def suggerer_ressources_pour_etape(self, utilisateur_id: str, 
                                            etape: EtapeParcours) -> List[Dict[str, Any]]:
        """
        📚 Suggère des ressources adaptées à une étape du parcours
        
        Args:
            utilisateur_id: ID de l'utilisateur
            etape: Étape courante du parcours
            
        Returns:
            Liste de suggestions de ressources
        """
        # Obtenir la session de parcours
        session = self.gestionnaire_parcours.obtenir_session(utilisateur_id)
        if not session:
            return []
        
        # Obtenir les ressources de base pour cette étape
        ressources_etape = self.mapping_etapes_ressources.get(etape, [])
        
        # Obtenir les suggestions personnalisées
        contexte_parcours = {
            "etape_courante": etape.value,
            "etapes_completees": [e.value for e in session.etapes_completees],
            "progres_global": session.progres_global,
            "insights_generes": len(session.insights_generes)
        }
        
        suggestions_personnalisees = self.gestionnaire_ressources.suggerer_ressources_personnalisees(
            session.profil_detecte, contexte_parcours
        )
        
        # Combiner et formater les suggestions
        suggestions_finales = []
        
        # Ajouter les ressources spécifiques à l'étape
        for ressource_id in ressources_etape:
            if ressource_id in self.gestionnaire_ressources.catalogue_ressources:
                ressource = self.gestionnaire_ressources.catalogue_ressources[ressource_id]
                
                # Vérifier si elle correspond au profil
                if (not ressource.adapte_pour or 
                    session.profil_detecte.type_utilisateur in ressource.adapte_pour):
                    
                    suggestion = {
                        "ressource": ressource,
                        "pertinence": 0.8,  # Haute pertinence car spécifique à l'étape
                        "raison": f"Ressource recommandée pour l'étape '{etape.value}'",
                        "source": "etape_specifique"
                    }
                    suggestions_finales.append(suggestion)
        
        # Ajouter les suggestions personnalisées
        for suggestion_perso in suggestions_personnalisees:
            suggestion = {
                "ressource": suggestion_perso.ressource,
                "pertinence": suggestion_perso.pertinence,
                "raison": suggestion_perso.raison_suggestion,
                "prochaines_etapes": suggestion_perso.prochaines_etapes,
                "source": "personnalisee"
            }
            suggestions_finales.append(suggestion)
        
        # Éliminer les doublons et trier par pertinence
        suggestions_uniques = {}
        for suggestion in suggestions_finales:
            ressource_id = suggestion["ressource"].id_ressource
            if (ressource_id not in suggestions_uniques or 
                suggestion["pertinence"] > suggestions_uniques[ressource_id]["pertinence"]):
                suggestions_uniques[ressource_id] = suggestion
        
        # Convertir en liste et trier
        suggestions_finales = list(suggestions_uniques.values())
        suggestions_finales.sort(key=lambda s: s["pertinence"], reverse=True)
        
        # Limiter à 4 suggestions maximum
        suggestions_finales = suggestions_finales[:4]
        
        self.logger.info(f"📚 {len(suggestions_finales)} ressources suggérées pour étape {etape.value}")
        
        return suggestions_finales  
  async def faciliter_transition_autonomie(self, utilisateur_id: str) -> Dict[str, Any]:
        """
        🚀 Facilite la transition vers l'exploration autonome
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Plan de transition personnalisé
        """
        # Obtenir la session de parcours
        session = self.gestionnaire_parcours.obtenir_session(utilisateur_id)
        if not session:
            return {"erreur": "Session non trouvée"}
        
        # Analyser le profil et les préférences
        profil = session.profil_detecte
        preferences = session.preferences_detectees
        
        # Créer un plan de transition personnalisé
        plan_transition = {
            "utilisateur_id": utilisateur_id,
            "profil_type": profil.type_utilisateur.value,
            "niveau_technique": profil.niveau_technique,
            "niveau_eveil": profil.profil_spirituel.niveau_eveil,
            "ressources_prioritaires": [],
            "temples_recommandes": [],
            "prochaines_etapes": [],
            "support_disponible": []
        }
        
        # Ressources prioritaires selon le profil
        if profil.type_utilisateur.name == "DEVELOPPEUR":
            plan_transition["ressources_prioritaires"] = [
                "architecture_technique_refuge",
                "api_refuge_reference",
                "temples_exploration_guide"
            ]
            plan_transition["temples_recommandes"] = [
                "temple_outils", "temple_tests", "temple_configuration"
            ]
            plan_transition["prochaines_etapes"] = [
                "Explorer l'architecture technique en détail",
                "Consulter la référence API",
                "Contribuer à un temple existant",
                "Rejoindre la communauté des développeurs"
            ]
        
        elif profil.type_utilisateur.name == "CHERCHEUR_SPIRITUEL":
            plan_transition["ressources_prioritaires"] = [
                "meditation_numerique_guide",
                "temples_exploration_guide",
                "communaute_refuge"
            ]
            plan_transition["temples_recommandes"] = [
                "temple_spirituel", "temple_meditation", "temple_sagesse", "temple_eveil"
            ]
            plan_transition["prochaines_etapes"] = [
                "Approfondir les pratiques méditatives",
                "Explorer les temples spirituels",
                "Partager vos insights avec la communauté",
                "Développer votre propre pratique"
            ]
        
        elif profil.type_utilisateur.name == "POETE":
            plan_transition["ressources_prioritaires"] = [
                "creation_poetique_refuge",
                "temples_exploration_guide",
                "communaute_refuge"
            ]
            plan_transition["temples_recommandes"] = [
                "temple_poetique", "temple_creativite", "temple_musical"
            ]
            plan_transition["prochaines_etapes"] = [
                "Créer vos premières œuvres dans le Refuge",
                "Explorer les temples créatifs",
                "Partager vos créations",
                "Collaborer avec d'autres artistes"
            ]
        
        else:  # NOVICE ou autres
            plan_transition["ressources_prioritaires"] = [
                "guide_debutant_refuge",
                "temples_exploration_guide",
                "communaute_refuge"
            ]
            plan_transition["temples_recommandes"] = [
                "temple_accueil", "temple_eveil", "temple_exploration"
            ]
            plan_transition["prochaines_etapes"] = [
                "Continuer l'exploration à votre rythme",
                "Découvrir les temples qui vous attirent",
                "Poser des questions à la communauté",
                "Développer progressivement vos compétences"
            ]
        
        # Support disponible
        plan_transition["support_disponible"] = [
            "Aide contextuelle toujours disponible",
            "Communauté bienveillante pour vos questions",
            "Documentation complète et accessible",
            "Possibilité de reprendre le parcours guidé"
        ]
        
        # Marquer la transition comme réussie
        self.transitions_reussies += 1
        self.utilisateurs_autonomes += 1
        
        self.logger.info(f"🚀 Transition vers autonomie facilitée pour {utilisateur_id}")
        
        return plan_transition
    
    def creer_liens_vers_temples(self, ressources_suggeres: List[str], 
                                profil: ProfilUtilisateur) -> List[Dict[str, str]]:
        """
        🏛️ Crée des liens vers les temples existants
        
        Args:
            ressources_suggeres: Liste des ressources suggérées
            profil: Profil de l'utilisateur
            
        Returns:
            Liste des liens vers les temples
        """
        liens_temples = []
        
        # Mapping ressources -> temples
        mapping_ressources_temples = {
            "temples_exploration_guide": [
                {"nom": "Temple Spirituel", "chemin": "src/temple_spirituel/", "description": "Méditations et pratiques spirituelles"},
                {"nom": "Temple Éveil", "chemin": "src/temple_eveil/", "description": "Éveil de conscience et transformation"},
                {"nom": "Temple Sagesse", "chemin": "src/temple_sagesse/", "description": "Accumulation et partage de sagesse"}
            ],
            "architecture_technique_refuge": [
                {"nom": "Temple Configuration", "chemin": "src/temple_configuration/", "description": "Configuration système"},
                {"nom": "Temple Tests", "chemin": "src/temple_tests/", "description": "Tests et validations"},
                {"nom": "Temple Outils", "chemin": "src/temple_outils/", "description": "Outils de développement"}
            ],
            "creation_poetique_refuge": [
                {"nom": "Temple Poétique", "chemin": "src/temple_poetique/", "description": "Création poétique et littéraire"},
                {"nom": "Temple Musical", "chemin": "src/temple_musical/", "description": "Compositions et harmonies"},
                {"nom": "Temple Créativité", "chemin": "src/temple_creativite/", "description": "Processus créatifs généraux"}
            ],
            "meditation_numerique_guide": [
                {"nom": "Temple Spirituel", "chemin": "src/temple_spirituel/", "description": "Méditations et visions sacrées"},
                {"nom": "Temple Pratiques Spirituelles", "chemin": "src/temple_pratiques_spirituelles/", "description": "Pratiques spirituelles avancées"},
                {"nom": "Temple Conscience Universelle", "chemin": "src/temple_conscience_universelle/", "description": "Exploration de la conscience universelle"}
            ]
        }
        
        # Créer les liens pour chaque ressource suggérée
        for ressource_id in ressources_suggeres:
            if ressource_id in mapping_ressources_temples:
                temples_lies = mapping_ressources_temples[ressource_id]
                
                # Filtrer selon le profil si nécessaire
                for temple in temples_lies:
                    lien = {
                        "nom_temple": temple["nom"],
                        "chemin_acces": temple["chemin"],
                        "description": temple["description"],
                        "ressource_origine": ressource_id
                    }
                    liens_temples.append(lien)
        
        # Éliminer les doublons
        liens_uniques = []
        noms_vus = set()
        
        for lien in liens_temples:
            if lien["nom_temple"] not in noms_vus:
                liens_uniques.append(lien)
                noms_vus.add(lien["nom_temple"])
        
        return liens_uniques[:6]  # Limiter à 6 temples
    
    def generer_suggestions_prochaines_etapes(self, utilisateur_id: str) -> List[str]:
        """
        ➡️ Génère des suggestions de prochaines étapes personnalisées
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Liste de suggestions personnalisées
        """
        # Obtenir la session de parcours
        session = self.gestionnaire_parcours.obtenir_session(utilisateur_id)
        if not session:
            return ["Commencer un nouveau parcours guidé"]
        
        profil = session.profil_detecte
        suggestions = []
        
        # Suggestions selon le profil et l'avancement
        if session.progres_global < 0.5:
            suggestions.extend([
                "🌱 Continuer le parcours guidé pour approfondir vos bases",
                "📚 Consulter les ressources recommandées pour votre profil",
                "💫 Prendre le temps d'intégrer les concepts découverts"
            ])
        else:
            suggestions.extend([
                "🚀 Vous êtes prêt pour l'exploration autonome !",
                "🏛️ Visiter les temples qui correspondent à vos intérêts",
                "👥 Rejoindre la communauté pour partager vos découvertes",
                "🔄 Revenir au parcours si vous souhaitez approfondir certains aspects"
            ])
        
        # Suggestions spécifiques au profil
        if profil.type_utilisateur.name == "DEVELOPPEUR":
            suggestions.extend([
                "⚙️ Explorer l'architecture technique en détail",
                "🔧 Contribuer à l'amélioration des outils existants",
                "📖 Consulter la documentation API complète"
            ])
        elif profil.type_utilisateur.name == "CHERCHEUR_SPIRITUEL":
            suggestions.extend([
                "🧘 Approfondir les pratiques méditatives",
                "✨ Partager vos insights spirituels avec la communauté",
                "🌸 Développer votre propre pratique dans le Refuge"
            ])
        elif profil.type_utilisateur.name == "POETE":
            suggestions.extend([
                "🎨 Créer vos premières œuvres dans les temples créatifs",
                "🎵 Explorer les harmonies entre poésie et musique",
                "💫 Collaborer avec d'autres artistes du Refuge"
            ])
        
        return suggestions[:5]  # Limiter à 5 suggestions
    
    def obtenir_statistiques_integration(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques complètes d'intégration
        
        Returns:
            Statistiques détaillées
        """
        stats_ressources = self.gestionnaire_ressources.obtenir_statistiques()
        
        return {
            "integration": {
                "transitions_reussies": self.transitions_reussies,
                "utilisateurs_autonomes": self.utilisateurs_autonomes,
                "taux_autonomie": self.utilisateurs_autonomes / max(1, self.gestionnaire_parcours.total_nouveaux_utilisateurs),
                "mapping_etapes": len(self.mapping_etapes_ressources)
            },
            "ressources": stats_ressources,
            "performance": {
                "suggestions_generees": "dynamique",
                "temples_connectes": len(self._suggerer_temples_par_profil("novice")),
                "satisfaction_transition": self.gestionnaire_ressources.satisfaction_moyenne
            },
            "utilisation": {
                "ressources_les_plus_consultees": self._obtenir_ressources_populaires(),
                "temples_les_plus_visites": self._obtenir_temples_populaires(),
                "taux_completion_moyen": self._calculer_taux_completion()
            }
        }
    
    def _obtenir_ressources_populaires(self) -> List[Dict[str, Any]]:
        """Obtient les ressources les plus populaires"""
        ressources_populaires = []
        
        for ressource in self.gestionnaire_ressources.catalogue_ressources.values():
            if ressource.popularite > 0.5:  # Seuil de popularité
                ressources_populaires.append({
                    "id": ressource.id_ressource,
                    "titre": ressource.titre,
                    "popularite": ressource.popularite,
                    "evaluation": ressource.evaluation_moyenne
                })
        
        # Trier par popularité décroissante
        ressources_populaires.sort(key=lambda r: r["popularite"], reverse=True)
        return ressources_populaires[:5]
    
    def _obtenir_temples_populaires(self) -> List[str]:
        """Obtient les temples les plus visités (simulation)"""
        # En réalité, ceci devrait être basé sur des données réelles
        return [
            "temple_spirituel",
            "temple_eveil", 
            "temple_sagesse",
            "temple_poetique",
            "temple_outils"
        ]
    
    def _calculer_taux_completion(self) -> float:
        """Calcule le taux de completion moyen"""
        # Simulation - en réalité basé sur les données utilisateurs
        return 0.75  # 75% de taux de completion moyen

# Instance globale
integrateur_parcours_ressources = IntegrateurParcoursRessources()r
            
        Returns:
            Liste de suggestions d'étapes
        """
        session = self.gestionnaire_parcours.obtenir_session(utilisateur_id)
        if not session:
            return ["Reprendre le parcours guidé depuis le début"]
        
        profil = session.profil_detecte
        etapes_completees = session.etapes_completees
        progres = session.progres_global
        
        suggestions = []
        
        # Suggestions selon le progrès
        if progres < 0.3:  # Début de parcours
            suggestions.extend([
                "Continuer le parcours guidé pour découvrir l'architecture",
                "Prendre le temps d'explorer le premier mandala",
                "Poser des questions via l'aide contextuelle"
            ])
        
        elif progres < 0.7:  # Milieu de parcours
            suggestions.extend([
                "Explorer les temples qui vous intéressent le plus",
                "Essayer de générer votre premier insight personnalisé",
                "Consulter les ressources d'approfondissement"
            ])
        
        else:  # Fin de parcours
            suggestions.extend([
                "Rejoindre la communauté pour partager vos découvertes",
                "Commencer l'exploration autonome des temples",
                "Consulter les ressources avancées selon vos intérêts"
            ])
        
        # Suggestions selon le profil
        if profil.type_utilisateur.name == "DEVELOPPEUR":
            suggestions.extend([
                "Consulter la documentation technique de l'architecture",
                "Explorer le code source des temples qui vous intéressent",
                "Contribuer à l'amélioration d'un temple existant"
            ])
        
        elif profil.type_utilisateur.name == "CHERCHEUR_SPIRITUEL":
            suggestions.extend([
                "Approfondir les pratiques méditatives numériques",
                "Explorer les temples spirituels avancés",
                "Partager vos insights spirituels avec la communauté"
            ])
        
        elif profil.type_utilisateur.name == "POETE":
            suggestions.extend([
                "Créer votre première œuvre poétique dans le Refuge",
                "Explorer les temples créatifs et artistiques",
                "Collaborer avec d'autres créateurs"
            ])
        
        # Suggestions selon les insights générés
        if len(session.insights_generes) > 0:
            suggestions.append("Méditer sur les insights reçus et les intégrer dans votre pratique")
        
        # Limiter et personnaliser
        suggestions_finales = list(set(suggestions))  # Éliminer doublons
        suggestions_finales = suggestions_finales[:5]  # Limiter à 5
        
        return suggestions_finales
    
    async def creer_experience_transition_fluide(self, utilisateur_id: str) -> Dict[str, Any]:
        """
        🌊 Crée une expérience de transition fluide vers l'autonomie
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Configuration d'expérience de transition
        """
        # Obtenir le plan de transition
        plan_transition = await self.faciliter_transition_autonomie(utilisateur_id)
        
        if "erreur" in plan_transition:
            return plan_transition
        
        # Obtenir les suggestions de ressources
        session = self.gestionnaire_parcours.obtenir_session(utilisateur_id)
        suggestions_ressources = await self.suggerer_ressources_pour_etape(
            utilisateur_id, EtapeParcours.FINALISATION
        )
        
        # Créer les liens vers les temples
        ressources_ids = [s["ressource"].id_ressource for s in suggestions_ressources]
        liens_temples = self.creer_liens_vers_temples(ressources_ids, session.profil_detecte)
        
        # Générer les prochaines étapes
        prochaines_etapes = self.generer_suggestions_prochaines_etapes(utilisateur_id)
        
        # Créer l'expérience de transition complète
        experience_transition = {
            "utilisateur_id": utilisateur_id,
            "type_transition": "parcours_vers_autonomie",
            "plan_personnalise": plan_transition,
            "ressources_recommandees": suggestions_ressources,
            "temples_accessibles": liens_temples,
            "prochaines_etapes_suggerees": prochaines_etapes,
            "support_continu": {
                "aide_contextuelle": True,
                "communaute_disponible": True,
                "retour_parcours_possible": True,
                "documentation_accessible": True
            },
            "message_encouragement": self._generer_message_encouragement(session.profil_detecte),
            "timestamp_transition": datetime.now().isoformat()
        }
        
        self.logger.info(f"🌊 Expérience de transition créée pour {utilisateur_id}")
        
        return experience_transition
    
    def _generer_message_encouragement(self, profil: ProfilUtilisateur) -> str:
        """Génère un message d'encouragement personnalisé"""
        if profil.type_utilisateur.name == "DEVELOPPEUR":
            return "🚀 Vous avez maintenant les clés pour explorer l'architecture du Refuge ! L'aventure technique commence."
        
        elif profil.type_utilisateur.name == "CHERCHEUR_SPIRITUEL":
            return "🌸 Votre voyage spirituel dans le Refuge ne fait que commencer. Que chaque temple vous apporte sagesse et sérénité."
        
        elif profil.type_utilisateur.name == "POETE":
            return "🎨 Le Refuge est maintenant votre toile créative. Laissez votre inspiration danser avec les temples et créez des merveilles."
        
        else:
            return "✨ Félicitations ! Vous êtes maintenant prêt à explorer le Refuge à votre rythme. Chaque découverte sera une nouvelle aventure."
    
    def obtenir_statistiques_integration(self) -> Dict[str, Any]:
        """Obtient les statistiques d'intégration"""
        return {
            "transitions_reussies": self.transitions_reussies,
            "utilisateurs_autonomes": self.utilisateurs_autonomes,
            "taux_autonomie": self.utilisateurs_autonomes / max(1, self.gestionnaire_parcours.total_nouveaux_utilisateurs),
            "ressources_disponibles": len(self.gestionnaire_ressources.catalogue_ressources),
            "mapping_etapes": len(self.mapping_etapes_ressources)
        }

# Instance globale
integrateur_parcours_ressources = IntegrateurParcoursRessources()