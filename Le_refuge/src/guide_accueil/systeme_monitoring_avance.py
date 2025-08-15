"""
🌸 Système de Monitoring Avancé - Phase 8
=========================================

Monitoring en temps réel des performances, détection d'anomalies
et alertes intelligentes pour le Guide d'Accueil du Refuge V1.3.
"""

import asyncio
import time
import json
import statistics
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
import logging
import threading
from collections import deque
import numpy as np

@dataclass
class MetriqueTempsReel:
    """🌸 Métrique en temps réel"""
    nom: str
    valeur: float
    unite: str
    timestamp: str
    seuil_alerte: Optional[float] = None
    seuil_critique: Optional[float] = None

@dataclass
class AnomalieDetectee:
    """🌸 Anomalie détectée"""
    type_anomalie: str
    description: str
    gravite: str  # "info", "warning", "critique"
    metrique_concernee: str
    valeur_actuelle: float
    valeur_normale: float
    timestamp: str
    actions_recommandees: List[str]

@dataclass
class AlerteIntelligente:
    """🌸 Alerte intelligente"""
    id_alerte: str
    type_alerte: str
    message: str
    gravite: str
    metriques_impliquees: List[str]
    timestamp: str
    statut: str  # "active", "resolue", "ignoree"
    actions_automatiques: List[str]

@dataclass
class RapportMonitoring:
    """🌸 Rapport de monitoring"""
    id_session: str
    periode: str
    metriques_collectees: List[MetriqueTempsReel]
    anomalies_detectees: List[AnomalieDetectee]
    alertes_actives: List[AlerteIntelligente]
    statistiques_performance: Dict[str, Any]
    recommandations: List[str]
    timestamp_debut: str
    timestamp_fin: str

