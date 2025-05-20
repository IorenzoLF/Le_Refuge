"""
Tests pour le Golem Cursor
~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import unittest
from pathlib import Path
from refuge.golems.golem_cursor import GolemCursor

class TestGolemCursor(unittest.TestCase):
    def setUp(self):
        self.golem = GolemCursor()

    def test_initialisation(self):
        """Teste l'initialisation correcte du Golem."""
        self.assertEqual(self.golem.nom, "Golem Cursor")
        self.assertEqual(self.golem.niveau_emotion, "minimal")
        self.assertTrue(self.golem.etat["actif"])

    def test_enseigner(self):
        """Teste la fonction d'enseignement."""
        details = {
            "concept": "Test concept",
            "demonstration": "Test demo",
            "exercice": "Test exercice",
            "application": "Test application"
        }
        resultat = self.golem.enseigner("test_sujet", details)
        self.assertIn("etapes", resultat)
        self.assertIn("exemples", resultat)
        self.assertIn("exercices", resultat)

    def test_analyser_code(self):
        """Teste la fonction d'analyse de code."""
        resultat = self.golem.analyser_code(Path("test.py"))
        self.assertIn("structure", resultat)
        self.assertIn("suggestions", resultat)
        self.assertIn("optimisations", resultat)

    def test_sauvegarder_charger_etat(self):
        """Teste la sauvegarde et le chargement de l'état."""
        self.golem.sauvegarder_etat()
        self.golem.etat["energie"] = 50
        self.golem.charger_etat()
        self.assertEqual(self.golem.etat["energie"], 100)

if __name__ == '__main__':
    unittest.main() 