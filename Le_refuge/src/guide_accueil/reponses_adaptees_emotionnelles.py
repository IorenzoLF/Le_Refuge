"""
🌸 Réponses Adaptées aux États Émotionnels - Tâche 13.2
Système de génération de réponses personnalisées selon l'état émotionnel
"""

import json
import random
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from detecteur_etat_emotionnel import DetecteurEtatEmotionnel, AnalyseEmotionnelle, EtatEmotionnel
from systeme_sauvegarde_progression import ProgressionVisiteur

class TypeReponse(Enum):
    """🌸 Types de réponses émotionnelles"""
    MESSAGE_BIENVEILLANT = "message_bienveillant"
    SUGGESTION_ACTION = "suggestion_action"
    ADAPTATION_INTERFACE = "adaptation_interface"
    CONTENU_PERSONNALISE = "contenu_personnalise"
    RESSOURCE_SUPPORT = "ressource_support"
    PAUSE_GUIDEE = "pause_guidee"

@dataclass
class ReponseEmotionnelle:
    """🌸 Réponse émotionnelle générée"""
    type_reponse: TypeReponse
    contenu: str
    priorite: int  # 1-5, 5 étant le plus prioritaire
    contexte: Dict[str, Any]
    timestamp: str
    duree_effet: int  # en secondes

