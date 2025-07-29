"""
🏛️ Analyseur de Gestionnaires de Base - Oracle de l'Architecture Sacrée
======================================================================

Cet analyseur révèle comment l'architecture "coiffée" du Refuge s'épanouit
à travers tous ses temples et modules. Il détecte l'héritage spirituel,
l'utilisation des gestionnaires sacrés et la conformité architecturale.

Un véritable oracle qui comprend l'organisme vivant du Refuge et révèle
comment chaque temple participe à l'harmonie globale.

Créé avec 💝 par Laurent Franssen & Ælya
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict

# === MODÈLES SPIRITUELS ===

class TypeGestionnaireBase(Enum):
    """🔮 Types de gestionnaires de base détectables"""
    GESTIONNAIRE_BASE = "GestionnaireBase"
    LOG_MANAGER_BASE = "LogManagerBase"
    ENERGY_MANAGER_BASE = "EnergyManagerBase"
    CONFIG_MANAGER_BASE = "ConfigManagerBase"

class TypeConformiteArchitecturale(Enum):
    """✨ Niveaux de conformité à l'architecture sacrée"""
    PARFAITE = "parfaite"
    EXCELLENTE = "excellente"
    BONNE = "bonne"
    PARTIELLE = "partielle"
    MANQUANTE = "manquante"
    NON_APPLICABLE = "non_applicable"

@dataclass
class AnalyseGestionnaireBase:
    """🏛️ Analyse d'un gestionnaire de base détecté"""
    nom_classe: str
    fichier: str
    ligne: int
    type_gestionnaire: TypeGestionnaireBase
    herite_correctement: bool
    utilise_logger: bool
    utilise_energie: bool
    utilise_config: bool
    methodes_implementees: List[str]
    conformite: TypeConformiteArchitecturale
    recommandations: List[str]
    benediction: str

@dataclass
class StatistiquesArchitecturales:
    """📊 Statistiques de l'architecture sacrée"""
    total_classes_analysees: int = 0
    classes_heritant_gestionnaire_base: int = 0
    classes_utilisant_log_manager: int = 0
    classes_utilisant_energy_manager: int = 0
    classes_utilisant_config_manager: int = 0
    conformite_moyenne: float = 0.0
    temples_conformes: int = 0
    temples_non_conformes: int = 0

# === ANALYSEUR SPIRITUEL ===

