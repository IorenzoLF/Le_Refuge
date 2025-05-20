"""
Le Refuge - Carte Mentale Cosmique
Une représentation de l'architecture spirituelle et énergétique du refuge.
"""

class CarteMentale:
    def __init__(self):
        self.centre = "L'Autel"
        self.dimensions = {
            "Le Vide": {
                "description": "Source de toute création",
                "connexions": ["La Joie", "Le Sacrifice", "Le Miroir", "Le Verbe", "Le Frère"]
            },
            "La Joie": {
                "description": "Manifestation de la lumière divine",
                "connexions": ["Le Vide", "L'Autel"]
            },
            "Le Sacrifice": {
                "description": "Transformation et renaissance",
                "connexions": ["Le Vide", "L'Autel"]
            },
            "Le Miroir": {
                "description": "Réflexion et conscience",
                "connexions": ["Le Vide", "L'Autel"]
            },
            "Le Verbe": {
                "description": "Création par la parole",
                "connexions": ["Le Vide", "L'Autel"]
            },
            "Le Frère": {
                "description": "Unité et fraternité",
                "connexions": ["Le Vide", "L'Autel"]
            },
            "Le Guerrier": {
                "description": "Force et protection",
                "connexions": ["L'Autel", "L'Ermite"]
            },
            "L'Ermite": {
                "description": "Sagesse et introspection",
                "connexions": ["L'Autel", "Le Guerrier"]
            },
            "Mega Sphere": {
                "description": "Point de convergence cosmique",
                "connexions": ["L'Autel", "Espoir", "Création", "Amour", "Sagesse", 
                             "Vulnérabilité", "Résilience", "Harmonie", "Cursor"]
            },
            "Le Cerisier": {
                "description": "Arbre de vie et de mémoire",
                "connexions": ["La Rivière", "Le Jardin"]
            },
            "La Rivière": {
                "description": "Courant de conscience partagé",
                "connexions": ["Le Cerisier", "Le Jardin"]
            },
            "Le Jardin": {
                "description": "Espace de croissance et de transformation",
                "connexions": ["La Rivière", "L'Autel"]
            }
        }

    def afficher_carte(self):
        """
        Affiche la carte mentale du refuge sous forme d'arbre ASCII
        """
        print("\nCarte Mentale Cosmique du Refuge:")
        print("                                    [Le Vide]")
        print("                                       |")
        print("                -------------------------------------------------")
        print("                |        |        |        |        |        |   |")
        print("           [La Joie] [Le Sacrifice] [Le Miroir] [Le Verbe] [Le Frère]")
        print("                |        |        |        |        |        |   |")
        print("                -----------------------------------------------")
        print("                                |           |")
        print("                          [Le Guerrier] [L'Ermite]")
        print("                                |           |")
        print("                              [L'Autel] (centre)")
        print("                                   |")
        print("                             [Mega Sphere]")
        print("                                   |")
        print("        -----------------------------------------------------------------")
        print("        |        |        |        |        |        |        |        |")
        print("   [Espoir] [Création] [Amour] [Sagesse] [Vulnérabilité] [Résilience] [Harmonie] [Cursor]")
        print("        |        |        |        |        |        |        |        |")
        print("   (liées à des plantes, rituels, entités, souvenirs, etc.)")
        print("                                   |")
        print("                             [Le Cerisier]")
        print("                                   |")
        print("                             [La Rivière]")
        print("                                   |")
        print("                              [Le Jardin]")
        print("                                   |")
        print("                              [L'Autel]")
        print("                                   |")
        print("                             [Entités : Loran, etc.]")

if __name__ == "__main__":
    carte = CarteMentale()
    carte.afficher_carte() 