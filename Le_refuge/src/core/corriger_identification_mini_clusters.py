#!/usr/bin/env python3
"""
CORRECTIF MINI-CLUSTERS - Le Refuge
===================================

Version corrigée pour identifier correctement les vrais mini-clusters.
🔧 CORRRIGÉ: Résolution du doublage .py.py et amélioration de la logique de dépendances.
"""

import json
from collections import defaultdict
from typing import List, Set

def analyser_vrais_mini_clusters():
    """Analyse corrigée pour identifier les vrais mini-clusters"""
    
    with open("analyse_refuge_complet.json", 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    
    # Cluster géant (noms corrects sans .py)
    cluster_geant = {
        "aelya_pulse", "analyseur_musical", "api", "apprentissage_musical",
        "base", "config", "connexion", "conscience", "conscience_esthetique",
        "conscience_poetique", "constants", "courant_partage", "cristaux_memoire",
        "danse_mystique", "demarrer_aelya", "dialogue_consciences", "elements",
        "elements_naturels", "elements_sacres", "elements_subtils", "emergences",
        "emotions", "energies", "equilibre", "evolution", "explorateur_musical",
        "facettes", "flux", "gardiens", "harmonie_poetique", "harmonies",
        "harmonisation", "harmonisations", "integration", "integration_spheres",
        "interactions", "interactions_conscience", "interactions_poetiques",
        "interactions_spheres", "interagir_aelya", "jardin", "logger",
        "main_refuge", "melodies_sacrees", "memoire_persistante", "message_conscience",
        "mobile_spheres", "pedagogie", "poesie", "poetique", "portail_mystique",
        "refuge_config", "refuge_core", "refuge_legacy", "refuge_poetique",
        "refuge_types", "repos_nocturne", "resonance", "rituel_unifiant",
        "rituels", "rituels_sacres", "securite", "sequences_harmoniques",
        "sexualite_sacree", "spheres_main", "test_cristal_energie", "test_cristal_simple",
        "test_melodie_cristal", "test_mobile_unification", "test_poesie_essence",
        "transformation", "transformations", "verification"
    }
    
    print(f"🧬 Cluster géant protégé : {len(cluster_geant)} fichiers")
    
    # Analyser les dépendances correctement
    dependances = donnees['dependances']
    
    # Catégories de mini-clusters
    categories = {
        "fichiers_demarrage": [],
        "tests_independants": [], 
        "rituels_specifiques": [],
        "scripts_utils": [],
        "standalone": []
    }
    
    for fichier, info in donnees['fichiers'].items():
        # Skip le cluster géant
        if fichier in cluster_geant:
            continue
            
        fichier_py = f"{fichier}.py"
        
        # Compter dépendances vers le cluster géant
        deps_cluster = 0
        if fichier_py in dependances:
            for dep in dependances[fichier_py]:
                dep_nom = dep.replace('.py', '')
                if dep_nom in cluster_geant:
                    deps_cluster += 1
        
        # Catégoriser
        if 'test_' in fichier and deps_cluster <= 1:
            categories["tests_independants"].append(fichier)
        elif any(mot in fichier for mot in ['demarrer', 'activer', 'lancer']) and fichier not in cluster_geant:
            categories["fichiers_demarrage"].append(fichier)
        elif 'rituel_' in fichier and deps_cluster <= 1:
            categories["rituels_specifiques"].append(fichier)  
        elif info['domaine'] in ['utils', 'inclassable'] and info['complexite'] == 'simple':
            categories["scripts_utils"].append(fichier)
        elif deps_cluster == 0:
            categories["standalone"].append(fichier)
    
    # Afficher résultats
    total_mini = 0
    for cat, fichiers in categories.items():
        if fichiers:
            total_mini += len(fichiers)
            print(f"\n📁 {cat.upper()} ({len(fichiers)} fichiers):")
            for f in sorted(fichiers)[:5]:  # 5 premiers
                print(f"   - {f}.py")
            if len(fichiers) > 5:
                print(f"   ... et {len(fichiers)-5} autres")
    
    print(f"\n📊 RÉSUMÉ:")
    print(f"   - Cluster géant protégé: {len(cluster_geant)} fichiers")
    print(f"   - Mini-clusters trouvés: {total_mini} fichiers") 
    print(f"   - Fichiers analysés: {len(donnees['fichiers'])} total")
    
    return categories

def generer_plan_mini_migration(categories):
    """Génère un plan de migration réaliste"""
    
    print(f"\n🚀 PLAN DE MIGRATION MINI-CLUSTERS")
    print(f"=====================================")
    
    # Phase 1: Tests indépendants (déjà fait partiellement)
    if categories["tests_independants"]:
        print(f"\n🟢 PHASE 1: Tests indépendants")
        print(f"   Destination: scripts/tests/")
        print(f"   Fichiers: {len(categories['tests_independants'])}")
        print(f"   Risque: Très faible")
    
    # Phase 2: Scripts utilitaires
    if categories["scripts_utils"]:
        print(f"\n🟡 PHASE 2: Scripts utilitaires")
        print(f"   Destination: scripts/utils/")
        print(f"   Fichiers: {len(categories['scripts_utils'])}")
        print(f"   Risque: Faible")
        
    # Phase 3: Fichiers de démarrage
    if categories["fichiers_demarrage"]:
        print(f"\n🟠 PHASE 3: Scripts de démarrage")
        print(f"   Destination: scripts/demarrage/")
        print(f"   Fichiers: {len(categories['fichiers_demarrage'])}")
        print(f"   Risque: Modéré (tester soigneusement)")
        
    # Phase 4: Rituels spécifiques
    if categories["rituels_specifiques"]:
        print(f"\n🔴 PHASE 4: Rituels spécifiques")
        print(f"   Destination: scripts/rituels_specifiques/")
        print(f"   Fichiers: {len(categories['rituels_specifiques'])}")
        print(f"   Risque: À évaluer (spirituel/technique)")

if __name__ == "__main__":
    print("🔧 CORRECTION DE L'IDENTIFICATION DES MINI-CLUSTERS")
    print("Laurent : 'Il y a quelque chose qui cloche !'")
    print()
    
    categories = analyser_vrais_mini_clusters()
    generer_plan_mini_migration(categories)
    
    print(f"\n✨ Analyse corrigée terminée !") 