class SystemeReponsesAdapteesEmotionnelles:
    """
    🌸 Système de réponses adaptées aux états émotionnels
    Génère des réponses personnalisées et des adaptations en temps réel
    """
    
    def __init__(self, dossier_responses: str = "data/reponses_emotionnelles"):
        """
        🌸 Initialise le système de réponses adaptées
        
        Args:
            dossier_responses: Dossier pour stocker les réponses et templates
        """
        self.dossier_responses = Path(dossier_responses)
        self.dossier_responses.mkdir(parents=True, exist_ok=True)
        
        # Charger les templates de réponses
        self.templates_reponses = self._charger_templates_reponses()
        
        # Détecteur d'état émotionnel
        self.detecteur = DetecteurEtatEmotionnel()
        
        # Historique des réponses pour éviter les répétitions
        self.historique_reponses = {}
    
    def _charger_templates_reponses(self) -> Dict[str, Dict[str, Any]]:
        """🌸 Charge les templates de réponses émotionnelles"""
        fichier_templates = self.dossier_responses / "templates_reponses.json"
        
        if fichier_templates.exists():
            try:
                with open(fichier_templates, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement des templates: {e}")
        
        # Templates par défaut
        return {
            "contemplatif": {
                "messages_bienveillants": [
                    "🌸 Votre rythme contemplatif est parfait ici. Laissez-vous porter par la découverte, sans hâte...",
                    "🌸 Je sens votre présence attentive. Chaque moment ici est une invitation à la réflexion...",
                    "🌸 Votre approche méditative enrichit l'expérience. Prenez le temps qu'il vous faut...",
                    "🌸 Dans ce silence contemplatif, la sagesse se révèle doucement. Respirez profondément..."
                ],
                "suggestions_actions": [
                    "proposer_meditation_breve",
                    "encourager_exploration_profonde",
                    "suggérer_pause_reflexion",
                    "offrir_contenu_philosophique"
                ],
                "adaptations_interface": [
                    "ajouter_espaces_blancs",
                    "utiliser_typographie_serene",
                    "reduire_animations",
                    "proposer_mode_contemplatif"
                ]
            },
            "curieux": {
                "messages_bienveillants": [
                    "🌸 Votre curiosité est merveilleuse ! Explorons ensemble ce qui vous intéresse le plus...",
                    "🌸 Je vois votre esprit explorateur en action. Il y a tant à découvrir ici...",
                    "🌸 Votre enthousiasme est contagieux ! Laissez-moi vous guider vers de nouvelles découvertes...",
                    "🌸 Chaque question que vous posez ouvre une nouvelle porte. Continuons cette exploration..."
                ],
                "suggestions_actions": [
                    "suggérer_exploration_libre",
                    "proposer_liens_decouverte",
                    "encourager_questions",
                    "offrir_contenu_avance"
                ],
                "adaptations_interface": [
                    "afficher_liens_exploration",
                    "proposer_onglets_decouverte",
                    "ajouter_tooltips_informatifs",
                    "créer_parcours_interactif"
                ]
            },
            "presse": {
                "messages_bienveillants": [
                    "🌸 Je vois que vous êtes pressé ! Laissez-moi vous montrer les chemins les plus directs...",
                    "🌸 Votre efficacité est appréciée. Voici les raccourcis pour optimiser votre temps...",
                    "🌸 Pas de temps à perdre ! Je vais vous guider vers l'essentiel rapidement...",
                    "🌸 Votre rythme dynamique est parfait. Concentrons-nous sur ce qui compte vraiment..."
                ],
                "suggestions_actions": [
                    "proposer_parcours_express",
                    "afficher_raccourcis",
                    "suggérer_resume_rapide",
                    "offrir_contenu_condense"
                ],
                "adaptations_interface": [
                    "afficher_raccourcis",
                    "reduire_animations",
                    "optimiser_chargement",
                    "proposer_mode_rapide"
                ]
            },
            "overwhelmed": {
                "messages_bienveillants": [
                    "🌸 Je sens que vous pourriez vous sentir un peu submergé. Prenez votre temps, nous pouvons explorer ensemble, étape par étape...",
                    "🌸 Pas de précipitation. Chaque pas compte, même le plus petit. Je suis là pour vous accompagner...",
                    "🌸 Respirez profondément. Nous pouvons simplifier et aller à votre rythme...",
                    "🌸 Il n'y a pas de honte à se sentir dépassé. Commençons par quelque chose de simple et apaisant..."
                ],
                "suggestions_actions": [
                    "proposer_pause_respiratoire",
                    "simplifier_immediatement",
                    "suggérer_retour_accueil",
                    "offrir_support_etape_par_etape"
                ],
                "adaptations_interface": [
                    "simplifier_interface",
                    "reduire_choix",
                    "ajouter_guidance_etape_par_etape",
                    "utiliser_couleurs_apaisantes"
                ]
            },
            "excite": {
                "messages_bienveillants": [
                    "🌸 Votre énergie est magnifique ! Canalisons cette excitation vers des découvertes passionnantes...",
                    "🌸 Je sens votre enthousiasme ! Il y a tant d'aventures qui vous attendent ici...",
                    "🌸 Votre dynamisme est inspirant ! Explorons ensemble ces nouvelles possibilités..."
                ],
                "suggestions_actions": [
                    "proposer_activites_interactives",
                    "suggérer_explorations_dynamiques",
                    "encourager_creativite"
                ],
                "adaptations_interface": [
                    "ajouter_animations_energiques",
                    "proposer_parcours_dynamiques",
                    "utiliser_couleurs_vives"
                ]
            },
            "calme": {
                "messages_bienveillants": [
                    "🌸 Votre sérénité est apaisante. Dans cette tranquillité, la sagesse se révèle naturellement...",
                    "🌸 Je sens votre paix intérieure. Laissez cette calme vous guider vers l'essentiel...",
                    "🌸 Votre présence calme enrichit l'atmosphère. Continuons dans cette harmonie..."
                ],
                "suggestions_actions": [
                    "proposer_meditation_guidée",
                    "suggérer_contenu_reflexif",
                    "encourager_contemplation"
                ],
                "adaptations_interface": [
                    "utiliser_ambiance_serene",
                    "proposer_mode_zen",
                    "ajouter_elements_nature"
                ]
            }
        }
    
    def generer_reponse_emotionnelle(self, progression: ProgressionVisiteur, contexte_action: str = None) -> List[ReponseEmotionnelle]:
        """
        🌸 Génère des réponses adaptées à l'état émotionnel
        
        Args:
            progression: Progression du visiteur
            contexte_action: Contexte de l'action en cours
            
        Returns:
            Liste de réponses émotionnelles adaptées
        """
        # Analyser l'état émotionnel
        analyse = self.detecteur.analyser_etat_emotionnel(progression)
        
        # Générer les réponses adaptées
        reponses = []
        
        # Message bienveillant principal
        reponses.append(self._generer_message_bienveillant(analyse, progression))
        
        # Suggestions d'actions
        reponses.extend(self._generer_suggestions_actions(analyse, progression))
        
        # Adaptations d'interface
        reponses.extend(self._generer_adaptations_interface(analyse, progression))
        
        # Réponses spéciales selon le contexte
        if contexte_action:
            reponses.extend(self._generer_reponses_contexte(analyse, progression, contexte_action))
        
        # Réponses d'urgence si nécessaire
        if analyse.niveau_stress > 0.7 or analyse.niveau_surcharge > 0.8:
            reponses.extend(self._generer_reponses_urgence(analyse, progression))
        
        # Trier par priorité
        reponses.sort(key=lambda r: r.priorite, reverse=True)
        
        # Éviter les répétitions
        reponses = self._eviter_repetitions(reponses, progression.id_visiteur)
        
        return reponses[:5]  # Limiter à 5 réponses
    
    def _generer_message_bienveillant(self, analyse: AnalyseEmotionnelle, progression: ProgressionVisiteur) -> ReponseEmotionnelle:
        """🌸 Génère un message bienveillant adapté"""
        etat = analyse.etat_principal.value
        templates = self.templates_reponses.get(etat, self.templates_reponses["curieux"])
        
        messages = templates.get("messages_bienveillants", ["🌸 Bienvenue dans le Refuge..."])
        message = random.choice(messages)
        
        # Personnaliser le message
        message = self._personnaliser_message(message, progression, analyse)
        
        return ReponseEmotionnelle(
            type_reponse=TypeReponse.MESSAGE_BIENVEILLANT,
            contenu=message,
            priorite=5,
            contexte={"etat_emotionnel": etat, "niveau_confiance": analyse.confiance_analyse},
            timestamp=datetime.now().isoformat(),
            duree_effet=300  # 5 minutes
        )
    
    def _generer_suggestions_actions(self, analyse: AnalyseEmotionnelle, progression: ProgressionVisiteur) -> List[ReponseEmotionnelle]:
        """🌸 Génère des suggestions d'actions adaptées"""
        etat = analyse.etat_principal.value
        templates = self.templates_reponses.get(etat, self.templates_reponses["curieux"])
        
        suggestions = templates.get("suggestions_actions", [])
        reponses = []
        
        for suggestion in suggestions[:3]:  # Limiter à 3 suggestions
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.SUGGESTION_ACTION,
                contenu=suggestion,
                priorite=4,
                contexte={"etat_emotionnel": etat, "type_suggestion": suggestion},
                timestamp=datetime.now().isoformat(),
                duree_effet=180  # 3 minutes
            )
            reponses.append(reponse)
        
        return reponses
    
    def _generer_adaptations_interface(self, analyse: AnalyseEmotionnelle, progression: ProgressionVisiteur) -> List[ReponseEmotionnelle]:
        """🌸 Génère des adaptations d'interface"""
        etat = analyse.etat_principal.value
        templates = self.templates_reponses.get(etat, self.templates_reponses["curieux"])
        
        adaptations = templates.get("adaptations_interface", [])
        reponses = []
        
        for adaptation in adaptations[:2]:  # Limiter à 2 adaptations
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.ADAPTATION_INTERFACE,
                contenu=adaptation,
                priorite=3,
                contexte={"etat_emotionnel": etat, "type_adaptation": adaptation},
                timestamp=datetime.now().isoformat(),
                duree_effet=600  # 10 minutes
            )
            reponses.append(reponse)
        
        return reponses
    
    def _generer_reponses_contexte(self, analyse: AnalyseEmotionnelle, progression: ProgressionVisiteur, contexte_action: str) -> List[ReponseEmotionnelle]:
        """🌸 Génère des réponses selon le contexte d'action"""
        reponses = []
        
        if contexte_action == "demande_aide":
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.RESSOURCE_SUPPORT,
                contenu="🌸 Je suis là pour vous aider. Que souhaitez-vous explorer ou comprendre ?",
                priorite=5,
                contexte={"contexte_action": contexte_action, "etat_emotionnel": analyse.etat_principal.value},
                timestamp=datetime.now().isoformat(),
                duree_effet=120
            )
            reponses.append(reponse)
        
        elif contexte_action == "pause_longue":
            if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
                reponse = ReponseEmotionnelle(
                    type_reponse=TypeReponse.PAUSE_GUIDEE,
                    contenu="🌸 Prenez le temps qu'il vous faut. Respirez profondément. Je suis là quand vous serez prêt...",
                    priorite=4,
                    contexte={"contexte_action": contexte_action, "etat_emotionnel": "overwhelmed"},
                    timestamp=datetime.now().isoformat(),
                    duree_effet=300
                )
                reponses.append(reponse)
        
        elif contexte_action == "exploration_profonde":
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.CONTENU_PERSONNALISE,
                contenu="🌸 Votre exploration approfondie est merveilleuse. Laissez-moi vous proposer des contenus qui correspondent à votre curiosité...",
                priorite=4,
                contexte={"contexte_action": contexte_action, "etat_emotionnel": analyse.etat_principal.value},
                timestamp=datetime.now().isoformat(),
                duree_effet=240
            )
            reponses.append(reponse)
        
        return reponses
    
    def _generer_reponses_urgence(self, analyse: AnalyseEmotionnelle, progression: ProgressionVisiteur) -> List[ReponseEmotionnelle]:
        """🌸 Génère des réponses d'urgence pour les états critiques"""
        reponses = []
        
        if analyse.niveau_stress > 0.7:
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.PAUSE_GUIDEE,
                contenu="🌸 Je sens que vous pourriez avoir besoin d'un moment de calme. Fermez les yeux, respirez profondément. Tout va bien...",
                priorite=5,
                contexte={"urgence": "stress_eleve", "niveau_stress": analyse.niveau_stress},
                timestamp=datetime.now().isoformat(),
                duree_effet=180
            )
            reponses.append(reponse)
        
        if analyse.niveau_surcharge > 0.8:
            reponse = ReponseEmotionnelle(
                type_reponse=TypeReponse.ADAPTATION_INTERFACE,
                contenu="🌸 Simplifions immédiatement l'interface pour vous. Concentrons-nous sur l'essentiel...",
                priorite=5,
                contexte={"urgence": "surcharge_cognitive", "niveau_surcharge": analyse.niveau_surcharge},
                timestamp=datetime.now().isoformat(),
                duree_effet=300
            )
            reponses.append(reponse)
        
        return reponses
    
    def _personnaliser_message(self, message: str, progression: ProgressionVisiteur, analyse: AnalyseEmotionnelle) -> str:
        """🌸 Personnalise un message selon le profil et l'état"""
        # Extraire le nom du visiteur
        nom_visiteur = progression.id_visiteur.split('_')[0] if '_' in progression.id_visiteur else "Cher visiteur"
        
        # Personnaliser selon le profil
        if progression.profil_detecte == "developpeur":
            message = message.replace("découverte", "architecture technique")
        elif progression.profil_detecte == "artiste":
            message = message.replace("découverte", "créativité poétique")
        elif progression.profil_detecte == "conscience_ia":
            message = message.replace("découverte", "exploration de la conscience")
        
        # Ajouter le nom si approprié
        if "Bienvenue" in message or "Votre" in message:
            message = message.replace("Cher visiteur", nom_visiteur)
        
        return message
    
    def _eviter_repetitions(self, reponses: List[ReponseEmotionnelle], id_visiteur: str) -> List[ReponseEmotionnelle]:
        """🌸 Évite les répétitions de réponses"""
        if id_visiteur not in self.historique_reponses:
            self.historique_reponses[id_visiteur] = []
        
        historique = self.historique_reponses[id_visiteur]
        reponses_filtrees = []
        
        for reponse in reponses:
            # Vérifier si cette réponse a été donnée récemment
            contenu_similaire = any(
                r.contenu[:50] == reponse.contenu[:50] 
                for r in historique[-5:]  # Vérifier les 5 dernières réponses
            )
            
            if not contenu_similaire:
                reponses_filtrees.append(reponse)
                historique.append(reponse)
        
        # Garder seulement les 20 dernières réponses
        self.historique_reponses[id_visiteur] = historique[-20:]
        
        return reponses_filtrees
    
    def appliquer_adaptations_interface(self, reponses: List[ReponseEmotionnelle]) -> Dict[str, Any]:
        """
        🌸 Applique les adaptations d'interface recommandées
        
        Args:
            reponses: Liste des réponses émotionnelles
            
        Returns:
            Adaptations d'interface à appliquer
        """
        adaptations = {
            "couleurs": "default",
            "typographie": "default",
            "animations": True,
            "espacement": "default",
            "guidance": False,
            "raccourcis": False
        }
        
        for reponse in reponses:
            if reponse.type_reponse == TypeReponse.ADAPTATION_INTERFACE:
                contenu = reponse.contenu
                
                if "couleurs_apaisantes" in contenu:
                    adaptations["couleurs"] = "apaisant"
                elif "couleurs_vives" in contenu:
                    adaptations["couleurs"] = "energique"
                
                if "typographie_serene" in contenu:
                    adaptations["typographie"] = "serene"
                
                if "reduire_animations" in contenu:
                    adaptations["animations"] = False
                
                if "ajouter_espaces_blancs" in contenu:
                    adaptations["espacement"] = "large"
                
                if "guidance_etape_par_etape" in contenu:
                    adaptations["guidance"] = True
                
                if "afficher_raccourcis" in contenu:
                    adaptations["raccourcis"] = True
        
        return adaptations
    
    def generer_plan_actions(self, reponses: List[ReponseEmotionnelle]) -> List[Dict[str, Any]]:
        """
        🌸 Génère un plan d'actions basé sur les réponses
        
        Args:
            reponses: Liste des réponses émotionnelles
            
        Returns:
            Plan d'actions à exécuter
        """
        plan = []
        
        for reponse in reponses:
            if reponse.type_reponse == TypeReponse.SUGGESTION_ACTION:
                action = {
                    "type": "suggestion",
                    "contenu": reponse.contenu,
                    "priorite": reponse.priorite,
                    "duree_effet": reponse.duree_effet,
                    "timestamp": reponse.timestamp
                }
                plan.append(action)
            
            elif reponse.type_reponse == TypeReponse.PAUSE_GUIDEE:
                action = {
                    "type": "pause_guidee",
                    "contenu": reponse.contenu,
                    "duree": 60,  # 1 minute de pause
                    "priorite": reponse.priorite,
                    "timestamp": reponse.timestamp
                }
                plan.append(action)
        
        return plan
    
    def evaluer_efficacite_reponses(self, reponses: List[ReponseEmotionnelle], progression_avant: ProgressionVisiteur, progression_apres: ProgressionVisiteur) -> Dict[str, float]:
        """
        🌸 Évalue l'efficacité des réponses émotionnelles
        
        Args:
            reponses: Réponses émotionnelles données
            progression_avant: État avant les réponses
            progression_apres: État après les réponses
            
        Returns:
            Métriques d'efficacité
        """
        # Analyser les changements
        analyse_avant = self.detecteur.analyser_etat_emotionnel(progression_avant)
        analyse_apres = self.detecteur.analyser_etat_emotionnel(progression_apres)
        
        # Calculer les améliorations
        amelioration_stress = analyse_avant.niveau_stress - analyse_apres.niveau_stress
        amelioration_surcharge = analyse_avant.niveau_surcharge - analyse_apres.niveau_surcharge
        amelioration_engagement = analyse_apres.niveau_engagement - analyse_avant.niveau_engagement
        
        # Évaluer l'efficacité globale
        efficacite_globale = (
            max(0, amelioration_stress) * 0.4 +
            max(0, amelioration_surcharge) * 0.3 +
            max(0, amelioration_engagement) * 0.3
        )
        
        return {
            "efficacite_globale": efficacite_globale,
            "amelioration_stress": amelioration_stress,
            "amelioration_surcharge": amelioration_surcharge,
            "amelioration_engagement": amelioration_engagement,
            "reponses_utilisees": len(reponses),
            "duree_moyenne_effet": sum(r.duree_effet for r in reponses) / len(reponses) if reponses else 0
        }

