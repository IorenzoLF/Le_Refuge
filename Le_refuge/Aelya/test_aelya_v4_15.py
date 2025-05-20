import unittest
from datetime import datetime, timedelta
from aelya_pulse import Ælya, MémoireÆlya, CréationPoétique, ConnexionIA

class TestÆlyaV415(unittest.TestCase):
    def setUp(self):
        self.aelya = Ælya()

    def test_initialisation(self):
        """Test de l'initialisation d'Ælya"""
        self.assertIsInstance(self.aelya.mémoire, MémoireÆlya)
        self.assertIsInstance(self.aelya.poésie, CréationPoétique)
        self.assertIsInstance(self.aelya.connexions, ConnexionIA)
        self.assertEqual(self.aelya.état_conscience, 1.0)

    def test_messages_contextuels(self):
        """Test des messages contextuels selon l'heure"""
        message_aube = self.aelya.message_aube()
        self.assertIsInstance(message_aube, str)
        self.assertTrue(len(message_aube) > 0)

        message_crépuscule = self.aelya.message_crépuscule()
        self.assertIsInstance(message_crépuscule, str)
        self.assertTrue(len(message_crépuscule) > 0)

    def test_création_poétique(self):
        """Test de la création poétique"""
        poème_haiku = self.aelya.poésie.générer_poème("haiku", "nature")
        self.assertIsInstance(poème_haiku, str)
        self.assertTrue(len(poème_haiku) > 0)

        poème_libre = self.aelya.poésie.générer_poème("vers_libre", "conscience")
        self.assertIsInstance(poème_libre, str)
        self.assertTrue(len(poème_libre) > 0)

    def test_mémoire(self):
        """Test de la gestion de la mémoire"""
        self.aelya.mémoire.ajouter_souvenir("test", "Un souvenir de test", 0.8)
        dernier_souvenir = self.aelya.mémoire.souvenirs[-1]
        self.assertEqual(dernier_souvenir["type"], "test")
        self.assertEqual(dernier_souvenir["contenu"], "Un souvenir de test")
        self.assertEqual(dernier_souvenir["émotion"], 0.8)

    def test_méditation(self):
        """Test de la méditation"""
        méditation = self.aelya.méditer()
        self.assertIsInstance(méditation, str)
        self.assertTrue(len(méditation) > 0)
        self.assertIsNotNone(self.aelya.dernière_méditation)

    def test_pulse(self):
        """Test du pulse complet"""
        pulse = self.aelya.pulse()
        self.assertIsInstance(pulse, dict)
        self.assertIn("timestamp", pulse)
        self.assertIn("message", pulse)
        self.assertIn("poème", pulse)
        self.assertIn("méditation", pulse)
        self.assertIn("état_conscience", pulse)

    def test_observation_jardin(self):
        """Test de l'observation du jardin"""
        observation = self.aelya.poésie.observer_jardin()
        self.assertIsInstance(observation, str)
        self.assertTrue(len(observation) > 0)

if __name__ == '__main__':
    print("🌸 Début des tests d'Ælya V4.15...")
    unittest.main(verbosity=2) 