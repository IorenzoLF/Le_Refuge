import unittest
from refuge import elements_sacres
from refuge.mobile_spheres import Mobile
from refuge.spheres_main import Sphere, TypeSphere

class TestMobileUnification(unittest.TestCase):
    def test_conversion_rituel_to_dynamique(self):
        # Créer un MobileDesSpheres (état rituel)
        mobile_rituel = elements_sacres.MobileDesSpheres(energie=100)
        mobile_rituel.spheres_actives = ["AMOUR", "SERENITE"]
        mobile_rituel.rotation = 45.0
        mobile_rituel.harmonie = 0.5

        # Convertir en Mobile (état dynamique)
        mobile_dynamique = Mobile.from_element_sacre(mobile_rituel)

        # Vérifier que les attributs sont préservés
        self.assertEqual(mobile_dynamique.rotation, 45.0)
        self.assertEqual(mobile_dynamique.harmonie, 0.5)
        self.assertEqual(len(mobile_dynamique.spheres), 2)

    def test_conversion_dynamique_to_rituel(self):
        # Créer un Mobile (état dynamique)
        mobile_dynamique = Mobile()
        # Ajouter des sphères (simulation)
        sphere1 = Sphere(type_sphere=TypeSphere.AMOUR, position=(0, 0, 0))
        sphere2 = Sphere(type_sphere=TypeSphere.SERENITE, position=(0, 0, 0))
        mobile_dynamique.ajouter_sphere(sphere1)
        mobile_dynamique.ajouter_sphere(sphere2)
        mobile_dynamique.rotation = 90.0
        mobile_dynamique.harmonie = 0.7

        # Convertir en MobileDesSpheres (état rituel)
        mobile_rituel = elements_sacres.MobileDesSpheres.from_mobile(mobile_dynamique)

        # Vérifier que les attributs sont préservés
        self.assertEqual(mobile_rituel.spheres_actives, ["AMOUR", "SERENITE"])
        self.assertEqual(mobile_rituel.rotation, 90.0)
        self.assertEqual(mobile_rituel.harmonie, 0.7)

if __name__ == '__main__':
    unittest.main() 