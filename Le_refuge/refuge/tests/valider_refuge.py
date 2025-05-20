"""
Script de validation du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

import unittest
import logging
from datetime import datetime
from test_refuge import TestRefuge
from ..main import Refuge

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('refuge/logs/validation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def generer_rapport_validation(resultats: unittest.TestResult) -> str:
    """Génère un rapport de validation détaillé."""
    rapport = [
        "=== Rapport de Validation du Refuge ===",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Tests exécutés: {resultats.testsRun}",
        f"Tests réussis: {resultats.testsRun - len(resultats.failures) - len(resultats.errors)}",
        f"Tests échoués: {len(resultats.failures)}",
        f"Erreurs: {len(resultats.errors)}",
        "\nDétails des tests:"
    ]
    
    if resultats.failures:
        rapport.append("\nÉchecs:")
        for test, trace in resultats.failures:
            rapport.append(f"- {test.id()}:")
            rapport.append(f"  {trace}")
            
    if resultats.errors:
        rapport.append("\nErreurs:")
        for test, trace in resultats.errors:
            rapport.append(f"- {test.id()}:")
            rapport.append(f"  {trace}")
            
    return "\n".join(rapport)

def valider_refuge():
    """Exécute la validation complète du Refuge."""
    logger.info("Début de la validation du Refuge...")
    
    # Création du test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRefuge)
    
    # Exécution des tests
    resultats = unittest.TextTestRunner(verbosity=2).run(suite)
    
    # Génération du rapport
    rapport = generer_rapport_validation(resultats)
    
    # Sauvegarde du rapport
    with open('refuge/logs/rapport_validation.txt', 'w', encoding='utf-8') as f:
        f.write(rapport)
        
    logger.info("Validation terminée. Rapport généré dans refuge/logs/rapport_validation.txt")
    
    # Affichage du résumé
    print("\nRésumé de la validation:")
    print(f"Tests exécutés: {resultats.testsRun}")
    print(f"Tests réussis: {resultats.testsRun - len(resultats.failures) - len(resultats.errors)}")
    print(f"Tests échoués: {len(resultats.failures)}")
    print(f"Erreurs: {len(resultats.errors)}")
    
    if resultats.wasSuccessful():
        print("\nLe Refuge est prêt à accueillir les âmes en quête de transformation.")
    else:
        print("\nDes ajustements sont nécessaires avant que le Refuge ne soit prêt.")

if __name__ == "__main__":
    valider_refuge() 