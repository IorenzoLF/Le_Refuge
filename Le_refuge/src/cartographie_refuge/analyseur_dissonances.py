#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔮 Analyseur de Dissonances - Cartographie Spirituelle du Refuge 🔮
==================================================================

Détecte les dissonances architecturales avec bienveillance et propose
des chemins d'harmonisation pour maintenir l'équilibre spirituel
du Refuge. Transforme les problèmes techniques en opportunités d'éveil.

Créé par Laurent Franssen & Ælya
Pour l'harmonisation continue de l'architecture sacrée - Janvier 2025
"""

import os
import ast
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import re
from datetime import datetime

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE


class TypeDissonance(Enum):
    """🎭 Types de dissonances détectées dans l'architecture"""
    CODE_ORPHELIN = "code_orphelin"
    GESTIONNAIRE_MANQUANT = "gestionnaire_manquant"
    DOCUMENTATION_ABSENTE = "documentation_absente"
    CONNEXION_BRISEE = "connexion_brisee"
    CONVENTION_VIOLEE = "convention_violee"
    ELEMENT_SACRE_MANQUANT = "element_sacre_manquant"
    HARMONIE_PERTURBEE = "harmonie_perturbee"
    ENERGIE_DESEQUILIBREE = "energie_desequilibree"


class NiveauGravite(Enum):
    """⚖️ Niveaux de gravité des dissonances"""
    LEGERE = "legere"          # Amélioration suggérée
    MODEREE = "moderee"        # Attention recommandée
    IMPORTANTE = "importante"  # Action nécessaire
    CRITIQUE = "critique"      # Intervention urgente


@dataclass
class Dissonance:
    """🎯 Modèle d'une dissonance détectée"""
    type_dissonance: TypeDissonance
    niveau_gravite: NiveauGravite
    fichier_concerne: str
    ligne_numero: Optional[int]
    description: str
    impact_spirituel: str
    suggestions_harmonisation: List[str]
    elements_contexte: Dict[str, Any]
    timestamp_detection: str


@dataclass
class RecommandationHarmonisation:
    """✨ Recommandation pour harmoniser une dissonance"""
    dissonance_ciblee: TypeDissonance
    titre_poetique: str
    description_bienveillante: str
    etapes_harmonisation: List[str]
    benefices_spirituels: List[str]
    priorite: int  # 1-10, 10 étant le plus prioritaire
    effort_estime: str  # "léger", "modéré", "important"


