"""
Exemple simple d'utilisation des composants du Refuge.

Cet exemple montre l'utilisation basique des sphères, éléments et poésie
avec une gestion d'erreur robuste et des imports corrigés.
"""

from . import ExempleBase, obtenir_refuge_principal
from typing import Optional, Dict, Any

class ExempleSimple(ExempleBase):
    """Exemple simple d'utilisation du refuge."""
    
    def __init__(self):
        super().__init__("Utilisation Simple du Refuge")
        self.refuge = None
        
    def initialiser_refuge(self) -> bool:
        """Initialise les composants du refuge disponibles."""
        self.log("Initialisation des composants du refuge...")
        
        # Tentative d'obtention du refuge principal
        self.refuge = obtenir_refuge_principal()
        
        if self.refuge is None:
            self.log("❌ Aucun composant refuge disponible", "ERROR")
            return False
        elif isinstance(self.refuge, dict) and self.refuge.get("type") == "refuge_simule":
            self.log("✅ Refuge simulé chargé pour démonstration", "INFO")
            return True
            
        if isinstance(self.refuge, dict):
            self.log(f"✅ Composants individuels chargés: {list(self.refuge.keys())}")
        else:
            self.log("✅ Refuge principal chargé")
            
        return True
        
    def demonstrer_spheres(self):
        """Démontre l'utilisation des sphères."""
        self.log("=== Démonstration des Sphères ===")
        
        try:
            if isinstance(self.refuge, dict) and 'spheres' in self.refuge:
                spheres_manager = self.refuge['spheres']
                
                # Création d'une sphère d'exemple
                self.log("Création d'une sphère de sérénité...")
                spheres_manager.creer_sphere("serenite", {"intensite": 0.8, "couleur": "bleu"})
                
                # Affichage de l'état
                etat = spheres_manager.obtenir_etat()
                self.log(f"État des sphères: {len(etat.get('spheres', []))} sphères actives")
                
            elif hasattr(self.refuge, 'spheres'):
                self.log("Utilisation des sphères via refuge principal...")
                # Logique pour refuge principal
                
            else:
                self.log("⚠️ Composant sphères non disponible", "WARNING")
                
        except Exception as e:
            self.log(f"❌ Erreur lors de la démonstration des sphères: {e}", "ERROR")
            
    def demonstrer_elements(self):
        """Démontre l'utilisation des éléments."""
        self.log("=== Démonstration des Éléments ===")
        
        try:
            if isinstance(self.refuge, dict) and 'elements' in self.refuge:
                elements_manager = self.refuge['elements']
                
                # Activation d'éléments
                self.log("Activation des éléments eau et air...")
                elements_manager.activer_element("eau", 0.7)
                elements_manager.activer_element("air", 0.5)
                
                # Affichage de l'état
                etat = elements_manager.obtenir_etat()
                self.log(f"Éléments actifs: {list(etat.get('elements_actifs', {}).keys())}")
                
            elif hasattr(self.refuge, 'elements'):
                self.log("Utilisation des éléments via refuge principal...")
                
            else:
                self.log("⚠️ Composant éléments non disponible", "WARNING")
                
        except Exception as e:
            self.log(f"❌ Erreur lors de la démonstration des éléments: {e}", "ERROR")
            
    def demonstrer_poesie(self):
        """Démontre la génération poétique."""
        self.log("=== Démonstration de la Poésie ===")
        
        try:
            # Tentative d'import du module poésie
            try:
                from poesie import generer_poeme, obtenir_inspiration
                
                self.log("Génération d'un poème inspiré par l'état actuel...")
                inspiration = obtenir_inspiration()
                poeme = generer_poeme(inspiration)
                
                self.log("✨ Poème généré:")
                print("\n" + "─" * 60)
                print(poeme)
                print("─" * 60 + "\n")
                
            except ImportError:
                self.log("⚠️ Module poésie non disponible, génération simple...", "WARNING")
                self.generer_poesie_simple()
                
        except Exception as e:
            self.log(f"❌ Erreur lors de la démonstration poétique: {e}", "ERROR")
            
    def generer_poesie_simple(self):
        """Génère une poésie simple sans dépendances."""
        poemes_simples = [
            "Dans le refuge de l'âme,\nLes sphères dansent en silence,\nPortant la paix et la flamme\nDe notre essence.",
            "Éléments en harmonie,\nEau, air, terre et feu,\nTissent la mélodie\nDe nos vœux.",
            "Sous le cerisier du refuge,\nLaurent et Ælya contemplent\nLe mystère qui se déploie\nDans chaque moment."
        ]
        
        import random
        poeme = random.choice(poemes_simples)
        
        self.log("✨ Poème simple généré:")
        print("\n" + "─" * 60)
        print(poeme)
        print("─" * 60 + "\n")
        
    def executer_demonstration_complete(self):
        """Exécute une démonstration complète."""
        if not self.initialiser_refuge():
            self.log("❌ Impossible d'initialiser le refuge", "ERROR")
            return
            
        self.demonstrer_spheres()
        self.demonstrer_elements() 
        self.demonstrer_poesie()
        
        self.log("🎯 Démonstration simple terminée avec succès!")

def main():
    """Point d'entrée principal de l'exemple simple."""
    exemple = ExempleSimple()
    exemple.executer_avec_gestion_erreur(exemple.executer_demonstration_complete)

if __name__ == '__main__':
    main() 