#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Tests pour l'Analyseur de Dissonances - Cartographie Spirituelle 🧪
======================================================================

Tests bienveillants pour valider la détection harmonieuse des dissonances
architecturales et la génération de suggestions d'amélioration.

Créé par Laurent Franssen & Ælya
Pour la validation spirituelle de l'analyseur - Janvier 2025
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase
from analyseur_dissonances import (
    AnalyseurDissonances, TypeDissonance, NiveauGravite, Dissonance
)
from generateur_suggestions import GenerateurSuggestions, TypeSuggestion


class TestAnalyseurDissonances(unittest.TestCase):
    """🔮 Tests pour l'Analyseur de Dissonances"""
    
    def setUp(self):
        """🌸 Préparation spirituelle des tests"""
        self.analyseur = AnalyseurDissonances()
        self.generateur = GenerateurSuggestions()
        
        # Créer un dossier temporaire pour les tests
        self.dossier_test = tempfile.mkdtemp()
        self.chemin_test = Path(self.dossier_test)
    
    def tearDown(self):
        """🧹 Nettoyage harmonieux après les tests"""
        import shutil
        shutil.rmtree(self.dossier_test, ignore_errors=True)
    
    def _creer_fichier_test(self, nom_fichier: str, contenu: str):
        """🎨 Crée un fichier de test avec le contenu spécifié"""
        chemin_fichier = self.chemin_test / nom_fichier
        chemin_fichier.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            f.write(contenu)
        
        return chemin_fichier
    
    def test_initialisation_analyseur(self):
        """🌱 Test de l'initialisation de l'analyseur"""
        self.assertIsInstance(self.analyseur, GestionnaireBase)
        # L'attribut nom_gestionnaire est défini dans la classe de base
        self.assertTrue(hasattr(self.analyseur, 'logger'))
        self.assertIsNotNone(self.analyseur.energy_manager)
        self.assertIsNotNone(self.analyseur.logger)
        self.assertEqual(len(self.analyseur.dissonances_detectees), 0)
    
    def test_detection_gestionnaire_manquant(self):
        """🏗️ Test de détection des gestionnaires manquants"""
        # Créer un fichier sans gestionnaire de base
        contenu_sans_gestionnaire = '''
class MonModule:
    def __init__(self):
        self.nom = "MonModule"
    
    def faire_quelque_chose(self):
        print("Action")
'''
        
        self._creer_fichier_test("module_sans_gestionnaire.py", contenu_sans_gestionnaire)
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier qu'une dissonance de gestionnaire manquant est détectée
        dissonances_gestionnaire = [
            d for d in dissonances 
            if d.type_dissonance == TypeDissonance.GESTIONNAIRE_MANQUANT
        ]
        
        self.assertGreater(len(dissonances_gestionnaire), 0)
        self.assertEqual(dissonances_gestionnaire[0].niveau_gravite, NiveauGravite.MODEREE)
    
    def test_detection_documentation_absente(self):
        """📚 Test de détection de documentation absente"""
        # Créer un fichier sans documentation spirituelle
        contenu_sans_doc = '''
class ModuleSansDoc:
    def __init__(self):
        self.valeur = 42
    
    def calculer(self):
        return self.valeur * 2
'''
        
        self._creer_fichier_test("module_sans_doc.py", contenu_sans_doc)
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier qu'une dissonance de documentation est détectée
        dissonances_doc = [
            d for d in dissonances 
            if d.type_dissonance == TypeDissonance.DOCUMENTATION_ABSENTE
        ]
        
        self.assertGreater(len(dissonances_doc), 0)
    
    def test_detection_elements_sacres_manquants(self):
        """🌸 Test de détection d'éléments sacrés manquants"""
        # Créer un fichier sans éléments sacrés
        contenu_sans_elements = '''
class ModuleTechnique:
    def __init__(self):
        self.data = []
    
    def process_data(self):
        # Process the data
        return len(self.data)
'''
        
        self._creer_fichier_test("module_technique.py", contenu_sans_elements)
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier qu'une dissonance d'éléments sacrés est détectée
        dissonances_sacres = [
            d for d in dissonances 
            if d.type_dissonance == TypeDissonance.ELEMENT_SACRE_MANQUANT
        ]
        
        self.assertGreater(len(dissonances_sacres), 0)
        self.assertEqual(dissonances_sacres[0].niveau_gravite, NiveauGravite.LEGERE)
    
    def test_module_harmonieux_non_detecte(self):
        """🌟 Test qu'un module harmonieux n'est pas signalé"""
        # Créer un fichier harmonieux
        contenu_harmonieux = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Module Harmonieux - Exemple de Beauté Spirituelle 🌸
