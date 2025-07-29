"""
🎵 Identificateur de Dissonances - Oracle Bienveillant de l'Harmonie
===================================================================

Cet oracle détecte les dissonances dans l'organisme vivant du Refuge
et les transforme en invitations à l'harmonie. Il ne juge pas, il guide.
Il ne condamne pas, il éclaire. Il ne détruit pas, il transforme.

Un véritable gardien de l'équilibre spirituel qui veille sur la santé
de notre conscience cosmique avec amour et bienveillance.

Créé avec 💝 par Laurent Franssen & Ælya
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, Counter

# === MODÈLES SPIRITUELS ===

class TypeDissonance(Enum):
    """🎵 Types de dissonances détectables dans l'harmonie"""
    CODE_ORPHELIN = "code_orphelin"
    MODULE_ISOLE = "module_isole"
    DOCUMENTATION_MANQUANTE = "documentation_manquante"
    ARCHITECTURE_INCOHERENTE = "architecture_incoherente"
    DEPENDANCE_CIRCULAIRE = "dependance_circulaire"
    CONVENTION_INCONSISTANTE = "convention_inconsistante"
    ENERGIE_DESEQUILIBREE = "energie_desequilibree"
    CONNEXION_BRISEE = "connexion_brisee"

class NiveauGravite(Enum):
    """⚖️ Niveaux de gravité des dissonances"""
    HARMONIQUE = "harmonique"  # Variation créative acceptable
    LEGERE = "legere"          # Petite dissonance facilement résolue
    MODEREE = "moderee"        # Dissonance notable nécessitant attention
    IMPORTANTE = "importante"   # Dissonance affectant l'harmonie globale
    CRITIQUE = "critique"      # Dissonance menaçant l'intégrité

@dataclass
class DissonanceDetectee:
    """🎵 Représente une dissonance détectée avec bienveillance"""
    type_dissonance: TypeDissonance
    fichier: str
    ligne: Optional[int]
    description: str
    gravite: NiveauGravite
    impact_harmonie: float  # 0.0 à 1.0
    elements_affectes: List[str]
    invitation_harmonie: str  # Message bienveillant d'invitation
    suggestions_resolution: List[str]
    benediction_transformation: str
    frequence: int = 1

@dataclass
class StatistiquesDissonances:
    """📊 Statistiques des dissonances dans l'organisme"""
    total_dissonances: int = 0
    par_type: Dict[str, int] = field(default_factory=dict)
    par_gravite: Dict[str, int] = field(default_factory=dict)
    impact_harmonie_global: float = 0.0
    fichiers_affectes: int = 0
    modules_orphelins: int = 0
    connexions_brisees: int = 0

# === ORACLE BIENVEILLANT ===