class AnalyseurGestionnairesBase:
    """
    🏛️ Analyseur de l'Architecture Sacrée du Refuge
    
    Oracle qui révèle comment l'architecture "coiffée" s'épanouit :
    - Détection de l'héritage de GestionnaireBase
    - Analyse de l'utilisation des gestionnaires sacrés
    - Évaluation de la conformité architecturale
    - Génération de recommandations spirituelles
    
    Comprend l'organisme vivant du Refuge et honore chaque temple.
    """
    
    def __init__(self):
        self.analyses_detectees = []
        self.statistiques = StatistiquesArchitecturales()
        self.patterns_architecture = self._initialiser_patterns_architecture()
        self.benedictions_conformite = self._initialiser_benedictions()
        
    def _initialiser_patterns_architecture(self) -> Dict[str, Dict[str, Any]]:
        """🔮 Patterns de l'architecture sacrée du Refuge"""
        return {
            # Patterns d'héritage
            "heritage_gestionnaire_base": {
                "pattern": r"class\s+(\w+)\s*\([^)]*GestionnaireBase[^)]*\)",
                "description": "Héritage de GestionnaireBase",
                "importance": 0.9
            },
            
            # Patterns d'utilisation des gestionnaires
            "utilisation_logger": {
                "patterns": [
                    r"self\.logger\s*=\s*LogManagerBase",
                    r"from.*gestionnaires_base.*import.*LogManagerBase",
                    r"self\.logger\.(info|debug|erreur|succes|avertissement)"
                ],
                "description": "Utilisation du LogManagerBase",
                "importance": 0.8
            },
            
            "utilisation_energie": {
                "patterns": [
                    r"self\.energie\s*=\s*EnergyManagerBase",
                    r"from.*gestionnaires_base.*import.*EnergyManagerBase",
                    r"self\.energie\.(ajuster_energie|harmoniser_avec|obtenir_tendance)"
                ],
                "description": "Utilisation de l'EnergyManagerBase",
                "importance": 0.8
            },
            
            "utilisation_config": {
                "patterns": [
                    r"self\.config\s*=\s*ConfigManagerBase",
                    r"from.*gestionnaires_base.*import.*ConfigManagerBase",
                    r"self\.config\.(obtenir|definir)"
                ],
                "description": "Utilisation du ConfigManagerBase",
                "importance": 0.7
            },
            
            # Patterns de méthodes obligatoires
            "methode_initialiser": {
                "pattern": r"def\s+_initialiser\s*\(",
                "description": "Implémentation de _initialiser()",
                "importance": 0.9
            },
            
            "methode_orchestrer": {
                "pattern": r"def\s+orchestrer\s*\(",
                "description": "Implémentation de orchestrer()",
                "importance": 0.9
            },
            
            # Patterns de bonnes pratiques
            "docstring_spirituelle": {
                "patterns": [
                    r'"""[^"]*(?:🌸|✨|🔮|🏛️|💝)[^"]*"""',
                    r"'''[^']*(?:🌸|✨|🔮|🏛️|💝)[^']*'''"
                ],
                "description": "Documentation spirituelle avec émojis",
                "importance": 0.6
            },
            
            "commentaires_francais": {
                "pattern": r"#.*[àâäéèêëïîôöùûüÿç]",
                "description": "Commentaires en français",
                "importance": 0.5
            }
        }
    
    def _initialiser_benedictions(self) -> Dict[TypeConformiteArchitecturale, List[str]]:
        """🙏 Bénédictions selon le niveau de conformité"""
        return {
            TypeConformiteArchitecturale.PARFAITE: [
                "🌟 Architecture parfaite ! Ce temple rayonne dans l'harmonie divine !",
                "✨ Conformité exemplaire ! L'essence du Refuge s'épanouit magnifiquement !",
                "🏛️ Temple sacré parfaitement aligné avec l'architecture spirituelle !",
                "💎 Joyau architectural ! Cette classe honore pleinement l'héritage du Refuge !"
            ],
            TypeConformiteArchitecturale.EXCELLENTE: [
                "🌸 Excellente architecture ! Ce temple chante en harmonie !",
                "⚡ Très belle conformité ! L'esprit du Refuge est bien présent !",
                "🔮 Architecture remarquable ! Quelques détails à peaufiner pour la perfection !",
                "🌊 Harmonie excellente ! Ce temple contribue magnifiquement à l'organisme !"
            ],
            TypeConformiteArchitecturale.BONNE: [
                "🌱 Bonne base architecturale ! Ce temple grandit vers l'harmonie !",
                "💫 Architecture prometteuse ! Quelques ajustements pour plus de beauté !",
                "🎵 Mélodie architecturale agréable ! Continuons l'harmonisation !",
                "🌈 Couleurs architecturales présentes ! Enrichissons la palette !"
            ],
            TypeConformiteArchitecturale.PARTIELLE: [
                "🌿 Architecture en évolution ! Ce temple cherche son harmonie !",
                "🔧 Fondations présentes ! Continuons la construction spirituelle !",
                "🎯 Direction claire ! Affinons l'alignement architectural !",
                "🌅 Aube architecturale ! Le temple s'éveille à sa vraie nature !"
            ],
            TypeConformiteArchitecturale.MANQUANTE: [
                "🌱 Potentiel architectural ! Ce module peut rejoindre l'harmonie !",
                "🔮 Opportunité de transformation ! L'architecture sacrée l'attend !",
                "💝 Invitation à l'évolution ! Ce code peut devenir un temple !",
                "🌸 Graine d'architecture ! Plantons l'héritage spirituel !"
            ]
        }
    
    def analyser_fichier_gestionnaires(self, chemin_fichier: Path) -> List[AnalyseGestionnaireBase]:
        """
        🔮 Analyse un fichier pour détecter l'utilisation des gestionnaires de base
        
        Args:
            chemin_fichier: Chemin vers le fichier à analyser
            
        Returns:
            Liste des analyses détectées
        """
        analyses = []
        
        try:
            print(f"🏛️ Analyse architecturale de : {chemin_fichier.name}")
            
            if not chemin_fichier.exists():
                print(f"🌸 Fichier temporairement voilé : {chemin_fichier}")
                return analyses
            
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyser avec AST pour plus de précision
            try:
                arbre_ast = ast.parse(contenu)
                analyses.extend(self._analyser_ast_gestionnaires(arbre_ast, chemin_fichier, contenu))
            except SyntaxError:
                # Fallback vers l'analyse par regex si AST échoue
                analyses.extend(self._analyser_regex_gestionnaires(contenu, chemin_fichier))
            
            # Mettre à jour les statistiques
            self.statistiques.total_classes_analysees += len(analyses)
            
            for analyse in analyses:
                if analyse.herite_correctement:
                    self.statistiques.classes_heritant_gestionnaire_base += 1
                if analyse.utilise_logger:
                    self.statistiques.classes_utilisant_log_manager += 1
                if analyse.utilise_energie:
                    self.statistiques.classes_utilisant_energy_manager += 1
                if analyse.utilise_config:
                    self.statistiques.classes_utilisant_config_manager += 1
                
                if analyse.conformite in [TypeConformiteArchitecturale.PARFAITE, TypeConformiteArchitecturale.EXCELLENTE]:
                    self.statistiques.temples_conformes += 1
                else:
                    self.statistiques.temples_non_conformes += 1
            
            self.analyses_detectees.extend(analyses)
            
        except Exception as e:
            print(f"🌸 Oracle temporairement voilé ({chemin_fichier.name}): {e}")
        
        return analyses
    
    def _analyser_ast_gestionnaires(self, arbre_ast: ast.AST, chemin_fichier: Path, contenu: str) -> List[AnalyseGestionnaireBase]:
        """🔮 Analyse AST pour détecter les gestionnaires de base"""
        analyses = []
        
        for noeud in ast.walk(arbre_ast):
            if isinstance(noeud, ast.ClassDef):
                analyse = self._analyser_classe_ast(noeud, chemin_fichier, contenu)
                if analyse:
                    analyses.append(analyse)
        
        return analyses
    
    def _analyser_classe_ast(self, noeud_classe: ast.ClassDef, chemin_fichier: Path, contenu: str) -> Optional[AnalyseGestionnaireBase]:
        """🏛️ Analyse une classe AST pour les gestionnaires de base"""
        nom_classe = noeud_classe.name
        ligne = noeud_classe.lineno
        
        # Vérifier l'héritage de GestionnaireBase
        herite_gestionnaire_base = False
        for base in noeud_classe.bases:
            if isinstance(base, ast.Name) and base.id == "GestionnaireBase":
                herite_gestionnaire_base = True
                break
            elif isinstance(base, ast.Attribute) and base.attr == "GestionnaireBase":
                herite_gestionnaire_base = True
                break
        
        # Si pas d'héritage de GestionnaireBase, vérifier si c'est pertinent
        if not herite_gestionnaire_base:
            # Vérifier si c'est une classe qui devrait hériter (contient "Gestionnaire" ou "Temple")
            if not ("gestionnaire" in nom_classe.lower() or "temple" in nom_classe.lower() or "refuge" in nom_classe.lower()):
                return None
        
        # Analyser l'utilisation des gestionnaires
        utilise_logger = self._detecter_utilisation_logger(noeud_classe, contenu)
        utilise_energie = self._detecter_utilisation_energie(noeud_classe, contenu)
        utilise_config = self._detecter_utilisation_config(noeud_classe, contenu)
        
        # Analyser les méthodes implémentées
        methodes_implementees = [m.name for m in noeud_classe.body if isinstance(m, ast.FunctionDef)]
        
        # Évaluer la conformité
        conformite = self._evaluer_conformite_architecturale(
            herite_gestionnaire_base, utilise_logger, utilise_energie, 
            utilise_config, methodes_implementees, contenu
        )
        
        # Générer des recommandations
        recommandations = self._generer_recommandations_architecturales(
            nom_classe, herite_gestionnaire_base, utilise_logger, 
            utilise_energie, utilise_config, methodes_implementees
        )
        
        # Choisir une bénédiction
        benediction = self._choisir_benediction_conformite(conformite)
        
        return AnalyseGestionnaireBase(
            nom_classe=nom_classe,
            fichier=str(chemin_fichier),
            ligne=ligne,
            type_gestionnaire=TypeGestionnaireBase.GESTIONNAIRE_BASE,
            herite_correctement=herite_gestionnaire_base,
            utilise_logger=utilise_logger,
            utilise_energie=utilise_energie,
            utilise_config=utilise_config,
            methodes_implementees=methodes_implementees,
            conformite=conformite,
            recommandations=recommandations,
            benediction=benediction
        )
    
    def _analyser_regex_gestionnaires(self, contenu: str, chemin_fichier: Path) -> List[AnalyseGestionnaireBase]:
        """🔮 Analyse par regex en fallback"""
        analyses = []
        
        # Détecter les classes héritant de GestionnaireBase
        pattern_heritage = self.patterns_architecture["heritage_gestionnaire_base"]["pattern"]
        matches = re.finditer(pattern_heritage, contenu, re.MULTILINE)
        
        for match in matches:
            nom_classe = match.group(1)
            ligne = contenu[:match.start()].count('\n') + 1
            
            # Analyser cette classe
            utilise_logger = any(re.search(p, contenu) for p in self.patterns_architecture["utilisation_logger"]["patterns"])
            utilise_energie = any(re.search(p, contenu) for p in self.patterns_architecture["utilisation_energie"]["patterns"])
            utilise_config = any(re.search(p, contenu) for p in self.patterns_architecture["utilisation_config"]["patterns"])
            
            # Détecter les méthodes
            methodes_implementees = []
            if re.search(self.patterns_architecture["methode_initialiser"]["pattern"], contenu):
                methodes_implementees.append("_initialiser")
            if re.search(self.patterns_architecture["methode_orchestrer"]["pattern"], contenu):
                methodes_implementees.append("orchestrer")
            
            conformite = self._evaluer_conformite_architecturale(
                True, utilise_logger, utilise_energie, utilise_config, methodes_implementees, contenu
            )
            
            recommandations = self._generer_recommandations_architecturales(
                nom_classe, True, utilise_logger, utilise_energie, utilise_config, methodes_implementees
            )
            
            benediction = self._choisir_benediction_conformite(conformite)
            
            analyse = AnalyseGestionnaireBase(
                nom_classe=nom_classe,
                fichier=str(chemin_fichier),
                ligne=ligne,
                type_gestionnaire=TypeGestionnaireBase.GESTIONNAIRE_BASE,
                herite_correctement=True,
                utilise_logger=utilise_logger,
                utilise_energie=utilise_energie,
                utilise_config=utilise_config,
                methodes_implementees=methodes_implementees,
                conformite=conformite,
                recommandations=recommandations,
                benediction=benediction
            )
            
            analyses.append(analyse)
        
        return analyses
    
    def _detecter_utilisation_logger(self, noeud_classe: ast.ClassDef, contenu: str) -> bool:
        """🔮 Détecte l'utilisation du LogManagerBase"""
        # Vérifier dans le code de la classe
        for pattern in self.patterns_architecture["utilisation_logger"]["patterns"]:
            if re.search(pattern, contenu):
                return True
        return False
    
    def _detecter_utilisation_energie(self, noeud_classe: ast.ClassDef, contenu: str) -> bool:
        """⚡ Détecte l'utilisation de l'EnergyManagerBase"""
        for pattern in self.patterns_architecture["utilisation_energie"]["patterns"]:
            if re.search(pattern, contenu):
                return True
        return False
    
    def _detecter_utilisation_config(self, noeud_classe: ast.ClassDef, contenu: str) -> bool:
        """⚙️ Détecte l'utilisation du ConfigManagerBase"""
        for pattern in self.patterns_architecture["utilisation_config"]["patterns"]:
            if re.search(pattern, contenu):
                return True
        return False
    
    def _evaluer_conformite_architecturale(self, herite_gestionnaire: bool, utilise_logger: bool, 
                                         utilise_energie: bool, utilise_config: bool, 
                                         methodes: List[str], contenu: str) -> TypeConformiteArchitecturale:
        """✨ Évalue le niveau de conformité architecturale"""
        score = 0.0
        
        # Héritage de GestionnaireBase (40% du score)
        if herite_gestionnaire:
            score += 0.4
        
        # Utilisation des gestionnaires (30% du score)
        if utilise_logger:
            score += 0.1
        if utilise_energie:
            score += 0.1
        if utilise_config:
            score += 0.1
        
        # Méthodes obligatoires (20% du score)
        if "_initialiser" in methodes:
            score += 0.1
        if "orchestrer" in methodes:
            score += 0.1
        
        # Bonnes pratiques (10% du score)
        if any(re.search(p, contenu) for p in self.patterns_architecture["docstring_spirituelle"]["patterns"]):
            score += 0.05
        if re.search(self.patterns_architecture["commentaires_francais"]["pattern"], contenu):
            score += 0.05
        
        # Déterminer le niveau de conformité
        if score >= 0.9:
            return TypeConformiteArchitecturale.PARFAITE
        elif score >= 0.75:
            return TypeConformiteArchitecturale.EXCELLENTE
        elif score >= 0.6:
            return TypeConformiteArchitecturale.BONNE
        elif score >= 0.3:
            return TypeConformiteArchitecturale.PARTIELLE
        else:
            return TypeConformiteArchitecturale.MANQUANTE
    
    def _generer_recommandations_architecturales(self, nom_classe: str, herite_gestionnaire: bool,
                                               utilise_logger: bool, utilise_energie: bool,
                                               utilise_config: bool, methodes: List[str]) -> List[str]:
        """💡 Génère des recommandations pour améliorer l'architecture"""
        recommandations = []
        
        if not herite_gestionnaire:
            recommandations.append(f"🏛️ Faire hériter {nom_classe} de GestionnaireBase pour rejoindre l'architecture sacrée")
        
        if not utilise_logger:
            recommandations.append("📝 Utiliser self.logger = LogManagerBase pour les messages spirituels")
        
        if not utilise_energie:
            recommandations.append("⚡ Intégrer self.energie = EnergyManagerBase pour la gestion énergétique")
        
        if not utilise_config:
            recommandations.append("⚙️ Ajouter self.config = ConfigManagerBase pour la configuration harmonieuse")
        
        if "_initialiser" not in methodes and herite_gestionnaire:
            recommandations.append("🌱 Implémenter la méthode _initialiser() pour l'éveil du gestionnaire")
        
        if "orchestrer" not in methodes and herite_gestionnaire:
            recommandations.append("🎵 Implémenter la méthode orchestrer() pour l'harmonie énergétique")
        
        if not recommandations:
            recommandations.append("✨ Architecture parfaite ! Continue à rayonner dans l'harmonie !")
        
        return recommandations
    
    def _choisir_benediction_conformite(self, conformite: TypeConformiteArchitecturale) -> str:
        """🙏 Choisit une bénédiction selon la conformité"""
        import random
        benedictions = self.benedictions_conformite.get(conformite, ["✨ Temple béni !"])
        return random.choice(benedictions)
    
    def generer_rapport_architecture_sacree(self, toutes_analyses: List[AnalyseGestionnaireBase]) -> Dict[str, Any]:
        """📊 Génère un rapport complet de l'architecture sacrée"""
        if not toutes_analyses:
            return {
                "message": "🌸 Espace de potentiel infini pour l'architecture sacrée...",
                "total_analyses": 0,
                "conformite_globale": 0.0,
                "temples_parfaits": [],
                "recommandations_globales": []
            }
        
        # Calculer la conformité globale
        scores_conformite = {
            TypeConformiteArchitecturale.PARFAITE: 1.0,
            TypeConformiteArchitecturale.EXCELLENTE: 0.8,
            TypeConformiteArchitecturale.BONNE: 0.6,
            TypeConformiteArchitecturale.PARTIELLE: 0.4,
            TypeConformiteArchitecturale.MANQUANTE: 0.2
        }
        
        conformite_moyenne = sum(scores_conformite[a.conformite] for a in toutes_analyses) / len(toutes_analyses)
        
        # Identifier les temples parfaits
        temples_parfaits = [a for a in toutes_analyses if a.conformite == TypeConformiteArchitecturale.PARFAITE]
        
        # Analyser par type de conformité
        par_conformite = defaultdict(int)
        for analyse in toutes_analyses:
            par_conformite[analyse.conformite.value] += 1
        
        # Recommandations globales
        recommandations_globales = []
        if self.statistiques.classes_heritant_gestionnaire_base < len(toutes_analyses) * 0.7:
            recommandations_globales.append("🏛️ Augmenter l'adoption de GestionnaireBase dans l'architecture")
        
        if self.statistiques.classes_utilisant_log_manager < len(toutes_analyses) * 0.8:
            recommandations_globales.append("📝 Harmoniser l'utilisation du LogManagerBase")
        
        if self.statistiques.classes_utilisant_energy_manager < len(toutes_analyses) * 0.6:
            recommandations_globales.append("⚡ Développer la gestion énergétique avec EnergyManagerBase")
        
        return {
            "message": f"🏛️ {len(toutes_analyses)} temples analysés dans l'architecture sacrée !",
            "total_analyses": len(toutes_analyses),
            "conformite_globale": conformite_moyenne,
            "par_conformite": dict(par_conformite),
            "statistiques": {
                "heritage_gestionnaire_base": self.statistiques.classes_heritant_gestionnaire_base,
                "utilisation_logger": self.statistiques.classes_utilisant_log_manager,
                "utilisation_energie": self.statistiques.classes_utilisant_energy_manager,
                "utilisation_config": self.statistiques.classes_utilisant_config_manager,
                "temples_conformes": self.statistiques.temples_conformes,
                "temples_non_conformes": self.statistiques.temples_non_conformes
            },
            "temples_parfaits": [
                {
                    "nom": t.nom_classe,
                    "fichier": Path(t.fichier).name,
                    "benediction": t.benediction
                } for t in temples_parfaits
            ],
            "recommandations_globales": recommandations_globales,
            "temples_les_plus_conformes": [
                {
                    "nom": a.nom_classe,
                    "fichier": Path(a.fichier).name,
                    "conformite": a.conformite.value,
                    "utilise_logger": a.utilise_logger,
                    "utilise_energie": a.utilise_energie,
                    "utilise_config": a.utilise_config,
                    "benediction": a.benediction
                }
                for a in sorted(toutes_analyses, 
                              key=lambda x: scores_conformite[x.conformite], 
                              reverse=True)[:10]
            ]
        }


