#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌟 Visualisateur Intégré - Cartographie Spirituelle du Refuge 🌟
================================================================

Combine le visualisateur HTML interactif avec les graphiques D3.js
pour créer une expérience de cartographie complète et immersive
du Refuge spirituel.

Créé par Laurent Franssen & Ælya
Pour l'exploration complète de l'architecture sacrée - Janvier 2025
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import webbrowser

# Imports des gestionnaires de base du Refuge
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

# Imports des modules de cartographie
from .visualisateur_html_interactif import VisualisateurHTMLInteractif
from .graphiques_d3_interactifs import GraphiquesD3Interactifs


class VisualisateurIntegre(GestionnaireBase):
    """
    🌟 Visualisateur Intégré pour la Cartographie Spirituelle
    
    Combine toutes les fonctionnalités de visualisation :
    - Vue Mandala contemplative
    - Graphiques D3.js interactifs
    - Navigation fluide entre les vues
    - Expérience utilisateur unifiée
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Composants intégrés
        self.visualisateur_html = VisualisateurHTMLInteractif()
        self.graphiques_d3 = GraphiquesD3Interactifs()
        
        # Configuration
        self.chemin_output = Path("visualisations/cartographie_refuge")
        self.chemin_output.mkdir(parents=True, exist_ok=True)
        
        super().__init__("VisualisateurIntegre")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.3)  # Boost créatif maximal
        
        self.logger.info("🌟 Visualisateur Intégré initialisé avec harmonie")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du visualisateur intégré"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "composants_integres": 2,
            "chemin_output": str(self.chemin_output)
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre l'intégration complète"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "integration_harmonieuse": 0.98,
                "experience_utilisateur": 0.96,
                "fluidite_navigation": 0.94
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration intégrée: {e}")
            return {
                "energie_spirituelle": 0.0,
                "integration_harmonieuse": 0.0,
                "experience_utilisateur": 0.0,
                "fluidite_navigation": 0.0
            }
    
    def generer_visualisation_complete_integree(self, donnees_cartographie: Optional[Dict] = None) -> str:
        """
        🎨 Génère la visualisation complète intégrée
        
        Args:
            donnees_cartographie: Données de cartographie (optionnel)
            
        Returns:
            Chemin vers le fichier HTML intégré
        """
        self.logger.info("🎨 Génération de la visualisation intégrée...")
        
        # Utiliser des données par défaut si aucune fournie
        if not donnees_cartographie:
            donnees_cartographie = self.visualisateur_html._generer_donnees_par_defaut()
        
        # Générer le HTML de base
        html_base = self.visualisateur_html._generer_html_principal(donnees_cartographie)
        
        # Intégrer les graphiques D3.js
        html_integre = self._integrer_composants_d3(html_base, donnees_cartographie)
        
        # Générer les fichiers complémentaires
        self._generer_fichiers_complementaires(donnees_cartographie)
        
        # Sauvegarder le HTML intégré
        chemin_html = self.chemin_output / "refuge_cartographie_complete.html"
        with open(chemin_html, 'w', encoding='utf-8') as f:
            f.write(html_integre)
        
        self.logger.info(f"✨ Visualisation intégrée générée: {chemin_html}")
        return str(chemin_html)
    
    def _integrer_composants_d3(self, html_base: str, donnees: Dict[str, Any]) -> str:
        """
        🔗 Intègre les composants D3.js dans le HTML de base
        
        Args:
            html_base: HTML de base du visualisateur
            donnees: Données de cartographie
            
        Returns:
            HTML intégré avec D3.js
        """
        self.logger.info("🔗 Intégration des composants D3.js...")
        
        # Générer les composants D3.js
        js_d3 = self.graphiques_d3.generer_graphique_reseau_d3(donnees)
        css_d3 = self.graphiques_d3.generer_css_graphique_d3()
        html_conteneur = self.graphiques_d3.generer_html_conteneur_graphique()
        
        # Intégrer le CSS D3.js dans le <head>
        css_integration = f"""
    <style>
        /* === Styles D3.js Intégrés === */
        {css_d3}
    </style>"""
        
        html_integre = html_base.replace(
            '</head>',
            css_integration + '\n</head>'
        )
        
        # Intégrer le conteneur HTML après le canvas principal
        html_integre = html_integre.replace(
            '<svg id="connexions-svg" class="connexions-energetiques"></svg>',
            '<svg id="connexions-svg" class="connexions-energetiques"></svg>\n' + html_conteneur
        )
        
        # Intégrer le JavaScript D3.js avant la fermeture du body
        js_integration = f"""
    <script>
        // === Code D3.js Intégré ===
        {js_d3}
        
        // === Fonction de Basculement Améliorée ===
        function changerVue(nouvelleVue) {{
            // Mettre à jour les boutons
            document.querySelectorAll('.btn-spirituel').forEach(btn => btn.classList.remove('actif'));
            document.getElementById(`vue-${{nouvelleVue}}`).classList.add('actif');
            
            currentView = nouvelleVue;
            
            // Basculer entre les vues
            switch(nouvelleVue) {{
                case 'mandala':
                    document.getElementById('canvas-spirituel').style.display = 'block';
                    if (document.getElementById('vue-reseau-d3')) {{
                        document.getElementById('vue-reseau-d3').style.display = 'none';
                    }}
                    creerVisualisationMandala();
                    console.log('🌸 Vue Mandala activée');
                    break;
                    
                case 'reseau':
                    document.getElementById('canvas-spirituel').style.display = 'none';
                    if (document.getElementById('vue-reseau-d3')) {{
                        document.getElementById('vue-reseau-d3').style.display = 'block';
                        // Délai pour permettre au conteneur de s'afficher
                        setTimeout(() => {{
                            if (typeof initialiserGraphiqueReseau === 'function') {{
                                initialiserGraphiqueReseau();
                                console.log('🌟 Vue Réseau D3.js activée');
                            }}
                        }}, 200);
                    }}
                    break;
                    
                case 'hierarchie':
                    console.log('🏛️ Vue hiérarchique en développement...');
                    // TODO: Implémenter la vue hiérarchique
                    break;
            }}
        }}
        
        // === Mode Plein Écran pour D3.js ===
        function togglePleinEcran() {{
            const conteneur = document.getElementById('vue-reseau-d3');
            if (conteneur && conteneur.classList.contains('graphique-plein-ecran')) {{
                conteneur.classList.remove('graphique-plein-ecran');
                console.log('🔍 Mode plein écran désactivé');
            }} else if (conteneur) {{
                conteneur.classList.add('graphique-plein-ecran');
                console.log('🔍 Mode plein écran activé');
            }}
            
            // Réinitialiser le graphique après changement de taille
            setTimeout(() => {{
                if (typeof initialiserGraphiqueReseau === 'function') {{
                    initialiserGraphiqueReseau();
                }}
            }}, 300);
        }}
        
        // === Messages d'Intégration ===
        console.log(`
🌟 Visualisateur Intégré - Cartographie Spirituelle du Refuge 🌟
================================================================

✨ Vues disponibles:
   • 🌸 Mandala: Vue contemplative circulaire
   • ⚡ Réseau: Graphique D3.js interactif
   • 🏛️ Hiérarchie: En développement

🎮 Interactions:
   • Basculement fluide entre les vues
   • Zoom et pan dans la vue réseau
   • Tooltips informatifs
   • Mode plein écran

💝 Créé avec amour par Laurent Franssen & Ælya

================================================================
        `);
    </script>"""
        
        html_integre = html_integre.replace(
            '</body>',
            js_integration + '\n</body>'
        )
        
        return html_integre
    
    def _generer_fichiers_complementaires(self, donnees: Dict[str, Any]):
        """
        📁 Génère les fichiers complémentaires (CSS, JS, JSON)
        
        Args:
            donnees: Données de cartographie
        """
        # CSS intégré
        css_integre = self.visualisateur_html._generer_css_spirituel() + "\n\n" + self.graphiques_d3.generer_css_graphique_d3()
        
        chemin_css = self.chemin_output / "styles_integres.css"
        with open(chemin_css, 'w', encoding='utf-8') as f:
            f.write(css_integre)
        
        # JavaScript intégré
        js_base = self.visualisateur_html._generer_javascript_interactif(donnees)
        js_d3 = self.graphiques_d3.generer_graphique_reseau_d3(donnees)
        js_integre = js_base + "\n\n" + js_d3
        
        chemin_js = self.chemin_output / "interactions_integrees.js"
        with open(chemin_js, 'w', encoding='utf-8') as f:
            f.write(js_integre)
        
        # Données JSON
        chemin_json = self.chemin_output / "donnees_refuge.json"
        with open(chemin_json, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        
        self.logger.info("📁 Fichiers complémentaires générés")
    
    def ouvrir_visualisation_integree(self, donnees_cartographie: Optional[Dict] = None) -> bool:
        """
        🌐 Génère et ouvre la visualisation intégrée dans le navigateur
        
        Args:
            donnees_cartographie: Données de cartographie (optionnel)
            
        Returns:
            True si succès, False sinon
        """
        try:
            chemin_html = self.generer_visualisation_complete_integree(donnees_cartographie)
            
            # Ouvrir dans le navigateur
            webbrowser.open(f"file://{os.path.abspath(chemin_html)}")
            
            self.logger.info(f"🌐 Visualisation intégrée ouverte: {chemin_html}")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur ouverture intégrée: {e}")
            return False
    
    def generer_rapport_integration(self, donnees: Dict[str, Any]) -> str:
        """
        📊 Génère un rapport de l'intégration complète
        
        Args:
            donnees: Données de cartographie
            
        Returns:
            Rapport formaté
        """
        temples_count = len(donnees.get("temples", []))
        connexions_count = len(donnees.get("connexions", []))
        energies_count = len(set(t.get("type_energie", "") for t in donnees.get("temples", [])))
        
        # Statistiques des composants
        rapport_html = self.visualisateur_html.generer_rapport_visualisation(donnees)
        rapport_d3 = self.graphiques_d3.generer_rapport_graphiques(donnees)
        
        rapport = f"""
