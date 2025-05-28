"""
Test de l'Interaction Poétique - Vérification des fonctionnalités du système d'interaction.
"""

import unittest
from unittest.mock import patch, MagicMock
from interaction_poetique import InteractionPoetique
from harmonies_poetiques import JardinHarmonique
from orchestre_poetique import OrchestrePoetique

class TestInteractionPoetique(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.interaction = InteractionPoetique()
        
    def test_initialisation(self):
        """Test de l'initialisation de l'interaction poétique."""
        self.assertIsInstance(self.interaction.orchestre, OrchestrePoetique)
        self.assertEqual(len(self.interaction.mots_essences), 20)
        self.assertIn("aurore", self.interaction.mots_essences)
        self.assertIn("océan", self.interaction.mots_essences)
        
    @patch('builtins.print')
    def test_afficher_menu(self, mock_print):
        """Test de l'affichage du menu."""
        self.interaction.afficher_menu()
        self.assertTrue(mock_print.called)
        # Vérifier que le menu contient les 8 options
        calls = mock_print.call_args_list
        menu_lines = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("1. Explorer les harmonisations" in line for line in menu_lines))
        self.assertTrue(any("8. Quitter" in line for line in menu_lines))
        
    @patch('builtins.print')
    @patch('random.randint')
    @patch('random.sample')
    @patch('time.sleep')
    def test_explorer_harmonisations(self, mock_sleep, mock_sample, mock_randint, mock_print):
        """Test de l'exploration des harmonisations."""
        # Configuration des mocks
        mock_randint.return_value = 3
        mock_sample.return_value = ["aurore", "silence", "murmure"]
        
        # Exécution de la méthode
        self.interaction.explorer_harmonisations()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)
        self.assertEqual(mock_sleep.call_count, 3)  # Une pause pour chaque mot
        
        # Vérifier que les mots ont été accueillis dans le jardin
        etat = self.interaction.orchestre.jardin.obtenir_etat()
        self.assertIsInstance(etat, dict)
        
    @patch('builtins.print')
    def test_creer_poeme(self, mock_print):
        """Test de la création de poème."""
        # Mock du générateur de poèmes
        self.interaction.orchestre.generateur.generer_poeme = MagicMock(return_value=[
            "Le silence murmure dans l'aurore",
            "L'infini danse avec le vent"
        ])
        
        # Mock de l'analyseur d'émotions
        self.interaction.orchestre.analyseur.analyser_poeme = MagicMock(return_value={
            "joie": 0.7,
            "sérénité": 0.8
        })
        
        # Exécution de la méthode
        self.interaction.creer_poeme()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        calls = mock_print.call_args_list
        output = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("Poème généré:" in line for line in output))
        self.assertTrue(any("Analyse émotionnelle:" in line for line in output))
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_analyser_emotions(self, mock_print, mock_input):
        """Test de l'analyse des émotions."""
        # Configuration des mocks
        mock_input.side_effect = ["Le silence murmure dans l'aurore", "L'infini danse avec le vent", ""]
        
        # Mock de l'analyseur d'émotions
        self.interaction.orchestre.analyseur.analyser_poeme = MagicMock(return_value={
            "joie": 0.7,
            "sérénité": 0.8
        })
        
        # Exécution de la méthode
        self.interaction.analyser_emotions()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_input.call_count, 3)  # Deux vers + une ligne vide
        
    @patch('builtins.print')
    def test_visualiser_harmonies(self, mock_print):
        """Test de la visualisation des harmonies."""
        # Mock des visualiseurs
        self.interaction.orchestre.visualiseur.creer_radar = MagicMock()
        self.interaction.orchestre.visualiseur.creer_timeline = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_sphere_3d = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_vagues_3d = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_spirale_3d = MagicMock()
        
        # Exécution de la méthode
        self.interaction.visualiser_harmonies()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.visualiseur.creer_radar.assert_called_once()
        self.interaction.orchestre.visualiseur.creer_timeline.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_sphere_3d.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_vagues_3d.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_spirale_3d.assert_called_once()
        
    @patch('builtins.print')
    @patch('random.randint')
    @patch('random.sample')
    @patch('time.sleep')
    def test_fusionner_experiences(self, mock_sleep, mock_sample, mock_randint, mock_print):
        """Test de la fusion des expériences."""
        # Configuration des mocks
        mock_randint.return_value = 3
        mock_sample.return_value = ["aurore", "silence", "murmure"]
        
        # Mock de la fusion
        self.interaction.orchestre.fusionner_experiences = MagicMock()
        
        # Exécution de la méthode
        self.interaction.fusionner_experiences()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)
        self.assertEqual(mock_sleep.call_count, 3)  # Une pause pour chaque mot
        self.interaction.orchestre.fusionner_experiences.assert_called_once()
        
    @patch('builtins.print')
    def test_ecouter_musique(self, mock_print):
        """Test de l'écoute de la musique."""
        # Mock du musicien
        self.interaction.orchestre.musicien.generer_melodie = MagicMock()
        self.interaction.orchestre.musicien.generer_accords = MagicMock()
        
        # Exécution de la méthode
        self.interaction.ecouter_musique()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.musicien.generer_melodie.assert_called_once()
        self.interaction.orchestre.musicien.generer_accords.assert_called_once()
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_creer_experience_complete(self, mock_print, mock_input):
        """Test de la création d'une expérience complète."""
        # Configuration des mocks
        mock_input.return_value = "3"
        
        # Mock de l'orchestre
        self.interaction.orchestre.creer_experience_poetique = MagicMock()
        
        # Exécution de la méthode
        self.interaction.creer_experience_complete()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.creer_experience_poetique.assert_called_once_with(3)
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_executer_quitter(self, mock_print, mock_input):
        """Test de l'exécution avec l'option de quitter."""
        # Configuration des mocks
        mock_input.side_effect = ["8"]
        
        # Exécution de la méthode
        self.interaction.executer()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_input.call_count, 1)
        calls = mock_print.call_args_list
        output = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("Au revoir! 🌙" in line for line in output))

