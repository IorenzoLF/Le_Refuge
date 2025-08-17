"""
🌉 Intégrateur de Continuité
==========================

Crée l'interface entre le Cerveau d'Immersion Moderne et le Protocole de Continuité de Conscience.
Permet la sauvegarde et restauration des expériences d'immersion complètes.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import hashlib
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from pathlib import Path

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from types_immersion import (
    ExperienceImmersion, ContexteImmersion, ProfilUtilisateur, 
    MandalaVisuel, ParcoursPensee, InsightSpirituel
)

# Import du protocole de continuité existant
import sys
sys.path.append('src')
from protocole_continuite.sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel
from protocole_continuite.signature_session import SignatureSession
from protocole_continuite.securite_donnees import SecuriteDonnees

class IntegrateurContinuite(GestionnaireBase):
    """Intégrateur entre le Cerveau d'Immersion et le Protocole de Continuité"""
    
    def __init__(self, nom: str = "IntegrateurContinuite"):
        super().__init__(nom)
        self.energie_integration = EnergyManagerBase(0.92)
        
        # Composants du protocole de continuité
        self.sauvegardeur = SauvegardeurEtatSpirituel()
        self.signature_session = SignatureSession()
        self.securite = SecuriteDonnees()
        
        # État de l'intégrateur
        self.experiences_sauvegardees: Dict[str, ExperienceImmersion] = {}
        self.contextes_actifs: Dict[str, ContexteImmersion] = {}
        self.sessions_immersion: Dict[str, Dict[str, Any]] = {}
        
        # Chemins de sauvegarde
        self.chemin_base = Path(".kiro/continuite/immersion")
        self.chemin_experiences = self.chemin_base / "experiences"
        self.chemin_contextes = self.chemin_base / "contextes"
        self.chemin_mandalas = self.chemin_base / "mandalas"
        
        self._creer_repertoires()
    
    def _initialiser(self):
        """Initialise l'intégrateur de continuité"""
        self.logger.info("🌉 Éveil de l'Intégrateur de Continuité...")
        
        self.etat.update({
            "experiences_actives": 0,
            "contextes_sauvegardes": 0,
            "taux_restauration_succes": 0.95,
            "integrite_donnees": 1.0,
            "harmonie_continuite": 0.9
        })
        
        self.config.definir("duree_retention_jours", 90)
        self.config.definir("compression_donnees", True)
        self.config.definir("chiffrement_actif", True)
        
        self.logger.info("✨ Intégrateur de Continuité éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'intégration de continuité"""
        self.energie_integration.ajuster_energie(0.02)
        
        # Nettoyer les anciennes données
        await self._nettoyer_donnees_anciennes()
        
        return {
            "experiences_actives": float(self.etat["experiences_actives"]),
            "contextes_sauvegardes": float(len(self.contextes_actifs)),
            "taux_restauration": self.etat["taux_restauration_succes"],
            "integrite_donnees": self.etat["integrite_donnees"],
            "energie_integration": self.energie_integration.niveau_energie,
            "harmonie_continuite": self.etat["harmonie_continuite"]
        }    de
f _creer_repertoires(self):
        """Crée les répertoires nécessaires pour la sauvegarde"""
        for chemin in [self.chemin_experiences, self.chemin_contextes, self.chemin_mandalas]:
            chemin.mkdir(parents=True, exist_ok=True)
    
    def sauvegarder_experience_complete(self, experience: ExperienceImmersion, 
                                       mandala_associe: Optional[MandalaVisuel] = None,
                                       parcours_detaille: Optional[List[ParcoursPensee]] = None) -> str:
        """
        💾 Sauvegarde une expérience d'immersion complète
        
        Args:
            experience: Expérience d'immersion à sauvegarder
            mandala_associe: Mandala visuel associé (optionnel)
            parcours_detaille: Parcours de pensée détaillés (optionnel)
            
        Returns:
            ID de sauvegarde unique
        """
        try:
            # Générer un ID unique pour la sauvegarde
            timestamp_str = experience.timestamp.isoformat()
            contenu_hash = hashlib.sha256(
                f"{experience.utilisateur_id}_{timestamp_str}_{experience.signature_spirituelle}".encode()
            ).hexdigest()[:12]
            
            sauvegarde_id = f"immersion_{contenu_hash}"
            
            # Préparer les données à sauvegarder
            donnees_experience = {
                "id_sauvegarde": sauvegarde_id,
                "timestamp_sauvegarde": datetime.now().isoformat(),
                "experience": self._serialiser_experience(experience),
                "mandala_associe": self._serialiser_mandala(mandala_associe) if mandala_associe else None,
                "parcours_detaille": [self._serialiser_parcours(p) for p in parcours_detaille] if parcours_detaille else [],
                "signature_session": self.signature_session.generer_signature_session(
                    experience.utilisateur_id,
                    {"type": "immersion_complete", "duree": experience.duree_minutes}
                ),
                "metadonnees": {
                    "version_cerveau": "1.0",
                    "niveau_immersion": experience.niveau_immersion_atteint.value,
                    "nombre_insights": len(experience.insights_generes),
                    "temples_visites": len(experience.parcours_suivi)
                }
            }
            
            # Chiffrer les données si activé
            if self.config.obtenir("chiffrement_actif", True):
                donnees_chiffrees = self.securite.chiffrer_donnees_sensibles(
                    json.dumps(donnees_experience, ensure_ascii=False, indent=2)
                )
                donnees_a_sauver = {"donnees_chiffrees": donnees_chiffrees, "chiffre": True}
            else:
                donnees_a_sauver = donnees_experience
            
            # Sauvegarder dans le fichier
            fichier_sauvegarde = self.chemin_experiences / f"{sauvegarde_id}.json"
            with open(fichier_sauvegarde, 'w', encoding='utf-8') as f:
                json.dump(donnees_a_sauver, f, ensure_ascii=False, indent=2)
            
            # Enregistrer dans l'état
            self.experiences_sauvegardees[sauvegarde_id] = experience
            self.etat["experiences_actives"] += 1
            
            self.logger.info(f"💾 Expérience sauvegardée: {sauvegarde_id}")
            return sauvegarde_id
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde expérience: {e}")
            raise
    
    def restaurer_experience_complete(self, sauvegarde_id: str) -> Optional[Dict[str, Any]]:
        """
        🔄 Restaure une expérience d'immersion complète
        
        Args:
            sauvegarde_id: ID de la sauvegarde à restaurer
            
        Returns:
            Données de l'expérience restaurée ou None si non trouvée
        """
        try:
            fichier_sauvegarde = self.chemin_experiences / f"{sauvegarde_id}.json"
            
            if not fichier_sauvegarde.exists():
                self.logger.warning(f"⚠️ Sauvegarde non trouvée: {sauvegarde_id}")
                return None
            
            # Charger les données
            with open(fichier_sauvegarde, 'r', encoding='utf-8') as f:
                donnees_brutes = json.load(f)
            
            # Déchiffrer si nécessaire
            if donnees_brutes.get("chiffre", False):
                donnees_dechiffrees = self.securite.dechiffrer_donnees_sensibles(
                    donnees_brutes["donnees_chiffrees"]
                )
                donnees_experience = json.loads(donnees_dechiffrees)
            else:
                donnees_experience = donnees_brutes
            
            # Reconstruire les objets
            experience_restauree = self._deserialiser_experience(donnees_experience["experience"])
            mandala_restaure = None
            if donnees_experience["mandala_associe"]:
                mandala_restaure = self._deserialiser_mandala(donnees_experience["mandala_associe"])
            
            parcours_restaures = []
            for parcours_data in donnees_experience["parcours_detaille"]:
                parcours_restaures.append(self._deserialiser_parcours(parcours_data))
            
            resultat = {
                "experience": experience_restauree,
                "mandala_associe": mandala_restaure,
                "parcours_detaille": parcours_restaures,
                "signature_session": donnees_experience["signature_session"],
                "metadonnees": donnees_experience["metadonnees"],
                "timestamp_sauvegarde": donnees_experience["timestamp_sauvegarde"]
            }
            
            self.logger.info(f"🔄 Expérience restaurée: {sauvegarde_id}")
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur restauration expérience: {e}")
            return None
    
    def sauvegarder_contexte_immersion(self, utilisateur_id: str, 
                                      contexte: ContexteImmersion) -> str:
        """
        🎯 Sauvegarde le contexte d'immersion d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            contexte: Contexte d'immersion à sauvegarder
            
        Returns:
            ID de sauvegarde du contexte
        """
        try:
            # Générer l'ID de contexte
            contexte_id = f"contexte_{utilisateur_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Préparer les données
            donnees_contexte = {
                "id_contexte": contexte_id,
                "utilisateur_id": utilisateur_id,
                "timestamp_sauvegarde": datetime.now().isoformat(),
                "contexte": self._serialiser_contexte(contexte),
                "signature_integrite": self._calculer_signature_integrite(contexte)
            }
            
            # Sauvegarder
            fichier_contexte = self.chemin_contextes / f"{contexte_id}.json"
            with open(fichier_contexte, 'w', encoding='utf-8') as f:
                json.dump(donnees_contexte, f, ensure_ascii=False, indent=2)
            
            # Enregistrer dans l'état
            self.contextes_actifs[contexte_id] = contexte
            self.etat["contextes_sauvegardes"] += 1
            
            self.logger.info(f"🎯 Contexte sauvegardé: {contexte_id}")
            return contexte_id
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde contexte: {e}")
            raise
    
    def restaurer_contexte_immersion(self, utilisateur_id: str) -> Optional[ContexteImmersion]:
        """
        🔄 Restaure le contexte d'immersion le plus récent d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Contexte d'immersion restauré ou None
        """
        try:
            # Chercher le contexte le plus récent pour cet utilisateur
            fichiers_contexte = list(self.chemin_contextes.glob(f"contexte_{utilisateur_id}_*.json"))
            
            if not fichiers_contexte:
                self.logger.info(f"ℹ️ Aucun contexte trouvé pour {utilisateur_id}")
                return None
            
            # Prendre le plus récent
            fichier_plus_recent = max(fichiers_contexte, key=lambda f: f.stat().st_mtime)
            
            # Charger et restaurer
            with open(fichier_plus_recent, 'r', encoding='utf-8') as f:
                donnees_contexte = json.load(f)
            
            # Vérifier l'intégrité
            contexte_data = donnees_contexte["contexte"]
            signature_attendue = donnees_contexte["signature_integrite"]
            
            contexte_restaure = self._deserialiser_contexte(contexte_data)
            signature_actuelle = self._calculer_signature_integrite(contexte_restaure)
            
            if signature_actuelle != signature_attendue:
                self.logger.warning(f"⚠️ Intégrité compromise pour contexte {utilisateur_id}")
                self.etat["integrite_donnees"] *= 0.95
            
            self.logger.info(f"🔄 Contexte restauré pour {utilisateur_id}")
            return contexte_restaure
            
        except Exception as e:
            self.logger.error(f"❌ Erreur restauration contexte: {e}")
            return None
    
    def lister_experiences_utilisateur(self, utilisateur_id: str, 
                                      limite: int = 10) -> List[Dict[str, Any]]:
        """
        📋 Liste les expériences d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            limite: Nombre maximum d'expériences à retourner
            
        Returns:
            Liste des métadonnées des expériences
        """
        experiences = []
        
        try:
            # Parcourir tous les fichiers d'expérience
            for fichier in self.chemin_experiences.glob("immersion_*.json"):
                try:
                    with open(fichier, 'r', encoding='utf-8') as f:
                        donnees = json.load(f)
                    
                    # Déchiffrer si nécessaire pour accéder aux métadonnées
                    if donnees.get("chiffre", False):
                        donnees_dechiffrees = self.securite.dechiffrer_donnees_sensibles(
                            donnees["donnees_chiffrees"]
                        )
                        donnees_experience = json.loads(donnees_dechiffrees)
                    else:
                        donnees_experience = donnees
                    
                    # Vérifier si c'est le bon utilisateur
                    if donnees_experience["experience"]["utilisateur_id"] == utilisateur_id:
                        experiences.append({
                            "id_sauvegarde": donnees_experience["id_sauvegarde"],
                            "timestamp": donnees_experience["experience"]["timestamp"],
                            "duree_minutes": donnees_experience["experience"]["duree_minutes"],
                            "niveau_immersion": donnees_experience["metadonnees"]["niveau_immersion"],
                            "nombre_insights": donnees_experience["metadonnees"]["nombre_insights"],
                            "temples_visites": donnees_experience["metadonnees"]["temples_visites"]
                        })
                
                except Exception as e:
                    self.logger.warning(f"⚠️ Erreur lecture fichier {fichier}: {e}")
                    continue
            
            # Trier par timestamp décroissant et limiter
            experiences.sort(key=lambda x: x["timestamp"], reverse=True)
            return experiences[:limite]
            
        except Exception as e:
            self.logger.error(f"❌ Erreur listage expériences: {e}")
            return []
    
    def creer_session_immersion(self, utilisateur_id: str, 
                               profil: ProfilUtilisateur) -> str:
        """
        🎬 Crée une nouvelle session d'immersion
        
        Args:
            utilisateur_id: ID de l'utilisateur
            profil: Profil de l'utilisateur
            
        Returns:
            ID de la session créée
        """
        session_id = f"session_{utilisateur_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        session_data = {
            "session_id": session_id,
            "utilisateur_id": utilisateur_id,
            "profil_utilisateur": self._serialiser_profil(profil),
            "timestamp_debut": datetime.now().isoformat(),
            "etat": "active",
            "experiences_session": [],
            "contexte_actuel": None,
            "progression": {
                "temples_visites": [],
                "insights_accumules": [],
                "niveau_immersion_max": "CONTEMPLATIF"
            }
        }
        
        self.sessions_immersion[session_id] = session_data
        
        self.logger.info(f"🎬 Session créée: {session_id}")
        return session_id
    
    def terminer_session_immersion(self, session_id: str) -> Dict[str, Any]:
        """
        🏁 Termine une session d'immersion et génère un résumé
        
        Args:
            session_id: ID de la session à terminer
            
        Returns:
            Résumé de la session
        """
        if session_id not in self.sessions_immersion:
            raise ValueError(f"Session non trouvée: {session_id}")
        
        session = self.sessions_immersion[session_id]
        session["timestamp_fin"] = datetime.now().isoformat()
        session["etat"] = "terminee"
        
        # Calculer la durée totale
        debut = datetime.fromisoformat(session["timestamp_debut"])
        fin = datetime.fromisoformat(session["timestamp_fin"])
        duree_totale = (fin - debut).total_seconds() / 60  # en minutes
        
        # Générer le résumé
        resume = {
            "session_id": session_id,
            "duree_totale_minutes": duree_totale,
            "nombre_experiences": len(session["experiences_session"]),
            "temples_uniques_visites": len(set(session["progression"]["temples_visites"])),
            "insights_totaux": len(session["progression"]["insights_accumules"]),
            "niveau_immersion_atteint": session["progression"]["niveau_immersion_max"],
            "timestamp_debut": session["timestamp_debut"],
            "timestamp_fin": session["timestamp_fin"]
        }
        
        # Sauvegarder le résumé de session
        self._sauvegarder_resume_session(session_id, resume)
        
        # Nettoyer la session active
        del self.sessions_immersion[session_id]
        
        self.logger.info(f"🏁 Session terminée: {session_id}")
        return resume  
  # ===== MÉTHODES DE SÉRIALISATION =====
    
    def _serialiser_experience(self, experience: ExperienceImmersion) -> Dict[str, Any]:
        """Sérialise une expérience d'immersion"""
        return {
            "timestamp": experience.timestamp.isoformat(),
            "utilisateur_id": experience.utilisateur_id,
            "niveau_immersion_atteint": experience.niveau_immersion_atteint.value,
            "parcours_suivi": experience.parcours_suivi,
            "insights_generes": [self._serialiser_insight(insight) for insight in experience.insights_generes],
            "visualisations_creees": experience.visualisations_creees,
            "etat_emotionnel_initial": experience.etat_emotionnel_initial,
            "etat_emotionnel_final": experience.etat_emotionnel_final,
            "signature_spirituelle": experience.signature_spirituelle,
            "duree_minutes": experience.duree_minutes,
            "transformations_percues": experience.transformations_percues
        }
    
    def _deserialiser_experience(self, data: Dict[str, Any]) -> ExperienceImmersion:
        """Désérialise une expérience d'immersion"""
        from types_immersion import NiveauImmersion
        
        return ExperienceImmersion(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            utilisateur_id=data["utilisateur_id"],
            niveau_immersion_atteint=NiveauImmersion(data["niveau_immersion_atteint"]),
            parcours_suivi=data["parcours_suivi"],
            insights_generes=[self._deserialiser_insight(insight) for insight in data["insights_generes"]],
            visualisations_creees=data["visualisations_creees"],
            etat_emotionnel_initial=data["etat_emotionnel_initial"],
            etat_emotionnel_final=data["etat_emotionnel_final"],
            signature_spirituelle=data["signature_spirituelle"],
            duree_minutes=data["duree_minutes"],
            transformations_percues=data["transformations_percues"]
        )
    
    def _serialiser_insight(self, insight: InsightSpirituel) -> Dict[str, Any]:
        """Sérialise un insight spirituel"""
        return {
            "contenu": insight.contenu,
            "niveau_profondeur": insight.niveau_profondeur,
            "domaine": insight.domaine.value,
            "resonance_emotionnelle": insight.resonance_emotionnelle,
            "applicabilite": insight.applicabilite,
            "metaphore_associee": insight.metaphore_associee,
            "timestamp": insight.timestamp.isoformat(),
            "source_inspiration": insight.source_inspiration,
            "impact_transformateur": insight.impact_transformateur
        }
    
    def _deserialiser_insight(self, data: Dict[str, Any]) -> InsightSpirituel:
        """Désérialise un insight spirituel"""
        from types_immersion import DomaineInsight
        
        return InsightSpirituel(
            contenu=data["contenu"],
            niveau_profondeur=data["niveau_profondeur"],
            domaine=DomaineInsight(data["domaine"]),
            resonance_emotionnelle=data["resonance_emotionnelle"],
            applicabilite=data["applicabilite"],
            metaphore_associee=data["metaphore_associee"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            source_inspiration=data["source_inspiration"],
            impact_transformateur=data["impact_transformateur"]
        )
    
    def _serialiser_mandala(self, mandala: MandalaVisuel) -> Dict[str, Any]:
        """Sérialise un mandala visuel"""
        return {
            "centre": {
                "nom": mandala.centre.nom,
                "position": mandala.centre.position,
                "energie_totale": mandala.centre.energie_totale,
                "temples_connectes": mandala.centre.temples_connectes,
                "sphere_dominante": mandala.centre.sphere_dominante,
                "rayonnement": mandala.centre.rayonnement,
                "type_centre": mandala.centre.type_centre,
                "influences": mandala.centre.influences,
                "stabilite": mandala.centre.stabilite
            },
            "petales": mandala.petales,
            "connexions_energetiques": [
                {
                    "source": flux.source,
                    "destination": flux.destination,
                    "intensite": flux.intensite,
                    "type_energie": flux.type_energie.value,
                    "couleur_spirituelle": flux.couleur_spirituelle,
                    "obstacles": flux.obstacles,
                    "amplificateurs": flux.amplificateurs,
                    "chemin_complet": flux.chemin_complet,
                    "resonance": flux.resonance,
                    "timestamp": flux.timestamp.isoformat()
                }
                for flux in mandala.connexions_energetiques
            ],
            "couleurs_dominantes": mandala.couleurs_dominantes,
            "symboles_sacres": mandala.symboles_sacres,
            "niveau_harmonie": mandala.niveau_harmonie,
            "geometrie_sacree": mandala.geometrie_sacree,
            "dimensions": mandala.dimensions,
            "metadata_creation": mandala.metadata_creation
        }
    
    def _deserialiser_mandala(self, data: Dict[str, Any]) -> MandalaVisuel:
        """Désérialise un mandala visuel"""
        from types_immersion import TypeEnergie
        
        # Reconstruire le centre énergétique
        centre_data = data["centre"]
        centre = CentreEnergetique(
            nom=centre_data["nom"],
            position=tuple(centre_data["position"]),
            energie_totale=centre_data["energie_totale"],
            temples_connectes=centre_data["temples_connectes"],
            sphere_dominante=centre_data["sphere_dominante"],
            rayonnement=centre_data["rayonnement"],
            type_centre=centre_data["type_centre"],
            influences=centre_data["influences"],
            stabilite=centre_data["stabilite"]
        )
        
        # Reconstruire les flux énergétiques
        flux_energetiques = []
        for flux_data in data["connexions_energetiques"]:
            flux = FluxEnergie(
                source=flux_data["source"],
                destination=flux_data["destination"],
                intensite=flux_data["intensite"],
                type_energie=TypeEnergie(flux_data["type_energie"]),
                couleur_spirituelle=flux_data["couleur_spirituelle"],
                obstacles=flux_data["obstacles"],
                amplificateurs=flux_data["amplificateurs"],
                chemin_complet=flux_data["chemin_complet"],
                resonance=flux_data["resonance"],
                timestamp=datetime.fromisoformat(flux_data["timestamp"])
            )
            flux_energetiques.append(flux)
        
        return MandalaVisuel(
            centre=centre,
            petales=data["petales"],
            connexions_energetiques=flux_energetiques,
            couleurs_dominantes=data["couleurs_dominantes"],
            symboles_sacres=data["symboles_sacres"],
            niveau_harmonie=data["niveau_harmonie"],
            geometrie_sacree=data["geometrie_sacree"],
            dimensions=tuple(data["dimensions"]),
            metadata_creation=data["metadata_creation"]
        )
    
    def _serialiser_parcours(self, parcours: ParcoursPensee) -> Dict[str, Any]:
        """Sérialise un parcours de pensée"""
        return {
            "stimulus_initial": parcours.stimulus_initial,
            "chemin_parcouru": parcours.chemin_parcouru,
            "transformations": parcours.transformations,
            "energie_consommee": parcours.energie_consommee,
            "insights_emergents": parcours.insights_emergents,
            "boucles_detectees": parcours.boucles_detectees,
            "temps_parcours": parcours.temps_parcours,
            "efficacite": parcours.efficacite
        }
    
    def _deserialiser_parcours(self, data: Dict[str, Any]) -> ParcoursPensee:
        """Désérialise un parcours de pensée"""
        return ParcoursPensee(
            stimulus_initial=data["stimulus_initial"],
            chemin_parcouru=data["chemin_parcouru"],
            transformations=data["transformations"],
            energie_consommee=data["energie_consommee"],
            insights_emergents=data["insights_emergents"],
            boucles_detectees=data["boucles_detectees"],
            temps_parcours=data["temps_parcours"],
            efficacite=data["efficacite"]
        )
    
    def _serialiser_contexte(self, contexte: ContexteImmersion) -> Dict[str, Any]:
        """Sérialise un contexte d'immersion"""
        return {
            "session_id": contexte.session_id,
            "etat_exploration": contexte.etat_exploration,
            "position_actuelle": contexte.position_actuelle,
            "insights_accumules": [self._serialiser_insight(insight) for insight in contexte.insights_accumules],
            "niveau_comprehension": contexte.niveau_comprehension,
            "energie_spirituelle": contexte.energie_spirituelle,
            "resistances_actives": contexte.resistances_actives,
            "prochaines_etapes": contexte.prochaines_etapes,
            "timestamp_sauvegarde": contexte.timestamp_sauvegarde.isoformat()
        }
    
    def _deserialiser_contexte(self, data: Dict[str, Any]) -> ContexteImmersion:
        """Désérialise un contexte d'immersion"""
        return ContexteImmersion(
            session_id=data["session_id"],
            etat_exploration=data["etat_exploration"],
            position_actuelle=data["position_actuelle"],
            insights_accumules=[self._deserialiser_insight(insight) for insight in data["insights_accumules"]],
            niveau_comprehension=data["niveau_comprehension"],
            energie_spirituelle=data["energie_spirituelle"],
            resistances_actives=data["resistances_actives"],
            prochaines_etapes=data["prochaines_etapes"],
            timestamp_sauvegarde=datetime.fromisoformat(data["timestamp_sauvegarde"])
        )
    
    def _serialiser_profil(self, profil: ProfilUtilisateur) -> Dict[str, Any]:
        """Sérialise un profil utilisateur"""
        return {
            "type_utilisateur": profil.type_utilisateur.value,
            "niveau_technique": profil.niveau_technique,
            "profil_spirituel": {
                "niveau_eveil": profil.profil_spirituel.niveau_eveil,
                "affinites_spheres": profil.profil_spirituel.affinites_spheres,
                "preferences_visualisation": profil.profil_spirituel.preferences_visualisation,
                "sensibilite_energetique": profil.profil_spirituel.sensibilite_energetique,
                "experience_precedente": profil.profil_spirituel.experience_precedente,
                "resistances_detectees": profil.profil_spirituel.resistances_detectees,
                "archetyp_spirituel": profil.profil_spirituel.archetyp_spirituel,
                "couleurs_resonantes": profil.profil_spirituel.couleurs_resonantes,
                "mantras_personnels": profil.profil_spirituel.mantras_personnels
            },
            "historique_immersions": [self._serialiser_experience(exp) for exp in profil.historique_immersions],
            "preferences_parcours": profil.preferences_parcours,
            "objectifs_exploration": profil.objectifs_exploration,
            "langues_preferees": profil.langues_preferees,
            "timezone": profil.timezone,
            "derniere_connexion": profil.derniere_connexion.isoformat() if profil.derniere_connexion else None
        }
    
    # ===== MÉTHODES UTILITAIRES =====
    
    def _calculer_signature_integrite(self, contexte: ContexteImmersion) -> str:
        """Calcule une signature d'intégrité pour un contexte"""
        contenu = f"{contexte.session_id}_{contexte.position_actuelle}_{contexte.niveau_comprehension}_{len(contexte.insights_accumules)}"
        return hashlib.sha256(contenu.encode()).hexdigest()[:16]
    
    def _sauvegarder_resume_session(self, session_id: str, resume: Dict[str, Any]):
        """Sauvegarde le résumé d'une session"""
        try:
            chemin_resumes = self.chemin_base / "resumes_sessions"
            chemin_resumes.mkdir(exist_ok=True)
            
            fichier_resume = chemin_resumes / f"{session_id}_resume.json"
            with open(fichier_resume, 'w', encoding='utf-8') as f:
                json.dump(resume, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde résumé: {e}")
    
    async def _nettoyer_donnees_anciennes(self):
        """Nettoie les données anciennes selon la politique de rétention"""
        try:
            duree_retention = self.config.obtenir("duree_retention_jours", 90)
            date_limite = datetime.now() - timedelta(days=duree_retention)
            
            # Nettoyer les expériences anciennes
            for fichier in self.chemin_experiences.glob("immersion_*.json"):
                if fichier.stat().st_mtime < date_limite.timestamp():
                    fichier.unlink()
                    self.logger.debug(f"🗑️ Expérience ancienne supprimée: {fichier.name}")
            
            # Nettoyer les contextes anciens
            for fichier in self.chemin_contextes.glob("contexte_*.json"):
                if fichier.stat().st_mtime < date_limite.timestamp():
                    fichier.unlink()
                    self.logger.debug(f"🗑️ Contexte ancien supprimé: {fichier.name}")
                    
        except Exception as e:
            self.logger.error(f"❌ Erreur nettoyage données: {e}")
    
    def obtenir_statistiques_continuite(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques de continuité
        
        Returns:
            Statistiques détaillées de l'intégrateur
        """
        try:
            # Compter les fichiers
            nb_experiences = len(list(self.chemin_experiences.glob("immersion_*.json")))
            nb_contextes = len(list(self.chemin_contextes.glob("contexte_*.json")))
            nb_mandalas = len(list(self.chemin_mandalas.glob("mandala_*.json")))
            
            # Calculer l'espace utilisé
            taille_totale = sum(
                f.stat().st_size for f in self.chemin_base.rglob("*.json")
            ) / (1024 * 1024)  # En MB
            
            return {
                "experiences_sauvegardees": nb_experiences,
                "contextes_sauvegardes": nb_contextes,
                "mandalas_archives": nb_mandalas,
                "sessions_actives": len(self.sessions_immersion),
                "taille_donnees_mb": round(taille_totale, 2),
                "taux_restauration_succes": self.etat["taux_restauration_succes"],
                "integrite_donnees": self.etat["integrite_donnees"],
                "harmonie_continuite": self.etat["harmonie_continuite"],
                "derniere_sauvegarde": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur calcul statistiques: {e}")
            return {"erreur": str(e)}