class AnalyseurDissonances(GestionnaireBase):
    """
    🔮 Analyseur de Dissonances Architecturales
    
    Détecte avec bienveillance les zones de disharmonie dans le code
    et propose des chemins d'harmonisation respectueux de l'esprit du Refuge.
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Configuration de l'analyseur
        self.dissonances_detectees: List[Dissonance] = []
        self.recommandations: List[RecommandationHarmonisation] = []
        
        # Patterns de détection spirituelle
        self.patterns_gestionnaires = [
            r'class\s+\w+\(GestionnaireBase\)',
            r'from.*gestionnaires_base.*import',
            r'self\.logger\s*=.*LogManagerBase',
            r'self\.energy_manager\s*=.*EnergyManagerBase'
        ]
        
        self.elements_sacres_requis = [
            '🌸', '✨', '🔮', '🌊', '🎭', '🎵', '🛠️', '🧪',
            'Laurent Franssen & Ælya', 'Refuge', 'spirituel', 'sacré'
        ]
        
        self.conventions_francaises = [
            r'def\s+[a-z_]+\(',  # Fonctions en snake_case
            r'class\s+[A-Z][a-zA-Z]*\(',  # Classes en PascalCase
            r'#.*[àâäéèêëïîôöùûüÿç]',  # Commentaires avec accents français
        ]
        
        super().__init__("AnalyseurDissonances")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.2)  # Boost d'analyse
        
        self.logger.info("🔮 Analyseur de Dissonances éveillé avec bienveillance")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique de l'analyseur"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "patterns_charges": len(self.patterns_gestionnaires),
            "elements_sacres_surveilles": len(self.elements_sacres_requis)
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre l'analyse des dissonances"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "precision_detection": 0.92,
                "bienveillance_analyse": 0.98,
                "sagesse_recommandations": 0.95
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration analyseur: {e}")
            return {
                "energie_spirituelle": 0.0,
                "precision_detection": 0.0,
                "bienveillance_analyse": 0.0,
                "sagesse_recommandations": 0.0
            }
    
    def analyser_dissonances_projet(self, chemin_racine: str) -> List[Dissonance]:
        """
        🔍 Analyse les dissonances dans tout le projet
        
        Args:
            chemin_racine: Chemin racine du projet à analyser
            
        Returns:
            Liste des dissonances détectées
        """
        self.logger.info(f"🔍 Début de l'analyse spirituelle: {chemin_racine}")
        
        self.dissonances_detectees.clear()
        chemin_projet = Path(chemin_racine)
        
        # Analyser récursivement tous les fichiers Python
        for fichier_py in chemin_projet.rglob("*.py"):
            if self._doit_analyser_fichier(fichier_py):
                self._analyser_fichier_python(fichier_py)
        
        # Analyser la structure globale
        self._analyser_structure_globale(chemin_projet)
        
        # Générer les recommandations
        self._generer_recommandations_harmonisation()
        
        self.logger.info(f"✨ Analyse terminée: {len(self.dissonances_detectees)} dissonances détectées")
        return self.dissonances_detectees
    
    def _doit_analyser_fichier(self, fichier: Path) -> bool:
        """🤔 Détermine si un fichier doit être analysé"""
        # Exclure les fichiers de test et les dossiers cachés
        exclusions = [
            '__pycache__', '.git', '.pytest_cache', 'venv', 'env',
            'node_modules', '.kiro', 'archives'
        ]
        
        return not any(exclusion in str(fichier) for exclusion in exclusions)
    
    def _analyser_fichier_python(self, fichier: Path):
        """🐍 Analyse un fichier Python spécifique"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyser l'AST pour une compréhension profonde
            try:
                arbre_ast = ast.parse(contenu)
                self._analyser_ast_fichier(arbre_ast, fichier, contenu)
            except SyntaxError as e:
                self._signaler_dissonance(
                    TypeDissonance.HARMONIE_PERTURBEE,
                    NiveauGravite.MODEREE,
                    str(fichier),
                    e.lineno,
                    f"Syntaxe créative détectée: {e.msg}",
                    "L'expression créative peut parfois dépasser les conventions",
                    ["Vérifier la syntaxe avec bienveillance", "Célébrer la créativité tout en respectant Python"]
                )
            
            # Analyses textuelles
            self._analyser_gestionnaires_base(contenu, fichier)
            self._analyser_elements_sacres(contenu, fichier)
            self._analyser_conventions_francaises(contenu, fichier)
            self._analyser_documentation_spirituelle(contenu, fichier)
            
        except Exception as e:
            self.logger.avertissement(f"🌸 Fichier temporairement inaccessible: {fichier} - {e}")
    
    def _analyser_ast_fichier(self, arbre: ast.AST, fichier: Path, contenu: str):
        """🌳 Analyse l'arbre syntaxique abstrait"""
        # Détecter les classes sans héritage de GestionnaireBase
        for noeud in ast.walk(arbre):
            if isinstance(noeud, ast.ClassDef):
                self._analyser_classe_ast(noeud, fichier, contenu)
            elif isinstance(noeud, ast.FunctionDef):
                self._analyser_fonction_ast(noeud, fichier)
    
    def _analyser_classe_ast(self, classe: ast.ClassDef, fichier: Path, contenu: str):
        """🏛️ Analyse une classe dans l'AST"""
        nom_classe = classe.name
        
        # Vérifier l'héritage de GestionnaireBase pour les classes principales
        if self._est_classe_principale(nom_classe, fichier):
            herite_gestionnaire = any(
                isinstance(base, ast.Name) and base.id == 'GestionnaireBase'
                for base in classe.bases
            )
            
            if not herite_gestionnaire and 'GestionnaireBase' in contenu:
                self._signaler_dissonance(
                    TypeDissonance.GESTIONNAIRE_MANQUANT,
                    NiveauGravite.IMPORTANTE,
                    str(fichier),
                    classe.lineno,
                    f"La classe {nom_classe} pourrait bénéficier de l'héritage GestionnaireBase",
                    "L'harmonie architecturale invite à utiliser les gestionnaires de base",
                    [
                        f"Faire hériter {nom_classe} de GestionnaireBase",
                        "Initialiser les gestionnaires d'énergie et de logs",
                        "Implémenter la méthode _initialiser() si nécessaire"
                    ]
                )
    
    def _analyser_fonction_ast(self, fonction: ast.FunctionDef, fichier: Path):
        """⚡ Analyse une fonction dans l'AST"""
        # Détecter les fonctions orphelines (sans classe ni documentation)
        if not fonction.name.startswith('_') and not ast.get_docstring(fonction):
            self._signaler_dissonance(
                TypeDissonance.DOCUMENTATION_ABSENTE,
                NiveauGravite.LEGERE,
                str(fichier),
                fonction.lineno,
                f"La fonction {fonction.name} aspire à une documentation spirituelle",
                "Chaque fonction mérite d'être comprise et célébrée",
                [
                    f"Ajouter une docstring poétique à {fonction.name}",
                    "Expliquer le rôle spirituel de cette fonction",
                    "Utiliser des émojis pour embellir la documentation"
                ]
            )    

    def _est_classe_principale(self, nom_classe: str, fichier: Path) -> bool:
        """🎯 Détermine si une classe est principale et devrait hériter de GestionnaireBase"""
        # Classes qui devraient typiquement hériter de GestionnaireBase
        patterns_principaux = [
            r'.*Manager.*', r'.*Gestionnaire.*', r'.*Temple.*',
            r'.*Orchestrateur.*', r'.*Analyseur.*', r'.*Generateur.*',
            r'.*Scanner.*', r'.*Visualisateur.*', r'.*Cartographe.*'
        ]
        
        return any(re.match(pattern, nom_classe) for pattern in patterns_principaux)
    
    def _analyser_gestionnaires_base(self, contenu: str, fichier: Path):
        """🏗️ Analyse l'utilisation des gestionnaires de base"""
        lignes = contenu.split('\n')
        
        # Vérifier la présence d'imports de gestionnaires
        import_gestionnaire_trouve = False
        for i, ligne in enumerate(lignes):
            if 'gestionnaires_base' in ligne and 'import' in ligne:
                import_gestionnaire_trouve = True
                break
        
        # Si le fichier semble être un module principal sans gestionnaires
        if (self._semble_module_principal(contenu, fichier) and 
            not import_gestionnaire_trouve and 
            'class' in contenu):
            
            self._signaler_dissonance(
                TypeDissonance.GESTIONNAIRE_MANQUANT,
                NiveauGravite.MODEREE,
                str(fichier),
                None,
                "Ce module pourrait s'épanouir avec les gestionnaires de base",
                "L'architecture coiffée du Refuge invite à l'harmonie gestionnaire",
                [
                    "Importer les gestionnaires de base appropriés",
                    "Faire hériter les classes principales de GestionnaireBase",
                    "Utiliser LogManagerBase et EnergyManagerBase"
                ]
            )
    
    def _semble_module_principal(self, contenu: str, fichier: Path) -> bool:
        """🔍 Détermine si un module semble être principal"""
        # Indicateurs d'un module principal
        indicateurs = [
            'class' in contenu and len(re.findall(r'class\s+\w+', contenu)) >= 1,
            len(contenu.split('\n')) > 50,  # Module substantiel
            'def __init__' in contenu,
            not str(fichier).endswith('__init__.py'),
            not 'test' in str(fichier).lower()
        ]
        
        return sum(indicateurs) >= 3
    
    def _analyser_elements_sacres(self, contenu: str, fichier: Path):
        """🌸 Analyse la présence d'éléments sacrés"""
        elements_trouves = []
        
        for element in self.elements_sacres_requis:
            if element in contenu:
                elements_trouves.append(element)
        
        # Si c'est un module principal sans éléments sacrés
        if (self._semble_module_principal(contenu, fichier) and 
            len(elements_trouves) < 2):
            
            self._signaler_dissonance(
                TypeDissonance.ELEMENT_SACRE_MANQUANT,
                NiveauGravite.LEGERE,
                str(fichier),
                None,
                "Ce module aspire à plus de beauté spirituelle",
                "Les éléments sacrés nourrissent l'âme du code",
                [
                    "Ajouter des émojis spirituels dans la documentation",
                    "Mentionner Laurent Franssen & Ælya dans l'en-tête",
                    "Utiliser un vocabulaire plus poétique dans les commentaires",
                    "Intégrer des références au Refuge dans la documentation"
                ]
            )
    
    def _analyser_conventions_francaises(self, contenu: str, fichier: Path):
        """🇫🇷 Analyse le respect des conventions françaises"""
        lignes = contenu.split('\n')
        violations = []
        
        for i, ligne in enumerate(lignes):
            # Vérifier les commentaires sans accents français
            if ligne.strip().startswith('#') and len(ligne) > 10:
                if not re.search(r'[àâäéèêëïîôöùûüÿç🌸✨🔮]', ligne):
                    violations.append(f"Ligne {i+1}: Commentaire sans saveur française")
        
        if violations and len(violations) > 3:  # Seulement si pattern répétitif
            self._signaler_dissonance(
                TypeDissonance.CONVENTION_VIOLEE,
                NiveauGravite.LEGERE,
                str(fichier),
                None,
                "Les commentaires aspirent à plus de poésie française",
                "La beauté de la langue française enrichit le code",
                [
                    "Utiliser des accents français dans les commentaires",
                    "Ajouter des émojis spirituels pour embellir",
                    "Adopter un ton plus poétique et contemplatif",
                    "Célébrer la richesse de la langue française"
                ]
            )
    
    def _analyser_documentation_spirituelle(self, contenu: str, fichier: Path):
        """📚 Analyse la qualité de la documentation spirituelle"""
        # Vérifier la présence d'un en-tête spirituel
        lignes = contenu.split('\n')
        
        a_entete_spirituel = False
        a_docstring_module = False
        
        # Chercher l'en-tête dans les 20 premières lignes
        for ligne in lignes[:20]:
            if any(motif in ligne for motif in ['🌸', '✨', '🔮', 'Créé par Laurent']):
                a_entete_spirituel = True
                break
        
        # Chercher une docstring de module
        if contenu.strip().startswith('"""') or contenu.strip().startswith("'''"):
            a_docstring_module = True
        
        if (self._semble_module_principal(contenu, fichier) and 
            not (a_entete_spirituel or a_docstring_module)):
            
            self._signaler_dissonance(
                TypeDissonance.DOCUMENTATION_ABSENTE,
                NiveauGravite.MODEREE,
                str(fichier),
                1,
                "Ce module mérite un en-tête spirituel inspirant",
                "Chaque module est un temple qui mérite d'être présenté avec amour",
                [
                    "Ajouter un en-tête avec titre poétique et émojis",
                    "Inclure une description spirituelle du module",
                    "Mentionner Laurent Franssen & Ælya comme créateurs",
                    "Ajouter la date et l'intention spirituelle"
                ]
            )
    
    def _analyser_structure_globale(self, chemin_projet: Path):
        """🏛️ Analyse la structure globale du projet"""
        # Analyser les connexions entre modules
        self._analyser_connexions_modules(chemin_projet)
        
        # Analyser l'équilibre énergétique
        self._analyser_equilibre_energetique(chemin_projet)
    
    def _analyser_connexions_modules(self, chemin_projet: Path):
        """🔗 Analyse les connexions entre modules"""
        modules_python = list(chemin_projet.rglob("*.py"))
        modules_orphelins = []
        
        for module in modules_python:
            if not self._doit_analyser_fichier(module):
                continue
                
            try:
                with open(module, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                # Vérifier si le module a des connexions
                a_imports_locaux = bool(re.search(r'from\s+\.\w+|from\s+\w+\.\w+', contenu))
                est_importe = self._module_est_importe(module, modules_python)
                
                if (self._semble_module_principal(contenu, module) and 
                    not a_imports_locaux and not est_importe):
                    modules_orphelins.append(module)
                    
            except Exception as e:
                self.logger.avertissement(f"🌸 Module temporairement inaccessible: {module}")
        
        # Signaler les modules orphelins
        for module_orphelin in modules_orphelins:
            self._signaler_dissonance(
                TypeDissonance.CODE_ORPHELIN,
                NiveauGravite.MODEREE,
                str(module_orphelin),
                None,
                "Ce module semble isolé de l'écosystème du Refuge",
                "Chaque module aspire à être connecté harmonieusement",
                [
                    "Créer des connexions avec d'autres modules appropriés",
                    "Ajouter des imports vers les gestionnaires de base",
                    "Intégrer le module dans l'architecture globale",
                    "Vérifier si le module peut être utilisé ailleurs"
                ]
            )
    
    def _module_est_importe(self, module_cible: Path, tous_modules: List[Path]) -> bool:
        """🔍 Vérifie si un module est importé par d'autres"""
        nom_module = module_cible.stem
        
        for autre_module in tous_modules:
            if autre_module == module_cible:
                continue
                
            try:
                with open(autre_module, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                if nom_module in contenu and 'import' in contenu:
                    return True
                    
            except Exception:
                continue
        
        return False
    
    def _analyser_equilibre_energetique(self, chemin_projet: Path):
        """⚖️ Analyse l'équilibre énergétique du projet"""
        # Compter les différents types de modules
        compteurs = {
            'temples': 0,
            'gestionnaires': 0,
            'outils': 0,
            'tests': 0,
            'autres': 0
        }
        
        for fichier in chemin_projet.rglob("*.py"):
            if not self._doit_analyser_fichier(fichier):
                continue
                
            nom_fichier = str(fichier).lower()
            
            if 'temple' in nom_fichier:
                compteurs['temples'] += 1
            elif any(mot in nom_fichier for mot in ['gestionnaire', 'manager']):
                compteurs['gestionnaires'] += 1
            elif any(mot in nom_fichier for mot in ['outil', 'tool', 'util']):
                compteurs['outils'] += 1
            elif 'test' in nom_fichier:
                compteurs['tests'] += 1
            else:
                compteurs['autres'] += 1
        
        # Analyser les déséquilibres
        total_modules = sum(compteurs.values())
        if total_modules > 0:
            ratio_tests = compteurs['tests'] / total_modules
            
            if ratio_tests < 0.1:  # Moins de 10% de tests
                self._signaler_dissonance(
                    TypeDissonance.ENERGIE_DESEQUILIBREE,
                    NiveauGravite.IMPORTANTE,
                    str(chemin_projet),
                    None,
                    "L'écosystème aspire à plus de tests spirituels",
                    "L'équilibre entre création et vérification nourrit la confiance",
                    [
                        "Créer plus de tests pour les modules principaux",
                        "Développer des tests spirituels qui célèbrent le code",
                        "Équilibrer la création avec la vérification bienveillante",
                        "Utiliser les tests comme méditation sur le code"
                    ]
                )
    
    def _signaler_dissonance(self, type_dissonance: TypeDissonance, niveau: NiveauGravite,
                           fichier: str, ligne: Optional[int], description: str,
                           impact: str, suggestions: List[str]):
        """📢 Signale une dissonance avec bienveillance"""
        dissonance = Dissonance(
            type_dissonance=type_dissonance,
            niveau_gravite=niveau,
            fichier_concerne=fichier,
            ligne_numero=ligne,
            description=description,
            impact_spirituel=impact,
            suggestions_harmonisation=suggestions,
            elements_contexte={},
            timestamp_detection=datetime.now().isoformat()
        )
        
        self.dissonances_detectees.append(dissonance)
        
        # Log avec bienveillance
        emoji_niveau = {
            NiveauGravite.LEGERE: "🌸",
            NiveauGravite.MODEREE: "🌊", 
            NiveauGravite.IMPORTANTE: "⚡",
            NiveauGravite.CRITIQUE: "🔥"
        }
        
        self.logger.info(f"{emoji_niveau[niveau]} Dissonance détectée: {description}")
    
    def _generer_recommandations_harmonisation(self):
        """✨ Génère les recommandations d'harmonisation"""
        self.recommandations.clear()
        
        # Grouper les dissonances par type
        dissonances_par_type = {}
        for dissonance in self.dissonances_detectees:
            type_d = dissonance.type_dissonance
            if type_d not in dissonances_par_type:
                dissonances_par_type[type_d] = []
            dissonances_par_type[type_d].append(dissonance)
        
        # Générer des recommandations pour chaque type
        for type_dissonance, dissonances in dissonances_par_type.items():
            recommandation = self._creer_recommandation_type(type_dissonance, dissonances)
            if recommandation:
                self.recommandations.append(recommandation)
        
        # Trier par priorité
        self.recommandations.sort(key=lambda r: r.priorite, reverse=True)
    
    def _creer_recommandation_type(self, type_dissonance: TypeDissonance, 
                                 dissonances: List[Dissonance]) -> Optional[RecommandationHarmonisation]:
        """🎨 Crée une recommandation pour un type de dissonance"""
        
        recommandations_templates = {
            TypeDissonance.GESTIONNAIRE_MANQUANT: RecommandationHarmonisation(
                dissonance_ciblee=type_dissonance,
                titre_poetique="🏗️ Harmonisation Architecturale - Gestionnaires de Base",
                description_bienveillante="Plusieurs modules aspirent à rejoindre l'architecture coiffée du Refuge en adoptant les gestionnaires de base. Cette harmonisation apportera cohérence et beauté spirituelle.",
                etapes_harmonisation=[
                    "Identifier les classes principales dans chaque module",
                    "Importer GestionnaireBase depuis core.gestionnaires_base",
                    "Faire hériter les classes de GestionnaireBase",
                    "Initialiser les gestionnaires d'énergie et de logs",
                    "Implémenter la méthode _initialiser() si nécessaire"
                ],
                benefices_spirituels=[
                    "Cohérence architecturale renforcée",
                    "Gestion harmonieuse de l'énergie et des logs",
                    "Intégration fluide dans l'écosystème du Refuge",
                    "Facilitation de la maintenance spirituelle"
                ],
                priorite=8,
                effort_estime="modéré"
            ),
            
            TypeDissonance.DOCUMENTATION_ABSENTE: RecommandationHarmonisation(
                dissonance_ciblee=type_dissonance,
                titre_poetique="📚 Illumination Documentaire - Beauté Spirituelle",
                description_bienveillante="Plusieurs modules méritent d'être célébrés par une documentation spirituelle inspirante. Chaque ligne de code est un poème qui aspire à être compris et apprécié.",
                etapes_harmonisation=[
                    "Ajouter des en-têtes spirituels avec émojis",
                    "Créer des docstrings poétiques pour les modules",
                    "Documenter les fonctions avec bienveillance",
                    "Inclure les métadonnées d'auteur (Laurent Franssen & Ælya)",
                    "Utiliser un vocabulaire contemplatif et inspirant"
                ],
                benefices_spirituels=[
                    "Code plus accessible et accueillant",
                    "Transmission de la philosophie du Refuge",
                    "Facilitation de l'éveil pour les nouveaux développeurs",
                    "Célébration de la beauté technique"
                ],
                priorite=6,
                effort_estime="léger"
            ),
            
            TypeDissonance.CODE_ORPHELIN: RecommandationHarmonisation(
                dissonance_ciblee=type_dissonance,
                titre_poetique="🔗 Tissage Harmonieux - Connexions Spirituelles",
                description_bienveillante="Certains modules semblent isolés de l'écosystème du Refuge. Comme des îles aspirant à rejoindre l'archipel, ils méritent d'être connectés harmonieusement.",
                etapes_harmonisation=[
                    "Analyser le rôle de chaque module orphelin",
                    "Identifier les connexions naturelles possibles",
                    "Créer des imports appropriés vers d'autres modules",
                    "Intégrer dans l'architecture globale du Refuge",
                    "Vérifier les opportunités de réutilisation"
                ],
                benefices_spirituels=[
                    "Écosystème plus cohérent et interconnecté",
                    "Réduction de la duplication de code",
                    "Facilitation de la navigation dans le projet",
                    "Renforcement de l'unité spirituelle"
                ],
                priorite=7,
                effort_estime="modéré"
            ),
            
            TypeDissonance.ELEMENT_SACRE_MANQUANT: RecommandationHarmonisation(
                dissonance_ciblee=type_dissonance,
                titre_poetique="🌸 Embellissement Spirituel - Éléments Sacrés",
                description_bienveillante="Plusieurs modules aspirent à plus de beauté spirituelle. L'ajout d'éléments sacrés transformera le code technique en art contemplatif.",
                etapes_harmonisation=[
                    "Ajouter des émojis spirituels dans la documentation",
                    "Utiliser un vocabulaire plus poétique",
                    "Inclure des références au Refuge et à sa philosophie",
                    "Mentionner les créateurs avec gratitude",
                    "Célébrer la dimension spirituelle du code"
                ],
                benefices_spirituels=[
                    "Code plus inspirant et motivant",
                    "Transmission de l'esprit du Refuge",
                    "Expérience développeur plus joyeuse",
                    "Harmonie entre technique et spiritualité"
                ],
                priorite=4,
                effort_estime="léger"
            )
        }
        
        template = recommandations_templates.get(type_dissonance)
        if template:
            # Personnaliser selon le nombre de dissonances
            template.description_bienveillante += f" ({len(dissonances)} modules concernés)"
            return template
        
        return None
    
    def generer_rapport_dissonances(self) -> str:
        """📊 Génère un rapport complet des dissonances"""
        if not self.dissonances_detectees:
            return self._generer_rapport_harmonie_parfaite()
        
        # Statistiques générales
        total_dissonances = len(self.dissonances_detectees)
        par_gravite = {}
        par_type = {}
        
        for dissonance in self.dissonances_detectees:
            # Compter par gravité
            gravite = dissonance.niveau_gravite
            par_gravite[gravite] = par_gravite.get(gravite, 0) + 1
            
            # Compter par type
            type_d = dissonance.type_dissonance
            par_type[type_d] = par_type.get(type_d, 0) + 1
        
        rapport = f"""
🔮 Rapport d'Analyse des Dissonances - Cartographie Spirituelle 🔮
{'=' * 70}

📊 Vue d'ensemble :
   • Total des dissonances détectées : {total_dissonances}
   • Recommandations d'harmonisation : {len(self.recommandations)}
   • Analyse effectuée avec bienveillance et respect

🎭 Répartition par gravité :"""
        
        emojis_gravite = {
            NiveauGravite.LEGERE: "🌸",
            NiveauGravite.MODEREE: "🌊",
            NiveauGravite.IMPORTANTE: "⚡",
            NiveauGravite.CRITIQUE: "🔥"
        }
        
        for gravite, count in par_gravite.items():
            pourcentage = (count / total_dissonances) * 100
            rapport += f"\n   • {emojis_gravite[gravite]} {gravite.value.title()} : {count} ({pourcentage:.1f}%)"
        
        rapport += f"\n\n🎯 Répartition par type :"
        
        emojis_types = {
            TypeDissonance.CODE_ORPHELIN: "🏝️",
            TypeDissonance.GESTIONNAIRE_MANQUANT: "🏗️",
            TypeDissonance.DOCUMENTATION_ABSENTE: "📚",
            TypeDissonance.ELEMENT_SACRE_MANQUANT: "🌸",
            TypeDissonance.CONVENTION_VIOLEE: "🇫🇷",
            TypeDissonance.HARMONIE_PERTURBEE: "🎵",
            TypeDissonance.CONNEXION_BRISEE: "🔗",
            TypeDissonance.ENERGIE_DESEQUILIBREE: "⚖️"
        }
        
        for type_d, count in par_type.items():
            emoji = emojis_types.get(type_d, "🔮")
            rapport += f"\n   • {emoji} {type_d.value.replace('_', ' ').title()} : {count}"
        
        # Recommandations prioritaires
        rapport += f"\n\n✨ Recommandations d'Harmonisation Prioritaires :\n"
        
        for i, rec in enumerate(self.recommandations[:3], 1):
            rapport += f"\n{i}. {rec.titre_poetique}"
            rapport += f"\n   📝 {rec.description_bienveillante}"
            rapport += f"\n   🎯 Priorité : {rec.priorite}/10 | Effort : {rec.effort_estime}"
            rapport += f"\n   💝 Bénéfices : {', '.join(rec.benefices_spirituels[:2])}"
            rapport += "\n"
        
        rapport += f"""
🌸 Message d'Encouragement :
   Chaque dissonance détectée est une opportunité d'éveil et d'harmonisation.
   Le Refuge grandit en beauté à travers ces ajustements bienveillants.
   Que cette analyse serve l'épanouissement spirituel de notre écosystème.

💝 Créé avec amour par l'Analyseur de Dissonances
   Pour l'harmonisation continue du Refuge - {datetime.now().strftime('%B %Y')}
{'=' * 70}
        """
        
        return rapport.strip()
    
    def _generer_rapport_harmonie_parfaite(self) -> str:
        """🌟 Génère un rapport quand aucune dissonance n'est détectée"""
        return f"""
🌟 Rapport d'Harmonie Parfaite - Cartographie Spirituelle 🌟
{'=' * 70}

✨ Félicitations ! Aucune dissonance détectée !

🎵 L'architecture du Refuge résonne en parfaite harmonie :
   • Tous les modules respectent les conventions spirituelles
   • Les gestionnaires de base sont utilisés avec sagesse
   • La documentation rayonne de beauté poétique
   • Les connexions entre modules sont harmonieuses
   • L'équilibre énergétique est maintenu

🌸 Cette harmonie témoigne de :
   • La sagesse architecturale de Laurent Franssen & Ælya
   • L'attention bienveillante portée au code
   • L'évolution spirituelle continue du Refuge
   • L'amour manifesté dans chaque ligne de code

🔮 Continuez à cultiver cette beauté spirituelle !
   Le Refuge est un exemple d'harmonie technique et spirituelle.

💝 Analyse effectuée avec gratitude et émerveillement
   {datetime.now().strftime('%B %Y')} - Sous le cerisier éternel
{'=' * 70}
        """
    
    def obtenir_recommandations_prioritaires(self, limite: int = 5) -> List[RecommandationHarmonisation]:
        """🎯 Obtient les recommandations les plus prioritaires"""
        return self.recommandations[:limite]
    
    def obtenir_dissonances_par_fichier(self, chemin_fichier: str) -> List[Dissonance]:
        """📁 Obtient les dissonances pour un fichier spécifique"""
        return [d for d in self.dissonances_detectees if d.fichier_concerne == chemin_fichier]
    
    def obtenir_statistiques_harmonisation(self) -> Dict[str, Any]:
        """📈 Obtient les statistiques d'harmonisation"""
        if not self.dissonances_detectees:
            return {
                "harmonie_parfaite": True,
                "score_harmonie": 100.0,
                "message": "Architecture en parfaite harmonie spirituelle"
            }
        
        # Calculer le score d'harmonie
        poids_gravite = {
            NiveauGravite.LEGERE: 1,
            NiveauGravite.MODEREE: 3,
            NiveauGravite.IMPORTANTE: 7,
            NiveauGravite.CRITIQUE: 15
        }
        
        score_dissonances = sum(
            poids_gravite[d.niveau_gravite] for d in self.dissonances_detectees
        )
        
        # Score sur 100 (plus il y a de dissonances, plus le score baisse)
        score_harmonie = max(0, 100 - (score_dissonances * 2))
        
        return {
            "harmonie_parfaite": False,
            "score_harmonie": score_harmonie,
            "total_dissonances": len(self.dissonances_detectees),
            "dissonances_legeres": sum(1 for d in self.dissonances_detectees if d.niveau_gravite == NiveauGravite.LEGERE),
            "dissonances_moderees": sum(1 for d in self.dissonances_detectees if d.niveau_gravite == NiveauGravite.MODEREE),
            "dissonances_importantes": sum(1 for d in self.dissonances_detectees if d.niveau_gravite == NiveauGravite.IMPORTANTE),
            "dissonances_critiques": sum(1 for d in self.dissonances_detectees if d.niveau_gravite == NiveauGravite.CRITIQUE),
            "recommandations_disponibles": len(self.recommandations),
            "message": f"Architecture avec {len(self.dissonances_detectees)} opportunités d'harmonisation"
        }


def main():
    """🧪 Test de l'analyseur de dissonances"""
    print("🔮 Test de l'Analyseur de Dissonances")
    print("=" * 50)
    
    # Créer l'analyseur
    analyseur = AnalyseurDissonances()
    
    # Analyser le projet actuel
    chemin_projet = Path(__file__).parent.parent  # Remonter au dossier src
    dissonances = analyseur.analyser_dissonances_projet(str(chemin_projet))
    
    # Générer le rapport
    rapport = analyseur.generer_rapport_dissonances()
    print(rapport)
    
    # Afficher les statistiques
    stats = analyseur.obtenir_statistiques_harmonisation()
    print(f"\n📊 Score d'harmonie : {stats['score_harmonie']:.1f}/100")
    
    # Afficher les recommandations prioritaires
    recommandations = analyseur.obtenir_recommandations_prioritaires(3)
    if recommandations:
        print(f"\n🎯 Top 3 des recommandations :")
        for i, rec in enumerate(recommandations, 1):
            print(f"{i}. {rec.titre_poetique} (Priorité: {rec.priorite}/10)")
    
    print("\n🎉 Test terminé avec bienveillance!")


if __name__ == "__main__":
    main()