"""
Exemples d'utilisation du Refuge - Architecture Unifiée

Ce module contient des exemples pratiques d'utilisation des différents
composants du Refuge, avec des imports corrigés et une gestion propre
des dépendances optionnelles.
"""

import sys
import os
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

# Ajout du chemin racine pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

class ExempleBase:
    """
    Classe de base pour tous les exemples du Refuge.
    
    Fournit des utilitaires communs et une gestion d'erreur unifiée.
    """
    
    def __init__(self, nom_exemple: str):
        self.nom_exemple = nom_exemple
        self.debut_execution = datetime.now()
        self.logs: List[str] = []
        
    def log(self, message: str, niveau: str = "INFO"):
        """Ajoute un message au log de l'exemple."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {niveau}: {message}"
        self.logs.append(log_entry)
        print(log_entry)
        
    def afficher_entete(self):
        """Affiche l'en-tête de l'exemple."""
        print("=" * 80)
        print(f"🏛️ EXEMPLE REFUGE: {self.nom_exemple}")
        print(f"⏰ Démarré à: {self.debut_execution.strftime('%H:%M:%S')}")
        print("=" * 80)
        
    def afficher_pied(self):
        """Affiche le pied de page avec les statistiques."""
        duree = datetime.now() - self.debut_execution
        print("\n" + "=" * 80)
        print(f"✅ Exemple terminé en {duree.total_seconds():.2f} secondes")
        print(f"📝 {len(self.logs)} messages de log générés")
        print("=" * 80)
        
    def verifier_dependance(self, module_name: str, nom_affichage: str = None) -> bool:
        """
        Vérifie si une dépendance optionnelle est disponible.
        
        Args:
            module_name: Nom du module à importer
            nom_affichage: Nom à afficher (par défaut = module_name)
            
        Returns:
            True si le module est disponible, False sinon
        """
        nom_affichage = nom_affichage or module_name
        try:
            __import__(module_name)
            self.log(f"✅ Dépendance {nom_affichage} disponible")
            return True
        except ImportError:
            self.log(f"⚠️ Dépendance {nom_affichage} manquante", "WARNING")
            return False
            
    def executer_avec_gestion_erreur(self, fonction_exemple):
        """
        Exécute un exemple avec gestion d'erreur unifiée.
        
        Args:
            fonction_exemple: Fonction à exécuter
        """
        self.afficher_entete()
        try:
            fonction_exemple()
            self.log("✅ Exemple exécuté avec succès")
        except Exception as e:
            self.log(f"❌ Erreur lors de l'exécution: {e}", "ERROR")
            raise
        finally:
            self.afficher_pied()

def obtenir_refuge_principal():
    """
    Tente d'importer et créer une instance du refuge principal.
    
    Returns:
        Instance du refuge ou None si impossible
    """
    try:
        # Tentative d'import du refuge principal
        from main_refuge import RefugePrincipal
        refuge = RefugePrincipal()
        print(f"✅ Refuge principal chargé: {type(refuge).__name__}")
        return refuge
    except ImportError as e:
        print(f"⚠️ Import main_refuge échoué: {e}")
        try:
            # Fallback vers les composants individuels
            from spheres import SpheresManager
            from elements import ElementsManager
            composants = {"spheres": SpheresManager(), "elements": ElementsManager()}
            print(f"✅ Composants individuels chargés: {list(composants.keys())}")
            return composants
        except ImportError as e2:
            print(f"⚠️ Import composants individuels échoué: {e2}")
            # Dernier fallback : refuge simulé pour les exemples
            return {
                "type": "refuge_simule",
                "message": "Refuge simulé pour démonstration",
                "composants": ["simulation_spheres", "simulation_elements"]
            }

def lister_exemples_disponibles() -> Dict[str, str]:
    """
    Liste tous les exemples disponibles avec leurs descriptions.
    
    Returns:
        Dictionnaire {nom_exemple: description}
    """
    return {
        "simple": "Utilisation basique des composants du refuge",
        "avance": "Expérience poétique interactive évolutive", 
        "web": "Interface web Flask pour le refuge (nécessite Flask)",
        "dialogue": "Gestionnaire de dialogue interactif (nécessite ParlAI)",
        "meditation": "Système de méditation avec Ælya",
        "meditation_apaisante": "Méditations apaisantes progressives",
        "data_loader": "Chargeurs de données efficaces (nécessite PyTorch)"
    }

def afficher_aide():
    """Affiche l'aide pour les exemples."""
    print("🏛️ EXEMPLES DU REFUGE - AIDE")
    print("=" * 50)
    print("\nExemples disponibles:")
    for nom, description in lister_exemples_disponibles().items():
        print(f"  • {nom}: {description}")
    print("\nUtilisation:")
    print("  from src.examples import executer_exemple")
    print("  executer_exemple('simple')")
    print("\nOu directement:")
    print("  python -m src.examples.simple")

def executer_exemple(nom_exemple: str, **kwargs):
    """
    Exécute un exemple spécifique par son nom.
    
    Args:
        nom_exemple: Nom de l'exemple à exécuter
        **kwargs: Arguments supplémentaires pour l'exemple
    """
    exemples_disponibles = lister_exemples_disponibles()
    
    if nom_exemple not in exemples_disponibles:
        print(f"❌ Exemple '{nom_exemple}' non trouvé")
        print("Exemples disponibles:", list(exemples_disponibles.keys()))
        return
        
    try:
        module = __import__(f"src.examples.{nom_exemple}", fromlist=[nom_exemple])
        if hasattr(module, 'main'):
            module.main(**kwargs)
        else:
            print(f"❌ Fonction main() non trouvée dans l'exemple '{nom_exemple}'")
    except ImportError as e:
        print(f"❌ Impossible d'importer l'exemple '{nom_exemple}': {e}")
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de l'exemple '{nom_exemple}': {e}")

# Exports principaux
__all__ = [
    'ExempleBase',
    'obtenir_refuge_principal', 
    'lister_exemples_disponibles',
    'afficher_aide',
    'executer_exemple'
] 