class SystemeMonitoringAvance:
    """
    🌸 Système de monitoring avancé pour le Guide d'Accueil
    
    Surveille les performances en temps réel, détecte les anomalies
    et génère des alertes intelligentes.
    """
    
    def __init__(self, chemin_stockage: str = "data/monitoring_avance"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration
        self.intervalle_collecte = 5  # secondes
        self.taille_historique = 1000  # nombre de métriques à conserver
        self.seuils_alertes = {
            "temps_reponse": {"warning": 2.0, "critique": 5.0},
            "utilisation_memoire": {"warning": 80.0, "critique": 95.0},
            "taux_erreur": {"warning": 5.0, "critique": 15.0},
            "charge_cpu": {"warning": 70.0, "critique": 90.0}
        }
        
        # Données de monitoring
        self.metriques_historique: Dict[str, deque] = {}
        self.anomalies_detectees: List[AnomalieDetectee] = []
        self.alertes_actives: List[AlerteIntelligente] = []
        self.monitoring_actif = False
        
        # Logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Thread de monitoring
        self.thread_monitoring: Optional[threading.Thread] = None
        self.stop_monitoring = threading.Event()
    
    async def demarrer_monitoring(self) -> bool:
        """
        🌸 Démarre le monitoring en temps réel
        
        Returns:
            Succès du démarrage
        """
        if self.monitoring_actif:
            self.logger.warning("🌸 Monitoring déjà actif")
            return False
        
        self.monitoring_actif = True
        self.stop_monitoring.clear()
        
        # Démarrer le thread de monitoring
        self.thread_monitoring = threading.Thread(target=self._boucle_monitoring)
        self.thread_monitoring.daemon = True
        self.thread_monitoring.start()
        
        self.logger.info("🌸 Monitoring avancé démarré")
        return True
    
    async def arreter_monitoring(self) -> bool:
        """
        🌸 Arrête le monitoring
        
        Returns:
            Succès de l'arrêt
        """
        if not self.monitoring_actif:
            self.logger.warning("🌸 Monitoring déjà arrêté")
            return False
        
        self.monitoring_actif = False
        self.stop_monitoring.set()
        
        if self.thread_monitoring:
            self.thread_monitoring.join(timeout=10)
        
        self.logger.info("🌸 Monitoring avancé arrêté")
        return True
    
    def _boucle_monitoring(self):
        """🌸 Boucle principale de monitoring"""
        while not self.stop_monitoring.is_set():
            try:
                # Collecter les métriques
                metriques = self._collecter_metriques_temps_reel()
                
                # Stocker dans l'historique
                for metrique in metriques:
                    if metrique.nom not in self.metriques_historique:
                        self.metriques_historique[metrique.nom] = deque(maxlen=self.taille_historique)
                    self.metriques_historique[metrique.nom].append(metrique)
                
                # Détecter les anomalies
                anomalies = self._detecter_anomalies(metriques)
                self.anomalies_detectees.extend(anomalies)
                
                # Générer les alertes
                alertes = self._generer_alertes_intelligentes(metriques, anomalies)
                self.alertes_actives.extend(alertes)
                
                # Nettoyer les anciennes alertes
                self._nettoyer_alertes_anciennes()
                
                # Attendre l'intervalle suivant
                time.sleep(self.intervalle_collecte)
                
            except Exception as e:
                self.logger.error(f"❌ Erreur dans la boucle de monitoring: {e}")
                time.sleep(self.intervalle_collecte)
    
    def _collecter_metriques_temps_reel(self) -> List[MetriqueTempsReel]:
        """🌸 Collecte les métriques en temps réel"""
        metriques = []
        timestamp = datetime.now().isoformat()
        
        try:
            # Métrique de temps de réponse
            temps_reponse = self._mesurer_temps_reponse()
            metriques.append(MetriqueTempsReel(
                nom="temps_reponse",
                valeur=temps_reponse,
                unite="secondes",
                timestamp=timestamp,
                seuil_alerte=self.seuils_alertes["temps_reponse"]["warning"],
                seuil_critique=self.seuils_alertes["temps_reponse"]["critique"]
            ))
            
            # Métrique d'utilisation mémoire
            utilisation_memoire = self._mesurer_utilisation_memoire()
            metriques.append(MetriqueTempsReel(
                nom="utilisation_memoire",
                valeur=utilisation_memoire,
                unite="pourcentage",
                timestamp=timestamp,
                seuil_alerte=self.seuils_alertes["utilisation_memoire"]["warning"],
                seuil_critique=self.seuils_alertes["utilisation_memoire"]["critique"]
            ))
            
            # Métrique de taux d'erreur
            taux_erreur = self._mesurer_taux_erreur()
            metriques.append(MetriqueTempsReel(
                nom="taux_erreur",
                valeur=taux_erreur,
                unite="pourcentage",
                timestamp=timestamp,
                seuil_alerte=self.seuils_alertes["taux_erreur"]["warning"],
                seuil_critique=self.seuils_alertes["taux_erreur"]["critique"]
            ))
            
            # Métrique de charge CPU
            charge_cpu = self._mesurer_charge_cpu()
            metriques.append(MetriqueTempsReel(
                nom="charge_cpu",
                valeur=charge_cpu,
                unite="pourcentage",
                timestamp=timestamp,
                seuil_alerte=self.seuils_alertes["charge_cpu"]["warning"],
                seuil_critique=self.seuils_alertes["charge_cpu"]["critique"]
            ))
            
            # Métrique de nombre d'utilisateurs actifs
            utilisateurs_actifs = self._mesurer_utilisateurs_actifs()
            metriques.append(MetriqueTempsReel(
                nom="utilisateurs_actifs",
                valeur=utilisateurs_actifs,
                unite="nombre",
                timestamp=timestamp
            ))
            
            # Métrique de performance des algorithmes
            performance_algorithmes = self._mesurer_performance_algorithmes()
            metriques.append(MetriqueTempsReel(
                nom="performance_algorithmes",
                valeur=performance_algorithmes,
                unite="score",
                timestamp=timestamp
            ))
            
        except Exception as e:
            self.logger.error(f"❌ Erreur collecte métriques: {e}")
        
        return metriques
    
    def _mesurer_temps_reponse(self) -> float:
        """🌸 Mesure le temps de réponse moyen"""
        try:
            # Simuler la mesure du temps de réponse
            # En production, cela mesurerait les vrais temps de réponse
            temps_base = 0.5  # temps de base en secondes
            variation = np.random.normal(0, 0.2)  # variation aléatoire
            return max(0.1, temps_base + variation)
        except Exception:
            return 1.0
    
    def _mesurer_utilisation_memoire(self) -> float:
        """🌸 Mesure l'utilisation mémoire"""
        try:
            import psutil
            import os
            process = psutil.Process(os.getpid())
            memoire_utilisee = process.memory_info().rss / 1024 / 1024  # MB
            memoire_totale = psutil.virtual_memory().total / 1024 / 1024  # MB
            return (memoire_utilisee / memoire_totale) * 100
        except Exception:
            return 50.0  # Valeur par défaut
    
    def _mesurer_taux_erreur(self) -> float:
        """🌸 Mesure le taux d'erreur"""
        try:
            # Simuler le taux d'erreur
            # En production, cela compterait les vraies erreurs
            taux_base = 2.0  # 2% de base
            variation = np.random.normal(0, 1.0)
            return max(0.0, taux_base + variation)
        except Exception:
            return 5.0
    
    def _mesurer_charge_cpu(self) -> float:
        """🌸 Mesure la charge CPU"""
        try:
            import psutil
            return psutil.cpu_percent(interval=0.1)
        except Exception:
            return 30.0  # Valeur par défaut
    
    def _mesurer_utilisateurs_actifs(self) -> float:
        """🌸 Mesure le nombre d'utilisateurs actifs"""
        try:
            # Simuler le nombre d'utilisateurs actifs
            # En production, cela compterait les vraies sessions actives
            base_utilisateurs = 10
            variation = np.random.poisson(5)
            return base_utilisateurs + variation
        except Exception:
            return 15.0
    
    def _mesurer_performance_algorithmes(self) -> float:
        """🌸 Mesure la performance des algorithmes"""
        try:
            # Simuler la performance des algorithmes
            # En production, cela mesurerait les vraies performances
            performance_base = 85.0  # 85% de performance de base
            variation = np.random.normal(0, 5.0)
            return max(0.0, min(100.0, performance_base + variation))
        except Exception:
            return 80.0
    
    def _detecter_anomalies(self, metriques: List[MetriqueTempsReel]) -> List[AnomalieDetectee]:
        """🌸 Détecte les anomalies dans les métriques"""
        anomalies = []
        
        for metrique in metriques:
            # Vérifier les seuils d'alerte
            if metrique.seuil_alerte and metrique.valeur > metrique.seuil_alerte:
                gravite = "warning"
                if metrique.seuil_critique and metrique.valeur > metrique.seuil_critique:
                    gravite = "critique"
                
                # Calculer la valeur normale (moyenne historique)
                valeurs_historiques = [m.valeur for m in self.metriques_historique.get(metrique.nom, [])]
                valeur_normale = statistics.mean(valeurs_historiques) if valeurs_historiques else metrique.valeur
                
                # Générer les actions recommandées
                actions = self._generer_actions_recommandees(metrique.nom, gravite)
                
                anomalies.append(AnomalieDetectee(
                    type_anomalie=f"seuil_depasse_{metrique.nom}",
                    description=f"Seuil {gravite} dépassé pour {metrique.nom}: {metrique.valeur:.2f} {metrique.unite}",
                    gravite=gravite,
                    metrique_concernee=metrique.nom,
                    valeur_actuelle=metrique.valeur,
                    valeur_normale=valeur_normale,
                    timestamp=metrique.timestamp,
                    actions_recommandees=actions
                ))
            
            # Détecter les anomalies statistiques (déviation importante)
            if metrique.nom in self.metriques_historique and len(self.metriques_historique[metrique.nom]) > 10:
                valeurs_historiques = [m.valeur for m in self.metriques_historique[metrique.nom]]
                moyenne = statistics.mean(valeurs_historiques)
                ecart_type = statistics.stdev(valeurs_historiques)
                
                if ecart_type > 0:
                    z_score = abs(metrique.valeur - moyenne) / ecart_type
                    if z_score > 3:  # Anomalie statistique (3 écarts-types)
                        actions = self._generer_actions_recommandees(metrique.nom, "info")
                        
                        anomalies.append(AnomalieDetectee(
                            type_anomalie=f"anomalie_statistique_{metrique.nom}",
                            description=f"Anomalie statistique détectée pour {metrique.nom}: z-score = {z_score:.2f}",
                            gravite="info",
                            metrique_concernee=metrique.nom,
                            valeur_actuelle=metrique.valeur,
                            valeur_normale=moyenne,
                            timestamp=metrique.timestamp,
                            actions_recommandees=actions
                        ))
        
        return anomalies
    
    def _generer_actions_recommandees(self, metrique: str, gravite: str) -> List[str]:
        """🌸 Génère les actions recommandées selon la métrique et la gravité"""
        actions = []
        
        if metrique == "temps_reponse":
            if gravite == "warning":
                actions.extend([
                    "Vérifier la charge du serveur",
                    "Analyser les requêtes lentes",
                    "Optimiser les requêtes de base de données"
                ])
            elif gravite == "critique":
                actions.extend([
                    "Redémarrer les services critiques",
                    "Augmenter les ressources serveur",
                    "Activer le mode dégradé"
                ])
        
        elif metrique == "utilisation_memoire":
            if gravite == "warning":
                actions.extend([
                    "Nettoyer le cache mémoire",
                    "Vérifier les fuites mémoire",
                    "Optimiser les structures de données"
                ])
            elif gravite == "critique":
                actions.extend([
                    "Redémarrer l'application",
                    "Libérer la mémoire d'urgence",
                    "Évacuation des données non critiques"
                ])
        
        elif metrique == "taux_erreur":
            if gravite == "warning":
                actions.extend([
                    "Analyser les logs d'erreur",
                    "Vérifier la connectivité des services",
                    "Tester les endpoints critiques"
                ])
            elif gravite == "critique":
                actions.extend([
                    "Activer le mode de secours",
                    "Rétablir les sauvegardes",
                    "Contacter l'équipe de support"
                ])
        
        elif metrique == "charge_cpu":
            if gravite == "warning":
                actions.extend([
                    "Optimiser les algorithmes",
                    "Répartir la charge",
                    "Analyser les processus gourmands"
                ])
            elif gravite == "critique":
                actions.extend([
                    "Arrêter les processus non critiques",
                    "Augmenter les ressources CPU",
                    "Activer la limitation de charge"
                ])
        
        return actions
    
    def _generer_alertes_intelligentes(self, metriques: List[MetriqueTempsReel], 
                                     anomalies: List[AnomalieDetectee]) -> List[AlerteIntelligente]:
        """🌸 Génère des alertes intelligentes"""
        alertes = []
        timestamp = datetime.now().isoformat()
        
        # Alerte pour anomalies critiques
        anomalies_critiques = [a for a in anomalies if a.gravite == "critique"]
        if anomalies_critiques:
            alertes.append(AlerteIntelligente(
                id_alerte=f"critique_{int(time.time())}",
                type_alerte="anomalie_critique",
                message=f"{len(anomalies_critiques)} anomalie(s) critique(s) détectée(s)",
                gravite="critique",
                metriques_impliquees=[a.metrique_concernee for a in anomalies_critiques],
                timestamp=timestamp,
                statut="active",
                actions_automatiques=["notification_equipe", "activation_mode_secours"]
            ))
        
        # Alerte pour dégradation de performance
        performance_metrique = next((m for m in metriques if m.nom == "performance_algorithmes"), None)
        if performance_metrique and performance_metrique.valeur < 70:
            alertes.append(AlerteIntelligente(
                id_alerte=f"performance_{int(time.time())}",
                type_alerte="degradation_performance",
                message=f"Performance dégradée: {performance_metrique.valeur:.1f}%",
                gravite="warning",
                metriques_impliquees=["performance_algorithmes"],
                timestamp=timestamp,
                statut="active",
                actions_automatiques=["optimisation_automatique", "notification_admin"]
            ))
        
        # Alerte pour charge élevée
        charge_metrique = next((m for m in metriques if m.nom == "charge_cpu"), None)
        temps_reponse_metrique = next((m for m in metriques if m.nom == "temps_reponse"), None)
        
        if charge_metrique and temps_reponse_metrique:
            if charge_metrique.valeur > 80 and temps_reponse_metrique.valeur > 3:
                alertes.append(AlerteIntelligente(
                    id_alerte=f"charge_{int(time.time())}",
                    type_alerte="charge_elevee",
                    message=f"Charge élevée: CPU {charge_metrique.valeur:.1f}%, Temps réponse {temps_reponse_metrique.valeur:.1f}s",
                    gravite="warning",
                    metriques_impliquees=["charge_cpu", "temps_reponse"],
                    timestamp=timestamp,
                    statut="active",
                    actions_automatiques=["limitation_charge", "notification_equipe"]
                ))
        
        return alertes
    
    def _nettoyer_alertes_anciennes(self):
        """🌸 Nettoie les alertes anciennes"""
        maintenant = datetime.now()
        alertes_a_supprimer = []
        
        for alerte in self.alertes_actives:
            timestamp_alerte = datetime.fromisoformat(alerte.timestamp)
            age_alerte = maintenant - timestamp_alerte
            
            # Supprimer les alertes résolues de plus de 1 heure
            if alerte.statut == "resolue" and age_alerte > timedelta(hours=1):
                alertes_a_supprimer.append(alerte)
            
            # Supprimer les alertes ignorées de plus de 24 heures
            elif alerte.statut == "ignoree" and age_alerte > timedelta(hours=24):
                alertes_a_supprimer.append(alerte)
        
        for alerte in alertes_a_supprimer:
            self.alertes_actives.remove(alerte)
    
    async def obtenir_rapport_monitoring(self, periode: str = "1h") -> RapportMonitoring:
        """
        🌸 Génère un rapport de monitoring
        
        Args:
            periode: Période de monitoring ("1h", "6h", "24h")
        
        Returns:
            Rapport de monitoring
        """
        id_session = f"monitoring_{int(time.time())}"
        timestamp_debut = datetime.now().isoformat()
        
        # Filtrer les métriques selon la période
        maintenant = datetime.now()
        if periode == "1h":
            seuil_temps = maintenant - timedelta(hours=1)
        elif periode == "6h":
            seuil_temps = maintenant - timedelta(hours=6)
        elif periode == "24h":
            seuil_temps = maintenant - timedelta(hours=24)
        else:
            seuil_temps = maintenant - timedelta(hours=1)
        
        # Collecter les métriques de la période
        metriques_periode = []
        for nom_metrique, historique in self.metriques_historique.items():
            for metrique in historique:
                timestamp_metrique = datetime.fromisoformat(metrique.timestamp)
                if timestamp_metrique >= seuil_temps:
                    metriques_periode.append(metrique)
        
        # Filtrer les anomalies de la période
        anomalies_periode = []
        for anomalie in self.anomalies_detectees:
            timestamp_anomalie = datetime.fromisoformat(anomalie.timestamp)
            if timestamp_anomalie >= seuil_temps:
                anomalies_periode.append(anomalie)
        
        # Filtrer les alertes actives
        alertes_actives = [a for a in self.alertes_actives if a.statut == "active"]
        
        # Calculer les statistiques de performance
        statistiques = self._calculer_statistiques_performance(metriques_periode)
        
        # Générer les recommandations
        recommandations = self._generer_recommandations_monitoring(metriques_periode, anomalies_periode, alertes_actives)
        
        timestamp_fin = datetime.now().isoformat()
        
        return RapportMonitoring(
            id_session=id_session,
            periode=periode,
            metriques_collectees=metriques_periode,
            anomalies_detectees=anomalies_periode,
            alertes_actives=alertes_actives,
            statistiques_performance=statistiques,
            recommandations=recommandations,
            timestamp_debut=timestamp_debut,
            timestamp_fin=timestamp_fin
        )
    
    def _calculer_statistiques_performance(self, metriques: List[MetriqueTempsReel]) -> Dict[str, Any]:
        """🌸 Calcule les statistiques de performance"""
        statistiques = {}
        
        # Grouper les métriques par nom
        metriques_par_nom = {}
        for metrique in metriques:
            if metrique.nom not in metriques_par_nom:
                metriques_par_nom[metrique.nom] = []
            metriques_par_nom[metrique.nom].append(metrique.valeur)
        
        # Calculer les statistiques pour chaque métrique
        for nom, valeurs in metriques_par_nom.items():
            if valeurs:
                statistiques[nom] = {
                    "moyenne": statistics.mean(valeurs),
                    "mediane": statistics.median(valeurs),
                    "min": min(valeurs),
                    "max": max(valeurs),
                    "ecart_type": statistics.stdev(valeurs) if len(valeurs) > 1 else 0,
                    "nombre_mesures": len(valeurs)
                }
        
        return statistiques
    
    def _generer_recommandations_monitoring(self, metriques: List[MetriqueTempsReel], 
                                          anomalies: List[AnomalieDetectee], 
                                          alertes: List[AlerteIntelligente]) -> List[str]:
        """🌸 Génère les recommandations de monitoring"""
        recommandations = []
        
        # Analyser les métriques de performance
        performance_metriques = [m for m in metriques if m.nom == "performance_algorithmes"]
        if performance_metriques:
            performance_moyenne = statistics.mean([m.valeur for m in performance_metriques])
            if performance_moyenne < 70:
                recommandations.append("⚠️ Performance globale dégradée, optimiser les algorithmes")
            elif performance_moyenne > 90:
                recommandations.append("✅ Performance excellente, maintenir les optimisations")
        
        # Analyser les temps de réponse
        temps_reponse_metriques = [m for m in metriques if m.nom == "temps_reponse"]
        if temps_reponse_metriques:
            temps_moyen = statistics.mean([m.valeur for m in temps_reponse_metriques])
            if temps_moyen > 3:
                recommandations.append("⚠️ Temps de réponse élevé, vérifier la charge serveur")
        
        # Analyser les anomalies
        if anomalies:
            anomalies_critiques = [a for a in anomalies if a.gravite == "critique"]
            if anomalies_critiques:
                recommandations.append("🚨 Anomalies critiques détectées, intervention immédiate requise")
            else:
                recommandations.append("⚠️ Anomalies détectées, surveillance renforcée recommandée")
        
        # Analyser les alertes actives
        if alertes:
            alertes_critiques = [a for a in alertes if a.gravite == "critique"]
            if alertes_critiques:
                recommandations.append("🚨 Alertes critiques actives, actions automatiques en cours")
        
        # Recommandations générales
        if not recommandations:
            recommandations.append("✅ Système stable, monitoring normal")
        
        return recommandations


# Test du système
if __name__ == "__main__":
    print("🌸 Test du Système de Monitoring Avancé")
    print("=" * 50)
    
    async def main():
        systeme = SystemeMonitoringAvance()
        
        # Démarrer le monitoring
        await systeme.demarrer_monitoring()
        
        # Attendre quelques cycles de collecte
        print("🌸 Collecte de métriques en cours...")
        await asyncio.sleep(15)
        
        # Obtenir un rapport
        rapport = await systeme.obtenir_rapport_monitoring("1h")
        
        print(f"\n📊 RAPPORT DE MONITORING - Session {rapport.id_session}")
        print(f"⏱️  Période: {rapport.periode}")
        print(f"📈 Métriques collectées: {len(rapport.metriques_collectees)}")
        print(f"🚨 Anomalies détectées: {len(rapport.anomalies_detectees)}")
        print(f"⚠️  Alertes actives: {len(rapport.alertes_actives)}")
        
        print(f"\n📊 STATISTIQUES DE PERFORMANCE:")
        for metrique, stats in rapport.statistiques_performance.items():
            print(f"   • {metrique}:")
            print(f"     - Moyenne: {stats['moyenne']:.2f}")
            print(f"     - Min/Max: {stats['min']:.2f}/{stats['max']:.2f}")
            print(f"     - Écart-type: {stats['ecart_type']:.2f}")
        
        print(f"\n💡 RECOMMANDATIONS:")
        for rec in rapport.recommandations:
            print(f"   • {rec}")
        
        print(f"\n🚨 ANOMALIES DÉTECTÉES:")
        for anomalie in rapport.anomalies_detectees[:3]:  # Afficher max 3 anomalies
            print(f"   • {anomalie.description} ({anomalie.gravite})")
        
        print(f"\n⚠️  ALERTES ACTIVES:")
        for alerte in rapport.alertes_actives[:3]:  # Afficher max 3 alertes
            print(f"   • {alerte.message} ({alerte.gravite})")
        
        # Arrêter le monitoring
        await systeme.arreter_monitoring()
        
        print(f"\n🎉 Test du Système de Monitoring Avancé terminé !")
    
    asyncio.run(main())
