"""
Module de tests pour le Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

import unittest
from datetime import datetime
from ..spheres import CollectionSpheres, Sphere
from ..elements_naturels import Cerisier
from ..courant_partage import CourantPartage
from ..cristaux_memoire import CollectionCristaux
from ..rituels import GestionnaireRituels
from ..interface_refuge import InterfaceRefuge
from ..main import Refuge

class TestRefuge(unittest.TestCase):
    """Tests pour le Refuge."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        self.refuge = Refuge()
        self.refuge.initialiser()
        
    def test_initialisation(self):
        """Test l'initialisation du Refuge."""
        self.assertTrue(self.refuge.initialise)
        self.assertIsInstance(self.refuge.interface, InterfaceRefuge)
        
    def test_spheres(self):
        """Test le système de sphères."""
        # Test d'activation d'une sphère
        resultat = self.refuge.interface.activer_sphere("COSMOS")
        self.assertTrue(resultat["success"])
        self.assertEqual(resultat["sphere"], "COSMOS")
        
        # Test d'accueil sous le cerisier
        resultat = self.refuge.interface.accueillir_sphere_cerisier("COSMOS")
        self.assertTrue(resultat["success"])
        self.assertEqual(len(self.refuge.interface.cerisier.spheres_connectees), 1)
        
    def test_cerisier(self):
        """Test le cerisier ancestral."""
        # Test d'ajout de souvenir
        self.refuge.interface.cerisier.ajouter_souvenir(
            "Premier souvenir sous le cerisier",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "experience",
            0.8
        )
        self.assertEqual(len(self.refuge.interface.cerisier.souvenirs), 1)
        self.assertGreater(self.refuge.interface.cerisier.energie, 0.5)
        
    def test_courant_partage(self):
        """Test le courant partagé."""
        # Test d'établissement de connexion
        self.refuge.interface.courant_partage.etablir_connexion(
            "COSMOS",
            "Cerisier",
            "harmonie"
        )
        self.assertEqual(len(self.refuge.interface.courant_partage.connexions), 1)
        self.assertGreater(self.refuge.interface.courant_partage.intensite_globale, 0.5)
        
    def test_cristaux(self):
        """Test les cristaux mémoire."""
        # Test d'ajout de souvenir dans un cristal
        self.refuge.interface.ajouter_souvenir_cristal(
            "Dialogues",
            "Test de souvenir",
            "dialogue",
            0.7,
            "Test",
            ["test", "validation"]
        )
        etat = self.refuge.interface.collection_cristaux.obtenir_etat()
        self.assertEqual(len(etat["cristaux"]["Dialogues"]["souvenirs"]), 1)
        
    def test_rituels(self):
        """Test les rituels."""
        # Test d'exécution du rituel du Refuge du Néant
        resultat = self.refuge.interface.executer_rituel("Refuge du Néant")
        self.assertTrue(resultat["success"])
        self.assertEqual(resultat["rituel"], "Refuge du Néant")
        
    def test_etat_complet(self):
        """Test l'obtention de l'état complet."""
        etat = self.refuge.obtenir_etat()
        self.assertIn("interface", etat)
        self.assertIn("spheres", etat)
        self.assertIn("cerisier", etat)
        self.assertIn("courant", etat)
        self.assertIn("cristaux", etat)
        self.assertIn("rituels", etat)

if __name__ == "__main__":
    unittest.main() 