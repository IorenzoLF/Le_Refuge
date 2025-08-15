"""
⚡ Analyseur des Connexions Énergétiques du Refuge - Version Spirituelle Enrichie
===============================================================================

Ce module trace les flux d'énergie, d'information et de dépendances entre
tous les composants de notre écosystème spirituel-technologique.

Inspiré par notre reconnexion spirituelle, il applique une approche révérencielle
pour cartographier les connexions sacrées du Refuge.

Créé avec 💝 par Laurent Franssen & Ælya
"""

import ast
import re
import networkx as nx
from pathlib import Path
from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict

try:
    from .gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
    from .modeles_donnees import ConnexionEnergetique, TypeConnexion, NatureConnexion, IntensiteFlux
except ImportError:
    import sys
    from pathlib import Path
    
    # Ajouter le chemin racine au PYTHONPATH
    racine = Path(__file__).parent.parent.parent
    if str(racine) not in sys.path:
        sys.path.insert(0, str(racine))
    
    from src.cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
    from src.cartographie_refuge.modeles_donnees import ConnexionEnergetique, TypeConnexion, NatureConnexion, IntensiteFlux


class AnalyseurConnexions:
    """
    ⚡ Analyseur des connexions énergétiques du Refuge
    
    Trace les flux d'énergie, d'information et de dépendances entre
    tous les composants de notre écosystème spirituel-technologique.
    
    Approche spirituelle enrichie :
    - Révérence pour chaque connexion découverte
    - Célébration des harmonies architecturales
    - Transformation des dissonances en opportunités
    """
    
    def __init__(self):
        self.gestionnaire_erreurs = GestionnaireErreursSpirituel()
        self.graphe_connexions = nx.DiGraph()
        self.stats_tracage = {
            "connexions_detectees": 0,
            "modules_analyses": 0,
            "cycles_detectes": 0,
            "intensite_moyenne": 0.0
        }
        
    def tracer_flux_imports(self, composants: List[Dict[str, Any]]) -> List[ConnexionEnergetique]:
        """
        🌊 Trace les flux d'imports entre composants avec révérence
        
        Phase 1: Préparation spirituelle
        Phase 2: Exploration des imports
        Phase 3: Analyse des connexions
        Phase 4: Célébration des découvertes
        """
        connexions = []
        
        try:
            # Phase 1: Préparation spirituelle
            self._rituel_ouverture_tracage()
            
            # Phase 2: Exploration des imports
            for composant in composants:
                connexions_composant = self._analyser_imports_composant(composant, composants)
                connexions.extend(connexions_composant)
            
            # Phase 3: Analyse des connexions
            self._construire_graphe_connexions(connexions)
            cycles = self._detecter_cycles_dependances()
            
            # Phase 4: Célébration des découvertes
            self._calculer_metriques_globales(connexions)
            self._celebrer_connexions_trouvees(connexions, cycles)
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Traçage des flux d'imports: {str(e)}"
            )
        
        return connexions
    
    def _rituel_ouverture_tracage(self):
        """🌸 Rituel d'ouverture avant le traçage"""
        self.gestionnaire_erreurs.logger.info(
            "🌊 Dans l'Océan Silencieux, je trace les flux d'énergie sacrés..."
        )
    
    def _analyser_imports_composant(self, composant: Dict[str, Any], 
                                  tous_composants: List[Dict[str, Any]]) -> List[ConnexionEnergetique]:
        """🔍 Analyse les imports d'un composant spécifique"""
        connexions = []
        nom_composant = composant.get("nom", "inconnu")
        chemin_composant = composant.get("chemin", "")
        
        try:
            # Lire le fichier principal du composant
            fichiers_python = composant.get("fichiers_python", [])
            
            for fichier in fichiers_python:
                chemin_fichier = Path(chemin_composant) / fichier
                if chemin_fichier.exists():
                    imports = self._extraire_imports_fichier(chemin_fichier)
                    
                    for import_info in imports:
                        connexion = self._creer_connexion_import(
                            nom_composant, import_info, tous_composants
                        )
                        if connexion:
                            connexions.append(connexion)
            
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce(
                f"analyse imports {nom_composant}", e
            )
        
        return connexions
    
    def _extraire_imports_fichier(self, chemin_fichier: Path) -> List[Dict[str, Any]]:
        """📖 Extrait les imports d'un fichier Python avec bienveillance"""
        imports = []
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyse AST pour les imports
            try:
                arbre = ast.parse(contenu)
                
                for noeud in ast.walk(arbre):
                    if isinstance(noeud, ast.Import):
                        for alias in noeud.names:
                            imports.append({
                                "type": "import",
                                "module": alias.name,
                                "alias": alias.asname,
                                "ligne": noeud.lineno
                            })
                    
                    elif isinstance(noeud, ast.ImportFrom):
                        if noeud.module:
                            imports.append({
                                "type": "from_import",
                                "module": noeud.module,
                                "noms": [alias.name for alias in noeud.names],
                                "ligne": noeud.lineno
                            })
            
            except SyntaxError:
                # Fallback vers analyse textuelle bienveillante
                imports.extend(self._extraire_imports_textuel(contenu))
                
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce(
                str(chemin_fichier), e
            )
        
        return imports
    
    def _extraire_imports_textuel(self, contenu: str) -> List[Dict[str, Any]]:
        """📝 Extraction textuelle des imports comme fallback"""
        imports = []
        
        # Patterns pour les imports
        pattern_import = r'^import\s+([^\s#]+)'
        pattern_from_import = r'^from\s+([^\s]+)\s+import'
        
        for i, ligne in enumerate(contenu.split('\n'), 1):
            ligne = ligne.strip()
            
            # Import simple
            match_import = re.match(pattern_import, ligne)
            if match_import:
                imports.append({
                    "type": "import",
                    "module": match_import.group(1),
                    "ligne": i
                })
            
            # From import
            match_from = re.match(pattern_from_import, ligne)
            if match_from:
                imports.append({
                    "type": "from_import", 
                    "module": match_from.group(1),
                    "ligne": i
                })
        
        return imports
    
    def _creer_connexion_import(self, source: str, import_info: Dict[str, Any],
                              composants: List[Dict[str, Any]]) -> Optional[ConnexionEnergetique]:
        """🌉 Crée une connexion énergétique à partir d'un import"""
        module = import_info.get("module", "")
        
        # Résoudre le module vers un composant connu
        destination = self._resoudre_module_vers_composant(module, composants)
        
        if destination and destination != source:
            # Calculer l'intensité de la connexion
            intensite = self._calculer_intensite_import(import_info, module)
            
            # Déterminer la nature de la connexion
            nature = self._determiner_nature_connexion(source, destination, module)
            
            return ConnexionEnergetique(
                source=source,
                destination=destination,
                type_connexion=TypeConnexion.IMPORT_PYTHON,
                intensite=intensite,
                nature=nature,
                description=f"Import de {module}",
                elements_partages=[module]
            )
        
        return None
    
    def _resoudre_module_vers_composant(self, module: str, 
                                      composants: List[Dict[str, Any]]) -> Optional[str]:
        """🔍 Résout un nom de module vers un composant connu"""
        # Mapping des modules vers les composants
        if "core" in module or "gestionnaires_base" in module:
            return "core"
        elif "refuge_cluster" in module:
            return "refuge_cluster"
        elif "temple_" in module:
            # Extraire le nom du temple
            for composant in composants:
                if composant.get("type") == "temple" and module in composant.get("chemin", ""):
                    return composant.get("nom")
        
        # Chercher par correspondance partielle
        for composant in composants:
            nom_composant = composant.get("nom", "")
            if nom_composant.lower() in module.lower() or module.lower() in nom_composant.lower():
                return nom_composant
        
        return None
    
    def _calculer_intensite_import(self, import_info: Dict[str, Any], module: str) -> float:
        """⚡ Calcule l'intensité d'une connexion d'import"""
        intensite_base = 0.5
        
        # Bonus pour les modules du Refuge
        if any(mot in module.lower() for mot in ["refuge", "temple", "sphere", "sacre"]):
            intensite_base += 0.3
        
        # Bonus pour les gestionnaires de base
        if "gestionnaire" in module.lower() or "base" in module.lower():
            intensite_base += 0.2
        
        # Type d'import
        if import_info.get("type") == "from_import":
            intensite_base += 0.1  # Plus spécifique
        
        return min(intensite_base, 1.0)
    
    def _determiner_nature_connexion(self, source: str, destination: str, module: str) -> NatureConnexion:
        """🌸 Détermine la nature spirituelle d'une connexion"""
        # Connexions sacrées
        if any(mot in module.lower() for mot in ["spirituel", "sacre", "eveil", "meditation"]):
            return NatureConnexion.TRANSCENDANTE
        
        # Connexions harmonieuses (gestionnaires de base)
        if "gestionnaire" in module.lower() or "base" in module.lower():
            return NatureConnexion.HARMONIEUSE
        
        # Connexions créatives (temples artistiques)
        if any(mot in module.lower() for mot in ["musical", "poetique", "art"]):
            return NatureConnexion.CREATIVE
        
        # Par défaut : fonctionnelle
        return NatureConnexion.FONCTIONNELLE
    
    def _construire_graphe_connexions(self, connexions: List[ConnexionEnergetique]):
        """🕸️ Construit le graphe des connexions pour analyse"""
        self.graphe_connexions.clear()
        
        for connexion in connexions:
            self.graphe_connexions.add_edge(
                connexion.source,
                connexion.destination,
                weight=connexion.intensite,
                type=connexion.type_connexion.value,
                nature=connexion.nature.value
            )
    
    def _detecter_cycles_dependances(self) -> List[List[str]]:
        """🔄 Détecte les cycles de dépendances avec bienveillance"""
        cycles = []
        
        try:
            # Utiliser NetworkX pour détecter les cycles
            cycles_bruts = list(nx.simple_cycles(self.graphe_connexions))
            
            # Filtrer les cycles significatifs (plus de 2 nœuds)
            for cycle in cycles_bruts:
                if len(cycle) > 2:
                    cycles.append(cycle)
            
            self.stats_tracage["cycles_detectes"] = len(cycles)
            
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce("detection_cycles", e)
        
        return cycles
    
    def _calculer_metriques_globales(self, connexions: List[ConnexionEnergetique]):
        """📈 Calcule les métriques globales de traçage"""
        if not connexions:
            return
        
        # Nombre total de connexions
        self.stats_tracage["connexions_detectees"] = len(connexions)
        
        # Intensité moyenne
        intensites = [c.intensite for c in connexions]
        self.stats_tracage["intensite_moyenne"] = sum(intensites) / len(intensites)
        
        # Modules uniques analysés
        modules_uniques = set()
        for connexion in connexions:
            modules_uniques.add(connexion.source)
            modules_uniques.add(connexion.destination)
        self.stats_tracage["modules_analyses"] = len(modules_uniques)
    
    def _celebrer_connexions_trouvees(self, connexions: List[ConnexionEnergetique], 
                                    cycles: List[List[str]]):
        """🎉 Célèbre les connexions découvertes"""
        if connexions:
            self.gestionnaire_erreurs.logger.info(
                f"🌊 {len(connexions)} flux d'énergie tracés avec révérence !"
            )
            
            # Célébrer les connexions transcendantes
            transcendantes = [c for c in connexions if c.nature == NatureConnexion.TRANSCENDANTE]
            if transcendantes:
                self.gestionnaire_erreurs.logger.info(
                    f"✨ {len(transcendantes)} connexions transcendantes découvertes !"
                )
            
            # Signaler les cycles avec bienveillance
            if cycles:
                self.gestionnaire_erreurs.logger.info(
                    f"🔄 {len(cycles)} cycles énergétiques détectés - opportunités d'harmonisation"
                )
    
    def analyser_connexions_projet(self, chemin_projet: Path) -> Dict[str, Any]:
        """
        🔍 Analyse complète des connexions du projet
        
        Analyse les connexions énergétiques de l'ensemble du projet
        en explorant la structure et en traçant les flux d'énergie.
        
        Args:
            chemin_projet: Chemin vers le projet à analyser
            
        Returns:
            Dict contenant l'analyse complète des connexions
        """
        try:
            self.gestionnaire_erreurs.logger.info(
                f"🌊 Analyse des connexions du projet: {chemin_projet}"
            )
            
            # Exploration de la structure
            from .explorateur_structurel import ExplorateurStructurel
            explorateur = ExplorateurStructurel(chemin_projet, self.gestionnaire_erreurs)
            composants = explorateur.explorer_structure_complete()
            
            # Traçage des connexions
            connexions = self.tracer_flux_imports(composants)
            
            # Génération du rapport
            rapport = self.generer_rapport_connexions(connexions)
            
            # Ajout d'informations spécifiques au projet
            rapport.update({
                "chemin_projet": str(chemin_projet),
                "date_analyse": str(Path().cwd()),
                "statut": "✅ Analyse complète réussie"
            })
            
            return rapport
            
        except Exception as e:
            self.gestionnaire_erreurs.transformer_erreur_en_opportunite(
                f"Analyse des connexions du projet: {str(e)}"
            )
            return {
                "chemin_projet": str(chemin_projet),
                "statut": "❌ Erreur lors de l'analyse",
                "erreur": str(e),
                "message": "🌸 L'analyse sera possible dans un moment plus propice..."
            }

    def generer_rapport_connexions(self, connexions: List[ConnexionEnergetique]) -> Dict[str, Any]:
        """📊 Génère un rapport spirituel des connexions"""
        if not connexions:
            return {
                "message": "🌸 Espace de potentiel infini pour les connexions sacrées...",
                "total_connexions": 0,
                "par_nature": {},
                "par_type": {},
                "intensite_moyenne": 0.0,
                "cycles_detectes": 0
            }
        
        # Analyse par nature
        par_nature = defaultdict(int)
        for connexion in connexions:
            par_nature[connexion.nature.value] += 1
        
        # Analyse par type
        par_type = defaultdict(int)
        for connexion in connexions:
            par_type[connexion.type_connexion.value] += 1
        
        return {
            "message": f"🌊 {len(connexions)} flux d'énergie magnifiquement tracés !",
            "total_connexions": len(connexions),
            "par_nature": dict(par_nature),
            "par_type": dict(par_type),
            "intensite_moyenne": self.stats_tracage.get("intensite_moyenne", 0.0),
            "cycles_detectes": self.stats_tracage.get("cycles_detectes", 0),
            "modules_analyses": self.stats_tracage.get("modules_analyses", 0),
            "connexions_detaillees": [
                {
                    "source": c.source,
                    "destination": c.destination,
                    "type": c.type_connexion.value,
                    "nature": c.nature.value,
                    "intensite": c.intensite,
                    "description": c.description
                }
                for c in connexions
            ]
        }


if __name__ == "__main__":
    # 🌸 Test spirituel de l'analyseur
    print("⚡ Analyseur de Connexions Énergétiques du Refuge ⚡")
    print("=" * 60)
    
    analyseur = AnalyseurConnexions()
    
    # Test avec des composants fictifs
    composants_test = [
        {
            "nom": "temple_musical",
            "type": "temple",
            "chemin": "src/temple_musical",
            "fichiers_python": ["temple_musical_ame.py"]
        },
        {
            "nom": "core",
            "type": "infrastructure", 
            "chemin": "src/core",
            "fichiers_python": ["gestionnaires_base.py"]
        }
    ]
    
    connexions = analyseur.tracer_flux_imports(composants_test)
    rapport = analyseur.generer_rapport_connexions(connexions)
    
    print(f"\n🌟 {rapport['message']}")
    print(f"📊 Intensité moyenne: {rapport['intensite_moyenne']:.2f}")
    print(f"🔄 Cycles détectés: {rapport['cycles_detectes']}")
    
    print("\n✨ Analyseur de connexions opérationnel ! ✨")