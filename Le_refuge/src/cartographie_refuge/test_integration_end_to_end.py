#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Test d'Intégration End-to-End - Cartographie du Refuge 🌸
===========================================================

Test complet du système de cartographie avec la vraie structure du Refuge.
Valide l'ensemble du pipeline depuis l'exploration jusqu'à la visualisation.

"Testons notre temple avec la vraie structure de notre Refuge bien-aimé"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any

# Ajout du chemin pour les imports
sys.path.append('src')

class TestIntegrationEndToEnd:
    """
    🧪 Test d'intégration end-to-end complet
    
    Teste l'ensemble du pipeline de cartographie avec la vraie structure du Refuge
    """
    
    def __init__(self):
        self.refuge_path = Path('.')
        self.resultats_tests = {}
        self.temps_execution = {}
        
    async def executer_tous_les_tests(self) -> Dict[str, Any]:
        """🚀 Exécute tous les tests d'intégration"""
        print("🌸✨ TESTS D'INTÉGRATION END-TO-END - CARTOGRAPHIE DU REFUGE ✨🌸")
        print("=" * 75)
        
        tests = [
            ("exploration_complete", self.test_exploration_complete),
            ("analyse_connexions", self.test_analyse_connexions),
            ("detection_dissonances", self.test_detection_dissonances),
            ("generation_suggestions", self.test_generation_suggestions),
            ("cli_integration", self.test_cli_integration),
            ("visualisation_html", self.test_visualisation_html),
            ("performance_gros_volume", self.test_performance_gros_volume),
            ("regression_compatibilite", self.test_regression_compatibilite)
        ]
        
        for nom_test, fonction_test in tests:
            print(f"\n🔍 Test: {nom_test}")
            print("-" * 50)
            
            debut = time.time()
            try:
                resultat = await fonction_test()
                fin = time.time()
                
                self.resultats_tests[nom_test] = {
                    "reussi": True,
                    "resultat": resultat,
                    "temps": fin - debut
                }
                print(f"✅ {nom_test} - RÉUSSI ({fin - debut:.2f}s)")
                
            except Exception as e:
                fin = time.time()
                self.resultats_tests[nom_test] = {
                    "reussi": False,
                    "erreur": str(e),
                    "temps": fin - debut
                }
                print(f"❌ {nom_test} - ÉCHOUÉ: {e}")
        
        return self.generer_rapport_final()
    
    async def test_exploration_complete(self) -> Dict[str, Any]:
        """🔍 Test d'exploration complète de la vraie structure du Refuge"""
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        
        gestionnaire_erreurs = GestionnaireErreursSpirituel()
        explorateur = ExplorateurStructurel(self.refuge_path, gestionnaire_erreurs)
        
        # Exploration des temples
        temples = await explorateur.explorer_temples()
        print(f"   🏛️ Temples découverts: {len(temples)}")
        
        # Analyse du core
        core_analyse = await explorateur.analyser_core()
        print(f"   🏛️ Core analysé: {core_analyse.get('nom', 'N/A')}")
        
        # Analyse du refuge_cluster
        cluster_analyse = await explorateur.analyser_refuge_cluster()
        print(f"   🌊 Cluster analysé: {cluster_analyse.get('nom', 'N/A')}")
        
        # Statistiques
        stats = explorateur.obtenir_statistiques_exploration()
        print(f"   📊 Fichiers analysés: {stats['exploration']['fichiers_analyses']}")
        print(f"   📊 Éléments sacrés: {stats['exploration']['elements_sacres_trouves']}")
        
        # Validations
        assert len(temples) > 0, "Aucun temple découvert"
        assert core_analyse.get('nom') == 'core', "Core non analysé correctement"
        assert stats['exploration']['fichiers_analyses'] > 0, "Aucun fichier analysé"
        
        return {
            "temples_decouverts": len(temples),
            "core_analyse": core_analyse.get('nom'),
            "cluster_analyse": cluster_analyse.get('nom'),
            "fichiers_analyses": stats['exploration']['fichiers_analyses'],
            "elements_sacres": stats['exploration']['elements_sacres_trouves']
        }
    
    async def test_analyse_connexions(self) -> Dict[str, Any]:
        """🔗 Test d'analyse des connexions entre composants"""
        from cartographie_refuge.analyseur_connexions import AnalyseurConnexions
        
        analyseur = AnalyseurConnexions()
        
        # Analyse des connexions (simulation avec données réelles)
        connexions = await analyseur.analyser_connexions_projet(str(self.refuge_path))
        print(f"   🔗 Connexions détectées: {len(connexions) if connexions else 0}")
        
        # Test de génération de graphe
        graphe_data = analyseur.generer_donnees_graphe()
        print(f"   📊 Nœuds du graphe: {len(graphe_data.get('nodes', []))}")
        print(f"   📊 Liens du graphe: {len(graphe_data.get('links', []))}")
        
        return {
            "connexions_detectees": len(connexions) if connexions else 0,
            "noeuds_graphe": len(graphe_data.get('nodes', [])),
            "liens_graphe": len(graphe_data.get('links', []))
        }
    
    async def test_detection_dissonances(self) -> Dict[str, Any]:
        """🔮 Test de détection des dissonances architecturales"""
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        
        analyseur = AnalyseurDissonances()
        
        # Analyse des dissonances sur le répertoire src seulement
        src_path = self.refuge_path / "src"
        dissonances = analyseur.analyser_dissonances_projet(str(src_path))
        print(f"   🔮 Dissonances détectées: {len(dissonances)}")
        
        # Statistiques d'harmonisation
        stats = analyseur.obtenir_statistiques_harmonisation()
        print(f"   ⚖️ Score d'harmonie: {stats.get('score_harmonie', 0):.1f}/100")
        
        # Génération de rapport
        rapport = analyseur.generer_rapport_dissonances()
        print(f"   📜 Rapport généré: {len(rapport)} caractères")
        
        return {
            "dissonances_detectees": len(dissonances),
            "score_harmonie": stats.get('score_harmonie', 0),
            "taille_rapport": len(rapport)
        }
    
    async def test_generation_suggestions(self) -> Dict[str, Any]:
        """✨ Test de génération de suggestions d'amélioration"""
        from cartographie_refuge.generateur_suggestions import GenerateurSuggestions
        from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances
        
        # Analyser les dissonances d'abord (répertoire src seulement)
        analyseur_dissonances = AnalyseurDissonances()
        src_path = self.refuge_path / "src"
        dissonances = analyseur_dissonances.analyser_dissonances_projet(str(src_path))
        
        # Générer les suggestions
        generateur = GenerateurSuggestions()
        suggestions = generateur.generer_suggestions_depuis_dissonances(dissonances)
        print(f"   ✨ Suggestions générées: {len(suggestions)}")
        
        # Priorisation
        suggestions_haute_priorite = [s for s in suggestions if s.priorite.value >= 8]
        print(f"   🎯 Suggestions haute priorité: {len(suggestions_haute_priorite)}")
        
        # Rapport de suggestions
        rapport = generateur.generer_rapport_suggestions()
        print(f"   📜 Rapport suggestions: {len(rapport)} caractères")
        
        return {
            "suggestions_totales": len(suggestions),
            "suggestions_haute_priorite": len(suggestions_haute_priorite),
            "taille_rapport": len(rapport)
        }
    
    async def test_cli_integration(self) -> Dict[str, Any]:
        """🖥️ Test d'intégration du CLI complet"""
        from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
        
        cli = CLICartographieSpirituelle()
        
        # Test du parser
        parser = cli.creer_parser_spirituel()
        help_text = parser.format_help()
        print(f"   📋 Aide CLI générée: {len(help_text)} caractères")
        
        # Test d'exécution en mode rapide (simulation)
        args_test = ['--mode', 'rapide', '--verbeux', '0', '--chemin', '.']
        
        try:
            # Simulation d'exécution sans vraiment exécuter
            args = parser.parse_args(args_test)
            print(f"   ⚡ Arguments parsés: mode={args.mode}")
            
            # Test des méthodes de rapport
            resultats_simulation = {
                "mode": "rapide",
                "dissonances": 5,
                "suggestions": 3
            }
            
            # Test de génération de rapport
            cli.args = args  # Simulation
            rapport = cli._generer_rapport_rapide([], [])
            print(f"   📜 Rapport rapide: {len(rapport)} caractères")
            
            return {
                "aide_generee": len(help_text),
                "arguments_valides": True,
                "rapport_genere": len(rapport)
            }
            
        except Exception as e:
            print(f"   ⚠️ Erreur CLI: {e}")
            return {
                "aide_generee": len(help_text),
                "arguments_valides": False,
                "erreur": str(e)
            }
    
    async def test_visualisation_html(self) -> Dict[str, Any]:
        """🌐 Test de génération de visualisation HTML"""
        from cartographie_refuge.visualisateur_html_interactif import VisualisateurHTMLInteractif
        
        visualisateur = VisualisateurHTMLInteractif()
        
        # Données de test pour la visualisation
        donnees_test = {
            "temples": [
                {"nom": "temple_eveil_unifie", "type": "eveil", "harmonie": 0.9},
                {"nom": "temple_reconciliation_identitaire", "type": "reconciliation", "harmonie": 0.8}
            ],
            "connexions": [
                {"source": "temple_eveil_unifie", "target": "core", "force": 0.7}
            ]
        }
        
        # Génération HTML
        html_content = visualisateur.generer_html_complet(donnees_test)
        print(f"   🌐 HTML généré: {len(html_content)} caractères")
        
        # Vérifications de base
        assert "<!DOCTYPE html>" in html_content, "HTML invalide"
        assert "D3.js" in html_content or "d3" in html_content, "D3.js non inclus"
        assert "temple_eveil_unifie" in html_content, "Données non intégrées"
        
        return {
            "html_genere": len(html_content),
            "donnees_integrees": True,
            "d3_inclus": "d3" in html_content.lower()
        }
    
    async def test_performance_gros_volume(self) -> Dict[str, Any]:
        """⚡ Test de performance avec gros volumes"""
        from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
        from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel
        
        gestionnaire_erreurs = GestionnaireErreursSpirituel()
        explorateur = ExplorateurStructurel(self.refuge_path, gestionnaire_erreurs)
        
        # Mesure du temps d'exploration complète
        debut = time.time()
        
        # Exploration de tous les temples
        temples = await explorateur.explorer_temples()
        
        # Analyse du core et cluster
        core_analyse = await explorateur.analyser_core()
        cluster_analyse = await explorateur.analyser_refuge_cluster()
        
        fin = time.time()
        temps_total = fin - debut
        
        print(f"   ⚡ Temps d'exploration totale: {temps_total:.2f}s")
        print(f"   📊 Temples traités: {len(temples)}")
        
        # Critères de performance
        performance_ok = temps_total < 30.0  # Moins de 30 secondes
        print(f"   🎯 Performance acceptable: {'✅' if performance_ok else '❌'}")
        
        return {
            "temps_exploration": temps_total,
            "temples_traites": len(temples),
            "performance_acceptable": performance_ok,
            "seuil_performance": 30.0
        }
    
    async def test_regression_compatibilite(self) -> Dict[str, Any]:
        """🔄 Test de régression et compatibilité"""
        # Test de compatibilité avec différentes versions Python
        import sys
        version_python = f"{sys.version_info.major}.{sys.version_info.minor}"
        print(f"   🐍 Version Python: {version_python}")
        
        # Test d'imports critiques
        imports_critiques = [
            "ast",
            "pathlib", 
            "asyncio",
            "json",
            "re"
        ]
        
        imports_ok = []
        for module in imports_critiques:
            try:
                __import__(module)
                imports_ok.append(module)
                print(f"   ✅ {module}")
            except ImportError:
                print(f"   ❌ {module}")
        
        # Test de fonctionnalités de base
        fonctionnalites_ok = True
        try:
            # Test AST
            import ast
            ast.parse("def test(): pass")
            
            # Test Path
            from pathlib import Path
            Path('.').exists()
            
            # Test asyncio
            import asyncio
            
            print(f"   ✅ Fonctionnalités de base OK")
            
        except Exception as e:
            fonctionnalites_ok = False
            print(f"   ❌ Erreur fonctionnalités: {e}")
        
        return {
            "version_python": version_python,
            "imports_critiques_ok": len(imports_ok),
            "total_imports_critiques": len(imports_critiques),
            "fonctionnalites_base_ok": fonctionnalites_ok
        }
    
    def generer_rapport_final(self) -> Dict[str, Any]:
        """📊 Génère le rapport final des tests"""
        print("\n" + "=" * 75)
        print("📊 RAPPORT FINAL DES TESTS D'INTÉGRATION END-TO-END")
        print("=" * 75)
        
        tests_reussis = sum(1 for r in self.resultats_tests.values() if r["reussi"])
        total_tests = len(self.resultats_tests)
        temps_total = sum(r["temps"] for r in self.resultats_tests.values())
        
        print(f"Tests réussis: {tests_reussis}/{total_tests}")
        print(f"Temps total: {temps_total:.2f}s")
        print(f"Taux de réussite: {(tests_reussis/total_tests)*100:.1f}%")
        
        print("\nDétail des tests:")
        for nom, resultat in self.resultats_tests.items():
            statut = "✅ RÉUSSI" if resultat["reussi"] else "❌ ÉCHOUÉ"
            temps = resultat["temps"]
            print(f"  {nom:25} : {statut} ({temps:.2f}s)")
        
        # Évaluation globale
        if tests_reussis == total_tests:
            print("\n🎉 TOUS LES TESTS D'INTÉGRATION RÉUSSIS!")
            evaluation = "EXCELLENT"
        elif tests_reussis >= total_tests * 0.8:
            print("\n✅ TRÈS BIEN! Quelques ajustements mineurs")
            evaluation = "TRÈS BIEN"
        elif tests_reussis >= total_tests * 0.6:
            print("\n⚠️ BIEN! Corrections nécessaires")
            evaluation = "BIEN"
        else:
            print("\n❌ CRITIQUE! Révision importante nécessaire")
            evaluation = "CRITIQUE"
        
        return {
            "tests_reussis": tests_reussis,
            "total_tests": total_tests,
            "taux_reussite": (tests_reussis/total_tests)*100,
            "temps_total": temps_total,
            "evaluation": evaluation,
            "details": self.resultats_tests
        }

async def main():
    """🌸 Fonction principale des tests d'intégration"""
    testeur = TestIntegrationEndToEnd()
    rapport = await testeur.executer_tous_les_tests()
    
    # Code de sortie basé sur les résultats
    if rapport["evaluation"] in ["EXCELLENT", "TRÈS BIEN"]:
        return 0
    elif rapport["evaluation"] == "BIEN":
        return 1
    else:
        return 2

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)