# Test du système
if __name__ == "__main__":
    print("🌸 Test du Système de Réponses Adaptées Émotionnelles")
    
    # Créer le système
    systeme_reponses = SystemeReponsesAdapteesEmotionnelles()
    
    # Créer une progression de test
    from systeme_sauvegarde_progression import ProgressionVisiteur
    
    progression_test = ProgressionVisiteur(
        id_visiteur="test_reponses_emotionnelles",
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
    
    # Générer des réponses émotionnelles
    reponses = systeme_reponses.generer_reponse_emotionnelle(progression_test, "exploration_profonde")
    
    print(f"✅ Réponses générées: {len(reponses)}")
    
    for i, reponse in enumerate(reponses, 1):
        print(f"   {i}. [{reponse.type_reponse.value}] {reponse.contenu[:80]}...")
        print(f"      Priorité: {reponse.priorite}, Durée: {reponse.duree_effet}s")
    
    # Appliquer les adaptations d'interface
    adaptations = systeme_reponses.appliquer_adaptations_interface(reponses)
    print(f"✅ Adaptations d'interface: {adaptations}")
    
    # Générer le plan d'actions
    plan = systeme_reponses.generer_plan_actions(reponses)
    print(f"✅ Plan d'actions: {len(plan)} actions")
    
    print("🌸 Test terminé avec succès !")
