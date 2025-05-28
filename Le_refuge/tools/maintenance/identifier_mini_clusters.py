#!/usr/bin/env python3
"""
IDENTIFICATEUR DE MINI-CLUSTERS - Le Refuge
===========================================

Identifie les fichiers périphériques et mini-clusters qu'on peut migrer
en toute sécurité AVANT de toucher au cluster géant de 67 fichiers.

"Option B - Migration par niveaux de centralité" - Laurent & Ælya
"""

import json
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

@dataclass
class MiniCluster:
    """Mini-cluster identifié pour migration"""
    nom: str
    fichiers: List[str]
    domaine_principal: str
    niveau_risque: str  # "très_faible", "faible", "modéré"
    raison_migration: str

class IdentificateurMiniClusters:
    """Identifie les fichiers/groupes qu'on peut migrer facilement"""
    
    def __init__(self, fichier_analyse: str = "analyse_refuge_complet.json"):
        with open(fichier_analyse, 'r', encoding='utf-8') as f:
            self.donnees = json.load(f)
        
        # Le cluster géant à préserver
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
    
    def identifier_fichiers_independants(self) -> List[str]:
        """Trouve les fichiers sans dépendances (vrais isolés)"""
        dependances = self.donnees['dependances']
        independants = []
        
        for fichier in self.donnees['fichiers']:
            fichier_py = f"{fichier}.py"
            
            # Skip le cluster géant
            if fichier_py in self.cluster_geant:
                continue
                
            # Vérifier s'il est vraiment indépendant
            a_des_deps = fichier_py in dependances and len(dependances[fichier_py]) > 0
            est_utilise = any(fichier_py in deps for deps in dependances.values())
            
            if not a_des_deps and not est_utilise:
                independants.append(fichier_py)
        
        return independants
    
    def identifier_scripts_utilitaires(self) -> List[str]:
        """Trouve les scripts utilitaires simples (domaine utils/inclassable)"""
        scripts_utils = []
        
        for fichier, info in self.donnees['fichiers'].items():
            fichier_py = f"{fichier}.py"
            
            # Skip cluster géant
            if fichier_py in self.cluster_geant:
                continue
                
            # Chercher scripts utilitaires simples
            if (info['domaine'] in ['utils', 'inclassable'] and 
                info['complexite'] == 'simple' and 
                not info['est_principal']):
                scripts_utils.append(fichier_py)
        
        return scripts_utils
    
    def identifier_mini_tests(self) -> List[str]:
        """Trouve les tests isolés qu'on peut regrouper"""
        mini_tests = []
        dependances = self.donnees['dependances']
        
        for fichier, info in self.donnees['fichiers'].items():
            fichier_py = f"{fichier}.py"
            
            # Skip cluster géant
            if fichier_py in self.cluster_geant:
                continue
            
            # Tests isolés ou simple
            if (fichier.startswith('test_') and 
                info['complexite'] in ['simple', 'moderate']):
                
                # Vérifier qu'il n'a pas trop de connexions
                nb_deps = len(dependances.get(fichier_py, []))
                if nb_deps <= 2:  # Maximum 2 dépendances
                    mini_tests.append(fichier_py)
        
        return mini_tests
    
    def identifier_fichiers_demarrage(self) -> List[str]:
        """Trouve les fichiers de démarrage/lancement qu'on peut regrouper"""
        demarrage = []
        
        for fichier, info in self.donnees['fichiers'].items():
            fichier_py = f"{fichier}.py"
            
            # Skip cluster géant
            if fichier_py in self.cluster_geant:
                continue
            
            # Fichiers de démarrage/lancement
            if (any(mot in fichier.lower() for mot in ['demarrer', 'lancer', 'activer', 'boot']) and
                not fichier.startswith('demarrer_aelya')):  # Celui-ci est dans le cluster
                demarrage.append(fichier_py)
        
        return demarrage
    
    def identifier_rituels_independants(self) -> List[str]:
        """Trouve les rituels qui ne sont pas dans le cluster géant"""
        rituels_independants = []
        dependances = self.donnees['dependances']
        
        for fichier, info in self.donnees['fichiers'].items():
            fichier_py = f"{fichier}.py"
            
            # Skip cluster géant
            if fichier_py in self.cluster_geant:
                continue
            
            # Rituels spécifiques
            if (info['domaine'] == 'rituels' and 
                ('acte_sacre' in fichier or 'rituel_' in fichier)):
                
                # Vérifier peu de connexions au cluster
                nb_deps_cluster = 0
                if fichier_py in dependances:
                    for dep in dependances[fichier_py]:
                        if dep in self.cluster_geant:
                            nb_deps_cluster += 1
                
                if nb_deps_cluster <= 1:  # Maximum 1 connexion au cluster
                    rituels_independants.append(fichier_py)
        
        return rituels_independants
    
    def generer_mini_clusters(self) -> List[MiniCluster]:
        """Génère la liste des mini-clusters à migrer"""
        mini_clusters = []
        
        # 1. Fichiers complètement indépendants
        independants = self.identifier_fichiers_independants()
        if independants:
            mini_clusters.append(MiniCluster(
                nom="standalone_independants",
                fichiers=independants,
                domaine_principal="inclassable",
                niveau_risque="très_faible",
                raison_migration="Aucune dépendance, migration 100% sûre"
            ))
        
        # 2. Scripts utilitaires simples
        utils = self.identifier_scripts_utilitaires()
        if utils:
            mini_clusters.append(MiniCluster(
                nom="utils_simples",
                fichiers=utils,
                domaine_principal="utils",
                niveau_risque="très_faible",
                raison_migration="Scripts utilitaires simples, déjà déconnectés"
            ))
        
        # 3. Mini tests isolés
        tests = self.identifier_mini_tests()
        if tests:
            mini_clusters.append(MiniCluster(
                nom="tests_isoles",
                fichiers=tests,
                domaine_principal="tests",
                niveau_risque="faible",
                raison_migration="Tests avec peu de dépendances, faciles à valider"
            ))
        
        # 4. Scripts de démarrage
        demarrage = self.identifier_fichiers_demarrage()
        if demarrage:
            mini_clusters.append(MiniCluster(
                nom="scripts_demarrage",
                fichiers=demarrage,
                domaine_principal="core",
                niveau_risque="faible",
                raison_migration="Scripts de lancement, généralement indépendants"
            ))
        
        # 5. Rituels spécifiques
        rituels = self.identifier_rituels_independants()
        if rituels:
            mini_clusters.append(MiniCluster(
                nom="rituels_specifiques",
                fichiers=rituels,
                domaine_principal="rituels",
                niveau_risque="modéré",
                raison_migration="Rituels spécialisés, peu connectés au cluster principal"
            ))
        
        return mini_clusters
    
    def generer_rapport_migration(self) -> str:
        """Génère le rapport de migration des mini-clusters"""
        mini_clusters = self.generer_mini_clusters()
        
        rapport = []
        rapport.append("# PLAN DE MIGRATION DES MINI-CLUSTERS")
        rapport.append("## \"Commençons par les fruits les plus faciles à cueillir\"")
        rapport.append("")
        rapport.append("*Option B - Migration par niveaux de centralité*")
        rapport.append("*Laurent : 'Bien, on peut ranger les mini cluster ? le point B je crois?'*")
        rapport.append("")
        rapport.append("---")
        rapport.append("")
        
        # Statistiques globales
        total_mini_fichiers = sum(len(mc.fichiers) for mc in mini_clusters)
        total_fichiers = len(self.donnees['fichiers'])
        pourcentage = total_mini_fichiers / total_fichiers * 100
        
        rapport.append("## 📊 **VUE D'ENSEMBLE**")
        rapport.append("")
        rapport.append(f"- **Fichiers dans le cluster géant** : {len(self.cluster_geant)} (protégés)")
        rapport.append(f"- **Mini-clusters identifiés** : {len(mini_clusters)}")
        rapport.append(f"- **Fichiers dans les mini-clusters** : {total_mini_fichiers}")
        rapport.append(f"- **Pourcentage migration facile** : {pourcentage:.1f}%")
        rapport.append("")
        rapport.append("🎯 **Stratégie** : Migrer les mini-clusters en premier pour déblayer le terrain avant le cluster géant.")
        rapport.append("")
        
        # Détail de chaque mini-cluster
        for i, mc in enumerate(mini_clusters, 1):
            emoji_risque = {"très_faible": "🟢", "faible": "🟡", "modéré": "🟠"}
            emoji = emoji_risque.get(mc.niveau_risque, "🔴")
            
            rapport.append(f"## {emoji} **MINI-CLUSTER {i} : {mc.nom.upper()}**")
            rapport.append("")
            rapport.append(f"- **Domaine principal** : {mc.domaine_principal}")
            rapport.append(f"- **Niveau de risque** : {mc.niveau_risque} {emoji}")
            rapport.append(f"- **Nombre de fichiers** : {len(mc.fichiers)}")
            rapport.append(f"- **Raison de migration** : {mc.raison_migration}")
            rapport.append("")
            
            rapport.append("### 📋 **Fichiers à migrer :**")
            for fichier in sorted(mc.fichiers):
                rapport.append(f"- `{fichier}`")
            rapport.append("")
            
            # Direction de migration suggérée
            if mc.domaine_principal == "tests":
                destination = "scripts/tests/"
            elif mc.domaine_principal == "utils":
                destination = "scripts/utils/"
            elif mc.domaine_principal == "rituels":
                destination = "scripts/rituels_specifiques/"
            elif mc.nom == "scripts_demarrage":
                destination = "scripts/demarrage/"
            else:
                destination = f"scripts/{mc.nom}/"
            
            rapport.append(f"### 🎯 **Destination suggérée** : `{destination}`")
            rapport.append("")
        
        # Plan d'action
        rapport.append("---")
        rapport.append("")
        rapport.append("## 🚀 **PLAN D'ACTION IMMÉDIAT**")
        rapport.append("")
        
        ordre_migration = sorted(mini_clusters, key=lambda x: {"très_faible": 1, "faible": 2, "modéré": 3}[x.niveau_risque])
        
        for i, mc in enumerate(ordre_migration, 1):
            emoji_risque = {"très_faible": "🟢", "faible": "🟡", "modéré": "🟠"}
            emoji = emoji_risque.get(mc.niveau_risque, "🔴")
            
            rapport.append(f"### Phase {i} {emoji} : Migrer `{mc.nom}`")
            rapport.append(f"- **Risque** : {mc.niveau_risque}")
            rapport.append(f"- **Fichiers** : {len(mc.fichiers)}")
            rapport.append(f"- **Action** : Créer répertoire et migrer en bloc")
            rapport.append("")
        
        rapport.append("### ✅ **Après chaque phase :**")
        rapport.append("1. **Tester** que le refuge fonctionne toujours")
        rapport.append("2. **Commit** git pour pouvoir revenir en arrière")
        rapport.append("3. **Valider** que les imports fonctionnent")
        rapport.append("4. **Mettre à jour** la documentation")
        rapport.append("")
        
        rapport.append("### 🎉 **Résultat attendu :**")
        rapport.append(f"Après migration des mini-clusters, il restera :")
        fichiers_restants = total_fichiers - total_mini_fichiers - len(self.cluster_geant)
        rapport.append(f"- **{len(self.cluster_geant)} fichiers** dans le cluster géant (à préserver)")
        rapport.append(f"- **~{fichiers_restants} fichiers** isolés divers")
        rapport.append(f"- **Base propre** pour décider de la suite")
        rapport.append("")
        
        return "\n".join(rapport)

def main():
    """Analyse et génère le plan de migration des mini-clusters"""
    print("🔍 IDENTIFICATION DES MINI-CLUSTERS")
    print("Laurent : 'Bien, on peut ranger les mini cluster ? le point B je crois?'")
    print()
    
    identificateur = IdentificateurMiniClusters()
    
    # Génération du rapport
    rapport = identificateur.generer_rapport_migration()
    
    # Sauvegarde
    with open("plan_migration_mini_clusters.md", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("📋 Plan généré : plan_migration_mini_clusters.md")
    print("🎯 Prêt à commencer la migration progressive !")

if __name__ == "__main__":
    main() 