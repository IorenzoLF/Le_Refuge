#!/usr/bin/env python3
"""
ANALYSEUR COMPLET DU REFUGE
===========================

Script d'analyse méthodique des 157 fichiers Python de la racine
- Classification par domaines logiques
- Analyse des imports et dépendances  
- Cartographie des interactions
- Recommandations de migration

Créé le 25/05/2025 - Session Laurent & Ælya
Méthodologie : "Méthode de la Boîte" appliquée à l'architecture
"""

import os
import re
import ast
import json
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

@dataclass
class FichierAnalyse:
    """Analyse complète d'un fichier Python"""
    nom: str
    taille: int
    lignes: int
    classes: List[str]
    fonctions: List[str]
    imports_locaux: List[str]
    imports_externes: List[str]
    domaine_suggere: str
    niveau_complexite: str
    est_principal: bool
    description: str

class AnalyseurRefugeComplet:
    """Analyseur méthodique du Refuge selon la méthode de la boîte"""
    
    def __init__(self):
        self.fichiers_analyses = {}
        self.dependances = defaultdict(set)
        self.imports_inverses = defaultdict(set)
        self.clusters = {}
        
        # Domaines identifiés selon notre méthodologie
        self.domaines_patterns = {
            "aelya": ["aelya", "conscience", "pulse", "dialogue", "repondeur"],
            "musique": ["harmonie", "melodie", "danse", "musical", "analyseur", "explorateur", "apprentissage"],
            "poesie": ["poetique", "poeme", "creation", "essence", "ancrage"],
            "rituels": ["rituel", "sacre", "meditation", "spirituel", "bain", "offrande", "clochette", "visualisation", "soumission"],
            "core": ["refuge_core", "main", "config", "base", "init", "boot", "constants"],
            "interface": ["interface", "web", "gui", "ui", "demarrer", "api"],
            "spheres": ["sphere", "gardien", "mobile", "jardinier", "unification"],
            "utils": ["util", "tool", "helper", "mapper", "carte", "recherche", "verification", "logger", "charger"],
            "tests": ["test_", "validation"],
            "flux": ["flux", "energie", "equilibre", "transformation", "integration", "harmonisation"],
            "elements": ["element", "cristaux", "facettes", "symbolique"],
            "gestion": ["gestion", "sauvegarde", "migration", "transition", "organiser"]
        }
    
    def analyser_fichier(self, chemin_fichier: str) -> FichierAnalyse:
        """Analyse complète d'un fichier selon la méthode de la boîte"""
        print(f"📂 Ouverture de la boîte : {chemin_fichier}")
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
        except UnicodeDecodeError:
            try:
                with open(chemin_fichier, 'r', encoding='latin-1') as f:
                    contenu = f.read()
            except Exception as e:
                print(f"❌ Erreur lecture {chemin_fichier}: {e}")
                return None
        
        nom = Path(chemin_fichier).stem
        taille = len(contenu)
        lignes = len(contenu.splitlines())
        
        # Analyse AST pour extraire classes et fonctions
        classes, fonctions = self._extraire_definitions(contenu)
        
        # Analyse des imports
        imports_locaux, imports_externes = self._analyser_imports(contenu)
        
        # Classification par domaine
        domaine = self._classifier_domaine(nom, classes, fonctions)
        
        # Évaluation de la complexité
        complexite = self._evaluer_complexite(lignes, len(classes), len(fonctions))
        
        # Détection si fichier principal
        est_principal = self._est_fichier_principal(nom, contenu)
        
        # Description automatique
        description = self._generer_description(nom, classes, fonctions, domaine)
        
        return FichierAnalyse(
            nom=nom,
            taille=taille,
            lignes=lignes,
            classes=classes,
            fonctions=fonctions,
            imports_locaux=imports_locaux,
            imports_externes=imports_externes,
            domaine_suggere=domaine,
            niveau_complexite=complexite,
            est_principal=est_principal,
            description=description
        )
    
    def _extraire_definitions(self, contenu: str) -> Tuple[List[str], List[str]]:
        """Extrait classes et fonctions via AST"""
        classes, fonctions = [], []
        
        try:
            arbre = ast.parse(contenu)
            for noeud in ast.walk(arbre):
                if isinstance(noeud, ast.ClassDef):
                    classes.append(noeud.name)
                elif isinstance(noeud, ast.FunctionDef):
                    fonctions.append(noeud.name)
        except SyntaxError:
            # Fallback avec regex si AST échoue
            classes = re.findall(r'^class\s+(\w+)', contenu, re.MULTILINE)
            fonctions = re.findall(r'^def\s+(\w+)', contenu, re.MULTILINE)
        
        return classes, fonctions
    
    def _analyser_imports(self, contenu: str) -> Tuple[List[str], List[str]]:
        """Analyse les imports locaux vs externes"""
        imports_locaux = []
        imports_externes = []
        
        # Patterns d'imports
        patterns = [
            r'from\s+(\w+)\s+import',
            r'import\s+(\w+)',
            r'from\s+\.(\w+)\s+import',
            r'from\s+\.\.(\w+)\s+import'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, contenu)
            for match in matches:
                # Heuristique : si le module commence par une majuscule ou est dans les modules standards
                if match in ['os', 'sys', 'json', 'datetime', 'pathlib', 'asyncio', 'sqlite3', 'logging', 'typing', 'dataclasses', 'collections', 'functools', 'itertools', 'math', 'random', 'time', 'threading', 'multiprocessing', 'requests', 'urllib', 'http', 'socket', 'email', 'csv', 'xml', 'html', 'base64', 'hashlib', 'uuid', 'subprocess', 'shutil', 'glob', 'pickle', 'gzip', 'zipfile', 'tarfile']:
                    imports_externes.append(match)
                else:
                    imports_locaux.append(match)
        
        return list(set(imports_locaux)), list(set(imports_externes))
    
    def _classifier_domaine(self, nom: str, classes: List[str], fonctions: List[str]) -> str:
        """Classification intelligente par domaine"""
        texte_analyse = f"{nom} {' '.join(classes)} {' '.join(fonctions)}".lower()
        
        scores = {}
        for domaine, patterns in self.domaines_patterns.items():
            score = sum(1 for pattern in patterns if pattern in texte_analyse)
            if score > 0:
                scores[domaine] = score
        
        if scores:
            return max(scores, key=scores.get)
        else:
            return "inclassable"
    
    def _evaluer_complexite(self, lignes: int, nb_classes: int, nb_fonctions: int) -> str:
        """Évalue la complexité du fichier"""
        score = lignes + nb_classes * 10 + nb_fonctions * 5
        
        if score < 50:
            return "simple"
        elif score < 200:
            return "moderate"
        elif score < 500:
            return "complexe"
        else:
            return "tres_complexe"
    
    def _est_fichier_principal(self, nom: str, contenu: str) -> bool:
        """Détecte si c'est un fichier principal/entry point"""
        indicateurs = [
            'if __name__ == "__main__"',
            'main()',
            'demarrer',
            'boot',
            'app.run',
            'FastAPI',
            'flask'
        ]
        
        return any(indicateur in contenu for indicateur in indicateurs)
    
    def _generer_description(self, nom: str, classes: List[str], fonctions: List[str], domaine: str) -> str:
        """Génère une description automatique"""
        if classes and fonctions:
            return f"Module {domaine} avec {len(classes)} classe(s) et {len(fonctions)} fonction(s)"
        elif classes:
            return f"Définitions de classe pour {domaine}"
        elif fonctions:
            return f"Utilitaires {domaine} avec {len(fonctions)} fonction(s)"
        else:
            return f"Script {domaine}"
    
    def analyser_tous_fichiers(self) -> Dict[str, FichierAnalyse]:
        """Analyse tous les fichiers .py de la racine"""
        print("🔍 === ANALYSE COMPLÈTE DU REFUGE - MÉTHODE DE LA BOÎTE ===")
        print()
        
        fichiers_py = [f for f in os.listdir('.') if f.endswith('.py')]
        print(f"📋 {len(fichiers_py)} fichiers Python détectés dans la racine")
        print()
        
        for fichier in sorted(fichiers_py):
            analyse = self.analyser_fichier(fichier)
            if analyse:
                self.fichiers_analyses[fichier] = analyse
                
                # Construction des graphes de dépendances
                for import_local in analyse.imports_locaux:
                    fichier_importe = f"{import_local}.py"
                    if fichier_importe in fichiers_py:
                        self.dependances[fichier].add(fichier_importe)
                        self.imports_inverses[fichier_importe].add(fichier)
        
        return self.fichiers_analyses
    
    def generer_rapport_complet(self) -> str:
        """Génère un rapport d'analyse détaillé"""
        if not self.fichiers_analyses:
            return "Aucune analyse effectuée"
        
        rapport = []
        rapport.append("# RAPPORT D'ANALYSE COMPLET DU REFUGE")
        rapport.append("## Analyse méthodique des 157 fichiers Python")
        rapport.append(f"*Généré le 25/05/2025 - Méthode de la Boîte*")
        rapport.append("")
        rapport.append("---")
        rapport.append("")
        
        # Statistiques générales
        total_fichiers = len(self.fichiers_analyses)
        total_lignes = sum(f.lignes for f in self.fichiers_analyses.values())
        total_classes = sum(len(f.classes) for f in self.fichiers_analyses.values())
        total_fonctions = sum(len(f.fonctions) for f in self.fichiers_analyses.values())
        
        rapport.append("## 📊 STATISTIQUES GÉNÉRALES")
        rapport.append("")
        rapport.append(f"- **Fichiers analysés** : {total_fichiers}")
        rapport.append(f"- **Lignes de code total** : {total_lignes:,}")
        rapport.append(f"- **Classes définies** : {total_classes}")
        rapport.append(f"- **Fonctions définies** : {total_fonctions}")
        rapport.append("")
        
        # Classification par domaines
        domaines_count = Counter(f.domaine_suggere for f in self.fichiers_analyses.values())
        
        rapport.append("## 🏗️ CLASSIFICATION PAR DOMAINES")
        rapport.append("")
        for domaine, count in domaines_count.most_common():
            emoji = self._get_emoji_domaine(domaine)
            rapport.append(f"- **{emoji} {domaine.upper()}** : {count} fichiers")
        rapport.append("")
        
        # Analyse des dépendances
        rapport.append("## 🔗 ANALYSE DES DÉPENDANCES")
        rapport.append("")
        
        # Fichiers les plus importés
        fichiers_populaires = Counter()
        for importeurs in self.imports_inverses.values():
            for importeur in importeurs:
                fichiers_populaires[importeur] += 1
        
        if fichiers_populaires:
            rapport.append("### 📈 Modules les plus importés (centraux)")
            for fichier, nb_imports in fichiers_populaires.most_common(10):
                analyse = self.fichiers_analyses.get(fichier)
                if analyse:
                    rapport.append(f"- **{fichier}** ({analyse.domaine_suggere}) : {nb_imports} imports")
            rapport.append("")
        
        # Fichiers avec le plus de dépendances
        fichiers_dependants = [(f, len(deps)) for f, deps in self.dependances.items() if deps]
        fichiers_dependants.sort(key=lambda x: x[1], reverse=True)
        
        if fichiers_dependants:
            rapport.append("### 🕸️ Fichiers avec le plus de dépendances")
            for fichier, nb_deps in fichiers_dependants[:10]:
                analyse = self.fichiers_analyses.get(fichier)
                if analyse:
                    rapport.append(f"- **{fichier}** ({analyse.domaine_suggere}) : {nb_deps} dépendances")
            rapport.append("")
        
        # Détail par domaine
        rapport.append("## 📂 DÉTAIL PAR DOMAINE")
        rapport.append("")
        
        for domaine in sorted(domaines_count.keys()):
            fichiers_domaine = [f for f in self.fichiers_analyses.values() if f.domaine_suggere == domaine]
            emoji = self._get_emoji_domaine(domaine)
            
            rapport.append(f"### {emoji} DOMAINE {domaine.upper()}")
            rapport.append("")
            
            for fichier in sorted(fichiers_domaine, key=lambda x: x.nom):
                deps = len(self.dependances.get(f"{fichier.nom}.py", []))
                importeurs = len(self.imports_inverses.get(f"{fichier.nom}.py", []))
                
                rapport.append(f"#### {fichier.nom}.py")
                rapport.append(f"- **Description** : {fichier.description}")
                rapport.append(f"- **Complexité** : {fichier.niveau_complexite} ({fichier.lignes} lignes)")
                rapport.append(f"- **Classes** : {', '.join(fichier.classes) if fichier.classes else 'Aucune'}")
                rapport.append(f"- **Dépendances** : {deps} / **Importé par** : {importeurs}")
                if fichier.est_principal:
                    rapport.append(f"- **🚀 FICHIER PRINCIPAL** (entry point)")
                rapport.append("")
        
        # Recommandations de migration
        rapport.append("## 🎯 RECOMMANDATIONS DE MIGRATION")
        rapport.append("")
        
        # Ordre de migration suggéré
        rapport.append("### 📋 Ordre de migration suggéré")
        rapport.append("")
        rapport.append("**Phase 1 - Modules indépendants :**")
        independants = [f for f, deps in self.dependances.items() if not deps]
        for fichier in sorted(independants):
            analyse = self.fichiers_analyses.get(fichier)
            if analyse:
                rapport.append(f"- {fichier} → `scripts/{analyse.domaine_suggere}/`")
        rapport.append("")
        
        rapport.append("**Phase 2 - Modules avec peu de dépendances :**")
        peu_dependants = [f for f, deps in self.dependances.items() if 0 < len(deps) <= 2]
        for fichier in sorted(peu_dependants):
            analyse = self.fichiers_analyses.get(fichier)
            if analyse:
                deps_str = ', '.join(self.dependances[fichier])
                rapport.append(f"- {fichier} → `scripts/{analyse.domaine_suggere}/` (dépend de: {deps_str})")
        rapport.append("")
        
        rapport.append("**Phase 3 - Modules complexes :**")
        tres_dependants = [f for f, deps in self.dependances.items() if len(deps) > 2]
        for fichier in sorted(tres_dependants):
            analyse = self.fichiers_analyses.get(fichier)
            if analyse:
                rapport.append(f"- {fichier} → `scripts/{analyse.domaine_suggere}/` ⚠️ Migration délicate")
        rapport.append("")
        
        # Clusters d'interdépendance
        clusters = self._detecter_clusters()
        if clusters:
            rapport.append("### 🔗 Clusters d'interdépendance")
            rapport.append("*Groupes de fichiers qui s'importent mutuellement - à migrer ensemble*")
            rapport.append("")
            
            for i, cluster in enumerate(clusters, 1):
                rapport.append(f"**Cluster {i} :**")
                for fichier in sorted(cluster):
                    analyse = self.fichiers_analyses.get(fichier)
                    if analyse:
                        rapport.append(f"- {fichier} ({analyse.domaine_suggere})")
                rapport.append("")
        
        return "\n".join(rapport)
    
    def _get_emoji_domaine(self, domaine: str) -> str:
        """Retourne l'emoji correspondant au domaine"""
        emojis = {
            "aelya": "🧠",
            "musique": "🎵", 
            "poesie": "📜",
            "rituels": "🔮",
            "core": "⚙️",
            "interface": "🌐",
            "spheres": "🌸",
            "utils": "🛠️",
            "tests": "🧪",
            "flux": "💫",
            "elements": "💎",
            "gestion": "📋",
            "inclassable": "❓"
        }
        return emojis.get(domaine, "📄")
    
    def _detecter_clusters(self) -> List[Set[str]]:
        """Détecte les clusters de fichiers interdépendants"""
        clusters = []
        visites = set()
        
        def explorer_cluster(fichier, cluster_actuel):
            if fichier in visites:
                return
            visites.add(fichier)
            cluster_actuel.add(fichier)
            
            # Explorer les dépendances
            for dep in self.dependances.get(fichier, []):
                if dep not in visites:
                    explorer_cluster(dep, cluster_actuel)
            
            # Explorer les importeurs
            for importeur in self.imports_inverses.get(fichier, []):
                if importeur not in visites:
                    explorer_cluster(importeur, cluster_actuel)
        
        for fichier in self.dependances:
            if fichier not in visites:
                cluster = set()
                explorer_cluster(fichier, cluster)
                if len(cluster) > 1:  # Seulement les vrais clusters
                    clusters.append(cluster)
        
        return clusters
    
    def sauvegarder_analyse(self, fichier_sortie: str = "analyse_refuge_complet.json"):
        """Sauvegarde l'analyse en JSON pour usage ultérieur"""
        donnees = {
            "metadata": {
                "date_analyse": "2025-05-25",
                "methode": "Méthode de la Boîte",
                "total_fichiers": len(self.fichiers_analyses)
            },
            "fichiers": {
                nom: {
                    "domaine": analyse.domaine_suggere,
                    "taille": analyse.taille,
                    "lignes": analyse.lignes,
                    "classes": analyse.classes,
                    "fonctions": analyse.fonctions,
                    "imports_locaux": analyse.imports_locaux,
                    "complexite": analyse.niveau_complexite,
                    "est_principal": analyse.est_principal,
                    "description": analyse.description
                }
                for nom, analyse in self.fichiers_analyses.items()
            },
            "dependances": {
                fichier: list(deps) for fichier, deps in self.dependances.items()
            }
        }
        
        with open(fichier_sortie, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Analyse sauvegardée dans {fichier_sortie}")

def main():
    """Fonction principale d'analyse"""
    print("🌟 ANALYSEUR COMPLET DU REFUGE 🌟")
    print("Méthode : 'C'est comme une boîte, on ne la jette pas sans savoir ce qu'il y a dedans'")
    print()
    
    analyseur = AnalyseurRefugeComplet()
    
    # Analyse complète
    analyses = analyseur.analyser_tous_fichiers()
    
    print(f"✅ Analyse terminée : {len(analyses)} fichiers traités")
    print()
    
    # Génération du rapport
    rapport = analyseur.generer_rapport_complet()
    
    # Sauvegarde
    with open("rapport_analyse_refuge.md", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    analyseur.sauvegarder_analyse()
    
    print("📊 Rapport généré : rapport_analyse_refuge.md")
    print("💾 Données JSON : analyse_refuge_complet.json")
    print()
    print("🎯 Prêt pour la migration méthodique !")

if __name__ == "__main__":
    main() 