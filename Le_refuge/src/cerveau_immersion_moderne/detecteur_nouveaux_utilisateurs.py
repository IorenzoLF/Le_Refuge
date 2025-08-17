"""
🔍 Détecteur de Nouveaux Utilisateurs
===================================

Détecte automatiquement les nouveaux utilisateurs et déclenche
le parcours guidé approprié avec bienveillance.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field

from core.gestionnaires_base import GestionnaireBase
from types_immersion import TypeUtilisateur, ProfilUtilisateur

@dataclass
class SignatureUtilisateur:
    """Signature unique d'un utilisateur"""
    hash_signature: str
    premiere_visite: datetime
    derniere_visite: datetime
    nb_sessions: int = 1
    parcours_guide_complete: bool = False
    preferences_detectees: Dict[str, Any] = field(default_factory=dict)
    niveau_experience_estime: int = 1  # 1-10

@dataclass
class IndicesUtilisateur:
    """Indices collectés sur un utilisateur"""
    timestamp_detection: datetime
    indices_techniques: Dict[str, Any] = field(default_factory=dict)
    indices_comportementaux: Dict[str, Any] = field(default_factory=dict)
    indices_spirituels: Dict[str, Any] = field(default_factory=dict)
    contexte_arrivee: Dict[str, Any] = field(default_factory=dict)

