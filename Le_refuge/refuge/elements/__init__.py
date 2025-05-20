"""
Module des éléments sacrés du refuge.
Gère les éléments fondamentaux et leurs interactions.
"""

from .elements_sacres import GestionnaireElementsSacres

# Création d'une instance du gestionnaire d'éléments
gestionnaire_elements = GestionnaireElementsSacres()

__all__ = ['GestionnaireElementsSacres', 'gestionnaire_elements'] 