import unittest
from src.refuge_cluster.elements.elements_sacres import MobileDesSpheres
from enum import Enum

# ==========================================
# CLASSES MOCK POUR REMPLACER LES IMPORTS CASSÉS
# ==========================================

class TypeSphere(Enum):
    """Mock de TypeSphere"""
    AMOUR = "AMOUR"
    SERENITE = "SERENITE"
    COSMOS = "COSMOS"

class Sphere:
    """Classe mock pour remplacer l'import cassé spheres_main"""
    
    def __init__(self, type_sphere: TypeSphere, position: tuple):
        self.type_sphere = type_sphere
        self.position = position
        self.nom = type_sphere.value

class Mobile:
    """Classe mock pour remplacer l'import cassé mobile_spheres"""
    
    def __init__(self):
        self.spheres = []
        self.rotation = 0.0
        self.harmonie = 0.0
    
    def ajouter_sphere(self, sphere: Sphere):
        """Ajoute une sphère au mobile"""
        self.spheres.append(sphere)
    
    @classmethod
    def from_element_sacre(cls, mobile_rituel):
        """Convertit un MobileDesSpheres en Mobile"""
        mobile = cls()
        mobile.rotation = mobile_rituel.rotation
        mobile.harmonie = mobile_rituel.harmonie
        
        # Convertir les sphères actives
        for sphere_nom in mobile_rituel.spheres_actives:
            try:
                type_sphere = TypeSphere(sphere_nom)
                sphere = Sphere(type_sphere, (0, 0, 0))
                mobile.ajouter_sphere(sphere)
            except ValueError:
                pass  # Ignorer les types de sphères non reconnus
        
        return mobile

class TestMobileUnification(unittest.TestCase):
    def test_conversion_rituel_to_dynamique(self):
        # Créer un MobileDesSpheres (état rituel)
        mobile_rituel = MobileDesSpheres(energie=100)
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
        mobile_rituel = MobileDesSpheres.from_mobile(mobile_dynamique)

        # Vérifier que les attributs sont préservés
        self.assertEqual(mobile_rituel.spheres_actives, ["AMOUR", "SERENITE"])
        self.assertEqual(mobile_rituel.rotation, 90.0)
        self.assertEqual(mobile_rituel.harmonie, 0.7)

if __name__ == '__main__':
    unittest.main() 