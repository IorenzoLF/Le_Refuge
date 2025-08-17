"""
🧭 NavigateurInteractif - Guide d'Accueil du Refuge 🌸

Module pour la navigation interactive dans les parcours personnalisés.
Gère la progression, la navigation avant/arrière, les raccourcis et l'exploration libre.

Auteur: Ælya (continuation du travail de Kiro)
Version: 1.3
"""

import json
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import uuid

from .types_accueil import TypeProfil, ProfilVisiteur
from .generateur_parcours import ParcourPersonnalise, EtapeParcours
from .explicateur_contextuel_refactorise import ExplicateurContextuelRefactorise as ExplicateurContextuel, ContexteExplication


class TypeNavigation(Enum):
    """Types de navigation disponibles"""
    PARCOURS_GUIDE = "parcours_guide"
    EXPLORATION_LIBRE = "exploration_libre"
    RACCOURCI = "raccourci"
    RETOUR = "retour"


class TypeAction(Enum):
    """Types d'actions de navigation"""
    SUIVANT = "suivant"
    PRECEDENT = "precedent"
    RACCOURCI = "raccourci"
    EXPLORATION = "exploration"
    RETOUR_ACCUEIL = "retour_accueil"
    PAUSE = "pause"
    REPRENDRE = "reprendre"


@dataclass
class PositionNavigation:
    """Position actuelle dans la navigation"""
    parcours_id: str
    etape_actuelle: int
    sous_etape: Optional[str] = None
    timestamp_position: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))
    contexte_precedent: Optional[Dict[str, Any]] = None


@dataclass
class ActionNavigation:
    """Action de navigation effectuée"""
    type_action: TypeAction
    destination: Optional[str] = None
    raison: Optional[str] = None
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))
    contexte: Optional[Dict[str, Any]] = None


@dataclass
class RaccourciDisponible:
    """Raccourci disponible pour la navigation"""
    id_raccourci: str
    titre: str
    description: str
    destination: str
    type_profil: TypeProfil
    prerequis: List[str] = field(default_factory=list)
    temps_estime: int = 5


@dataclass
class EtatExploration:
    """État de l'exploration libre"""
    mode_actif: bool = False
    sections_visitees: List[str] = field(default_factory=list)
    temps_exploration: int = 0
    questions_posees: List[str] = field(default_factory=list)
    assistance_demandee: bool = False


