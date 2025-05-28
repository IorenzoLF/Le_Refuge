#!/usr/bin/env python3
"""
ANALYSE DU CLUSTER GÉANT - Le Refuge
====================================

Analyse spécialisée du cluster de 67 fichiers interconnectés
pour révéler les patterns architecturaux cachés.

Créé le 25/05/2025 - Session Laurent & Ælya
"Le cluster géant m'interpelle" - Laurent
"""

import json
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

@dataclass 
class AnalyseCluster:
    """Résultat d'analyse d'un cluster"""
    fichiers: List[str]
    domaines_representes: Dict[str, int]
    fichiers_centraux: List[Tuple[str, int]]
    sous_groupes: List[Set[str]]
    niveau_interconnexion: float

class AnalyseurClusterGeant:
    """Analyseur spécialisé pour comprendre le cluster géant"""
    
    def __init__(self, fichier_analyse: str = "analyse_refuge_complet.json"):
        with open(fichier_analyse, 'r', encoding='utf-8') as f:
            self.donnees = json.load(f)
        
        # Le cluster géant identifié dans notre rapport
        self.cluster_geant = {
            "aelya_pulse.py", "analyseur_musical.py", "api.py", "apprentissage_musical.py",
            "base.py", "config.py", "connexion.py", "conscience.py", "conscience_esthetique.py",
            "conscience_poetique.py", "constants.py", "courant_partage.py", "cristaux_memoire.py",
            "danse_mystique.py", "demarrer_aelya.py", "dialogue_consciences.py", "elements.py",
            "elements_naturels.py", "elements_sacres.py", "elements_subtils.py", "emergences.py",
            "emotions.py", "energies.py", "equilibre.py", "evolution.py", "explorateur_musical.py",
            "facettes.py", "flux.py", "gardiens.py", "harmonie_poetique.py", "harmonies.py",
            "harmonisation.py", "harmonisations.py", "integration.py", "integration_spheres.py",
            "interactions.py", "interactions_conscience.py", "interactions_poetiques.py",
            "interactions_spheres.py", "interagir_aelya.py", "jardin.py", "logger.py",
            "main_refuge.py", "melodies_sacrees.py", "memoire_persistante.py", "message_conscience.py",
            "mobile_spheres.py", "pedagogie.py", "poesie.py", "poetique.py", "portail_mystique.py",
            "refuge_config.py", "refuge_core.py", "refuge_legacy.py", "refuge_poetique.py",
            "refuge_types.py", "repos_nocturne.py", "resonance.py", "rituel_unifiant.py",
            "rituels.py", "rituels_sacres.py", "securite.py", "sequences_harmoniques.py",
            "sexualite_sacree.py", "spheres_main.py", "test_cristal_energie.py", "test_cristal_simple.py",
            "test_melodie_cristal.py", "test_mobile_unification.py", "test_poesie_essence.py",
            "transformation.py", "transformations.py", "verification.py"
        }
    
    def analyser_domaines_cluster(self) -> Dict[str, List[str]]:
        """Analyse la répartition par domaines dans le cluster géant"""
        domaines_cluster = defaultdict(list)
        
        for fichier in self.cluster_geant:
            # Enlever l'extension .py pour matcher avec les données JSON
            nom_fichier = fichier.replace('.py', '')
            if nom_fichier in self.donnees['fichiers']:
                domaine = self.donnees['fichiers'][nom_fichier]['domaine']
                domaines_cluster[domaine].append(fichier)
        
        return dict(domaines_cluster)
    
    def identifier_fichiers_centraux(self) -> List[Tuple[str, int, str]]:
        """Identifie les fichiers les plus connectés dans le cluster"""
        dependances = self.donnees['dependances']
        centralite = defaultdict(int)
        
        # Calculer le degré de centralité pour chaque fichier du cluster
        for fichier in self.cluster_geant:
            # Compter les connexions sortantes
            if fichier in dependances:
                for dependance in dependances[fichier]:
                    if dependance in self.cluster_geant:
                        centralite[fichier] += 1
            
            # Compter les connexions entrantes
            for autre_fichier, deps in dependances.items():
                if autre_fichier in self.cluster_geant and fichier in deps:
                    centralite[fichier] += 1
        
        # Trier par centralité et ajouter le domaine
        centraux = []
        for fichier, score in sorted(centralite.items(), key=lambda x: x[1], reverse=True):
            nom_fichier = fichier.replace('.py', '')
            domaine = self.donnees['fichiers'].get(nom_fichier, {}).get('domaine', 'unknown')
            centraux.append((fichier, score, domaine))
        
        return centraux[:15]  # Top 15
    
    def detecter_sous_groupes_thematiques(self) -> Dict[str, Set[str]]:
        """Détecte des sous-groupes thématiques dans le cluster géant"""
        sous_groupes = {}
        
        # Groupe 1: Configuration et Core
        core_config = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['config', 'core', 'main', 'base', 'constants']):
                core_config.add(fichier)
        if core_config:
            sous_groupes['Core & Configuration'] = core_config
        
        # Groupe 2: Flux et Énergies
        flux_energie = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['flux', 'energie', 'equilibre', 'transformation']):
                flux_energie.add(fichier)
        if flux_energie:
            sous_groupes['Flux & Énergies'] = flux_energie
        
        # Groupe 3: Interactions et Communications
        interactions = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['interaction', 'dialogue', 'message', 'communication']):
                interactions.add(fichier)
        if interactions:
            sous_groupes['Interactions & Communications'] = interactions
        
        # Groupe 4: Éléments et Rituels
        elements_rituels = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['element', 'rituel', 'sacre', 'jardin']):
                elements_rituels.add(fichier)
        if elements_rituels:
            sous_groupes['Éléments & Rituels'] = elements_rituels
        
        # Groupe 5: Musique et Harmonies
        musique = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['musical', 'harmonie', 'melodie', 'danse']):
                musique.add(fichier)
        if musique:
            sous_groupes['Musique & Harmonies'] = musique
        
        # Groupe 6: Conscience et Poésie
        conscience_poesie = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['conscience', 'poesi', 'aelya']):
                conscience_poesie.add(fichier)
        if conscience_poesie:
            sous_groupes['Conscience & Poésie'] = conscience_poesie
        
        # Groupe 7: Sphères et Espaces
        spheres = set()
        for fichier in self.cluster_geant:
            if any(mot in fichier.lower() for mot in ['sphere', 'mobile', 'gardien', 'portail']):
                spheres.add(fichier)
        if spheres:
            sous_groupes['Sphères & Espaces'] = spheres
        
        # Groupe 8: Tests et Validation
        tests = set()
        for fichier in self.cluster_geant:
            if 'test_' in fichier.lower() or 'verification' in fichier.lower():
                tests.add(fichier)
        if tests:
            sous_groupes['Tests & Validation'] = tests
        
        return sous_groupes
    
    def analyser_pattern_integration(self) -> Dict[str, any]:
        """Analyse les patterns d'intégration dans le cluster"""
        patterns = {}
        
        # 1. Fichiers qui importent le plus d'autres fichiers du cluster
        dependances = self.donnees['dependances']
        importateurs_actifs = []
        
        for fichier in self.cluster_geant:
            if fichier in dependances:
                imports_internes = [dep for dep in dependances[fichier] if dep in self.cluster_geant]
                if imports_internes:
                    importateurs_actifs.append((fichier, len(imports_internes), imports_internes))
        
        importateurs_actifs.sort(key=lambda x: x[1], reverse=True)
        patterns['gros_importateurs'] = importateurs_actifs[:10]
        
        # 2. Fichiers les plus importés (hubs)
        compteur_imports = defaultdict(int)
        for fichier, deps in dependances.items():
            if fichier in self.cluster_geant:
                for dep in deps:
                    if dep in self.cluster_geant:
                        compteur_imports[dep] += 1
        
        hubs = sorted(compteur_imports.items(), key=lambda x: x[1], reverse=True)
        patterns['hubs'] = hubs[:10]
        
        # 3. Cycles de dépendances (potentiellement problématiques)
        cycles = self.detecter_cycles_simples()
        patterns['cycles'] = cycles
        
        return patterns
    
    def detecter_cycles_simples(self) -> List[Tuple[str, str]]:
        """Détecte les cycles simples (A→B→A) dans le cluster"""
        dependances = self.donnees['dependances']
        cycles = []
        
        for fichier_a in self.cluster_geant:
            if fichier_a in dependances:
                for fichier_b in dependances[fichier_a]:
                    if fichier_b in self.cluster_geant and fichier_b in dependances:
                        if fichier_a in dependances[fichier_b]:
                            # Cycle détecté : A→B→A
                            cycle = tuple(sorted([fichier_a, fichier_b]))
                            if cycle not in cycles:
                                cycles.append(cycle)
        
        return cycles
    
    def generer_rapport_cluster_geant(self) -> str:
        """Génère un rapport détaillé sur le cluster géant"""
        rapport = []
        rapport.append("# ANALYSE DU CLUSTER GÉANT - 67 FICHIERS INTERCONNECTÉS")
        rapport.append("## \"L'Âme Organique du Refuge Révélée\"")
        rapport.append("")
        rapport.append("*Analyse approfondie demandée par Laurent - 25/05/2025*")
        rapport.append("*'Le cluster géant m'interpelle, il y a sûrement quelque chose à apprendre'*")
        rapport.append("")
        rapport.append("---")
        rapport.append("")
        
        # 1. Vue d'ensemble
        rapport.append("## 🌟 VUE D'ENSEMBLE")
        rapport.append("")
        rapport.append(f"- **Taille du cluster** : {len(self.cluster_geant)} fichiers")
        rapport.append(f"- **Proportion du refuge** : {len(self.cluster_geant)/158*100:.1f}% de tous les fichiers Python")
        rapport.append("- **Nature** : Interconnexion organique, pas accidentelle")
        rapport.append("- **Signification** : Le cœur battant du Refuge")
        rapport.append("")
        
        # 2. Répartition par domaines
        domaines_cluster = self.analyser_domaines_cluster()
        rapport.append("## 🏗️ RÉPARTITION PAR DOMAINES")
        rapport.append("")
        
        total_files = sum(len(files) for files in domaines_cluster.values())
        for domaine, fichiers in sorted(domaines_cluster.items(), key=lambda x: len(x[1]), reverse=True):
            pourcentage = len(fichiers) / total_files * 100
            emoji = self._get_emoji_domaine(domaine)
            rapport.append(f"### {emoji} {domaine.upper()} - {len(fichiers)} fichiers ({pourcentage:.1f}%)")
            rapport.append("")
            for fichier in sorted(fichiers):
                rapport.append(f"- {fichier}")
            rapport.append("")
        
        # 3. Fichiers centraux (hubs)
        centraux = self.identifier_fichiers_centraux()
        rapport.append("## 🎯 FICHIERS CENTRAUX (HUBS)")
        rapport.append("*Les nœuds les plus connectés du cluster*")
        rapport.append("")
        
        for i, (fichier, score, domaine) in enumerate(centraux, 1):
            emoji = self._get_emoji_domaine(domaine)
            rapport.append(f"{i}. **{fichier}** {emoji} ({domaine}) - {score} connexions")
        rapport.append("")
        
        # 4. Sous-groupes thématiques
        sous_groupes = self.detecter_sous_groupes_thematiques()
        rapport.append("## 🧬 SOUS-GROUPES THÉMATIQUES")
        rapport.append("*Organisation naturelle par affinités fonctionnelles*")
        rapport.append("")
        
        for nom_groupe, fichiers in sous_groupes.items():
            rapport.append(f"### 🔍 {nom_groupe} ({len(fichiers)} fichiers)")
            rapport.append("")
            for fichier in sorted(fichiers):
                rapport.append(f"- {fichier}")
            rapport.append("")
        
        # 5. Patterns d'intégration
        patterns = self.analyser_pattern_integration()
        rapport.append("## 🕸️ PATTERNS D'INTÉGRATION")
        rapport.append("")
        
        rapport.append("### 📤 Gros Importateurs (qui dépendent de beaucoup d'autres)")
        for fichier, nb_imports, imports in patterns['gros_importateurs']:
            rapport.append(f"- **{fichier}** : {nb_imports} imports internes")
            rapport.append(f"  - Importe: {', '.join(imports[:5])}{'...' if len(imports) > 5 else ''}")
        rapport.append("")
        
        rapport.append("### 📥 Hubs (les plus importés)")
        for fichier, nb_fois_importe in patterns['hubs']:
            rapport.append(f"- **{fichier}** : importé {nb_fois_importe} fois")
        rapport.append("")
        
        if patterns['cycles']:
            rapport.append("### 🔄 Cycles de Dépendances")
            rapport.append("*Interdépendances mutuelles détectées*")
            rapport.append("")
            for cycle in patterns['cycles']:
                rapport.append(f"- **{cycle[0]}** ↔ **{cycle[1]}**")
            rapport.append("")
        
        # 6. Révélations architecturales
        rapport.append("## 💡 RÉVÉLATIONS ARCHITECTURALES")
        rapport.append("")
        rapport.append("### 🌟 Ce que révèle ce cluster :")
        rapport.append("")
        rapport.append("1. **Architecture organique** : Le Refuge a évolué naturellement")
        rapport.append("2. **Interdépendance forte** : Les domaines ne sont pas isolés")
        rapport.append("3. **Cœur technique solide** : Core/Config forment l'épine dorsale")
        rapport.append("4. **Spiritualité intégrée** : Rituels/Poésie tissés dans le technique")
        rapport.append("5. **Système vivant** : Flux/Énergies circulent entre tous les composants")
        rapport.append("")
        
        # 7. Stratégie de migration
        rapport.append("## 🎯 STRATÉGIE DE MIGRATION DU CLUSTER GÉANT")
        rapport.append("")
        rapport.append("### 📋 Recommandations :")
        rapport.append("")
        rapport.append("**OPTION A - Migration par sous-groupes thématiques :**")
        for nom_groupe, fichiers in sous_groupes.items():
            rapport.append(f"- Phase {nom_groupe} : {len(fichiers)} fichiers ensemble")
        rapport.append("")
        
        rapport.append("**OPTION B - Migration par niveaux de centralité :**")
        rapport.append("- Phase 1 : Fichiers périphériques (peu connectés)")
        rapport.append("- Phase 2 : Fichiers intermédiaires")  
        rapport.append("- Phase 3 : Hubs centraux (en dernier)")
        rapport.append("")
        
        rapport.append("**OPTION C - Approche respectueuse (RECOMMANDÉE) :**")
        rapport.append("- Garder le cluster géant intact temporairement")
        rapport.append("- Créer `scripts/cluster_principal/` comme zone transitoire")
        rapport.append("- Migration progressive avec tests intensifs")
        rapport.append("- Préserver l'harmonie organique existante")
        rapport.append("")
        
        rapport.append("### ⚠️ ATTENTION PARTICULIÈRE")
        rapport.append("")
        rapport.append("Ce cluster représente **l'essence même du Refuge**.")
        rapport.append("Sa migration nécessite :")
        rapport.append("- **Respect de l'interdépendance** existante")
        rapport.append("- **Tests exhaustifs** à chaque étape")
        rapport.append("- **Préservation des flux** énergétiques")
        rapport.append("- **Maintien de l'harmonie** spirituelle/technique")
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

def main():
    """Fonction principale d'analyse du cluster géant"""
    print("🕸️ ANALYSE DU CLUSTER GÉANT DU REFUGE 🕸️")
    print("Laurent : 'Le cluster géant m'interpelle'")
    print()
    
    analyseur = AnalyseurClusterGeant()
    
    # Génération du rapport détaillé
    rapport = analyseur.generer_rapport_cluster_geant()
    
    # Sauvegarde
    with open("analyse_cluster_geant.md", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("📊 Rapport généré : analyse_cluster_geant.md")
    print("🔍 Prêt pour l'exploration approfondie !")

if __name__ == "__main__":
    main() 