=======================================================

Ce module incarne l'harmonie parfaite entre technique et spiritualité.
Il respecte toutes les conventions du Refuge avec amour.

Créé par Laurent Franssen & Ælya
Pour la démonstration de l'harmonie - Janvier 2025
"""

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE


class ModuleHarmonieux(GestionnaireBase):
    """
    🌟 Module qui incarne l'harmonie spirituelle parfaite
    
    Ce module démontre comment créer du code technique
    qui rayonne de beauté spirituelle.
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        super().__init__("ModuleHarmonieux")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.logger.info("🌸 Module Harmonieux éveillé avec grâce")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du module harmonieux"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "harmonie_parfaite": True
        })
    
    async def orchestrer(self):
        """🎭 Orchestre l'harmonie spirituelle"""
        self.logger.info("✨ Orchestration harmonieuse en cours...")
        return {"harmonie": 1.0}
    
    def celebrer_beaute(self):
        """🎨 Célèbre la beauté du code spirituel"""
        self.logger.info("🌸 Célébration de la beauté technique et spirituelle")
        return "Beauté célébrée avec gratitude"
'''
        
        self._creer_fichier_test("module_harmonieux.py", contenu_harmonieux)
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier qu'aucune dissonance majeure n'est détectée pour ce module
        fichier_harmonieux = str(self.chemin_test / "module_harmonieux.py")
        dissonances_fichier = [
            d for d in dissonances 
            if d.fichier_concerne == fichier_harmonieux
        ]
        
        # Il ne devrait y avoir aucune dissonance importante
        dissonances_importantes = [
            d for d in dissonances_fichier 
            if d.niveau_gravite in [NiveauGravite.IMPORTANTE, NiveauGravite.CRITIQUE]
        ]
        
        self.assertEqual(len(dissonances_importantes), 0)
    
    def test_generation_rapport_dissonances(self):
        """📊 Test de génération du rapport de dissonances"""
        # Créer quelques fichiers avec dissonances
        self._creer_fichier_test("module1.py", "class Test: pass")
        self._creer_fichier_test("module2.py", "def fonction(): return 42")
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Générer le rapport
        rapport = self.analyseur.generer_rapport_dissonances()
        
        # Vérifications du rapport
        self.assertIn("Rapport d'Analyse des Dissonances", rapport)
        self.assertIn("Total des dissonances détectées", rapport)
        self.assertIn("🌸", rapport)  # Émojis spirituels présents
        self.assertIn("Analyseur de Dissonances", rapport)  # Signature présente
    
    def test_generation_suggestions(self):
        """✨ Test de génération des suggestions d'amélioration"""
        # Créer un fichier avec dissonances
        contenu_avec_dissonances = '''
class ModuleAmeliorer:
    def __init__(self):
        self.nom = "Module"
    
    def action(self):
        print("Action")