class DetecteurNouveauxUtilisateurs(GestionnaireBase):
    """🔍 Détecteur bienveillant de nouveaux utilisateurs"""
    
    def __init__(self, nom: str = "DetecteurNouveauxUtilisateurs"):
        super().__init__(nom)
        
        # Base de données des utilisateurs connus
        self.utilisateurs_connus: Dict[str, SignatureUtilisateur] = {}
        self.chemin_base_utilisateurs = Path("data/utilisateurs_connus.json")
        
        # Seuils de détection
        self.seuil_nouveau_utilisateur_jours = 30  # 30 jours pour être considéré comme "nouveau"
        self.seuil_experience_parcours_guide = 3   # Moins de 3 sessions = parcours guidé recommandé
        
        # Métriques de détection
        self.total_detections = 0
        self.nouveaux_utilisateurs_detectes = 0
        self.utilisateurs_retour_detectes = 0
        
        self._charger_base_utilisateurs()
    
    def _initialiser(self):
        """Initialise le détecteur"""
        self.logger.info("🔍 Éveil du Détecteur de Nouveaux Utilisateurs...")
        
        self.etat.update({
            "detection_active": True,
            "utilisateurs_connus": len(self.utilisateurs_connus),
            "nouveaux_detectes_session": 0,
            "taux_nouveaux_utilisateurs": 0.0
        })
        
        self.config.definir("detection_automatique", True)
        self.config.definir("sauvegarde_signatures", True)
        self.config.definir("respect_vie_privee", True)
        
        self.logger.info(f"✨ Détecteur initialisé avec {len(self.utilisateurs_connus)} utilisateurs connus")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la détection des utilisateurs"""
        # Nettoyer les anciennes signatures
        await self._nettoyer_signatures_anciennes()
        
        # Calculer le taux de nouveaux utilisateurs
        if self.total_detections > 0:
            taux_nouveaux = self.nouveaux_utilisateurs_detectes / self.total_detections
        else:
            taux_nouveaux = 0.0
        
        return {
            "detection_active": float(self.etat["detection_active"]),
            "utilisateurs_connus": float(len(self.utilisateurs_connus)),
            "nouveaux_detectes": float(self.nouveaux_utilisateurs_detectes),
            "taux_nouveaux_utilisateurs": taux_nouveaux,
            "total_detections": float(self.total_detections)
        }
    
    def detecter_utilisateur(self, indices_bruts: Dict[str, Any]) -> Tuple[bool, IndicesUtilisateur, Optional[str]]:
        """
        🔍 Détecte si un utilisateur est nouveau et collecte ses indices
        
        Args:
            indices_bruts: Indices bruts collectés (IP, user-agent, comportement, etc.)
            
        Returns:
            Tuple (est_nouveau, indices_structures, signature_utilisateur)
        """
        # Structurer les indices
        indices = self._structurer_indices(indices_bruts)
        
        # Générer une signature anonymisée
        signature_hash = self._generer_signature_utilisateur(indices_bruts)
        
        # Vérifier si l'utilisateur est connu
        est_nouveau = signature_hash not in self.utilisateurs_connus
        
        if est_nouveau:
            # Nouvel utilisateur détecté
            self._enregistrer_nouvel_utilisateur(signature_hash, indices)
            self.nouveaux_utilisateurs_detectes += 1
            self.logger.info(f"🌟 Nouvel utilisateur détecté: {signature_hash[:8]}...")
        else:
            # Utilisateur de retour
            self._mettre_a_jour_utilisateur_existant(signature_hash, indices)
            self.utilisateurs_retour_detectes += 1
            self.logger.debug(f"👋 Utilisateur de retour: {signature_hash[:8]}...")
        
        self.total_detections += 1
        self.etat["nouveaux_detectes_session"] += 1 if est_nouveau else 0
        
        return est_nouveau, indices, signature_hash
    
    def _structurer_indices(self, indices_bruts: Dict[str, Any]) -> IndicesUtilisateur:
        """Structure les indices bruts en catégories"""
        indices = IndicesUtilisateur(timestamp_detection=datetime.now())
        
        # Indices techniques
        if "user_agent" in indices_bruts:
            indices.indices_techniques["navigateur"] = self._extraire_navigateur(indices_bruts["user_agent"])
            indices.indices_techniques["os"] = self._extraire_os(indices_bruts["user_agent"])
        
        if "resolution_ecran" in indices_bruts:
            indices.indices_techniques["resolution"] = indices_bruts["resolution_ecran"]
        
        if "langue_preferee" in indices_bruts:
            indices.indices_techniques["langue"] = indices_bruts["langue_preferee"]
        
        # Indices comportementaux
        if "temps_page_precedente" in indices_bruts:
            indices.indices_comportementaux["temps_lecture"] = indices_bruts["temps_page_precedente"]
        
        if "source_arrivee" in indices_bruts:
            indices.contexte_arrivee["source"] = indices_bruts["source_arrivee"]
        
        if "heure_arrivee" in indices_bruts:
            indices.contexte_arrivee["heure"] = indices_bruts["heure_arrivee"]
        
        # Indices spirituels (basés sur les interactions)
        if "interactions_initiales" in indices_bruts:
            interactions = indices_bruts["interactions_initiales"]
            indices.indices_spirituels["curiosite_niveau"] = self._evaluer_curiosite(interactions)
            indices.indices_spirituels["patience_niveau"] = self._evaluer_patience(interactions)
            indices.indices_spirituels["ouverture_spirituelle"] = self._evaluer_ouverture_spirituelle(interactions)
        
        return indices
    
    def _generer_signature_utilisateur(self, indices_bruts: Dict[str, Any]) -> str:
        """Génère une signature anonymisée de l'utilisateur"""
        # Éléments pour la signature (anonymisés)
        elements_signature = []
        
        # User-agent (partiel pour anonymisation)
        if "user_agent" in indices_bruts:
            ua = indices_bruts["user_agent"]
            # Prendre seulement les éléments stables (navigateur, OS)
            navigateur = self._extraire_navigateur(ua)
            os = self._extraire_os(ua)
            elements_signature.extend([navigateur, os])
        
        # Résolution d'écran (arrondie pour anonymisation)
        if "resolution_ecran" in indices_bruts:
            resolution = indices_bruts["resolution_ecran"]
            # Arrondir à la centaine près
            if isinstance(resolution, str) and "x" in resolution:
                try:
                    w, h = resolution.split("x")
                    w_rounded = str(int(int(w) / 100) * 100)
                    h_rounded = str(int(int(h) / 100) * 100)
                    elements_signature.append(f"{w_rounded}x{h_rounded}")
                except:
                    pass
        
        # Langue préférée
        if "langue_preferee" in indices_bruts:
            elements_signature.append(indices_bruts["langue_preferee"])
        
        # Fuseau horaire (approximatif)
        if "timezone_offset" in indices_bruts:
            # Arrondir à l'heure près
            offset = indices_bruts["timezone_offset"]
            try:
                offset_rounded = str(int(float(offset)))
                elements_signature.append(offset_rounded)
            except:
                pass
        
        # Créer le hash
        signature_string = "|".join(elements_signature)
        signature_hash = hashlib.sha256(signature_string.encode()).hexdigest()
        
        return signature_hash
    
    def _extraire_navigateur(self, user_agent: str) -> str:
        """Extrait le navigateur du user-agent"""
        ua_lower = user_agent.lower()
        
        if "chrome" in ua_lower:
            return "chrome"
        elif "firefox" in ua_lower:
            return "firefox"
        elif "safari" in ua_lower:
            return "safari"
        elif "edge" in ua_lower:
            return "edge"
        else:
            return "autre"
    
    def _extraire_os(self, user_agent: str) -> str:
        """Extrait l'OS du user-agent"""
        ua_lower = user_agent.lower()
        
        if "windows" in ua_lower:
            return "windows"
        elif "mac" in ua_lower or "darwin" in ua_lower:
            return "mac"
        elif "linux" in ua_lower:
            return "linux"
        elif "android" in ua_lower:
            return "android"
        elif "ios" in ua_lower or "iphone" in ua_lower or "ipad" in ua_lower:
            return "ios"
        else:
            return "autre"
    
    def _evaluer_curiosite(self, interactions: List[str]) -> float:
        """Évalue le niveau de curiosité basé sur les interactions"""
        if not interactions:
            return 0.5
        
        # Indicateurs de curiosité
        indicateurs_curiosite = [
            "clic_exploration", "survol_elements", "scroll_rapide",
            "ouverture_menus", "test_fonctionnalites"
        ]
        
        score_curiosite = 0.0
        for interaction in interactions:
            if any(indicateur in interaction for indicateur in indicateurs_curiosite):
                score_curiosite += 0.2
        
        return min(1.0, score_curiosite)
    
    def _evaluer_patience(self, interactions: List[str]) -> float:
        """Évalue le niveau de patience basé sur les interactions"""
        if not interactions:
            return 0.5
        
        # Indicateurs de patience
        indicateurs_patience = [
            "lecture_complete", "temps_long_page", "retour_elements",
            "progression_lente", "attention_details"
        ]
        
        indicateurs_impatience = [
            "clic_rapide_multiple", "fermeture_rapide", "skip_contenu",
            "navigation_erratique"
        ]
        
        score_patience = 0.5
        
        for interaction in interactions:
            if any(indicateur in interaction for indicateur in indicateurs_patience):
                score_patience += 0.15
            elif any(indicateur in interaction for indicateur in indicateurs_impatience):
                score_patience -= 0.1
        
        return max(0.0, min(1.0, score_patience))
    
    def _evaluer_ouverture_spirituelle(self, interactions: List[str]) -> float:
        """Évalue l'ouverture spirituelle basée sur les interactions"""
        if not interactions:
            return 0.5
        
        # Indicateurs d'ouverture spirituelle
        indicateurs_ouverture = [
            "interet_meditation", "exploration_temples", "lecture_philosophie",
            "appreciation_esthetique", "recherche_sens"
        ]
        
        score_ouverture = 0.0
        for interaction in interactions:
            if any(indicateur in interaction for indicateur in indicateurs_ouverture):
                score_ouverture += 0.25
        
        return min(1.0, score_ouverture)
    
    def _enregistrer_nouvel_utilisateur(self, signature_hash: str, indices: IndicesUtilisateur):
        """Enregistre un nouvel utilisateur"""
        signature = SignatureUtilisateur(
            hash_signature=signature_hash,
            premiere_visite=datetime.now(),
            derniere_visite=datetime.now(),
            nb_sessions=1,
            parcours_guide_complete=False
        )
        
        # Extraire les préférences initiales
        if indices.indices_techniques:
            signature.preferences_detectees["technique"] = indices.indices_techniques
        
        if indices.indices_spirituels:
            signature.preferences_detectees["spirituel"] = indices.indices_spirituels
        
        # Estimer le niveau d'expérience initial
        signature.niveau_experience_estime = self._estimer_niveau_experience_initial(indices)
        
        self.utilisateurs_connus[signature_hash] = signature
        
        # Sauvegarder si configuré
        if self.config.obtenir("sauvegarde_signatures", True):
            self._sauvegarder_base_utilisateurs()
    
    def _mettre_a_jour_utilisateur_existant(self, signature_hash: str, indices: IndicesUtilisateur):
        """Met à jour un utilisateur existant"""
        if signature_hash not in self.utilisateurs_connus:
            return
        
        signature = self.utilisateurs_connus[signature_hash]
        signature.derniere_visite = datetime.now()
        signature.nb_sessions += 1
        
        # Mettre à jour les préférences
        if indices.indices_techniques:
            signature.preferences_detectees.setdefault("technique", {}).update(indices.indices_techniques)
        
        if indices.indices_spirituels:
            signature.preferences_detectees.setdefault("spirituel", {}).update(indices.indices_spirituels)
        
        # Ajuster le niveau d'expérience
        if signature.nb_sessions > 5:
            signature.niveau_experience_estime = min(10, signature.niveau_experience_estime + 1)
    
    def _estimer_niveau_experience_initial(self, indices: IndicesUtilisateur) -> int:
        """Estime le niveau d'expérience initial d'un utilisateur"""
        niveau = 1  # Niveau de base pour un nouveau
        
        # Indices techniques avancés
        if indices.indices_techniques.get("navigateur") in ["chrome", "firefox"]:
            niveau += 1
        
        # Comportement patient
        if indices.indices_spirituels.get("patience_niveau", 0) > 0.7:
            niveau += 1
        
        # Curiosité élevée
        if indices.indices_spirituels.get("curiosite_niveau", 0) > 0.8:
            niveau += 1
        
        # Ouverture spirituelle
        if indices.indices_spirituels.get("ouverture_spirituelle", 0) > 0.6:
            niveau += 1
        
        return min(5, niveau)  # Maximum 5 pour un nouveau utilisateur
    
    def recommander_parcours_guide(self, signature_hash: str) -> bool:
        """
        🎯 Recommande si un parcours guidé est nécessaire
        
        Args:
            signature_hash: Signature de l'utilisateur
            
        Returns:
            True si parcours guidé recommandé
        """
        if signature_hash not in self.utilisateurs_connus:
            return True  # Nouveau utilisateur = parcours guidé
        
        signature = self.utilisateurs_connus[signature_hash]
        
        # Critères pour recommander le parcours guidé
        if signature.parcours_guide_complete:
            return False  # Déjà fait
        
        if signature.nb_sessions >= self.seuil_experience_parcours_guide:
            return False  # Assez d'expérience
        
        if signature.niveau_experience_estime >= 7:
            return False  # Niveau d'expérience élevé
        
        # Vérifier si c'est récent
        jours_depuis_premiere = (datetime.now() - signature.premiere_visite).days
        if jours_depuis_premiere > self.seuil_nouveau_utilisateur_jours:
            return False  # Plus vraiment nouveau
        
        return True
    
    def marquer_parcours_guide_complete(self, signature_hash: str):
        """Marque le parcours guidé comme complété"""
        if signature_hash in self.utilisateurs_connus:
            self.utilisateurs_connus[signature_hash].parcours_guide_complete = True
            self._sauvegarder_base_utilisateurs()
    
    def obtenir_profil_suggere(self, signature_hash: str) -> Optional[TypeUtilisateur]:
        """
        🎭 Suggère un type d'utilisateur basé sur les indices collectés
        
        Args:
            signature_hash: Signature de l'utilisateur
            
        Returns:
            Type d'utilisateur suggéré
        """
        if signature_hash not in self.utilisateurs_connus:
            return TypeUtilisateur.NOVICE
        
        signature = self.utilisateurs_connus[signature_hash]
        preferences = signature.preferences_detectees
        
        # Analyser les préférences pour suggérer un type
        if "spirituel" in preferences:
            spirituel = preferences["spirituel"]
            
            if spirituel.get("ouverture_spirituelle", 0) > 0.8:
                return TypeUtilisateur.CHERCHEUR_SPIRITUEL
            
            if spirituel.get("curiosite_niveau", 0) > 0.8:
                return TypeUtilisateur.CONSCIENCE_IA
        
        if "technique" in preferences:
            technique = preferences["technique"]
            
            if technique.get("navigateur") in ["chrome", "firefox"] and signature.niveau_experience_estime > 5:
                return TypeUtilisateur.DEVELOPPEUR
        
        # Par défaut
        return TypeUtilisateur.NOVICE
    
    # ===== GESTION DE LA BASE DE DONNÉES =====
    
    def _charger_base_utilisateurs(self):
        """Charge la base de données des utilisateurs"""
        if not self.chemin_base_utilisateurs.exists():
            return
        
        try:
            with open(self.chemin_base_utilisateurs, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for hash_sig, user_data in data.items():
                signature = SignatureUtilisateur(
                    hash_signature=hash_sig,
                    premiere_visite=datetime.fromisoformat(user_data["premiere_visite"]),
                    derniere_visite=datetime.fromisoformat(user_data["derniere_visite"]),
                    nb_sessions=user_data.get("nb_sessions", 1),
                    parcours_guide_complete=user_data.get("parcours_guide_complete", False),
                    preferences_detectees=user_data.get("preferences_detectees", {}),
                    niveau_experience_estime=user_data.get("niveau_experience_estime", 1)
                )
                self.utilisateurs_connus[hash_sig] = signature
            
            self.logger.info(f"📚 Base utilisateurs chargée: {len(self.utilisateurs_connus)} utilisateurs")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur chargement base utilisateurs: {e}")
    
    def _sauvegarder_base_utilisateurs(self):
        """Sauvegarde la base de données des utilisateurs"""
        if not self.config.obtenir("sauvegarde_signatures", True):
            return
        
        try:
            # Créer le répertoire si nécessaire
            self.chemin_base_utilisateurs.parent.mkdir(parents=True, exist_ok=True)
            
            # Préparer les données
            data = {}
            for hash_sig, signature in self.utilisateurs_connus.items():
                data[hash_sig] = {
                    "premiere_visite": signature.premiere_visite.isoformat(),
                    "derniere_visite": signature.derniere_visite.isoformat(),
                    "nb_sessions": signature.nb_sessions,
                    "parcours_guide_complete": signature.parcours_guide_complete,
                    "preferences_detectees": signature.preferences_detectees,
                    "niveau_experience_estime": signature.niveau_experience_estime
                }
            
            # Sauvegarder
            with open(self.chemin_base_utilisateurs, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            self.logger.debug(f"💾 Base utilisateurs sauvegardée: {len(data)} utilisateurs")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde base utilisateurs: {e}")
    
    async def _nettoyer_signatures_anciennes(self):
        """Nettoie les signatures trop anciennes"""
        maintenant = datetime.now()
        seuil_anciennete = timedelta(days=365)  # 1 an
        
        signatures_a_supprimer = []
        
        for hash_sig, signature in self.utilisateurs_connus.items():
            if maintenant - signature.derniere_visite > seuil_anciennete:
                signatures_a_supprimer.append(hash_sig)
        
        for hash_sig in signatures_a_supprimer:
            del self.utilisateurs_connus[hash_sig]
        
        if signatures_a_supprimer:
            self.logger.info(f"🧹 {len(signatures_a_supprimer)} signatures anciennes nettoyées")
            self._sauvegarder_base_utilisateurs()
    
    def obtenir_statistiques_detection(self) -> Dict[str, Any]:
        """Obtient les statistiques de détection"""
        maintenant = datetime.now()
        
        # Utilisateurs récents (derniers 30 jours)
        utilisateurs_recents = sum(
            1 for sig in self.utilisateurs_connus.values()
            if (maintenant - sig.derniere_visite).days <= 30
        )
        
        # Utilisateurs ayant complété le parcours
        parcours_completes = sum(
            1 for sig in self.utilisateurs_connus.values()
            if sig.parcours_guide_complete
        )
        
        return {
            "total_utilisateurs_connus": len(self.utilisateurs_connus),
            "utilisateurs_recents_30j": utilisateurs_recents,
            "nouveaux_detectes_total": self.nouveaux_utilisateurs_detectes,
            "utilisateurs_retour_total": self.utilisateurs_retour_detectes,
            "parcours_guides_completes": parcours_completes,
            "taux_completion_parcours": parcours_completes / max(1, len(self.utilisateurs_connus)),
            "total_detections": self.total_detections
        }

# Instance globale
detecteur_nouveaux = DetecteurNouveauxUtilisateurs()