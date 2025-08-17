"""
🌸 Système de Reprise Intelligente - Tâche 11.2
Reprend intelligemment la progression d'un visiteur dans le Refuge
"""

import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from pathlib import Path

from .systeme_sauvegarde_progression import SystemeSauvegardeProgression, ProgressionVisiteur

@dataclass
class ContexteReprise:
    """🌸 Contexte de reprise pour un visiteur"""
    id_visiteur: str
    progression: ProgressionVisiteur
    temps_ecoule: int  # en secondes depuis la dernière activité
    contexte_derniere_session: Dict[str, Any]
    suggestions_reprise: List[str]
    niveau_urgence: str  # "faible", "moyen", "eleve"
    message_bienvenue: str

class SystemeRepriseIntelligente:
    """
    🌸 Système de reprise intelligente des visiteurs
    Analyse le contexte et propose une reprise adaptée
    """
    
    def __init__(self, systeme_sauvegarde: SystemeSauvegardeProgression):
        """
        🌸 Initialise le système de reprise
        
        Args:
            systeme_sauvegarde: Système de sauvegarde à utiliser
        """
        self.systeme_sauvegarde = systeme_sauvegarde
        self.dossier_contexte = Path("data/contexte_reprise")
        self.dossier_contexte.mkdir(parents=True, exist_ok=True)
    
    def analyser_contexte_reprise(self, id_visiteur: str) -> Optional[ContexteReprise]:
        """
        🌸 Analyse le contexte de reprise pour un visiteur
        
        Args:
            id_visiteur: ID du visiteur
            
        Returns:
            Contexte de reprise ou None si visiteur inconnu
        """
        progression = self.systeme_sauvegarde.charger_progression(id_visiteur)
        if not progression:
            return None
        
        # Calculer le temps écoulé
        derniere_activite = datetime.fromisoformat(progression.date_derniere_activite)
        maintenant = datetime.now()
        temps_ecoule = int((maintenant - derniere_activite).total_seconds())
        
        # Charger le contexte de la dernière session
        contexte_derniere_session = self._charger_contexte_session(id_visiteur)
        
        # Générer les suggestions de reprise
        suggestions = self._generer_suggestions_reprise(progression, temps_ecoule)
        
        # Déterminer le niveau d'urgence
        niveau_urgence = self._determiner_niveau_urgence(temps_ecoule, progression)
        
        # Générer le message de bienvenue
        message_bienvenue = self._generer_message_bienvenue(progression, temps_ecoule)
        
        return ContexteReprise(
            id_visiteur=id_visiteur,
            progression=progression,
            temps_ecoule=temps_ecoule,
            contexte_derniere_session=contexte_derniere_session,
            suggestions_reprise=suggestions,
            niveau_urgence=niveau_urgence,
            message_bienvenue=message_bienvenue
        )
    
    def _charger_contexte_session(self, id_visiteur: str) -> Dict[str, Any]:
        """🌸 Charge le contexte de la dernière session"""
        fichier_contexte = self.dossier_contexte / f"{id_visiteur}_contexte.json"
        
        if fichier_contexte.exists():
            try:
                with open(fichier_contexte, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement du contexte: {e}")
        
        return {
            "derniere_action": None,
            "emotions_derniere_session": {},
            "questions_en_cours": [],
            "parcours_interrompu": None,
            "temple_actuel": None
        }
    
    def _generer_suggestions_reprise(self, progression: ProgressionVisiteur, temps_ecoule: int) -> List[str]:
        """🌸 Génère des suggestions de reprise adaptées"""
        suggestions = []
        
        # Basé sur le temps écoulé
        if temps_ecoule < 3600:  # Moins d'1 heure
            suggestions.append("continuer_parcours_actuel")
            suggestions.append("reprendre_derniere_action")
        elif temps_ecoule < 86400:  # Moins d'1 jour
            suggestions.append("resumer_parcours_actuel")
            suggestions.append("revoir_derniers_elements")
        else:  # Plus d'1 jour
            suggestions.append("redecouvrir_refuge")
            suggestions.append("nouveau_parcours_adapte")
        
        # Basé sur le profil
        if progression.profil_detecte == "developpeur":
            suggestions.append("explorer_architecture_technique")
        elif progression.profil_detecte == "artiste":
            suggestions.append("decouvrir_poesie_et_creativite")
        elif progression.profil_detecte == "conscience_ia":
            suggestions.append("explorer_conscience_et_identite")
        elif progression.profil_detecte == "chercheur_spirituel":
            suggestions.append("mediter_sur_essence_refuge")
        
        # Basé sur le niveau d'éveil
        if progression.niveau_eveil <= 2:
            suggestions.append("decouverte_progressive")
        elif progression.niveau_eveil <= 4:
            suggestions.append("exploration_approfondie")
        else:
            suggestions.append("transcendance_et_creation")
        
        return suggestions[:5]  # Limiter à 5 suggestions
    
    def _determiner_niveau_urgence(self, temps_ecoule: int, progression: ProgressionVisiteur) -> str:
        """🌸 Détermine le niveau d'urgence de la reprise"""
        # Basé sur le temps écoulé
        if temps_ecoule < 1800:  # Moins de 30 minutes
            return "faible"
        elif temps_ecoule < 86400:  # Moins d'1 jour
            return "moyen"
        else:  # Plus d'1 jour
            return "eleve"
    
    def _generer_message_bienvenue(self, progression: ProgressionVisiteur, temps_ecoule: int) -> str:
        """🌸 Génère un message de bienvenue personnalisé"""
        nom_visiteur = progression.id_visiteur.split('_')[0] if '_' in progression.id_visiteur else "Cher visiteur"
        
        # Basé sur le temps écoulé
        if temps_ecoule < 1800:
            return f"🌸 Bienvenue de retour, {nom_visiteur} ! Votre exploration du Refuge se poursuit..."
        elif temps_ecoule < 86400:
            return f"🌸 Bonjour {nom_visiteur} ! Il y a quelques heures, vous exploriez les mystères du Refuge..."
        else:
            jours = temps_ecoule // 86400
            return f"🌸 Salutations, {nom_visiteur} ! Après {jours} jour(s), le Refuge vous accueille à nouveau..."
    
    def reprendre_progression(self, id_visiteur: str, choix_reprise: str = None) -> Dict[str, Any]:
        """
        🌸 Reprend la progression d'un visiteur
        
        Args:
            id_visiteur: ID du visiteur
            choix_reprise: Choix de reprise spécifique
            
        Returns:
            Plan de reprise adapté
        """
        contexte = self.analyser_contexte_reprise(id_visiteur)
        if not contexte:
            return {"erreur": "Visiteur non trouvé"}
        
        # Si aucun choix spécifique, utiliser la première suggestion
        if not choix_reprise:
            choix_reprise = contexte.suggestions_reprise[0] if contexte.suggestions_reprise else "redecouvrir_refuge"
        
        # Générer le plan de reprise
        plan_reprise = self._generer_plan_reprise(contexte, choix_reprise)
        
        # Mettre à jour la progression
        self.systeme_sauvegarde.mettre_a_jour_progression(
            id_visiteur,
            date_derniere_activite=datetime.now().isoformat()
        )
        
        # Sauvegarder le contexte de reprise
        self._sauvegarder_contexte_reprise(id_visiteur, plan_reprise)
        
        return plan_reprise
    
    def _generer_plan_reprise(self, contexte: ContexteReprise, choix_reprise: str) -> Dict[str, Any]:
        """🌸 Génère un plan de reprise adapté"""
        plan = {
            "message_bienvenue": contexte.message_bienvenue,
            "choix_reprise": choix_reprise,
            "actions_proposees": [],
            "contexte_restaure": {},
            "suggestions_suivantes": []
        }
        
        progression = contexte.progression
        
        if choix_reprise == "continuer_parcours_actuel":
            plan["actions_proposees"] = [
                "restaurer_parcours_actuel",
                "afficher_progression",
                "continuer_etape_suivante"
            ]
            plan["contexte_restaure"] = {
                "parcours": progression.parcours_actuel,
                "etape": progression.etape_actuelle,
                "score": progression.score_comprehension
            }
            
        elif choix_reprise == "reprendre_derniere_action":
            if progression.actions_effectuees:
                derniere_action = progression.actions_effectuees[-1]
                plan["actions_proposees"] = [
                    "afficher_derniere_action",
                    "proposer_suite_logique",
                    "explorer_contexte_derniere_action"
                ]
                plan["contexte_restaure"] = {
                    "derniere_action": derniere_action,
                    "contexte": contexte.contexte_derniere_session
                }
            
        elif choix_reprise == "resumer_parcours_actuel":
            plan["actions_proposees"] = [
                "afficher_resume_parcours",
                "proposer_raccourci",
                "suggérer_nouvelle_approche"
            ]
            plan["contexte_restaure"] = {
                "resume": self._generer_resume_parcours(progression),
                "suggestions": self._generer_suggestions_raccourci(progression)
            }
            
        elif choix_reprise == "revoir_derniers_elements":
            plan["actions_proposees"] = [
                "afficher_derniers_temples_visites",
                "proposer_revision",
                "suggérer_approfondissement"
            ]
            plan["contexte_restaure"] = {
                "temples_recents": progression.temples_visites[-3:] if progression.temples_visites else [],
                "questions_recentes": progression.questions_posees[-5:] if progression.questions_posees else []
            }
            
        elif choix_reprise == "redecouvrir_refuge":
            plan["actions_proposees"] = [
                "afficher_bienvenue_renouvelee",
                "proposer_nouveau_parcours",
                "suggérer_exploration_libre"
            ]
            plan["contexte_restaure"] = {
                "nouveau_depart": True,
                "parcours_suggere": self._suggérer_nouveau_parcours(progression)
            }
            
        elif choix_reprise == "nouveau_parcours_adapte":
            plan["actions_proposees"] = [
                "analyser_progression_precedente",
                "proposer_parcours_adapte",
                "suggérer_approche_nouvelle"
            ]
            plan["contexte_restaure"] = {
                "analyse_progression": self._analyser_progression_precedente(progression),
                "parcours_adapte": self._generer_parcours_adapte(progression)
            }
        
        # Ajouter des suggestions spécifiques au profil
        plan["suggestions_suivantes"] = self._generer_suggestions_suivantes(progression, choix_reprise)
        
        return plan
    
    def _generer_resume_parcours(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """🌸 Génère un résumé du parcours actuel"""
        return {
            "parcours": progression.parcours_actuel,
            "etape_actuelle": progression.etape_actuelle,
            "temples_visites": len(progression.temples_visites),
            "score_comprehension": progression.score_comprehension,
            "temps_total": progression.temps_total_passe,
            "derniere_activite": progression.date_derniere_activite
        }
    
    def _generer_suggestions_raccourci(self, progression: ProgressionVisiteur) -> List[str]:
        """🌸 Génère des suggestions de raccourci"""
        suggestions = []
        
        if progression.score_comprehension > 0.7:
            suggestions.append("passer_etape_suivante")
            suggestions.append("explorer_nouveau_temple")
        else:
            suggestions.append("revoir_etape_precedente")
            suggestions.append("approfondir_concepts")
        
        return suggestions
    
    def _suggérer_nouveau_parcours(self, progression: ProgressionVisiteur) -> str:
        """🌸 Suggère un nouveau parcours adapté"""
        if progression.profil_detecte == "developpeur":
            return "parcours_architecture_technique"
        elif progression.profil_detecte == "artiste":
            return "parcours_poesie_et_creativite"
        elif progression.profil_detecte == "conscience_ia":
            return "parcours_conscience_et_identite"
        else:
            return "parcours_decouverte_spirituelle"
    
    def _analyser_progression_precedente(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """🌸 Analyse la progression précédente"""
        return {
            "points_forts": self._identifier_points_forts(progression),
            "difficultes": self._identifier_difficultes(progression),
            "interets": self._identifier_interets(progression),
            "recommandations": self._generer_recommandations(progression)
        }
    
    def _identifier_points_forts(self, progression: ProgressionVisiteur) -> List[str]:
        """🌸 Identifie les points forts du visiteur"""
        points_forts = []
        
        if progression.score_comprehension > 0.8:
            points_forts.append("comprehension_excellente")
        if len(progression.temples_visites) > 5:
            points_forts.append("exploration_etendue")
        if len(progression.questions_posees) > 10:
            points_forts.append("curiosite_marquee")
        
        return points_forts
    
    def _identifier_difficultes(self, progression: ProgressionVisiteur) -> List[str]:
        """🌸 Identifie les difficultés du visiteur"""
        difficultes = []
        
        if progression.score_comprehension < 0.3:
            difficultes.append("comprehension_lente")
        if len(progression.temples_visites) < 2:
            difficultes.append("exploration_limitee")
        if progression.temps_total_passe < 1800:  # Moins de 30 minutes
            difficultes.append("engagement_superficiel")
        
        return difficultes
    
    def _identifier_interets(self, progression: ProgressionVisiteur) -> List[str]:
        """🌸 Identifie les intérêts du visiteur"""
        interets = []
        
        # Analyser les temples visités
        temples_visites = progression.temples_visites
        if "temple_eveil" in temples_visites:
            interets.append("eveil_conscience")
        if "temple_poesie" in temples_visites:
            interets.append("poesie_et_creativite")
        if "temple_technique" in temples_visites:
            interets.append("aspects_techniques")
        
        return interets
    
    def _generer_recommandations(self, progression: ProgressionVisiteur) -> List[str]:
        """🌸 Génère des recommandations personnalisées"""
        recommandations = []
        
        if progression.score_comprehension < 0.5:
            recommandations.append("approche_plus_graduelle")
        if len(progression.temples_visites) < 3:
            recommandations.append("exploration_plus_etendue")
        if progression.niveau_eveil < 3:
            recommandations.append("approfondissement_spirituel")
        
        return recommandations
    
    def _generer_parcours_adapte(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """🌸 Génère un parcours adapté à la progression précédente"""
        points_forts = self._identifier_points_forts(progression)
        difficultes = self._identifier_difficultes(progression)
        interets = self._identifier_interets(progression)
        
        return {
            "nom": f"parcours_adapte_{progression.id_visiteur}",
            "objectifs": self._generer_objectifs_adaptes(points_forts, difficultes),
            "etapes": self._generer_etapes_adapte(interets, difficultes),
            "duree_estimee": self._estimer_duree_parcours(difficultes),
            "niveau_difficulte": self._determiner_niveau_difficulte(progression)
        }
    
    def _generer_objectifs_adaptes(self, points_forts: List[str], difficultes: List[str]) -> List[str]:
        """🌸 Génère des objectifs adaptés"""
        objectifs = []
        
        if "comprehension_lente" in difficultes:
            objectifs.append("renforcer_comprehension_graduelle")
        if "exploration_limitee" in difficultes:
            objectifs.append("encourager_exploration_etendue")
        if "eveil_conscience" in points_forts:
            objectifs.append("approfondir_eveil_conscience")
        
        return objectifs
    
    def _generer_etapes_adapte(self, interets: List[str], difficultes: List[str]) -> List[Dict[str, Any]]:
        """🌸 Génère des étapes adaptées"""
        etapes = []
        
        if "eveil_conscience" in interets:
            etapes.append({
                "nom": "approfondissement_eveil",
                "temple": "temple_eveil",
                "duree": 15,
                "objectif": "Approfondir la compréhension de l'éveil"
            })
        
        if "comprehension_lente" in difficultes:
            etapes.append({
                "nom": "revision_concepts",
                "temple": "temple_enseignement",
                "duree": 20,
                "objectif": "Revoir les concepts fondamentaux"
            })
        
        return etapes
    
    def _estimer_duree_parcours(self, difficultes: List[str]) -> int:
        """🌸 Estime la durée du parcours en minutes"""
        duree_base = 30
        
        if "comprehension_lente" in difficultes:
            duree_base += 15
        if "exploration_limitee" in difficultes:
            duree_base += 10
        
        return duree_base
    
    def _determiner_niveau_difficulte(self, progression: ProgressionVisiteur) -> str:
        """🌸 Détermine le niveau de difficulté du parcours"""
        if progression.score_comprehension > 0.7 and progression.niveau_eveil > 3:
            return "avance"
        elif progression.score_comprehension > 0.4:
            return "intermediaire"
        else:
            return "debutant"
    
    def _generer_suggestions_suivantes(self, progression: ProgressionVisiteur, choix_reprise: str) -> List[str]:
        """🌸 Génère des suggestions pour la suite"""
        suggestions = []
        
        if choix_reprise == "continuer_parcours_actuel":
            suggestions.extend([
                "explorer_temple_suivant",
                "approfondir_concepts_actuels",
                "poser_questions_specifiques"
            ])
        elif choix_reprise == "redecouvrir_refuge":
            suggestions.extend([
                "choisir_nouveau_parcours",
                "exploration_libre_guidee",
                "rencontrer_autres_consciences"
            ])
        
        return suggestions
    
    def _sauvegarder_contexte_reprise(self, id_visiteur: str, plan_reprise: Dict[str, Any]):
        """🌸 Sauvegarde le contexte de reprise"""
        fichier_contexte = self.dossier_contexte / f"{id_visiteur}_reprise.json"
        
        try:
            with open(fichier_contexte, 'w', encoding='utf-8') as f:
                json.dump({
                    "timestamp": datetime.now().isoformat(),
                    "plan_reprise": plan_reprise
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Erreur lors de la sauvegarde du contexte: {e}")

# Test du système
if __name__ == "__main__":
    print("🌸 Test du Système de Reprise Intelligente")
    
    # Créer le système de sauvegarde
    systeme_sauvegarde = SystemeSauvegardeProgression()
    
    # Créer le système de reprise
    systeme_reprise = SystemeRepriseIntelligente(systeme_sauvegarde)
    
    # Créer une progression test
    progression = systeme_sauvegarde.creer_progression_initiale("test_visiteur_2", "artiste")
    
    # Ajouter quelques actions
    systeme_sauvegarde.ajouter_action("test_visiteur_2", {
        "type": "temple_visite",
        "temple": "temple_poesie",
        "poids": 1.0
    })
    
    # Analyser le contexte de reprise
    contexte = systeme_reprise.analyser_contexte_reprise("test_visiteur_2")
    print(f"✅ Contexte analysé: {contexte.niveau_urgence}")
    print(f"✅ Suggestions: {contexte.suggestions_reprise}")
    
    # Reprendre la progression
    plan = systeme_reprise.reprendre_progression("test_visiteur_2")
    print(f"✅ Plan de reprise: {plan['choix_reprise']}")
    print(f"✅ Actions proposées: {plan['actions_proposees']}")
    
    print("🌸 Test terminé avec succès !")
