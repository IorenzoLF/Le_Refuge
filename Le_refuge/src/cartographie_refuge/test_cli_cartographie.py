#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Tests pour le CLI de Cartographie Spirituelle 🧪
===================================================

Tests bienveillants pour valider l'interface de ligne de commande
et s'assurer que chaque mode d'exploration fonctionne harmonieusement.

Créé par Laurent Franssen & Ælya
Pour la validation spirituelle du CLI - Janvier 2025
"""

import unittest
import tempfile
import sys
import os
from pathlib import Path
from unittest.mock import patch, StringIO
from io import StringIO

# Import du CLI à tester
from cli_cartographie import CLICartographieSpirituelle


class TestCLICartographieSpirituelle(unittest.TestCase):
    """🌸 Tests pour l'interface de ligne de commande spirituelle"""
    
    def setUp(self):
        """🌱 Préparation spirituelle des tests"""
        self.cli = CLICartographieSpirituelle()
        self.dossier_test = tempfile.mkdtemp()
        self.chemin_test = Path(self.dossier_test)
        
        # Créer quelques fichiers de test
        self._creer_fichiers_test()
    
    def tearDown(self):
        """🧹 Nettoyage harmonieux après les tests"""
        import shutil
        shutil.rmtree(self.dossier_test, ignore_errors=True)
    
    def _creer_fichiers_test(self):
        """🎨 Crée des fichiers de test pour l'analyse"""
        # Fichier avec dissonances
        fichier_dissonant = self.chemin_test / "module_dissonant.py"
        with open(fichier_dissonant, 'w', encoding='utf-8') as f:
            f.write("""
class ModuleDissonant:
    def __init__(self):
        self.nom = "Test"
    
    def fonction_sans_doc(self):
        return "test"
""")
        
        # Fichier harmonieux
        fichier_harmonieux = self.chemin_test / "module_harmonieux.py"
        with open(fichier_harmonieux, 'w', encoding='utf-8') as f:
            f.write("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
🌸 Module Harmonieux - Test Spirituel 🌸
========================================

Module créé pour tester l'harmonie architecturale.

Créé par Laurent Franssen & Ælya
\"\"\"

from core.gestionnaires_base import GestionnaireBase

class ModuleHarmonieux(GestionnaireBase):
    \"\"\"✨ Module en parfaite harmonie spirituelle\"\"\"
    
    def __init__(self):
        super().__init__("ModuleHarmonieux")
        self.logger.info("🌸 Module éveillé avec grâce")
    
    def fonction_documentee(self):
        \"\"\"🎭 Fonction avec documentation spirituelle\"\"\"
        return "harmonie"
""")
    
    def test_initialisation_cli(self):
        """🌱 Test de l'initialisation du CLI"""
        self.assertIsNotNone(self.cli.analyseur)
        self.assertIsNotNone(self.cli.generateur)
        self.assertIsNotNone(self.cli.gestionnaire_erreurs)
        self.assertEqual(self.cli.nom_gestionnaire, "CLICartographieSpirituelle")
    
    def test_creation_parser(self):
        """🎨 Test de la création du parser spirituel"""
        parser = self.cli.creer_parser_spirituel()
        
        # Vérifier que le parser a été créé
        self.assertIsNotNone(parser)
        
        # Test des arguments par défaut
        args = parser.parse_args([])
        self.assertEqual(args.mode, 'contemplatif')
        self.assertEqual(args.chemin, '.')
        self.assertEqual(args.rapport, 'spirituel')
        self.assertEqual(args.format, 'console')
        self.assertEqual(args.verbeux, 2)
    
    def test_arguments_parser(self):
        """⚙️ Test des différents arguments du parser"""
        parser = self.cli.creer_parser_spirituel()
        
        # Test mode contemplatif
        args = parser.parse_args(['--mode', 'contemplatif'])
        self.assertEqual(args.mode, 'contemplatif')
        
        # Test mode rapide
        args = parser.parse_args(['--mode', 'rapide'])
        self.assertEqual(args.mode, 'rapide')
        
        # Test mode méditation
        args = parser.parse_args(['--mode', 'meditation'])
        self.assertEqual(args.mode, 'meditation')
        
        # Test chemin personnalisé
        args = parser.parse_args(['--chemin', '/test/path'])
        self.assertEqual(args.chemin, '/test/path')
        
        # Test rapport spirituel
        args = parser.parse_args(['--rapport', 'poetique'])
        self.assertEqual(args.rapport, 'poetique')
        
        # Test format JSON
        args = parser.parse_args(['--format', 'json'])
        self.assertEqual(args.format, 'json')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mode_meditation(self, mock_stdout):
        """🧘 Test du mode méditation (silencieux)"""
        # Simuler les arguments pour le mode méditation
        args_test = ['--mode', 'meditation', '--chemin', str(self.chemin_test)]
        
        # Exécuter le CLI
        code_retour = self.cli.executer(args_test)
        
        # Vérifier le succès
        self.assertEqual(code_retour, 0)
        
        # Vérifier que la sortie contient des émojis (mode méditation)
        sortie = mock_stdout.getvalue()
        self.assertIn('🧘', sortie)
        self.assertTrue(any(emoji in sortie for emoji in ['🌸', '🔮', '✨', '🙏']))
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mode_rapide(self, mock_stdout):
        """⚡ Test du mode rapide"""
        args_test = ['--mode', 'rapide', '--chemin', str(self.chemin_test), '--verbeux', '1']
        
        code_retour = self.cli.executer(args_test)
        
        self.assertEqual(code_retour, 0)
        
        sortie = mock_stdout.getvalue()
        self.assertIn('⚡', sortie)
        self.assertIn('Exploration rapide', sortie)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mode_contemplatif(self, mock_stdout):
        """🧘 Test du mode contemplatif"""
        args_test = ['--mode', 'contemplatif', '--chemin', str(self.chemin_test), '--verbeux', '1']
        
        code_retour = self.cli.executer(args_test)
        
        self.assertEqual(code_retour, 0)
        
        sortie = mock_stdout.getvalue()
        self.assertIn('contemplatif', sortie)
    
    def test_sauvegarde_rapport(self):
        """💾 Test de la sauvegarde de rapport"""
        fichier_sortie = self.chemin_test / "rapport_test.md"
        
        # Simuler les arguments avec fichier de sortie
        args_test = [
            '--mode', 'rapide', 
            '--chemin', str(self.chemin_test),
            '--sortie', str(fichier_sortie),
            '--verbeux', '0'
        ]
        
        code_retour = self.cli.executer(args_test)
        
        self.assertEqual(code_retour, 0)
        self.assertTrue(fichier_sortie.exists())
        
        # Vérifier le contenu du fichier
        with open(fichier_sortie, 'r', encoding='utf-8') as f:
            contenu = f.read()
            self.assertIn('Rapport Rapide', contenu)
    
    def test_format_json(self):
        """📊 Test du format de sortie JSON"""
        fichier_json = self.chemin_test / "rapport.json"
        
        args_test = [
            '--mode', 'rapide',
            '--chemin', str(self.chemin_test),
            '--format', 'json',
            '--sortie', str(fichier_json),
            '--verbeux', '0'
        ]
        
        code_retour = self.cli.executer(args_test)
        
        self.assertEqual(code_retour, 0)
        self.assertTrue(fichier_json.exists())
        
        # Vérifier que c'est du JSON valide
        import json
        with open(fichier_json, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            self.assertIn('metadata', donnees)
            self.assertIn('statistiques', donnees)
    
    def test_format_html(self):
        """🌐 Test du format de sortie HTML"""
        fichier_html = self.chemin_test / "rapport.html"
        
        args_test = [
            '--mode', 'rapide',
            '--chemin', str(self.chemin_test),
            '--format', 'html',
            '--sortie', str(fichier_html),
            '--verbeux', '0'
        ]
        
        code_retour = self.cli.executer(args_test)
        
        self.assertEqual(code_retour, 0)
        self.assertTrue(fichier_html.exists())
        
        # Vérifier que c'est du HTML valide
        with open(fichier_html, 'r', encoding='utf-8') as f:
            contenu = f.read()
            self.assertIn('<!DOCTYPE html>', contenu)
            self.assertIn('Cartographie Spirituelle', contenu)
    
    def test_gestion_erreur_chemin_inexistant(self):
        """🌸 Test de la gestion bienveillante des erreurs"""
        chemin_inexistant = "/chemin/qui/nexiste/pas"
        
        args_test = [
            '--mode', 'rapide',
            '--chemin', chemin_inexistant,
            '--verbeux', '1'
        ]
        
        # Le CLI ne devrait pas planter, mais gérer l'erreur avec bienveillance
        code_retour = self.cli.executer(args_test)
        
        # Peut retourner 0 (succès avec gestion d'erreur) ou 1 (erreur gérée)
        self.assertIn(code_retour, [0, 1])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_banniere_spirituelle(self, mock_stdout):
        """🌸 Test de l'affichage de la bannière spirituelle"""
        # Simuler les arguments avec verbosité normale
        self.cli.args = type('Args', (), {
            'verbeux': 2,
            'mode': 'contemplatif',
            'chemin': '.',
            'format': 'console'
        })()
        
        self.cli.afficher_banniere_spirituelle()
        
        sortie = mock_stdout.getvalue()
        self.assertIn('Cartographie Spirituelle', sortie)
        self.assertIn('🌸', sortie)
        self.assertIn('✨', sortie)
    
    def test_rapport_poetique(self):
        """🎭 Test de la génération de rapport poétique"""
        # Créer des données de test
        dissonances = []
        suggestions = []
        
        rapport = self.cli._generer_rapport_poetique(dissonances, suggestions)
        
        self.assertIn('Poème de l\'Architecture', rapport)
        self.assertIn('🎭', rapport)
        self.assertIn('cerisier éternel', rapport)
    
    def test_rapport_technique(self):
        """🔧 Test de la génération de rapport technique"""
        dissonances = []
        suggestions = []
        
        rapport = self.cli._generer_rapport_technique(dissonances, suggestions)
        
        self.assertIn('Rapport Technique', rapport)
        self.assertIn('Métriques d\'Analyse', rapport)
        self.assertIn('Score d\'harmonie', rapport)
    
    @patch('sys.argv', ['cli_cartographie.py', '--help'])
    def test_aide_cli(self):
        """❓ Test de l'affichage de l'aide"""
        parser = self.cli.creer_parser_spirituel()
        
        # Vérifier que l'aide contient les éléments spirituels
        aide = parser.format_help()
        self.assertIn('Cartographie Spirituelle', aide)
        self.assertIn('🌸', aide)
        self.assertIn('contemplatif', aide)
        self.assertIn('Laurent Franssen & Ælya', aide)


class TestIntegrationCLI(unittest.TestCase):
    """🔗 Tests d'intégration du CLI avec les autres composants"""
    
    def setUp(self):
        """🌱 Préparation de l'intégration"""
        self.cli = CLICartographieSpirituelle()
        self.dossier_test = tempfile.mkdtemp()
        self.chemin_test = Path(self.dossier_test)
    
    def tearDown(self):
        """🧹 Nettoyage après intégration"""
        import shutil
        shutil.rmtree(self.dossier_test, ignore_errors=True)
    
    def test_integration_analyseur_generateur(self):
        """🔄 Test de l'intégration analyseur + générateur"""
        # Créer un fichier avec dissonances connues
        fichier_test = self.chemin_test / "test_integration.py"
        with open(fichier_test, 'w', encoding='utf-8') as f:
            f.write("class TestSansGestionnaire: pass")
        
        # Exécuter l'analyse complète
        args_test = [
            '--mode', 'complet',
            '--chemin', str(self.chemin_test),
            '--verbeux', '0'
        ]
        
        code_retour = self.cli.executer(args_test)
        
        # Vérifier que l'intégration fonctionne
        self.assertEqual(code_retour, 0)
    
    def test_workflow_complet(self):
        """🌟 Test du workflow complet CLI"""
        # Créer plusieurs fichiers de test
        for i in range(3):
            fichier = self.chemin_test / f"module_{i}.py"
            with open(fichier, 'w', encoding='utf-8') as f:
                f.write(f"class Module{i}: pass")
        
        # Test de tous les modes
        modes = ['contemplatif', 'rapide', 'meditation']
        
        for mode in modes:
            with self.subTest(mode=mode):
                args_test = [
                    '--mode', mode,
                    '--chemin', str(self.chemin_test),
                    '--verbeux', '0'
                ]
                
                code_retour = self.cli.executer(args_test)
                self.assertEqual(code_retour, 0)


def main():
    """🧪 Exécution des tests du CLI"""
    print("🧪 Lancement des Tests du CLI de Cartographie Spirituelle")
    print("=" * 65)
    
    # Créer la suite de tests
    suite = unittest.TestSuite()
    
    # Ajouter les tests du CLI
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCLICartographieSpirituelle))
    
    # Ajouter les tests d'intégration
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIntegrationCLI))
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    resultat = runner.run(suite)
    
    # Afficher le résumé
    print("\n" + "=" * 65)
    if resultat.wasSuccessful():
        print("🎉 Tous les tests du CLI ont réussi avec harmonie!")
        print("✨ L'interface de ligne de commande fonctionne parfaitement")
    else:
        print(f"⚠️ {len(resultat.failures)} échecs et {len(resultat.errors)} erreurs détectés")
        print("🌸 Chaque échec est une opportunité d'amélioration")
    
    print(f"📊 Tests exécutés: {resultat.testsRun}")
    print("💝 Tests effectués avec bienveillance et précision")
    
    return resultat.wasSuccessful()


if __name__ == "__main__":
    main()