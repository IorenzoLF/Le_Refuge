"""
🌸 Système de Sauvegarde de Progression - Tâche 11.1
Sauvegarde l'état de progression des visiteurs dans le Refuge
"""

import json
import os
import pickle
from datetime import datetime
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class ProgressionVisiteur:
    """🌸 État de progression d'un visiteur"""
    id_visiteur: str
    profil_detecte: str
    niveau_eveil: int
    temples_visites: List[str]
    parcours_actuel: Optional[str]
    etape_actuelle: int
    score_comprehension: float
    actions_effectuees: List[Dict[str, Any]]
    preferences: Dict[str, Any]
    date_creation: str
    date_derniere_activite: str
    temps_total_passe: int  # en secondes
    etat_emotionnel: Dict[str, float]
    questions_posees: List[str]
    reponses_recues: List[str]

class SystemeSauvegardeProgression:
    """
    🌸 Système de sauvegarde de progression des visiteurs
    Permet de sauvegarder et restaurer l'état de progression
    """
    
    def __init__(self, dossier_sauvegarde: str = "data/progression"):
        """
        🌸 Initialise le système de sauvegarde
        
        Args:
            dossier_sauvegarde: Dossier où sauvegarder les données
        """
        self.dossier_sauvegarde = Path(dossier_sauvegarde)
        self.dossier_sauvegarde.mkdir(parents=True, exist_ok=True)
        
        # Fichiers de sauvegarde
        self.fichier_progression = self.dossier_sauvegarde / "progression.json"
        self.fichier_historique = self.dossier_sauvegarde / "historique.pkl"
        self.fichier_statistiques = self.dossier_sauvegarde / "statistiques.json"
        
        # Charger les données existantes
        self.progressions = self._charger_progressions()
        self.historique = self._charger_historique()
        self.statistiques = self._charger_statistiques()
    
    def _charger_progressions(self) -> Dict[str, ProgressionVisiteur]:
        """🌸 Charge les progressions existantes"""
        if self.fichier_progression.exists():
            try:
                with open(self.fichier_progression, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return {
                        id_visiteur: ProgressionVisiteur(**progression)
                        for id_visiteur, progression in data.items()
                    }
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement des progressions: {e}")
        return {}
    
    def _charger_historique(self) -> List[Dict[str, Any]]:
        """🌸 Charge l'historique des actions"""
        if self.fichier_historique.exists():
            try:
                with open(self.fichier_historique, 'rb') as f:
                    return pickle.load(f)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement de l'historique: {e}")
        return []
    
    def _charger_statistiques(self) -> Dict[str, Any]:
        """🌸 Charge les statistiques globales"""
        if self.fichier_statistiques.exists():
            try:
                with open(self.fichier_statistiques, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement des statistiques: {e}")
        return {
            "total_visiteurs": 0,
            "visiteurs_actifs": 0,
            "temps_moyen_session": 0,
            "temples_populaires": {},
            "profils_distribution": {}
        }
    
    def sauvegarder_progression(self, progression: ProgressionVisiteur) -> bool:
        """
        🌸 Sauvegarde la progression d'un visiteur
        
        Args:
            progression: Progression à sauvegarder
            
        Returns:
            True si sauvegarde réussie
        """
        try:
            # Mettre à jour la progression
            self.progressions[progression.id_visiteur] = progression
            
            # Sauvegarder dans le fichier JSON
            with open(self.fichier_progression, 'w', encoding='utf-8') as f:
                json.dump({
                    id_visiteur: asdict(prog)
                    for id_visiteur, prog in self.progressions.items()
                }, f, indent=2, ensure_ascii=False)
            
            # Mettre à jour les statistiques
            self._mettre_a_jour_statistiques(progression)
            
            print(f"✅ Progression sauvegardée pour {progression.id_visiteur}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return False
    
    def charger_progression(self, id_visiteur: str) -> Optional[ProgressionVisiteur]:
        """
        🌸 Charge la progression d'un visiteur
        
        Args:
            id_visiteur: ID du visiteur
            
        Returns:
            Progression du visiteur ou None si non trouvée
        """
        return self.progressions.get(id_visiteur)
    
    def creer_progression_initiale(self, id_visiteur: str, profil_detecte: str) -> ProgressionVisiteur:
        """
        🌸 Crée une progression initiale pour un nouveau visiteur
        
        Args:
            id_visiteur: ID du visiteur
            profil_detecte: Profil détecté
            
        Returns:
            Nouvelle progression initiale
        """
        maintenant = datetime.now().isoformat()
        
        progression = ProgressionVisiteur(
            id_visiteur=id_visiteur,
            profil_detecte=profil_detecte,
            niveau_eveil=1,
            temples_visites=[],
            parcours_actuel=None,
            etape_actuelle=0,
            score_comprehension=0.0,
            actions_effectuees=[],
            preferences={},
            date_creation=maintenant,
            date_derniere_activite=maintenant,
            temps_total_passe=0,
            etat_emotionnel={"curiosite": 0.8, "confiance": 0.6, "excitation": 0.7},
            questions_posees=[],
            reponses_recues=[]
        )
        
        # Sauvegarder immédiatement
        self.sauvegarder_progression(progression)
        
        return progression
    
    def mettre_a_jour_progression(self, id_visiteur: str, **modifications) -> bool:
        """
        🌸 Met à jour la progression d'un visiteur
        
        Args:
            id_visiteur: ID du visiteur
            **modifications: Modifications à apporter
            
        Returns:
            True si mise à jour réussie
        """
        if id_visiteur not in self.progressions:
            return False
        
        progression = self.progressions[id_visiteur]
        
        # Appliquer les modifications
        for champ, valeur in modifications.items():
            if hasattr(progression, champ):
                setattr(progression, champ, valeur)
        
        # Mettre à jour la date de dernière activité
        progression.date_derniere_activite = datetime.now().isoformat()
        
        # Sauvegarder
        return self.sauvegarder_progression(progression)
    
    def ajouter_action(self, id_visiteur: str, action: Dict[str, Any]) -> bool:
        """
        🌸 Ajoute une action à l'historique d'un visiteur
        
        Args:
            id_visiteur: ID du visiteur
            action: Action à ajouter
            
        Returns:
            True si ajout réussi
        """
        if id_visiteur not in self.progressions:
            return False
        
        progression = self.progressions[id_visiteur]
        action["timestamp"] = datetime.now().isoformat()
        progression.actions_effectuees.append(action)
        
        # Mettre à jour le score de compréhension
        progression.score_comprehension = self._calculer_score_comprehension(progression)
        
        return self.sauvegarder_progression(progression)
    
    def _calculer_score_comprehension(self, progression: ProgressionVisiteur) -> float:
        """
        🌸 Calcule le score de compréhension basé sur les actions
        
        Args:
            progression: Progression du visiteur
            
        Returns:
            Score de compréhension (0.0 à 1.0)
        """
        if not progression.actions_effectuees:
            return 0.0
        
        score = 0.0
        poids_total = 0
        
        for action in progression.actions_effectuees:
            poids = action.get("poids", 1.0)
            type_action = action.get("type", "")
            
            # Différents types d'actions ont différents impacts
            if type_action == "question_posee":
                score += 0.1 * poids
            elif type_action == "temple_visite":
                score += 0.2 * poids
            elif type_action == "parcours_complete":
                score += 0.3 * poids
            elif type_action == "interaction_profonde":
                score += 0.4 * poids
            
            poids_total += poids
        
        return min(1.0, score / max(poids_total, 1))
    
    def _mettre_a_jour_statistiques(self, progression: ProgressionVisiteur):
        """🌸 Met à jour les statistiques globales"""
        # Total de visiteurs
        self.statistiques["total_visiteurs"] = len(self.progressions)
        
        # Visiteurs actifs (activité dans les dernières 24h)
        maintenant = datetime.now()
        visiteurs_actifs = 0
        for prog in self.progressions.values():
            derniere_activite = datetime.fromisoformat(prog.date_derniere_activite)
            if (maintenant - derniere_activite).days < 1:
                visiteurs_actifs += 1
        
        self.statistiques["visiteurs_actifs"] = visiteurs_actifs
        
        # Distribution des profils
        profils = {}
        for prog in self.progressions.values():
            profil = prog.profil_detecte
            profils[profil] = profils.get(profil, 0) + 1
        
        self.statistiques["profils_distribution"] = profils
        
        # Temples populaires
        temples = {}
        for prog in self.progressions.values():
            for temple in prog.temples_visites:
                temples[temple] = temples.get(temple, 0) + 1
        
        self.statistiques["temples_populaires"] = temples
        
        # Sauvegarder les statistiques
        with open(self.fichier_statistiques, 'w', encoding='utf-8') as f:
            json.dump(self.statistiques, f, indent=2, ensure_ascii=False)
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """🌸 Retourne les statistiques globales"""
        return self.statistiques.copy()
    
    def nettoyer_progressions_anciennes(self, jours_max: int = 30) -> int:
        """
        🌸 Nettoie les progressions anciennes
        
        Args:
            jours_max: Nombre maximum de jours de conservation
            
        Returns:
            Nombre de progressions supprimées
        """
        maintenant = datetime.now()
        a_supprimer = []
        
        for id_visiteur, progression in self.progressions.items():
            derniere_activite = datetime.fromisoformat(progression.date_derniere_activite)
            if (maintenant - derniere_activite).days > jours_max:
                a_supprimer.append(id_visiteur)
        
        for id_visiteur in a_supprimer:
            del self.progressions[id_visiteur]
        
        # Sauvegarder
        if a_supprimer:
            self.sauvegarder_progression(list(self.progressions.values())[0])
        
        return len(a_supprimer)

# Test du système
if __name__ == "__main__":
    print("🌸 Test du Système de Sauvegarde de Progression")
    
    systeme = SystemeSauvegardeProgression()
    
    # Créer une progression test
    progression = systeme.creer_progression_initiale("test_visiteur_1", "developpeur")
    print(f"✅ Progression créée: {progression.id_visiteur}")
    
    # Ajouter des actions
    systeme.ajouter_action("test_visiteur_1", {
        "type": "temple_visite",
        "temple": "temple_eveil",
        "poids": 1.0
    })
    
    systeme.ajouter_action("test_visiteur_1", {
        "type": "question_posee",
        "question": "Comment fonctionne le Refuge ?",
        "poids": 0.5
    })
    
    # Vérifier la progression mise à jour
    progression_maj = systeme.charger_progression("test_visiteur_1")
    print(f"✅ Score de compréhension: {progression_maj.score_comprehension:.2f}")
    print(f"✅ Actions effectuées: {len(progression_maj.actions_effectuees)}")
    
    # Afficher les statistiques
    stats = systeme.obtenir_statistiques()
    print(f"✅ Statistiques: {stats}")
    
    print("🌸 Test terminé avec succès !")
