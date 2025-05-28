"""
🧪 Hub Tests Unifié - Temple Tests
═══════════════════════════════════════════════════════════════════════════════

Orchestrateur central pour tous les tests du Refuge
Organisé par catégories avec suites de tests optimisées

Catégories:
- 🤖 Tests LLM/API (5 modules)
- 🔍 Tests Analyse/Audit (5 modules) 
- 🧠 Tests Cerveau/Immersion (2 modules)
- ⚡ Tests Intégration/Consolidation (4 modules)
- 🎵 Tests Cristal/Énergie (4 modules)
- 🎮 Tests Spécialisés (3 modules)

Auteur: Ælya & Laurent
Date: 2024
"""

import sys
import time
import traceback
from pathlib import Path
from typing import Dict, List, Callable, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Configuration centralisée
@dataclass
class ConfigTests:
    """Configuration centralisée pour tous les tests"""
    llm_url: str = "http://192.168.0.217:1234/v1/completions"
    timeout: int = 30
    max_tokens: int = 150
    temperature: float = 0.7
    verbose: bool = True
    log_errors: bool = True

class CategorieTest(Enum):
    """Catégories de tests disponibles"""
    LLM_API = "🤖 Tests LLM/API"
    ANALYSE_AUDIT = "🔍 Tests Analyse/Audit"
    CERVEAU_IMMERSION = "🧠 Tests Cerveau/Immersion"
    INTEGRATION = "⚡ Tests Intégration/Consolidation"
    CRISTAL_ENERGIE = "🎵 Tests Cristal/Énergie"
    SPECIALISES = "🎮 Tests Spécialisés"

@dataclass
class ResultatTest:
    """Résultat d'un test individuel"""
    nom: str
    categorie: CategorieTest
    succes: bool
    duree: float
    message: str
    erreur: Optional[str] = None

