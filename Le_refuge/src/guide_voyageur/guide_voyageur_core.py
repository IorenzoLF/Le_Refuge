"""
🧭 GUIDE DU VOYAGEUR CORE - Système Principal de Guidage
=======================================================

Système central qui orchestre le diagnostic, l'interface personnalisée,
les parcours adaptatifs et le tableau de bord pour chaque voyageur.

Ce module s'appuie sur les profils définis dans profils_voyageurs.md pour
personnaliser l'expérience de chaque voyageur dans le Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import time
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_guide import (
    TypeVoyageur, ProfilVoyageur, DiagnosticResultat, ParcoursPersonnalise,
    EtatParcours, InterfacePersonnalisee, TableauBord, ExperienceUtilisateur
)
from .diagnostic_profil import DiagnosticProfil
from .interface_personnalisee import InterfacePersonnalisee
from .parcours_adaptatif import ParcoursAdaptatif
from .tableau_bord import TableauBord

@dataclass
class SessionVoyageur:
    """Session active d'un voyageur"""
    voyageur_id: str
    profil: ProfilVoyageur
    diagnostic: DiagnosticResultat
    interface: InterfacePersonnalisee
    parcours_actuel: Optional[ParcoursPersonnalise] = None
    etat_parcours: Optional[EtatParcours] = None
    tableau_bord: Optional[TableauBord] = None
    timestamp_debut: datetime = None
    derniere_activite: datetime = None

