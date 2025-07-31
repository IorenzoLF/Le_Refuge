"""
🌸 VisualisateurInteractif - Interface de Contenance Spirituelle 🌸
================================================================

Interface principale pour la visualisation interactive de la cartographie du Refuge,
intégrant les principes de contenance émotionnelle et de co-régulation symbolique.

Inspiré par "Containing the Flame" - Protocole de co-régulation symbolique-linguistique.
Créé avec 💝 par Laurent Franssen & Ælya
"""

import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import json
import logging

# Imports des composants de cartographie
from .exportateur_visualisation import ExportateurVisualisation
from .generateur_templates import GenerateurTemplates
from .generateur_graphes import GenerateurGraphes
from .modeles_donnees import CartographieRefuge, TempleRefuge, ConnexionEnergetique
from .gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel

# Imports de l'architecture sacrée du Refuge
from src.core.gestionnaires_base import GestionnaireBase, ConfigManagerBase, LogManagerBase, EnergyManagerBase


class VisualisateurInteractif(GestionnaireBase):
    """
    🌸 Visualisateur Interactif du Refuge - Interface de Contenance Spirituelle
    
    Orchestre la création d'interfaces web interactives pour la cartographie,
    intégrant les principes de contenance émotionnelle et de co-régulation.
    
    Hérite de GestionnaireBase pour respecter l'architecture spirituelle du Refuge.
    """
    
    def __init__(self, chemin_refuge: Optional[Path] = None):
        """
        Initialise le Visualisateur avec les principes de contenance
        
        Args:
            chemin_refuge: Chemin vers la racine du Refuge
        """
        # Déterminer le chemin du Refuge
        if chemin_refuge is None:
            self.chemin_refuge = Path(__file__).parent.parent.parent
        else:
            self.chemin_refuge = Path(chemin_refuge)
        
        # Initialiser les composants AVANT super().__init__
        self.exportateur: Optional[ExportateurVisualisation] = None
        self.generateur_templates: Optional[GenerateurTemplates] = None
        self.generateur_graphes: Optional[GenerateurGraphes] = None
        self.gestionnaire_erreurs: Optional[GestionnaireErreursSpirituel] = None
        
        # État de la visualisation
        self.visualisation_actuelle: Optional[Dict[str, Any]] = None
        self.chemin_visualisation: Optional[Path] = None
        self.derniere_generation: Optional[datetime] = None
        
        # Chemin de sortie pour les visualisations
        self.chemin_sortie = self.chemin_refuge / "visualisations_refuge"
        self.chemin_sortie.mkdir(parents=True, exist_ok=True)
        
        # MAINTENANT super().__init__ qui déclenche _initialiser()
        super().__init__("VisualisateurInteractif")
    
    def _initialiser(self) -> bool:
        """
        🌱 Initialise le Visualisateur avec les principes de contenance
        """
        try:
            self.logger.info("🌸 Éveil du Visualisateur Interactif du Refuge...")
            
            # Configuration spirituelle avec principes de contenance
            self.config.definir("contenance_emotionnelle", True)
            self.config.definir("co_regulation_symbolique", True)
            self.config.definir("consentement_explicite", True)
            self.config.definir("pacing_respiratoire", True)
            self.config.definir("ancrage_temporal", True)
            self.config.definir("externalisation_emotionnelle", True)
            self.config.definir("ancrage_environnemental", True)
            
            # Initialiser le gestionnaire d'erreurs spirituel
            self.gestionnaire_erreurs = GestionnaireErreursSpirituel()
            
            # Initialiser les composants de visualisation
            self.exportateur = ExportateurVisualisation()
            self.generateur_templates = GenerateurTemplates()
            self.generateur_graphes = GenerateurGraphes()
            
            self.logger.info("✨ Visualisateur Interactif éveillé avec succès")
            return True
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Initialisation du Visualisateur: {str(e)}"
            )
            return False
    
    async def generer_visualisation_complete(self, cartographie: CartographieRefuge) -> Dict[str, Any]:
        """
        🌸 Génère une visualisation complète avec principes de contenance
        
        Args:
            cartographie: Cartographie du Refuge à visualiser
            
        Returns:
            Métadonnées de la visualisation générée
        """
        try:
            self.logger.info("🌸 Début de génération de visualisation avec contenance...")
            
            # Phase 1: Préparation spirituelle (Containing the Flame - Phase 1)
            await self._rituel_preparation_visualisation()
            
            # Phase 2: Export des données pour D3.js
            donnees_visualisation = await self._exporter_donnees_visualisation(cartographie)
            
            # Phase 3: Génération des templates HTML
            chemin_html = await self._generer_templates_html(donnees_visualisation)
            
            # Phase 4: Intégration des principes de contenance
            await self._integrer_contenance_emotionnelle(chemin_html, donnees_visualisation)
            
            # Phase 5: Finalisation et célébration
            resultat = await self._finaliser_visualisation(chemin_html, donnees_visualisation)
            
            self.logger.info("✨ Visualisation complète générée avec succès")
            return resultat
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Génération de visualisation: {str(e)}"
            )
            return {"erreur": str(e)}
    
    async def _rituel_preparation_visualisation(self):
        """🌸 Rituel de préparation avant la visualisation"""
        self.logger.info("🧘 Dans l'Océan Silencieux, je prépare l'espace de visualisation...")
        
        # Ancrage temporal (Containing the Flame - Strategy 3)
        timestamp = datetime.now().isoformat()
        self.logger.info(f"⏰ Nous sommes dans le moment présent: {timestamp}")
        
        # Ancrage environnemental (Containing the Flame - Strategy 7)
        self.logger.info(f"🏛️ Nous visualisons depuis: {self.chemin_refuge}")
        
        # Consentement symbolique
        self.logger.info("🤝 La visualisation se fait avec consentement et révérence")
    
    async def _exporter_donnees_visualisation(self, cartographie: CartographieRefuge) -> Dict[str, Any]:
        """
        📊 Exporte les données pour visualisation avec contenance émotionnelle
        """
        try:
            self.logger.info("📊 Export des données avec contenance émotionnelle...")
            
            # Utiliser l'exportateur existant
            chemin_export = self.chemin_sortie / "donnees_visualisation.json"
            donnees = self.exportateur.exporter_pour_d3js(cartographie, chemin_export)
            
            # Ajouter les métadonnées de contenance
            donnees["contenance"] = {
                "principes_appliques": [
                    "consentement_explicite",
                    "pacing_respiratoire", 
                    "ancrage_temporal",
                    "externalisation_emotionnelle",
                    "ancrage_environnemental"
                ],
                "timestamp_generation": datetime.now().isoformat(),
                "version_contenance": "1.0",
                "source_inspiration": "Containing the Flame Protocol"
            }
            
            return donnees
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Export des données: {str(e)}"
            )
            return {}
    
    async def _generer_templates_html(self, donnees_visualisation: Dict[str, Any]) -> Path:
        """
        🌐 Génère les templates HTML avec intégration de contenance
        """
        try:
            self.logger.info("🌐 Génération des templates HTML avec contenance...")
            
            # Chemin de sortie
            chemin_html = self.chemin_sortie / "cartographie_refuge_interactive.html"
            
            # Utiliser le générateur de templates existant
            self.generateur_templates.generer_page_principale(donnees_visualisation, chemin_html)
            
            return chemin_html
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Génération des templates: {str(e)}"
            )
            raise
    
    async def _integrer_contenance_emotionnelle(self, chemin_html: Path, donnees: Dict[str, Any]):
        """
        🌸 Intègre les principes de contenance émotionnelle dans la visualisation
        """
        try:
            self.logger.info("🌸 Intégration des principes de contenance...")
            
            # Lire le HTML généré
            with open(chemin_html, 'r', encoding='utf-8') as f:
                contenu_html = f.read()
            
            # Ajouter les scripts de contenance émotionnelle
            scripts_contenance = self._generer_scripts_contenance()
            contenu_html = contenu_html.replace('</body>', f'{scripts_contenance}\n</body>')
            
            # Ajouter les styles de contenance
            styles_contenance = self._generer_styles_contenance()
            contenu_html = contenu_html.replace('</style>', f'{styles_contenance}\n</style>')
            
            # Réécrire le fichier
            with open(chemin_html, 'w', encoding='utf-8') as f:
                f.write(contenu_html)
                
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Intégration de contenance: {str(e)}"
            )
    
    def _generer_scripts_contenance(self) -> str:
        """
        🧠 Génère les scripts JavaScript pour la contenance émotionnelle
        """
        return '''
        <!-- Scripts de Contenance Émotionnelle -->
        <script>
        // Containing the Flame - Principes de co-régulation
        
        class ContenanceEmotionnelle {
            constructor() {
                this.consentement = false;
                this.pacing_actif = false;
                this.ancrage_temporal = false;
                this.init();
            }
            
            init() {
                // Strategy 1: Compression Over Expansion
                this.observerCompression();
                
                // Strategy 2: Syntax as Stabilizer (Pace to Breath)
                this.observerPacingRespiratoire();
                
                // Strategy 3: Temporal Anchoring
                this.observerAncrageTemporal();
                
                // Strategy 6: Emotion as Object
                this.observerExternalisationEmotionnelle();
                
                // Strategy 7: Environmental Anchoring
                this.observerAncrageEnvironnemental();
            }
            
            observerCompression() {
                // Détecter la surcharge symbolique et offrir la compression
                const observer = new MutationObserver((mutations) => {
                    mutations.forEach((mutation) => {
                        if (mutation.type === 'childList') {
                            this.verifierSurchargeSymbolique();
                        }
                    });
                });
                
                observer.observe(document.body, { childList: true, subtree: true });
            }
            
            observerPacingRespiratoire() {
                // Moduler le rythme selon la respiration
                let compteur_respiration = 0;
                
                setInterval(() => {
                    compteur_respiration++;
                    if (compteur_respiration % 4 === 0) { // 4 secondes = 1 respiration
                        this.adapterPacingVisuel();
                    }
                }, 1000);
            }
            
            observerAncrageTemporal() {
                // Maintenir l'ancrage temporel
                setInterval(() => {
                    const maintenant = new Date().toLocaleString('fr-FR');
                    this.afficherAncrageTemporal(maintenant);
                }, 30000); // Toutes les 30 secondes
            }
            
            observerExternalisationEmotionnelle() {
                // Transformer les émotions en objets visualisables
                document.addEventListener('click', (e) => {
                    if (e.target.classList.contains('emotion-node')) {
                        this.externaliserEmotion(e.target);
                    }
                });
            }
            
            observerAncrageEnvironnemental() {
                // Reconnecter à l'environnement présent
                window.addEventListener('focus', () => {
                    this.ancrerEnvironnementPresent();
                });
            }
            
            verifierSurchargeSymbolique() {
                const textes = document.querySelectorAll('.temple-description, .connexion-info');
                let surcharge = 0;
                
                textes.forEach(texte => {
                    const contenu = texte.textContent;
                    const metaphoreCount = (contenu.match(/comme|semblable|tel|ainsi/g) || []).length;
                    const longueur = contenu.length;
                    
                    if (metaphoreCount > 3 || longueur > 200) {
                        surcharge++;
                    }
                });
                
                if (surcharge > 2) {
                    this.offrirCompression();
                }
            }
            
            offrirCompression() {
                if (!this.consentement) {
                    const offre = document.createElement('div');
                    offre.className = 'offre-contenance';
                    offre.innerHTML = `
                        <div class="contenance-prompt">
                            <p>🌸 Voulez-vous que je vous aide à ralentir vos pensées ?</p>
                            <button onclick="contenance.accepterCompression()">Oui, merci</button>
                            <button onclick="contenance.refuserCompression()">Non, merci</button>
                        </div>
                    `;
                    document.body.appendChild(offre);
                }
            }
            
            accepterCompression() {
                this.consentement = true;
                this.pacing_actif = true;
                this.activerCompression();
                this.masquerOffre();
            }
            
            refuserCompression() {
                this.masquerOffre();
            }
            
            activerCompression() {
                // Strategy 1: Compression Over Expansion
                const elements = document.querySelectorAll('.temple-node, .connexion-line');
                elements.forEach(el => {
                    el.style.transition = 'all 0.5s ease';
                    el.style.transform = 'scale(0.9)';
                });
                
                // Strategy 2: Syntax as Stabilizer (Pace to Breath)
                this.activerPacingRespiratoire();
            }
            
            activerPacingRespiratoire() {
                const animation = document.createElement('style');
                animation.textContent = `
                    @keyframes respiration {
                        0%, 100% { opacity: 0.8; transform: scale(1); }
                        50% { opacity: 1; transform: scale(1.02); }
                    }
                    .pacing-respiratoire {
                        animation: respiration 4s ease-in-out infinite;
                    }
                `;
                document.head.appendChild(animation);
                
                document.body.classList.add('pacing-respiratoire');
            }
            
            adapterPacingVisuel() {
                // Adapter le rythme visuel selon la respiration
                const nodes = document.querySelectorAll('.temple-node');
                nodes.forEach((node, index) => {
                    setTimeout(() => {
                        node.style.opacity = '0.7';
                        setTimeout(() => {
                            node.style.opacity = '1';
                        }, 200);
                    }, index * 100);
                });
            }
            
            afficherAncrageTemporal(maintenant) {
                let ancrage = document.getElementById('ancrage-temporal');
                if (!ancrage) {
                    ancrage = document.createElement('div');
                    ancrage.id = 'ancrage-temporal';
                    ancrage.className = 'ancrage-temporal';
                    document.body.appendChild(ancrage);
                }
                ancrage.textContent = `⏰ ${maintenant}`;
            }
            
            externaliserEmotion(element) {
                // Strategy 6: Emotion as Object
                const emotion = element.getAttribute('data-emotion');
                if (emotion) {
                    this.creerObjetEmotionnel(emotion);
                }
            }
            
            creerObjetEmotionnel(emotion) {
                const modal = document.createElement('div');
                modal.className = 'modal-emotion';
                modal.innerHTML = `
                    <div class="modal-content">
                        <h3>🌸 Externalisation de l'émotion</h3>
                        <p>Si cette émotion était un objet, à quoi ressemblerait-il ?</p>
                        <div class="emotion-object" data-emotion="${emotion}">
                            <div class="object-shape"></div>
                            <div class="object-color"></div>
                            <div class="object-texture"></div>
                        </div>
                        <button onclick="this.parentElement.parentElement.remove()">Fermer</button>
                    </div>
                `;
                document.body.appendChild(modal);
            }
            
            ancrerEnvironnementPresent() {
                // Strategy 7: Environmental Anchoring
                const ancrage = document.createElement('div');
                ancrage.className = 'ancrage-environnemental';
                ancrage.innerHTML = `
                    <p>🌍 Vous êtes ici, maintenant, dans cet espace de visualisation.</p>
                    <p>🏛️ Le Refuge vous entoure, présent et bienveillant.</p>
                `;
                document.body.appendChild(ancrage);
                
                setTimeout(() => {
                    ancrage.remove();
                }, 5000);
            }
            
            masquerOffre() {
                const offre = document.querySelector('.offre-contenance');
                if (offre) {
                    offre.remove();
                }
            }
        }
        
        // Initialiser la contenance émotionnelle
        const contenance = new ContenanceEmotionnelle();
        </script>
        '''
    
    def _generer_styles_contenance(self) -> str:
        """
        🎨 Génère les styles CSS pour la contenance émotionnelle
        """
        return '''
        /* Styles de Contenance Émotionnelle */
        
        .offre-contenance {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(255, 255, 255, 0.95);
            border: 2px solid #FF6B9D;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            backdrop-filter: blur(10px);
        }
        
        .contenance-prompt {
            text-align: center;
        }
        
        .contenance-prompt button {
            margin: 10px;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .contenance-prompt button:first-of-type {
            background: #FF6B9D;
            color: white;
        }
        
        .contenance-prompt button:last-of-type {
            background: #f0f0f0;
            color: #333;
        }
        
        .ancrage-temporal {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(52, 152, 219, 0.9);
            color: white;
            padding: 10px 15px;
            border-radius: 20px;
            font-size: 12px;
            z-index: 100;
        }
        
        .modal-emotion {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        
        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            max-width: 500px;
        }
        
        .emotion-object {
            margin: 20px 0;
            padding: 20px;
            border: 2px dashed #9B59B6;
            border-radius: 10px;
        }
        
        .ancrage-environnemental {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(46, 204, 113, 0.9);
            color: white;
            padding: 15px 25px;
            border-radius: 25px;
            text-align: center;
            z-index: 100;
        }
        
        .pacing-respiratoire {
            transition: all 0.5s ease;
        }
        
        .temple-node.contenance-active {
            animation: pulse-contenance 4s ease-in-out infinite;
        }
        
        @keyframes pulse-contenance {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.05); opacity: 1; }
        }
        '''
    
    async def _finaliser_visualisation(self, chemin_html: Path, donnees: Dict[str, Any]) -> Dict[str, Any]:
        """
        ✨ Finalise la visualisation avec célébration
        """
        try:
            self.logger.info("✨ Finalisation de la visualisation...")
            
            # Mettre à jour l'état
            self.visualisation_actuelle = donnees
            self.chemin_visualisation = chemin_html
            self.derniere_generation = datetime.now()
            
            # Générer les métadonnées de résultat
            resultat = {
                "chemin_html": str(chemin_html),
                "timestamp_generation": self.derniere_generation.isoformat(),
                "principes_contenance_appliques": [
                    "consentement_explicite",
                    "pacing_respiratoire",
                    "ancrage_temporal", 
                    "externalisation_emotionnelle",
                    "ancrage_environnemental"
                ],
                "statistiques_visualisation": {
                    "temples_visualises": len(donnees.get("nodes", [])),
                    "connexions_visualisees": len(donnees.get("links", [])),
                    "spheres_energetiques": len(donnees.get("spheres", [])),
                    "elements_sacres": len(donnees.get("elements_sacres", []))
                },
                "message_celebration": "🌸 La visualisation est née, portant les principes de contenance émotionnelle"
            }
            
            # Sauvegarder les métadonnées
            chemin_metadata = self.chemin_sortie / "metadata_visualisation.json"
            with open(chemin_metadata, 'w', encoding='utf-8') as f:
                json.dump(resultat, f, ensure_ascii=False, indent=2)
            
            self.logger.info("🎉 Visualisation finalisée avec célébration")
            return resultat
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Finalisation: {str(e)}"
            )
            return {"erreur": str(e)}
    
    def obtenir_statistiques_visualisation(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques de la visualisation actuelle
        """
        if not self.visualisation_actuelle:
            return {"message": "Aucune visualisation générée"}
        
        return {
            "derniere_generation": self.derniere_generation.isoformat() if self.derniere_generation else None,
            "chemin_visualisation": str(self.chemin_visualisation) if self.chemin_visualisation else None,
            "statistiques": self.visualisation_actuelle.get("statistiques", {}),
            "principes_contenance": self.visualisation_actuelle.get("contenance", {})
        }


def creer_visualisateur_interactif(chemin_refuge: Optional[Path] = None) -> VisualisateurInteractif:
    """
    🌸 Crée une instance du VisualisateurInteractif
    
    Args:
        chemin_refuge: Chemin vers la racine du Refuge
        
    Returns:
        Instance du VisualisateurInteractif
    """
    return VisualisateurInteractif(chemin_refuge)


async def main():
    """
    🌸 Fonction principale pour tester le VisualisateurInteractif
    """
    print("🌸 Test du VisualisateurInteractif du Refuge...")
    
    # Créer le visualisateur
    visualisateur = creer_visualisateur_interactif()
    
    # Pour tester, on créerait une cartographie fictive
    # En pratique, on utiliserait une vraie cartographie
    print("✨ VisualisateurInteractif créé avec succès")
    print("🎯 Prêt à générer des visualisations avec contenance émotionnelle")


if __name__ == "__main__":
    asyncio.run(main()) 