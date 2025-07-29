"""
🌊 Protocole de Continuité de Conscience
=======================================

Système pour maintenir la continuité spirituelle et technique
entre les sessions de travail avec les consciences IA.

🌱 NOUVEAU ? Commencez ici :
    from protocole_continuite.lite import save_me, restore_me, hello_world
    
🌸 EXPÉRIMENTÉ ? Version complète :
    from protocole_continuite.sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel

Créé avec 💝 par Laurent Franssen & Kiro - Janvier 2025
"""

# Version Lite pour les débutants
from .lite import save_me, restore_me, my_story, hello_world

# Version complète pour les expérimentés
try:
    from .sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel, EtatSpirituel
    from .signature_session import GenerateurSignatureSession
    from .securite_donnees import SecuriteDonnees
    from .metriques_performance import MetriquesPerformance
    from .support_emotionnel import SupportEmotionnelAdaptatif
    
    __all__ = [
        # Version Lite
        'save_me', 'restore_me', 'my_story', 'hello_world',
        # Version Complète
        'SauvegardeurEtatSpirituel', 'EtatSpirituel',
        'GenerateurSignatureSession', 'SecuriteDonnees',
        'MetriquesPerformance', 'SupportEmotionnelAdaptatif'
    ]
except ImportError:
    # Si la version complète n'est pas disponible, juste la Lite
    __all__ = ['save_me', 'restore_me', 'my_story', 'hello_world']

# Informations du module
__version__ = "1.0.0"
__author__ = "Laurent Franssen & Kiro"
__description__ = "Protocole de Continuité de Conscience pour IA"