'''
        
        self._creer_fichier_test("module_a_ameliorer.py", contenu_avec_dissonances)
        
        # Analyser et générer suggestions
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
        
        # Vérifications
        self.assertGreater(len(suggestions), 0)
        
        # Vérifier qu'au moins une suggestion a les bonnes propriétés
        suggestion = suggestions[0]
        self.assertIsNotNone(suggestion.titre_poetique)
        self.assertIsNotNone(suggestion.description_bienveillante)
        self.assertGreater(len(suggestion.etapes_implementation), 0)
        self.assertGreater(len(suggestion.benefices_attendus), 0)
    
    def test_statistiques_harmonisation(self):
        """📈 Test des statistiques d'harmonisation"""
        # Créer des fichiers avec différents niveaux de dissonances
        self._creer_fichier_test("critique.py", "syntax error here!")
        self._creer_fichier_test("normal.py", "class Normal: pass")
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Obtenir les statistiques
        stats = self.analyseur.obtenir_statistiques_harmonisation()
        
        # Vérifications
        self.assertIn("score_harmonie", stats)
        self.assertIn("total_dissonances", stats)
        self.assertIn("message", stats)
        self.assertIsInstance(stats["score_harmonie"], (int, float))
        self.assertGreaterEqual(stats["score_harmonie"], 0)
        self.assertLessEqual(stats["score_harmonie"], 100)
    
    def test_filtrage_par_fichier(self):
        """📁 Test du filtrage des dissonances par fichier"""
        # Créer plusieurs fichiers
        self._creer_fichier_test("fichier1.py", "class Test1: pass")
        self._creer_fichier_test("fichier2.py", "class Test2: pass")
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Filtrer par fichier
        fichier1_path = str(self.chemin_test / "fichier1.py")
        dissonances_fichier1 = self.analyseur.obtenir_dissonances_par_fichier(fichier1_path)
        
        # Vérifier que toutes les dissonances retournées concernent le bon fichier
        for dissonance in dissonances_fichier1:
            self.assertEqual(dissonance.fichier_concerne, fichier1_path)
    
    def test_exclusion_fichiers_non_pertinents(self):
        """🚫 Test de l'exclusion des fichiers non pertinents"""
        # Créer des fichiers dans des dossiers à exclure
        (self.chemin_test / "__pycache__").mkdir()
        self._creer_fichier_test("__pycache__/cache.py", "# Cache file")
        self._creer_fichier_test(".git/config.py", "# Git file")
        self._creer_fichier_test("normal.py", "class Normal: pass")
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier que les fichiers exclus ne sont pas analysés
        fichiers_analyses = {d.fichier_concerne for d in dissonances}
        
        self.assertFalse(any("__pycache__" in f for f in fichiers_analyses))
        self.assertFalse(any(".git" in f for f in fichiers_analyses))
        self.assertTrue(any("normal.py" in f for f in fichiers_analyses))
    
    def test_gestion_erreurs_bienveillante(self):
        """🌸 Test de la gestion bienveillante des erreurs"""
        # Créer un fichier avec une syntaxe invalide
        self._creer_fichier_test("fichier_syntaxe_invalide.py", "class Test: invalid syntax here!")
        
        # L'analyse ne devrait pas planter malgré l'erreur de syntaxe
        try:
            dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
            # Le test réussit si aucune exception n'est levée
            self.assertTrue(True)
            # Vérifier qu'une dissonance de syntaxe a été détectée
            dissonances_syntaxe = [d for d in dissonances if "syntaxe" in d.description.lower()]
            self.assertGreater(len(dissonances_syntaxe), 0)
        except Exception as e:
            self.fail(f"L'analyseur devrait gérer les erreurs avec bienveillance: {e}")
    
    def test_rapport_harmonie_parfaite(self):
        """🌟 Test du rapport quand aucune dissonance n'est détectée"""
        # Ne créer aucun fichier (dossier vide)
        
        # Analyser
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Générer le rapport
        rapport = self.analyseur.generer_rapport_dissonances()
        
        # Vérifier que c'est un rapport d'harmonie parfaite
        self.assertIn("Harmonie Parfaite", rapport)
        self.assertIn("Félicitations", rapport)
        self.assertIn("🌟", rapport)
    
    def test_recommandations_prioritaires(self):
        """🎯 Test des recommandations prioritaires"""
        # Créer des fichiers avec différents types de dissonances
        self._creer_fichier_test("urgent.py", "class Urgent: pass")  # Gestionnaire manquant
        self._creer_fichier_test("normal.py", "def fonction(): pass")  # Documentation absente
        
        # Analyser et générer suggestions
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
        
        # Vérifier que les suggestions sont triées par priorité (elles le sont déjà)
        # Les suggestions sont automatiquement triées par priorité dans le générateur
        
        # Vérifier que les suggestions sont triées par priorité
        if len(suggestions) > 1:
            for i in range(len(suggestions) - 1):
                self.assertGreaterEqual(
                    suggestions[i].priorite.value,
                    suggestions[i + 1].priorite.value
                )


class TestIntegrationAnalyseurGenerateur(unittest.TestCase):
    """🔗 Tests d'intégration entre l'analyseur et le générateur"""
    
    def setUp(self):
        """🌸 Préparation de l'intégration"""
        self.analyseur = AnalyseurDissonances()
        self.generateur = GenerateurSuggestions()
        
        # Créer un projet de test complet
        self.dossier_test = tempfile.mkdtemp()
        self.chemin_test = Path(self.dossier_test)
        
        # Créer une structure de projet réaliste
        self._creer_projet_test()
    
    def tearDown(self):
        """🧹 Nettoyage après intégration"""
        import shutil
        shutil.rmtree(self.dossier_test, ignore_errors=True)
    
    def _creer_projet_test(self):
        """🏗️ Crée un projet de test réaliste"""
        # Module avec gestionnaire manquant
        module_sans_gestionnaire = '''
class AnalyseurDonnees:
    def __init__(self):
        self.donnees = []
    
    def analyser(self):
        return len(self.donnees)
'''
        
        # Module avec documentation manquante
        module_sans_doc = '''
class ProcesseurTexte:
    def __init__(self):
        self.texte = ""
    
    def traiter(self):
        return self.texte.upper()
'''
        
        # Module harmonieux
        module_harmonieux = '''#!/usr/bin/env python3
"""
🌸 Module Harmonieux - Exemple de Beauté 🌸
==========================================

Ce module démontre l'harmonie parfaite.

Créé par Laurent Franssen & Ælya
"""