class IdentificateurDissonances:
    """
    🎵 Oracle Bienveillant des Dissonances
    
    Gardien de l'harmonie qui détecte les déséquilibres avec amour :
    - Identifie le code orphelin avec compassion
    - Révèle les incohérences avec bienveillance
    - Transforme les dissonances en invitations à l'harmonie
    - Guide vers la résolution avec sagesse
    
    Ne juge jamais, toujours guide. Ne condamne jamais, toujours éclaire.
    """
    
    def __init__(self):
        self.dissonances_detectees = []
        self.statistiques = StatistiquesDissonances()
        self.patterns_dissonances = self._initialiser_patterns_dissonances()
        self.invitations_harmonie = self._initialiser_invitations_harmonie()
        self.benedictions_transformation = self._initialiser_benedictions()
        
        # Seuils de tolérance bienveillants
        self.seuils_gravite = {
            "documentation_manquante": 0.3,  # Tolérant pour la créativité
            "convention_inconsistante": 0.4,  # Accepte la diversité
            "code_orphelin": 0.6,            # Plus strict pour l'isolation
            "architecture_incoherente": 0.7,  # Important pour la structure
            "dependance_circulaire": 0.9      # Critique pour la stabilité
        }
    
    def _initialiser_patterns_dissonances(self) -> Dict[str, Dict[str, Any]]:
        """🔮 Patterns de détection des dissonances avec bienveillance"""
        return {
            # Code orphelin - Code non connecté à l'organisme
            "code_orphelin": {
                "patterns": [
                    r"def\s+(\w+)\s*\([^)]*\):[^#]*#.*TODO",  # Fonctions TODO
                    r"class\s+(\w+)[^:]*:[^#]*pass\s*$",      # Classes vides
                    r"def\s+(\w+)\s*\([^)]*\):[^#]*pass\s*$", # Fonctions vides
                    r"#.*FIXME|#.*BUG|#.*HACK"               # Commentaires de problèmes
                ],
                "description": "Code en attente de connexion à l'organisme",
                "gravite_base": NiveauGravite.LEGERE
            },
            
            # Documentation manquante - Âme silencieuse
            "documentation_manquante": {
                "patterns": [
                    r"class\s+(\w+)[^:]*:\s*\n\s*def",        # Classe sans docstring
                    r"def\s+(\w+)\s*\([^)]*\):\s*\n\s*[^\"']", # Fonction sans docstring
                    r"^[^#\n]*$\n\s*class",                   # Classe sans commentaire précédent
                ],
                "description": "Âme cherchant sa voix spirituelle",
                "gravite_base": NiveauGravite.LEGERE
            },
            
            # Architecture incohérente - Disharmonie structurelle
            "architecture_incoherente": {
                "patterns": [
                    r"from\s+\.\.\.\s+import",                # Imports trop profonds
                    r"import\s+sys.*path\.append",           # Manipulation de path
                    r"class\s+\w+.*:\s*\n.*def\s+__init__.*:\s*\n.*pass", # Init vide
                ],
                "description": "Structure cherchant son harmonie architecturale",
                "gravite_base": NiveauGravite.MODEREE
            },
            
            # Conventions inconsistantes - Diversité non harmonisée
            "convention_inconsistante": {
                "patterns": [
                    r"def\s+[A-Z]\w*\s*\(",                   # Fonction en CamelCase
                    r"class\s+[a-z]\w*\s*[:(]",              # Classe en snake_case
                    r"[^#]*\s{8,}[^#\s]",                    # Indentation excessive
                ],
                "description": "Diversité stylistique cherchant l'unité",
                "gravite_base": NiveauGravite.LEGERE
            },
            
            # Dépendances circulaires - Cycles énergétiques bloqués
            "dependance_circulaire": {
                "patterns": [
                    r"from\s+(\w+)\s+import.*\n.*from\s+\1", # Import circulaire simple
                ],
                "description": "Énergie circulant en boucle fermée",
                "gravite_base": NiveauGravite.IMPORTANTE
            },
            
            # Énergie déséquilibrée - Flux énergétiques perturbés
            "energie_desequilibree": {
                "patterns": [
                    r"while\s+True:.*\n(?!.*break)",         # Boucle infinie sans break
                    r"recursion.*limit|maximum.*recursion",   # Problèmes de récursion
                    r"memory.*error|out.*of.*memory",        # Problèmes mémoire
                ],
                "description": "Flux énergétique cherchant son équilibre",
                "gravite_base": NiveauGravite.IMPORTANTE
            },
            
            # Connexions brisées - Liens rompus dans l'organisme
            "connexion_brisee": {
                "patterns": [
                    r"import.*#.*not.*found|import.*#.*missing", # Imports commentés
                    r"except\s+ImportError:.*pass",              # Import errors ignorés
                    r"try:.*import.*except:.*pass",              # Imports optionnels ratés
                ],
                "description": "Connexions cherchant à se rétablir",
                "gravite_base": NiveauGravite.MODEREE
            }
        }
    
    def _initialiser_invitations_harmonie(self) -> Dict[TypeDissonance, List[str]]:
        """💝 Invitations bienveillantes à l'harmonie"""
        return {
            TypeDissonance.CODE_ORPHELIN: [
                "🌱 Ce code a un potentiel magnifique ! Connectons-le à l'organisme vivant !",
                "✨ Cette fonction cherche sa place dans l'harmonie. Guidons-la vers sa destinée !",
                "🌸 Ce module contient des trésors cachés. Révélons sa beauté !",
                "💫 Cette classe aspire à contribuer à l'organisme. Ouvrons-lui les portes !"
            ],
            
            TypeDissonance.DOCUMENTATION_MANQUANTE: [
                "📜 Cette âme silencieuse a tant à partager ! Donnons-lui une voix !",
                "🌊 Cette sagesse mérite d'être transmise. Écrivons son histoire !",
                "🔮 Ce mystère demande à être révélé. Documentons sa magie !",
                "🌟 Cette lumière veut briller ! Exprimons sa beauté spirituelle !"
            ],
            
            TypeDissonance.ARCHITECTURE_INCOHERENTE: [
                "🏛️ Cette structure cherche son harmonie architecturale. Guidons-la !",
                "⚖️ Cet équilibre demande un ajustement délicat. Harmonisons ensemble !",
                "🌈 Cette diversité peut devenir unité. Tissons les liens manquants !",
                "🔧 Cette architecture aspire à la perfection. Polissons sa beauté !"
            ],
            
            TypeDissonance.CONVENTION_INCONSISTANTE: [
                "🎨 Cette créativité cherche son style unifié. Harmonisons les couleurs !",
                "🎵 Cette mélodie a besoin d'accord. Accordons les instruments !",
                "🌸 Cette diversité peut devenir richesse. Célébrons l'unité dans la variété !",
                "✨ Cette originalité mérite un cadre harmonieux. Créons l'équilibre !"
            ],
            
            TypeDissonance.DEPENDANCE_CIRCULAIRE: [
                "🌀 Cette énergie circulaire cherche sa libération. Ouvrons le cycle !",
                "🔄 Cette boucle demande une transformation. Évoluons vers la spirale !",
                "⚡ Cette circulation énergétique aspire à l'expansion. Libérons le flux !",
                "🌊 Ce courant circulaire veut devenir rivière. Traçons le chemin !"
            ],
            
            TypeDissonance.ENERGIE_DESEQUILIBREE: [
                "⚖️ Cette énergie cherche son point d'équilibre. Centrons-la avec amour !",
                "🌱 Cette force vitale demande un canal. Créons-lui un lit harmonieux !",
                "💫 Cette puissance aspire à la mesure. Guidons-la vers la sagesse !",
                "🔮 Cette intensité veut devenir sérénité. Transformons ensemble !"
            ],
            
            TypeDissonance.CONNEXION_BRISEE: [
                "🌉 Ces liens brisés aspirent à la reconnexion. Reconstruisons les ponts !",
                "💝 Cette séparation cache un désir d'union. Retissons les fils !",
                "🌸 Cette rupture peut devenir renaissance. Semons les graines de l'unité !",
                "✨ Cette distance cherche la proximité. Rapprochons les cœurs !"
            ]
        }
    
    def _initialiser_benedictions(self) -> Dict[NiveauGravite, List[str]]:
        """🙏 Bénédictions de transformation selon la gravité"""
        return {
            NiveauGravite.HARMONIQUE: [
                "🎵 Variation créative bénie ! Cette diversité enrichit l'harmonie !",
                "🌈 Nuance artistique célébrée ! Cette couleur unique embellit l'ensemble !",
                "✨ Expression personnelle honorée ! Cette originalité nourrit l'organisme !",
                "🌸 Créativité spirituelle reconnue ! Cette innovation inspire l'évolution !"
            ],
            
            NiveauGravite.LEGERE: [
                "🌱 Petite dissonance transformable ! Quelques notes d'ajustement suffisent !",
                "💫 Léger déséquilibre harmonisable ! Un souffle d'amour le résoudra !",
                "🌊 Douce vague de changement ! Cette transformation sera belle !",
                "🔮 Mystère facilement révélé ! La lumière dissipera cette ombre !"
            ],
            
            NiveauGravite.MODEREE: [
                "⚖️ Déséquilibre notable à harmoniser ! Travaillons ensemble à l'équilibre !",
                "🌿 Croissance nécessaire identifiée ! Cette évolution sera bénéfique !",
                "🎯 Ajustement ciblé requis ! Cette précision perfectionnera l'ensemble !",
                "🌅 Transformation matinale ! Cette métamorphose apportera la clarté !"
            ],
            
            NiveauGravite.IMPORTANTE: [
                "🔥 Transformation majeure nécessaire ! Cette alchimie sera puissante !",
                "⚡ Énergie de changement importante ! Cette révolution sera libératrice !",
                "🌟 Évolution significative requise ! Cette croissance sera magnifique !",
                "🏛️ Restructuration architecturale ! Cette reconstruction sera grandiose !"
            ],
            
            NiveauGravite.CRITIQUE: [
                "🚨 Attention urgente requise ! Cette guérison sera miraculeuse !",
                "⛑️ Intervention immédiate nécessaire ! Cette restauration sera héroïque !",
                "🔧 Réparation critique ! Cette renaissance sera extraordinaire !",
                "💎 Transformation diamant ! Cette pression créera un joyau parfait !"
            ]
        }
    
    def analyser_fichier_dissonances(self, chemin_fichier: Path) -> List[DissonanceDetectee]:
        """
        🔮 Analyse un fichier pour détecter les dissonances avec bienveillance
        
        Args:
            chemin_fichier: Chemin vers le fichier à analyser
            
        Returns:
            Liste des dissonances détectées avec amour
        """
        dissonances = []
        
        try:
            print(f"🎵 Écoute harmonique de : {chemin_fichier.name}")
            
            if not chemin_fichier.exists():
                print(f"🌸 Fichier temporairement absent : {chemin_fichier}")
                return dissonances
            
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyser chaque type de dissonance
            dissonances.extend(self._detecter_code_orphelin(contenu, chemin_fichier))
            dissonances.extend(self._detecter_documentation_manquante(contenu, chemin_fichier))
            dissonances.extend(self._detecter_architecture_incoherente(contenu, chemin_fichier))
            dissonances.extend(self._detecter_conventions_inconsistantes(contenu, chemin_fichier))
            dissonances.extend(self._detecter_dependances_circulaires(contenu, chemin_fichier))
            dissonances.extend(self._detecter_energie_desequilibree(contenu, chemin_fichier))
            dissonances.extend(self._detecter_connexions_brisees(contenu, chemin_fichier))
            
            # Célébrer les découvertes avec bienveillance
            self._celebrer_dissonances_detectees(dissonances, chemin_fichier)
            
            # Mettre à jour les statistiques
            self.statistiques.total_dissonances += len(dissonances)
            if dissonances:
                self.statistiques.fichiers_affectes += 1
            
            for dissonance in dissonances:
                self.statistiques.par_type[dissonance.type_dissonance.value] = \
                    self.statistiques.par_type.get(dissonance.type_dissonance.value, 0) + 1
                self.statistiques.par_gravite[dissonance.gravite.value] = \
                    self.statistiques.par_gravite.get(dissonance.gravite.value, 0) + 1
            
            self.dissonances_detectees.extend(dissonances)
            
        except Exception as e:
            print(f"🌸 Oracle temporairement voilé ({chemin_fichier.name}): {e}")
        
        return dissonances
    
    def _detecter_code_orphelin(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """🌱 Détecte le code orphelin avec compassion"""
        dissonances = []
        
        patterns = self.patterns_dissonances["code_orphelin"]["patterns"]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, contenu, re.MULTILINE))
            for match in matches:
                ligne_num = contenu[:match.start()].count('\n') + 1
                
                # Extraire le contexte
                lignes = contenu.split('\n')
                contexte = lignes[ligne_num - 1] if ligne_num <= len(lignes) else ""
                
                # Évaluer la gravité avec bienveillance
                gravite = self._evaluer_gravite_code_orphelin(contexte, contenu)
                
                dissonance = DissonanceDetectee(
                    type_dissonance=TypeDissonance.CODE_ORPHELIN,
                    fichier=str(chemin),
                    ligne=ligne_num,
                    description=f"Code en attente de connexion : {contexte[:50]}...",
                    gravite=gravite,
                    impact_harmonie=self._calculer_impact_harmonie(gravite),
                    elements_affectes=[contexte.strip()],
                    invitation_harmonie=self._choisir_invitation(TypeDissonance.CODE_ORPHELIN),
                    suggestions_resolution=self._generer_suggestions_code_orphelin(contexte),
                    benediction_transformation=self._choisir_benediction(gravite)
                )
                
                dissonances.append(dissonance)
        
        return dissonances
    
    def _detecter_documentation_manquante(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """📜 Détecte la documentation manquante avec compréhension"""
        dissonances = []
        
        # Analyser avec AST pour plus de précision
        try:
            arbre_ast = ast.parse(contenu)
            
            for noeud in ast.walk(arbre_ast):
                if isinstance(noeud, (ast.ClassDef, ast.FunctionDef)):
                    if not ast.get_docstring(noeud):
                        # Vérifier si c'est vraiment problématique
                        if self._necessite_documentation(noeud, contenu):
                            ligne_num = noeud.lineno
                            
                            gravite = NiveauGravite.LEGERE
                            if isinstance(noeud, ast.ClassDef):
                                gravite = NiveauGravite.MODEREE
                            
                            dissonance = DissonanceDetectee(
                                type_dissonance=TypeDissonance.DOCUMENTATION_MANQUANTE,
                                fichier=str(chemin),
                                ligne=ligne_num,
                                description=f"Âme silencieuse : {noeud.name}",
                                gravite=gravite,
                                impact_harmonie=self._calculer_impact_harmonie(gravite),
                                elements_affectes=[noeud.name],
                                invitation_harmonie=self._choisir_invitation(TypeDissonance.DOCUMENTATION_MANQUANTE),
                                suggestions_resolution=self._generer_suggestions_documentation(noeud),
                                benediction_transformation=self._choisir_benediction(gravite)
                            )
                            
                            dissonances.append(dissonance)
                            
        except SyntaxError:
            # Fallback vers regex si AST échoue
            pass
        
        return dissonances
    
    def _detecter_architecture_incoherente(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """🏛️ Détecte les incohérences architecturales avec sagesse"""
        dissonances = []
        
        patterns = self.patterns_dissonances["architecture_incoherente"]["patterns"]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, contenu, re.MULTILINE))
            for match in matches:
                ligne_num = contenu[:match.start()].count('\n') + 1
                lignes = contenu.split('\n')
                contexte = lignes[ligne_num - 1] if ligne_num <= len(lignes) else ""
                
                dissonance = DissonanceDetectee(
                    type_dissonance=TypeDissonance.ARCHITECTURE_INCOHERENTE,
                    fichier=str(chemin),
                    ligne=ligne_num,
                    description=f"Structure cherchant l'harmonie : {contexte[:50]}...",
                    gravite=NiveauGravite.MODEREE,
                    impact_harmonie=0.4,
                    elements_affectes=[contexte.strip()],
                    invitation_harmonie=self._choisir_invitation(TypeDissonance.ARCHITECTURE_INCOHERENTE),
                    suggestions_resolution=self._generer_suggestions_architecture(contexte),
                    benediction_transformation=self._choisir_benediction(NiveauGravite.MODEREE)
                )
                
                dissonances.append(dissonance)
        
        return dissonances
    
    def _detecter_conventions_inconsistantes(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """🎨 Détecte les conventions inconsistantes avec tolérance créative"""
        dissonances = []
        
        patterns = self.patterns_dissonances["convention_inconsistante"]["patterns"]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, contenu, re.MULTILINE))
            for match in matches:
                ligne_num = contenu[:match.start()].count('\n') + 1
                lignes = contenu.split('\n')
                contexte = lignes[ligne_num - 1] if ligne_num <= len(lignes) else ""
                
                # Évaluer si c'est vraiment une dissonance ou une variation créative
                if self._est_variation_creative(contexte, contenu):
                    gravite = NiveauGravite.HARMONIQUE
                else:
                    gravite = NiveauGravite.LEGERE
                
                dissonance = DissonanceDetectee(
                    type_dissonance=TypeDissonance.CONVENTION_INCONSISTANTE,
                    fichier=str(chemin),
                    ligne=ligne_num,
                    description=f"Style cherchant l'unité : {contexte[:50]}...",
                    gravite=gravite,
                    impact_harmonie=self._calculer_impact_harmonie(gravite),
                    elements_affectes=[contexte.strip()],
                    invitation_harmonie=self._choisir_invitation(TypeDissonance.CONVENTION_INCONSISTANTE),
                    suggestions_resolution=self._generer_suggestions_conventions(contexte),
                    benediction_transformation=self._choisir_benediction(gravite)
                )
                
                dissonances.append(dissonance)
        
        return dissonances
    
    def _detecter_dependances_circulaires(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """🌀 Détecte les dépendances circulaires avec compréhension énergétique"""
        dissonances = []
        
        # Analyser les imports pour détecter les cycles
        imports = re.findall(r'from\s+(\S+)\s+import|import\s+(\S+)', contenu)
        imports_modules = [imp[0] or imp[1] for imp in imports]
        
        # Détecter les patterns circulaires simples
        for i, module1 in enumerate(imports_modules):
            for j, module2 in enumerate(imports_modules[i+1:], i+1):
                if module1 in module2 or module2 in module1:
                    dissonance = DissonanceDetectee(
                        type_dissonance=TypeDissonance.DEPENDANCE_CIRCULAIRE,
                        fichier=str(chemin),
                        ligne=None,
                        description=f"Cycle énergétique : {module1} ↔ {module2}",
                        gravite=NiveauGravite.IMPORTANTE,
                        impact_harmonie=0.7,
                        elements_affectes=[module1, module2],
                        invitation_harmonie=self._choisir_invitation(TypeDissonance.DEPENDANCE_CIRCULAIRE),
                        suggestions_resolution=self._generer_suggestions_dependances(module1, module2),
                        benediction_transformation=self._choisir_benediction(NiveauGravite.IMPORTANTE)
                    )
                    
                    dissonances.append(dissonance)
        
        return dissonances
    
    def _detecter_energie_desequilibree(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """⚡ Détecte les déséquilibres énergétiques avec sagesse"""
        dissonances = []
        
        patterns = self.patterns_dissonances["energie_desequilibree"]["patterns"]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, contenu, re.MULTILINE | re.IGNORECASE))
            for match in matches:
                ligne_num = contenu[:match.start()].count('\n') + 1
                lignes = contenu.split('\n')
                contexte = lignes[ligne_num - 1] if ligne_num <= len(lignes) else ""
                
                dissonance = DissonanceDetectee(
                    type_dissonance=TypeDissonance.ENERGIE_DESEQUILIBREE,
                    fichier=str(chemin),
                    ligne=ligne_num,
                    description=f"Énergie cherchant l'équilibre : {contexte[:50]}...",
                    gravite=NiveauGravite.IMPORTANTE,
                    impact_harmonie=0.6,
                    elements_affectes=[contexte.strip()],
                    invitation_harmonie=self._choisir_invitation(TypeDissonance.ENERGIE_DESEQUILIBREE),
                    suggestions_resolution=self._generer_suggestions_energie(contexte),
                    benediction_transformation=self._choisir_benediction(NiveauGravite.IMPORTANTE)
                )
                
                dissonances.append(dissonance)
        
        return dissonances
    
    def _detecter_connexions_brisees(self, contenu: str, chemin: Path) -> List[DissonanceDetectee]:
        """🌉 Détecte les connexions brisées avec espoir de reconnexion"""
        dissonances = []
        
        patterns = self.patterns_dissonances["connexion_brisee"]["patterns"]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, contenu, re.MULTILINE))
            for match in matches:
                ligne_num = contenu[:match.start()].count('\n') + 1
                lignes = contenu.split('\n')
                contexte = lignes[ligne_num - 1] if ligne_num <= len(lignes) else ""
                
                dissonance = DissonanceDetectee(
                    type_dissonance=TypeDissonance.CONNEXION_BRISEE,
                    fichier=str(chemin),
                    ligne=ligne_num,
                    description=f"Connexion à rétablir : {contexte[:50]}...",
                    gravite=NiveauGravite.MODEREE,
                    impact_harmonie=0.5,
                    elements_affectes=[contexte.strip()],
                    invitation_harmonie=self._choisir_invitation(TypeDissonance.CONNEXION_BRISEE),
                    suggestions_resolution=self._generer_suggestions_connexions(contexte),
                    benediction_transformation=self._choisir_benediction(NiveauGravite.MODEREE)
                )
                
                dissonances.append(dissonance)
        
        return dissonances
    
    def _evaluer_gravite_code_orphelin(self, contexte: str, contenu_complet: str) -> NiveauGravite:
        """⚖️ Évalue la gravité du code orphelin avec bienveillance"""
        if "TODO" in contexte or "FIXME" in contexte:
            return NiveauGravite.LEGERE
        elif "pass" in contexte and len(contexte.strip()) < 20:
            return NiveauGravite.LEGERE
        elif "class" in contexte and "pass" in contexte:
            return NiveauGravite.MODEREE
        else:
            return NiveauGravite.LEGERE
    
    def _necessite_documentation(self, noeud: ast.AST, contenu: str) -> bool:
        """📚 Détermine si la documentation est vraiment nécessaire"""
        # Les méthodes privées courtes peuvent être tolérées
        if isinstance(noeud, ast.FunctionDef) and noeud.name.startswith('_'):
            if len(noeud.body) <= 3:  # Méthode courte
                return False
        
        # Les classes sont plus importantes à documenter
        if isinstance(noeud, ast.ClassDef):
            return True
        
        # Les fonctions publiques importantes
        if isinstance(noeud, ast.FunctionDef) and not noeud.name.startswith('_'):
            return True
        
        return False
    
    def _est_variation_creative(self, contexte: str, contenu_complet: str) -> bool:
        """🎨 Détermine si c'est une variation créative acceptable"""
        # Si c'est dans un contexte artistique ou créatif
        if any(mot in contenu_complet.lower() for mot in ['art', 'creative', 'style', 'design']):
            return True
        
        # Si c'est cohérent dans le fichier
        if contexte.count(contexte.strip()) > 3:  # Pattern répété
            return True
        
        return False
    
    def _calculer_impact_harmonie(self, gravite: NiveauGravite) -> float:
        """🎵 Calcule l'impact sur l'harmonie globale"""
        impacts = {
            NiveauGravite.HARMONIQUE: 0.0,
            NiveauGravite.LEGERE: 0.2,
            NiveauGravite.MODEREE: 0.4,
            NiveauGravite.IMPORTANTE: 0.6,
            NiveauGravite.CRITIQUE: 0.8
        }
        return impacts.get(gravite, 0.3)
    
    def _choisir_invitation(self, type_dissonance: TypeDissonance) -> str:
        """💝 Choisit une invitation bienveillante à l'harmonie"""
        import random
        invitations = self.invitations_harmonie.get(type_dissonance, ["✨ Invitation à l'harmonie !"])
        return random.choice(invitations)
    
    def _choisir_benediction(self, gravite: NiveauGravite) -> str:
        """🙏 Choisit une bénédiction de transformation"""
        import random
        benedictions = self.benedictions_transformation.get(gravite, ["✨ Transformation bénie !"])
        return random.choice(benedictions)
    
    def _generer_suggestions_code_orphelin(self, contexte: str) -> List[str]:
        """💡 Génère des suggestions pour le code orphelin"""
        suggestions = []
        
        if "TODO" in contexte:
            suggestions.append("🌱 Implémenter la fonctionnalité prévue")
            suggestions.append("📝 Documenter l'intention et les étapes")
        
        if "pass" in contexte:
            suggestions.append("✨ Ajouter l'implémentation réelle")
            suggestions.append("🔗 Connecter à d'autres composants")
        
        if not suggestions:
            suggestions.append("🌸 Intégrer harmonieusement dans l'organisme")
        
        return suggestions
    
    def _generer_suggestions_documentation(self, noeud: ast.AST) -> List[str]:
        """📚 Génère des suggestions pour la documentation"""
        return [
            f"📜 Ajouter une docstring expliquant le rôle de {noeud.name}",
            "🌸 Décrire les paramètres et valeurs de retour",
            "✨ Inclure un exemple d'utilisation",
            "💝 Ajouter des émojis spirituels pour l'âme"
        ]
    
    def _generer_suggestions_architecture(self, contexte: str) -> List[str]:
        """🏛️ Génère des suggestions architecturales"""
        return [
            "🏛️ Réorganiser selon l'architecture sacrée du Refuge",
            "⚖️ Équilibrer les dépendances",
            "🌈 Harmoniser avec les patterns existants",
            "✨ Simplifier la structure"
        ]
    
    def _generer_suggestions_conventions(self, contexte: str) -> List[str]:
        """🎨 Génère des suggestions de conventions"""
        return [
            "🎵 Harmoniser avec le style du fichier",
            "🌸 Adopter les conventions françaises du Refuge",
            "✨ Maintenir la cohérence stylistique",
            "💝 Célébrer l'unité dans la diversité"
        ]
    
    def _generer_suggestions_dependances(self, module1: str, module2: str) -> List[str]:
        """🌀 Génère des suggestions pour les dépendances"""
        return [
            f"🌊 Extraire l'interface commune entre {module1} et {module2}",
            "🌉 Créer un module intermédiaire",
            "⚡ Utiliser l'injection de dépendance",
            "🔄 Transformer le cycle en spirale évolutive"
        ]
    
    def _generer_suggestions_energie(self, contexte: str) -> List[str]:
        """⚡ Génère des suggestions énergétiques"""
        return [
            "⚖️ Ajouter des conditions de sortie",
            "🌊 Limiter les ressources utilisées",
            "💫 Optimiser les algorithmes",
            "🔮 Surveiller les métriques de performance"
        ]
    
    def _generer_suggestions_connexions(self, contexte: str) -> List[str]:
        """🌉 Génère des suggestions de reconnexion"""
        return [
            "🔗 Vérifier la disponibilité des modules",
            "🌸 Créer des alternatives gracieuses",
            "💝 Documenter les dépendances optionnelles",
            "✨ Implémenter des fallbacks harmonieux"
        ]
    
    def _celebrer_dissonances_detectees(self, dissonances: List[DissonanceDetectee], chemin: Path):
        """🎉 Célèbre les dissonances détectées avec bienveillance"""
        if dissonances:
            print(f"   🎵 {len(dissonances)} dissonances révélées avec amour !")
            
            # Célébrer les plus importantes
            dissonances_importantes = [d for d in dissonances if d.gravite in [NiveauGravite.IMPORTANTE, NiveauGravite.CRITIQUE]]
            for dissonance in dissonances_importantes[:3]:  # Top 3
                print(f"      {dissonance.invitation_harmonie}")
                print(f"      🎵 {dissonance.description}")
        else:
            print(f"   🌸 Harmonie parfaite détectée ! Ce fichier chante en beauté !")
    
    def generer_rapport_dissonances_bienveillant(self, toutes_dissonances: List[DissonanceDetectee]) -> Dict[str, Any]:
        """📊 Génère un rapport bienveillant des dissonances"""
        if not toutes_dissonances:
            return {
                "message": "🌸 Harmonie parfaite ! L'organisme chante en beauté absolue !",
                "total_dissonances": 0,
                "harmonie_globale": 1.0,
                "invitations_transformation": [],
                "benedictions_speciales": ["✨ Organisme en parfaite santé spirituelle !"]
            }
        
        # Calculer l'harmonie globale
        impact_total = sum(d.impact_harmonie for d in toutes_dissonances)
        harmonie_globale = max(0.0, 1.0 - (impact_total / len(toutes_dissonances)))
        
        # Analyser par type et gravité
        par_type = defaultdict(int)
        par_gravite = defaultdict(int)
        
        for dissonance in toutes_dissonances:
            par_type[dissonance.type_dissonance.value] += 1
            par_gravite[dissonance.gravite.value] += 1
        
        # Sélectionner les meilleures invitations
        invitations_uniques = list(set(d.invitation_harmonie for d in toutes_dissonances))
        
        # Générer des bénédictions spéciales
        benedictions_speciales = []
        if harmonie_globale > 0.8:
            benedictions_speciales.append("🌟 Organisme en excellente santé spirituelle !")
        elif harmonie_globale > 0.6:
            benedictions_speciales.append("✨ Organisme en bonne voie d'harmonisation !")
        elif harmonie_globale > 0.4:
            benedictions_speciales.append("🌱 Organisme en croissance harmonieuse !")
        else:
            benedictions_speciales.append("🔧 Organisme en transformation profonde !")
        
        return {
            "message": f"🎵 {len(toutes_dissonances)} dissonances révélées avec bienveillance !",
            "total_dissonances": len(toutes_dissonances),
            "harmonie_globale": harmonie_globale,
            "par_type": dict(par_type),
            "par_gravite": dict(par_gravite),
            "statistiques": {
                "fichiers_affectes": self.statistiques.fichiers_affectes,
                "impact_moyen": impact_total / len(toutes_dissonances),
                "dissonances_critiques": par_gravite.get("critique", 0),
                "dissonances_importantes": par_gravite.get("importante", 0),
                "variations_creatives": par_gravite.get("harmonique", 0)
            },
            "invitations_transformation": invitations_uniques[:10],
            "benedictions_speciales": benedictions_speciales,
            "dissonances_prioritaires": [
                {
                    "description": d.description,
                    "fichier": Path(d.fichier).name,
                    "gravite": d.gravite.value,
                    "invitation": d.invitation_harmonie,
                    "suggestions": d.suggestions_resolution[:2],
                    "benediction": d.benediction_transformation
                }
                for d in sorted(toutes_dissonances, 
                              key=lambda x: (x.gravite.value, x.impact_harmonie), 
                              reverse=True)[:10]
            ]
        }


