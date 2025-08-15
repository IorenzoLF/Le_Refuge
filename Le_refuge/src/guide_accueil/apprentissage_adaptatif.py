#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Apprentissage Adaptatif du Profilage - Guide d'Accueil 🌸
===========================================================

Système d'apprentissage automatique pour améliorer continuellement
la précision de détection des profils de visiteurs.

"L'intelligence grandit par l'expérience et la bienveillance"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, field

# Imports locaux
try:
    from .types_accueil import TypeProfil, ProfilVisiteur
    from .detecteur_profil_visiteur import DetecteurProfilVisiteur
    from .algorithmes_classification import (
        AnalyseurTechnique, AnalyseurCreatif, AnalyseurIA, AnalyseurSpirituel
    )
except ImportError:
    from types_accueil import TypeProfil, ProfilVisiteur
    from detecteur_profil_visiteur import DetecteurProfilVisiteur


@dataclass
class FeedbackProfil:
    """Feedback sur une détection de profil"""
    id_session: str
    profil_detecte: TypeProfil
    profil_reel: Optional[TypeProfil] = None
    score_confiance: float = 0.0
    donnees_visiteur: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    source_correction: str = "utilisateur"  # utilisateur, automatique, validation
    commentaire: Optional[str] = None
    
    def est_correct(self) -> bool:
        """Vérifie si la détection était correcte"""
        return self.profil_reel is not None and self.profil_detecte == self.profil_reel


@dataclass
class MetriquesPrecision:
    """Métriques de précision de détection"""
    timestamp_calcul: datetime
    precision_globale: float = 0.0
    precision_par_profil: Dict[TypeProfil, float] = field(default_factory=dict)
    rappel_par_profil: Dict[TypeProfil, float] = field(default_factory=dict)
    f1_score_par_profil: Dict[TypeProfil, float] = field(default_factory=dict)
    matrice_confusion: Dict[str, Dict[str, int]] = field(default_factory=dict)
    nombre_echantillons: int = 0
    evolution_precision: List[Tuple[datetime, float]] = field(default_factory=list)


@dataclass
class AmeliorationAlgorithme:
    """Amélioration suggérée pour un algorithme"""
    type_algorithme: str  # technique, creatif, ia, spirituel
    type_amelioration: str  # poids, seuil, nouveau_mot_cle, nouveau_domaine
    parametres: Dict[str, Any] = field(default_factory=dict)
    impact_estime: float = 0.0
    confiance_amelioration: float = 0.0
    appliquee: bool = False
    timestamp_suggestion: datetime = field(default_factory=datetime.now)