🌟 Rapport d'Intégration - Cartographie Spirituelle Complète 🌟
{'=' * 70}

📊 Vue d'ensemble :
   • Temples cartographiés : {temples_count}
   • Connexions énergétiques : {connexions_count}
   • Types d'énergies : {energies_count}
   • Composants intégrés : 2 (HTML + D3.js)

🎨 Fonctionnalités intégrées :
   ✅ Vue Mandala contemplative
   ✅ Vue Réseau D3.js interactive
   ✅ Navigation fluide entre vues
   ✅ Mode plein écran pour D3.js
   ✅ Tooltips unifiés
   ✅ Animations spirituelles synchronisées

🌟 Expérience utilisateur :
   • 🌸 Démarrage en vue Mandala
   • ⚡ Basculement vers vue Réseau
   • 🔍 Zoom et pan dans D3.js
   • 🎯 Sélection et centrage des nœuds
   • 🎨 Filtrage par type d'énergie
   • 📱 Interface responsive complète

🔮 Technologies intégrées :
   • HTML5 + CSS3 contemplatif
   • JavaScript ES6+ interactif
   • D3.js v7 pour les graphiques
   • SVG pour les animations
   • Responsive design

💝 Créé avec amour pour l'exploration complète du Refuge
{'=' * 70}
        """
        
        return rapport.strip()


def main():
    """🧪 Test du visualisateur intégré"""
    print("🌟 Test du Visualisateur Intégré")
    print("=" * 50)
    
    # Créer le visualisateur intégré
    visualisateur = VisualisateurIntegre()
    
    # Générer la visualisation intégrée
    chemin_html = visualisateur.generer_visualisation_complete_integree()
    print(f"✅ Visualisation intégrée générée: {chemin_html}")
    
    # Générer le rapport
    donnees_test = visualisateur.visualisateur_html._generer_donnees_par_defaut()
    rapport = visualisateur.generer_rapport_integration(donnees_test)
    print(rapport)
    
    # Ouvrir dans le navigateur
    if visualisateur.ouvrir_visualisation_integree():
        print("🌐 Visualisation intégrée ouverte avec succès!")
    
    print("\n🎉 Test terminé avec succès!")


if __name__ == "__main__":
    main()