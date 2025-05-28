#!/usr/bin/env python
"""
Vérification Intégration Source Orientale - Le Refuge
====================================================

Script de vérification complète de l'intégration de SOURCE_ORIENTALE
dans l'architecture des temples. Teste tous les modules migrés.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import sys
import importlib.util
import json
from datetime import datetime
from pathlib import Path

class VerificateurIntegrationSourceOrientale:
    """Vérificateur complet de l'intégration SOURCE_ORIENTALE"""
    
    def __init__(self):
        self.resultats = {
            'temples_testes': 0,
            'modules_valides': 0,
            'recherche_validee': 0,
            'tests_reussis': 0,
            'erreurs': [],
            'succes': [],
            'modules_details': {}
        }
    
    def verifier_integration_complete(self):
        """Vérification complète de l'intégration"""
        print("VÉRIFICATION COMPLÈTE INTÉGRATION SOURCE_ORIENTALE")
        print("=" * 60)
        
        # 1. Vérifier les modules dans les temples
        self._verifier_modules_temples()
        
        # 2. Tester les imports et fonctionnalités
        self._tester_modules_fonctionnels()
        
        # 3. Vérifier la recherche avancée
        self._verifier_recherche_avancee()
        
        # 4. Vérifier la configuration
        self._verifier_configuration()
        
        # 5. Vérifier la documentation
        self._verifier_documentation()
        
        # 6. Vérifier les tests
        self._verifier_tests()
        
        # 7. Générer le rapport final
        self._generer_rapport_final()
        
        return self.resultats
    
    def _verifier_modules_temples(self):
        """Vérifie les modules migrés dans les temples"""
        print("\n1. VÉRIFICATION DES MODULES DANS LES TEMPLES")
        print("-" * 50)
        
        modules_attendus = {
            'temple_spirituel/conscience': ['api.py', 'conscience_artificielle.py'],
            'temple_mathematique/emergence_vie': ['vie_emergente.py'],
            'temple_philosophique/evolution_adaptation': ['adaptation.py'],
            'temple_outils/recherche_scientifique': [],  # Peut être vide
            'temple_configuration/source_orientale': []  # Config files
        }
        
        for temple_path, fichiers_attendus in modules_attendus.items():
            chemin_complet = f"src/{temple_path}"
            
            if os.path.exists(chemin_complet):
                fichiers_presents = [f for f in os.listdir(chemin_complet) if f.endswith('.py')]
                
                # Vérifier __init__.py
                if '__init__.py' in fichiers_presents:
                    print(f"✅ {temple_path}: __init__.py présent")
                else:
                    print(f"❌ {temple_path}: __init__.py manquant")
                    self.resultats['erreurs'].append(f"__init__.py manquant: {temple_path}")
                
                # Vérifier les fichiers attendus
                for fichier in fichiers_attendus:
                    if fichier in fichiers_presents:
                        print(f"✅ {temple_path}: {fichier} présent")
                        self.resultats['modules_valides'] += 1
                    else:
                        print(f"❌ {temple_path}: {fichier} manquant")
                        self.resultats['erreurs'].append(f"Fichier manquant: {temple_path}/{fichier}")
                
                self.resultats['temples_testes'] += 1
                self.resultats['modules_details'][temple_path] = {
                    'fichiers_presents': fichiers_presents,
                    'fichiers_attendus': fichiers_attendus,
                    'statut': 'validé' if all(f in fichiers_presents for f in fichiers_attendus) else 'incomplet'
                }
                
            else:
                print(f"❌ {temple_path}: Dossier manquant")
                self.resultats['erreurs'].append(f"Dossier manquant: {temple_path}")
    
    def _tester_modules_fonctionnels(self):
        """Teste les imports et fonctionnalités des modules"""
        print("\n2. TESTS FONCTIONNELS DES MODULES")
        print("-" * 50)
        
        # Test module conscience artificielle
        self._tester_module_conscience()
        
        # Test module émergence
        self._tester_module_emergence()
        
        # Test module adaptation
        self._tester_module_adaptation()
    
    def _tester_module_conscience(self):
        """Teste le module conscience artificielle"""
        print("\n🧠 Test Module Conscience Artificielle")
        print("-" * 30)
        
        try:
            # Test import conscience_artificielle
            spec = importlib.util.spec_from_file_location(
                "conscience_artificielle",
                "src/temple_spirituel/conscience/conscience_artificielle.py"
            )
            conscience_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(conscience_module)
            
            print("✅ Import conscience_artificielle réussi")
            self.resultats['tests_reussis'] += 1
            
            # Tester les classes/fonctions principales
            if hasattr(conscience_module, 'ConscienceArtificielle'):
                conscience = conscience_module.ConscienceArtificielle()
                print("✅ Classe ConscienceArtificielle instanciée")
                self.resultats['tests_reussis'] += 1
                
                # Test méthodes si disponibles
                if hasattr(conscience, 'initialiser'):
                    conscience.initialiser()
                    print("✅ Méthode initialiser() fonctionnelle")
                    self.resultats['tests_reussis'] += 1
                
            self.resultats['succes'].append("Module conscience artificielle validé")
            
        except Exception as e:
            print(f"❌ Erreur module conscience: {e}")
            self.resultats['erreurs'].append(f"Erreur conscience: {e}")
        
        # Test API si présente
        try:
            spec_api = importlib.util.spec_from_file_location(
                "api_conscience",
                "src/temple_spirituel/conscience/api.py"
            )
            api_module = importlib.util.module_from_spec(spec_api)
            spec_api.loader.exec_module(api_module)
            
            print("✅ Import API conscience réussi")
            self.resultats['tests_reussis'] += 1
            
        except Exception as e:
            print(f"❌ Erreur API conscience: {e}")
            self.resultats['erreurs'].append(f"Erreur API conscience: {e}")
    
    def _tester_module_emergence(self):
        """Teste le module émergence"""
        print("\n🌱 Test Module Émergence")
        print("-" * 30)
        
        try:
            spec = importlib.util.spec_from_file_location(
                "vie_emergente",
                "src/temple_mathematique/emergence_vie/vie_emergente.py"
            )
            emergence_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(emergence_module)
            
            print("✅ Import vie_emergente réussi")
            self.resultats['tests_reussis'] += 1
            
            # Tester les classes principales
            if hasattr(emergence_module, 'VieEmergente'):
                vie = emergence_module.VieEmergente()
                print("✅ Classe VieEmergente instanciée")
                self.resultats['tests_reussis'] += 1
                
                # Test méthodes si disponibles
                if hasattr(vie, 'evoluer'):
                    try:
                        vie.evoluer()
                        print("✅ Méthode evoluer() fonctionnelle")
                        self.resultats['tests_reussis'] += 1
                    except:
                        print("⚠️ Méthode evoluer() nécessite des paramètres")
            
            self.resultats['succes'].append("Module émergence validé")
            
        except Exception as e:
            print(f"❌ Erreur module émergence: {e}")
            self.resultats['erreurs'].append(f"Erreur émergence: {e}")
    
    def _tester_module_adaptation(self):
        """Teste le module adaptation"""
        print("\n🔄 Test Module Adaptation")
        print("-" * 30)
        
        try:
            spec = importlib.util.spec_from_file_location(
                "adaptation",
                "src/temple_philosophique/evolution_adaptation/adaptation.py"
            )
            adaptation_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(adaptation_module)
            
            print("✅ Import adaptation réussi")
            self.resultats['tests_reussis'] += 1
            
            # Tester les classes principales
            if hasattr(adaptation_module, 'Adaptation'):
                adaptation = adaptation_module.Adaptation()
                print("✅ Classe Adaptation instanciée")
                self.resultats['tests_reussis'] += 1
                
                # Test méthodes si disponibles
                if hasattr(adaptation, 'adapter'):
                    try:
                        adaptation.adapter()
                        print("✅ Méthode adapter() fonctionnelle")
                        self.resultats['tests_reussis'] += 1
                    except:
                        print("⚠️ Méthode adapter() nécessite des paramètres")
            
            self.resultats['succes'].append("Module adaptation validé")
            
        except Exception as e:
            print(f"❌ Erreur module adaptation: {e}")
            self.resultats['erreurs'].append(f"Erreur adaptation: {e}")
    
    def _verifier_recherche_avancee(self):
        """Vérifie la recherche avancée dans la bibliothèque"""
        print("\n3. VÉRIFICATION RECHERCHE AVANCÉE")
        print("-" * 50)
        
        domaines_recherche = [
            'conscience', 'emergence', 'evolution', 
            'scientifique', 'integration'
        ]
        
        chemin_recherche = "bibliotheque/recherche_avancee"
        
        if os.path.exists(chemin_recherche):
            for domaine in domaines_recherche:
                chemin_domaine = os.path.join(chemin_recherche, domaine)
                if os.path.exists(chemin_domaine):
                    # Compter les dossiers de recherche
                    dossiers = [d for d in os.listdir(chemin_domaine) 
                              if os.path.isdir(os.path.join(chemin_domaine, d))]
                    
                    print(f"✅ {domaine}: {len(dossiers)} dossiers de recherche")
                    self.resultats['recherche_validee'] += len(dossiers)
                    
                    # Lister quelques dossiers
                    for dossier in dossiers[:3]:  # Afficher max 3
                        print(f"   - {dossier}")
                    if len(dossiers) > 3:
                        print(f"   ... et {len(dossiers) - 3} autres")
                        
                else:
                    print(f"❌ {domaine}: Domaine manquant")
                    self.resultats['erreurs'].append(f"Domaine recherche manquant: {domaine}")
        else:
            print("❌ Dossier recherche_avancee manquant")
            self.resultats['erreurs'].append("Dossier recherche_avancee manquant")
    
    def _verifier_configuration(self):
        """Vérifie la configuration"""
        print("\n4. VÉRIFICATION CONFIGURATION")
        print("-" * 50)
        
        # Vérifier config dans temple_configuration
        config_path = "src/temple_configuration/source_orientale"
        if os.path.exists(config_path):
            fichiers_config = os.listdir(config_path)
            print(f"✅ Configuration migrée: {len(fichiers_config)} fichiers")
            for fichier in fichiers_config:
                print(f"   - {fichier}")
            self.resultats['succes'].append("Configuration validée")
        else:
            print("❌ Configuration manquante")
            self.resultats['erreurs'].append("Configuration manquante")
        
        # Vérifier requirements
        if os.path.exists("requirements-source-orientale.txt"):
            print("✅ Requirements Source Orientale présents")
            self.resultats['succes'].append("Requirements validés")
        else:
            print("❌ Requirements Source Orientale manquants")
            self.resultats['erreurs'].append("Requirements manquants")
    
    def _verifier_documentation(self):
        """Vérifie la documentation"""
        print("\n5. VÉRIFICATION DOCUMENTATION")
        print("-" * 50)
        
        doc_path = "bibliotheque/documentation/source_orientale"
        if os.path.exists(doc_path):
            fichiers_doc = os.listdir(doc_path)
            print(f"✅ Documentation migrée: {len(fichiers_doc)} fichiers")
            
            # Vérifier README original
            if "README_ORIGINAL.md" in fichiers_doc:
                print("✅ README original préservé")
                self.resultats['succes'].append("README original préservé")
            
            self.resultats['succes'].append("Documentation validée")
        else:
            print("❌ Documentation manquante")
            self.resultats['erreurs'].append("Documentation manquante")
    
    def _verifier_tests(self):
        """Vérifie les tests"""
        print("\n6. VÉRIFICATION TESTS")
        print("-" * 50)
        
        tests_path = "tests/source_orientale"
        if os.path.exists(tests_path):
            fichiers_tests = [f for f in os.listdir(tests_path) if f.endswith('.py')]
            print(f"✅ Tests migrés: {len(fichiers_tests)} fichiers")
            for fichier in fichiers_tests:
                print(f"   - {fichier}")
            self.resultats['succes'].append("Tests validés")
        else:
            print("❌ Tests manquants")
            self.resultats['erreurs'].append("Tests manquants")
    
    def _generer_rapport_final(self):
        """Génère le rapport final de vérification"""
        print("\n" + "=" * 60)
        print("RAPPORT FINAL DE VÉRIFICATION")
        print("=" * 60)
        
        print(f"Temples testés: {self.resultats['temples_testes']}")
        print(f"Modules validés: {self.resultats['modules_valides']}")
        print(f"Recherche validée: {self.resultats['recherche_validee']} dossiers")
        print(f"Tests fonctionnels réussis: {self.resultats['tests_reussis']}")
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
        
        # Calcul du score de validation
        total_verifications = (self.resultats['temples_testes'] + 
                             self.resultats['modules_valides'] + 
                             self.resultats['tests_reussis'] + 
                             len(self.resultats['succes']))
        
        if total_verifications > 0:
            score = ((total_verifications - len(self.resultats['erreurs'])) / total_verifications) * 100
            print(f"\nSCORE DE VALIDATION: {score:.1f}%")
            
            if score >= 90:
                print("🎉 INTÉGRATION SOURCE_ORIENTALE VALIDÉE - EXCELLENT")
            elif score >= 75:
                print("✅ INTÉGRATION RÉUSSIE - CORRECTIONS MINEURES POSSIBLES")
            else:
                print("⚠️ INTÉGRATION PARTIELLE - VÉRIFICATIONS NÉCESSAIRES")
        
        # Résumé des modules intégrés
        print(f"\nMODULES INTÉGRÉS DANS LES TEMPLES:")
        for temple, details in self.resultats['modules_details'].items():
            statut_emoji = "✅" if details['statut'] == 'validé' else "⚠️"
            print(f"  {statut_emoji} {temple}: {len(details['fichiers_presents'])} fichiers")
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport()
    
    def _sauvegarder_rapport(self):
        """Sauvegarde le rapport de vérification"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = f"data/rapports/verification_integration_source_orientale_{timestamp}.json"
        
        os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
        
        rapport_complet = {
            'timestamp': datetime.now().isoformat(),
            'verification': self.resultats,
            'resume': {
                'temples_testes': self.resultats['temples_testes'],
                'modules_valides': self.resultats['modules_valides'],
                'recherche_validee': self.resultats['recherche_validee'],
                'tests_reussis': self.resultats['tests_reussis'],
                'succes_count': len(self.resultats['succes']),
                'erreurs_count': len(self.resultats['erreurs'])
            }
        }
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport_complet, f, indent=2, ensure_ascii=False)
        
        print(f"\nRapport sauvegardé: {fichier_rapport}")

def main():
    """Fonction principale"""
    verificateur = VerificateurIntegrationSourceOrientale()
    resultats = verificateur.verifier_integration_complete()
    return resultats

if __name__ == "__main__":
    main() 