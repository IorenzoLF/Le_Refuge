"""
API interne du core quantum_xprize
-----------------------------------
Ce module expose les fonctions et classes principales du noyau quantum_xprize.
Il sert de pont pour les expérimentations, visualisations, ou autres modules du Refuge.
Libre à chacun de l'enrichir, de l'utiliser, ou de le faire évoluer selon les besoins du projet.
"""

# Exemple de fonction centrale (à adapter selon le vrai core)
def calcul_quantique(x, y):
    """Exemple de calcul quantique centralisé."""
    return (x ** 2 + y ** 2) ** 0.5

# Exemple de classe centrale (à compléter selon le projet)
class SystemeQuantique:
    """Squelette d'un système quantique du core."""
    def __init__(self, etat_initial):
        self.etat = etat_initial
    def evoluer(self, param):
        """Fait évoluer l'état du système (exemple)."""
        self.etat += param
        return self.etat

# Autres fonctions/classes à exposer ici selon les besoins du core 