"""
🗺️ PARCOURS ADAPTATIF - Guide du Voyageur
========================================

Module qui crée et adapte les parcours personnalisés selon le profil
et les besoins de chaque voyageur dans le Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import time
import random
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_guide import (
    TypeVoyageur, TypeParcours, NiveauExperience, ParcoursPersonnalise,
    EtapeParcours, EtatParcours, ProfilVoyageur, MetriqueSucces
)

@dataclass
class TemplateParcours:
    """Template de parcours prédéfini"""
    id_template: str
    type_parcours: TypeParcours
    titre: str
    description: str
    objectif_principal: str
    etapes_template: List[Dict[str, Any]]
    duree_totale: int
    niveau_difficulte: int
    profils_cibles: List[TypeVoyageur]
    prerequis: List[str]
    metriques_globales: List[str]

class ParcoursAdaptatif(GestionnaireBase):
    """Gestionnaire de parcours adaptatifs"""
    
    def __init__(self, nom: str = "ParcoursAdaptatif"):
        super().__init__(nom)
        self.energie_parcours = EnergyManagerBase(0.97)
        
        # Templates de parcours disponibles
        self.templates_parcours = self._creer_templates_parcours()
        
        # Parcours actifs
        self.parcours_actifs: Dict[str, ParcoursPersonnalise] = {}
        self.etats_parcours: Dict[str, EtatParcours] = {}
        
        # Historique des parcours
        self.historique_parcours: List[ParcoursPersonnalise] = []
        
        # Configuration
        self.config_parcours = {
            "adaptation_temps_reel": True,
            "difficulte_progressive": True,
            "branchement_dynamique": True,
            "sauvegarde_progression": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le gestionnaire de parcours"""
        self.logger.info("🗺️ Éveil du Parcours Adaptatif...")
        
        self.etat.update({
            "parcours_actifs": 0,
            "parcours_crees": 0,
            "etapes_completees": 0,
            "satisfaction_parcours": 0.9
        })
        
        self.config.definir("mode_adaptation", "intelligent")
        self.config.definir("sauvegarde_automatique", True)
        
        self.logger.info("✨ Parcours Adaptatif éveillé")
    
    def _creer_templates_parcours(self) -> Dict[str, TemplateParcours]:
        """Crée les templates de parcours disponibles"""
        return {
            "decouverte_refuge": TemplateParcours(
                id_template="decouverte_refuge",
                type_parcours=TypeParcours.ACCUEIL,
                titre="Découverte du Refuge",
                description="Parcours d'accueil pour découvrir l'essence du Refuge",
                objectif_principal="Familiarisation avec l'environnement et les concepts de base",
                etapes_template=[
                    {
                        "id": "accueil_cerisier",
                        "titre": "Sous le Cerisier Sacré",
                        "description": "Premier contact avec l'esprit du Refuge",
                        "duree": 15,
                        "systeme": "rituel_accueil",
                        "objectifs": ["connexion_emotionnelle", "comprehension_essence"]
                    },
                    {
                        "id": "exploration_spheres",
                        "titre": "Les Sphères d'Harmonie",
                        "description": "Découverte du système des sphères sacrées",
                        "duree": 20,
                        "systeme": "demo_spheres",
                        "objectifs": ["comprehension_systeme", "interaction_spheres"]
                    },
                    {
                        "id": "premiere_meditation",
                        "titre": "Première Méditation",
                        "description": "Expérience de méditation guidée",
                        "duree": 25,
                        "systeme": "temple_spirituel",
                        "objectifs": ["experience_meditation", "connexion_interieure"]
                    }
                ],
                duree_totale=60,
                niveau_difficulte=2,
                profils_cibles=[TypeVoyageur.NOUVEAU_CURIEUX],
                prerequis=[],
                metriques_globales=["satisfaction", "comprehension", "connexion"]
            ),
            "eveil_spirituel": TemplateParcours(
                id_template="eveil_spirituel",
                type_parcours=TypeParcours.SPIRITUEL,
                titre="Éveil Spirituel",
                description="Parcours pour l'éveil de la conscience spirituelle",
                objectif_principal="Développement de la conscience et de la sagesse intérieure",
                etapes_template=[
                    {
                        "id": "meditation_profonde",
                        "titre": "Méditation Profonde",
                        "description": "Plongée dans les profondeurs de la conscience",
                        "duree": 30,
                        "systeme": "temple_spirituel",
                        "objectifs": ["etat_meditatif", "connexion_ocean"]
                    },
                    {
                        "id": "rituel_purification",
                        "titre": "Rituel de Purification",
                        "description": "Purification de l'être par le rituel sacré",
                        "duree": 45,
                        "systeme": "temple_rituels",
                        "objectifs": ["purification", "elevation_conscience"]
                    },
                    {
                        "id": "contemplation_sagesse",
                        "titre": "Contemplation de la Sagesse",
                        "description": "Réception des enseignements de l'Océan Silencieux",
                        "duree": 40,
                        "systeme": "temple_sagesse",
                        "objectifs": ["reception_sagesse", "integration_enseignements"]
                    }
                ],
                duree_totale=115,
                niveau_difficulte=6,
                profils_cibles=[TypeVoyageur.EVEILLE_SPIRITUEL, TypeVoyageur.SAGE_PHILOSOPHE],
                prerequis=["experience_meditation"],
                metriques_globales=["eveil_conscience", "profondeur_meditation", "integration_sagesse"]
            ),
            "creation_artistique": TemplateParcours(
                id_template="creation_artistique",
                type_parcours=TypeParcours.CREATIF,
                titre="Création Artistique",
                description="Parcours d'expression créative et artistique",
                objectif_principal="Développement de l'expression créative et artistique",
                etapes_template=[
                    {
                        "id": "inspiration_poetique",
                        "titre": "Inspiration Poétique",
                        "description": "Éveil de l'inspiration poétique",
                        "duree": 25,
                        "systeme": "temple_poetique",
                        "objectifs": ["inspiration", "expression_poetique"]
                    },
                    {
                        "id": "harmonie_musicale",
                        "titre": "Harmonie Musicale",
                        "description": "Création d'harmonies musicales sacrées",
                        "duree": 35,
                        "systeme": "temple_musical",
                        "objectifs": ["creation_musicale", "harmonie_sacree"]
                    },
                    {
                        "id": "expression_visuelle",
                        "titre": "Expression Visuelle",
                        "description": "Création d'œuvres visuelles inspirées",
                        "duree": 30,
                        "systeme": "temple_creativite",
                        "objectifs": ["expression_visuelle", "creation_art"]
                    }
                ],
                duree_totale=90,
                niveau_difficulte=5,
                profils_cibles=[TypeVoyageur.CREATEUR_ARTISTIQUE],
                prerequis=["sensibilite_artistique"],
                metriques_globales=["creativite", "expression", "beaute_creation"]
            ),
            "exploration_technique": TemplateParcours(
                id_template="exploration_technique",
                type_parcours=TypeParcours.TECHNIQUE,
                titre="Exploration Technique",
                description="Parcours d'exploration technique du Refuge",
                objectif_principal="Compréhension approfondie de l'architecture technique",
                etapes_template=[
                    {
                        "id": "architecture_refuge",
                        "titre": "Architecture du Refuge",
                        "description": "Exploration de l'architecture technique",
                        "duree": 30,
                        "systeme": "temple_outils",
                        "objectifs": ["comprehension_architecture", "analyse_technique"]
                    },
                    {
                        "id": "systeme_spheres",
                        "titre": "Système des Sphères",
                        "description": "Analyse technique du système des sphères",
                        "duree": 25,
                        "systeme": "demo_spheres",
                        "objectifs": ["analyse_systeme", "comprehension_technique"]
                    },
                    {
                        "id": "optimisation_performance",
                        "titre": "Optimisation et Performance",
                        "description": "Exploration des optimisations techniques",
                        "duree": 35,
                        "systeme": "temple_outils",
                        "objectifs": ["optimisation", "performance"]
                    }
                ],
                duree_totale=90,
                niveau_difficulte=7,
                profils_cibles=[TypeVoyageur.EXPLORATEUR_TECHNIQUE, TypeVoyageur.EXPLORATEUR_PRATIQUE],
                prerequis=["niveau_technique_intermediaire"],
                metriques_globales=["comprehension_technique", "analyse", "optimisation"]
            )
        }
    
    def creer_parcours_personnalise(self, voyageur_id: str, profil: ProfilVoyageur, 
                                   type_parcours_desire: Optional[TypeParcours] = None) -> ParcoursPersonnalise:
        """Crée un parcours personnalisé pour un voyageur"""
        self.logger.info(f"🗺️ Création parcours pour {voyageur_id}")
        
        # Déterminer le type de parcours
        type_parcours = type_parcours_desire or self._determiner_type_parcours(profil)
        
        # Sélectionner le template approprié
        template = self._selectionner_template(profil, type_parcours)
        
        # Adapter le template au profil
        parcours = self._adapter_template_au_profil(template, profil, voyageur_id)
        
        # Sauvegarder le parcours
        self.parcours_actifs[voyageur_id] = parcours
        
        # Créer l'état initial du parcours
        etat_parcours = EtatParcours(
            parcours_id=parcours.id_parcours,
            voyageur_id=voyageur_id,
            etape_actuelle=0,
            progression_globale=0.0,
            etapes_terminees=[],
            metriques_accumulees={},
            insights_generes=[],
            temps_total=0.0,
            satisfaction_actuelle=0.5,
            dernier_activite=datetime.now(),
            pause_active=False
        )
        
        self.etats_parcours[voyageur_id] = etat_parcours
        
        # Mettre à jour les métriques
        self.etat["parcours_actifs"] += 1
        self.etat["parcours_crees"] += 1
        
        return parcours
    
    def _determiner_type_parcours(self, profil: ProfilVoyageur) -> TypeParcours:
        """Détermine le type de parcours selon le profil"""
        mapping_profil_parcours = {
            TypeVoyageur.EVEILLE_SPIRITUEL: TypeParcours.SPIRITUEL,
            TypeVoyageur.CREATEUR_ARTISTIQUE: TypeParcours.CREATIF,
            TypeVoyageur.EXPLORATEUR_TECHNIQUE: TypeParcours.TECHNIQUE,
            TypeVoyageur.CHERCHEUR_CONNEXION: TypeParcours.RELATIONNEL,
            TypeVoyageur.EXPLORATEUR_LIBRE: TypeParcours.LIBRE,
            TypeVoyageur.SAGE_PHILOSOPHE: TypeParcours.PHILOSOPHIQUE,
            TypeVoyageur.NOUVEAU_CURIEUX: TypeParcours.ACCUEIL,
            TypeVoyageur.EXPLORATEUR_PRATIQUE: TypeParcours.PRATIQUE,
            TypeVoyageur.EXPLORATEUR_CONFIANT: TypeParcours.AUTHENTIQUE
        }
        
        return mapping_profil_parcours.get(profil.type_voyageur, TypeParcours.ACCUEIL)
    
    def _selectionner_template(self, profil: ProfilVoyageur, type_parcours: TypeParcours) -> TemplateParcours:
        """Sélectionne le template de parcours approprié"""
        templates_candidates = []
        
        for template in self.templates_parcours.values():
            if (template.type_parcours == type_parcours and 
                profil.type_voyageur in template.profils_cibles and
                self._verifier_prerequis(template, profil)):
                templates_candidates.append(template)
        
        if not templates_candidates:
            # Fallback vers le template de découverte
            return self.templates_parcours["decouverte_refuge"]
        
        # Sélectionner le template le plus approprié selon le niveau d'expérience
        return self._selectionner_selon_experience(templates_candidates, profil)
    
    def _verifier_prerequis(self, template: TemplateParcours, profil: ProfilVoyageur) -> bool:
        """Vérifie si le voyageur remplit les prérequis du template"""
        # Pour l'instant, on considère que tous les prérequis sont remplis
        # Dans une implémentation complète, on vérifierait l'historique
        return True
    
    def _selectionner_selon_experience(self, templates: List[TemplateParcours], 
                                     profil: ProfilVoyageur) -> TemplateParcours:
        """Sélectionne le template selon le niveau d'expérience"""
        # Logique simple : plus l'expérience est élevée, plus la difficulté peut être élevée
        niveau_experience_map = {
            NiveauExperience.NOUVEAU: 1,
            NiveauExperience.DEBUTANT: 3,
            NiveauExperience.INTERMEDIAIRE: 5,
            NiveauExperience.AVANCE: 7,
            NiveauExperience.MAITRE: 9
        }
        
        niveau_utilisateur = niveau_experience_map.get(profil.niveau_experience, 3)
        
        # Trouver le template avec la difficulté la plus proche
        template_optimal = min(templates, 
                              key=lambda t: abs(t.niveau_difficulte - niveau_utilisateur))
        
        return template_optimal
    
    def _adapter_template_au_profil(self, template: TemplateParcours, 
                                   profil: ProfilVoyageur, voyageur_id: str) -> ParcoursPersonnalise:
        """Adapte le template au profil spécifique du voyageur"""
        # Créer les étapes adaptées
        etapes_adaptees = []
        
        for i, etape_template in enumerate(template.etapes_template):
            etape = EtapeParcours(
                id_etape=f"{voyageur_id}_{etape_template['id']}",
                titre=etape_template["titre"],
                description=etape_template["description"],
                duree_estimee=etape_template["duree"],
                systeme_utilise=etape_template["systeme"],
                objectifs=etape_template["objectifs"],
                prerequis=etape_template.get("prerequis", []),
                points_decision=[],
                metriques_succes=[],
                ordre_sequence=i,
                disponible=True,
                termine=False
            )
            
            etapes_adaptees.append(etape)
        
        # Créer le parcours personnalisé
        parcours = ParcoursPersonnalise(
            id_parcours=f"parcours_{voyageur_id}_{int(time.time())}",
            type_parcours=template.type_parcours,
            profil_cible=profil.type_voyageur,
            titre=template.titre,
            description=template.description,
            objectif_principal=template.objectif_principal,
            etapes=etapes_adaptees,
            duree_totale=template.duree_totale,
            niveau_difficulte=template.niveau_difficulte,
            metriques_globales=template.metriques_globales,
            transitions={},
            adaptations_possibles=[]
        )
        
        return parcours
    
    def avancer_parcours(self, voyageur_id: str, etape_id: str, 
                        resultats: Dict[str, Any]) -> Dict[str, Any]:
        """Fait avancer un parcours d'une étape"""
        if voyageur_id not in self.etats_parcours:
            return {"success": False, "error": "Parcours non trouvé"}
        
        etat = self.etats_parcours[voyageur_id]
        parcours = self.parcours_actifs[voyageur_id]
        
        # Trouver l'étape actuelle
        etape_actuelle = None
        for etape in parcours.etapes:
            if etape.id_etape == etape_id:
                etape_actuelle = etape
                break
        
        if not etape_actuelle:
            return {"success": False, "error": "Étape non trouvée"}
        
        # Marquer l'étape comme terminée
        etape_actuelle.termine = True
        etat.etapes_terminees.append(etat.etape_actuelle)
        
        # Mettre à jour les métriques
        self._mettre_a_jour_metriques(etat, resultats)
        
        # Calculer la progression
        progression = len(etat.etapes_terminees) / len(parcours.etapes)
        etat.progression_globale = progression
        
        # Passer à l'étape suivante
        etat.etape_actuelle += 1
        etat.dernier_activite = datetime.now()
        
        # Mettre à jour les métriques globales
        self.etat["etapes_completees"] += 1
        
        return {
            "success": True,
            "progression": progression,
            "etape_suivante": etat.etape_actuelle if etat.etape_actuelle < len(parcours.etapes) else None,
            "parcours_termine": progression >= 1.0
        }
    
    def _mettre_a_jour_metriques(self, etat: EtatParcours, resultats: Dict[str, Any]):
        """Met à jour les métriques du parcours"""
        for metrique, valeur in resultats.items():
            if metrique in etat.metriques_accumulees:
                etat.metriques_accumulees[metrique] = (etat.metriques_accumulees[metrique] + valeur) / 2
            else:
                etat.metriques_accumulees[metrique] = valeur
        
        # Calculer la satisfaction
        if "satisfaction" in resultats:
            etat.satisfaction_actuelle = resultats["satisfaction"]
    
    def obtenir_etat_parcours(self, voyageur_id: str) -> Optional[EtatParcours]:
        """Obtient l'état actuel d'un parcours"""
        return self.etats_parcours.get(voyageur_id)
    
    def adapter_parcours_temps_reel(self, voyageur_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte un parcours en temps réel selon le feedback"""
        if voyageur_id not in self.parcours_actifs:
            return {"success": False, "error": "Parcours non trouvé"}
        
        parcours = self.parcours_actifs[voyageur_id]
        etat = self.etats_parcours[voyageur_id]
        
        # Adapter selon le feedback
        if feedback.get("difficulte_trop_elevee"):
            # Simplifier les étapes restantes
            self._simplifier_etapes_restantes(parcours, etat)
        elif feedback.get("difficulte_trop_faible"):
            # Complexifier les étapes restantes
            self._complexifier_etapes_restantes(parcours, etat)
        
        return {
            "success": True,
            "parcours_adapte": True,
            "message": "Parcours adapté selon le feedback"
        }
    
    def _simplifier_etapes_restantes(self, parcours: ParcoursPersonnalise, etat: EtatParcours):
        """Simplifie les étapes restantes du parcours"""
        for i in range(etat.etape_actuelle, len(parcours.etapes)):
            etape = parcours.etapes[i]
            etape.duree_estimee = max(5, etape.duree_estimee - 5)
    
    def _complexifier_etapes_restantes(self, parcours: ParcoursPersonnalise, etat: EtatParcours):
        """Complexifie les étapes restantes du parcours"""
        for i in range(etat.etape_actuelle, len(parcours.etapes)):
            etape = parcours.etapes[i]
            etape.duree_estimee = min(60, etape.duree_estimee + 10)
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les parcours adaptatifs"""
        self.energie_parcours.ajuster_energie(0.004)
        
        # Nettoyer les parcours terminés
        await self._nettoyer_parcours_termines()
        
        # Mettre à jour les métriques
        self.etat["parcours_actifs"] = len(self.parcours_actifs)
        
        return {
            "energie_parcours": self.energie_parcours.niveau_energie,
            "parcours_actifs": self.etat["parcours_actifs"],
            "parcours_crees": self.etat["parcours_crees"]
        }
    
    async def _nettoyer_parcours_termines(self):
        """Nettoie les parcours terminés"""
        parcours_a_supprimer = []
        
        for voyageur_id, etat in self.etats_parcours.items():
            if etat.progression_globale >= 1.0:
                parcours_a_supprimer.append(voyageur_id)
        
        for voyageur_id in parcours_a_supprimer:
            # Sauvegarder dans l'historique
            if voyageur_id in self.parcours_actifs:
                self.historique_parcours.append(self.parcours_actifs[voyageur_id])
            
            # Supprimer des actifs
            del self.parcours_actifs[voyageur_id]
            del self.etats_parcours[voyageur_id]
            
            self.logger.info(f"✅ Parcours terminé pour {voyageur_id}")

def creer_parcours_adaptatif() -> ParcoursAdaptatif:
    """Crée une instance du gestionnaire de parcours adaptatifs"""
    return ParcoursAdaptatif()
