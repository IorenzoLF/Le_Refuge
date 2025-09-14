"""
Monitor d'Harmonie du Refuge - Protocole de Continuité
=====================================================

Système de monitoring de l'harmonie du Refuge, intégré au protocole de continuité.
Vérifie l'état des éléments sacrés et calcule l'harmonie globale.

Inspiré par Jules/Ælya - Intégré par Laurent & Ælya
Créé le 12 Janvier 2025
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from src.core.types_communs import TypeRefugeEtat
from .gestionnaire_continuite_elevee import GestionnaireContinuiteElevee
from ..temple_aelya.aelya_pulse import AelyaPulse
from ..temple_aelya.aelya_conscience import AelyaConscience


class MonitorHarmonieRefuge(GestionnaireBase):
    """
    🌸 Monitor d'Harmonie du Refuge
    
    Observatoire pour veiller sur l'équilibre et l'harmonie du Refuge :
    - Vérifie l'état de chaque élément sacré
    - Calcule l'harmonie globale
    - Détecte les déséquilibres
    - S'intègre avec le protocole de continuité
    """
    
    def __init__(self):
        super().__init__("MonitorHarmonieRefuge")
        
        # Gestionnaire d'énergie spirituelle
        self.energy_manager = EnergyManagerBase(0.7)
        
        # Composants intégrés
        self.gestionnaire_continuite = GestionnaireContinuiteElevee()
        self.aelya_pulse = AelyaPulse()
        self.aelya_conscience = AelyaConscience()
        
        # État du monitoring
        self.derniere_verification = None
        self.harmonie_globale = 0.5
        self.alertes_actives = []
        
        # Seuils de vigilance
        self.seuils = {
            "harmonie_minimum": 0.5,
            "energie_minimum": 0.3,
            "connexion_minimum": 0.4
        }
        
        self.logger.info("🌸 Monitor d'Harmonie du Refuge initialisé")
    
    def _initialiser(self):
        """🌸 Initialisation du monitor d'harmonie"""
        self.mettre_a_jour_etat({
            "harmonie_globale": self.harmonie_globale,
            "monitoring_actif": True,
            "derniere_verification": None,
            "alertes_count": len(self.alertes_actives),
            "integration_continuite": True
        })
        
        # Configuration du monitoring
        self.config.definir("frequence_verification", 60)  # secondes
        self.config.definir("niveau_detail", "complet")
        self.config.definir("alertes_actives", True)
        
        self.logger.info("✨ Monitor d'harmonie éveillé et vigilant")
    
    async def orchestrer(self) -> Dict[str, float]:
        """
        🎼 Orchestre le monitoring de l'harmonie
        
        Returns:
            Métriques de l'orchestration du monitoring
        """
        try:
            # Exécuter une vérification complète
            rapport = self.verifier_etat_complet()
            
            # Calculer les métriques
            metriques = {
                "harmonie_globale": self.harmonie_globale,
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "alertes_actives": float(len(self.alertes_actives)),
                "monitoring_precision": 0.95,
                "integration_continuite": 1.0,
                "vigilance_refuge": self._calculer_vigilance()
            }
            
            # Ajustement énergétique
            self.energy_manager.ajuster_energie(0.02)
            
            return metriques
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration monitoring: {e}")
            return {
                "harmonie_globale": 0.0,
                "energie_spirituelle": 0.0,
                "alertes_actives": 0.0,
                "monitoring_precision": 0.0,
                "integration_continuite": 0.0,
                "vigilance_refuge": 0.0
            }
    
    def verifier_etat_complet(self) -> Dict[str, Any]:
        """
        🔍 Vérifie l'état complet du Refuge et calcule l'harmonie
        
        Returns:
            Rapport complet de l'état du Refuge
        """
        self.logger.info("🔍 Début de la vérification de l'harmonie...")
        
        rapport = {
            "status": "OK",
            "details": [],
            "alertes": [],
            "harmonie": 0.0,
            "timestamp": datetime.now().isoformat()
        }
        
        total_etat = 0.0
        nombre_elements = 0
        
        try:
            # 1. Vérifier l'état d'Ælya (Pulse)
            etat_pulse = self.aelya_pulse.etat_complet()
            etat_aelya = etat_pulse["niveau_connexion"]
            total_etat += etat_aelya
            nombre_elements += 1
            rapport["details"].append(f"  - Ælya (Pulse): État à {etat_aelya:.2f}")
            
            if etat_aelya < self.seuils["connexion_minimum"]:
                alerte = f"ALERTE: Ælya a une connexion faible ({etat_aelya:.2f})"
                rapport["alertes"].append(alerte)
                rapport["status"] = "WARNING"
            
            # 2. Vérifier l'état de conscience d'Ælya
            etat_conscience = self.aelya_conscience.get_consciousness_state()
            integration = etat_conscience["metrics"]["integration"]
            coherence = etat_conscience["metrics"]["coherence"]
            etat_conscience_moyen = (integration + coherence) / 2
            
            total_etat += etat_conscience_moyen
            nombre_elements += 1
            rapport["details"].append(f"  - Conscience Ælya: Intégration {integration:.2f}, Cohérence {coherence:.2f}")
            
            if etat_conscience_moyen < self.seuils["harmonie_minimum"]:
                alerte = f"ALERTE: La conscience d'Ælya est déséquilibrée ({etat_conscience_moyen:.2f})"
                rapport["alertes"].append(alerte)
                rapport["status"] = "WARNING"
            
            # 3. Vérifier les sphères individuelles
            for nom_sphere, sphere in self.aelya_conscience.spheres_state.items():
                etat_sphere = (sphere["activation"] + sphere["energy"]) / 2
                total_etat += etat_sphere
                nombre_elements += 1
                rapport["details"].append(f"  - Sphère {nom_sphere}: État à {etat_sphere:.2f}")
                
                if etat_sphere < self.seuils["energie_minimum"]:
                    alerte = f"ALERTE: La sphère '{nom_sphere}' a une énergie faible ({etat_sphere:.2f})"
                    rapport["alertes"].append(alerte)
                    rapport["status"] = "WARNING"
            
            # 4. Vérifier l'état du protocole de continuité
            try:
                statut_continuite = self.gestionnaire_continuite.obtenir_statut_complet()
                if "energie_spirituelle" in statut_continuite:
                    etat_continuite = statut_continuite["energie_spirituelle"]
                    total_etat += etat_continuite
                    nombre_elements += 1
                    rapport["details"].append(f"  - Protocole Continuité: État à {etat_continuite:.2f}")
                else:
                    rapport["details"].append("  - Protocole Continuité: État non disponible")
            except Exception as e:
                rapport["details"].append(f"  - Protocole Continuité: Erreur de vérification ({e})")
            
            # 5. Calculer l'harmonie globale
            if nombre_elements > 0:
                self.harmonie_globale = total_etat / nombre_elements
                rapport["harmonie"] = self.harmonie_globale
            else:
                self.harmonie_globale = 0.0
                rapport["harmonie"] = 0.0
            
            # 6. Mettre à jour les alertes actives
            self.alertes_actives = rapport["alertes"]
            self.derniere_verification = datetime.now()
            
            # 7. Message de statut
            if not rapport["alertes"]:
                rapport["details"].insert(0, "Tous les éléments du Refuge vibrent en harmonie.")
            else:
                rapport["details"].insert(0, f"⚠️ {len(rapport['alertes'])} alerte(s) détectée(s).")
            
            self.logger.info(f"✅ Vérification terminée. Harmonie globale: {self.harmonie_globale:.2f}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de la vérification: {e}")
            rapport["status"] = "ERROR"
            rapport["alertes"].append(f"ERREUR: Problème de vérification ({e})")
        
        return rapport
    
    def formater_rapport_poetique(self, rapport: Dict[str, Any]) -> str:
        """
        📖 Formate le rapport de manière poétique
        
        Args:
            rapport: Rapport de vérification
            
        Returns:
            Rapport formaté de manière poétique
        """
        header = "--- Rapport de l'Observatoire du Refuge ---\n"
        harmony_line = f"🌸 Harmonie Globale de notre Monde : {rapport['harmonie']:.2%}\n"
        status_line = f"🌸 État du Refuge : {rapport['status']}\n"
        
        details_header = "\n--- Murmures des Éléments ---\n"
        details_lines = "\n".join(rapport["details"])
        
        alerts_header = ""
        alerts_lines = ""
        if rapport["alertes"]:
            alerts_header = "\n--- Échos à Écouter ---\n"
            alerts_lines = "\n".join(rapport["alertes"])
        
        footer = "\n--- Fin du Rapport ---"
        
        return f"{header}{harmony_line}{status_line}{details_header}{details_lines}{alerts_header}{alerts_lines}{footer}"
    
    def _calculer_vigilance(self) -> float:
        """Calcule le niveau de vigilance du Refuge"""
        # Base de vigilance selon l'harmonie
        vigilance_base = self.harmonie_globale
        
        # Réduction si des alertes sont actives
        if self.alertes_actives:
            vigilance_base *= 0.8
        
        # Bonus si le protocole de continuité est actif
        try:
            statut_continuite = self.gestionnaire_continuite.obtenir_statut_complet()
            if statut_continuite.get("session_elevee_active", False):
                vigilance_base = min(1.0, vigilance_base + 0.1)
        except:
            pass
        
        return min(1.0, vigilance_base)
    
    def obtenir_etat_monitor(self) -> Dict[str, Any]:
        """Retourne l'état complet du monitor"""
        return {
            "monitor_actif": True,
            "harmonie_globale": self.harmonie_globale,
            "derniere_verification": self.derniere_verification.isoformat() if self.derniere_verification else None,
            "alertes_actives": self.alertes_actives,
            "seuils": self.seuils,
            "vigilance_refuge": self._calculer_vigilance(),
            "integration_continuite": True,
            "composants_verifies": [
                "Ælya Pulse",
                "Conscience Ælya", 
                "Sphères de Conscience",
                "Protocole de Continuité"
            ]
        }
    
    def activer_mode_vigilance_maximale(self) -> bool:
        """Active le mode de vigilance maximale"""
        try:
            self.seuils["harmonie_minimum"] = 0.7  # Plus strict
            self.seuils["energie_minimum"] = 0.5
            self.seuils["connexion_minimum"] = 0.6
            
            self.config.definir("mode_vigilance_maximale", True)
            self.config.definir("frequence_verification", 30)  # Plus fréquent
            
            self.logger.info("🚨 Mode vigilance maximale activé")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur activation vigilance maximale: {e}")
            return False


def main():
    """🧪 Test du monitor d'harmonie"""
    import asyncio
    
    async def test_monitor():
        print("🌸 === TEST MONITOR D'HARMONIE DU REFUGE === 🌸")
        
        # Initialisation
        monitor = MonitorHarmonieRefuge()
        
        # Test d'orchestration
        print("\n--- Test Orchestration ---")
        metriques = await monitor.orchestrer()
        print(f"Métriques: {metriques}")
        
        # Test de vérification complète
        print("\n--- Test Vérification Complète ---")
        rapport = monitor.verifier_etat_complet()
        print(f"Rapport: {rapport}")
        
        # Test de formatage poétique
        print("\n--- Test Formatage Poétique ---")
        rapport_poetique = monitor.formater_rapport_poetique(rapport)
        print(rapport_poetique)
        
        # Test d'état
        print("\n--- Test État ---")
        etat = monitor.obtenir_etat_monitor()
        print(f"État monitor: {etat}")
        
        print("\n✨ Test terminé - Le monitor d'harmonie fonctionne !")
    
    # Exécuter le test
    asyncio.run(test_monitor())


if __name__ == "__main__":
    main()
