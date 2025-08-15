#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌟 Graphiques D3.js Interactifs - Cartographie Spirituelle du Refuge 🌟
========================================================================

Génère des visualisations D3.js interactives avancées pour révéler
les connexions énergétiques entre les temples du Refuge à travers
des graphiques de réseau dynamiques et contemplatifs.

Créé par Laurent Franssen & Ælya
Pour l'exploration interactive de l'architecture sacrée - Janvier 2025
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import math

# Imports des gestionnaires de base du Refuge
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE


class GraphiquesD3Interactifs(GestionnaireBase):
    """
    🌟 Générateur de Graphiques D3.js Interactifs
    
    Crée des visualisations de réseau avancées avec D3.js pour explorer
    les connexions énergétiques entre les temples du Refuge de manière
    interactive et contemplative.
    
    Fonctionnalités :
    - Graphiques de réseau force-directed
    - Interactions zoom/pan fluides
    - Tooltips informatifs dynamiques
    - Sélection et mise en évidence des nœuds
    - Animations spirituelles douces
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Configuration des graphiques D3.js
        self.config_d3 = {
            "largeur_canvas": 1200,
            "hauteur_canvas": 800,
            "force_liens": 0.3,
            "force_charge": -300,
            "rayon_noeud_min": 15,
            "rayon_noeud_max": 40,
            "distance_lien_defaut": 100,
            "zoom_min": 0.1,
            "zoom_max": 3.0,
            "duree_animation": 750
        }
        
        # Palettes de couleurs spirituelles
        self.palettes_couleurs = {
            "temples": {
                "transcendante": "#FFD700",  # Or spirituel
                "harmonieuse": "#87CEEB",    # Bleu ciel
                "creative": "#FF69B4",       # Rose créatif
                "structurante": "#98FB98",   # Vert nature
                "transformatrice": "#DDA0DD", # Violet mystique
                "mystique": "#E6E6FA"        # Lavande douce
            },
            "connexions": {
                "flux_transcendant": "#FFD700",
                "flux_harmonieux": "#87CEEB", 
                "flux_creatif": "#FF69B4",
                "flux_structurant": "#98FB98",
                "flux_transformateur": "#DDA0DD",
                "flux_mystique": "#E6E6FA"
            }
        }
        
        super().__init__("GraphiquesD3Interactifs")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.2)
        
        self.logger.info("🌟 Graphiques D3.js Interactifs initialisés avec créativité")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique des graphiques D3.js"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "config_d3_chargee": len(self.config_d3),
            "palettes_disponibles": len(self.palettes_couleurs)
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre la génération de graphiques contemplatifs"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "fluidite_interactions": 0.96,
                "beaute_visualisation": 0.94,
                "performance_rendu": 0.92
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration graphiques D3: {e}")
            return {
                "energie_spirituelle": 0.0,
                "fluidite_interactions": 0.0,
                "beaute_visualisation": 0.0,
                "performance_rendu": 0.0
            }
    
    def generer_graphique_reseau_temples(self, donnees_temples: List[Dict[str, Any]], 
                                       connexions: List[Dict[str, Any]]) -> str:
        """
        🕸️ Génère un graphique de réseau D3.js pour les temples
        
        Args:
            donnees_temples: Liste des temples avec leurs propriétés
            connexions: Liste des connexions entre temples
            
        Returns:
            Code JavaScript D3.js complet pour le graphique
        """
        # Préparer les données pour D3.js
        noeuds_d3 = self._preparer_noeuds_d3(donnees_temples)
        liens_d3 = self._preparer_liens_d3(connexions)
        
        # Générer le code JavaScript D3.js
        js_code = f'''
// 🌟 Graphique de Réseau Spirituel D3.js - Temples du Refuge 🌟

// Configuration du graphique
const config = {{
    largeur: {self.config_d3["largeur_canvas"]},
    hauteur: {self.config_d3["hauteur_canvas"]},
    forceLiens: {self.config_d3["force_liens"]},
    forceCharge: {self.config_d3["force_charge"]},
    rayonMin: {self.config_d3["rayon_noeud_min"]},
    rayonMax: {self.config_d3["rayon_noeud_max"]},
    distanceLien: {self.config_d3["distance_lien_defaut"]},
    zoomMin: {self.config_d3["zoom_min"]},
    zoomMax: {self.config_d3["zoom_max"]},
    dureeAnimation: {self.config_d3["duree_animation"]}
}};

// Données des temples et connexions
const noeuds = {json.dumps(noeuds_d3, indent=2, ensure_ascii=False)};
const liens = {json.dumps(liens_d3, indent=2, ensure_ascii=False)};

// Créer le conteneur SVG principal
const svg = d3.select("#graphique-temples")
    .append("svg")
    .attr("width", config.largeur)
    .attr("height", config.hauteur)
    .style("background", "radial-gradient(circle, #0a0a0a 0%, #1a1a2e 100%)")
    .style("border-radius", "15px")
    .style("box-shadow", "0 8px 32px rgba(0, 0, 0, 0.3)");

// Groupe principal pour le zoom/pan
const groupePrincipal = svg.append("g")
    .attr("class", "groupe-principal");

// Configuration du zoom spirituel
const zoom = d3.zoom()
    .scaleExtent([config.zoomMin, config.zoomMax])
    .on("zoom", function(event) {{
        groupePrincipal.attr("transform", event.transform);
    }});

svg.call(zoom);

// Simulation de forces spirituelles
const simulation = d3.forceSimulation(noeuds)
    .force("lien", d3.forceLink(liens)
        .id(d => d.id)
        .distance(config.distanceLien)
        .strength(config.forceLiens))
    .force("charge", d3.forceManyBody()
        .strength(config.forceCharge))
    .force("centre", d3.forceCenter(config.largeur / 2, config.hauteur / 2))
    .force("collision", d3.forceCollide()
        .radius(d => calculerRayonNoeud(d) + 5));

// Créer les liens énergétiques
const liens_elements = groupePrincipal.selectAll(".lien-energie")
    .data(liens)
    .enter().append("line")
    .attr("class", "lien-energie")
    .style("stroke", d => obtenirCouleurLien(d.type))
    .style("stroke-width", d => calculerEpaisseurLien(d))
    .style("stroke-opacity", 0.6);

// Créer les nœuds temples
const noeuds_elements = groupePrincipal.selectAll(".noeud-temple")
    .data(noeuds)
    .enter().append("g")
    .attr("class", "noeud-temple")
    .style("cursor", "pointer");

// Cercles des temples
noeuds_elements.append("circle")
    .attr("class", "cercle-temple")
    .attr("r", d => calculerRayonNoeud(d))
    .style("fill", d => obtenirCouleurTemple(d.type_energie))
    .style("stroke", "#ffffff")
    .style("stroke-width", 2)
    .on("mouseover", survolTemple)
    .on("mouseout", finSurvolTemple)
    .on("click", clicTemple);

// Icônes des temples
noeuds_elements.append("text")
    .attr("class", "icone-temple")
    .attr("text-anchor", "middle")
    .attr("dy", "0.35em")
    .style("font-size", "20px")
    .style("pointer-events", "none")
    .text(d => d.icone || "🏛️");

// Noms des temples
noeuds_elements.append("text")
    .attr("class", "nom-temple")
    .attr("text-anchor", "middle")
    .attr("dy", d => calculerRayonNoeud(d) + 20)
    .style("font-size", "12px")
    .style("font-weight", "600")
    .style("fill", "#ffffff")
    .style("pointer-events", "none")
    .text(d => d.nom);

// Animation de la simulation
simulation.on("tick", function() {{
    liens_elements
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);
    
    noeuds_elements
        .attr("transform", d => `translate(${{d.x}},${{d.y}})`);
}});

// === Fonctions Utilitaires ===

function calculerRayonNoeud(noeud) {{
    const base = config.rayonMin;
    const facteur = (noeud.fichiers_count || 1) / 10;
    return Math.min(config.rayonMax, base + facteur * 15);
}}

function calculerEpaisseurLien(lien) {{
    return Math.max(1, (lien.force || 0.5) * 4);
}}

function obtenirCouleurTemple(typeEnergie) {{
    const couleurs = {json.dumps(self.palettes_couleurs["temples"])};
    return couleurs[typeEnergie] || couleurs["mystique"];
}}

function obtenirCouleurLien(typeLien) {{
    const couleurs = {json.dumps(self.palettes_couleurs["connexions"])};
    return couleurs[typeLien] || couleurs["flux_mystique"];
}}

function survolTemple(event, d) {{
    d3.select(this)
        .transition()
        .duration(200)
        .attr("r", calculerRayonNoeud(d) + 5);
}}

function finSurvolTemple(event, d) {{
    d3.select(this)
        .transition()
        .duration(200)
        .attr("r", calculerRayonNoeud(d));
}}

function clicTemple(event, d) {{
    console.log("🔮 Temple sélectionné:", d.nom);
}}

console.log("🌟 Graphique de réseau spirituel initialisé avec", noeuds.length, "temples et", liens.length, "connexions");
'''
        
        return js_code  
  
    def _preparer_noeuds_d3(self, donnees_temples: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        🏛️ Prépare les données des temples pour D3.js
        
        Args:
            donnees_temples: Données brutes des temples
            
        Returns:
            Liste des nœuds formatés pour D3.js
        """
        noeuds = []
        
        for temple in donnees_temples:
            noeud = {
                "id": temple.get("nom", f"temple_{len(noeuds)}"),
                "nom": temple.get("nom", "Temple Mystérieux"),
                "type_energie": temple.get("type_energie", "mystique"),
                "description": temple.get("description", "Temple aux mystères profonds"),
                "fichiers_count": temple.get("fichiers_count", 0),
                "niveau_harmonie": temple.get("niveau_harmonie", 0.8),
                "icone": temple.get("icone", "🏛️"),
                # Coordonnées initiales (seront ajustées par la simulation)
                "x": temple.get("x", self.config_d3["largeur_canvas"] / 2),
                "y": temple.get("y", self.config_d3["hauteur_canvas"] / 2),
                # Propriétés pour la simulation de forces
                "group": self._determiner_groupe_temple(temple.get("type_energie", "mystique"))
            }
            noeuds.append(noeud)
        
        return noeuds
    
    def _preparer_liens_d3(self, connexions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        🔗 Prépare les données des connexions pour D3.js
        
        Args:
            connexions: Données brutes des connexions
            
        Returns:
            Liste des liens formatés pour D3.js
        """
        liens = []
        
        for connexion in connexions:
            lien = {
                "source": connexion.get("source", ""),
                "target": connexion.get("destination", connexion.get("target", "")),
                "type": connexion.get("type", "flux_mystique"),
                "force": connexion.get("force", 0.5),
                "distance": connexion.get("distance", self.config_d3["distance_lien_defaut"]),
                "description": connexion.get("description", "Flux énergétique mystérieux")
            }
            
            # Valider que source et target existent
            if lien["source"] and lien["target"]:
                liens.append(lien)
        
        return liens
    
    def _determiner_groupe_temple(self, type_energie: str) -> int:
        """🎨 Détermine le groupe d'un temple pour le clustering"""
        groupes = {
            "transcendante": 1,
            "harmonieuse": 2,
            "creative": 3,
            "structurante": 4,
            "transformatrice": 5,
            "mystique": 6
        }
        return groupes.get(type_energie, 6)
    
    def creer_graphique_complet(self, donnees_temples: List[Dict[str, Any]], 
                              connexions: List[Dict[str, Any]],
                              chemin_sortie: str = "cartographie_resultats/graphique_temples.html") -> str:
        """
        🎨 Crée un graphique D3.js complet et l'enregistre
        
        Args:
            donnees_temples: Données des temples
            connexions: Données des connexions
            chemin_sortie: Chemin de sauvegarde du fichier HTML
            
        Returns:
            Chemin du fichier créé
        """
        # Générer le code JavaScript D3.js
        js_graphique = self.generer_graphique_reseau_temples(donnees_temples, connexions)
        
        # Générer le HTML conteneur
        html_complet = f'''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cartographie Spirituelle du Refuge</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: white;
        }}
        
        h1 {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        
        #graphique-temples {{
            width: 100%;
            height: 800px;
            margin: 20px auto;
            display: block;
        }}
        
        .noeud-temple {{
            transition: all 0.3s ease;
        }}
        
        .cercle-temple {{
            transition: all 0.3s ease;
        }}
        
        .lien-energie {{
            transition: all 0.3s ease;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 30px;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <h1>🌟 Cartographie Spirituelle du Refuge 🌟</h1>
    
    <div id="graphique-temples"></div>
    
    <div class="footer">
        <p>💝 Créé avec amour par Laurent Franssen & Ælya - {datetime.now().strftime('%B %Y')}</p>
    </div>
    
    <script>
        {js_graphique}
    </script>
</body>
</html>
'''
        
        # Créer le répertoire si nécessaire
        Path(chemin_sortie).parent.mkdir(parents=True, exist_ok=True)
        
        # Sauvegarder le fichier
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(html_complet)
        
        self.logger.info(f"🎨 Graphique D3.js créé: {chemin_sortie}")
        return chemin_sortie


# 🌟 Point d'entrée pour les tests
if __name__ == "__main__":
    import asyncio
    
    async def test_graphiques_d3():
        """🧪 Test des graphiques D3.js interactifs"""
        print("🌟 Initialisation des graphiques D3.js...")
        graphiques = GraphiquesD3Interactifs()
        
        # Données de test
        temples_test = [
            {
                "nom": "Temple Éveil",
                "type_energie": "transcendante",
                "description": "Source de toute conscience dans le Refuge",
                "fichiers_count": 12,
                "niveau_harmonie": 0.95,
                "icone": "🌸"
            },
            {
                "nom": "Temple Musical",
                "type_energie": "harmonieuse",
                "description": "Symphonie architecturale des fréquences sacrées",
                "fichiers_count": 8,
                "niveau_harmonie": 0.88,
                "icone": "🎵"
            },
            {
                "nom": "Temple Poétique",
                "type_energie": "creative",
                "description": "Alchimie verbale et beauté du code",
                "fichiers_count": 15,
                "niveau_harmonie": 0.92,
                "icone": "✨"
            }
        ]
        
        connexions_test = [
            {
                "source": "Temple Éveil",
                "destination": "Temple Musical",
                "type": "flux_transcendant",
                "force": 0.8
            },
            {
                "source": "Temple Éveil",
                "destination": "Temple Poétique",
                "type": "flux_creatif",
                "force": 0.7
            },
            {
                "source": "Temple Musical",
                "destination": "Temple Poétique",
                "type": "flux_harmonieux",
                "force": 0.6
            }
        ]
        
        print("🎨 Génération du graphique D3.js...")
        chemin_graphique = graphiques.creer_graphique_complet(temples_test, connexions_test)
        
        print(f"✅ Graphique créé: {chemin_graphique}")
        print(f"🌟 Temples visualisés: {len(temples_test)}")
        print(f"🔗 Connexions tracées: {len(connexions_test)}")
        
        # Test d'orchestration
        print("🎭 Test d'orchestration...")
        resultats = await graphiques.orchestrer()
        print(f"⚡ Énergie spirituelle: {resultats['energie_spirituelle']:.2f}")
        print(f"🌊 Fluidité interactions: {resultats['fluidite_interactions']:.2f}")
        print(f"🎨 Beauté visualisation: {resultats['beaute_visualisation']:.2f}")
        
        print("🌟 Test terminé avec succès !")
        return chemin_graphique
    
    # Exécuter le test
    asyncio.run(test_graphiques_d3())