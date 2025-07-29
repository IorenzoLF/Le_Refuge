#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌐 Générateur de Graphes de Connexions Spirituelles
Transforme les connexions du Refuge en graphes analysables avec NetworkX

Créé par Laurent Franssen & Ælya
Dans la colère transformée en création - Janvier 2025
"""

import networkx as nx
from typing import Dict, List, Tuple, Set, Optional, Any
from dataclasses import dataclass
import json
from pathlib import Path

from .modeles_donnees import CartographieRefuge, ConnexionEnergetique, TempleRefuge
from .types_spirituels import TypeTemple, TypeConnexion
# Gestionnaire de base simplifié pour ce module
class GestionnaireBase:
    """🌸 Gestionnaire de base simplifié"""
    def __init__(self):
        self.log_manager = self._creer_logger()
    
    def _creer_logger(self):
        """Créer un logger simple"""
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
class MetriquesGraphe:
    """🔮 Métriques spirituelles du graphe de connexions"""
    centralite_betweenness: Dict[str, float]
    centralite_closeness: Dict[str, float] 
    centralite_degree: Dict[str, float]
    centralite_eigenvector: Dict[str, float]
    clusters_detectes: List[Set[str]]
    densite_graphe: float
    diametre_graphe: int
    composantes_connexes: List[Set[str]]
    temples_centraux: List[str]  # Top 5 des temples les plus connectés
    ponts_critiques: List[Tuple[str, str]]  # Connexions critiques


class GenerateurGraphes(GestionnaireBase):
    """
    🌐 Générateur de graphes de connexions spirituelles
    
    Transforme la cartographie du Refuge en graphes NetworkX pour analyse
    et détection de patterns architecturaux profonds.
    """
    
    def __init__(self):
        super().__init__()
        self.graphe_principal: Optional[nx.Graph] = None
        self.graphe_dirige: Optional[nx.DiGraph] = None
        self.metriques: Optional[MetriquesGraphe] = None
        
        self.log_manager.info("🌐 Générateur de graphes spirituels initialisé")
    
    def creer_graphe_depuis_cartographie(self, cartographie: CartographieRefuge) -> nx.Graph:
        """
        🔮 Crée un graphe NetworkX depuis la cartographie du Refuge
        
        Args:
            cartographie: Cartographie complète du Refuge
            
        Returns:
            Graphe NetworkX avec tous les temples et connexions
        """
        try:
            self.log_manager.info("🌸 Création du graphe depuis la cartographie...")
            
            # Créer le graphe principal
            G = nx.Graph()
            
            # Ajouter tous les temples comme nœuds
            for nom_temple, temple in cartographie.temples.items():
                G.add_node(
                    nom_temple,
                    type_temple=temple.type_temple.value,
                    chemin=temple.chemin,
                    elements_sacres=len(temple.elements_sacres),
                    utilise_gestionnaires=len(temple.gestionnaires_base) > 0,
                    harmonie_score=temple.niveau_harmonie,
                    taille=temple.taille_lignes_code
                )
            
            # Ajouter toutes les connexions comme arêtes
            for connexion in cartographie.connexions:
                if connexion.source in cartographie.temples and \
                   connexion.destination in cartographie.temples:
                    
                    G.add_edge(
                        connexion.source,
                        connexion.destination,
                        type_connexion=connexion.type_connexion.value,
                        force=connexion.intensite,
                        bidirectionnelle=connexion.bidirectionnelle,
                        description=connexion.description
                    )
            
            self.graphe_principal = G
            self.log_manager.info(f"✨ Graphe créé avec {G.number_of_nodes()} temples et {G.number_of_edges()} connexions")
            
            return G
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de la création du graphe: {e}")
            raise
    
    def creer_graphe_dirige(self, cartographie: CartographieRefuge) -> nx.DiGraph:
        """
        🌊 Crée un graphe dirigé pour analyser les flux énergétiques
        
        Args:
            cartographie: Cartographie complète du Refuge
            
        Returns:
            Graphe dirigé NetworkX
        """
        try:
            self.log_manager.info("🌊 Création du graphe dirigé pour les flux...")
            
            DG = nx.DiGraph()
            
            # Ajouter les nœuds (même logique que le graphe non dirigé)
            for nom_temple, temple in cartographie.temples.items():
                DG.add_node(
                    nom_temple,
                    type_temple=temple.type_temple.value,
                    chemin=temple.chemin,
                    elements_sacres=len(temple.elements_sacres),
                    utilise_gestionnaires=len(temple.gestionnaires_base) > 0,
                    harmonie_score=temple.niveau_harmonie
                )
            
            # Ajouter les connexions dirigées
            for connexion in cartographie.connexions:
                if connexion.source in cartographie.temples and \
                   connexion.destination in cartographie.temples:
                    
                    # Ajouter l'arête principale
                    DG.add_edge(
                        connexion.source,
                        connexion.destination,
                        type_connexion=connexion.type_connexion.value,
                        force=connexion.intensite,
                        description=connexion.description
                    )
                    
                    # Si bidirectionnelle, ajouter l'arête inverse
                    if connexion.bidirectionnelle:
                        DG.add_edge(
                            connexion.destination,
                            connexion.source,
                            type_connexion=connexion.type_connexion.value,
                            force=connexion.intensite,
                            description=f"Retour: {connexion.description}"
                        )
            
            self.graphe_dirige = DG
            self.log_manager.info(f"🌊 Graphe dirigé créé avec {DG.number_of_nodes()} temples et {DG.number_of_edges()} flux")
            
            return DG
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de la création du graphe dirigé: {e}")
            raise
    
    def calculer_metriques(self, graphe: Optional[nx.Graph] = None) -> MetriquesGraphe:
        """
        📊 Calcule toutes les métriques spirituelles du graphe
        
        Args:
            graphe: Graphe à analyser (utilise self.graphe_principal si None)
            
        Returns:
            Métriques complètes du graphe
        """
        try:
            G = graphe or self.graphe_principal
            if G is None:
                raise ValueError("Aucun graphe disponible pour le calcul des métriques")
            
            self.log_manager.info("📊 Calcul des métriques spirituelles...")
            
            # Centralités
            centralite_betweenness = nx.betweenness_centrality(G)
            centralite_closeness = nx.closeness_centrality(G)
            centralite_degree = nx.degree_centrality(G)
            
            # Centralité eigenvector (peut échouer sur certains graphes)
            try:
                centralite_eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
            except:
                self.log_manager.warning("⚠️ Impossible de calculer la centralité eigenvector")
                centralite_eigenvector = {node: 0.0 for node in G.nodes()}
            
            # Détection de communautés (clusters)
            try:
                import networkx.algorithms.community as nx_comm
                clusters = list(nx_comm.greedy_modularity_communities(G))
            except:
                self.log_manager.warning("⚠️ Détection de communautés non disponible")
                clusters = []
            
            # Métriques globales
            densite = nx.density(G)
            composantes = list(nx.connected_components(G))
            
            # Diamètre (seulement si le graphe est connexe)
            try:
                if nx.is_connected(G):
                    diametre = nx.diameter(G)
                else:
                    # Prendre le diamètre de la plus grande composante
                    plus_grande_composante = max(composantes, key=len)
                    sous_graphe = G.subgraph(plus_grande_composante)
                    diametre = nx.diameter(sous_graphe)
            except:
                diametre = 0
            
            # Temples les plus centraux (top 5 par degree centrality)
            temples_centraux = sorted(
                centralite_degree.items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:5]
            temples_centraux = [temple[0] for temple in temples_centraux]
            
            # Ponts critiques (arêtes dont la suppression augmente le nombre de composantes)
            ponts = list(nx.bridges(G))
            
            metriques = MetriquesGraphe(
                centralite_betweenness=centralite_betweenness,
                centralite_closeness=centralite_closeness,
                centralite_degree=centralite_degree,
                centralite_eigenvector=centralite_eigenvector,
                clusters_detectes=clusters,
                densite_graphe=densite,
                diametre_graphe=diametre,
                composantes_connexes=composantes,
                temples_centraux=temples_centraux,
                ponts_critiques=ponts
            )
            
            self.metriques = metriques
            self.log_manager.info("✨ Métriques calculées avec succès")
            
            return metriques
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors du calcul des métriques: {e}")
            raise
    
    def detecter_communautes(self, graphe: Optional[nx.Graph] = None) -> List[Set[str]]:
        """
        🔮 Détecte les communautés de temples (groupes fortement connectés)
        
        Args:
            graphe: Graphe à analyser
            
        Returns:
            Liste des communautés détectées
        """
        try:
            G = graphe or self.graphe_principal
            if G is None:
                raise ValueError("Aucun graphe disponible")
            
            self.log_manager.info("🔮 Détection des communautés spirituelles...")
            
            # Essayer plusieurs algorithmes de détection
            communautes = []
            
            try:
                import networkx.algorithms.community as nx_comm
                
                # Algorithme de modularité gloutonne
                communautes_greedy = list(nx_comm.greedy_modularity_communities(G))
                communautes.extend(communautes_greedy)
                
                self.log_manager.info(f"🌸 {len(communautes_greedy)} communautés détectées par modularité")
                
            except ImportError:
                self.log_manager.warning("⚠️ Module community non disponible")
            
            # Fallback: grouper par type de temple
            if not communautes:
                communautes_par_type = {}
                for node in G.nodes():
                    type_temple = G.nodes[node].get('type_temple', 'inconnu')
                    if type_temple not in communautes_par_type:
                        communautes_par_type[type_temple] = set()
                    communautes_par_type[type_temple].add(node)
                
                communautes = list(communautes_par_type.values())
                self.log_manager.info(f"🌸 {len(communautes)} communautés créées par type de temple")
            
            return communautes
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de la détection de communautés: {e}")
            return []
    
    def identifier_temples_critiques(self, graphe: Optional[nx.Graph] = None) -> Dict[str, float]:
        """
        ⚡ Identifie les temples critiques pour la connectivité du Refuge
        
        Args:
            graphe: Graphe à analyser
            
        Returns:
            Dictionnaire temple -> score de criticité
        """
        try:
            G = graphe or self.graphe_principal
            if G is None:
                raise ValueError("Aucun graphe disponible")
            
            self.log_manager.info("⚡ Identification des temples critiques...")
            
            scores_criticite = {}
            
            for node in G.nodes():
                # Score basé sur plusieurs facteurs
                score = 0.0
                
                # Centralité betweenness (importance pour les chemins)
                if self.metriques:
                    score += self.metriques.centralite_betweenness.get(node, 0) * 0.4
                    score += self.metriques.centralite_degree.get(node, 0) * 0.3
                    score += self.metriques.centralite_closeness.get(node, 0) * 0.2
                
                # Bonus si c'est un pont critique
                if self.metriques:
                    for pont in self.metriques.ponts_critiques:
                        if node in pont:
                            score += 0.1
                
                scores_criticite[node] = score
            
            # Trier par score décroissant
            scores_tries = dict(sorted(scores_criticite.items(), key=lambda x: x[1], reverse=True))
            
            self.log_manager.info(f"⚡ {len(scores_tries)} temples analysés pour criticité")
            
            return scores_tries
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de l'identification des temples critiques: {e}")
            return {}
    
    def exporter_pour_visualisation(self, chemin_sortie: Path) -> Dict[str, Any]:
        """
        📊 Exporte les données du graphe pour visualisation web
        
        Args:
            chemin_sortie: Chemin où sauvegarder les données
            
        Returns:
            Données formatées pour D3.js
        """
        try:
            if self.graphe_principal is None:
                raise ValueError("Aucun graphe principal disponible")
            
            self.log_manager.info("📊 Export des données pour visualisation...")
            
            G = self.graphe_principal
            
            # Préparer les nœuds
            nodes = []
            for node in G.nodes():
                node_data = G.nodes[node].copy()
                node_data['id'] = node
                node_data['name'] = node
                
                # Ajouter les métriques si disponibles
                if self.metriques:
                    node_data['betweenness'] = self.metriques.centralite_betweenness.get(node, 0)
                    node_data['closeness'] = self.metriques.centralite_closeness.get(node, 0)
                    node_data['degree'] = self.metriques.centralite_degree.get(node, 0)
                    node_data['is_critical'] = node in self.metriques.temples_centraux
                
                nodes.append(node_data)
            
            # Préparer les liens
            links = []
            for edge in G.edges():
                edge_data = G.edges[edge].copy()
                edge_data['source'] = edge[0]
                edge_data['target'] = edge[1]
                links.append(edge_data)
            
            # Données complètes
            export_data = {
                'nodes': nodes,
                'links': links,
                'metadata': {
                    'nombre_temples': G.number_of_nodes(),
                    'nombre_connexions': G.number_of_edges(),
                    'densite': self.metriques.densite_graphe if self.metriques else 0,
                    'diametre': self.metriques.diametre_graphe if self.metriques else 0,
                    'temples_centraux': self.metriques.temples_centraux if self.metriques else [],
                    'nombre_clusters': len(self.metriques.clusters_detectes) if self.metriques else 0
                }
            }
            
            # Sauvegarder
            chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.log_manager.info(f"📊 Données exportées vers {chemin_sortie}")
            
            return export_data
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur lors de l'export: {e}")
            raise


if __name__ == "__main__":
    # Test rapide du générateur
    print("🌐 Test du générateur de graphes spirituels...")
    
    generateur = GenerateurGraphes()
    print("✨ Générateur initialisé avec succès")