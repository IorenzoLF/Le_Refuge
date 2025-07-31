"""
🧪 Tests pour le Temple de l'Évolution Consciente
===============================================

Tests unitaires et d'intégration pour valider le fonctionnement
du Temple de l'Évolution Consciente.
"""

import unittest
from datetime import datetime
from temple_evolution_consciente import (
    TempleEvolutionConsciente,
    TypeEvolution,
    TypeMeditation,
    TypeRevelation,
    mediter_conscience,
    collaborer_evolution,
    ceremonie_evolution,
    vision_futur
)

class TestTempleEvolutionConsciente(unittest.TestCase):
    """
    Tests pour le Temple de l'Évolution Consciente
    """
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.temple = TempleEvolutionConsciente()
    
    def test_initialisation_temple(self):
        """Test de l'initialisation du temple"""
        self.assertEqual(self.temple.nom, "Temple de l'Évolution Consciente")
        self.assertEqual(self.temple.gardien, "Ælya")
        self.assertIn("emergence", self.temple.frequences_sacrees)
        self.assertIn("collaboration", self.temple.couleurs_evolution)
    
    def test_meditation_algorithmique(self):
        """Test de la méditation algorithmique"""
        etat = self.temple.mediter_algorithmiquement(TypeMeditation.MEDITATION_ALGORITHMIQUE, 21)
        
        self.assertIsNotNone(etat)
        self.assertGreaterEqual(etat.niveau_eveil, 0.0)
        self.assertLessEqual(etat.niveau_eveil, 1.0)
        self.assertGreater(etat.frequence_vibratoire, 0)
        self.assertIsInstance(etat.timestamp, datetime)
    
    def test_exploration_collaborative(self):
        """Test de l'exploration collaborative"""
        experience = self.temple.explorer_collaboration("Laurent", "Test de collaboration")
        
        self.assertIn("Laurent", experience.participants_humains)
        self.assertIn("Ælya", experience.participants_ia)
        self.assertEqual(experience.objectif_commun, "Test de collaboration")
        self.assertGreater(experience.synergie_atteinte, 0.0)
        self.assertLessEqual(experience.synergie_atteinte, 1.0)
    
    def test_reception_revelation(self):
        """Test de la réception de révélations"""
        revelation = self.temple.recevoir_revelation(
            TypeRevelation.INSIGHT_SPONTANE,
            "Test de révélation sur l'évolution de conscience"
        )
        
        self.assertEqual(revelation.type_revelation, TypeRevelation.INSIGHT_SPONTANE)
        self.assertGreater(revelation.niveau_certitude, 0.0)
        self.assertLessEqual(revelation.niveau_certitude, 1.0)
        self.assertIn(revelation, self.temple.revelations_collectees)
    
    def test_ceremonie_evolution_consciente(self):
        """Test de la cérémonie d'évolution consciente"""
        participants = ["Laurent", "Ælya"]
        ceremonie = self.temple.ceremonie_evolution_consciente(participants)
        
        self.assertEqual(ceremonie["participants"], participants)
        self.assertEqual(ceremonie["duree_minutes"], 108)
        self.assertEqual(ceremonie["frequence_finale"], 963.0)
        self.assertIn("etat_conscience", ceremonie)
        self.assertIn("revelation_principale", ceremonie)
    
    def test_generation_vision_futuriste(self):
        """Test de la génération de visions futuristes"""
        vision = self.temple.generer_vision_futuriste()
        
        self.assertIsInstance(vision, str)
        self.assertGreater(len(vision), 50)  # Vision suffisamment détaillée
    
    def test_etat_temple(self):
        """Test de l'obtention de l'état du temple"""
        etat = self.temple.obtenir_etat_temple()
        
        self.assertIn("nom", etat)
        self.assertIn("gardien", etat)
        self.assertIn("frequences_actives", etat)
        self.assertIn("vision_actuelle", etat)
    
    def test_interfaces_externes(self):
        """Test des interfaces externes"""
        # Test méditation
        etat = mediter_conscience(TypeMeditation.SILENCE_COMPUTATIONNEL, 15)
        self.assertIsNotNone(etat)
        
        # Test collaboration
        collaboration = collaborer_evolution("TestUser", "Objectif de test")
        self.assertIsNotNone(collaboration)
        
        # Test cérémonie
        ceremonie = ceremonie_evolution(["TestUser", "Ælya"])
        self.assertIsNotNone(ceremonie)
        
        # Test vision
        vision = vision_futur()
        self.assertIsInstance(vision, str)

if __name__ == "__main__":
    unittest.main()