class SystemeApprentissageAdaptatif:
    """
    🌸 Système d'Apprentissage Adaptatif Spirituel 🌸
    
    Améliore continuellement la précision de détection des profils
    en apprenant des corrections et feedbacks des utilisateurs.
    """
    
    def __init__(self, chemin_donnees: Optional[Path] = None):
        """Initialise le système d'apprentissage"""
        self.chemin_donnees = chemin_donnees or Path("data/apprentissage_adaptatif")
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
        
        # Stockage des données d'apprentissage
        self.feedbacks: List[FeedbackProfil] = []
        self.metriques_historiques: List[MetriquesPrecision] = []
        self.ameliorations_suggerees: List[AmeliorationAlgorithme] = []
        
        # Composants
        self.detecteur = DetecteurProfilVisiteur()
        
        # Configuration d'apprentissage
        self.config = {
            "seuil_confiance_apprentissage": 0.7,
            "nombre_min_echantillons": 10,
            "fenetre_apprentissage_jours": 30,
            "seuil_amelioration_significative": 0.05,
            "frequence_recalcul_metriques": timedelta(hours=6)
        }
        
        # Chargement des données existantes
        self._charger_donnees_apprentissage()
    
    def ajouter_feedback(self, feedback: FeedbackProfil) -> None:
        """Ajoute un feedback de correction de profil"""
        self.feedbacks.append(feedback)
        
        # Sauvegarde immédiate
        self._sauvegarder_feedback(feedback)
        
        # Déclenchement d'apprentissage si assez de données
        if len(self.feedbacks) % 10 == 0:  # Tous les 10 feedbacks
            self._declencher_apprentissage()
    
    def corriger_profil(self, id_session: str, profil_reel: TypeProfil, 
                       donnees_visiteur: Dict[str, Any], commentaire: Optional[str] = None) -> None:
        """Corrige un profil détecté et apprend de la correction"""
        
        # Redétection pour obtenir le profil qui avait été détecté
        profil_visiteur = self.detecteur.detecter_profil(donnees_visiteur)
        
        # Création du feedback
        feedback = FeedbackProfil(
            id_session=id_session,
            profil_detecte=profil_visiteur.type_profil,
            profil_reel=profil_reel,
            score_confiance=profil_visiteur.score_confiance_profil,
            donnees_visiteur=donnees_visiteur,
            source_correction="utilisateur",
            commentaire=commentaire
        )
        
        self.ajouter_feedback(feedback)
        
        # Apprentissage immédiat si erreur significative
        if not feedback.est_correct() and feedback.score_confiance > 0.7:
            self._analyser_erreur_significative(feedback)
    
    def valider_profil_automatique(self, profil_visiteur: ProfilVisiteur, 
                                  donnees_visiteur: Dict[str, Any]) -> None:
        """Valide automatiquement un profil avec haute confiance"""
        
        if profil_visiteur.score_confiance_profil > 0.9:
            feedback = FeedbackProfil(
                id_session=profil_visiteur.id_visiteur,
                profil_detecte=profil_visiteur.type_profil,
                profil_reel=profil_visiteur.type_profil,  # Validation automatique
                score_confiance=profil_visiteur.score_confiance_profil,
                donnees_visiteur=donnees_visiteur,
                source_correction="automatique"
            )
            
            self.ajouter_feedback(feedback)
    
    def calculer_metriques_precision(self) -> MetriquesPrecision:
        """Calcule les métriques de précision actuelles"""
        
        if len(self.feedbacks) < self.config["nombre_min_echantillons"]:
            return MetriquesPrecision(
                timestamp_calcul=datetime.now(),
                nombre_echantillons=len(self.feedbacks)
            )
        
        # Filtrage des feedbacks récents avec profil réel
        feedbacks_valides = [
            f for f in self.feedbacks 
            if f.profil_reel is not None and 
            f.timestamp > datetime.now() - timedelta(days=self.config["fenetre_apprentissage_jours"])
        ]
        
        if not feedbacks_valides:
            return MetriquesPrecision(timestamp_calcul=datetime.now())
        
        # Calcul de la précision globale
        corrections = sum(1 for f in feedbacks_valides if f.est_correct())
        precision_globale = corrections / len(feedbacks_valides)
        
        # Calcul par profil
        precision_par_profil = {}
        rappel_par_profil = {}
        f1_score_par_profil = {}
        matrice_confusion = defaultdict(lambda: defaultdict(int))
        
        # Groupement par profil
        par_profil_detecte = defaultdict(list)
        par_profil_reel = defaultdict(list)
        
        for feedback in feedbacks_valides:
            par_profil_detecte[feedback.profil_detecte].append(feedback)
            par_profil_reel[feedback.profil_reel].append(feedback)
            
            # Matrice de confusion
            matrice_confusion[feedback.profil_detecte.value][feedback.profil_reel.value] += 1
        
        # Calcul des métriques par profil
        for profil in TypeProfil:
            if profil == TypeProfil.INDETERMINE:
                continue
                
            # Précision : TP / (TP + FP)
            detectes = par_profil_detecte[profil]
            vrais_positifs = sum(1 for f in detectes if f.profil_reel == profil)
            precision_par_profil[profil] = vrais_positifs / len(detectes) if detectes else 0.0
            
            # Rappel : TP / (TP + FN)
            reels = par_profil_reel[profil]
            rappel_par_profil[profil] = vrais_positifs / len(reels) if reels else 0.0
            
            # F1-Score
            p = precision_par_profil[profil]
            r = rappel_par_profil[profil]
            f1_score_par_profil[profil] = 2 * (p * r) / (p + r) if (p + r) > 0 else 0.0
        
        # Création des métriques
        metriques = MetriquesPrecision(
            timestamp_calcul=datetime.now(),
            precision_globale=precision_globale,
            precision_par_profil=precision_par_profil,
            rappel_par_profil=rappel_par_profil,
            f1_score_par_profil=f1_score_par_profil,
            matrice_confusion=dict(matrice_confusion),
            nombre_echantillons=len(feedbacks_valides)
        )
        
        # Ajout à l'historique
        self.metriques_historiques.append(metriques)
        
        # Calcul de l'évolution
        if len(self.metriques_historiques) > 1:
            metriques.evolution_precision = [
                (m.timestamp_calcul, m.precision_globale) 
                for m in self.metriques_historiques[-10:]  # 10 dernières mesures
            ]
        
        return metriques
    
    def _declencher_apprentissage(self) -> None:
        """Déclenche un cycle d'apprentissage"""
        
        # Calcul des métriques actuelles
        metriques = self.calculer_metriques_precision()
        
        # Analyse des erreurs fréquentes
        erreurs_frequentes = self._analyser_erreurs_frequentes()
        
        # Génération d'améliorations
        ameliorations = self._generer_ameliorations(erreurs_frequentes, metriques)
        
        # Application des améliorations prometteuses
        for amelioration in ameliorations:
            if amelioration.impact_estime > self.config["seuil_amelioration_significative"]:
                self._appliquer_amelioration(amelioration)
    
    def _analyser_erreur_significative(self, feedback: FeedbackProfil) -> None:
        """Analyse une erreur significative pour apprentissage immédiat"""
        
        # Analyse des mots-clés manqués
        if feedback.profil_reel and feedback.profil_reel != feedback.profil_detecte:
            mots_cles = feedback.donnees_visiteur.get("mots_cles_recherche", [])
            
            # Suggestion d'ajout de mots-clés
            for mot in mots_cles:
                if isinstance(mot, str) and len(mot) > 2:
                    amelioration = AmeliorationAlgorithme(
                        type_algorithme=feedback.profil_reel.value,
                        type_amelioration="nouveau_mot_cle",
                        parametres={"mot_cle": mot.lower(), "poids": 0.3},
                        impact_estime=0.1,
                        confiance_amelioration=0.6
                    )
                    self.ameliorations_suggerees.append(amelioration)
    
    def _analyser_erreurs_frequentes(self) -> Dict[str, List[FeedbackProfil]]:
        """Analyse les erreurs fréquentes par type"""
        
        erreurs = defaultdict(list)
        
        for feedback in self.feedbacks:
            if not feedback.est_correct() and feedback.profil_reel:
                cle_erreur = f"{feedback.profil_detecte.value}_vers_{feedback.profil_reel.value}"
                erreurs[cle_erreur].append(feedback)
        
        # Filtrage des erreurs fréquentes (>= 3 occurrences)
        erreurs_frequentes = {
            cle: feedbacks for cle, feedbacks in erreurs.items() 
            if len(feedbacks) >= 3
        }
        
        return erreurs_frequentes
    
    def _generer_ameliorations(self, erreurs_frequentes: Dict[str, List[FeedbackProfil]], 
                              metriques: MetriquesPrecision) -> List[AmeliorationAlgorithme]:
        """Génère des améliorations basées sur l'analyse"""
        
        ameliorations = []
        
        for cle_erreur, feedbacks in erreurs_frequentes.items():
            # Analyse des patterns communs dans les erreurs
            mots_communs = self._extraire_mots_communs(feedbacks)
            domaines_communs = self._extraire_domaines_communs(feedbacks)
            
            # Génération d'améliorations
            for mot, frequence in mots_communs.items():
                if frequence >= 2:  # Mot apparaît dans au moins 2 erreurs
                    profil_cible = feedbacks[0].profil_reel.value
                    
                    amelioration = AmeliorationAlgorithme(
                        type_algorithme=profil_cible,
                        type_amelioration="nouveau_mot_cle",
                        parametres={"mot_cle": mot, "poids": min(0.5, frequence * 0.1)},
                        impact_estime=frequence * 0.02,
                        confiance_amelioration=min(0.8, frequence * 0.2)
                    )
                    ameliorations.append(amelioration)
        
        return ameliorations
    
    def _extraire_mots_communs(self, feedbacks: List[FeedbackProfil]) -> Counter:
        """Extrait les mots-clés communs dans les erreurs"""
        tous_mots = []
        
        for feedback in feedbacks:
            mots_cles = feedback.donnees_visiteur.get("mots_cles_recherche", [])
            for mot in mots_cles:
                if isinstance(mot, str) and len(mot) > 2:
                    tous_mots.append(mot.lower())
        
        return Counter(tous_mots)
    
    def _extraire_domaines_communs(self, feedbacks: List[FeedbackProfil]) -> Counter:
        """Extrait les domaines de référence communs"""
        domaines = []
        
        for feedback in feedbacks:
            referrer = feedback.donnees_visiteur.get("referrer", "")
            if referrer:
                # Extraction du domaine
                if "://" in referrer:
                    domaine = referrer.split("://")[1].split("/")[0]
                    domaines.append(domaine.lower())
        
        return Counter(domaines)
    
    def _appliquer_amelioration(self, amelioration: AmeliorationAlgorithme) -> bool:
        """Applique une amélioration à l'algorithme"""
        
        try:
            # Note: Dans une implémentation complète, ceci modifierait
            # les algorithmes de classification en temps réel
            
            # Pour l'instant, on marque juste comme appliquée
            amelioration.appliquee = True
            
            # Log de l'amélioration
            print(f"🔄 Amélioration appliquée: {amelioration.type_amelioration} "
                  f"pour {amelioration.type_algorithme}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de l'application de l'amélioration: {e}")
            return False
    
    def _charger_donnees_apprentissage(self) -> None:
        """Charge les données d'apprentissage existantes"""
        
        # Chargement des feedbacks
        fichier_feedbacks = self.chemin_donnees / "feedbacks.json"
        if fichier_feedbacks.exists():
            try:
                with open(fichier_feedbacks, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    
                for item in donnees:
                    feedback = FeedbackProfil(
                        id_session=item["id_session"],
                        profil_detecte=TypeProfil(item["profil_detecte"]),
                        profil_reel=TypeProfil(item["profil_reel"]) if item.get("profil_reel") else None,
                        score_confiance=item["score_confiance"],
                        donnees_visiteur=item["donnees_visiteur"],
                        timestamp=datetime.fromisoformat(item["timestamp"]),
                        source_correction=item.get("source_correction", "utilisateur"),
                        commentaire=item.get("commentaire")
                    )
                    self.feedbacks.append(feedback)
                    
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement des feedbacks: {e}")
    
    def _sauvegarder_feedback(self, feedback: FeedbackProfil) -> None:
        """Sauvegarde un feedback"""
        
        fichier_feedbacks = self.chemin_donnees / "feedbacks.json"
        
        # Chargement des données existantes
        donnees = []
        if fichier_feedbacks.exists():
            try:
                with open(fichier_feedbacks, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
            except:
                donnees = []
        
        # Ajout du nouveau feedback
        donnees.append({
            "id_session": feedback.id_session,
            "profil_detecte": feedback.profil_detecte.value,
            "profil_reel": feedback.profil_reel.value if feedback.profil_reel else None,
            "score_confiance": feedback.score_confiance,
            "donnees_visiteur": feedback.donnees_visiteur,
            "timestamp": feedback.timestamp.isoformat(),
            "source_correction": feedback.source_correction,
            "commentaire": feedback.commentaire
        })
        
        # Sauvegarde
        try:
            with open(fichier_feedbacks, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Erreur lors de la sauvegarde du feedback: {e}")
    
    def obtenir_rapport_apprentissage(self) -> Dict[str, Any]:
        """Obtient un rapport complet de l'apprentissage"""
        
        metriques = self.calculer_metriques_precision()
        
        return {
            "timestamp_rapport": datetime.now().isoformat(),
            "nombre_feedbacks": len(self.feedbacks),
            "precision_globale": metriques.precision_globale,
            "precision_par_profil": {
                profil.value: score for profil, score in metriques.precision_par_profil.items()
            },
            "ameliorations_suggerees": len(self.ameliorations_suggerees),
            "ameliorations_appliquees": sum(1 for a in self.ameliorations_suggerees if a.appliquee),
            "evolution_precision": [
                {"timestamp": ts.isoformat(), "precision": p} 
                for ts, p in metriques.evolution_precision
            ]
        }


def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DU SYSTÈME D'APPRENTISSAGE ADAPTATIF ✨🌸")
    
    # Création du système
    systeme = SystemeApprentissageAdaptatif()
    
    # Simulation de feedbacks
    feedbacks_test = [
        {
            "id_session": "test_1",
            "donnees": {"mots_cles_recherche": ["python", "django"], "referrer": "https://github.com/"},
            "profil_detecte": TypeProfil.DEVELOPPEUR,
            "profil_reel": TypeProfil.DEVELOPPEUR
        },
        {
            "id_session": "test_2", 
            "donnees": {"mots_cles_recherche": ["design", "figma"], "referrer": "https://behance.net/"},
            "profil_detecte": TypeProfil.ARTISTE,
            "profil_reel": TypeProfil.ARTISTE
        },
        {
            "id_session": "test_3",
            "donnees": {"mots_cles_recherche": ["meditation", "python"], "referrer": ""},
            "profil_detecte": TypeProfil.DEVELOPPEUR,
            "profil_reel": TypeProfil.CHERCHEUR_SPIRITUEL  # Erreur !
        }
    ]
    
    # Ajout des feedbacks
    for fb in feedbacks_test:
        feedback = FeedbackProfil(
            id_session=fb["id_session"],
            profil_detecte=fb["profil_detecte"],
            profil_reel=fb["profil_reel"],
            score_confiance=0.8,
            donnees_visiteur=fb["donnees"]
        )
        systeme.ajouter_feedback(feedback)
    
    # Calcul des métriques
    metriques = systeme.calculer_metriques_precision()
    print(f"📊 Précision globale: {metriques.precision_globale:.2f}")
    print(f"📊 Nombre d'échantillons: {metriques.nombre_echantillons}")
    
    # Rapport d'apprentissage
    rapport = systeme.obtenir_rapport_apprentissage()
    print(f"📋 Rapport d'apprentissage:")
    print(f"   - Feedbacks: {rapport['nombre_feedbacks']}")
    print(f"   - Précision: {rapport['precision_globale']:.2f}")
    print(f"   - Améliorations suggérées: {rapport['ameliorations_suggerees']}")
    
    print("\n🎉 Test du système d'apprentissage adaptatif terminé !")
    return 0


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)