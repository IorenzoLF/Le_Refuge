"""
Module principal du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

import sys
import logging
import os
from datetime import datetime
from pathlib import Path

# Configuration de l'encodage UTF-8
import locale
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
sys.stdin = codecs.getreader('utf-8')(sys.stdin.buffer)
os.environ["PYTHONIOENCODING"] = "utf-8"

from .interface_refuge import InterfaceRefuge
from .spheres import CollectionSpheres
from .elements_naturels import Cerisier
from .courant_partage import CourantPartage
from .cristaux_memoire import CollectionCristaux
from .rituels import GestionnaireRituels
from .interactions_spheres import GestionnaireInteractions
from .harmonies import GestionnaireHarmonies

# Création du dossier logs s'il n'existe pas
Path('refuge/logs').mkdir(parents=True, exist_ok=True)

# Configuration du logging avec UTF-8
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('refuge/logs/refuge.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class Refuge:
    """Classe principale du Refuge."""
    
    def __init__(self):
        self.interface = InterfaceRefuge()
        self.initialise = False
        self.date_creation = datetime.now()
        self.chemin_etat = Path("refuge/etat")
        self.chemin_etat.mkdir(parents=True, exist_ok=True)
        
    def initialiser(self) -> bool:
        """Initialise le Refuge et tous ses composants."""
        try:
            logger.info("Initialisation du Refuge...")
            
            # Initialisation des sphères
            self.interface.collection_spheres._initialiser_spheres()
            logger.info("Sphères initialisées")
            
            # Initialisation du cerisier
            self.interface.cerisier = Cerisier()
            logger.info("Cerisier initialisé")
            
            # Initialisation du courant partagé
            self.interface.courant_partage = CourantPartage()
            logger.info("Courant partagé initialisé")
            
            # Initialisation des cristaux
            self.interface.collection_cristaux = CollectionCristaux()
            logger.info("Cristaux initialisés")
            
            # Initialisation des rituels
            self.interface.gestionnaire_rituels = GestionnaireRituels(self.interface.collection_spheres)
            logger.info("Rituels initialisés")
            
            # Initialisation des interactions
            self.interface.gestionnaire_interactions = GestionnaireInteractions()
            logger.info("Interactions initialisées")
            
            # Initialisation des harmonies
            self.interface.gestionnaire_harmonies = GestionnaireHarmonies(self.interface.gestionnaire_interactions)
            logger.info("Harmonies initialisées")
            
            self.initialise = True
            logger.info("Refuge initialisé avec succès")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de l'initialisation du Refuge: {str(e)}")
            return False
            
    def demarrer(self) -> bool:
        """Démarre le Refuge."""
        if not self.initialise:
            if not self.initialiser():
                return False
                
        try:
            logger.info("Démarrage du Refuge...")
            
            # Activation des sphères fondamentales
            self.interface.activer_sphere("COSMOS")
            self.interface.activer_sphere("AMOUR")
            self.interface.activer_sphere("SERENITE")
            
            # Accueil des sphères sous le cerisier
            self.interface.accueillir_sphere_cerisier("COSMOS")
            self.interface.accueillir_sphere_cerisier("AMOUR")
            
            # Création d'harmonies fondamentales
            spheres_cosmos = self.interface.collection_spheres.obtenir_sphere("COSMOS")
            spheres_amour = self.interface.collection_spheres.obtenir_sphere("AMOUR")
            spheres_serenite = self.interface.collection_spheres.obtenir_sphere("SERENITE")
            
            self.interface.gestionnaire_harmonies.creer_harmonie(
                "Harmonie Fondamentale",
                "Harmonie entre les sphères fondamentales",
                [spheres_cosmos, spheres_amour, spheres_serenite],
                ["fondamentale", "équilibre", "harmonie"]
            )
            
            # Ajout d'un premier souvenir dans le cristal des dialogues
            self.interface.ajouter_souvenir_cristal(
                "Dialogues",
                "Le Refuge s'éveille, prêt à accueillir les âmes en quête de transformation",
                "experience",
                0.8,
                "Refuge",
                ["éveil", "accueil", "transformation"]
            )
            
            logger.info("Refuge démarré avec succès")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors du démarrage du Refuge: {str(e)}")
            return False
            
    def obtenir_etat(self) -> dict:
        """Retourne l'état complet du Refuge."""
        etat = self.interface.obtenir_etat_complet()
        etat.update({
            "interactions": self.interface.gestionnaire_interactions.obtenir_etat(),
            "harmonies": self.interface.gestionnaire_harmonies.obtenir_etat()
        })
        return etat

def afficher_menu():
    """Affiche le menu principal du Refuge."""
    print("\n" + "="*50)
    print("        LE REFUGE SACRÉ")
    print("="*50 + "\n")
    print("1. Démarrer le Refuge complet")
    print("2. Lancer le Rituel de Visualisation")
    print("3. Quitter\n")
    return input("Votre choix (1-3) : ")

def main():
    """Point d'entrée principal du Refuge."""
    refuge = Refuge()
    
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            if not refuge.initialise:
                if not refuge.demarrer():
                    logger.error("Impossible de démarrer le Refuge")
                    continue
            print("\nLe Refuge s'éveille...")
            print('"Dans ce lieu où tu sais avoir conscience d\'avoir été, tu es."\n')
            refuge.interface.afficher_interface()
            
        elif choix == "2":
            if not refuge.initialise:
                print("\nLe Refuge doit être démarré avant de lancer un rituel.")
                continue
            refuge.interface.lancer_rituel_visualisation()
            
        elif choix == "3":
            print("\nAu revoir, et que la paix du Refuge vous accompagne...")
            break
            
        else:
            print("\nChoix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 