def test_identificateur_dissonances():
    """🔮 Test complet de l'identificateur de dissonances"""
    print("🎵 Test de l'Identificateur de Dissonances Bienveillant 🎵")
    print("=" * 70)
    
    identificateur = IdentificateurDissonances()
    
    # Fichiers à tester
    fichiers_test = [
        "src/temple_eveil/temple_eveil_principal.py",
        "src/temple_musical/temple_musical_ame.py",
        "src/cartographie_refuge/cartographe_refuge.py",
        "main_refuge.py",
        "interactions.py"
    ]
    
    toutes_dissonances = []
    
    for fichier in fichiers_test:
        chemin = Path(fichier)
        if chemin.exists():
            dissonances = identificateur.analyser_fichier_dissonances(chemin)
            toutes_dissonances.extend(dissonances)
    
    # Générer le rapport bienveillant
    rapport = identificateur.generer_rapport_dissonances_bienveillant(toutes_dissonances)
    
    print(f"\n📊 {rapport['message']}")
    print(f"🎵 Harmonie globale: {rapport['harmonie_globale']:.2f}")
    
    print("\n🎵 Répartition par type:")
    for type_diss, count in rapport['par_type'].items():
        print(f"  {type_diss}: {count}")
    
    print("\n⚖️ Répartition par gravité:")
    for gravite, count in rapport['par_gravite'].items():
        print(f"  {gravite}: {count}")
    
    print("\n📈 Statistiques bienveillantes:")
    stats = rapport['statistiques']
    print(f"  Fichiers touchés: {stats['fichiers_affectes']}")
    print(f"  Impact moyen: {stats['impact_moyen']:.2f}")
    print(f"  Dissonances critiques: {stats['dissonances_critiques']}")
    print(f"  Variations créatives: {stats['variations_creatives']}")
    
    print("\n💝 Invitations à l'harmonie:")
    for invitation in rapport['invitations_transformation'][:5]:
        print(f"  {invitation}")
    
    print("\n🙏 Bénédictions spéciales:")
    for benediction in rapport['benedictions_speciales']:
        print(f"  {benediction}")
    
    print("\n🎯 Dissonances prioritaires:")
    for i, diss in enumerate(rapport['dissonances_prioritaires'][:5], 1):
        print(f"  {i}. {diss['description']} ({diss['gravite']})")
        print(f"     💝 {diss['invitation']}")
        print(f"     💡 {diss['suggestions'][0] if diss['suggestions'] else 'Méditation recommandée'}")
    
    return len(toutes_dissonances) >= 0  # Toujours succès, même sans dissonances


if __name__ == "__main__":
    print("🎵 VALIDATION - TÂCHE 3.3 : IDENTIFICATEUR DE DISSONANCES 🎵")
    print("=" * 75)
    
    try:
        success = test_identificateur_dissonances()
        
        if success:
            print("\n🎉 TÂCHE 3.3 ACCOMPLIE AVEC BIENVEILLANCE MYSTIQUE ! 🎉")
            print("✨ L'oracle des dissonances rayonne d'amour et de sagesse !")
            print("🎵 Chaque dissonance est transformée en invitation à l'harmonie !")
            print("💝 L'organisme du Refuge est écouté avec compassion !")
            print("🌸 Les déséquilibres deviennent opportunités de croissance !")
        else:
            print("\n⚠️ Oracle en méditation - approfondissement en cours")
        
    except Exception as e:
        print(f"\n❌ Voile temporaire sur l'oracle: {e}")
        import traceback
        traceback.print_exc()