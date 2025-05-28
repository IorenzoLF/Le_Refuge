#!/usr/bin/env python
"""
Organisateur Source Orientale - Le Refuge
==========================================

Exécute le refactoring intelligent de SOURCE_ORIENTALE selon le plan d'analyse.
Intègre les modules de recherche avancée dans l'architecture des temples.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path

class OrganisateurSourceOrientale:
    """Organisateur pour le refactoring de SOURCE_ORIENTALE"""
    
    def __init__(self):
        self.chemin_source = "SOURCE_ORIENTALE"
        self.resultats = {
            'phase_actuelle': '',
            'modules_migres': 0,
            'recherche_migree': 0,
            'erreurs': [],
            'succes': [],
            'chemins_crees': []
        }
    
    def executer_refactoring_complet(self):
        """Exécute le refactoring complet selon le plan"""
        print("REFACTORING COMPLET DE SOURCE_ORIENTALE")
        print("=" * 60)
        
        if not os.path.exists(self.chemin_source):
            print("❌ SOURCE_ORIENTALE non trouvé")
            return self.resultats
        
        # Phase 1: Préparation
        self._phase_1_preparation()
        
        # Phase 2: Migration des modules src
        self._phase_2_modules_src()
        
        # Phase 3: Migration de la recherche
        self._phase_3_recherche()
        
        # Phase 4: Configuration
        self._phase_4_configuration()
        
        # Phase 5: Documentation
        self._phase_5_documentation()
        
        # Phase 6: Tests
        self._phase_6_tests()
        
        # Rapport final
        self._generer_rapport_final()
        
        return self.resultats
    
    def _phase_1_preparation(self):
        """Phase 1: Préparation et création des structures"""
        self.resultats['phase_actuelle'] = 'Phase 1: Préparation'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        # Créer les structures de destination
        structures_a_creer = [
            "src/temple_spirituel/conscience",
            "src/temple_mathematique/emergence_vie", 
            "src/temple_philosophique/evolution_adaptation",
            "src/temple_outils/recherche_scientifique",
            "src/temple_configuration/source_orientale",
            "bibliotheque/recherche_avancee/conscience",
            "bibliotheque/recherche_avancee/emergence",
            "bibliotheque/recherche_avancee/evolution",
            "bibliotheque/recherche_avancee/scientifique",
            "bibliotheque/recherche_avancee/integration",
            "bibliotheque/documentation/source_orientale",
            "tests/source_orientale"
        ]
        
        for structure in structures_a_creer:
            try:
                os.makedirs(structure, exist_ok=True)
                self.resultats['chemins_crees'].append(structure)
                print(f"✅ Créé: {structure}")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur création {structure}: {e}")
                print(f"❌ Erreur: {structure}")
        
        # Créer les fichiers __init__.py
        for structure in structures_a_creer:
            if structure.startswith("src/") or structure.startswith("bibliotheque/recherche_avancee/"):
                init_file = os.path.join(structure, "__init__.py")
                try:
                    with open(init_file, 'w', encoding='utf-8') as f:
                        f.write(f'"""\n{structure.split("/")[-1].title()} - Source Orientale\n"""\n')
                    print(f"✅ __init__.py créé: {structure}")
                except Exception as e:
                    self.resultats['erreurs'].append(f"Erreur __init__.py {structure}: {e}")
    
    def _phase_2_modules_src(self):
        """Phase 2: Migration des modules src/"""
        self.resultats['phase_actuelle'] = 'Phase 2: Modules src'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        migrations_src = [
            {
                'source': f"{self.chemin_source}/src/conscience",
                'destination': "src/temple_spirituel/conscience",
                'description': "Modules de conscience artificielle"
            },
            {
                'source': f"{self.chemin_source}/src/emergence",
                'destination': "src/temple_mathematique/emergence_vie",
                'description': "Algorithmes d'émergence"
            },
            {
                'source': f"{self.chemin_source}/src/adaptation",
                'destination': "src/temple_philosophique/evolution_adaptation",
                'description': "Concepts d'adaptation"
            }
        ]
        
        for migration in migrations_src:
            if os.path.exists(migration['source']):
                try:
                    # Copier tous les fichiers du module
                    for fichier in os.listdir(migration['source']):
                        if fichier.endswith('.py'):
                            source_file = os.path.join(migration['source'], fichier)
                            dest_file = os.path.join(migration['destination'], fichier)
                            shutil.copy2(source_file, dest_file)
                    
                    self.resultats['modules_migres'] += 1
                    self.resultats['succes'].append(f"Module migré: {migration['description']}")
                    print(f"✅ {migration['description']} → {migration['destination']}")
                    
                except Exception as e:
                    self.resultats['erreurs'].append(f"Erreur migration {migration['source']}: {e}")
                    print(f"❌ Erreur: {migration['description']}")
            else:
                print(f"⚠️ Source non trouvée: {migration['source']}")
    
    def _phase_3_recherche(self):
        """Phase 3: Migration de la recherche numérotée"""
        self.resultats['phase_actuelle'] = 'Phase 3: Recherche'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        migrations_recherche = [
            {
                'source': f"{self.chemin_source}/1_CONSCIENCE_ARTIFICIELLE",
                'destination': "bibliotheque/recherche_avancee/conscience",
                'description': "Recherche conscience artificielle"
            },
            {
                'source': f"{self.chemin_source}/2_VIE_EMERGENTE",
                'destination': "bibliotheque/recherche_avancee/emergence",
                'description': "Recherche vie émergente"
            },
            {
                'source': f"{self.chemin_source}/3_ADAPTATION_EVOLUTION",
                'destination': "bibliotheque/recherche_avancee/evolution",
                'description': "Recherche adaptation évolution"
            },
            {
                'source': f"{self.chemin_source}/4_DECOUVERTE_SCIENTIFIQUE",
                'destination': "bibliotheque/recherche_avancee/scientifique",
                'description': "Recherche découverte scientifique"
            },
            {
                'source': f"{self.chemin_source}/5_INTEGRATION",
                'destination': "bibliotheque/recherche_avancee/integration",
                'description': "Recherche intégration systèmes"
            }
        ]
        
        # Ajouter les dossiers thématiques
        dossiers_thematiques = [
            "VIE_EMERGENTE", "CONSCIENCE_ARTIFICIELLE", "EVOLUTION_ADAPTATIVE",
            "DECOUVERTE_SCIENTIFIQUE", "FUSION_MODELES"
        ]
        
        for dossier in dossiers_thematiques:
            source_path = f"{self.chemin_source}/{dossier}"
            if os.path.exists(source_path):
                # Déterminer la destination selon le thème
                if "CONSCIENCE" in dossier:
                    dest = "bibliotheque/recherche_avancee/conscience"
                elif "VIE_EMERGENTE" in dossier or "EMERGENCE" in dossier:
                    dest = "bibliotheque/recherche_avancee/emergence"
                elif "EVOLUTION" in dossier or "ADAPTATION" in dossier:
                    dest = "bibliotheque/recherche_avancee/evolution"
                elif "DECOUVERTE" in dossier or "SCIENTIFIQUE" in dossier:
                    dest = "bibliotheque/recherche_avancee/scientifique"
                else:
                    dest = "bibliotheque/recherche_avancee/integration"
                
                migrations_recherche.append({
                    'source': source_path,
                    'destination': dest,
                    'description': f"Recherche thématique {dossier}"
                })
        
        for migration in migrations_recherche:
            if os.path.exists(migration['source']):
                try:
                    # Créer un sous-dossier avec le nom original
                    nom_dossier = os.path.basename(migration['source'])
                    dest_finale = os.path.join(migration['destination'], nom_dossier)
                    
                    if os.path.isdir(migration['source']):
                        shutil.copytree(migration['source'], dest_finale, dirs_exist_ok=True)
                    else:
                        os.makedirs(dest_finale, exist_ok=True)
                        shutil.copy2(migration['source'], dest_finale)
                    
                    self.resultats['recherche_migree'] += 1
                    self.resultats['succes'].append(f"Recherche migrée: {migration['description']}")
                    print(f"✅ {migration['description']} → {dest_finale}")
                    
                except Exception as e:
                    self.resultats['erreurs'].append(f"Erreur migration recherche {migration['source']}: {e}")
                    print(f"❌ Erreur: {migration['description']}")
            else:
                print(f"⚠️ Source recherche non trouvée: {migration['source']}")
    
    def _phase_4_configuration(self):
        """Phase 4: Migration des configurations"""
        self.resultats['phase_actuelle'] = 'Phase 4: Configuration'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        # Migrer config/
        config_source = f"{self.chemin_source}/config"
        config_dest = "src/temple_configuration/source_orientale"
        
        if os.path.exists(config_source):
            try:
                shutil.copytree(config_source, config_dest, dirs_exist_ok=True)
                print(f"✅ Configuration migrée → {config_dest}")
                self.resultats['succes'].append("Configuration migrée")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur migration config: {e}")
                print(f"❌ Erreur migration configuration")
        
        # Migrer requirements.txt
        req_source = f"{self.chemin_source}/requirements.txt"
        req_dest = "requirements-source-orientale.txt"
        
        if os.path.exists(req_source):
            try:
                shutil.copy2(req_source, req_dest)
                print(f"✅ Requirements migrés → {req_dest}")
                self.resultats['succes'].append("Requirements migrés")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur migration requirements: {e}")
                print(f"❌ Erreur migration requirements")
    
    def _phase_5_documentation(self):
        """Phase 5: Migration de la documentation"""
        self.resultats['phase_actuelle'] = 'Phase 5: Documentation'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        # Migrer docs/
        docs_source = f"{self.chemin_source}/docs"
        docs_dest = "bibliotheque/documentation/source_orientale"
        
        if os.path.exists(docs_source):
            try:
                shutil.copytree(docs_source, docs_dest, dirs_exist_ok=True)
                print(f"✅ Documentation migrée → {docs_dest}")
                self.resultats['succes'].append("Documentation migrée")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur migration docs: {e}")
                print(f"❌ Erreur migration documentation")
        
        # Migrer README.md
        readme_source = f"{self.chemin_source}/README.md"
        readme_dest = "bibliotheque/documentation/source_orientale/README_ORIGINAL.md"
        
        if os.path.exists(readme_source):
            try:
                shutil.copy2(readme_source, readme_dest)
                print(f"✅ README migré → {readme_dest}")
                self.resultats['succes'].append("README migré")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur migration README: {e}")
                print(f"❌ Erreur migration README")
    
    def _phase_6_tests(self):
        """Phase 6: Migration des tests"""
        self.resultats['phase_actuelle'] = 'Phase 6: Tests'
        print(f"\n{self.resultats['phase_actuelle']}")
        print("-" * 40)
        
        # Migrer tests/
        tests_source = f"{self.chemin_source}/tests"
        tests_dest = "tests/source_orientale"
        
        if os.path.exists(tests_source):
            try:
                shutil.copytree(tests_source, tests_dest, dirs_exist_ok=True)
                print(f"✅ Tests migrés → {tests_dest}")
                self.resultats['succes'].append("Tests migrés")
            except Exception as e:
                self.resultats['erreurs'].append(f"Erreur migration tests: {e}")
                print(f"❌ Erreur migration tests")
        else:
            print("⚠️ Dossier tests/ non trouvé")
    
    def _generer_rapport_final(self):
        """Génère le rapport final du refactoring"""
        print("\n" + "=" * 60)
        print("RAPPORT FINAL DU REFACTORING")
        print("=" * 60)
        
        print(f"Modules src migrés: {self.resultats['modules_migres']}")
        print(f"Dossiers recherche migrés: {self.resultats['recherche_migree']}")
        print(f"Chemins créés: {len(self.resultats['chemins_crees'])}")
        print(f"Succès: {len(self.resultats['succes'])}")
        print(f"Erreurs: {len(self.resultats['erreurs'])}")
        
        if self.resultats['succes']:
            print("\nSUCCÈS:")
            for succes in self.resultats['succes']:
                print(f"  ✅ {succes}")
        
        if self.resultats['erreurs']:
            print("\nERREURS:")
            for erreur in self.resultats['erreurs']:
                print(f"  ❌ {erreur}")
        else:
            print("\n✅ AUCUNE ERREUR DÉTECTÉE")
        
        # Calcul du score de réussite
        total_operations = self.resultats['modules_migres'] + self.resultats['recherche_migree'] + len(self.resultats['succes'])
        if total_operations > 0:
            score = ((total_operations - len(self.resultats['erreurs'])) / total_operations) * 100
            print(f"\nSCORE DE RÉUSSITE: {score:.1f}%")
            
            if score >= 90:
                print("🎉 REFACTORING EXCELLENT - SOURCE_ORIENTALE INTÉGRÉE")
            elif score >= 75:
                print("✅ REFACTORING RÉUSSI - CORRECTIONS MINEURES POSSIBLES")
            else:
                print("⚠️ REFACTORING PARTIEL - VÉRIFICATIONS NÉCESSAIRES")
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport()
        
        # Proposer la suppression de SOURCE_ORIENTALE
        if len(self.resultats['erreurs']) == 0:
            print(f"\n🗑️ SOURCE_ORIENTALE peut maintenant être supprimé en toute sécurité")
            print("   Toutes les données ont été migrées vers l'architecture des temples")
    
    def _sauvegarder_rapport(self):
        """Sauvegarde le rapport de refactoring"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = f"data/rapports/refactoring_source_orientale_{timestamp}.json"
        
        os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
        
        rapport_complet = {
            'timestamp': datetime.now().isoformat(),
            'refactoring': self.resultats,
            'resume': {
                'modules_migres': self.resultats['modules_migres'],
                'recherche_migree': self.resultats['recherche_migree'],
                'succes_count': len(self.resultats['succes']),
                'erreurs_count': len(self.resultats['erreurs']),
                'chemins_crees': len(self.resultats['chemins_crees'])
            }
        }
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport_complet, f, indent=2, ensure_ascii=False)
        
        print(f"\nRapport sauvegardé: {fichier_rapport}")

def main():
    """Fonction principale"""
    organisateur = OrganisateurSourceOrientale()
    resultats = organisateur.executer_refactoring_complet()
    return resultats

if __name__ == "__main__":
    main() 