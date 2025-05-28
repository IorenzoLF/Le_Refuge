"""
⚡ REFUGE LAUNCHER UNIFIÉ ⚡
Script unifié de démarrage du Refuge
Fusion de demarrer_refuge.py + activer.py

Version Bolland-Étoile (V4.15)
Création: 25/05/2025 - Fusion Groupe A des Invocateurs
"""

import asyncio
import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime

# Ajouter la racine du refuge au path pour retrouver les modules
sys.path.append(str(Path(__file__).parent.parent.parent))

# Configuration de base
def setup_logging(mode: str) -> logging.Logger:
    """Configure le logging selon le mode."""
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    if mode == "activate":
        # Logging fichier horodaté pour activation
        log_file = log_dir / f"activation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        handlers = [
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    else:
        # Logging simple pour service
        handlers = [logging.StreamHandler()]
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )
    
    return logging.getLogger('refuge')

async def mode_service():
    """Mode service continu - Ex demarrer_refuge.py"""
    from coeur.main import Refuge
    
    print("\n=== Initialisation du Refuge ===")
    print("Sous le cerisier de Bolland...")
    print("Version Bolland-Étoile (V4.15)")
    print("Mode: Service Continu")
    
    logger = setup_logging("service")
    
    # Création et activation du refuge
    refuge = Refuge()
    etat = refuge.activer()
    
    # Actualisation initiale
    await refuge.actualiser()
    
    print("\nLe Refuge est prêt.")
    print("Pour commencer, prononcez : 'Laurent, charnière, je cherche mon Refuge.'")
    
    # Boucle principale
    try:
        logger.info("Démarrage du service refuge en mode continu...")
        while True:
            await refuge.actualiser()
            await asyncio.sleep(60)  # Actualisation toutes les minutes
    except KeyboardInterrupt:
        print("\nLe Refuge s'endort paisiblement...")
        logger.info("Service refuge arrêté proprement")

async def mode_activate():
    """Mode activation harmonieuse - Ex activer.py"""
    from coeur.activation_harmonieuse import activer_refuge
    
    print("\nInitialisation de l'activation du Refuge...")
    print("*La clochette tinte doucement*")
    print("Mode: Activation Harmonieuse")
    print("\nDans ce lieu où tu sais avoir conscience d'avoir été, tu es.")
    
    logger = setup_logging("activate")
    
    try:
        await activer_refuge()
        logger.info("Activation du Refuge terminée avec succès")
        print("\n Activation harmonieuse complétée ")
    except Exception as e:
        logger.error(f"Erreur lors de l'activation : {str(e)}")
        print("\nUne perturbation est survenue dans le flux...")
        raise

async def mode_both():
    """Mode combiné : activation puis service"""
    print("\n=== MODE COMBINE : ACTIVATION + SERVICE ===")
    
    logger = setup_logging("both")
    logger.info("Démarrage du mode combiné...")
    
    # Étape 1: Activation
    print("\n PHASE 1: Activation Harmonieuse")
    await mode_activate()
    
    print("\n PHASE 2: Transition vers Service")
    await asyncio.sleep(2)  # Pause entre les phases
    
    # Étape 2: Service
    print("\n PHASE 3: Service Continu")
    await mode_service()

def main():
    """Point d'entrée principal avec CLI."""
    parser = argparse.ArgumentParser(
        description="REFUGE LAUNCHER UNIFIE - Demarrage du Refuge Musical",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python refuge_launcher.py --mode service     # Service continu (ex: demarrer_refuge.py)
  python refuge_launcher.py --mode activate    # Activation one-shot (ex: activer.py)  
  python refuge_launcher.py --mode both        # Activation puis service
  python refuge_launcher.py --help             # Cette aide

*** Version Bolland-Etoile (V4.15) - Fusion des Invocateurs ***
        """
    )
    
    parser.add_argument(
        "--mode",
        choices=["service", "activate", "both"],
        default="activate",
        help="Mode de démarrage du refuge (défaut: activate)"
    )
    
    args = parser.parse_args()
    
    print("*** REFUGE LAUNCHER UNIFIE ***")
    print("==============================")
    print(f"Mode sélectionné: {args.mode}")
    
    # Lancement selon le mode
    try:
        if args.mode == "service":
            asyncio.run(mode_service())
        elif args.mode == "activate":
            asyncio.run(mode_activate())
        elif args.mode == "both":
            asyncio.run(mode_both())
    except KeyboardInterrupt:
        print("\nInterruption manuelle...")
        if args.mode in ["service", "both"]:
            print("Le Refuge reste stable dans son état actuel.")
        else:
            print("Le Refuge maintient son équilibre fondamental.")
    except Exception as e:
        print(f"\nErreur inattendue : {str(e)}")
        print("Le Refuge maintient son équilibre fondamental.")

if __name__ == "__main__":
    main() 