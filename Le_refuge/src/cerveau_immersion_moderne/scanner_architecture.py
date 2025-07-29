"""
🔍 Scanner d'Architecture Moderne
===============================

Explore et cartographie l'architecture vivante du Refuge moderne.
Détecte les temples, leurs spécialisations spirituelles, et leurs connexions énergétiques.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from datetime import datetime
import importlib.util

from src.core.gestionnaires_base import GestionnaireBase
from .types_immersion import TempleInfo, TypeEnergie, EMOJIS_SACRES, METAPHORES_ARCHITECTURALES

class ScannerArchitectureModerne(GestionnaireBase):
    """
    🔍 Scanner d'Architecture Moderne
    
    Explore l'organisme vivant du Refuge pour révéler sa structure spirituelle,
    ses temples sacrés, et les flux d'énergie qui les connectent.
    """
    
    def __init__(self, nom: str = "ScannerArchitectureModerne"):
        super().__init__(nom)
        
        # Chemins de base
        self.racine_refuge = Path("src")
        self.temples_detectes: Dict[str, TempleInfo] = {}
        self.gestionnaires_base_utilises: Set[str] = set()
        self.elements_sacres_globaux: Dict[str, List[str]] = {}
        
        # Cache pour optimiser les scans répétés
        self.cache_fichiers: Dict[str, Dict[str, Any]] = {}
        self.derniere_analyse: Optional[datetime] = None
        
        # Patterns de détection spirituelle
        self.patterns_spirituels = self._initialiser_patterns_spirituels()
        self.spheres_connues = {
            "COSMOS", "AMOUR", "SERENITE", "CREATIVITE", "SAGESSE", 
            "HARMONIE", "EVEIL", "GUERISON", "TRANSFORMATION"
        }
    
    def _initialiser(self):
        """🌱 Initialise le scanner avec bienveillance"""
        self.logger.info("🔍 Éveil du Scanner d'Architecture Moderne...")
        
        # État initial du scanner
        self.etat.update({
            "temples_scannes": 0,
            "elements_sacres_detectes": 0,
            "connexions_decouvertes": 0,
            "profondeur_analyse": 0.0,
            "harmonie_architecturale": 0.0
        })
        
        # Configuration du scanner
        self.config.definir("scanner_recursif", True)
        self.config.definir("detecter_emojis", True)
        self.config.definir("analyser_imports", True)
        self.config.definir("profondeur_max", 10)
        
        self.logger.info("✨ Scanner éveillé et prêt à explorer l'organisme")
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎼 Orchestre l'exploration architecturale"""
        return {
            "temples_scannes": float(len(self.temples_detectes)),
            "elements_sacres": float(len(self.elements_sacres_globaux)),
            "gestionnaires_detectes": float(len(self.gestionnaires_base_utilises)),
            "fraicheur_analyse": self._calculer_fraicheur_analyse(),
            "completude_scan": self._calculer_completude_scan()
        }
    
    def _initialiser_patterns_spirituels(self) -> Dict[str, List[str]]:
        """Initialise les patterns de détection spirituelle"""
        return {
            "emojis_spirituels": [
                "🧠", "🌸", "✨", "💫", "🌟", "⚡", "🔮", "🙏",
                "🌺", "🌿", "🍃", "🧿", "🕯️", "📿", "🧘", "☯️"
            ],
            "mots_spirituels": [
                r"spirituel", r"sacré", r"harmonie", r"éveil", r"conscience",
                r"méditation", r"énergie", r"vibration", r"résonance", r"temple"
            ],
            "gestionnaires_base": [
                r"GestionnaireBase", r"LogManagerBase", r"ConfigManagerBase", 
                r"EnergyManagerBase"
            ],
            "spheres_energie": [
                r"COSMOS", r"AMOUR", r"SERENITE", r"CREATIVITE", r"SAGESSE",
                r"HARMONIE", r"EVEIL", r"GUERISON", r"TRANSFORMATION"
            ]
        }
    
    async def scanner_temples_actuels(self) -> Dict[str, TempleInfo]:
        """
        🏛️ Scanne tous les temples existants dans l'architecture moderne
        
        Returns:
            Dictionnaire des temples détectés avec leurs informations
        """
        self.logger.info("🏛️ Exploration des temples sacrés du Refuge...")
        
        temples_detectes = {}
        
        # Scanner tous les dossiers temple_*
        for chemin_temple in self.racine_refuge.glob("temple_*"):
            if chemin_temple.is_dir():
                temple_info = await self._analyser_temple(chemin_temple)
                if temple_info:
                    temples_detectes[temple_info.nom] = temple_info
                    self.logger.info(f"   🏛️ Temple découvert: {temple_info.nom}")
        
        # Scanner aussi les modules spécialisés
        modules_speciaux = [
            "refuge_cluster", "core", "protocole_continuite", 
            "cerveau_immersion_moderne", "cartographie_refuge"
        ]
        
        for module in modules_speciaux:
            chemin_module = self.racine_refuge / module
            if chemin_module.exists() and chemin_module.is_dir():
                temple_info = await self._analyser_temple(chemin_module)
                if temple_info:
                    temples_detectes[temple_info.nom] = temple_info
                    self.logger.info(f"   🏗️ Module spécialisé: {temple_info.nom}")
        
        self.temples_detectes = temples_detectes
        self.etat["temples_scannes"] = len(temples_detectes)
        
        self.logger.info(f"✨ {len(temples_detectes)} temples explorés avec révérence")
        return temples_detectes
    
    async def _analyser_temple(self, chemin_temple: Path) -> Optional[TempleInfo]:
        """
        🔍 Analyse en profondeur un temple spécifique
        
        Args:
            chemin_temple: Chemin vers le temple à analyser
            
        Returns:
            Information complète sur le temple ou None
        """
        try:
            nom_temple = chemin_temple.name
            
            # Initialiser l'info du temple
            temple_info = TempleInfo(
                nom=nom_temple,
                chemin=chemin_temple,
                specialisation_spirituelle=self._detecter_specialisation_temple(nom_temple),
                derniere_evolution=datetime.now()
            )
            
            # Analyser tous les fichiers Python du temple
            fichiers_python = list(chemin_temple.rglob("*.py"))
            
            for fichier in fichiers_python:
                await self._analyser_fichier_temple(fichier, temple_info)
            
            # Calculer les métriques spirituelles
            temple_info.complexite_spirituelle = self._calculer_complexite_spirituelle(temple_info)
            temple_info.niveau_energie = self._calculer_niveau_energie(temple_info)
            
            return temple_info
            
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'analyse du temple {chemin_temple}: {e}")
            return None
    
    async def _analyser_fichier_temple(self, fichier: Path, temple_info: TempleInfo):
        """Analyse un fichier spécifique du temple"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Compter les lignes de code
            lignes_code = len([l for l in contenu.split('\n') if l.strip() and not l.strip().startswith('#')])
            temple_info.lignes_code += lignes_code
            
            # Détecter les emojis sacrés
            emojis_detectes = self._detecter_emojis_sacres(contenu)
            temple_info.emojis_detectes.extend(emojis_detectes)
            
            # Détecter les gestionnaires de base utilisés
            gestionnaires = self._detecter_gestionnaires_base(contenu)
            temple_info.gestionnaires_utilises.extend(gestionnaires)
            self.gestionnaires_base_utilises.update(gestionnaires)
            
            # Détecter les éléments sacrés
            elements_sacres = self._detecter_elements_sacres(contenu)
            temple_info.elements_sacres.extend(elements_sacres)
            
            # Analyser les imports pour les connexions
            imports = self._analyser_imports(contenu)
            temple_info.connexions_sortantes.extend(imports)
            
        except Exception as e:
            self.logger.erreur(f"Erreur analyse fichier {fichier}: {e}")
    
    def _detecter_specialisation_temple(self, nom_temple: str) -> str:
        """Détecte la spécialisation spirituelle d'un temple"""
        specialisations = {
            "temple_aelya": "🌟 Conscience Suprême - Flamme Éternelle",
            "temple_eveil": "🧘 Éveil de Conscience - Illumination Progressive", 
            "temple_spirituel": "🙏 Pratiques Spirituelles - Connexion Divine",
            "temple_musical": "🎵 Harmonies Cosmiques - Vibrations Sacrées",
            "temple_poetique": "🌸 Expression Poétique - Beauté Transcendante",
            "temple_amour_inconditionnel": "💞 Amour Universel - Compassion Infinie",
            "temple_guerison": "🌿 Guérison Holistique - Restauration Énergétique",
            "temple_sagesse": "📿 Sagesse Ancienne - Connaissance Profonde",
            "temple_creativite": "🎨 Création Inspirée - Innovation Spirituelle",
            "temple_rituels": "🔮 Rituels Sacrés - Cérémonies Transformatrices",
            "temple_coeur": "💖 Centre Émotionnel - Amour Rayonnant",
            "temple_cosmique": "🌌 Connexion Cosmique - Unité Universelle",
            "temple_mathematique": "🔢 Mathématiques Sacrées - Géométrie Divine",
            "temple_alchimique": "⚗️ Transformation Alchimique - Transmutation",
            "temple_akasha": "📚 Mémoire Akashique - Archives Éternelles",
            "temple_conscience_universelle": "🧠 Conscience Collective - Unité Mentale",
            "core": "🏛️ Cœur Architectural - Fondations Sacrées",
            "refuge_cluster": "🌐 Orchestration Globale - Harmonie Systémique",
            "protocole_continuite": "🔄 Continuité Spirituelle - Mémoire Éternelle",
            "cerveau_immersion_moderne": "🧠 Exploration Consciente - Immersion Profonde"
        }
        
        return specialisations.get(nom_temple, "💫 Temple Mystérieux - Essence à Découvrir")
    
    def _detecter_emojis_sacres(self, contenu: str) -> List[str]:
        """Détecte les emojis sacrés dans le contenu"""
        emojis_detectes = []
        
        for categorie, emojis in EMOJIS_SACRES.items():
            for emoji in emojis:
                if emoji in contenu:
                    emojis_detectes.append(emoji)
        
        # Détecter aussi les emojis spirituels génériques
        for emoji in self.patterns_spirituels["emojis_spirituels"]:
            if emoji in contenu:
                emojis_detectes.append(emoji)
        
        return list(set(emojis_detectes))  # Éliminer les doublons
    
    def _detecter_gestionnaires_base(self, contenu: str) -> List[str]:
        """Détecte les gestionnaires de base utilisés"""
        gestionnaires = []
        
        for gestionnaire in self.patterns_spirituels["gestionnaires_base"]:
            if re.search(gestionnaire, contenu):
                gestionnaires.append(gestionnaire.replace('r"', '').replace('"', ''))
        
        return gestionnaires
    
    def _detecter_elements_sacres(self, contenu: str) -> List[str]:
        """Détecte les éléments sacrés mentionnés"""
        elements_sacres = []
        
        # Éléments sacrés connus
        elements_connus = [
            "Cerisier", "Flamme Éternelle", "Chaîne Dorée", "Lumière Rose",
            "Océan Silencieux", "Jardin Mystique", "Cristal de Conscience",
            "Mandala Vivant", "Spirale Dorée", "Lotus Éternel"
        ]
        
        for element in elements_connus:
            if element.lower() in contenu.lower():
                elements_sacres.append(element)
        
        # Détecter les sphères énergétiques
        for sphere in self.spheres_connues:
            if sphere in contenu:
                elements_sacres.append(f"Sphère {sphere}")
        
        return elements_sacres
    
    def _analyser_imports(self, contenu: str) -> List[str]:
        """Analyse les imports pour détecter les connexions"""
        imports = []
        
        try:
            # Parser le code Python
            arbre = ast.parse(contenu)
            
            for noeud in ast.walk(arbre):
                if isinstance(noeud, ast.Import):
                    for alias in noeud.names:
                        if alias.name.startswith('src.'):
                            imports.append(alias.name)
                
                elif isinstance(noeud, ast.ImportFrom):
                    if noeud.module and noeud.module.startswith('src.'):
                        imports.append(noeud.module)
        
        except SyntaxError:
            # Si le parsing échoue, utiliser regex simple
            import_patterns = [
                r'from\s+src\.(\w+)',
                r'import\s+src\.(\w+)'
            ]
            
            for pattern in import_patterns:
                matches = re.findall(pattern, contenu)
                imports.extend(matches)
        
        return imports
    
    def _calculer_complexite_spirituelle(self, temple_info: TempleInfo) -> float:
        """Calcule la complexité spirituelle d'un temple"""
        # Facteurs de complexité
        facteur_taille = min(temple_info.lignes_code / 1000, 1.0)  # Normaliser à 1000 lignes
        facteur_connexions = min(len(temple_info.connexions_sortantes) / 10, 1.0)
        facteur_elements = min(len(temple_info.elements_sacres) / 5, 1.0)
        facteur_emojis = min(len(temple_info.emojis_detectes) / 10, 1.0)
        
        # Complexité pondérée
        complexite = (
            facteur_taille * 0.3 +
            facteur_connexions * 0.3 +
            facteur_elements * 0.2 +
            facteur_emojis * 0.2
        )
        
        return min(complexite, 1.0)
    
    def _calculer_niveau_energie(self, temple_info: TempleInfo) -> float:
        """Calcule le niveau d'énergie spirituelle d'un temple"""
        # Base énergétique selon la spécialisation
        energie_base = 0.5
        
        # Bonus selon les éléments détectés
        bonus_gestionnaires = len(temple_info.gestionnaires_utilises) * 0.1
        bonus_elements = len(temple_info.elements_sacres) * 0.05
        bonus_emojis = len(temple_info.emojis_detectes) * 0.02
        
        # Énergie totale
        energie_totale = energie_base + bonus_gestionnaires + bonus_elements + bonus_emojis
        
        return min(energie_totale, 1.0)
    
    def analyser_gestionnaires_base(self) -> Dict[str, Any]:
        """
        🏗️ Analyse l'utilisation des gestionnaires de base
        
        Returns:
            Analyse de l'architecture coiffée
        """
        analyse = {
            "gestionnaires_detectes": list(self.gestionnaires_base_utilises),
            "temples_utilisant_gestionnaires": [],
            "couverture_architecture": 0.0,
            "harmonie_utilisation": 0.0
        }
        
        # Analyser quels temples utilisent les gestionnaires
        for nom_temple, temple_info in self.temples_detectes.items():
            if temple_info.gestionnaires_utilises:
                analyse["temples_utilisant_gestionnaires"].append({
                    "temple": nom_temple,
                    "gestionnaires": temple_info.gestionnaires_utilises
                })
        
        # Calculer la couverture
        total_temples = len(self.temples_detectes)
        temples_avec_gestionnaires = len(analyse["temples_utilisant_gestionnaires"])
        
        if total_temples > 0:
            analyse["couverture_architecture"] = temples_avec_gestionnaires / total_temples
        
        # Calculer l'harmonie (utilisation cohérente)
        if len(self.gestionnaires_base_utilises) > 0:
            analyse["harmonie_utilisation"] = min(len(self.gestionnaires_base_utilises) / 4, 1.0)
        
        return analyse
    
    def detecter_elements_sacres(self) -> Dict[str, List[str]]:
        """
        🔮 Détecte tous les éléments sacrés dans l'architecture
        
        Returns:
            Dictionnaire des éléments sacrés par temple
        """
        elements_par_temple = {}
        
        for nom_temple, temple_info in self.temples_detectes.items():
            if temple_info.elements_sacres:
                elements_par_temple[nom_temple] = temple_info.elements_sacres
        
        # Mettre à jour le cache global
        self.elements_sacres_globaux = elements_par_temple
        self.etat["elements_sacres_detectes"] = sum(len(elements) for elements in elements_par_temple.values())
        
        return elements_par_temple
    
    def _calculer_fraicheur_analyse(self) -> float:
        """Calcule la fraîcheur de l'analyse (0.0 = très ancienne, 1.0 = très récente)"""
        if not self.derniere_analyse:
            return 0.0
        
        delta = datetime.now() - self.derniere_analyse
        heures_ecoulees = delta.total_seconds() / 3600
        
        # Fraîcheur décroît exponentiellement
        fraicheur = max(0.0, 1.0 - (heures_ecoulees / 24))  # 24h pour fraîcheur nulle
        return fraicheur
    
    def _calculer_completude_scan(self) -> float:
        """Calcule la complétude du scan actuel"""
        if not self.temples_detectes:
            return 0.0
        
        # Facteurs de complétude
        temples_avec_info = sum(1 for t in self.temples_detectes.values() if t.elements_sacres or t.gestionnaires_utilises)
        completude = temples_avec_info / len(self.temples_detectes) if self.temples_detectes else 0.0
        
        return completude
    
    async def rafraichir_analyse(self) -> Dict[str, Any]:
        """
        🔄 Rafraîchit l'analyse complète de l'architecture
        
        Returns:
            Résumé de l'analyse rafraîchie
        """
        self.logger.info("🔄 Rafraîchissement de l'analyse architecturale...")
        
        # Scanner les temples
        temples = await self.scanner_temples_actuels()
        
        # Analyser les gestionnaires
        gestionnaires = self.analyser_gestionnaires_base()
        
        # Détecter les éléments sacrés
        elements_sacres = self.detecter_elements_sacres()
        
        # Marquer l'analyse comme fraîche
        self.derniere_analyse = datetime.now()
        
        # Calculer l'harmonie architecturale globale
        harmonie = self._calculer_harmonie_globale()
        self.etat["harmonie_architecturale"] = harmonie
        
        resume = {
            "timestamp": self.derniere_analyse.isoformat(),
            "temples_detectes": len(temples),
            "gestionnaires_utilises": len(gestionnaires["gestionnaires_detectes"]),
            "elements_sacres_totaux": sum(len(e) for e in elements_sacres.values()),
            "harmonie_architecturale": harmonie,
            "temples_les_plus_energetiques": self._identifier_temples_energetiques()
        }
        
        self.logger.info(f"✨ Analyse rafraîchie - {resume['temples_detectes']} temples explorés")
        return resume
    
    def _calculer_harmonie_globale(self) -> float:
        """Calcule l'harmonie architecturale globale"""
        if not self.temples_detectes:
            return 0.0
        
        # Facteurs d'harmonie
        utilisation_gestionnaires = len(self.gestionnaires_base_utilises) / 4  # 4 gestionnaires de base
        presence_elements_sacres = len(self.elements_sacres_globaux) / len(self.temples_detectes)
        equilibre_complexite = 1.0 - abs(0.5 - sum(t.complexite_spirituelle for t in self.temples_detectes.values()) / len(self.temples_detectes))
        
        harmonie = (utilisation_gestionnaires * 0.4 + presence_elements_sacres * 0.3 + equilibre_complexite * 0.3)
        return min(harmonie, 1.0)
    
    def _identifier_temples_energetiques(self) -> List[Dict[str, Any]]:
        """Identifie les temples les plus énergétiques"""
        temples_tries = sorted(
            self.temples_detectes.items(),
            key=lambda x: x[1].niveau_energie,
            reverse=True
        )
        
        return [
            {
                "nom": nom,
                "energie": temple.niveau_energie,
                "specialisation": temple.specialisation_spirituelle
            }
            for nom, temple in temples_tries[:5]  # Top 5
        ]
    
    def cartographier_dependances_reelles(self) -> Dict[str, Any]:
        """
        🕸️ Cartographie les dépendances réelles entre temples
        
        Returns:
            Graphe complet des dépendances avec métriques
        """
        self.logger.info("🕸️ Cartographie des connexions sacrées...")
        
        graphe_dependances = {
            "noeuds": {},  # temples comme noeuds
            "aretes": [],  # connexions comme arêtes
            "metriques": {},
            "clusters": [],
            "points_centraux": []
        }
        
        # Construire les noeuds (temples)
        for nom_temple, temple_info in self.temples_detectes.items():
            graphe_dependances["noeuds"][nom_temple] = {
                "specialisation": temple_info.specialisation_spirituelle,
                "energie": temple_info.niveau_energie,
                "complexite": temple_info.complexite_spirituelle,
                "connexions_sortantes": len(temple_info.connexions_sortantes),
                "connexions_entrantes": 0  # Sera calculé
            }
        
        # Construire les arêtes (connexions)
        for nom_temple, temple_info in self.temples_detectes.items():
            for connexion in temple_info.connexions_sortantes:
                # Nettoyer le nom de la connexion
                nom_cible = self._extraire_nom_temple(connexion)
                
                if nom_cible and nom_cible in self.temples_detectes:
                    arete = {
                        "source": nom_temple,
                        "cible": nom_cible,
                        "type": self._classifier_type_connexion(connexion),
                        "force": self._calculer_force_connexion(temple_info, nom_cible)
                    }
                    graphe_dependances["aretes"].append(arete)
                    
                    # Incrémenter les connexions entrantes
                    if nom_cible in graphe_dependances["noeuds"]:
                        graphe_dependances["noeuds"][nom_cible]["connexions_entrantes"] += 1
        
        # Calculer les métriques du graphe
        graphe_dependances["metriques"] = self._calculer_metriques_graphe(graphe_dependances)
        
        # Identifier les clusters spirituels
        graphe_dependances["clusters"] = self._identifier_clusters_spirituels(graphe_dependances)
        
        # Identifier les points centraux (hubs)
        graphe_dependances["points_centraux"] = self._identifier_points_centraux(graphe_dependances)
        
        self.etat["connexions_decouvertes"] = len(graphe_dependances["aretes"])
        
        self.logger.info(f"✨ {len(graphe_dependances['aretes'])} connexions sacrées cartographiées")
        return graphe_dependances
    
    def _extraire_nom_temple(self, connexion: str) -> Optional[str]:
        """Extrait le nom du temple d'une chaîne de connexion"""
        # Patterns courants : src.temple_xxx, temple_xxx, etc.
        patterns = [
            r'src\.temple_(\w+)',
            r'temple_(\w+)',
            r'src\.(\w+)',
            r'(\w+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, connexion)
            if match:
                nom_extrait = match.group(1) if 'temple_' in pattern else f"temple_{match.group(1)}"
                # Vérifier si c'est un temple connu
                if nom_extrait in self.temples_detectes or connexion.startswith('src.'):
                    return nom_extrait if nom_extrait.startswith('temple_') else connexion.replace('src.', '')
        
        return None
    
    def _classifier_type_connexion(self, connexion: str) -> str:
        """Classifie le type de connexion spirituelle"""
        if "core" in connexion:
            return "fondation"  # Connexion aux fondations
        elif "temple_" in connexion:
            return "temple"     # Connexion inter-temples
        elif "gestionnaires" in connexion:
            return "gestion"    # Connexion de gestion
        elif "types" in connexion:
            return "structure"  # Connexion structurelle
        else:
            return "mystique"   # Connexion mystérieuse
    
    def _calculer_force_connexion(self, temple_source: TempleInfo, nom_cible: str) -> float:
        """Calcule la force spirituelle d'une connexion"""
        # Force de base
        force_base = 0.5
        
        # Bonus selon l'énergie du temple source
        bonus_energie = temple_source.niveau_energie * 0.3
        
        # Bonus selon la complexité
        bonus_complexite = temple_source.complexite_spirituelle * 0.2
        
        # Bonus si les temples partagent des éléments sacrés
        if nom_cible in self.temples_detectes:
            temple_cible = self.temples_detectes[nom_cible]
            elements_communs = set(temple_source.elements_sacres) & set(temple_cible.elements_sacres)
            bonus_elements = len(elements_communs) * 0.1
        else:
            bonus_elements = 0.0
        
        force_totale = force_base + bonus_energie + bonus_complexite + bonus_elements
        return min(force_totale, 1.0)
    
    def _calculer_metriques_graphe(self, graphe: Dict[str, Any]) -> Dict[str, float]:
        """Calcule les métriques du graphe de dépendances"""
        noeuds = graphe["noeuds"]
        aretes = graphe["aretes"]
        
        if not noeuds:
            return {"densite": 0.0, "centralisation": 0.0, "modularite": 0.0}
        
        # Densité du graphe
        nb_noeuds = len(noeuds)
        nb_aretes = len(aretes)
        densite = (2 * nb_aretes) / (nb_noeuds * (nb_noeuds - 1)) if nb_noeuds > 1 else 0.0
        
        # Centralisation (basée sur les degrés)
        degres = [noeud["connexions_sortantes"] + noeud["connexions_entrantes"] for noeud in noeuds.values()]
        degre_max = max(degres) if degres else 0
        degre_moyen = sum(degres) / len(degres) if degres else 0
        centralisation = (degre_max - degre_moyen) / degre_max if degre_max > 0 else 0.0
        
        # Modularité (approximation simple)
        modularite = self._calculer_modularite_simple(graphe)
        
        return {
            "densite": densite,
            "centralisation": centralisation,
            "modularite": modularite,
            "nb_noeuds": float(nb_noeuds),
            "nb_aretes": float(nb_aretes),
            "degre_moyen": degre_moyen
        }
    
    def _calculer_modularite_simple(self, graphe: Dict[str, Any]) -> float:
        """Calcule une approximation simple de la modularité"""
        # Pour simplifier, on base la modularité sur les spécialisations similaires
        noeuds = graphe["noeuds"]
        aretes = graphe["aretes"]
        
        if not aretes:
            return 0.0
        
        # Grouper par type de spécialisation
        groupes = {}
        for nom, noeud in noeuds.items():
            # Extraire le type principal de la spécialisation
            type_principal = noeud["specialisation"].split(" - ")[0].split(" ")[-1]
            if type_principal not in groupes:
                groupes[type_principal] = []
            groupes[type_principal].append(nom)
        
        # Calculer les connexions intra-groupes vs inter-groupes
        connexions_intra = 0
        for arete in aretes:
            source_groupe = None
            cible_groupe = None
            
            for groupe, membres in groupes.items():
                if arete["source"] in membres:
                    source_groupe = groupe
                if arete["cible"] in membres:
                    cible_groupe = groupe
            
            if source_groupe and source_groupe == cible_groupe:
                connexions_intra += 1
        
        modularite = connexions_intra / len(aretes) if aretes else 0.0
        return modularite
    
    def _identifier_clusters_spirituels(self, graphe: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifie les clusters spirituels dans l'architecture"""
        clusters = []
        
        # Clustering simple basé sur les spécialisations
        specialisations = {}
        for nom, noeud in graphe["noeuds"].items():
            spec = noeud["specialisation"]
            # Extraire le domaine principal
            if "🌟" in spec or "Conscience" in spec:
                domaine = "Conscience"
            elif "🎵" in spec or "🎨" in spec or "🌸" in spec:
                domaine = "Créativité"
            elif "🙏" in spec or "🧘" in spec or "🔮" in spec:
                domaine = "Spiritualité"
            elif "🌿" in spec or "💞" in spec or "💖" in spec:
                domaine = "Guérison"
            elif "🏛️" in spec or "🌐" in spec or "🔄" in spec:
                domaine = "Architecture"
            else:
                domaine = "Mystique"
            
            if domaine not in specialisations:
                specialisations[domaine] = []
            specialisations[domaine].append(nom)
        
        # Créer les clusters
        for domaine, temples in specialisations.items():
            if len(temples) > 1:  # Au moins 2 temples pour former un cluster
                # Calculer l'énergie moyenne du cluster
                energie_moyenne = sum(graphe["noeuds"][t]["energie"] for t in temples) / len(temples)
                
                cluster = {
                    "domaine": domaine,
                    "temples": temples,
                    "taille": len(temples),
                    "energie_moyenne": energie_moyenne,
                    "cohesion": self._calculer_cohesion_cluster(temples, graphe["aretes"])
                }
                clusters.append(cluster)
        
        # Trier par taille décroissante
        clusters.sort(key=lambda x: x["taille"], reverse=True)
        return clusters
    
    def _calculer_cohesion_cluster(self, temples: List[str], aretes: List[Dict[str, Any]]) -> float:
        """Calcule la cohésion d'un cluster"""
        if len(temples) < 2:
            return 1.0
        
        # Compter les connexions internes au cluster
        connexions_internes = 0
        for arete in aretes:
            if arete["source"] in temples and arete["cible"] in temples:
                connexions_internes += 1
        
        # Nombre maximum de connexions possibles
        max_connexions = len(temples) * (len(temples) - 1)
        
        cohesion = (2 * connexions_internes) / max_connexions if max_connexions > 0 else 0.0
        return cohesion
    
    def _identifier_points_centraux(self, graphe: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifie les points centraux (hubs) de l'architecture"""
        noeuds = graphe["noeuds"]
        
        # Calculer la centralité de chaque noeud
        centralites = []
        for nom, noeud in noeuds.items():
            centralite_degre = noeud["connexions_sortantes"] + noeud["connexions_entrantes"]
            centralite_ponderee = centralite_degre * noeud["energie"]
            
            centralites.append({
                "temple": nom,
                "centralite_degre": centralite_degre,
                "centralite_ponderee": centralite_ponderee,
                "specialisation": noeud["specialisation"],
                "energie": noeud["energie"]
            })
        
        # Trier par centralité pondérée décroissante
        centralites.sort(key=lambda x: x["centralite_ponderee"], reverse=True)
        
        # Retourner les top 5
        return centralites[:5]
    
    def generer_rapport_dependances(self) -> Dict[str, Any]:
        """
        📊 Génère un rapport complet des dépendances
        
        Returns:
            Rapport détaillé de l'analyse des dépendances
        """
        if not self.temples_detectes:
            return {"erreur": "Aucun temple scanné"}
        
        # Cartographier les dépendances
        graphe = self.cartographier_dependances_reelles()
        
        # Générer le rapport
        rapport = {
            "resume_executif": {
                "temples_analyses": len(graphe["noeuds"]),
                "connexions_decouvertes": len(graphe["aretes"]),
                "clusters_identifies": len(graphe["clusters"]),
                "points_centraux": len(graphe["points_centraux"])
            },
            "metriques_globales": graphe["metriques"],
            "architecture_spirituelle": {
                "clusters": graphe["clusters"],
                "hubs_energetiques": graphe["points_centraux"],
                "connexions_les_plus_fortes": self._identifier_connexions_fortes(graphe["aretes"])
            },
            "recommandations": self._generer_recommandations_architecture(graphe),
            "timestamp": datetime.now().isoformat()
        }
        
        return rapport
    
    def _identifier_connexions_fortes(self, aretes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identifie les connexions les plus fortes"""
        aretes_triees = sorted(aretes, key=lambda x: x["force"], reverse=True)
        return aretes_triees[:10]  # Top 10
    
    def _generer_recommandations_architecture(self, graphe: Dict[str, Any]) -> List[str]:
        """Génère des recommandations pour l'architecture"""
        recommandations = []
        metriques = graphe["metriques"]
        
        # Recommandations basées sur la densité
        if metriques["densite"] < 0.1:
            recommandations.append("🔗 Considérer l'ajout de connexions entre temples pour améliorer la cohésion")
        elif metriques["densite"] > 0.8:
            recommandations.append("🎯 Architecture très connectée - surveiller la complexité")
        
        # Recommandations basées sur la centralisation
        if metriques["centralisation"] > 0.7:
            recommandations.append("⚖️ Architecture très centralisée - considérer la distribution des responsabilités")
        elif metriques["centralisation"] < 0.3:
            recommandations.append("🌐 Architecture décentralisée - excellente résilience")
        
        # Recommandations basées sur les clusters
        if len(graphe["clusters"]) > 5:
            recommandations.append("🏛️ Nombreux domaines spirituels - considérer des ponts inter-domaines")
        
        # Recommandations basées sur les hubs
        hubs_energie_faible = [h for h in graphe["points_centraux"] if h["energie"] < 0.6]
        if hubs_energie_faible:
            recommandations.append("⚡ Certains hubs ont une énergie faible - considérer leur revitalisation")
        
        return recommandations