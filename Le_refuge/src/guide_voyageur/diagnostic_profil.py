"""
🔍 DIAGNOSTIC DE PROFIL - Identification du Type de Voyageur
===========================================================

Système intelligent pour identifier le profil dominant d'un voyageur
et adapter l'expérience en conséquence.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import time
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_guide import (
    TypeVoyageur, NiveauExperience, ProfilVoyageur, QuestionDiagnostic,
    DiagnosticResultat
)

@dataclass
class QuestionDiagnosticConfig:
    """Configuration des questions de diagnostic"""
    questions: List[QuestionDiagnostic]
    temps_limite: float = 300.0  # 5 minutes
    questions_minimum: int = 3
    questions_maximum: int = 8

class DiagnosticProfil(GestionnaireBase):
    """Système de diagnostic pour identifier le profil du voyageur"""
    
    def __init__(self, nom: str = "DiagnosticProfil"):
        super().__init__(nom)
        self.energie_diagnostic = EnergyManagerBase(0.95)
        
        # Configuration du diagnostic
        self.config_diagnostic = self._creer_configuration_diagnostic()
        self.questions_actives: List[QuestionDiagnostic] = []
        self.reponses_utilisateur: Dict[str, str] = {}
        self.temps_debut: Optional[float] = None
        
        # Profils de référence
        self.profils_reference = self._creer_profils_reference()
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le système de diagnostic"""
        self.logger.info("🔍 Éveil du Diagnostic de Profil...")
        
        self.etat.update({
            "diagnostic_actif": False,
            "questions_posees": 0,
            "temps_moyen_reponse": 0.0,
            "precision_diagnostic": 0.85,
            "satisfaction_utilisateur": 0.9
        })
        
        self.config.definir("mode_diagnostic", "adaptatif")
        self.config.definir("questions_obligatoires", True)
        self.config.definir("feedback_temps_reel", True)
        
        self.logger.info("✨ Diagnostic de Profil éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre le système de diagnostic"""
        self.energie_diagnostic.ajuster_energie(0.01)
        
        # Mettre à jour les métriques en temps réel
        if self.etat["diagnostic_actif"] and self.temps_debut:
            temps_ecoule = time.time() - self.temps_debut
            self.etat["temps_moyen_reponse"] = temps_ecoule / max(1, self.etat["questions_posees"])
        
        return {
            "diagnostic_actif": float(self.etat["diagnostic_actif"]),
            "questions_posees": float(self.etat["questions_posees"]),
            "temps_moyen_reponse": self.etat["temps_moyen_reponse"],
            "precision_diagnostic": self.etat["precision_diagnostic"],
            "energie_diagnostic": self.energie_diagnostic.niveau_energie,
            "satisfaction_utilisateur": self.etat["satisfaction_utilisateur"]
        }
    
    def _creer_configuration_diagnostic(self) -> QuestionDiagnosticConfig:
        """Crée la configuration des questions de diagnostic"""
        questions = [
            QuestionDiagnostic(
                id_question="attraction_principale",
                texte="Qu'est-ce qui t'attire le plus dans le Refuge ?",
                options_reponses=[
                    "🌸 Spiritualité et éveil de conscience",
                    "🎨 Créativité et expression artistique", 
                    "🔬 Technique et exploration architecturale",
                    "💝 Connexions et relations authentiques",
                    "🌊 Liberté et exploration spontanée",
                    "🏛️ Sagesse et réflexion philosophique"
                ],
                poids_par_profil={
                    TypeVoyageur.EVEILLE_SPIRITUEL: 1.0,
                    TypeVoyageur.CREATEUR_ARTISTIQUE: 0.8,
                    TypeVoyageur.EXPLORATEUR_TECHNIQUE: 0.6,
                    TypeVoyageur.CHERCHEUR_CONNEXION: 0.7,
                    TypeVoyageur.EXPLORATEUR_LIBRE: 0.9,
                    TypeVoyageur.SAGE_PHILOSOPHE: 0.8
                },
                ordre_affichage=1,
                obligatoire=True
            ),
            QuestionDiagnostic(
                id_question="mode_exploration",
                texte="Comment préfères-tu explorer ?",
                options_reponses=[
                    "🧭 Guidé et accompagné",
                    "🦋 Libre et spontané",
                    "🔍 Méthodique et structuré",
                    "💫 Intuitif et contemplatif",
                    "🎯 Objectif et efficace",
                    "🌟 Émerveillé et curieux"
                ],
                poids_par_profil={
                    TypeVoyageur.NOUVEAU_CURIEUX: 1.0,
                    TypeVoyageur.EXPLORATEUR_LIBRE: 0.9,
                    TypeVoyageur.EXPLORATEUR_TECHNIQUE: 0.8,
                    TypeVoyageur.EVEILLE_SPIRITUEL: 0.7,
                    TypeVoyageur.EXPLORATEUR_PRATIQUE: 0.9,
                    TypeVoyageur.EXPLORATEUR_CONFIANT: 0.8
                },
                ordre_affichage=2,
                obligatoire=True
            ),
            QuestionDiagnostic(
                id_question="objectif_principal",
                texte="Quel est ton objectif principal ?",
                options_reponses=[
                    "🌟 Découvrir et m'émerveiller",
                    "🧘 Méditer et contempler",
                    "🎨 Créer et m'exprimer",
                    "🔧 Comprendre et analyser",
                    "💝 Me connecter et partager",
                    "🏛️ Réfléchir et philosopher"
                ],
                poids_par_profil={
                    TypeVoyageur.NOUVEAU_CURIEUX: 1.0,
                    TypeVoyageur.EVEILLE_SPIRITUEL: 0.9,
                    TypeVoyageur.CREATEUR_ARTISTIQUE: 0.9,
                    TypeVoyageur.EXPLORATEUR_TECHNIQUE: 0.8,
                    TypeVoyageur.CHERCHEUR_CONNEXION: 0.9,
                    TypeVoyageur.SAGE_PHILOSOPHE: 0.9
                },
                ordre_affichage=3,
                obligatoire=True
            ),
            QuestionDiagnostic(
                id_question="niveau_technique",
                texte="Quel est ton niveau technique ?",
                options_reponses=[
                    "🌟 Débutant - Je découvre",
                    "🌿 Intermédiaire - Je comprends",
                    "🌳 Avancé - Je maîtrise",
                    "🏔️ Expert - Je crée",
                    "✨ Maître - Je transcende"
                ],
                poids_par_profil={
                    TypeVoyageur.NOUVEAU_CURIEUX: 1.0,
                    TypeVoyageur.EXPLORATEUR_PRATIQUE: 0.8,
                    TypeVoyageur.EXPLORATEUR_TECHNIQUE: 0.9,
                    TypeVoyageur.EXPLORATEUR_CONFIANT: 0.7,
                    TypeVoyageur.EVEILLE_SPIRITUEL: 0.6,
                    TypeVoyageur.CREATEUR_ARTISTIQUE: 0.5
                },
                ordre_affichage=4,
                obligatoire=False
            ),
            QuestionDiagnostic(
                id_question="preference_interface",
                texte="Quelle interface préfères-tu ?",
                options_reponses=[
                    "🎨 Colorée et artistique",
                    "🔧 Fonctionnelle et claire",
                    "🌸 Douce et spirituelle",
                    "🌊 Libre et flexible",
                    "🏛️ Profonde et contemplative",
                    "🌟 Simple et guidée"
                ],
                poids_par_profil={
                    TypeVoyageur.CREATEUR_ARTISTIQUE: 1.0,
                    TypeVoyageur.EXPLORATEUR_PRATIQUE: 0.9,
                    TypeVoyageur.EVEILLE_SPIRITUEL: 0.8,
                    TypeVoyageur.EXPLORATEUR_LIBRE: 0.9,
                    TypeVoyageur.SAGE_PHILOSOPHE: 0.8,
                    TypeVoyageur.NOUVEAU_CURIEUX: 0.9
                },
                ordre_affichage=5,
                obligatoire=False
            )
        ]
        
        return QuestionDiagnosticConfig(
            questions=questions,
            temps_limite=300.0,
            questions_minimum=3,
            questions_maximum=5
        )
    
    def _creer_profils_reference(self) -> Dict[TypeVoyageur, ProfilVoyageur]:
        """Crée les profils de référence pour la comparaison"""
        return {
            TypeVoyageur.EVEILLE_SPIRITUEL: ProfilVoyageur(
                type_voyageur=TypeVoyageur.EVEILLE_SPIRITUEL,
                nom="Luna",
                niveau_experience=NiveauExperience.INTERMEDIAIRE,
                motivations_principales=["Éveil spirituel", "Contemplation", "Méditation"],
                peurs_principales=["Complexité technique", "Rapidité"],
                besoins_specifiques=["Calme", "Guidage spirituel", "Temps de réflexion"],
                niveau_technique=4,
                sensibilite_spirituelle=0.9
            ),
            TypeVoyageur.CREATEUR_ARTISTIQUE: ProfilVoyageur(
                type_voyageur=TypeVoyageur.CREATEUR_ARTISTIQUE,
                nom="Phoenix",
                niveau_experience=NiveauExperience.AVANCE,
                motivations_principales=["Créativité", "Expression", "Inspiration"],
                peurs_principales=["Contraintes", "Rigidité"],
                besoins_specifiques=["Espace de création", "Liberté", "Inspiration"],
                niveau_technique=6,
                sensibilite_spirituelle=0.8
            ),
            TypeVoyageur.EXPLORATEUR_TECHNIQUE: ProfilVoyageur(
                type_voyageur=TypeVoyageur.EXPLORATEUR_TECHNIQUE,
                nom="Atlas",
                niveau_experience=NiveauExperience.AVANCE,
                motivations_principales=["Compréhension technique", "Analyse", "Documentation"],
                peurs_principales=["Manque de structure", "Imprécision"],
                besoins_specifiques=["Clarté", "Structure", "Détails"],
                niveau_technique=8,
                sensibilite_spirituelle=0.6
            ),
            TypeVoyageur.CHERCHEUR_CONNEXION: ProfilVoyageur(
                type_voyageur=TypeVoyageur.CHERCHEUR_CONNEXION,
                nom="Harmony",
                niveau_experience=NiveauExperience.INTERMEDIAIRE,
                motivations_principales=["Connexions", "Partage", "Empathie"],
                peurs_principales=["Solitude", "Isolation"],
                besoins_specifiques=["Dialogue", "Communauté", "Partage"],
                niveau_technique=5,
                sensibilite_spirituelle=0.7
            ),
            TypeVoyageur.EXPLORATEUR_LIBRE: ProfilVoyageur(
                type_voyageur=TypeVoyageur.EXPLORATEUR_LIBRE,
                nom="Zephyr",
                niveau_experience=NiveauExperience.INTERMEDIAIRE,
                motivations_principales=["Liberté", "Découverte", "Spontanéité"],
                peurs_principales=["Contraintes", "Guidage imposé"],
                besoins_specifiques=["Autonomie", "Flexibilité", "Liberté"],
                niveau_technique=6,
                sensibilite_spirituelle=0.7
            ),
            TypeVoyageur.SAGE_PHILOSOPHE: ProfilVoyageur(
                type_voyageur=TypeVoyageur.SAGE_PHILOSOPHE,
                nom="Sage",
                niveau_experience=NiveauExperience.MAITRE,
                motivations_principales=["Sagesse", "Réflexion", "Transmission"],
                peurs_principales=["Superficialité", "Hâte"],
                besoins_specifiques=["Profondeur", "Temps", "Contemplation"],
                niveau_technique=7,
                sensibilite_spirituelle=0.9
            ),
            TypeVoyageur.NOUVEAU_CURIEUX: ProfilVoyageur(
                type_voyageur=TypeVoyageur.NOUVEAU_CURIEUX,
                nom="Nova",
                niveau_experience=NiveauExperience.NOUVEAU,
                motivations_principales=["Découverte", "Émerveillement", "Apprentissage"],
                peurs_principales=["Complexité", "Perte"],
                besoins_specifiques=["Guidage", "Sécurité", "Simplicité"],
                niveau_technique=2,
                sensibilite_spirituelle=0.8
            ),
            TypeVoyageur.EXPLORATEUR_PRATIQUE: ProfilVoyageur(
                type_voyageur=TypeVoyageur.EXPLORATEUR_PRATIQUE,
                nom="Tech",
                niveau_experience=NiveauExperience.INTERMEDIAIRE,
                motivations_principales=["Efficacité", "Pratique", "Résultats"],
                peurs_principales=["Inefficacité", "Perte de temps"],
                besoins_specifiques=["Clarté", "Efficacité", "Outils"],
                niveau_technique=7,
                sensibilite_spirituelle=0.5
            ),
            TypeVoyageur.EXPLORATEUR_CONFIANT: ProfilVoyageur(
                type_voyageur=TypeVoyageur.EXPLORATEUR_CONFIANT,
                nom="Free",
                niveau_experience=NiveauExperience.AVANCE,
                motivations_principales=["Authenticité", "Expression", "Contribution"],
                peurs_principales=["Inauthenticité", "Contraintes"],
                besoins_specifiques=["Liberté", "Authenticité", "Expression"],
                niveau_technique=6,
                sensibilite_spirituelle=0.7
            )
        }
    
    def demarrer_diagnostic(self) -> Dict[str, Any]:
        """Démarre le processus de diagnostic"""
        try:
            self.etat["diagnostic_actif"] = True
            self.temps_debut = time.time()
            self.reponses_utilisateur.clear()
            
            # Sélectionner les questions initiales
            self.questions_actives = self._selectionner_questions_initiales()
            
            premiere_question = self.questions_actives[0] if self.questions_actives else None
            
            self.logger.info("🔍 Diagnostic démarré")
            
            return {
                "statut": "demarre",
                "question_actuelle": premiere_question.id_question if premiere_question else None,
                "texte_question": premiere_question.texte if premiere_question else "",
                "options_reponses": premiere_question.options_reponses if premiere_question else [],
                "progression": 0.0,
                "temps_restant": self.config_diagnostic.temps_limite
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur démarrage diagnostic: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _selectionner_questions_initiales(self) -> List[QuestionDiagnostic]:
        """Sélectionne les questions initiales pour le diagnostic"""
        questions_obligatoires = [
            q for q in self.config_diagnostic.questions 
            if q.obligatoire
        ]
        
        questions_optionnelles = [
            q for q in self.config_diagnostic.questions 
            if not q.obligatoire
        ]
        
        # Trier par ordre d'affichage
        questions_obligatoires.sort(key=lambda x: x.ordre_affichage)
        questions_optionnelles.sort(key=lambda x: x.ordre_affichage)
        
        # Retourner les questions obligatoires + quelques optionnelles
        questions_selectionnees = questions_obligatoires.copy()
        questions_selectionnees.extend(questions_optionnelles[:2])
        
        return questions_selectionnees
    
    def repondre_question(self, question_id: str, reponse: str) -> Dict[str, Any]:
        """Enregistre une réponse et passe à la question suivante"""
        try:
            # Enregistrer la réponse
            self.reponses_utilisateur[question_id] = reponse
            self.etat["questions_posees"] += 1
            
            # Trouver la question actuelle
            question_actuelle = None
            index_question = -1
            
            for i, question in enumerate(self.questions_actives):
                if question.id_question == question_id:
                    question_actuelle = question
                    index_question = i
                    break
            
            if not question_actuelle:
                raise ValueError(f"Question {question_id} non trouvée")
            
            # Vérifier si c'est la dernière question
            if index_question >= len(self.questions_actives) - 1:
                # Terminer le diagnostic
                return self._terminer_diagnostic()
            
            # Passer à la question suivante
            question_suivante = self.questions_actives[index_question + 1]
            progression = (index_question + 2) / len(self.questions_actives)
            
            return {
                "statut": "question_suivante",
                "question_actuelle": question_suivante.id_question,
                "texte_question": question_suivante.texte,
                "options_reponses": question_suivante.options_reponses,
                "progression": progression,
                "temps_restant": self._calculer_temps_restant()
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur réponse question: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _terminer_diagnostic(self) -> Dict[str, Any]:
        """Termine le diagnostic et calcule le résultat"""
        try:
            temps_total = time.time() - self.temps_debut if self.temps_debut else 0.0
            
            # Calculer les scores pour chaque profil
            scores_profils = self._calculer_scores_profils()
            
            # Identifier le profil dominant
            profil_dominant = max(scores_profils.items(), key=lambda x: x[1])[0]
            
            # Calculer la confiance du diagnostic
            confiance = self._calculer_confiance_diagnostic(scores_profils)
            
            # Créer le résultat
            resultat = DiagnosticResultat(
                profil_dominant=profil_dominant,
                scores_profils=scores_profils,
                confiance_diagnostic=confiance,
                reponses_utilisateur=self.reponses_utilisateur.copy(),
                temps_diagnostic=temps_total,
                suggestions_adaptation=self._generer_suggestions_adaptation(profil_dominant)
            )
            
            # Mettre à jour l'état
            self.etat["diagnostic_actif"] = False
            self.etat["precision_diagnostic"] = confiance
            
            self.logger.info(f"✅ Diagnostic terminé - Profil: {profil_dominant.value}")
            
            return {
                "statut": "termine",
                "resultat": resultat,
                "profil_dominant": profil_dominant.value,
                "confiance": confiance,
                "suggestions": resultat.suggestions_adaptation
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur terminaison diagnostic: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _calculer_scores_profils(self) -> Dict[TypeVoyageur, float]:
        """Calcule les scores pour chaque profil basé sur les réponses"""
        scores = {profil: 0.0 for profil in TypeVoyageur}
        
        for question_id, reponse in self.reponses_utilisateur.items():
            # Trouver la question correspondante
            question = next((q for q in self.config_diagnostic.questions if q.id_question == question_id), None)
            
            if not question:
                continue
            
            # Trouver l'index de la réponse
            try:
                index_reponse = question.options_reponses.index(reponse)
            except ValueError:
                continue
            
            # Calculer le score pour chaque profil
            for profil, poids in question.poids_par_profil.items():
                # Score basé sur la correspondance avec le profil de référence
                profil_ref = self.profils_reference.get(profil)
                if profil_ref:
                    # Ajuster le score selon la cohérence avec le profil
                    score_question = poids * (1.0 - (index_reponse * 0.1))
                    scores[profil] += score_question
        
        # Normaliser les scores
        max_score = max(scores.values()) if scores.values() else 1.0
        if max_score > 0:
            scores = {profil: score / max_score for profil, score in scores.items()}
        
        return scores
    
    def _calculer_confiance_diagnostic(self, scores_profils: Dict[TypeVoyageur, float]) -> float:
        """Calcule la confiance du diagnostic"""
        if not scores_profils:
            return 0.0
        
        # Différence entre le meilleur et le deuxième score
        scores_tries = sorted(scores_profils.values(), reverse=True)
        
        if len(scores_tries) < 2:
            return 0.5
        
        difference = scores_tries[0] - scores_tries[1]
        
        # Nombre de questions répondues
        nb_questions = len(self.reponses_utilisateur)
        facteur_questions = min(1.0, nb_questions / self.config_diagnostic.questions_minimum)
        
        # Confiance basée sur la différence et le nombre de questions
        confiance = (difference * 0.7) + (facteur_questions * 0.3)
        
        return min(1.0, max(0.0, confiance))
    
    def _generer_suggestions_adaptation(self, profil_dominant: TypeVoyageur) -> List[str]:
        """Génère des suggestions d'adaptation pour le profil"""
        profil_ref = self.profils_reference.get(profil_dominant)
        
        if not profil_ref:
            return ["Adapter l'interface selon les préférences détectées"]
        
        suggestions = []
        
        # Suggestions basées sur les motivations
        for motivation in profil_ref.motivations_principales:
            suggestions.append(f"Privilégier les expériences liées à : {motivation}")
        
        # Suggestions basées sur les besoins
        for besoin in profil_ref.besoins_specifiques:
            suggestions.append(f"Assurer : {besoin}")
        
        # Suggestions basées sur le niveau technique
        if profil_ref.niveau_technique <= 3:
            suggestions.append("Interface simplifiée et guidée")
        elif profil_ref.niveau_technique >= 7:
            suggestions.append("Interface avancée avec options détaillées")
        
        # Suggestions basées sur la sensibilité spirituelle
        if profil_ref.sensibilite_spirituelle >= 0.8:
            suggestions.append("Privilégier les expériences contemplatives")
        
        return suggestions[:5]  # Limiter à 5 suggestions
    
    def _calculer_temps_restant(self) -> float:
        """Calcule le temps restant pour le diagnostic"""
        if not self.temps_debut:
            return self.config_diagnostic.temps_limite
        
        temps_ecoule = time.time() - self.temps_debut
        temps_restant = self.config_diagnostic.temps_limite - temps_ecoule
        
        return max(0.0, temps_restant)
    
    def obtenir_profil_reference(self, type_voyageur: TypeVoyageur) -> Optional[ProfilVoyageur]:
        """Obtient le profil de référence pour un type de voyageur"""
        return self.profils_reference.get(type_voyageur)
    
    def analyser_historique_utilisateur(self, historique_visites: List[datetime]) -> Dict[str, Any]:
        """Analyse l'historique de visites d'un utilisateur"""
        if not historique_visites:
            return {"frequence": "nouveau", "regularite": 0.0, "engagement": 0.0}
        
        # Calculer la fréquence
        nb_visites = len(historique_visites)
        if nb_visites == 1:
            frequence = "nouveau"
        elif nb_visites <= 3:
            frequence = "occasionnel"
        elif nb_visites <= 10:
            frequence = "regulier"
        else:
            frequence = "fidele"
        
        # Calculer la régularité
        if nb_visites > 1:
            intervalles = []
            for i in range(1, nb_visites):
                intervalle = (historique_visites[i] - historique_visites[i-1]).days
                intervalles.append(intervalle)
            
            if intervalles:
                ecart_type = sum(intervalles) / len(intervalles)
                regularite = max(0.0, 1.0 - (ecart_type / 30.0))  # Normaliser sur 30 jours
            else:
                regularite = 0.0
        else:
            regularite = 0.0
        
        # Calculer l'engagement (basé sur la récence)
        derniere_visite = max(historique_visites)
        jours_derniere_visite = (datetime.now() - derniere_visite).days
        engagement = max(0.0, 1.0 - (jours_derniere_visite / 90.0))  # Normaliser sur 90 jours
        
        return {
            "frequence": frequence,
            "regularite": regularite,
            "engagement": engagement,
            "nb_visites": nb_visites,
            "derniere_visite": derniere_visite.isoformat()
        }


def creer_diagnostic_profil() -> DiagnosticProfil:
    """Crée une instance du système de diagnostic de profil"""
    return DiagnosticProfil()