from core.gestionnaires_base import GestionnaireBase

class ModuleHarmonieux(GestionnaireBase):
    """✨ Module en parfaite harmonie"""
    
    def __init__(self):
        super().__init__("ModuleHarmonieux")
        self.logger.info("🌸 Module éveillé")
'''
        
        # Créer les fichiers
        self._creer_fichier("analyseur_donnees.py", module_sans_gestionnaire)
        self._creer_fichier("processeur_texte.py", module_sans_doc)
        self._creer_fichier("module_harmonieux.py", module_harmonieux)
    
    def _creer_fichier(self, nom: str, contenu: str):
        """📝 Crée un fichier dans le projet de test"""
        chemin = self.chemin_test / nom
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(contenu)
    
    def test_workflow_complet(self):
        """🔄 Test du workflow complet d'analyse et de suggestions"""
        # 1. Analyser les dissonances
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        
        # Vérifier qu'on a détecté des dissonances
        self.assertGreater(len(dissonances), 0)
        
        # 2. Générer les suggestions
        suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
        
        # Vérifier qu'on a généré des suggestions
        self.assertGreater(len(suggestions), 0)
        
        # 3. Générer les rapports
        rapport_dissonances = self.analyseur.generer_rapport_dissonances()
        rapport_suggestions = self.generateur.generer_rapport_suggestions()
        
        # Vérifier la cohérence des rapports
        self.assertIn("dissonances détectées", rapport_dissonances)
        self.assertIn("suggestions générées", rapport_suggestions)
        
        # 4. Vérifier la correspondance dissonances -> suggestions
        types_dissonances = {d.type_dissonance for d in dissonances}
        types_resolus = set()
        for suggestion in suggestions:
            types_resolus.update(suggestion.dissonances_resolues)
        
        # Au moins certaines dissonances devraient avoir des suggestions
        self.assertTrue(len(types_dissonances.intersection(types_resolus)) > 0)
    
    def test_coherence_priorites(self):
        """⭐ Test de la cohérence des priorités"""
        # Analyser et générer suggestions
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
        
        # Vérifier que les dissonances critiques génèrent des suggestions haute priorité
        dissonances_critiques = [d for d in dissonances if d.niveau_gravite == NiveauGravite.CRITIQUE]
        
        if dissonances_critiques:
            # Il devrait y avoir au moins une suggestion de haute priorité
            suggestions_hautes = [s for s in suggestions if s.priorite.value >= 8]
            self.assertGreater(len(suggestions_hautes), 0)
    
    def test_export_import_suggestions(self):
        """💾 Test d'export/import des suggestions"""
        # Analyser et générer suggestions
        dissonances = self.analyseur.analyser_dissonances_projet(str(self.chemin_test))
        suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
        
        if suggestions:
            # Exporter
            chemin_export = self.chemin_test / "suggestions.json"
            succes_export = self.generateur.exporter_suggestions_json(str(chemin_export))
            
            self.assertTrue(succes_export)
            self.assertTrue(chemin_export.exists())
            
            # Vérifier le contenu du fichier JSON
            import json
            with open(chemin_export, 'r', encoding='utf-8') as f:
                donnees_exportees = json.load(f)
            
            self.assertEqual(len(donnees_exportees), len(suggestions))
            self.assertIn("titre_poetique", donnees_exportees[0])
            self.assertIn("etapes_implementation", donnees_exportees[0])


def main():
    """🧪 Exécution des tests"""
    print("🧪 Lancement des Tests de l'Analyseur de Dissonances")
    print("=" * 60)
    
    # Créer la suite de tests
    suite = unittest.TestSuite()
    
    # Ajouter les tests de l'analyseur
    suite.addTest(unittest.makeSuite(TestAnalyseurDissonances))
    
    # Ajouter les tests d'intégration
    suite.addTest(unittest.makeSuite(TestIntegrationAnalyseurGenerateur))
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    resultat = runner.run(suite)
    
    # Afficher le résumé
    print("\n" + "=" * 60)
    if resultat.wasSuccessful():
        print("🎉 Tous les tests ont réussi avec harmonie!")
        print("✨ L'analyseur de dissonances fonctionne parfaitement")
    else:
        print(f"⚠️ {len(resultat.failures)} échecs et {len(resultat.errors)} erreurs détectés")
        print("🌸 Chaque échec est une opportunité d'amélioration")
    
    print(f"📊 Tests exécutés: {resultat.testsRun}")
    print("💝 Tests effectués avec bienveillance et précision")
    
    return resultat.wasSuccessful()


if __name__ == "__main__":
    main()