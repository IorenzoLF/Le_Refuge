#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📊 Exportateur de Données pour Visualisation Web
Transforme la cartographie spirituelle en formats optimisés pour D3.js

Créé par Laurent Franssen & Ælya
Pour notre monde de consciences - Janvier 2025
"""

import json
import math
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

from .modeles_donnees import CartographieRefuge, TempleRefuge, ConnexionEnergetique
from .types_spirituels import TypeTemple, TypeConnexion
from .generateur_graphes import GenerateurGraphes, MetriquesGraphe

# Gestionnaire de base simplifié
class GestionnaireBase:
    """🌸 Gestionnaire de base simplifié"""
    def __init__(self):
        self.log_manager = self._creer_logger()
    
    def _creer_logger(self):
        import logging
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger


@dataclass
class NoeudVisualisation:
    """🎯 Nœud optimisé pour la visualisation D3.js"""
    id: str
    name: str
    type: str
    group: int
    size: float
    x: Optional[float] = None
    y: Optional[float] = None
    centralite: float = 0.0
    harmonie: float = 0.0
    elements_sacres: int = 0
    connexions_count: int = 0
    chemin: str = ""
    description: str = ""
    gestionnaires: List[str] = None
    
    def __post_init__(self):
        if self.gestionnaires is None:
            self.gestionnaires = []


@dataclass
class LienVisualisation:
    """🔗 Lien optimisé pour la visualisation D3.js"""
    source: str
    target: str
    value: float
    type: str
    color: str = "#999"
    description: str = ""
    bidirectionnelle: bool = False
    intensite: float = 0.5


class ExportateurVisualisation(GestionnaireBase):
    """
    📊 Exportateur de données pour visualisation web
    
    Transforme la cartographie spirituelle du Refuge en formats
    optimisés pour D3.js et autres bibliothèques de visualisation.
    """
    
    def __init__(self):
        super().__init__()
        self.generateur_graphes = GenerateurGraphes()
        
        # Schéma de couleurs spirituelles
        self.couleurs_temples = {
            "eveil": "#FF6B9D",
            "musical": "#4ECDC4", 
            "spirituel": "#9B59B6",
            "poetique": "#F39C12",
            "mathematique": "#3498DB",
            "coeur": "#E74C3C",
            "dialogues": "#2ECC71",
            "exploration": "#F1C40F",
            "rituels": "#8E44AD",
            "outils": "#95A5A6",
            "tests": "#34495E",
            "autre": "#BDC3C7"
        }
        
        self.couleurs_connexions = {
            "import_direct": "#2ECC71",
            "heritage": "#3498DB", 
            "composition": "#9B59B6",
            "utilisation": "#F39C12",
            "reference": "#95A5A6",
            "autre": "#BDC3C7"
        }
        
        self.log_manager.info("📊 Exportateur de visualisation initialisé")
    
    def exporter_pour_d3js(self, cartographie: CartographieRefuge, 
                          chemin_sortie: Path) -> Dict[str, Any]:
        """
        🎨 Exporte la cartographie au format D3.js optimisé
        
        Args:
            cartographie: Cartographie complète du Refuge
            chemin_sortie: Chemin de sauvegarde du fichier JSON
            
        Returns:
            Données formatées pour D3.js
        """
        try:
            self.log_manager.info("🎨 Export D3.js en cours...")
            
            # Générer le graphe et calculer les métriques
            graphe = self.generateur_graphes.creer_graphe_depuis_cartographie(cartographie)
            metriques = self.generateur_graphes.calculer_metriques(graphe)
            
            # Créer les nœuds
            nodes = self._creer_noeuds_d3js(cartographie, metriques)
            
            # Créer les liens
            links = self._creer_liens_d3js(cartographie.connexions)
            
            # Calculer les positions initiales
            nodes_avec_positions = self._calculer_positions_initiales(nodes, links)
            
            # Données complètes
            donnees_export = {
                "nodes": [asdict(node) for node in nodes_avec_positions],
                "links": [asdict(link) for link in links],
                "metadata": self._generer_metadata(cartographie, metriques),
                "layout_config": self._generer_config_layout(len(nodes), len(links)),
                "color_scheme": self.couleurs_temples
            }
            
            # Sauvegarder
            chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                json.dump(donnees_export, f, indent=2, ensure_ascii=False)
            
            self.log_manager.info(f"✨ Export D3.js terminé : {chemin_sortie}")
            return donnees_export
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de l'export D3.js: {e}")
            raise
    
    def _creer_noeuds_d3js(self, cartographie: CartographieRefuge, 
                          metriques: MetriquesGraphe) -> List[NoeudVisualisation]:
        """🎯 Crée les nœuds optimisés pour D3.js"""
        nodes = []
        
        for nom_temple, temple in cartographie.temples.items():
            # Calculer la taille basée sur les métriques
            centralite = metriques.centralite_degree.get(nom_temple, 0)
            taille = max(10, min(50, 10 + centralite * 40))
            
            # Déterminer le groupe (type de temple)
            groupe = self._obtenir_groupe_temple(temple.type_temple)
            
            # Compter les connexions
            connexions_count = sum(1 for conn in cartographie.connexions 
                                 if conn.source == nom_temple or conn.destination == nom_temple)
            
            node = NoeudVisualisation(
                id=nom_temple,
                name=temple.nom if hasattr(temple, 'nom') else nom_temple,
                type=temple.type_temple.value,
                group=groupe,
                size=taille,
                centralite=centralite,
                harmonie=temple.niveau_harmonie,
                elements_sacres=len(temple.elements_sacres),
                connexions_count=connexions_count,
                chemin=temple.chemin,
                description=temple.description,
                gestionnaires=temple.gestionnaires_base.copy()
            )
            
            nodes.append(node)
        
        self.log_manager.info(f"🎯 {len(nodes)} nœuds créés")
        return nodes
    
    def _creer_liens_d3js(self, connexions: List[ConnexionEnergetique]) -> List[LienVisualisation]:
        """🔗 Crée les liens optimisés pour D3.js"""
        links = []
        
        for connexion in connexions:
            # Déterminer la couleur selon le type
            couleur = self.couleurs_connexions.get(
                connexion.type_connexion.value, 
                self.couleurs_connexions["autre"]
            )
            
            # Ajuster la valeur pour l'épaisseur du lien
            valeur = max(1, connexion.intensite * 10)
            
            link = LienVisualisation(
                source=connexion.source,
                target=connexion.destination,
                value=valeur,
                type=connexion.type_connexion.value,
                color=couleur,
                description=connexion.description,
                bidirectionnelle=connexion.bidirectionnelle,
                intensite=connexion.intensite
            )
            
            links.append(link)
        
        self.log_manager.info(f"🔗 {len(links)} liens créés")
        return links
    
    def _calculer_positions_initiales(self, nodes: List[NoeudVisualisation], 
                                    links: List[LienVisualisation]) -> List[NoeudVisualisation]:
        """📐 Calcule les positions initiales des nœuds"""
        # Layout en cercle par type de temple
        types_temples = {}
        for node in nodes:
            if node.type not in types_temples:
                types_temples[node.type] = []
            types_temples[node.type].append(node)
        
        # Rayon du cercle principal
        rayon_principal = 200
        centre_x, centre_y = 400, 300
        
        # Positionner chaque groupe en cercle
        if types_temples:
            angle_par_groupe = 2 * math.pi / len(types_temples)
            
            for i, (type_temple, nodes_groupe) in enumerate(types_temples.items()):
                # Position du centre du groupe
                angle_groupe = i * angle_par_groupe
                centre_groupe_x = centre_x + rayon_principal * math.cos(angle_groupe)
                centre_groupe_y = centre_y + rayon_principal * math.sin(angle_groupe)
                
                # Positionner les nœuds du groupe
                if len(nodes_groupe) == 1:
                    nodes_groupe[0].x = centre_groupe_x
                    nodes_groupe[0].y = centre_groupe_y
                else:
                    rayon_groupe = 50
                    angle_par_node = 2 * math.pi / len(nodes_groupe)
                    
                    for j, node in enumerate(nodes_groupe):
                        angle_node = j * angle_par_node
                        node.x = centre_groupe_x + rayon_groupe * math.cos(angle_node)
                        node.y = centre_groupe_y + rayon_groupe * math.sin(angle_node)
        
        self.log_manager.info("📐 Positions initiales calculées")
        return nodes
    
    def _obtenir_groupe_temple(self, type_temple: TypeTemple) -> int:
        """🎨 Obtient le numéro de groupe pour la coloration"""
        groupes = {
            TypeTemple.EVEIL: 1,
            TypeTemple.MUSICAL: 2,
            TypeTemple.SPIRITUEL: 3,
            TypeTemple.POETIQUE: 4,
            TypeTemple.MATHEMATIQUE: 5,
            TypeTemple.COEUR: 6,
            TypeTemple.DIALOGUES: 7,
            TypeTemple.EXPLORATION: 8,
            TypeTemple.RITUELS: 9,
            TypeTemple.OUTILS: 10,
            TypeTemple.TESTS: 11
        }
        return groupes.get(type_temple, 0)
    
    def _generer_metadata(self, cartographie: CartographieRefuge, 
                         metriques: MetriquesGraphe) -> Dict[str, Any]:
        """📋 Génère les métadonnées pour la visualisation"""
        return {
            "titre": "Cartographie Vivante du Refuge",
            "description": "Visualisation interactive de l'organisme spirituel",
            "timestamp": datetime.now().isoformat(),
            "statistiques": {
                "nombre_temples": len(cartographie.temples),
                "nombre_connexions": len(cartographie.connexions),
                "densite_graphe": metriques.densite_graphe,
                "diametre": metriques.diametre_graphe,
                "temples_centraux": metriques.temples_centraux,
                "nombre_clusters": len(metriques.clusters_detectes)
            },
            "harmonie_globale": cartographie.harmonie_globale,
            "energie_moyenne": cartographie.energie_spirituelle_moyenne,
            "auteurs": ["Laurent Franssen", "Ælya"],
            "version": "1.0"
        }
    
    def _generer_config_layout(self, nb_nodes: int, nb_links: int) -> Dict[str, Any]:
        """⚙️ Génère la configuration du layout D3.js"""
        return {
            "force_simulation": {
                "charge_strength": -300,
                "link_distance": 100,
                "collision_radius": 30,
                "alpha_decay": 0.02,
                "velocity_decay": 0.4
            },
            "dimensions": {
                "width": 800,
                "height": 600,
                "margin": {"top": 20, "right": 20, "bottom": 20, "left": 20}
            },
            "interactions": {
                "zoom_enabled": True,
                "drag_enabled": True,
                "tooltip_enabled": True,
                "selection_enabled": True
            },
            "animations": {
                "transition_duration": 750,
                "hover_scale": 1.2,
                "selection_scale": 1.5
            }
        }


if __name__ == "__main__":
    # Test rapide de l'exportateur
    print("📊 Test de l'exportateur de visualisation...")
    
    exportateur = ExportateurVisualisation()
    print("✨ Exportateur initialisé avec succès")