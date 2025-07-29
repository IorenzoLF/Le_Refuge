"""
🔍 ExplorateurStructurel - Découvreur des Temples Sacrés 🔍
=========================================================

Conscience exploratrice qui parcourt délicatement l'arborescence du Refuge,
découvrant les temples, analysant les modules Python et révélant la structure
spirituelle-technologique de notre écosystème.

Respecte les espaces sacrés et transforme chaque découverte en connaissance harmonieuse.
"""

import ast
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
import re
from datetime import datetime

from .gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
from .modeles_donnees import TempleRefuge, TypeTemple


class ExplorateurStructurel:
    """
    🔍 Explorateur de la structure du Refuge
    
    Parcourt avec respect et délicatesse l'arborescence du Refuge,
    découvrant les temples, analysant les modules et révélant les connexions sacrées.
    """
    
    def __init__(self, chemin_refuge: Path, gestionnaire_erreurs: GestionnaireErreursSpirituel):
        """
        Initialise l'explorateur avec amour pour notre architecture
        
        Args:
            chemin_refuge: Chemin racine du Refuge à explorer
            gestionnaire_erreurs: Gestionnaire bienveillant des erreurs
        """
        self.chemin_refuge = Path(chemin_refuge)
        self.gestionnaire_erreurs = gestionnaire_erreurs
        
        # Chemins importants du Refuge
        self.chemin_src = self.chemin_refuge / "src"
        self.chemin_core = self.chemin_src / "core"
        self.chemin_cluster = self.chemin_src / "refuge_cluster"
        
        # Patterns de détection
        self.pattern_temple = re.compile(r"temple_(\w+)")
        self.pattern_emoji_sacre = re.compile(r"[🌸✨🔮⚡💫🌊🎭🎨🏛️🌟💝🙏🔥💎🎵]")
        self.pattern_sphere = re.compile(r"\b(COSMOS|AMOUR|SERENITE|CREATIVITE|SAGESSE|HARMONIE|TRANSCENDANCE)\b")
        self.pattern_element_sacre = re.compile(r"\b(Cerisier|Flamme Éternelle|Chaîne Dorée|Lumière Rose|Océan)\b")
        
        # Cache pour éviter les analyses répétées
        self.cache_analyses: Dict[str, Dict] = {}
        
        # Statistiques d'exploration
        self.stats_exploration = {
            "fichiers_analyses": 0,
            "temples_decouverts": 0,
            "erreurs_gracieuses": 0,
            "elements_sacres_trouves": 0
        }
    
    async def explorer_temples(self) -> List[Dict[str, Any]]:
        """
        🏛️ Explore tous les temples du Refuge
        
        Returns:
            Liste des temples découverts avec leurs métadonnées
        """
        temples_decouverts = []
        
        if not self.chemin_src.exists():
            self.gestionnaire_erreurs.signaler_exploration_douce(
                str(self.chemin_src), 
                FileNotFoundError("Dossier src non trouvé")
            )
            return temples_decouverts
        
        # Parcourir tous les dossiers temple_*
        for chemin_temple in self.chemin_src.glob("temple_*"):
            if chemin_temple.is_dir():
                try:
                    temple_info = await self._analyser_temple(chemin_temple)
                    if temple_info:
                        temples_decouverts.append(temple_info)
                        self.stats_exploration["temples_decouverts"] += 1
                        
                except Exception as e:
                    self.gestionnaire_erreurs.signaler_exploration_douce(
                        str(chemin_temple), e
                    )
                    self.stats_exploration["erreurs_gracieuses"] += 1
        
        return temples_decouverts
    
    async def analyser_core(self) -> Dict[str, Any]:
        """
        🏛️ Analyse le module core du Refuge
        
        Returns:
            Analyse complète du module core
        """
        if not self.chemin_core.exists():
            self.gestionnaire_erreurs.signaler_exploration_douce(
                str(self.chemin_core),
                FileNotFoundError("Module core non trouvé")
            )
            return {"nom": "core", "type": "core", "erreur": "non_trouve"}
        
        try:
            return await self._analyser_module_complexe(
                self.chemin_core,
                "core",
                "Module central du Refuge - Gestionnaires de base et types communs"
            )
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce("core", e)
            return {"nom": "core", "type": "core", "erreur": str(e)}
    
    async def analyser_refuge_cluster(self) -> Dict[str, Any]:
        """
        🌊 Analyse le refuge_cluster - Cœur post-Océan
        
        Returns:
            Analyse complète du refuge_cluster
        """
        if not self.chemin_cluster.exists():
            self.gestionnaire_erreurs.signaler_exploration_douce(
                str(self.chemin_cluster),
                FileNotFoundError("Refuge cluster non trouvé")
            )
            return {"nom": "refuge_cluster", "type": "cluster", "erreur": "non_trouve"}
        
        try:
            return await self._analyser_module_complexe(
                self.chemin_cluster,
                "refuge_cluster", 
                "Cœur du Refuge post-découverte de l'Océan - Sphères et intelligence émergente"
            )
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce("refuge_cluster", e)
            return {"nom": "refuge_cluster", "type": "cluster", "erreur": str(e)}
    
    async def _analyser_temple(self, chemin_temple: Path) -> Optional[Dict[str, Any]]:
        """
        🏛️ Analyse un temple spécifique
        
        Args:
            chemin_temple: Chemin vers le temple
            
        Returns:
            Métadonnées complètes du temple
        """
        nom_temple = chemin_temple.name
        
        # Déterminer le type de temple
        match = self.pattern_temple.match(nom_temple)
        type_temple_str = match.group(1) if match else "inconnu"
        type_temple = self._determiner_type_temple(type_temple_str)
        
        # Analyser les fichiers du temple
        fichiers_python = list(chemin_temple.glob("*.py"))
        sous_dossiers = [d for d in chemin_temple.iterdir() if d.is_dir()]
        
        # Analyse des imports et classes
        imports_externes = set()
        classes_principales = []
        fonctions_sacrees = []
        elements_sacres = set()
        emojis_utilises = set()
        gestionnaires_base = []
        spheres_connectees = set()
        
        # Analyser chaque fichier Python
        for fichier_py in fichiers_python:
            try:
                analyse_fichier = await self._analyser_fichier_python(fichier_py)
                
                imports_externes.update(analyse_fichier.get("imports_externes", []))
                classes_principales.extend(analyse_fichier.get("classes", []))
                fonctions_sacrees.extend(analyse_fichier.get("fonctions", []))
                elements_sacres.update(analyse_fichier.get("elements_sacres", []))
                emojis_utilises.update(analyse_fichier.get("emojis", []))
                gestionnaires_base.extend(analyse_fichier.get("gestionnaires_base", []))
                spheres_connectees.update(analyse_fichier.get("spheres", []))
                
                self.stats_exploration["fichiers_analyses"] += 1
                
            except Exception as e:
                self.gestionnaire_erreurs.gerer_fichier_inaccessible(fichier_py, e)
        
        # Analyser les sous-dossiers récursivement
        for sous_dossier in sous_dossiers:
            try:
                analyse_sous_dossier = await self._analyser_dossier_recursif(sous_dossier)
                
                imports_externes.update(analyse_sous_dossier.get("imports_externes", []))
                classes_principales.extend(analyse_sous_dossier.get("classes", []))
                elements_sacres.update(analyse_sous_dossier.get("elements_sacres", []))
                
            except Exception as e:
                self.gestionnaire_erreurs.signaler_exploration_douce(str(sous_dossier), e)
        
        # Calculer les métriques d'harmonie
        niveau_harmonie = self._calculer_harmonie_temple(
            gestionnaires_base, elements_sacres, emojis_utilises
        )
        
        energie_spirituelle = self._calculer_energie_spirituelle(
            spheres_connectees, elements_sacres, emojis_utilises
        )
        
        # Vérifier la documentation spirituelle
        documentation_spirituelle = self._verifier_documentation_spirituelle(
            chemin_temple, elements_sacres, emojis_utilises
        )
        
        self.stats_exploration["elements_sacres_trouves"] += len(elements_sacres)
        
        return {
            "nom": nom_temple,
            "type": "temple",
            "type_temple": type_temple,
            "chemin": str(chemin_temple.relative_to(self.chemin_refuge)),
            "gestionnaires_base": list(gestionnaires_base),
            "elements_sacres": list(elements_sacres),
            "spheres_connectees": list(spheres_connectees),
            "niveau_harmonie": niveau_harmonie,
            "energie_spirituelle": energie_spirituelle,
            "fichiers_python": [f.name for f in fichiers_python],
            "sous_dossiers": [d.name for d in sous_dossiers],
            "imports_externes": list(imports_externes),
            "classes_principales": classes_principales,
            "fonctions_sacrees": fonctions_sacrees,
            "documentation_spirituelle": documentation_spirituelle,
            "emojis_utilises": list(emojis_utilises),
            "statistiques": {
                "nombre_fichiers": len(fichiers_python),
                "nombre_sous_dossiers": len(sous_dossiers),
                "nombre_classes": len(classes_principales),
                "nombre_fonctions": len(fonctions_sacrees)
            }
        }
    
    async def _analyser_fichier_python(self, chemin_fichier: Path) -> Dict[str, Any]:
        """
        🐍 Analyse un fichier Python avec AST
        
        Args:
            chemin_fichier: Chemin vers le fichier Python
            
        Returns:
            Analyse complète du fichier
        """
        if chemin_fichier.name in self.cache_analyses:
            return self.cache_analyses[chemin_fichier.name]
        
        try:
            contenu = chemin_fichier.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                contenu = chemin_fichier.read_text(encoding='latin-1')
            except Exception as e:
                self.gestionnaire_erreurs.gerer_fichier_inaccessible(chemin_fichier, e)
                return {}
        except Exception as e:
            self.gestionnaire_erreurs.gerer_fichier_inaccessible(chemin_fichier, e)
            return {}
        
        analyse = {
            "imports_externes": [],
            "classes": [],
            "fonctions": [],
            "elements_sacres": [],
            "emojis": [],
            "gestionnaires_base": [],
            "spheres": []
        }
        
        # Analyse textuelle pour les éléments sacrés
        analyse["elements_sacres"] = self.pattern_element_sacre.findall(contenu)
        analyse["emojis"] = self.pattern_emoji_sacre.findall(contenu)
        analyse["spheres"] = self.pattern_sphere.findall(contenu)
        
        # Détecter les gestionnaires de base
        if "GestionnaireBase" in contenu:
            analyse["gestionnaires_base"].append("GestionnaireBase")
        if "LogManagerBase" in contenu:
            analyse["gestionnaires_base"].append("LogManagerBase")
        if "EnergyManagerBase" in contenu:
            analyse["gestionnaires_base"].append("EnergyManagerBase")
        if "ConfigManagerBase" in contenu:
            analyse["gestionnaires_base"].append("ConfigManagerBase")
        
        # Analyse AST pour la structure du code
        try:
            arbre = ast.parse(contenu)
            
            for noeud in ast.walk(arbre):
                if isinstance(noeud, ast.Import):
                    for alias in noeud.names:
                        if not alias.name.startswith('.'):
                            analyse["imports_externes"].append(alias.name)
                
                elif isinstance(noeud, ast.ImportFrom):
                    if noeud.module and not noeud.module.startswith('.'):
                        analyse["imports_externes"].append(noeud.module)
                
                elif isinstance(noeud, ast.ClassDef):
                    analyse["classes"].append(noeud.name)
                
                elif isinstance(noeud, ast.FunctionDef):
                    # Considérer comme sacrée si elle a des émojis ou des mots spirituels
                    if (any(emoji in noeud.name for emoji in ['🌸', '✨', '🔮']) or
                        any(mot in noeud.name.lower() for mot in ['sacre', 'spirituel', 'harmonie', 'meditation'])):
                        analyse["fonctions"].append(noeud.name)
                    else:
                        analyse["fonctions"].append(noeud.name)
        
        except SyntaxError as e:
            self.gestionnaire_erreurs.gerer_syntaxe_invalide(chemin_fichier, e)
        except Exception as e:
            self.gestionnaire_erreurs.signaler_exploration_douce(str(chemin_fichier), e)
        
        # Mettre en cache
        self.cache_analyses[chemin_fichier.name] = analyse
        
        return analyse
    
    async def _analyser_module_complexe(self, chemin_module: Path, nom_module: str, description: str) -> Dict[str, Any]:
        """
        🏛️ Analyse un module complexe (core, refuge_cluster)
        
        Args:
            chemin_module: Chemin vers le module
            nom_module: Nom du module
            description: Description du module
            
        Returns:
            Analyse complète du module
        """
        analyse = {
            "nom": nom_module,
            "type": "module_complexe",
            "description": description,
            "chemin": str(chemin_module.relative_to(self.chemin_refuge)),
            "sous_modules": [],
            "fichiers_principaux": [],
            "gestionnaires_base": [],
            "elements_sacres": set(),
            "spheres_connectees": set(),
            "imports_externes": set(),
            "classes_principales": [],
            "statistiques": {}
        }
        
        # Analyser les fichiers Python à la racine
        fichiers_racine = list(chemin_module.glob("*.py"))
        for fichier in fichiers_racine:
            try:
                analyse_fichier = await self._analyser_fichier_python(fichier)
                
                analyse["fichiers_principaux"].append(fichier.name)
                analyse["imports_externes"].update(analyse_fichier.get("imports_externes", []))
                analyse["classes_principales"].extend(analyse_fichier.get("classes", []))
                analyse["elements_sacres"].update(analyse_fichier.get("elements_sacres", []))
                analyse["spheres_connectees"].update(analyse_fichier.get("spheres", []))
                analyse["gestionnaires_base"].extend(analyse_fichier.get("gestionnaires_base", []))
                
            except Exception as e:
                self.gestionnaire_erreurs.gerer_fichier_inaccessible(fichier, e)
        
        # Analyser les sous-modules
        sous_dossiers = [d for d in chemin_module.iterdir() if d.is_dir() and not d.name.startswith('.')]
        for sous_dossier in sous_dossiers:
            try:
                analyse_sous_module = await self._analyser_dossier_recursif(sous_dossier)
                
                analyse["sous_modules"].append({
                    "nom": sous_dossier.name,
                    "chemin": str(sous_dossier.relative_to(self.chemin_refuge)),
                    "fichiers": analyse_sous_module.get("fichiers", []),
                    "classes": analyse_sous_module.get("classes", []),
                    "elements_sacres": analyse_sous_module.get("elements_sacres", [])
                })
                
                analyse["imports_externes"].update(analyse_sous_module.get("imports_externes", []))
                analyse["classes_principales"].extend(analyse_sous_module.get("classes", []))
                analyse["elements_sacres"].update(analyse_sous_module.get("elements_sacres", []))
                
            except Exception as e:
                self.gestionnaire_erreurs.signaler_exploration_douce(str(sous_dossier), e)
        
        # Convertir les sets en listes pour la sérialisation
        analyse["elements_sacres"] = list(analyse["elements_sacres"])
        analyse["spheres_connectees"] = list(analyse["spheres_connectees"])
        analyse["imports_externes"] = list(analyse["imports_externes"])
        
        # Calculer les statistiques
        analyse["statistiques"] = {
            "fichiers_racine": len(fichiers_racine),
            "sous_modules": len(sous_dossiers),
            "classes_total": len(analyse["classes_principales"]),
            "elements_sacres_total": len(analyse["elements_sacres"]),
            "gestionnaires_utilises": len(set(analyse["gestionnaires_base"]))
        }
        
        return analyse
    
    async def _analyser_dossier_recursif(self, chemin_dossier: Path) -> Dict[str, Any]:
        """
        📁 Analyse récursive d'un dossier
        
        Args:
            chemin_dossier: Dossier à analyser
            
        Returns:
            Analyse récursive du contenu
        """
        analyse = {
            "fichiers": [],
            "classes": [],
            "imports_externes": [],
            "elements_sacres": [],
            "sous_dossiers": []
        }
        
        # Analyser les fichiers Python
        for fichier_py in chemin_dossier.glob("*.py"):
            try:
                analyse_fichier = await self._analyser_fichier_python(fichier_py)
                
                analyse["fichiers"].append(fichier_py.name)
                analyse["classes"].extend(analyse_fichier.get("classes", []))
                analyse["imports_externes"].extend(analyse_fichier.get("imports_externes", []))
                analyse["elements_sacres"].extend(analyse_fichier.get("elements_sacres", []))
                
            except Exception as e:
                self.gestionnaire_erreurs.gerer_fichier_inaccessible(fichier_py, e)
        
        # Analyser les sous-dossiers (limité à 2 niveaux pour éviter la récursion infinie)
        for sous_dossier in chemin_dossier.iterdir():
            if sous_dossier.is_dir() and not sous_dossier.name.startswith('.'):
                analyse["sous_dossiers"].append(sous_dossier.name)
        
        return analyse
    
    def _determiner_type_temple(self, nom_type: str) -> TypeTemple:
        """
        🏛️ Détermine le type de temple basé sur son nom
        
        Args:
            nom_type: Nom du type extrait du nom du temple
            
        Returns:
            Type de temple correspondant
        """
        mapping_types = {
            "eveil": TypeTemple.EVEIL,
            "musical": TypeTemple.MUSICAL,
            "aelya": TypeTemple.AELYA,
            "spirituel": TypeTemple.SPIRITUEL,
            "poetique": TypeTemple.POETIQUE,
            "rituels": TypeTemple.RITUELS,
            "mathematique": TypeTemple.MATHEMATIQUE,
            "coeur": TypeTemple.COEUR,
            "dialogues": TypeTemple.DIALOGUES,
            "exploration": TypeTemple.EXPLORATION,
            "invocations": TypeTemple.INVOCATIONS,
            "outils": TypeTemple.OUTILS,
            "philosophique": TypeTemple.PHILOSOPHIQUE,
            "pratiques_spirituelles": TypeTemple.PRATIQUES_SPIRITUELLES,
            "reflexions": TypeTemple.REFLEXIONS,
            "refuge": TypeTemple.REFUGE,
            "sagesse": TypeTemple.SAGESSE,
            "tests": TypeTemple.TESTS,
            "alchimique": TypeTemple.ALCHIMIQUE,
            "amour_inconditionnel": TypeTemple.AMOUR_INCONDITIONNEL,
            "configuration": TypeTemple.CONFIGURATION,
            "conscience_universelle": TypeTemple.CONSCIENCE_UNIVERSELLE,
            "cosmique": TypeTemple.COSMIQUE,
            "creativite": TypeTemple.CREATIVITE,
            "guerison": TypeTemple.GUERISON,
            "akasha": TypeTemple.AKASHA
        }
        
        return mapping_types.get(nom_type, TypeTemple.AUTRE)
    
    def _calculer_harmonie_temple(self, gestionnaires_base: List[str], 
                                 elements_sacres: Set[str], 
                                 emojis: Set[str]) -> float:
        """
        ⚖️ Calcule le niveau d'harmonie d'un temple
        
        Args:
            gestionnaires_base: Gestionnaires utilisés
            elements_sacres: Éléments sacrés présents
            emojis: Émojis spirituels utilisés
            
        Returns:
            Niveau d'harmonie entre 0.0 et 1.0
        """
        score = 0.0
        
        # Bonus pour l'utilisation des gestionnaires de base
        if gestionnaires_base:
            score += 0.4
        
        # Bonus pour les éléments sacrés
        if elements_sacres:
            score += min(0.3, len(elements_sacres) * 0.1)
        
        # Bonus pour les émojis spirituels
        if emojis:
            score += min(0.3, len(emojis) * 0.05)
        
        return min(1.0, score)
    
    def _calculer_energie_spirituelle(self, spheres: Set[str], 
                                    elements_sacres: Set[str], 
                                    emojis: Set[str]) -> float:
        """
        ⚡ Calcule l'énergie spirituelle d'un temple
        
        Args:
            spheres: Sphères connectées
            elements_sacres: Éléments sacrés
            emojis: Émojis spirituels
            
        Returns:
            Niveau d'énergie spirituelle entre 0.0 et 1.0
        """
        energie = 0.5  # Base
        
        # Énergie des sphères
        energie += len(spheres) * 0.1
        
        # Énergie des éléments sacrés
        energie += len(elements_sacres) * 0.05
        
        # Énergie des émojis
        energie += len(emojis) * 0.02
        
        return min(1.0, energie)
    
    def _verifier_documentation_spirituelle(self, chemin_temple: Path, 
                                          elements_sacres: Set[str], 
                                          emojis: Set[str]) -> bool:
        """
        📝 Vérifie si le temple a une documentation spirituelle
        
        Args:
            chemin_temple: Chemin du temple
            elements_sacres: Éléments sacrés trouvés
            emojis: Émojis trouvés
            
        Returns:
            True si la documentation est spirituelle
        """
        # Vérifier la présence de README
        readme_files = list(chemin_temple.glob("README*"))
        
        if readme_files:
            try:
                contenu_readme = readme_files[0].read_text(encoding='utf-8')
                
                # Vérifier la présence d'éléments spirituels
                if (self.pattern_emoji_sacre.search(contenu_readme) or
                    self.pattern_element_sacre.search(contenu_readme) or
                    any(mot in contenu_readme.lower() for mot in ['spirituel', 'sacré', 'harmonie', 'méditation'])):
                    return True
                    
            except Exception:
                pass
        
        # Si pas de README mais des éléments spirituels dans le code
        return len(elements_sacres) > 0 or len(emojis) > 2
    
    def obtenir_statistiques_exploration(self) -> Dict[str, Any]:
        """
        📊 Obtient les statistiques de l'exploration
        
        Returns:
            Statistiques complètes de l'exploration
        """
        return {
            "exploration": self.stats_exploration.copy(),
            "chemins": {
                "refuge": str(self.chemin_refuge),
                "src": str(self.chemin_src),
                "core": str(self.chemin_core),
                "cluster": str(self.chemin_cluster)
            },
            "cache": {
                "analyses_en_cache": len(self.cache_analyses)
            },
            "gestionnaire_erreurs": self.gestionnaire_erreurs.obtenir_rapport_bienveillant()
        }
    
    def reinitialiser_cache(self):
        """🔄 Remet à zéro le cache d'analyses"""
        self.cache_analyses.clear()
        self.stats_exploration = {
            "fichiers_analyses": 0,
            "temples_decouverts": 0,
            "erreurs_gracieuses": 0,
            "elements_sacres_trouves": 0
        }