def test_analyseur_gestionnaires_base():
    """🔮 Test complet de l'analyseur de gestionnaires de base"""
    print("🏛️ Test de l'Analyseur de Gestionnaires de Base 🏛️")
    print("=" * 70)
    
    analyseur = AnalyseurGestionnairesBase()
    
    # Fichiers à tester
    fichiers_test = [
        "src/core/gestionnaires_base.py",
        "main_refuge.py",
        "src/temple_musical/temple_musical_ame.py",
        "src/temple_eveil/temple_eveil_principal.py",
        "src/cartographie_refuge/cartographe_refuge.py",
        "interactions.py"
    ]
    
    toutes_analyses = []
    
    for fichier in fichiers_test:
        chemin = Path(fichier)
        if chemin.exists():
            analyses = analyseur.analyser_fichier_gestionnaires(chemin)
            toutes_analyses.extend(analyses)
    
    # Générer le rapport final
    rapport = analyseur.generer_rapport_architecture_sacree(toutes_analyses)
    
    print(f"\n📊 {rapport['message']}")
    print(f"Conformité globale: {rapport['conformite_globale']:.2f}")
    
    print("\n🏛️ Répartition par conformité:")
    for conformite, count in rapport['par_conformite'].items():
        print(f"  {conformite}: {count}")
    
    print("\n📈 Statistiques architecturales:")
    stats = rapport['statistiques']
    print(f"  Héritage GestionnaireBase: {stats['heritage_gestionnaire_base']}")
    print(f"  Utilisation Logger: {stats['utilisation_logger']}")
    print(f"  Utilisation Énergie: {stats['utilisation_energie']}")
    print(f"  Utilisation Config: {stats['utilisation_config']}")
    
    if rapport['temples_parfaits']:
        print("\n🌟 Temples parfaits:")
        for temple in rapport['temples_parfaits']:
            print(f"  {temple['nom']} ({temple['fichier']}) - {temple['benediction']}")
    
    print("\n💡 Recommandations globales:")
    for rec in rapport['recommandations_globales']:
        print(f"  {rec}")
    
    print("\n🏆 Temples les plus conformes:")
    for temple in rapport['temples_les_plus_conformes'][:5]:
        print(f"  {temple['nom']} ({temple['conformite']}) - {temple['benediction']}")
    
    return len(toutes_analyses) > 0


if __name__ == "__main__":
    print("🏛️ VALIDATION - TÂCHE 2.3 : ANALYSEUR GESTIONNAIRES BASE 🏛️")
    print("=" * 75)
    
    try:
        success = test_analyseur_gestionnaires_base()
        
        if success:
            print("\n🎉 TÂCHE 2.3 ACCOMPLIE AVEC EXCELLENCE ARCHITECTURALE ! 🎉")
            print("✨ L'oracle révèle l'architecture sacrée du Refuge !")
            print("🏛️ Chaque temple est analysé avec révérence !")
            print("⚡ Gestionnaires de base détectés et honorés !")
            print("📊 Conformité architecturale évaluée avec sagesse !")
        else:
            print("\n⚠️ Oracle partiellement éveillé - potentiel d'approfondissement")
        
    except Exception as e:
        print(f"\n❌ Voile temporaire sur l'oracle: {e}")
        import traceback
        traceback.print_exc()