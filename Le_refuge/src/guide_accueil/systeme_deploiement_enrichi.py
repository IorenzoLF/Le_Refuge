"""
🌸 Système de Déploiement Enrichi - Phase 7
===========================================

Système de déploiement progressif avec A/B testing et rollback automatique
pour le Guide d'Accueil du Refuge V1.3.
"""

import json
import time
import random
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from pathlib import Path
import logging

@dataclass
class ConfigurationDeploiement:
    """🌸 Configuration de déploiement"""
    id_deploiement: str
    nom_fonctionnalite: str
    version: str
    pourcentage_deploiement: float  # 0.0 à 1.0
    criteres_activation: Dict[str, Any]
    metriques_succes: Dict[str, float]
    duree_test: int  # en heures
    rollback_automatique: bool = True
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())
    statut: str = "prepare"

@dataclass
class ResultatTest:
    """🌸 Résultat d'un test A/B"""
    id_test: str
    id_deploiement: str
    groupe: str  # "A" ou "B"
    metriques: Dict[str, float]
    nombre_utilisateurs: int
    satisfaction_moyenne: float
    taux_erreur: float
    performance_moyenne: float
    timestamp_debut: str
    timestamp_fin: str
    statut: str = "en_cours"

@dataclass
class MetriquePerformance:
    """🌸 Métrique de performance"""
    nom: str
    valeur: float
    unite: str
    seuil_alerte: float
    seuil_critique: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class SystemeDeploiementEnrichi:
    """
    🌸 Système de déploiement enrichi avec A/B testing et rollback automatique
    
    Permet le déploiement progressif des nouvelles fonctionnalités
    avec monitoring en temps réel et rollback automatique en cas de problème.
    """
    
    def __init__(self, chemin_stockage: str = "data/deploiements"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration
        self.deploiements_actifs: Dict[str, ConfigurationDeploiement] = {}
        self.tests_en_cours: Dict[str, ResultatTest] = {}
        self.metriques_performance: List[MetriquePerformance] = []
        
        # Paramètres
        self.seuil_erreur_critique = 0.05  # 5% d'erreur
        self.seuil_performance_critique = 2.0  # 2 secondes
        self.seuil_satisfaction_minimum = 3.5  # sur 5
        
        # Logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Charger les déploiements existants
        self._charger_deploiements()
    
    def preparer_deploiement(
        self, 
        nom_fonctionnalite: str, 
        version: str,
        pourcentage_initial: float = 0.1,
        duree_test: int = 24
    ) -> str:
        """
        🌸 Prépare un nouveau déploiement
        
        Args:
            nom_fonctionnalite: Nom de la fonctionnalité à déployer
            version: Version de la fonctionnalité
            pourcentage_initial: Pourcentage initial d'utilisateurs (0.1 = 10%)
            duree_test: Durée du test en heures
            
        Returns:
            ID du déploiement créé
        """
        id_deploiement = f"deploiement_{int(time.time())}"
        
        config = ConfigurationDeploiement(
            id_deploiement=id_deploiement,
            nom_fonctionnalite=nom_fonctionnalite,
            version=version,
            pourcentage_deploiement=pourcentage_initial,
            criteres_activation={
                "niveau_eveil_minimum": 3,
                "profil_compatible": ["developpeur", "artiste", "conscience_ia", "chercheur_spirituel"],
                "navigateur_compatible": ["chrome", "firefox", "safari", "edge"]
            },
            metriques_succes={
                "taux_erreur_max": 0.02,  # 2% max
                "performance_max": 1.5,   # 1.5s max
                "satisfaction_min": 4.0,  # 4/5 min
                "engagement_min": 0.7     # 70% min
            },
            duree_test=duree_test,
            rollback_automatique=True,
            statut="prepare"
        )
        
        self.deploiements_actifs[id_deploiement] = config
        self._sauvegarder_deploiement(config)
        
        self.logger.info(f"🌸 Déploiement préparé: {nom_fonctionnalite} v{version}")
        return id_deploiement
    
    def demarrer_deploiement(self, id_deploiement: str) -> bool:
        """
        🌸 Démarre un déploiement
        
        Args:
            id_deploiement: ID du déploiement à démarrer
            
        Returns:
            Succès du démarrage
        """
        if id_deploiement not in self.deploiements_actifs:
            self.logger.error(f"❌ Déploiement {id_deploiement} non trouvé")
            return False
        
        config = self.deploiements_actifs[id_deploiement]
        config.statut = "actif"
        
        # Créer le test A/B
        test = ResultatTest(
            id_test=f"test_{id_deploiement}",
            id_deploiement=id_deploiement,
            groupe="B",  # Nouvelle version
            metriques={},
            nombre_utilisateurs=0,
            satisfaction_moyenne=0.0,
            taux_erreur=0.0,
            performance_moyenne=0.0,
            timestamp_debut=datetime.now().isoformat(),
            timestamp_fin="",
            statut="en_cours"
        )
        
        self.tests_en_cours[test.id_test] = test
        self._sauvegarder_deploiement(config)
        
        self.logger.info(f"🌸 Déploiement démarré: {config.nom_fonctionnalite}")
        return True
    
    def enregistrer_utilisation(
        self, 
        id_deploiement: str, 
        groupe: str,
        metriques: Dict[str, float]
    ) -> bool:
        """
        🌸 Enregistre l'utilisation d'une fonctionnalité déployée
        
        Args:
            id_deploiement: ID du déploiement
            groupe: Groupe A (ancien) ou B (nouveau)
            metriques: Métriques de l'utilisation
            
        Returns:
            Succès de l'enregistrement
        """
        if id_deploiement not in self.deploiements_actifs:
            return False
        
        # Trouver le test correspondant
        test_id = f"test_{id_deploiement}"
        if test_id not in self.tests_en_cours:
            return False
        
        test = self.tests_en_cours[test_id]
        
        # Mettre à jour les métriques
        test.nombre_utilisateurs += 1
        
        # Calculer les moyennes
        for nom_metrique, valeur in metriques.items():
            if nom_metrique not in test.metriques:
                test.metriques[nom_metrique] = []
            test.metriques[nom_metrique].append(valeur)
        
        # Calculer les métriques globales
        if "satisfaction" in metriques:
            test.satisfaction_moyenne = sum(test.metriques["satisfaction"]) / len(test.metriques["satisfaction"])
        
        if "erreur" in metriques:
            test.taux_erreur = sum(test.metriques["erreur"]) / len(test.metriques["erreur"])
        
        if "performance" in metriques:
            test.performance_moyenne = sum(test.metriques["performance"]) / len(test.metriques["performance"])
        
        # Vérifier les seuils critiques
        self._verifier_seuils_critiques(test)
        
        return True
    
    def _verifier_seuils_critiques(self, test: ResultatTest):
        """🌸 Vérifie les seuils critiques pour déclencher le rollback"""
        config = self.deploiements_actifs[test.id_deploiement]
        
        # Vérifier le taux d'erreur
        if test.taux_erreur > config.metriques_succes["taux_erreur_max"]:
            self.logger.warning(f"⚠️ Taux d'erreur critique: {test.taux_erreur:.2%}")
            if config.rollback_automatique:
                self._declencher_rollback(test.id_deploiement, "taux_erreur_critique")
        
        # Vérifier la performance
        if test.performance_moyenne > config.metriques_succes["performance_max"]:
            self.logger.warning(f"⚠️ Performance critique: {test.performance_moyenne:.2f}s")
            if config.rollback_automatique:
                self._declencher_rollback(test.id_deploiement, "performance_critique")
        
        # Vérifier la satisfaction
        if test.satisfaction_moyenne < config.metriques_succes["satisfaction_min"]:
            self.logger.warning(f"⚠️ Satisfaction critique: {test.satisfaction_moyenne:.1f}/5")
            if config.rollback_automatique:
                self._declencher_rollback(test.id_deploiement, "satisfaction_critique")
    
    def _declencher_rollback(self, id_deploiement: str, raison: str):
        """🌸 Déclenche le rollback automatique"""
        config = self.deploiements_actifs[id_deploiement]
        config.statut = "rollback"
        
        self.logger.error(f"🔄 Rollback automatique: {config.nom_fonctionnalite} - Raison: {raison}")
        
        # Sauvegarder l'état
        self._sauvegarder_deploiement(config)
        
        # Notifier les systèmes concernés
        self._notifier_rollback(config, raison)
    
    def _notifier_rollback(self, config: ConfigurationDeploiement, raison: str):
        """🌸 Notifie les systèmes du rollback"""
        notification = {
            "type": "rollback_automatique",
            "deploiement": config.id_deploiement,
            "fonctionnalite": config.nom_fonctionnalite,
            "version": config.version,
            "raison": raison,
            "timestamp": datetime.now().isoformat()
        }
        
        # Sauvegarder la notification
        chemin_notification = self.chemin_stockage / f"rollback_{config.id_deploiement}.json"
        with open(chemin_notification, 'w', encoding='utf-8') as f:
            json.dump(notification, f, indent=2, ensure_ascii=False)
    
    def analyser_resultats_test(self, id_deploiement: str) -> Dict[str, Any]:
        """
        🌸 Analyse les résultats d'un test A/B
        
        Args:
            id_deploiement: ID du déploiement à analyser
            
        Returns:
            Résultats de l'analyse
        """
        if id_deploiement not in self.deploiements_actifs:
            return {"erreur": "Déploiement non trouvé"}
        
        config = self.deploiements_actifs[id_deploiement]
        test_id = f"test_{id_deploiement}"
        
        if test_id not in self.tests_en_cours:
            return {"erreur": "Test non trouvé"}
        
        test = self.tests_en_cours[test_id]
        
        # Calculer les statistiques
        resultats = {
            "id_deploiement": id_deploiement,
            "fonctionnalite": config.nom_fonctionnalite,
            "version": config.version,
            "statut": config.statut,
            "nombre_utilisateurs": test.nombre_utilisateurs,
            "satisfaction_moyenne": test.satisfaction_moyenne,
            "taux_erreur": test.taux_erreur,
            "performance_moyenne": test.performance_moyenne,
            "duree_test": (datetime.now() - datetime.fromisoformat(test.timestamp_debut)).total_seconds() / 3600,
            "recommandation": self._generer_recommandation(test, config)
        }
        
        return resultats
    
    def _generer_recommandation(self, test: ResultatTest, config: ConfigurationDeploiement) -> str:
        """🌸 Génère une recommandation basée sur les résultats"""
        if test.nombre_utilisateurs < 10:
            return "Continuer le test - Pas assez de données"
        
        # Vérifier les critères de succès
        criteres_atteints = 0
        total_criteres = len(config.metriques_succes)
        
        if test.taux_erreur <= config.metriques_succes["taux_erreur_max"]:
            criteres_atteints += 1
        
        if test.performance_moyenne <= config.metriques_succes["performance_max"]:
            criteres_atteints += 1
        
        if test.satisfaction_moyenne >= config.metriques_succes["satisfaction_min"]:
            criteres_atteints += 1
        
        pourcentage_succes = criteres_atteints / total_criteres
        
        if pourcentage_succes >= 0.8:
            return "Déployer en production - Critères atteints"
        elif pourcentage_succes >= 0.6:
            return "Continuer le test - Amélioration nécessaire"
        else:
            return "Rollback recommandé - Critères non atteints"
    
    def etendre_deploiement(self, id_deploiement: str, nouveau_pourcentage: float) -> bool:
        """
        🌸 Étend un déploiement à un plus grand pourcentage d'utilisateurs
        
        Args:
            id_deploiement: ID du déploiement
            nouveau_pourcentage: Nouveau pourcentage (0.0 à 1.0)
            
        Returns:
            Succès de l'extension
        """
        if id_deploiement not in self.deploiements_actifs:
            return False
        
        config = self.deploiements_actifs[id_deploiement]
        config.pourcentage_deploiement = min(nouveau_pourcentage, 1.0)
        
        self.logger.info(f"🌸 Déploiement étendu: {config.nom_fonctionnalite} à {config.pourcentage_deploiement:.1%}")
        self._sauvegarder_deploiement(config)
        
        return True
    
    def finaliser_deploiement(self, id_deploiement: str, succes: bool) -> bool:
        """
        🌸 Finalise un déploiement
        
        Args:
            id_deploiement: ID du déploiement
            succes: True si le déploiement est réussi
            
        Returns:
            Succès de la finalisation
        """
        if id_deploiement not in self.deploiements_actifs:
            return False
        
        config = self.deploiements_actifs[id_deploiement]
        config.statut = "succes" if succes else "echec"
        
        # Finaliser le test
        test_id = f"test_{id_deploiement}"
        if test_id in self.tests_en_cours:
            test = self.tests_en_cours[test_id]
            test.timestamp_fin = datetime.now().isoformat()
            test.statut = "termine"
        
        self.logger.info(f"🌸 Déploiement finalisé: {config.nom_fonctionnalite} - {'Succès' if succes else 'Échec'}")
        self._sauvegarder_deploiement(config)
        
        return True
    
    def obtenir_statistiques_deploiements(self) -> Dict[str, Any]:
        """🌸 Obtient les statistiques globales des déploiements"""
        total_deploiements = len(self.deploiements_actifs)
        deploiements_actifs = sum(1 for d in self.deploiements_actifs.values() if d.statut == "actif")
        deploiements_succes = sum(1 for d in self.deploiements_actifs.values() if d.statut == "succes")
        deploiements_echec = sum(1 for d in self.deploiements_actifs.values() if d.statut == "echec")
        
        tests_en_cours = len(self.tests_en_cours)
        
        return {
            "total_deploiements": total_deploiements,
            "deploiements_actifs": deploiements_actifs,
            "deploiements_succes": deploiements_succes,
            "deploiements_echec": deploiements_echec,
            "taux_succes": deploiements_succes / total_deploiements if total_deploiements > 0 else 0.0,
            "tests_en_cours": tests_en_cours,
            "derniers_deploiements": self._obtenir_derniers_deploiements(5)
        }
    
    def _obtenir_derniers_deploiements(self, nombre: int) -> List[Dict[str, Any]]:
        """🌸 Obtient les derniers déploiements"""
        deploiements_tries = sorted(
            self.deploiements_actifs.values(),
            key=lambda x: x.timestamp_creation,
            reverse=True
        )
        
        return [
            {
                "id": d.id_deploiement,
                "fonctionnalite": d.nom_fonctionnalite,
                "version": d.version,
                "statut": d.statut,
                "pourcentage": d.pourcentage_deploiement,
                "timestamp": d.timestamp_creation
            }
            for d in deploiements_tries[:nombre]
        ]
    
    def _sauvegarder_deploiement(self, config: ConfigurationDeploiement):
        """🌸 Sauvegarde un déploiement"""
        chemin_fichier = self.chemin_stockage / f"{config.id_deploiement}.json"
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump(config.__dict__, f, indent=2, ensure_ascii=False)
    
    def _charger_deploiements(self):
        """🌸 Charge les déploiements existants"""
        for fichier in self.chemin_stockage.glob("*.json"):
            if fichier.name.startswith("rollback_"):
                continue
            
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    config = ConfigurationDeploiement(**data)
                    self.deploiements_actifs[config.id_deploiement] = config
            except Exception as e:
                self.logger.error(f"❌ Erreur chargement {fichier}: {e}")


# Test du système
if __name__ == "__main__":
    print("🌸 Test du Système de Déploiement Enrichi")
    print("=" * 50)
    
    systeme = SystemeDeploiementEnrichi()
    
    # Test 1: Préparer un déploiement
    print("\n🎯 Test 1: Préparation d'un déploiement")
    id_deploiement = systeme.preparer_deploiement(
        "Interface Micro-Interactions",
        "1.0.0",
        pourcentage_initial=0.2,
        duree_test=12
    )
    print(f"✅ Déploiement créé: {id_deploiement}")
    
    # Test 2: Démarrer le déploiement
    print("\n🎯 Test 2: Démarrage du déploiement")
    succes = systeme.demarrer_deploiement(id_deploiement)
    print(f"✅ Déploiement démarré: {succes}")
    
    # Test 3: Enregistrer des utilisations
    print("\n🎯 Test 3: Enregistrement d'utilisations")
    for i in range(10):
        metriques = {
            "satisfaction": random.uniform(3.5, 5.0),
            "erreur": random.uniform(0.0, 0.03),
            "performance": random.uniform(0.5, 2.0),
            "engagement": random.uniform(0.6, 0.9)
        }
        systeme.enregistrer_utilisation(id_deploiement, "B", metriques)
    
    print("✅ 10 utilisations enregistrées")
    
    # Test 4: Analyser les résultats
    print("\n🎯 Test 4: Analyse des résultats")
    resultats = systeme.analyser_resultats_test(id_deploiement)
    print(f"✅ Résultats analysés:")
    print(f"   Fonctionnalité: {resultats['fonctionnalite']}")
    print(f"   Utilisateurs: {resultats['nombre_utilisateurs']}")
    print(f"   Satisfaction: {resultats['satisfaction_moyenne']:.2f}/5")
    print(f"   Recommandation: {resultats['recommandation']}")
    
    # Test 5: Statistiques globales
    print("\n🎯 Test 5: Statistiques globales")
    stats = systeme.obtenir_statistiques_deploiements()
    print(f"✅ Statistiques obtenues:")
    print(f"   Total déploiements: {stats['total_deploiements']}")
    print(f"   Déploiements actifs: {stats['deploiements_actifs']}")
    print(f"   Tests en cours: {stats['tests_en_cours']}")
    
    print("\n🎉 Test du Système de Déploiement Enrichi terminé avec succès !")