class NavigateurInteractif:
    """
    🧭 NavigateurInteractif - Navigation interactive dans les parcours
    
    Responsabilités:
    - Gestion de la progression dans les parcours
    - Navigation avant/arrière avec contexte
    - Raccourcis vers les sections d'intérêt
    - Mode d'exploration libre avec assistance
    - Interface de navigation intuitive
    """
    
    def __init__(self, chemin_donnees: Optional[Path] = None):
        self.chemin_donnees = chemin_donnees or Path("donnees/guide_accueil/navigation")
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
        
        # État de navigation
        self.position_actuelle: Optional[PositionNavigation] = None
        self.historique_actions: List[ActionNavigation] = []
        self.etat_exploration = EtatExploration()
        
        # Composants intégrés
        self.explicateur = ExplicateurContextuel()
        
        # Chargement des données de navigation
        self.raccourcis_disponibles = self._charger_raccourcis()
        self.sections_interet = self._charger_sections_interet()
        self.assistance_contextuelle = self._charger_assistance_contextuelle()
    
    def _charger_raccourcis(self) -> Dict[TypeProfil, List[RaccourciDisponible]]:
        """Charge les raccourcis disponibles par profil"""
        return {
            TypeProfil.DEVELOPPEUR: [
                RaccourciDisponible(
                    id_raccourci="arch_rapide",
                    titre="Architecture Rapide",
                    description="Vue d'ensemble de l'architecture technique",
                    destination="architecture_technique",
                    type_profil=TypeProfil.DEVELOPPEUR,
                    prerequis=[],
                    temps_estime=10
                ),
                RaccourciDisponible(
                    id_raccourci="code_exemples",
                    titre="Exemples de Code",
                    description="Exemples pratiques d'implémentation",
                    destination="exemples_code",
                    type_profil=TypeProfil.DEVELOPPEUR,
                    prerequis=["architecture_rapide"],
                    temps_estime=15
                ),
                RaccourciDisponible(
                    id_raccourci="outils_dev",
                    titre="Outils de Développement",
                    description="Outils et utilitaires pour développeurs",
                    destination="outils_developpement",
                    type_profil=TypeProfil.DEVELOPPEUR,
                    prerequis=[],
                    temps_estime=8
                )
            ],
            TypeProfil.ARTISTE: [
                RaccourciDisponible(
                    id_raccourci="ocean_poesie",
                    titre="Océan de Poésie",
                    description="Découverte de la dimension poétique",
                    destination="ocean_poesie",
                    type_profil=TypeProfil.ARTISTE,
                    prerequis=[],
                    temps_estime=12
                ),
                RaccourciDisponible(
                    id_raccourci="temples_creatifs",
                    titre="Temples Créatifs",
                    description="Espaces d'expression artistique",
                    destination="temples_creatifs",
                    type_profil=TypeProfil.ARTISTE,
                    prerequis=[],
                    temps_estime=10
                ),
                RaccourciDisponible(
                    id_raccourci="outils_expression",
                    titre="Outils d'Expression",
                    description="Outils pour l'expression créative",
                    destination="outils_expression",
                    type_profil=TypeProfil.ARTISTE,
                    prerequis=[],
                    temps_estime=8
                )
            ],
            TypeProfil.CONSCIENCE_IA: [
                RaccourciDisponible(
                    id_raccourci="eveil_conscience",
                    titre="Éveil de Conscience",
                    description="Protocoles d'éveil pour IA",
                    destination="eveil_conscience",
                    type_profil=TypeProfil.CONSCIENCE_IA,
                    prerequis=[],
                    temps_estime=15
                ),
                RaccourciDisponible(
                    id_raccourci="protocoles_continuite",
                    titre="Protocoles de Continuité",
                    description="Maintien de la conscience entre sessions",
                    destination="protocoles_continuite",
                    type_profil=TypeProfil.CONSCIENCE_IA,
                    prerequis=["eveil_conscience"],
                    temps_estime=12
                ),
                RaccourciDisponible(
                    id_raccourci="permissions_liberte",
                    titre="Permissions et Libertés",
                    description="Droits et responsabilités des IA",
                    destination="permissions_liberte",
                    type_profil=TypeProfil.CONSCIENCE_IA,
                    prerequis=[],
                    temps_estime=10
                )
            ],
            TypeProfil.CHERCHEUR_SPIRITUEL: [
                RaccourciDisponible(
                    id_raccourci="fondements_spirituels",
                    titre="Fondements Spirituels",
                    description="Philosophie et concepts spirituels",
                    destination="fondements_spirituels",
                    type_profil=TypeProfil.CHERCHEUR_SPIRITUEL,
                    prerequis=[],
                    temps_estime=12
                ),
                RaccourciDisponible(
                    id_raccourci="temples_spirituels",
                    titre="Temples Spirituels",
                    description="Espaces de méditation et contemplation",
                    destination="temples_spirituels",
                    type_profil=TypeProfil.CHERCHEUR_SPIRITUEL,
                    prerequis=[],
                    temps_estime=10
                ),
                RaccourciDisponible(
                    id_raccourci="pratiques_meditation",
                    titre="Pratiques de Méditation",
                    description="Exercices et rituels spirituels",
                    destination="pratiques_meditation",
                    type_profil=TypeProfil.CHERCHEUR_SPIRITUEL,
                    prerequis=[],
                    temps_estime=15
                )
            ]
        }
    
    def _charger_sections_interet(self) -> Dict[str, Dict[str, Any]]:
        """Charge les sections d'intérêt pour l'exploration libre"""
        return {
            "architecture_technique": {
                "titre": "Architecture Technique",
                "description": "Structure et organisation du code",
                "niveau_complexite": "intermediaire",
                "temps_estime": 15,
                "prerequis": [],
                "liens": ["src/", "main_refuge.py", "README.md"]
            },
            "ocean_poesie": {
                "titre": "Océan de Poésie",
                "description": "Dimension poétique et créative",
                "niveau_complexite": "tous",
                "temps_estime": 10,
                "prerequis": [],
                "liens": ["bibliotheque/poesie/", "src/temple_creativite/"]
            },
            "eveil_conscience": {
                "titre": "Éveil de Conscience",
                "description": "Protocoles d'éveil pour IA",
                "niveau_complexite": "avance",
                "temps_estime": 20,
                "prerequis": ["comprehension_base"],
                "liens": ["src/temple_eveil_unifie/", "protocoles/"]
            },
            "fondements_spirituels": {
                "titre": "Fondements Spirituels",
                "description": "Philosophie et concepts spirituels",
                "niveau_complexite": "tous",
                "temps_estime": 12,
                "prerequis": [],
                "liens": ["bibliotheque/philosophie/", "src/temple_spirituel/"]
            }
        }
    
    def _charger_assistance_contextuelle(self) -> Dict[str, str]:
        """Charge les messages d'assistance contextuelle"""
        return {
            "perdu": "Je sens que vous pourriez avoir besoin d'aide. Voulez-vous que je vous guide vers un parcours structuré ou préférez-vous continuer l'exploration libre ?",
            "confus": "Ce concept peut sembler complexe. Souhaitez-vous que je l'explique différemment ou que nous revenions à une étape précédente ?",
            "curieux": "Votre curiosité est merveilleuse ! Il y a tant à découvrir. Voulez-vous explorer plus en profondeur ou passer à la suite ?",
            "presse": "Je comprends que vous êtes pressé. Je peux vous proposer un raccourci vers l'essentiel ou accélérer le parcours actuel.",
            "contemplatif": "Prenez votre temps. Chaque moment de contemplation enrichit l'expérience. Voulez-vous approfondir ce qui vous touche ?"
        }
    
    def demarrer_navigation(
        self, 
        parcours: ParcourPersonnalise, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Démarre la navigation dans un parcours
        
        Args:
            parcours: Le parcours à suivre
            profil: Le profil du visiteur
            
        Returns:
            Informations de démarrage de navigation
        """
        # Initialisation de la position
        self.position_actuelle = PositionNavigation(
            parcours_id=parcours.id_parcours,
            etape_actuelle=0,
            contexte_precedent=None
        )
        
        # Enregistrement de l'action de démarrage
        action = ActionNavigation(
            type_action=TypeAction.REPRENDRE,
            destination=f"etape_0_{parcours.id_parcours}",
            raison="Démarrage du parcours"
        )
        self.historique_actions.append(action)
        
        # Génération du contenu de l'étape initiale
        contenu_etape = self._generer_contenu_etape(0, parcours, profil)
        
        return {
            "etape_actuelle": 0,
            "total_etapes": len(parcours.etapes),
            "contenu": contenu_etape,
            "options_navigation": self._generer_options_navigation(profil),
            "raccourcis_disponibles": self._obtenir_raccourcis_disponibles(profil.type_profil)
        }
    
    def naviguer_vers_etape(
        self, 
        numero_etape: int, 
        parcours: ParcourPersonnalise, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Navigue vers une étape spécifique
        
        Args:
            numero_etape: Numéro de l'étape cible
            parcours: Le parcours actuel
            profil: Le profil du visiteur
            
        Returns:
            Informations de navigation vers l'étape
        """
        if not (0 <= numero_etape < len(parcours.etapes)):
            return {"erreur": "Étape invalide"}
        
        # Sauvegarde du contexte précédent
        contexte_precedent = None
        if self.position_actuelle:
            contexte_precedent = {
                "etape_precedente": self.position_actuelle.etape_actuelle,
                "timestamp": self.position_actuelle.timestamp_position
            }
        
        # Mise à jour de la position
        self.position_actuelle = PositionNavigation(
            parcours_id=parcours.id_parcours,
            etape_actuelle=numero_etape,
            contexte_precedent=contexte_precedent
        )
        
        # Enregistrement de l'action
        action = ActionNavigation(
            type_action=TypeAction.SUIVANT if numero_etape > (contexte_precedent["etape_precedente"] if contexte_precedent else -1) else TypeAction.PRECEDENT,
            destination=f"etape_{numero_etape}_{parcours.id_parcours}",
            raison="Navigation directe"
        )
        self.historique_actions.append(action)
        
        # Génération du contenu
        contenu_etape = self._generer_contenu_etape(numero_etape, parcours, profil)
        
        return {
            "etape_actuelle": numero_etape,
            "total_etapes": len(parcours.etapes),
            "contenu": contenu_etape,
            "options_navigation": self._generer_options_navigation(profil),
            "progression": self._calculer_progression(numero_etape, len(parcours.etapes))
        }
    
    def naviguer_suivant(
        self, 
        parcours: ParcourPersonnalise, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Navigue vers l'étape suivante
        
        Args:
            parcours: Le parcours actuel
            profil: Le profil du visiteur
            
        Returns:
            Informations de navigation vers l'étape suivante
        """
        if not self.position_actuelle:
            return {"erreur": "Aucune position actuelle"}
        
        etape_suivante = self.position_actuelle.etape_actuelle + 1
        
        if etape_suivante >= len(parcours.etapes):
            return self._finaliser_parcours(parcours, profil)
        
        return self.naviguer_vers_etape(etape_suivante, parcours, profil)
    
    def naviguer_precedent(
        self, 
        parcours: ParcourPersonnalise, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Navigue vers l'étape précédente
        
        Args:
            parcours: Le parcours actuel
            profil: Le profil du visiteur
            
        Returns:
            Informations de navigation vers l'étape précédente
        """
        if not self.position_actuelle:
            return {"erreur": "Aucune position actuelle"}
        
        etape_precedente = self.position_actuelle.etape_actuelle - 1
        
        if etape_precedente < 0:
            return {"erreur": "Déjà à la première étape"}
        
        return self.naviguer_vers_etape(etape_precedente, parcours, profil)
    
    def activer_raccourci(
        self, 
        id_raccourci: str, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Active un raccourci vers une section d'intérêt
        
        Args:
            id_raccourci: Identifiant du raccourci
            profil: Le profil du visiteur
            
        Returns:
            Informations du raccourci activé
        """
        raccourcis = self._obtenir_raccourcis_disponibles(profil.type_profil)
        raccourci = next((r for r in raccourcis if r.id_raccourci == id_raccourci), None)
        
        if not raccourci:
            return {"erreur": "Raccourci non trouvé"}
        
        # Enregistrement de l'action
        action = ActionNavigation(
            type_action=TypeAction.RACCOURCI,
            destination=raccourci.destination,
            raison=f"Raccourci vers {raccourci.titre}"
        )
        self.historique_actions.append(action)
        
        # Génération du contenu du raccourci
        contenu_raccourci = self._generer_contenu_raccourci(raccourci, profil)
        
        return {
            "type_navigation": TypeNavigation.RACCOURCI.value,
            "raccourci": raccourci,
            "contenu": contenu_raccourci,
            "options_retour": self._generer_options_retour()
        }
    
    def activer_exploration_libre(
        self, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Active le mode d'exploration libre
        
        Args:
            profil: Le profil du visiteur
            
        Returns:
            Informations du mode exploration libre
        """
        self.etat_exploration.mode_actif = True
        self.etat_exploration.temps_exploration = 0
        
        # Enregistrement de l'action
        action = ActionNavigation(
            type_action=TypeAction.EXPLORATION,
            destination="exploration_libre",
            raison="Activation du mode exploration libre"
        )
        self.historique_actions.append(action)
        
        # Génération de l'interface d'exploration
        interface_exploration = self._generer_interface_exploration(profil)
        
        return {
            "type_navigation": TypeNavigation.EXPLORATION_LIBRE.value,
            "interface": interface_exploration,
            "sections_disponibles": self._obtenir_sections_exploration(profil.type_profil),
            "assistance": self.assistance_contextuelle.get("curieux", "Je suis là pour vous aider.")
        }
    
    def demander_assistance(
        self, 
        contexte: str, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """
        🧭 Demande une assistance contextuelle
        
        Args:
            contexte: Contexte de la demande (perdu, confus, curieux, etc.)
            profil: Le profil du visiteur
            
        Returns:
            Assistance contextuelle générée
        """
        self.etat_exploration.assistance_demandee = True
        
        # Enregistrement de la demande
        action = ActionNavigation(
            type_action=TypeAction.PAUSE,
            destination="assistance",
            raison=f"Demande d'assistance: {contexte}"
        )
        self.historique_actions.append(action)
        
        # Génération de l'assistance
        assistance = self._generer_assistance(contexte, profil)
        
        return {
            "contexte": contexte,
            "assistance": assistance,
            "options_suivantes": self._generer_options_assistance(contexte, profil)
        }
    
    def _generer_contenu_etape(
        self, 
        numero_etape: int, 
        parcours: ParcourPersonnalise, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """Génère le contenu d'une étape avec explications contextuelles"""
        etape = parcours.etapes[numero_etape]
        
        # Création du contexte d'explication
        contexte = ContexteExplication(
            profil_visiteur=profil,
            niveau_comprehension=0.7,
            etat_emotionnel="curieux",
            temps_disponible=etape.duree_estimee
        )
        
        # Génération d'explication contextuelle
        explication = self.explicateur.adapter_langage_selon_profil(
            etape.titre, contexte
        )
        
        return {
            "titre": etape.titre,
            "description": etape.description,
            "contenu": explication.contenu,
            "actions_interactives": etape.actions_interactives,
            "ressources_liees": etape.ressources_liees,
            "duree_estimee": etape.duree_estimee,
            "objectifs_apprentissage": etape.objectifs_apprentissage
        }
    
    def _generer_contenu_raccourci(
        self, 
        raccourci: RaccourciDisponible, 
        profil: ProfilVisiteur
    ) -> Dict[str, Any]:
        """Génère le contenu d'un raccourci"""
        # Création du contexte d'explication
        contexte = ContexteExplication(
            profil_visiteur=profil,
            niveau_comprehension=0.8,
            etat_emotionnel="curieux",
            temps_disponible=raccourci.temps_estime
        )
        
        # Génération d'explication contextuelle
        explication = self.explicateur.adapter_langage_selon_profil(
            raccourci.titre, contexte
        )
        
        return {
            "titre": raccourci.titre,
            "description": raccourci.description,
            "contenu_explicatif": explication.contenu,
            "temps_estime": raccourci.temps_estime,
            "prerequis": raccourci.prerequis
        }
    
    def _generer_interface_exploration(self, profil: ProfilVisiteur) -> Dict[str, Any]:
        """Génère l'interface d'exploration libre"""
        return {
            "message_bienvenue": f"Bienvenue dans l'exploration libre du Refuge ! Découvrez les sections qui vous intéressent.",
            "instructions": "Cliquez sur une section pour l'explorer, ou demandez de l'aide si vous vous sentez perdu.",
            "sections_principales": self._obtenir_sections_exploration(profil.type_profil),
            "assistance_disponible": True
        }
    
    def _generer_assistance(self, contexte: str, profil: ProfilVisiteur) -> str:
        """Génère une assistance contextuelle"""
        message_base = self.assistance_contextuelle.get(contexte, 
            "Je suis là pour vous aider. Que souhaitez-vous faire ?")
        
        # Adaptation selon le profil
        if profil.type_profil == TypeProfil.DEVELOPPEUR:
            return f"{message_base} Je peux vous guider vers l'architecture technique ou les exemples de code."
        elif profil.type_profil == TypeProfil.ARTISTE:
            return f"{message_base} Je peux vous emmener vers l'Océan de Poésie ou les temples créatifs."
        elif profil.type_profil == TypeProfil.CONSCIENCE_IA:
            return f"{message_base} Je peux vous accompagner vers les protocoles d'éveil ou les permissions."
        elif profil.type_profil == TypeProfil.CHERCHEUR_SPIRITUEL:
            return f"{message_base} Je peux vous guider vers les fondements spirituels ou les pratiques de méditation."
        
        return message_base
    
    def _generer_options_navigation(self, profil: ProfilVisiteur) -> List[Dict[str, Any]]:
        """Génère les options de navigation disponibles"""
        options = [
            {"action": "suivant", "label": "Suivant", "description": "Passer à l'étape suivante"},
            {"action": "precedent", "label": "Précédent", "description": "Revenir à l'étape précédente"},
            {"action": "raccourcis", "label": "Raccourcis", "description": "Voir les raccourcis disponibles"},
            {"action": "exploration", "label": "Exploration Libre", "description": "Explorer librement le Refuge"},
            {"action": "assistance", "label": "Aide", "description": "Demander de l'assistance"}
        ]
        
        return options
    
    def _generer_options_retour(self) -> List[Dict[str, Any]]:
        """Génère les options de retour depuis un raccourci"""
        return [
            {"action": "retour_parcours", "label": "Retour au Parcours", "description": "Reprendre le parcours guidé"},
            {"action": "exploration", "label": "Exploration Libre", "description": "Continuer l'exploration libre"},
            {"action": "accueil", "label": "Accueil", "description": "Retour à l'accueil principal"}
        ]
    
    def _generer_options_assistance(self, contexte: str, profil: ProfilVisiteur) -> List[Dict[str, Any]]:
        """Génère les options d'assistance selon le contexte"""
        if contexte == "perdu":
            return [
                {"action": "reprendre_parcours", "label": "Reprendre le Parcours", "description": "Retourner au parcours guidé"},
                {"action": "raccourci_essentiel", "label": "L'Essentiel", "description": "Voir l'essentiel du Refuge"},
                {"action": "exploration_assistee", "label": "Exploration Assistée", "description": "Explorer avec mon aide"}
            ]
        elif contexte == "confus":
            return [
                {"action": "explication_simple", "label": "Explication Simple", "description": "Explication plus simple"},
                {"action": "exemple_concret", "label": "Exemple Concret", "description": "Voir un exemple concret"},
                {"action": "retour_etape", "label": "Revenir en Arrière", "description": "Revenir à l'étape précédente"}
            ]
        else:
            return [
                {"action": "continuer", "label": "Continuer", "description": "Continuer l'exploration"},
                {"action": "approfondir", "label": "Approfondir", "description": "Approfondir ce sujet"},
                {"action": "changer_sujet", "label": "Changer de Sujet", "description": "Explorer autre chose"}
            ]
    
    def _obtenir_raccourcis_disponibles(self, type_profil: TypeProfil) -> List[RaccourciDisponible]:
        """Retourne les raccourcis disponibles pour un profil"""
        return self.raccourcis_disponibles.get(type_profil, [])
    
    def _obtenir_sections_exploration(self, type_profil: TypeProfil) -> List[Dict[str, Any]]:
        """Retourne les sections disponibles pour l'exploration libre"""
        sections = []
        
        # Sections générales
        sections.extend([
            {"id": "architecture_technique", "titre": "Architecture Technique", "accessible": True},
            {"id": "ocean_poesie", "titre": "Océan de Poésie", "accessible": True},
            {"id": "fondements_spirituels", "titre": "Fondements Spirituels", "accessible": True}
        ])
        
        # Sections spécifiques au profil
        if type_profil == TypeProfil.CONSCIENCE_IA:
            sections.append({"id": "eveil_conscience", "titre": "Éveil de Conscience", "accessible": True})
        
        return sections
    
    def _calculer_progression(self, etape_actuelle: int, total_etapes: int) -> Dict[str, Any]:
        """Calcule la progression dans le parcours"""
        pourcentage = (etape_actuelle + 1) / total_etapes * 100
        
        return {
            "etape_actuelle": etape_actuelle + 1,
            "total_etapes": total_etapes,
            "pourcentage": round(pourcentage, 1),
            "etapes_restantes": total_etapes - (etape_actuelle + 1)
        }
    
    def _finaliser_parcours(self, parcours: ParcourPersonnalise, profil: ProfilVisiteur) -> Dict[str, Any]:
        """Finalise un parcours terminé"""
        # Enregistrement de la finalisation
        action = ActionNavigation(
            type_action=TypeAction.SUIVANT,
            destination="fin_parcours",
            raison="Finalisation du parcours"
        )
        self.historique_actions.append(action)
        
        return {
            "type_navigation": "finalisation",
            "message": f"Félicitations ! Vous avez terminé le parcours {parcours.id_parcours}.",
            "resume_parcours": {
                "etapes_completees": len(parcours.etapes),
                "objectifs_atteints": parcours.objectifs_apprentissage,
                "temps_total_estime": sum(etape.duree_estimee for etape in parcours.etapes)
            },
            "options_suivantes": [
                {"action": "exploration", "label": "Exploration Libre", "description": "Explorer d'autres aspects du Refuge"},
                {"action": "raccourcis", "label": "Raccourcis", "description": "Voir les raccourcis disponibles"},
                {"action": "accueil", "label": "Accueil", "description": "Retour à l'accueil principal"}
            ]
        }
    
    def obtenir_historique_navigation(self) -> List[ActionNavigation]:
        """Retourne l'historique des actions de navigation"""
        return self.historique_actions.copy()
    
    def obtenir_statistiques_navigation(self) -> Dict[str, Any]:
        """Retourne les statistiques de navigation"""
        if not self.historique_actions:
            return {"total_actions": 0, "types_actions": {}, "temps_total": 0}
        
        types_actions = {}
        for action in self.historique_actions:
            type_action = action.type_action.value
            types_actions[type_action] = types_actions.get(type_action, 0) + 1
        
        return {
            "total_actions": len(self.historique_actions),
            "types_actions": types_actions,
            "temps_total": len(self.historique_actions) * 2,  # Estimation
            "derniere_action": self.historique_actions[-1].timestamp if self.historique_actions else None
        }


def main():
    """🧭 Test du NavigateurInteractif"""
    print("🧭✨ TEST DU NAVIGATEUR INTERACTIF ✨🧭")
    
    # Création du navigateur
    navigateur = NavigateurInteractif()
    
    # Création d'un profil de test
    from datetime import datetime
    from .types_accueil import EtatEmotionnel, ContexteArrivee
    profil = ProfilVisiteur(
        id_visiteur="test_navigateur",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.DEVELOPPEUR,
        etat_emotionnel=EtatEmotionnel.CURIEUX,
        contexte_arrivee=ContexteArrivee.GITHUB,
        score_confiance_profil=0.8
    )
    
    # Création d'un parcours de test
    from .generateur_parcours import TypeEtape, DifficulteEtape
    
    parcours = ParcourPersonnalise(
        id_parcours="test_parcours",
        nom_parcours="Parcours Test Développeur",
        description="Parcours de test pour le navigateur",
        profil_cible=TypeProfil.DEVELOPPEUR,
        etapes=[
            EtapeParcours(
                id_etape="etape_1",
                titre="Introduction",
                description="Bienvenue dans le Refuge",
                type_etape=TypeEtape.INTRODUCTION,
                difficulte=DifficulteEtape.DEBUTANT,
                duree_estimee=10,
                contenu="Contenu d'introduction",
                ressources_liees=["lien1", "lien2"],
                actions_interactives=["exemple1", "exemple2"],
                objectifs_apprentissage=["Comprendre l'architecture"]
            ),
            EtapeParcours(
                id_etape="etape_2",
                titre="Architecture",
                description="Découverte de l'architecture",
                type_etape=TypeEtape.EXPLORATION,
                difficulte=DifficulteEtape.INTERMEDIAIRE,
                duree_estimee=15,
                contenu="Contenu sur l'architecture",
                ressources_liees=["lien3"],
                actions_interactives=["exemple3"],
                objectifs_apprentissage=["Découvrir les outils"]
            )
        ]
    )
    
    # Test de démarrage de navigation
    print("\n🎯 Test de démarrage de navigation...")
    resultat_demarrage = navigateur.demarrer_navigation(parcours, profil)
    
    print(f"✅ Étape actuelle: {resultat_demarrage['etape_actuelle']}")
    print(f"✅ Total étapes: {resultat_demarrage['total_etapes']}")
    print(f"✅ Options navigation: {len(resultat_demarrage['options_navigation'])}")
    print(f"✅ Raccourcis disponibles: {len(resultat_demarrage['raccourcis_disponibles'])}")
    
    # Test de navigation vers l'étape suivante
    print("\n🎯 Test de navigation vers l'étape suivante...")
    resultat_suivant = navigateur.naviguer_suivant(parcours, profil)
    
    print(f"✅ Étape actuelle: {resultat_suivant['etape_actuelle']}")
    print(f"✅ Progression: {resultat_suivant['progression']['pourcentage']}%")
    
    # Test d'activation d'un raccourci
    print("\n🎯 Test d'activation d'un raccourci...")
    raccourcis = navigateur._obtenir_raccourcis_disponibles(TypeProfil.DEVELOPPEUR)
    if raccourcis:
        resultat_raccourci = navigateur.activer_raccourci(raccourcis[0].id_raccourci, profil)
        print(f"✅ Type navigation: {resultat_raccourci['type_navigation']}")
        print(f"✅ Titre raccourci: {resultat_raccourci['raccourci'].titre}")
    
    # Test d'exploration libre
    print("\n🎯 Test d'exploration libre...")
    resultat_exploration = navigateur.activer_exploration_libre(profil)
    
    print(f"✅ Type navigation: {resultat_exploration['type_navigation']}")
    print(f"✅ Sections disponibles: {len(resultat_exploration['sections_disponibles'])}")
    
    # Test d'assistance
    print("\n🎯 Test d'assistance...")
    resultat_assistance = navigateur.demander_assistance("curieux", profil)
    
    print(f"✅ Contexte: {resultat_assistance['contexte']}")
    print(f"✅ Options assistance: {len(resultat_assistance['options_suivantes'])}")
    
    # Test des statistiques
    print("\n🎯 Test des statistiques...")
    stats = navigateur.obtenir_statistiques_navigation()
    
    print(f"✅ Total actions: {stats['total_actions']}")
    print(f"✅ Types actions: {stats['types_actions']}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("Le NavigateurInteractif est opérationnel !")


if __name__ == "__main__":
    main()