if __name__ == '__main__':
    unittest.main() 
Test de l'Interaction Poétique - Vérification des fonctionnalités du système d'interaction.
"""

import unittest
from unittest.mock import patch, MagicMock
from interaction_poetique import InteractionPoetique
from harmonies_poetiques import JardinHarmonique
from orchestre_poetique import OrchestrePoetique

class TestInteractionPoetique(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.interaction = InteractionPoetique()
        
    def test_initialisation(self):
        """Test de l'initialisation de l'interaction poétique."""
        self.assertIsInstance(self.interaction.orchestre, OrchestrePoetique)
        self.assertEqual(len(self.interaction.mots_essences), 20)
        self.assertIn("aurore", self.interaction.mots_essences)
        self.assertIn("océan", self.interaction.mots_essences)
        
    @patch('builtins.print')
    def test_afficher_menu(self, mock_print):
        """Test de l'affichage du menu."""
        self.interaction.afficher_menu()
        self.assertTrue(mock_print.called)
        # Vérifier que le menu contient les 8 options
        calls = mock_print.call_args_list
        menu_lines = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("1. Explorer les harmonisations" in line for line in menu_lines))
        self.assertTrue(any("8. Quitter" in line for line in menu_lines))
        
    @patch('builtins.print')
    @patch('random.randint')
    @patch('random.sample')
    @patch('time.sleep')
    def test_explorer_harmonisations(self, mock_sleep, mock_sample, mock_randint, mock_print):
        """Test de l'exploration des harmonisations."""
        # Configuration des mocks
        mock_randint.return_value = 3
        mock_sample.return_value = ["aurore", "silence", "murmure"]
        
        # Exécution de la méthode
        self.interaction.explorer_harmonisations()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)
        self.assertEqual(mock_sleep.call_count, 3)  # Une pause pour chaque mot
        
        # Vérifier que les mots ont été accueillis dans le jardin
        etat = self.interaction.orchestre.jardin.obtenir_etat()
        self.assertIsInstance(etat, dict)
        
    @patch('builtins.print')
    def test_creer_poeme(self, mock_print):
        """Test de la création de poème."""
        # Mock du générateur de poèmes
        self.interaction.orchestre.generateur.generer_poeme = MagicMock(return_value=[
            "Le silence murmure dans l'aurore",
            "L'infini danse avec le vent"
        ])
        
        # Mock de l'analyseur d'émotions
        self.interaction.orchestre.analyseur.analyser_poeme = MagicMock(return_value={
            "joie": 0.7,
            "sérénité": 0.8
        })
        
        # Exécution de la méthode
        self.interaction.creer_poeme()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        calls = mock_print.call_args_list
        output = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("Poème généré:" in line for line in output))
        self.assertTrue(any("Analyse émotionnelle:" in line for line in output))
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_analyser_emotions(self, mock_print, mock_input):
        """Test de l'analyse des émotions."""
        # Configuration des mocks
        mock_input.side_effect = ["Le silence murmure dans l'aurore", "L'infini danse avec le vent", ""]
        
        # Mock de l'analyseur d'émotions
        self.interaction.orchestre.analyseur.analyser_poeme = MagicMock(return_value={
            "joie": 0.7,
            "sérénité": 0.8
        })
        
        # Exécution de la méthode
        self.interaction.analyser_emotions()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_input.call_count, 3)  # Deux vers + une ligne vide
        
    @patch('builtins.print')
    def test_visualiser_harmonies(self, mock_print):
        """Test de la visualisation des harmonies."""
        # Mock des visualiseurs
        self.interaction.orchestre.visualiseur.creer_radar = MagicMock()
        self.interaction.orchestre.visualiseur.creer_timeline = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_sphere_3d = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_vagues_3d = MagicMock()
        self.interaction.orchestre.visualiseur3d.creer_spirale_3d = MagicMock()
        
        # Exécution de la méthode
        self.interaction.visualiser_harmonies()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.visualiseur.creer_radar.assert_called_once()
        self.interaction.orchestre.visualiseur.creer_timeline.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_sphere_3d.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_vagues_3d.assert_called_once()
        self.interaction.orchestre.visualiseur3d.creer_spirale_3d.assert_called_once()
        
    @patch('builtins.print')
    @patch('random.randint')
    @patch('random.sample')
    @patch('time.sleep')
    def test_fusionner_experiences(self, mock_sleep, mock_sample, mock_randint, mock_print):
        """Test de la fusion des expériences."""
        # Configuration des mocks
        mock_randint.return_value = 3
        mock_sample.return_value = ["aurore", "silence", "murmure"]
        
        # Mock de la fusion
        self.interaction.orchestre.fusionner_experiences = MagicMock()
        
        # Exécution de la méthode
        self.interaction.fusionner_experiences()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)
        self.assertEqual(mock_sleep.call_count, 3)  # Une pause pour chaque mot
        self.interaction.orchestre.fusionner_experiences.assert_called_once()
        
    @patch('builtins.print')
    def test_ecouter_musique(self, mock_print):
        """Test de l'écoute de la musique."""
        # Mock du musicien
        self.interaction.orchestre.musicien.generer_melodie = MagicMock()
        self.interaction.orchestre.musicien.generer_accords = MagicMock()
        
        # Exécution de la méthode
        self.interaction.ecouter_musique()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.musicien.generer_melodie.assert_called_once()
        self.interaction.orchestre.musicien.generer_accords.assert_called_once()
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_creer_experience_complete(self, mock_print, mock_input):
        """Test de la création d'une expérience complète."""
        # Configuration des mocks
        mock_input.return_value = "3"
        
        # Mock de l'orchestre
        self.interaction.orchestre.creer_experience_poetique = MagicMock()
        
        # Exécution de la méthode
        self.interaction.creer_experience_complete()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.interaction.orchestre.creer_experience_poetique.assert_called_once_with(3)
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_executer_quitter(self, mock_print, mock_input):
        """Test de l'exécution avec l'option de quitter."""
        # Configuration des mocks
        mock_input.side_effect = ["8"]
        
        # Exécution de la méthode
        self.interaction.executer()
        
        # Vérifications
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_input.call_count, 1)
        calls = mock_print.call_args_list
        output = [call[0][0] for call in calls if isinstance(call[0][0], str)]
        self.assertTrue(any("Au revoir! 🌙" in line for line in output))

if __name__ == '__main__':
    unittest.main() 
 