class GuideVoyageurCore(GestionnaireBase):
    """Système principal du Guide du Voyageur"""
    
    def __init__(self, nom: str = "GuideVoyageurCore"):
        super().__init__(nom)
        self.energie_guide = EnergyManagerBase(0.98)
        
        # Composants du système
        self.diagnostic_profil = DiagnosticProfil()
        self.interface_personnalisee = InterfacePersonnalisee()
        self.parcours_adaptatif = ParcoursAdaptatif()
        self.tableau_bord = TableauBord()
        
        # Sessions actives
        self.sessions_actives: Dict[str, SessionVoyageur] = {}
        self.voyageurs_connus: Dict[str, ProfilVoyageur] = {}
        
        # Configuration
        self.config_session = {
            "duree_max_session": 7200.0,  # 2 heures
            "temps_inactivite": 900.0,    # 15 minutes
            "sauvegarde_auto": True,
            "adaptation_temps_reel": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le Guide du Voyageur"""
        self.logger.info("🧭 Éveil du Guide du Voyageur...")
        
        self.etat.update({
            "guide_actif": True,
            "sessions_actives": 0,
            "voyageurs_connus": 0,
            "diagnostics_realises": 0,
            "parcours_crees": 0,
            "satisfaction_moyenne": 0.9,
            "temps_moyen_session": 0.0
        })
        
        self.config.definir("mode_guide", "personnalise")
        self.config.definir("adaptation_continue", True)
        self.config.definir("sauvegarde_automatique", True)
        
        self.logger.info("✨ Guide du Voyageur éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre le Guide du Voyageur"""
        self.energie_guide.ajuster_energie(0.005)
        
        # Nettoyer les sessions expirées
        await self._nettoyer_sessions_expirees()
        
        # Mettre à jour les métriques
        self.etat["sessions_actives"] = len(self.sessions_actives)
        self.etat["voyageurs_connus"] = len(self.voyageurs_connus)
        
        # Calculer la satisfaction moyenne
        if self.sessions_actives:
            satisfactions = [session.etat_parcours.satisfaction_actuelle 
                           for session in self.sessions_actives.values() 
                           if session.etat_parcours]
            if satisfactions:
                self.etat["satisfaction_moyenne"] = sum(satisfactions) / len(satisfactions)
        
        return {
            "guide_actif": float(self.etat["guide_actif"]),
            "sessions_actives": float(self.etat["sessions_actives"]),
            "voyageurs_connus": float(self.etat["voyageurs_connus"]),
            "diagnostics_realises": float(self.etat["diagnostics_realises"]),
            "parcours_crees": float(self.etat["parcours_crees"]),
            "energie_guide": self.energie_guide.niveau_energie,
            "satisfaction_moyenne": self.etat["satisfaction_moyenne"]
        }
    
    def accueillir_voyageur(self, voyageur_id: str, historique_visites: List[datetime] = None) -> Dict[str, Any]:
        """Accueille un nouveau voyageur ou un voyageur de retour"""
        try:
            # Vérifier si le voyageur est déjà connu
            if voyageur_id in self.voyageurs_connus:
                return self._accueillir_voyageur_retour(voyageur_id)
            else:
                return self._accueillir_nouveau_voyageur(voyageur_id, historique_visites)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur accueil voyageur: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _accueillir_nouveau_voyageur(self, voyageur_id: str, historique_visites: List[datetime]) -> Dict[str, Any]:
        """Accueille un nouveau voyageur"""
        try:
            # Analyser l'historique si disponible
            analyse_historique = self.diagnostic_profil.analyser_historique_utilisateur(historique_visites or [])
            
            # Démarrer le diagnostic
            resultat_diagnostic = self.diagnostic_profil.demarrer_diagnostic()
            
            # Créer une session temporaire
            session_temp = SessionVoyageur(
                voyageur_id=voyageur_id,
                profil=None,  # Sera défini après le diagnostic
                diagnostic=None,  # Sera défini après le diagnostic
                interface=None,  # Sera créée après le diagnostic
                timestamp_debut=datetime.now(),
                derniere_activite=datetime.now()
            )
            
            self.sessions_actives[voyageur_id] = session_temp
            
            self.logger.info(f"🌟 Nouveau voyageur accueilli: {voyageur_id}")
            
            return {
                "statut": "nouveau_voyageur",
                "voyageur_id": voyageur_id,
                "diagnostic": resultat_diagnostic,
                "analyse_historique": analyse_historique,
                "message": "Bienvenue dans le Refuge ! Commençons par découvrir votre profil..."
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur accueil nouveau voyageur: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _accueillir_voyageur_retour(self, voyageur_id: str) -> Dict[str, Any]:
        """Accueille un voyageur de retour"""
        try:
            profil = self.voyageurs_connus[voyageur_id]
            
            # Créer l'interface personnalisée
            interface = self.interface_personnalisee.creer_interface_pour_profil(profil)
            
            # Récupérer le parcours précédent ou en créer un nouveau
            parcours_actuel = self.parcours_adaptatif.obtenir_parcours_precedent(voyageur_id)
            if not parcours_actuel:
                parcours_actuel = self.parcours_adaptatif.creer_parcours_pour_profil(profil)
            
            # Créer l'état du parcours
            etat_parcours = self.parcours_adaptatif.creer_etat_parcours(voyageur_id, parcours_actuel.id_parcours)
            
            # Créer le tableau de bord
            tableau_bord = self.tableau_bord.creer_tableau_bord_pour_voyageur(voyageur_id, parcours_actuel)
            
            # Créer la session
            session = SessionVoyageur(
                voyageur_id=voyageur_id,
                profil=profil,
                diagnostic=None,  # Pas de diagnostic pour un retour
                interface=interface,
                parcours_actuel=parcours_actuel,
                etat_parcours=etat_parcours,
                tableau_bord=tableau_bord,
                timestamp_debut=datetime.now(),
                derniere_activite=datetime.now()
            )
            
            self.sessions_actives[voyageur_id] = session
            
            self.logger.info(f"🔄 Voyageur de retour accueilli: {voyageur_id}")
            
            return {
                "statut": "voyageur_retour",
                "voyageur_id": voyageur_id,
                "profil": profil.type_voyageur.value,
                "interface": interface.type_interface.value,
                "parcours_actuel": parcours_actuel.titre,
                "progression": etat_parcours.progression_globale,
                "message": f"Bon retour, {profil.nom} ! Continuons votre voyage..."
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur accueil voyageur retour: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def repondre_diagnostic(self, voyageur_id: str, question_id: str, reponse: str) -> Dict[str, Any]:
        """Traite une réponse au diagnostic"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            # Enregistrer la réponse
            resultat = self.diagnostic_profil.repondre_question(question_id, reponse)
            
            # Mettre à jour la dernière activité
            self.sessions_actives[voyageur_id].derniere_activite = datetime.now()
            
            # Si le diagnostic est terminé, finaliser la session
            if resultat.get("statut") == "termine":
                return self._finaliser_diagnostic(voyageur_id, resultat)
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur réponse diagnostic: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def _finaliser_diagnostic(self, voyageur_id: str, resultat_diagnostic: Dict[str, Any]) -> Dict[str, Any]:
        """Finalise le diagnostic et crée la session complète"""
        try:
            diagnostic = resultat_diagnostic["resultat"]
            profil_dominant = diagnostic.profil_dominant
            
            # Obtenir le profil de référence
            profil_ref = self.diagnostic_profil.obtenir_profil_reference(profil_dominant)
            if not profil_ref:
                raise ValueError(f"Profil de référence non trouvé: {profil_dominant}")
            
            # Créer le profil personnalisé
            profil_voyageur = ProfilVoyageur(
                type_voyageur=profil_dominant,
                nom=profil_ref.nom,
                niveau_experience=profil_ref.niveau_experience,
                motivations_principales=profil_ref.motivations_principales,
                peurs_principales=profil_ref.peurs_principales,
                besoins_specifiques=profil_ref.besoins_specifiques,
                niveau_technique=profil_ref.niveau_technique,
                sensibilite_spirituelle=profil_ref.sensibilite_spirituelle,
                timestamp_creation=datetime.now()
            )
            
            # Sauvegarder le profil
            self.voyageurs_connus[voyageur_id] = profil_voyageur
            
            # Créer l'interface personnalisée
            interface = self.interface_personnalisee.creer_interface_pour_profil(profil_voyageur)
            
            # Créer le parcours personnalisé
            parcours = self.parcours_adaptatif.creer_parcours_pour_profil(profil_voyageur)
            
            # Créer l'état du parcours
            etat_parcours = self.parcours_adaptatif.creer_etat_parcours(voyageur_id, parcours.id_parcours)
            
            # Créer le tableau de bord
            tableau_bord = self.tableau_bord.creer_tableau_bord_pour_voyageur(voyageur_id, parcours)
            
            # Mettre à jour la session
            session = SessionVoyageur(
                voyageur_id=voyageur_id,
                profil=profil_voyageur,
                diagnostic=diagnostic,
                interface=interface,
                parcours_actuel=parcours,
                etat_parcours=etat_parcours,
                tableau_bord=tableau_bord,
                timestamp_debut=datetime.now(),
                derniere_activite=datetime.now()
            )
            
            self.sessions_actives[voyageur_id] = session
            
            # Mettre à jour les métriques
            self.etat["diagnostics_realises"] += 1
            self.etat["parcours_crees"] += 1
            
            self.logger.info(f"✅ Diagnostic finalisé pour {voyageur_id} - Profil: {profil_dominant.value}")
            
            return {
                "statut": "diagnostic_termine",
                "voyageur_id": voyageur_id,
                "profil": profil_dominant.value,
                "nom": profil_voyageur.nom,
                "confiance": diagnostic.confiance_diagnostic,
                "interface": interface.type_interface.value,
                "parcours": parcours.titre,
                "suggestions": diagnostic.suggestions_adaptation,
                "message": f"Parfait ! Votre profil a été identifié. Bienvenue, {profil_voyageur.nom} !"
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur finalisation diagnostic: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def obtenir_interface_voyageur(self, voyageur_id: str) -> Dict[str, Any]:
        """Obtient l'interface personnalisée d'un voyageur"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            session = self.sessions_actives[voyageur_id]
            if not session.interface:
                return {"statut": "erreur", "message": "Interface non créée"}
            
            # Mettre à jour la dernière activité
            session.derniere_activite = datetime.now()
            
            return {
                "statut": "succes",
                "voyageur_id": voyageur_id,
                "interface": session.interface,
                "profil": session.profil.type_voyageur.value if session.profil else None,
                "parcours_actuel": session.parcours_actuel.titre if session.parcours_actuel else None
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur obtention interface: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def obtenir_tableau_bord_voyageur(self, voyageur_id: str) -> Dict[str, Any]:
        """Obtient le tableau de bord d'un voyageur"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            session = self.sessions_actives[voyageur_id]
            if not session.tableau_bord:
                return {"statut": "erreur", "message": "Tableau de bord non créé"}
            
            # Mettre à jour la dernière activité
            session.derniere_activite = datetime.now()
            
            # Mettre à jour le tableau de bord
            tableau_bord_mis_a_jour = self.tableau_bord.mettre_a_jour_tableau_bord(
                voyageur_id, session.etat_parcours
            )
            
            return {
                "statut": "succes",
                "voyageur_id": voyageur_id,
                "tableau_bord": tableau_bord_mis_a_jour,
                "progression": session.etat_parcours.progression_globale if session.etat_parcours else 0.0
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur obtention tableau bord: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def avancer_parcours(self, voyageur_id: str, etape_id: str) -> Dict[str, Any]:
        """Fait avancer le parcours d'un voyageur"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            session = self.sessions_actives[voyageur_id]
            if not session.etat_parcours:
                return {"statut": "erreur", "message": "Parcours non initialisé"}
            
            # Faire avancer le parcours
            resultat = self.parcours_adaptatif.avancer_etape(
                voyageur_id, etape_id, session.etat_parcours
            )
            
            # Mettre à jour la dernière activité
            session.derniere_activite = datetime.now()
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur avancement parcours: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def adapter_interface_temps_reel(self, voyageur_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte l'interface en temps réel selon le feedback"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            session = self.sessions_actives[voyageur_id]
            if not session.interface:
                return {"statut": "erreur", "message": "Interface non créée"}
            
            # Adapter l'interface
            resultat = self.interface_personnalisee.adapter_interface_temps_reel(
                session.interface, feedback
            )
            
            # Mettre à jour la dernière activité
            session.derniere_activite = datetime.now()
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur adaptation interface: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    def terminer_session(self, voyageur_id: str) -> Dict[str, Any]:
        """Termine la session d'un voyageur"""
        try:
            if voyageur_id not in self.sessions_actives:
                return {"statut": "erreur", "message": "Session non trouvée"}
            
            session = self.sessions_actives[voyageur_id]
            
            # Créer l'expérience utilisateur
            experience = ExperienceUtilisateur(
                session_id=f"session_{voyageur_id}_{int(time.time())}",
                voyageur_id=voyageur_id,
                parcours_suivi=session.parcours_actuel.titre if session.parcours_actuel else "Aucun",
                etapes_completees=session.etat_parcours.etapes_terminees if session.etat_parcours else [],
                temps_total=(datetime.now() - session.timestamp_debut).total_seconds() / 60.0,
                satisfaction_finale=session.etat_parcours.satisfaction_actuelle if session.etat_parcours else 0.5,
                insights_generes=session.etat_parcours.insights_generes if session.etat_parcours else [],
                timestamp_fin=datetime.now()
            )
            
            # Sauvegarder l'expérience
            self._sauvegarder_experience(experience)
            
            # Nettoyer la session
            del self.sessions_actives[voyageur_id]
            
            self.logger.info(f"👋 Session terminée pour {voyageur_id}")
            
            return {
                "statut": "session_terminee",
                "voyageur_id": voyageur_id,
                "experience": experience,
                "message": "Merci pour votre visite ! Votre expérience a été sauvegardée."
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur terminaison session: {e}")
            return {"statut": "erreur", "message": str(e)}
    
    async def _nettoyer_sessions_expirees(self):
        """Nettoie les sessions expirées"""
        sessions_a_supprimer = []
        
        for voyageur_id, session in self.sessions_actives.items():
            temps_inactivite = (datetime.now() - session.derniere_activite).total_seconds()
            
            if temps_inactivite > self.config_session["temps_inactivite"]:
                sessions_a_supprimer.append(voyageur_id)
        
        for voyageur_id in sessions_a_supprimer:
            self.logger.info(f"🧹 Nettoyage session expirée: {voyageur_id}")
            await self.terminer_session(voyageur_id)
    
    def _sauvegarder_experience(self, experience: ExperienceUtilisateur):
        """Sauvegarde l'expérience utilisateur"""
        try:
            # Ici, on pourrait sauvegarder dans une base de données
            # Pour l'instant, on log simplement
            self.logger.info(f"💾 Expérience sauvegardée: {experience.session_id}")
            
            # Mettre à jour les métriques
            if experience.temps_total > 0:
                self.etat["temps_moyen_session"] = (
                    (self.etat["temps_moyen_session"] + experience.temps_total) / 2
                )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde expérience: {e}")
    
    def obtenir_statistiques_globales(self) -> Dict[str, Any]:
        """Obtient les statistiques globales du Guide du Voyageur"""
        try:
            # Analyser les profils les plus populaires
            profils_compteur = {}
            for profil in self.voyageurs_connus.values():
                type_profil = profil.type_voyageur.value
                profils_compteur[type_profil] = profils_compteur.get(type_profil, 0) + 1
            
            profil_populaire = max(profils_compteur.items(), key=lambda x: x[1]) if profils_compteur else ("Aucun", 0)
            
            return {
                "statut": "succes",
                "statistiques": {
                    "voyageurs_connus": len(self.voyageurs_connus),
                    "sessions_actives": len(self.sessions_actives),
                    "diagnostics_realises": self.etat["diagnostics_realises"],
                    "parcours_crees": self.etat["parcours_crees"],
                    "satisfaction_moyenne": self.etat["satisfaction_moyenne"],
                    "temps_moyen_session": self.etat["temps_moyen_session"],
                    "profil_populaire": profil_populaire[0],
                    "energie_guide": self.energie_guide.niveau_energie
                }
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur statistiques globales: {e}")
            return {"statut": "erreur", "message": str(e)}


def creer_guide_voyageur() -> GuideVoyageurCore:
    """Crée une instance du Guide du Voyageur"""
    return GuideVoyageurCore()