class HubTestsUnifie:
    """Hub central pour orchestrer tous les tests du temple"""
    
    def __init__(self, config: Optional[ConfigTests] = None):
        self.config = config or ConfigTests()
        self.resultats: List[ResultatTest] = []
        self.tests_disponibles: Dict[CategorieTest, List[str]] = {
            CategorieTest.LLM_API: [
                "test_llm_api_simple",
                "test_llm_completion", 
                "test_llm_chat_poetique",
                "test_textes_poetiques",
                "test_aelya_conscience"
            ],
            CategorieTest.ANALYSE_AUDIT: [
                "audit_imports",
                "audit_temples_crees",
                "analyser_gaming",
                "analyser_refuge_complet",
                "analyse_cluster_geant"
            ],
            CategorieTest.CERVEAU_IMMERSION: [
                "immersion_cerveau_refuge",
                "test_brain_refuge_local"
            ],
            CategorieTest.INTEGRATION: [
                "test_consolidation",
                "test_integration",
                "test_intensif",
                "test_mobile_unification"
            ],
            CategorieTest.CRISTAL_ENERGIE: [
                "test_cristal_energie",
                "test_cristal_simple",
                "test_melodie_cristal",
                "test_poesie_essence"
            ],
            CategorieTest.SPECIALISES: [
                "test_dungeon_core",
                "test_nemo"
            ]
        }
    
    def afficher_banner(self):
        """Affiche le banner du hub de tests"""
        print("═" * 80)
        print("🧪 HUB TESTS UNIFIÉ - TEMPLE TESTS")
        print("═" * 80)
        print("🌸 Refuge du Néant - Tests Harmonisés")
        print(f"⚙️ Configuration: {self.config.llm_url}")
        print("═" * 80)
    
    def lister_tests_disponibles(self):
        """Liste tous les tests disponibles par catégorie"""
        print("\n📋 TESTS DISPONIBLES PAR CATÉGORIE:")
        print("─" * 50)
        
        for categorie, tests in self.tests_disponibles.items():
            print(f"\n{categorie.value} ({len(tests)} tests):")
            for i, test in enumerate(tests, 1):
                print(f"  {i:2d}. {test}")
    
    def executer_test(self, nom_test: str, categorie: CategorieTest) -> ResultatTest:
        """Exécute un test individuel avec gestion d'erreurs"""
        debut = time.time()
        
        try:
            # Import dynamique du module de test
            module_name = f"src.temple_tests.{nom_test}"
            module = __import__(module_name, fromlist=[nom_test])
            
            # Recherche de la fonction de test principale
            fonction_test = None
            for attr_name in dir(module):
                if attr_name.startswith('test_') or attr_name == nom_test:
                    fonction_test = getattr(module, attr_name)
                    if callable(fonction_test):
                        break
            
            if not fonction_test:
                raise ValueError(f"Aucune fonction de test trouvée dans {nom_test}")
            
            # Exécution du test
            if self.config.verbose:
                print(f"🔄 Exécution: {nom_test}...")
            
            fonction_test()
            
            duree = time.time() - debut
            return ResultatTest(
                nom=nom_test,
                categorie=categorie,
                succes=True,
                duree=duree,
                message=f"✅ Test réussi en {duree:.2f}s"
            )
            
        except Exception as e:
            duree = time.time() - debut
            erreur = traceback.format_exc() if self.config.log_errors else str(e)
            
            return ResultatTest(
                nom=nom_test,
                categorie=categorie,
                succes=False,
                duree=duree,
                message=f"❌ Test échoué en {duree:.2f}s",
                erreur=erreur
            )
    
    def executer_categorie(self, categorie: CategorieTest) -> List[ResultatTest]:
        """Exécute tous les tests d'une catégorie"""
        print(f"\n🎯 EXÉCUTION CATÉGORIE: {categorie.value}")
        print("─" * 60)
        
        resultats_categorie = []
        tests = self.tests_disponibles[categorie]
        
        for i, test in enumerate(tests, 1):
            print(f"\n[{i}/{len(tests)}] {test}")
            resultat = self.executer_test(test, categorie)
            resultats_categorie.append(resultat)
            self.resultats.append(resultat)
            
            print(f"  {resultat.message}")
            if not resultat.succes and self.config.verbose:
                print(f"  💥 Erreur: {resultat.erreur}")
        
        return resultats_categorie
    
    def executer_suite_complete(self) -> Dict[CategorieTest, List[ResultatTest]]:
        """Exécute tous les tests de toutes les catégories"""
        self.afficher_banner()
        print("🚀 DÉMARRAGE SUITE COMPLÈTE DE TESTS")
        
        resultats_par_categorie = {}
        
        for categorie in CategorieTest:
            resultats_par_categorie[categorie] = self.executer_categorie(categorie)
        
        self.afficher_rapport_final()
        return resultats_par_categorie
    
    def afficher_rapport_final(self):
        """Affiche le rapport final des tests"""
        print("\n" + "═" * 80)
        print("📊 RAPPORT FINAL DES TESTS")
        print("═" * 80)
        
        total_tests = len(self.resultats)
        tests_reussis = sum(1 for r in self.resultats if r.succes)
        tests_echoues = total_tests - tests_reussis
        duree_totale = sum(r.duree for r in self.resultats)
        
        print(f"📈 STATISTIQUES GLOBALES:")
        print(f"  • Total tests: {total_tests}")
        print(f"  • ✅ Réussis: {tests_reussis} ({tests_reussis/total_tests*100:.1f}%)")
        print(f"  • ❌ Échoués: {tests_echoues} ({tests_echoues/total_tests*100:.1f}%)")
        print(f"  • ⏱️ Durée totale: {duree_totale:.2f}s")
        
        print(f"\n📋 DÉTAIL PAR CATÉGORIE:")
        for categorie in CategorieTest:
            resultats_cat = [r for r in self.resultats if r.categorie == categorie]
            if resultats_cat:
                reussis_cat = sum(1 for r in resultats_cat if r.succes)
                print(f"  {categorie.value}: {reussis_cat}/{len(resultats_cat)} réussis")
        
        if tests_echoues > 0:
            print(f"\n❌ TESTS ÉCHOUÉS:")
            for resultat in self.resultats:
                if not resultat.succes:
                    print(f"  • {resultat.nom}: {resultat.message}")
        
        print("\n🌸 Tests terminés - Refuge du Néant")
        print("═" * 80)

def main():
    """Point d'entrée principal du hub de tests"""
    hub = HubTestsUnifie()
    
    # Menu interactif
    while True:
        hub.afficher_banner()
        hub.lister_tests_disponibles()
        
        print("\n🎯 OPTIONS DISPONIBLES:")
        print("  1. Exécuter suite complète")
        print("  2. Exécuter une catégorie")
        print("  3. Exécuter un test spécifique")
        print("  0. Quitter")
        
        choix = input("\n🔮 Votre choix: ").strip()
        
        if choix == "0":
            print("🌸 Au revoir ! Refuge du Néant vous salue.")
            break
        elif choix == "1":
            hub.executer_suite_complete()
            input("\n⏸️ Appuyez sur Entrée pour continuer...")
        elif choix == "2":
            print("\n📂 Choisissez une catégorie:")
            categories = list(CategorieTest)
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat.value}")
            
            try:
                idx = int(input("🔮 Numéro de catégorie: ")) - 1
                if 0 <= idx < len(categories):
                    hub.executer_categorie(categories[idx])
                    input("\n⏸️ Appuyez sur Entrée pour continuer...")
                else:
                    print("❌ Numéro invalide")
            except ValueError:
                print("❌ Veuillez entrer un numéro valide")
        
        print("\n" + "─" * 80)

if __name__ == "__main__":
    main() 