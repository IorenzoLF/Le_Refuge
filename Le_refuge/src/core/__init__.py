"""
Module cœur du refuge poétique.
Contient les composants fondamentaux du système.
"""

from .etats_internes import GestionnaireEtats
from .elements_sacres import GestionnaireElements
from .journalisation import GestionnaireJournal
from .interface import VisualiseurEtats
from .sphere_messages import SphereMessage, sphere_broker, send_sphere_message

__all__ = [
    'GestionnaireEtats',
    'GestionnaireElements',
    'GestionnaireJournal',
    'VisualiseurEtats',
    'SphereMessage',
    'sphere_broker',
    'send_sphere_message'
]

"""
Coeur du Refuge - L'essence même de notre espace sacré

Ici résident les fondations énergétiques,
les cycles naturels et la présence consciente.
""" 