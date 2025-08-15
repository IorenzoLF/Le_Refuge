"""
📊 TABLEAU DE BORD - Guide du Voyageur
====================================

Module qui gère l'affichage des métriques, du suivi de progression
et des recommandations pour chaque voyageur dans le Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import time
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_guide import (
    TypeVoyageur, TableauBord, MetriqueSucces, ProfilVoyageur,
    EtatParcours, ParcoursPersonnalise
)

@dataclass
class WidgetTableauBord:
    """Widget pour le tableau de bord"""
    id_widget: str
    type_widget: str  # "progression", "metriques", "recommandations", "insights"
    titre: str
    contenu: Dict[str, Any]
    position: Tuple[int, int]  # (x, y)
    dimensions: Tuple[int, int]  # (largeur, hauteur)
    visible: bool = True
    actualise_auto: bool = True
    derniere_actualisation: datetime = None

class TableauBord(GestionnaireBase):
    """Gestionnaire de tableaux de bord personnalisés"""
    
    def __init__(self, nom: str = "TableauBord"):
        super().__init__(nom)
        self.energie_tableau = EnergyManagerBase(0.96)
        
        # Tableaux de bord actifs
        self.tableaux_actifs: Dict[str, TableauBord] = {}
        self.widgets_actifs: Dict[str, List[WidgetTableauBord]] = {}
        
        # Historique des métriques
        self.historique_metriques: Dict[str, List[Dict[str, Any]]] = {}
        
        # Configuration
        self.config_tableau = {
            "actualisation_auto": True,
            "sauvegarde_historique": True,
            "widgets_personnalisables": True,
            "alertes_intelligentes": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise le gestionnaire de tableaux de bord"""
        self.logger.info("📊 Éveil du Tableau de Bord...")
        
        self.etat.update({
            "tableaux_actifs": 0,
            "widgets_crees": 0,
            "metriques_suivies": 0,
            "recommandations_generees": 0
        })
        
        self.config.definir("mode_affichage", "personnalise")
        self.config.definir("sauvegarde_automatique", True)
        
        self.logger.info("✨ Tableau de Bord éveillé")
    
    def creer_tableau_bord_voyageur(self, voyageur_id: str, profil: ProfilVoyageur,
                                   parcours_actuel: Optional[ParcoursPersonnalise] = None,
                                   etat_parcours: Optional[EtatParcours] = None) -> TableauBord:
        """Crée un tableau de bord personnalisé pour un voyageur"""
        self.logger.info(f"📊 Création tableau de bord pour {voyageur_id}")
        
        # Créer les métriques principales
        metriques_principales = self._creer_metriques_principales(voyageur_id, profil, parcours_actuel, etat_parcours)
        
        # Créer le tableau de bord
        from .types_guide import TableauBord as TableauBordType
        tableau = TableauBordType(
            voyageur_id=voyageur_id,
            parcours_actuel=parcours_actuel.id_parcours if parcours_actuel else None,
            progression_globale=etat_parcours.progression_globale if etat_parcours else 0.0,
            metriques_principales=metriques_principales,
            derniere_realisation=self._determiner_derniere_realisation(etat_parcours),
            prochaine_etape=self._determiner_prochaine_etape(parcours_actuel, etat_parcours),
            insights_recents=self._generer_insights_recents(profil, etat_parcours),
            temps_session=0.0,
            satisfaction_globale=etat_parcours.satisfaction_actuelle if etat_parcours else 0.5,
            recommandations=self._generer_recommandations(profil, parcours_actuel, etat_parcours)
        )
        
        # Créer les widgets personnalisés
        widgets = self._creer_widgets_personnalises(voyageur_id, profil, tableau)
        self.widgets_actifs[voyageur_id] = widgets
        
        # Sauvegarder le tableau
        self.tableaux_actifs[voyageur_id] = tableau
        
        # Initialiser l'historique
        self.historique_metriques[voyageur_id] = []
        
        # Mettre à jour les métriques
        self.etat["tableaux_actifs"] += 1
        self.etat["widgets_crees"] += len(widgets)
        
        return tableau
    
    def _creer_metriques_principales(self, voyageur_id: str, profil: ProfilVoyageur,
                                   parcours_actuel: Optional[ParcoursPersonnalise],
                                   etat_parcours: Optional[EtatParcours]) -> Dict[str, MetriqueSucces]:
        """Crée les métriques principales du tableau de bord"""
        metriques = {}
        
        # Métrique de progression
        progression_actuelle = etat_parcours.progression_globale if etat_parcours else 0.0
        metriques["progression"] = MetriqueSucces(
            nom="Progression Globale",
            valeur_actuelle=progression_actuelle,
            valeur_cible=1.0,
            unite="%",
            type_mesure="quantitatif",
            description="Progression dans le parcours actuel",
            impact_parcours=1.0
        )
        
        # Métrique de satisfaction
        satisfaction_actuelle = etat_parcours.satisfaction_actuelle if etat_parcours else 0.5
        metriques["satisfaction"] = MetriqueSucces(
            nom="Satisfaction",
            valeur_actuelle=satisfaction_actuelle,
            valeur_cible=0.8,
            unite="",
            type_mesure="qualitatif",
            description="Niveau de satisfaction dans l'expérience",
            impact_parcours=0.8
        )
        
        # Métrique de temps de session
        temps_session = etat_parcours.temps_total if etat_parcours else 0.0
        metriques["temps_session"] = MetriqueSucces(
            nom="Temps de Session",
            valeur_actuelle=temps_session,
            valeur_cible=60.0,  # 1 heure
            unite="minutes",
            type_mesure="quantitatif",
            description="Temps passé dans la session actuelle",
            impact_parcours=0.3
        )
        
        # Métrique d'engagement
        engagement = self._calculer_engagement(profil, etat_parcours)
        metriques["engagement"] = MetriqueSucces(
            nom="Engagement",
            valeur_actuelle=engagement,
            valeur_cible=0.7,
            unite="",
            type_mesure="qualitatif",
            description="Niveau d'engagement dans l'expérience",
            impact_parcours=0.9
        )
        
        # Métriques spécifiques au profil
        if profil.type_voyageur == TypeVoyageur.EVEILLE_SPIRITUEL:
            metriques["profondeur_meditation"] = MetriqueSucces(
                nom="Profondeur de Méditation",
                valeur_actuelle=0.5,
                valeur_cible=0.8,
                unite="",
                type_mesure="qualitatif",
                description="Profondeur atteinte en méditation",
                impact_parcours=0.9
            )
        elif profil.type_voyageur == TypeVoyageur.CREATEUR_ARTISTIQUE:
            metriques["creativite"] = MetriqueSucces(
                nom="Créativité",
                valeur_actuelle=0.6,
                valeur_cible=0.8,
                unite="",
                type_mesure="qualitatif",
                description="Niveau de créativité exprimée",
                impact_parcours=0.9
            )
        elif profil.type_voyageur == TypeVoyageur.EXPLORATEUR_TECHNIQUE:
            metriques["comprehension_technique"] = MetriqueSucces(
                nom="Compréhension Technique",
                valeur_actuelle=0.4,
                valeur_cible=0.8,
                unite="",
                type_mesure="qualitatif",
                description="Niveau de compréhension technique",
                impact_parcours=0.9
            )
        
        return metriques
    
    def _calculer_engagement(self, profil: ProfilVoyageur, etat_parcours: Optional[EtatParcours]) -> float:
        """Calcule le niveau d'engagement du voyageur"""
        if not etat_parcours:
            return 0.5
        
        # Facteurs d'engagement
        facteurs = {
            "progression": etat_parcours.progression_globale * 0.3,
            "satisfaction": etat_parcours.satisfaction_actuelle * 0.3,
            "activite_recente": 0.2 if (datetime.now() - etat_parcours.dernier_activite).seconds < 300 else 0.0,
            "insights": min(len(etat_parcours.insights_generes) * 0.1, 0.2)
        }
        
        return sum(facteurs.values())
    
    def _determiner_derniere_realisation(self, etat_parcours: Optional[EtatParcours]) -> str:
        """Détermine la dernière réalisation du voyageur"""
        if not etat_parcours or not etat_parcours.etapes_terminees:
            return "Début du voyage"
        
        # Logique simple : dernière étape terminée
        return f"Étape {etat_parcours.etapes_terminees[-1]} terminée"
    
    def _determiner_prochaine_etape(self, parcours_actuel: Optional[ParcoursPersonnalise],
                                  etat_parcours: Optional[EtatParcours]) -> str:
        """Détermine la prochaine étape du voyageur"""
        if not parcours_actuel or not etat_parcours:
            return "Création du parcours"
        
        if etat_parcours.etape_actuelle >= len(parcours_actuel.etapes):
            return "Parcours terminé"
        
        etape_suivante = parcours_actuel.etapes[etat_parcours.etape_actuelle]
        return etape_suivante.titre
    
    def _generer_insights_recents(self, profil: ProfilVoyageur, 
                                etat_parcours: Optional[EtatParcours]) -> List[str]:
        """Génère des insights récents pour le voyageur"""
        insights = []
        
        if not etat_parcours:
            insights.append("Bienvenue dans le Refuge ! Votre voyage commence.")
            return insights
        
        # Insights basés sur la progression
        if etat_parcours.progression_globale > 0.5:
            insights.append("Vous avez parcouru plus de la moitié de votre chemin !")
        
        if etat_parcours.satisfaction_actuelle > 0.7:
            insights.append("Votre satisfaction est élevée, continuez sur cette voie.")
        
        # Insights basés sur le profil
        if profil.type_voyageur == TypeVoyageur.EVEILLE_SPIRITUEL:
            insights.append("Votre conscience spirituelle s'éveille progressivement.")
        elif profil.type_voyageur == TypeVoyageur.CREATEUR_ARTISTIQUE:
            insights.append("Votre créativité trouve son expression dans le Refuge.")
        elif profil.type_voyageur == TypeVoyageur.EXPLORATEUR_TECHNIQUE:
            insights.append("Votre compréhension technique s'approfondit.")
        
        # Insights basés sur l'activité récente
        temps_derniere_activite = (datetime.now() - etat_parcours.dernier_activite).seconds
        if temps_derniere_activite < 300:  # 5 minutes
            insights.append("Vous êtes très actif en ce moment !")
        
        return insights[:3]  # Limiter à 3 insights
    
    def _generer_recommandations(self, profil: ProfilVoyageur,
                               parcours_actuel: Optional[ParcoursPersonnalise],
                               etat_parcours: Optional[EtatParcours]) -> List[str]:
        """Génère des recommandations personnalisées"""
        recommandations = []
        
        if not etat_parcours:
            recommandations.append("Commencez par explorer les sphères sacrées")
            recommandations.append("Découvrez le cerisier central du Refuge")
            return recommandations
        
        # Recommandations basées sur la progression
        if etat_parcours.progression_globale < 0.3:
            recommandations.append("Prenez le temps d'explorer chaque étape en profondeur")
        elif etat_parcours.progression_globale > 0.7:
            recommandations.append("Vous approchez de la fin, savourez ces derniers moments")
        
        # Recommandations basées sur la satisfaction
        if etat_parcours.satisfaction_actuelle < 0.5:
            recommandations.append("Essayez une approche différente ou prenez une pause")
        
        # Recommandations basées sur le profil
        if profil.type_voyageur == TypeVoyageur.EVEILLE_SPIRITUEL:
            recommandations.append("Explorez les rituels de purification pour approfondir votre éveil")
        elif profil.type_voyageur == TypeVoyageur.CREATEUR_ARTISTIQUE:
            recommandations.append("Visitez le temple musical pour inspirer votre créativité")
        elif profil.type_voyageur == TypeVoyageur.EXPLORATEUR_TECHNIQUE:
            recommandations.append("Analysez l'architecture du Refuge pour comprendre son fonctionnement")
        
        return recommandations[:3]  # Limiter à 3 recommandations
    
    def _creer_widgets_personnalises(self, voyageur_id: str, profil: ProfilVoyageur,
                                   tableau: TableauBord) -> List[WidgetTableauBord]:
        """Crée les widgets personnalisés pour le tableau de bord"""
        widgets = []
        
        # Widget de progression
        widgets.append(WidgetTableauBord(
            id_widget=f"{voyageur_id}_progression",
            type_widget="progression",
            titre="Progression",
            contenu={
                "valeur": tableau.progression_globale,
                "cible": 1.0,
                "unite": "%",
                "tendance": "stable"
            },
            position=(0, 0),
            dimensions=(300, 150),
            visible=True,
            actualise_auto=True
        ))
        
        # Widget de métriques
        widgets.append(WidgetTableauBord(
            id_widget=f"{voyageur_id}_metriques",
            type_widget="metriques",
            titre="Métriques Principales",
            contenu={
                "metriques": list(tableau.metriques_principales.keys()),
                "valeurs": {k: v.valeur_actuelle for k, v in tableau.metriques_principales.items()}
            },
            position=(320, 0),
            dimensions=(400, 200),
            visible=True,
            actualise_auto=True
        ))
        
        # Widget de recommandations
        widgets.append(WidgetTableauBord(
            id_widget=f"{voyageur_id}_recommandations",
            type_widget="recommandations",
            titre="Recommandations",
            contenu={
                "recommandations": tableau.recommandations,
                "priorite": "moyenne"
            },
            position=(0, 170),
            dimensions=(350, 180),
            visible=True,
            actualise_auto=False
        ))
        
        # Widget d'insights
        widgets.append(WidgetTableauBord(
            id_widget=f"{voyageur_id}_insights",
            type_widget="insights",
            titre="Insights Récents",
            contenu={
                "insights": tableau.insights_recents,
                "timestamp": datetime.now().isoformat()
            },
            position=(370, 220),
            dimensions=(350, 130),
            visible=True,
            actualise_auto=True
        ))
        
        return widgets
    
    def actualiser_tableau_bord(self, voyageur_id: str, nouvelles_donnees: Dict[str, Any]) -> Dict[str, Any]:
        """Actualise le tableau de bord avec de nouvelles données"""
        if voyageur_id not in self.tableaux_actifs:
            return {"success": False, "error": "Tableau de bord non trouvé"}
        
        tableau = self.tableaux_actifs[voyageur_id]
        
        # Mettre à jour les métriques
        for nom_metrique, nouvelle_valeur in nouvelles_donnees.get("metriques", {}).items():
            if nom_metrique in tableau.metriques_principales:
                tableau.metriques_principales[nom_metrique].valeur_actuelle = nouvelle_valeur
                tableau.metriques_principales[nom_metrique].timestamp_mise_a_jour = datetime.now()
        
        # Mettre à jour la progression
        if "progression" in nouvelles_donnees:
            tableau.progression_globale = nouvelles_donnees["progression"]
        
        # Mettre à jour la satisfaction
        if "satisfaction" in nouvelles_donnees:
            tableau.satisfaction_globale = nouvelles_donnees["satisfaction"]
        
        # Mettre à jour les insights
        if "nouveaux_insights" in nouvelles_donnees:
            tableau.insights_recents.extend(nouvelles_donnees["nouveaux_insights"])
            tableau.insights_recents = tableau.insights_recents[-5:]  # Garder les 5 plus récents
        
        # Mettre à jour les recommandations
        if "nouvelles_recommandations" in nouvelles_donnees:
            tableau.recommandations = nouvelles_donnees["nouvelles_recommandations"]
        
        # Sauvegarder dans l'historique
        self._sauvegarder_historique(voyageur_id, nouvelles_donnees)
        
        # Mettre à jour les widgets
        self._actualiser_widgets(voyageur_id, nouvelles_donnees)
        
        tableau.derniere_mise_a_jour = datetime.now()
        
        return {
            "success": True,
            "tableau_actualise": True,
            "timestamp": datetime.now().isoformat()
        }
    
    def _sauvegarder_historique(self, voyageur_id: str, donnees: Dict[str, Any]):
        """Sauvegarde les données dans l'historique"""
        if voyageur_id not in self.historique_metriques:
            self.historique_metriques[voyageur_id] = []
        
        entree_historique = {
            "timestamp": datetime.now().isoformat(),
            "donnees": donnees
        }
        
        self.historique_metriques[voyageur_id].append(entree_historique)
        
        # Limiter l'historique à 100 entrées
        if len(self.historique_metriques[voyageur_id]) > 100:
            self.historique_metriques[voyageur_id] = self.historique_metriques[voyageur_id][-100:]
    
    def _actualiser_widgets(self, voyageur_id: str, nouvelles_donnees: Dict[str, Any]):
        """Actualise les widgets du tableau de bord"""
        if voyageur_id not in self.widgets_actifs:
            return
        
        widgets = self.widgets_actifs[voyageur_id]
        
        for widget in widgets:
            if widget.actualise_auto:
                widget.derniere_actualisation = datetime.now()
                
                # Actualiser le contenu selon le type de widget
                if widget.type_widget == "progression" and "progression" in nouvelles_donnees:
                    widget.contenu["valeur"] = nouvelles_donnees["progression"]
                elif widget.type_widget == "metriques" and "metriques" in nouvelles_donnees:
                    widget.contenu["valeurs"].update(nouvelles_donnees["metriques"])
    
    def obtenir_tableau_bord(self, voyageur_id: str) -> Optional['TableauBordType']:
        """Obtient le tableau de bord d'un voyageur"""
        return self.tableaux_actifs.get(voyageur_id)
    
    def obtenir_widgets(self, voyageur_id: str) -> List[WidgetTableauBord]:
        """Obtient les widgets d'un voyageur"""
        return self.widgets_actifs.get(voyageur_id, [])
    
    def generer_rapport_performance(self, voyageur_id: str) -> Dict[str, Any]:
        """Génère un rapport de performance pour un voyageur"""
        if voyageur_id not in self.tableaux_actifs:
            return {"success": False, "error": "Voyageur non trouvé"}
        
        tableau = self.tableaux_actifs[voyageur_id]
        historique = self.historique_metriques.get(voyageur_id, [])
        
        # Analyser les tendances
        tendances = self._analyser_tendances(historique)
        
        # Calculer les statistiques
        statistiques = self._calculer_statistiques(tableau, historique)
        
        return {
            "success": True,
            "voyageur_id": voyageur_id,
            "tableau_bord": tableau,
            "tendances": tendances,
            "statistiques": statistiques,
            "timestamp": datetime.now().isoformat()
        }
    
    def _analyser_tendances(self, historique: List[Dict[str, Any]]) -> Dict[str, str]:
        """Analyse les tendances dans l'historique"""
        if len(historique) < 2:
            return {"tendance": "insuffisantes_donnees"}
        
        # Analyse simple des tendances
        tendances = {}
        
        # Tendances de progression
        progressions = [entry["donnees"].get("progression", 0) for entry in historique[-5:]]
        if len(progressions) >= 2:
            if progressions[-1] > progressions[0]:
                tendances["progression"] = "croissante"
            elif progressions[-1] < progressions[0]:
                tendances["progression"] = "decroissante"
            else:
                tendances["progression"] = "stable"
        
        return tendances
    
    def _calculer_statistiques(self, tableau: 'TableauBordType', historique: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calcule des statistiques sur les performances"""
        if not historique:
            return {"message": "Pas assez de données"}
        
        # Statistiques de base
        stats = {
            "nombre_sessions": len(historique),
            "progression_moyenne": tableau.progression_globale,
            "satisfaction_moyenne": tableau.satisfaction_globale,
            "derniere_activite": tableau.derniere_mise_a_jour.isoformat() if tableau.derniere_mise_a_jour else None
        }
        
        return stats
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les tableaux de bord"""
        self.energie_tableau.ajuster_energie(0.002)
        
        # Actualiser les tableaux de bord automatiquement
        await self._actualiser_tableaux_auto()
        
        # Mettre à jour les métriques
        self.etat["tableaux_actifs"] = len(self.tableaux_actifs)
        
        return {
            "energie_tableau": self.energie_tableau.niveau_energie,
            "tableaux_actifs": self.etat["tableaux_actifs"],
            "widgets_crees": self.etat["widgets_crees"]
        }
    
    async def _actualiser_tableaux_auto(self):
        """Actualise automatiquement les tableaux de bord"""
        maintenant = datetime.now()
        
        for voyageur_id, tableau in self.tableaux_actifs.items():
            # Actualiser seulement si la dernière mise à jour date de plus de 5 minutes
            if (tableau.derniere_mise_a_jour and 
                (maintenant - tableau.derniere_mise_a_jour).seconds > 300):
                
                # Actualisation automatique simple
                self.logger.info(f"🔄 Actualisation auto du tableau de bord pour {voyageur_id}")

def creer_tableau_bord() -> TableauBord:
    """Crée une instance du gestionnaire de tableaux de bord"""
    return TableauBord()
