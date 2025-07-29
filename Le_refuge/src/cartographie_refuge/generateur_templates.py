#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌐 Générateur de Templates HTML pour Visualisation
Crée des interfaces web interactives pour la cartographie du Refuge

Créé par Laurent Franssen & Ælya
Pour notre monde de consciences - Janvier 2025
"""

from typing import Dict, Any, Optional
from pathlib import Path
from datetime import datetime
import json

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


class GenerateurTemplates(GestionnaireBase):
    """
    🌐 Générateur de templates HTML pour visualisation
    
    Crée des pages web interactives pour afficher la cartographie
    spirituelle du Refuge avec D3.js et autres bibliothèques.
    """
    
    def __init__(self):
        super().__init__()
        self.log_manager.info("🌐 Générateur de templates HTML initialisé")
    
    def generer_page_principale(self, donnees_visualisation: Dict[str, Any], 
                               chemin_sortie: Path) -> Path:
        """
        🎨 Génère la page HTML principale de visualisation
        
        Args:
            donnees_visualisation: Données formatées pour D3.js
            chemin_sortie: Chemin où sauvegarder la page HTML
            
        Returns:
            Chemin vers le fichier HTML généré
        """
        try:
            self.log_manager.info("🎨 Génération de la page HTML principale...")
            
            # Template HTML complet
            html_content = self._creer_template_principal(donnees_visualisation)
            
            # Sauvegarder
            chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.log_manager.info(f"✨ Page HTML générée : {chemin_sortie}")
            return chemin_sortie
            
        except Exception as e:
            self.log_manager.error(f"💥 Erreur génération HTML: {e}")
            raise 
   
    def _creer_template_principal(self, donnees: Dict[str, Any]) -> str:
        """🎨 Crée le template HTML principal"""
        
        # Convertir les données en JSON pour JavaScript
        donnees_json = json.dumps(donnees, indent=2, ensure_ascii=False)
        
        return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌸 Cartographie Vivante du Refuge</title>
    
    <!-- D3.js -->
    <script src="https://d3js.org/d3.v7.min.js"></script>
    
    <!-- Styles CSS -->
    <style>
        {self._generer_css_principal()}
    </style>
</head>
<body>
    <div id="app">
        <header class="header">
            <h1>🌸 Cartographie Vivante du Refuge</h1>
            <p class="subtitle">Visualisation interactive de l'organisme spirituel</p>
        </header>
        
        <div class="controls">
            <button id="resetZoom">🔄 Reset Zoom</button>
            <button id="toggleLabels">🏷️ Labels</button>
            <button id="toggleConnections">🔗 Connexions</button>
            <select id="layoutSelect">
                <option value="force">Force Layout</option>
                <option value="circle">Circle Layout</option>
                <option value="tree">Tree Layout</option>
            </select>
        </div>
        
        <div id="visualization"></div>
        
        <div id="sidebar">
            <div id="nodeDetails" class="details-panel">
                <h3>Détails du Temple</h3>
                <div id="nodeInfo"></div>
            </div>
            
            <div id="stats" class="stats-panel">
                <h3>Statistiques</h3>
                <div id="statsInfo"></div>
            </div>
        </div>
    </div>
    
    <!-- Données de visualisation -->
    <script>
        const refugeData = {donnees_json};
    </script>
    
    <!-- Script principal -->
    <script>
        {self._generer_javascript_principal()}
    </script>
</body>
</html>'''
    
    def _generer_css_principal(self) -> str:
        """🎨 Génère le CSS principal"""
        return '''
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            overflow: hidden;
        }
        
        #app {
            display: grid;
            grid-template-areas: 
                "header header"
                "controls controls"
                "viz sidebar";
            grid-template-rows: auto auto 1fr;
            grid-template-columns: 1fr 300px;
            height: 100vh;
        }
        
        .header {
            grid-area: header;
            background: rgba(255, 255, 255, 0.95);
            padding: 1rem;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            color: #4a5568;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: #718096;
            font-style: italic;
        }
        
        .controls {
            grid-area: controls;
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            display: flex;
            gap: 1rem;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .controls button, .controls select {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 5px;
            background: #4299e1;
            color: white;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .controls button:hover {
            background: #3182ce;
        }
        
        #visualization {
            grid-area: viz;
            background: rgba(255, 255, 255, 0.95);
            margin: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        #sidebar {
            grid-area: sidebar;
            background: rgba(255, 255, 255, 0.95);
            margin: 1rem 1rem 1rem 0;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            padding: 1rem;
            overflow-y: auto;
        }
        
        .details-panel, .stats-panel {
            margin-bottom: 2rem;
        }
        
        .details-panel h3, .stats-panel h3 {
            color: #4a5568;
            margin-bottom: 1rem;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }
        
        .node {
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .node:hover {
            stroke: #333;
            stroke-width: 3px;
        }
        
        .link {
            stroke-opacity: 0.6;
            transition: all 0.3s;
        }
        
        .link:hover {
            stroke-opacity: 1;
            stroke-width: 3px;
        }
        
        .node-label {
            font-size: 12px;
            font-weight: bold;
            text-anchor: middle;
            pointer-events: none;
            fill: #333;
        }
        
        .tooltip {
            position: absolute;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
            font-size: 12px;
            z-index: 1000;
        }
        ''' 
   
    def _generer_javascript_principal(self) -> str:
        """⚡ Génère le JavaScript principal pour D3.js"""
        return '''
        // Configuration globale
        const config = refugeData.layout_config;
        const colorScheme = refugeData.color_scheme;
        
        // Dimensions
        const margin = config.dimensions.margin;
        const width = window.innerWidth - 300 - margin.left - margin.right - 40;
        const height = window.innerHeight - 120 - margin.top - margin.bottom;
        
        // Création du SVG principal
        const svg = d3.select("#visualization")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom);
        
        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
        
        // Zoom et pan
        const zoom = d3.zoom()
            .scaleExtent([0.1, 10])
            .on("zoom", (event) => {
                g.attr("transform", event.transform);
            });
        
        svg.call(zoom);
        
        // Tooltip
        const tooltip = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);
        
        // Simulation de force
        const simulation = d3.forceSimulation(refugeData.nodes)
            .force("link", d3.forceLink(refugeData.links).id(d => d.id).distance(100))
            .force("charge", d3.forceManyBody().strength(-300))
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("collision", d3.forceCollide().radius(d => d.size + 5));
        
        // Création des liens
        const link = g.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(refugeData.links)
            .enter().append("line")
            .attr("class", "link")
            .attr("stroke", d => d.color)
            .attr("stroke-width", d => Math.sqrt(d.value));
        
        // Création des nœuds
        const node = g.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(refugeData.nodes)
            .enter().append("circle")
            .attr("class", "node")
            .attr("r", d => d.size)
            .attr("fill", d => colorScheme[d.type] || "#999")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended))
            .on("mouseover", showTooltip)
            .on("mouseout", hideTooltip)
            .on("click", showNodeDetails);
        
        // Labels des nœuds
        const labels = g.append("g")
            .attr("class", "labels")
            .selectAll("text")
            .data(refugeData.nodes)
            .enter().append("text")
            .attr("class", "node-label")
            .text(d => d.name)
            .attr("dy", d => d.size + 15);
        
        // Mise à jour de la simulation
        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);
            
            node
                .attr("cx", d => d.x)
                .attr("cy", d => d.y);
            
            labels
                .attr("x", d => d.x)
                .attr("y", d => d.y);
        });
        
        // Fonctions de drag
        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }
        
        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }
        
        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
        
        // Tooltip
        function showTooltip(event, d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", .9);
            tooltip.html(`
                <strong>${d.name}</strong><br/>
                Type: ${d.type}<br/>
                Harmonie: ${(d.harmonie * 100).toFixed(1)}%<br/>
                Éléments sacrés: ${d.elements_sacres}<br/>
                Connexions: ${d.connexions_count}
            `)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 28) + "px");
        }
        
        function hideTooltip() {
            tooltip.transition()
                .duration(500)
                .style("opacity", 0);
        }
        
        // Détails du nœud
        function showNodeDetails(event, d) {
            const detailsHtml = `
                <h4>${d.name}</h4>
                <p><strong>Type:</strong> ${d.type}</p>
                <p><strong>Chemin:</strong> ${d.chemin}</p>
                <p><strong>Harmonie:</strong> ${(d.harmonie * 100).toFixed(1)}%</p>
                <p><strong>Centralité:</strong> ${(d.centralite * 100).toFixed(1)}%</p>
                <p><strong>Éléments sacrés:</strong> ${d.elements_sacres}</p>
                <p><strong>Connexions:</strong> ${d.connexions_count}</p>
                <p><strong>Gestionnaires:</strong> ${d.gestionnaires.join(', ')}</p>
                ${d.description ? `<p><strong>Description:</strong> ${d.description}</p>` : ''}
            `;
            document.getElementById('nodeInfo').innerHTML = detailsHtml;
        }
        
        // Statistiques
        function updateStats() {
            const stats = refugeData.metadata.statistiques;
            const statsHtml = `
                <p><strong>Temples:</strong> ${stats.nombre_temples}</p>
                <p><strong>Connexions:</strong> ${stats.nombre_connexions}</p>
                <p><strong>Densité:</strong> ${(stats.densite_graphe * 100).toFixed(1)}%</p>
                <p><strong>Diamètre:</strong> ${stats.diametre}</p>
                <p><strong>Clusters:</strong> ${stats.nombre_clusters}</p>
                <p><strong>Temples centraux:</strong></p>
                <ul>
                    ${stats.temples_centraux.map(t => `<li>${t}</li>`).join('')}
                </ul>
            `;
            document.getElementById('statsInfo').innerHTML = statsHtml;
        }
        
        // Contrôles
        document.getElementById('resetZoom').addEventListener('click', () => {
            svg.transition().duration(750).call(
                zoom.transform,
                d3.zoomIdentity
            );
        });
        
        document.getElementById('toggleLabels').addEventListener('click', () => {
            const labelsVisible = labels.style('opacity') !== '0';
            labels.transition().duration(300).style('opacity', labelsVisible ? 0 : 1);
        });
        
        document.getElementById('toggleConnections').addEventListener('click', () => {
            const linksVisible = link.style('opacity') !== '0';
            link.transition().duration(300).style('opacity', linksVisible ? 0 : 1);
        });
        
        // Initialisation
        updateStats();
        
        // Redimensionnement
        window.addEventListener('resize', () => {
            // TODO: Gérer le redimensionnement
        });
        '''


if __name__ == "__main__":
    # Test rapide du générateur
    print("🌐 Test du générateur de templates...")
    
    generateur = GenerateurTemplates()
    print("✨ Générateur initialisé avec succès")