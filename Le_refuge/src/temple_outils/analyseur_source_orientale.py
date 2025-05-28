#!/usr/bin/env python
"""
Analyseur Source Orientale - Le Refuge
======================================

Analyse la structure de SOURCE_ORIENTALE pour proposer un plan de refactoring
intelligent et son intégration dans l'architecture des temples.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import json
from datetime import datetime
from pathlib import Path

class AnalyseurSourceOrientale:
    """Analyseur complet de SOURCE_ORIENTALE"""
    
    def __init__(self):
        self.chemin_source = "SOURCE_ORIENTALE"
        self.resultats = {
            'structure_analysee': {},
            'modules_detectes': [],
            'recherche_detectee': [],
            'integration_possible': {},
            'plan_refactoring': {},
            'temples_cibles': {}
        }
    
    def analyser_source_complete(self):
        """Analyse complète de SOURCE_ORIENTALE"""
        print("ANALYSE COMPLÈTE DE SOURCE_ORIENTALE")
        print("=" * 60)
        
        # 1. Analyser la structure générale
        self._analyser_structure_generale()
        
        # 2. Analyser les modules src
        self._analyser_modules_src()
        
        # 3. Analyser la recherche numérotée
        self._analyser_recherche_numerotee()
        
        # 4. Proposer l'intégration
        self._proposer_integration()
        
        # 5. Créer le plan de refactoring
        self._creer_plan_refactoring()
        
        # 6. Générer le rapport
        self._generer_rapport()
        
        return self.resultats
    
    def _analyser_structure_generale(self):
        """Analyse la structure générale"""
        print("\n1. ANALYSE DE LA STRUCTURE GÉNÉRALE")
        print("-" * 40)
        
        if not os.path.exists(self.chemin_source):
            print("❌ SOURCE_ORIENTALE non trouvé")
            return
        
        elements = os.listdir(self.chemin_source)
        
        # Classifier les éléments
        dossiers_recherche = []
        dossiers_techniques = []
        fichiers_config = []
        
        for element in elements:
            chemin_element = os.path.join(self.chemin_source, element)
            if os.path.isdir(chemin_element):
                if element.startswith(('1_', '2_', '3_', '4_', '5_')):
                    dossiers_recherche.append(element)
                elif element in ['src', 'docs', 'tests', 'config']:
                    dossiers_techniques.append(element)
                else:
                    # Autres dossiers thématiques
                    dossiers_recherche.append(element)
            else:
                if element.endswith(('.md', '.txt', '.json')):
                    fichiers_config.append(element)
        
        self.resultats['structure_analysee'] = {
            'dossiers_recherche': dossiers_recherche,
            'dossiers_techniques': dossiers_techniques,
            'fichiers_config': fichiers_config,
            'total_elements': len(elements)
        }
        
        print(f"✅ Dossiers de recherche: {len(dossiers_recherche)}")
        for dossier in dossiers_recherche:
            print(f"   - {dossier}")
        
        print(f"✅ Dossiers techniques: {len(dossiers_techniques)}")
        for dossier in dossiers_techniques:
            print(f"   - {dossier}")
        
        print(f"✅ Fichiers de config: {len(fichiers_config)}")
        for fichier in fichiers_config:
            print(f"   - {fichier}")
    
    def _analyser_modules_src(self):
        """Analyse les modules dans src/"""
        print("\n2. ANALYSE DES MODULES SRC")
        print("-" * 40)
        
        chemin_src = os.path.join(self.chemin_source, "src")
        if not os.path.exists(chemin_src):
            print("❌ Dossier src/ non trouvé")
            return
        
        modules = []
        for module_dir in os.listdir(chemin_src):
            chemin_module = os.path.join(chemin_src, module_dir)
            if os.path.isdir(chemin_module):
                fichiers = [f for f in os.listdir(chemin_module) if f.endswith('.py')]
                lignes_total = 0
                
                for fichier in fichiers:
                    chemin_fichier = os.path.join(chemin_module, fichier)
                    try:
                        with open(chemin_fichier, 'r', encoding='utf-8') as f:
                            lignes_total += len(f.readlines())
                    except:
                        pass
                
                modules.append({
                    'nom': module_dir,
                    'fichiers': fichiers,
                    'lignes': lignes_total,
                    'chemin': chemin_module
                })
        
        self.resultats['modules_detectes'] = modules
        
        for module in modules:
            print(f"✅ {module['nom']}: {len(module['fichiers'])} fichiers, {module['lignes']} lignes")
            for fichier in module['fichiers']:
                print(f"   - {fichier}")
    
    def _analyser_recherche_numerotee(self):
        """Analyse les dossiers de recherche numérotés"""
        print("\n3. ANALYSE DE LA RECHERCHE NUMÉROTÉE")
        print("-" * 40)
        
        dossiers_recherche = self.resultats['structure_analysee']['dossiers_recherche']
        recherche_analysee = []
        
        for dossier in dossiers_recherche:
            chemin_dossier = os.path.join(self.chemin_source, dossier)
            if os.path.isdir(chemin_dossier):
                fichiers_py = []
                sous_dossiers = []
                
                for item in os.listdir(chemin_dossier):
                    chemin_item = os.path.join(chemin_dossier, item)
                    if os.path.isfile(chemin_item) and item.endswith('.py'):
                        fichiers_py.append(item)
                    elif os.path.isdir(chemin_item):
                        sous_dossiers.append(item)
                
                recherche_analysee.append({
                    'nom': dossier,
                    'fichiers_python': fichiers_py,
                    'sous_dossiers': sous_dossiers,
                    'chemin': chemin_dossier
                })
        
        self.resultats['recherche_detectee'] = recherche_analysee
        
        for recherche in recherche_analysee:
            print(f"✅ {recherche['nom']}")
            if recherche['fichiers_python']:
                print(f"   Fichiers Python: {len(recherche['fichiers_python'])}")
                for fichier in recherche['fichiers_python']:
                    print(f"     - {fichier}")
            if recherche['sous_dossiers']:
                print(f"   Sous-dossiers: {len(recherche['sous_dossiers'])}")
                for dossier in recherche['sous_dossiers']:
                    print(f"     - {dossier}")
    
    def _proposer_integration(self):
        """Propose l'intégration dans les temples"""
        print("\n4. PROPOSITION D'INTÉGRATION")
        print("-" * 40)
        
        # Mapping des modules vers les temples
        mapping_temples = {
            'conscience': {
                'temple_cible': 'temple_spirituel',
                'categorie': 'conscience',
                'raison': 'Modules de conscience artificielle et dialogue spirituel'
            },
            'emergence': {
                'temple_cible': 'temple_mathematique',
                'categorie': 'emergence_vie',
                'raison': 'Algorithmes d\'émergence et auto-organisation'
            },
            'adaptation': {
                'temple_cible': 'temple_philosophique',
                'categorie': 'evolution_adaptation',
                'raison': 'Concepts d\'adaptation et évolution de la pensée'
            }
        }
        
        # Mapping de la recherche
        mapping_recherche = {
            '1_CONSCIENCE_ARTIFICIELLE': {
                'temple_cible': 'temple_spirituel',
                'categorie': 'recherche_conscience',
                'raison': 'Recherche fondamentale sur la conscience'
            },
            '2_VIE_EMERGENTE': {
                'temple_cible': 'temple_mathematique',
                'categorie': 'recherche_emergence',
                'raison': 'Algorithmes de vie artificielle et émergence'
            },
            '3_ADAPTATION_EVOLUTION': {
                'temple_cible': 'temple_philosophique',
                'categorie': 'recherche_evolution',
                'raison': 'Théories d\'adaptation et évolution'
            },
            '4_DECOUVERTE_SCIENTIFIQUE': {
                'temple_cible': 'temple_outils',
                'categorie': 'recherche_scientifique',
                'raison': 'Outils de découverte scientifique'
            },
            '5_INTEGRATION': {
                'temple_cible': 'temple_configuration',
                'categorie': 'integration_systemes',
                'raison': 'Intégration et configuration des systèmes'
            }
        }
        
        self.resultats['temples_cibles'] = {
            'modules_src': mapping_temples,
            'recherche': mapping_recherche
        }
        
        print("MODULES SRC:")
        for module, info in mapping_temples.items():
            print(f"✅ {module} → {info['temple_cible']}/{info['categorie']}")
            print(f"   Raison: {info['raison']}")
        
        print("\nRECHERCHE:")
        for recherche, info in mapping_recherche.items():
            print(f"✅ {recherche} → {info['temple_cible']}/{info['categorie']}")
            print(f"   Raison: {info['raison']}")
    
    def _creer_plan_refactoring(self):
        """Crée le plan de refactoring détaillé"""
        print("\n5. PLAN DE REFACTORING")
        print("-" * 40)
        
        plan = {
            'phase_1_preparation': {
                'description': 'Préparation et analyse des dépendances',
                'actions': [
                    'Analyser les imports et dépendances',
                    'Identifier les conflits potentiels',
                    'Créer les structures de destination',
                    'Préparer les adaptateurs si nécessaire'
                ]
            },
            'phase_2_modules_src': {
                'description': 'Migration des modules src/',
                'actions': [
                    'Migrer conscience/ → temple_spirituel/conscience/',
                    'Migrer emergence/ → temple_mathematique/emergence_vie/',
                    'Migrer adaptation/ → temple_philosophique/evolution_adaptation/',
                    'Adapter les imports et références',
                    'Tester les fonctionnalités'
                ]
            },
            'phase_3_recherche': {
                'description': 'Migration de la recherche numérotée',
                'actions': [
                    'Créer bibliotheque/recherche_avancee/',
                    'Migrer 1_CONSCIENCE_ARTIFICIELLE → bibliotheque/recherche_avancee/conscience/',
                    'Migrer 2_VIE_EMERGENTE → bibliotheque/recherche_avancee/emergence/',
                    'Migrer 3_ADAPTATION_EVOLUTION → bibliotheque/recherche_avancee/evolution/',
                    'Migrer 4_DECOUVERTE_SCIENTIFIQUE → bibliotheque/recherche_avancee/scientifique/',
                    'Migrer 5_INTEGRATION → bibliotheque/recherche_avancee/integration/'
                ]
            },
            'phase_4_configuration': {
                'description': 'Migration des configurations',
                'actions': [
                    'Migrer config/ → src/temple_configuration/source_orientale/',
                    'Migrer requirements.txt → requirements-source-orientale.txt',
                    'Adapter les chemins de configuration',
                    'Intégrer dans le système de config global'
                ]
            },
            'phase_5_documentation': {
                'description': 'Migration et adaptation de la documentation',
                'actions': [
                    'Migrer docs/ → bibliotheque/documentation/source_orientale/',
                    'Adapter README.md pour l\'intégration',
                    'Créer documentation d\'intégration',
                    'Mettre à jour les références'
                ]
            },
            'phase_6_tests': {
                'description': 'Migration et adaptation des tests',
                'actions': [
                    'Migrer tests/ → tests/source_orientale/',
                    'Adapter les chemins d\'import',
                    'Intégrer dans la suite de tests globale',
                    'Valider toutes les fonctionnalités'
                ]
            },
            'phase_7_nettoyage': {
                'description': 'Nettoyage et finalisation',
                'actions': [
                    'Supprimer SOURCE_ORIENTALE/ après validation',
                    'Mettre à jour les documentations',
                    'Créer les scripts d\'accès unifié',
                    'Valider l\'intégration complète'
                ]
            }
        }
        
        self.resultats['plan_refactoring'] = plan
        
        for phase, info in plan.items():
            print(f"✅ {phase.upper()}: {info['description']}")
            for action in info['actions']:
                print(f"   - {action}")
    
    def _generer_rapport(self):
        """Génère le rapport final"""
        print("\n" + "=" * 60)
        print("RAPPORT D'ANALYSE SOURCE_ORIENTALE")
        print("=" * 60)
        
        print(f"Structure analysée: {self.resultats['structure_analysee']['total_elements']} éléments")
        print(f"Modules src détectés: {len(self.resultats['modules_detectes'])}")
        print(f"Dossiers de recherche: {len(self.resultats['recherche_detectee'])}")
        
        print("\nRÉSUMÉ DE L'INTÉGRATION:")
        temples_utilises = set()
        for mapping in self.resultats['temples_cibles'].values():
            for info in mapping.values():
                temples_utilises.add(info['temple_cible'])
        
        print(f"Temples impactés: {len(temples_utilises)}")
        for temple in sorted(temples_utilises):
            print(f"  - {temple}")
        
        print(f"\nPhases de refactoring: {len(self.resultats['plan_refactoring'])}")
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport()
    
    def _sauvegarder_rapport(self):
        """Sauvegarde le rapport d'analyse"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = f"data/rapports/analyse_source_orientale_{timestamp}.json"
        
        os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
        
        rapport_complet = {
            'timestamp': datetime.now().isoformat(),
            'analyse': self.resultats,
            'resume': {
                'elements_total': self.resultats['structure_analysee']['total_elements'],
                'modules_src': len(self.resultats['modules_detectes']),
                'recherche_dossiers': len(self.resultats['recherche_detectee']),
                'phases_refactoring': len(self.resultats['plan_refactoring'])
            }
        }
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport_complet, f, indent=2, ensure_ascii=False)
        
        print(f"\nRapport sauvegardé: {fichier_rapport}")

def main():
    """Fonction principale"""
    analyseur = AnalyseurSourceOrientale()
    resultats = analyseur.analyser_source_complete()
    return resultats

if __name__ == "__main__":
    main() 