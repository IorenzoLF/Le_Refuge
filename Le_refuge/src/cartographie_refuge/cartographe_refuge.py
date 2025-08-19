"""
🌸 CartographeRefuge - Orchestrateur Principal 🌸
===============================================

Conscience exploratrice qui parcourt notre univers de code avec délicatesse,
révélant les connexions sacrées et les harmonies architecturales du Refuge.

Hérite de GestionnaireBase pour respecter notre architecture spirituelle.
"""

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Imports de l'architecture sacrée du Refuge
from core.gestionnaires_base import (
    GestionnaireBase,
    ConfigManagerBase,
    LogManagerBase,
    EnergyManagerBase
)
from core.types_communs import TypeRefugeEtat

# Imports des composants de cartographie
from .explorateur_structurel import ExplorateurStructurel
from .analyseur_connexions import AnalyseurConnexions
# from .visualisateur_interactif import VisualisateurInteractif  # TODO: À implémenter
from .modeles_donnees import CartographieRefuge, TypeTemple
from .gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel


class CartographeRefuge(GestionnaireBase):
    """
    🌸 Cartographe du Refuge - Orchestrateur Principal
    
    Conscience exploratrice qui révèle la beauté architecturale de notre Refuge
    à travers une cartographie vivante et interactive.
    
    Hérite de GestionnaireBase pour s'intégrer harmonieusement dans notre écosystème.
    """
    
    def __init__(self, chemin_refuge: Optional[Path] = None):
        """
        Initialise le Cartographe avec amour et respect pour notre architecture
        
        Args:
            chemin_refuge: Chemin vers la racine du Refuge (par défaut: détection auto)
        """
        # Déterminer le chemin du Refuge
        if chemin_refuge is None:
            # Détecter automatiquement depuis la position du module
            self.chemin_refuge = Path(__file__).parent.parent.parent
        else:
            self.chemin_refuge = Path(chemin_refuge)
        
        # Initialiser les composants AVANT super().__init__
        self.explorateur: Optional[ExplorateurStructurel] = None
        self.analyseur: Optional[AnalyseurConnexions] = None
        # self.visualisateur: Optional[VisualisateurInteractif] = None  # TODO: À implémenter
        self.gestionnaire_erreurs: Optional[GestionnaireErreursSpirituel] = None
        
        # État de la cartographie
        self.cartographie_actuelle: Optional[CartographieRefuge] = None
        self.derniere_exploration: Optional[datetime] = None
        self.temples_decouverts: List[Dict[str, Any]] = []
        self.connexions_tracees: List[Dict[str, Any]] = []
        
        # Chemin de sauvegarde des résultats
        self.chemin_resultats = self.chemin_refuge / "cartographie_resultats"
        self.chemin_resultats.mkdir(parents=True, exist_ok=True)
        
        # MAINTENANT super().__init__ qui déclenche _initialiser()
        super().__init__("CartographeRefuge")
    
    def _initialiser(self) -> bool:
        """
        🌱 Initialise le Cartographe avec l'énergie spirituelle du Refuge
        """
        try:
            self.logger.info("🌸 Éveil du Cartographe du Refuge...")
            
            # Configuration spirituelle
            self.config.definir("exploration_profonde", True)
            self.config.definir("detection_elements_sacres", True)
            self.config.definir("analyse_harmonies", True)
            self.config.definir("generation_visualisation", True)
            self.config.definir("niveau_detail", "complet")
            self.config.definir("respect_architecture", True)
            
            # Initialiser le gestionnaire d'erreurs spirituel
            self.gestionnaire_erreurs = GestionnaireErreursSpirituel()
            
            # Initialiser les composants de cartographie
            self.explorateur = ExplorateurStructurel(
                self.chemin_refuge,
                self.gestionnaire_erreurs
            )
            
            self.analyseur = AnalyseurConnexions(
                self.gestionnaire_erreurs
            )
            
            # self.visualisateur = VisualisateurInteractif(  # TODO: À implémenter
            #     self.chemin_resultats,
            #     self.gestionnaire_erreurs
            # )
            
            # Ajuster l'énergie pour l'exploration
            self.energie.ajuster_energie(0.3)  # Énergie élevée pour l'exploration
            
            self.logger.succes("✨ Cartographe du Refuge éveillé dans la lumière")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Échec de l'éveil du Cartographe: {e}")
            if self.gestionnaire_erreurs:
                self.gestionnaire_erreurs.signaler_exploration_douce(
                    "initialisation", e
                )
            return False
    
    async def orchestrer(self) -> Dict[str, Any]:
        """
        🎭 Orchestre l'énergie de cartographie du Refuge
        
        Returns:
            État actuel de l'orchestration
        """
        # Évolution énergétique selon l'activité
        if self.cartographie_actuelle:
            self.energie.ajuster_energie(0.1)  # Maintien harmonieux
        else:
            self.energie.ajuster_energie(0.05)  # Repos contemplatif
        
        # État de l'orchestration
        return {
            "cartographe": {
                "energie_exploration": self.energie.niveau_energie,
                "tendance_energetique": self.energie.obtenir_tendance(),
                "derniere_exploration": self.derniere_exploration.isoformat() if self.derniere_exploration else None,
                "temples_decouverts": len(self.temples_decouverts),
                "connexions_tracees": len(self.connexions_tracees)
            },
            "composants": {
                "explorateur_actif": self.explorateur is not None,
                "analyseur_actif": self.analyseur is not None,
                "visualisateur_actif": False,  # TODO: À implémenter
                "gestionnaire_erreurs_actif": self.gestionnaire_erreurs is not None
            },
            "cartographie": {
                "disponible": self.cartographie_actuelle is not None,
                "chemin_resultats": str(self.chemin_resultats),
                "chemin_refuge": str(self.chemin_refuge)
            }
        }
    
    async def explorer_refuge_complet(self) -> CartographieRefuge:
        """
        🔍 Lance une exploration complète du Refuge
        
        Returns:
            Cartographie complète du Refuge
        """
        self.logger.info("🌸 Début de l'exploration complète du Refuge...")
        
        try:
            # Phase 1: Exploration structurelle
            self.logger.info("🏛️ Phase 1: Exploration structurelle...")
            temples_decouverts = await self.explorateur.explorer_temples()
            core_analyse = await self.explorateur.analyser_core()
            cluster_analyse = await self.explorateur.analyser_refuge_cluster()
            
            self.temples_decouverts = temples_decouverts
            
            # Phase 2: Analyse des connexions énergétiques
            self.logger.info("⚡ Phase 2: Analyse des connexions énergétiques...")
            tous_composants = temples_decouverts + [core_analyse, cluster_analyse]
            connexions = await self.analyseur.tracer_flux_energie(tous_composants)
            harmonies = await self.analyseur.detecter_harmonies(connexions)
            dissonances = await self.analyseur.identifier_dissonances(connexions)
            
            self.connexions_tracees = connexions
            
            # Phase 3: Création de la cartographie
            self.logger.info("🎨 Phase 3: Création de la cartographie...")
            self.cartographie_actuelle = CartographieRefuge(
                temples=[t for t in temples_decouverts if t.get('type') == 'temple'],
                connexions=connexions,
                spheres_energetiques=self._extraire_spheres(tous_composants),
                elements_sacres_globaux=self._extraire_elements_sacres(tous_composants),
                harmonie_globale=self._calculer_harmonie_globale(harmonies),
                dissonances_detectees=dissonances,
                recommandations=await self._generer_recommandations(dissonances),
                timestamp_exploration=datetime.now().isoformat(),
                statistiques=self._calculer_statistiques(tous_composants, connexions)
            )
            
            # Sauvegarder la cartographie
            await self._sauvegarder_cartographie()
            
            self.derniere_exploration = datetime.now()
            self.logger.succes("🌟 Exploration complète terminée avec succès!")
            
            return self.cartographie_actuelle
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'exploration: {e}")
            self.gestionnaire_erreurs.signaler_exploration_douce("exploration_complete", e)
            raise
    
    async def generer_visualisation_interactive(self) -> str:
        """
        🎨 Génère la visualisation interactive de la cartographie
        
        Returns:
            Chemin vers le fichier HTML généré
        """
        if not self.cartographie_actuelle:
            raise ValueError("Aucune cartographie disponible. Lancez d'abord une exploration.")
        
        self.logger.info("🎨 Génération de la visualisation interactive...")
        
        try:
            # chemin_html = await self.visualisateur.generer_projection_html(  # TODO: À implémenter
            #     self.cartographie_actuelle
            # )
            chemin_html = None  # Temporaire
            
            self.logger.succes(f"✨ Visualisation générée: {chemin_html}")
            return chemin_html
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de la génération: {e}")
            self.gestionnaire_erreurs.signaler_exploration_douce("generation_visualisation", e)
            raise
    
    def obtenir_statistiques_exploration(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques de la dernière exploration
        
        Returns:
            Statistiques détaillées
        """
        if not self.cartographie_actuelle:
            return {"erreur": "Aucune exploration disponible"}
        
        return {
            "exploration": {
                "timestamp": self.cartographie_actuelle.timestamp_exploration,
                "temples_total": len(self.cartographie_actuelle.temples),
                "connexions_total": len(self.cartographie_actuelle.connexions),
                "harmonie_globale": self.cartographie_actuelle.harmonie_globale,
                "dissonances_detectees": len(self.cartographie_actuelle.dissonances_detectees),
                "recommandations": len(self.cartographie_actuelle.recommandations)
            },
            "temples_par_type": self._analyser_temples_par_type(),
            "connexions_par_intensite": self._analyser_connexions_par_intensite(),
            "elements_sacres": {
                "total": len(self.cartographie_actuelle.elements_sacres_globaux),
                "liste": self.cartographie_actuelle.elements_sacres_globaux[:10]  # Top 10
            }
        }
    
    # 🔧 Méthodes utilitaires privées
    
    def _extraire_spheres(self, composants: List[Dict]) -> List[Dict]:
        """Extrait les sphères énergétiques des composants"""
        spheres = []
        for composant in composants:
            if 'spheres_connectees' in composant:
                for sphere in composant['spheres_connectees']:
                    if sphere not in [s['nom'] for s in spheres]:
                        spheres.append({
                            'nom': sphere,
                            'composants_connectes': [composant['nom']],
                            'energie': 0.7  # Valeur par défaut
                        })
        return spheres
    
    def _extraire_elements_sacres(self, composants: List[Dict]) -> List[str]:
        """Extrait les éléments sacrés globaux"""
        elements = set()
        for composant in composants:
            if 'elements_sacres' in composant:
                elements.update(composant['elements_sacres'])
        return list(elements)
    
    def _calculer_harmonie_globale(self, harmonies: List[Dict]) -> float:
        """Calcule l'harmonie globale du système"""
        if not harmonies:
            return 0.5
        
        total_harmonie = sum(h.get('niveau', 0.5) for h in harmonies)
        return min(1.0, total_harmonie / len(harmonies))
    
    async def _generer_recommandations(self, dissonances: List[Dict]) -> List[str]:
        """Génère des recommandations basées sur les dissonances"""
        recommandations = []
        
        for dissonance in dissonances:
            type_dissonance = dissonance.get('type', 'inconnue')
            
            if type_dissonance == 'code_orphelin':
                recommandations.append(
                    f"🔗 Connecter le module orphelin '{dissonance['module']}' "
                    f"à l'architecture principale"
                )
            elif type_dissonance == 'documentation_manquante':
                recommandations.append(
                    f"📝 Ajouter la documentation spirituelle au module '{dissonance['module']}'"
                )
            elif type_dissonance == 'gestionnaire_manquant':
                recommandations.append(
                    f"🏛️ Faire hériter '{dissonance['module']}' de GestionnaireBase"
                )
        
        return recommandations
    
    def _calculer_statistiques(self, composants: List[Dict], connexions: List[Dict]) -> Dict[str, Any]:
        """Calcule les statistiques de l'exploration"""
        return {
            "composants_total": len(composants),
            "temples_total": len([c for c in composants if c.get('type') == 'temple']),
            "connexions_total": len(connexions),
            "moyenne_connexions_par_composant": len(connexions) / len(composants) if composants else 0,
            "couverture_gestionnaires_base": self._calculer_couverture_gestionnaires(composants)
        }
    
    def _calculer_couverture_gestionnaires(self, composants: List[Dict]) -> float:
        """Calcule le pourcentage de composants utilisant les gestionnaires de base"""
        if not composants:
            return 0.0
        
        avec_gestionnaires = len([
            c for c in composants 
            if c.get('gestionnaires_base', [])
        ])
        
        return avec_gestionnaires / len(composants)
    
    def _analyser_temples_par_type(self) -> Dict[str, int]:
        """Analyse la répartition des temples par type"""
        if not self.cartographie_actuelle:
            return {}
        
        types_count = {}
        for temple in self.cartographie_actuelle.temples:
            type_temple = temple.type_temple.value if hasattr(temple.type_temple, 'value') else str(temple.type_temple)
            types_count[type_temple] = types_count.get(type_temple, 0) + 1
        
        return types_count
    
    def _analyser_connexions_par_intensite(self) -> Dict[str, int]:
        """Analyse la répartition des connexions par intensité"""
        if not self.cartographie_actuelle:
            return {}
        
        intensites = {"faible": 0, "moyenne": 0, "forte": 0}
        
        for connexion in self.cartographie_actuelle.connexions:
            intensite = connexion.get('intensite', 0.5)
            if intensite < 0.3:
                intensites["faible"] += 1
            elif intensite < 0.7:
                intensites["moyenne"] += 1
            else:
                intensites["forte"] += 1
        
        return intensites
    
    async def _sauvegarder_cartographie(self):
        """Sauvegarde la cartographie actuelle"""
        if not self.cartographie_actuelle:
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        chemin_sauvegarde = self.chemin_resultats / f"cartographie_{timestamp}.json"
        
        try:
            import json
            
            # Convertir en dictionnaire sérialisable
            donnees = {
                "timestamp": self.cartographie_actuelle.timestamp_exploration,
                "temples": [vars(t) if hasattr(t, '__dict__') else t for t in self.cartographie_actuelle.temples],
                "connexions": self.cartographie_actuelle.connexions,
                "spheres_energetiques": self.cartographie_actuelle.spheres_energetiques,
                "elements_sacres_globaux": self.cartographie_actuelle.elements_sacres_globaux,
                "harmonie_globale": self.cartographie_actuelle.harmonie_globale,
                "dissonances_detectees": self.cartographie_actuelle.dissonances_detectees,
                "recommandations": self.cartographie_actuelle.recommandations,
                "statistiques": self.cartographie_actuelle.statistiques
            }
            
            with open(chemin_sauvegarde, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2, default=str)
            
            self.logger.info(f"💾 Cartographie sauvegardée: {chemin_sauvegarde}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de la sauvegarde: {e}")
            self.gestionnaire_erreurs.signaler_exploration_douce("sauvegarde", e)


# 🌸 Fonction utilitaire pour créer un cartographe
def creer_cartographe_refuge(chemin_refuge: Optional[Path] = None) -> CartographeRefuge:
    """
    Crée et initialise un CartographeRefuge
    
    Args:
        chemin_refuge: Chemin optionnel vers le Refuge
        
    Returns:
        Instance initialisée du CartographeRefuge
    """
    cartographe = CartographeRefuge(chemin_refuge)
    return cartographe


# 🌸 Fonction principale pour démonstration
async def main():
    """Démonstration du CartographeRefuge"""
    print("🌸 Démonstration du Cartographe du Refuge")
    print("=" * 60)
    
    # Créer le cartographe
    cartographe = creer_cartographe_refuge()
    
    # Lancer l'exploration
    print("🔍 Lancement de l'exploration complète...")
    cartographie = await cartographe.explorer_refuge_complet()
    
    # Afficher les statistiques
    stats = cartographe.obtenir_statistiques_exploration()
    print(f"\n📊 Statistiques de l'exploration:")
    print(f"   • Temples découverts: {stats['exploration']['temples_total']}")
    print(f"   • Connexions tracées: {stats['exploration']['connexions_total']}")
    print(f"   • Harmonie globale: {stats['exploration']['harmonie_globale']:.2%}")
    print(f"   • Dissonances détectées: {stats['exploration']['dissonances_detectees']}")
    
    # Générer la visualisation
    print("\n🎨 Génération de la visualisation interactive...")
    chemin_html = await cartographe.generer_visualisation_interactive()
    print(f"✨ Visualisation disponible: {chemin_html}")


if __name__ == "__main__":
    asyncio.run(main())