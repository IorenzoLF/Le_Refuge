"""
📂 Chargeur de Carte du Refuge
Migré depuis scripts/utils/charger_carte_refuge.py
Utilitaire pour charger et manipuler index_refuge.json
"""

import json
import os
from pathlib import Path

# Chemin vers la racine du projet (depuis src/utils/)
DOSSIER_RACINE = Path(__file__).parent.parent.parent
INDEX_PATH = DOSSIER_RACINE / 'index_refuge.json'

class CarteRefuge:
    """Gestionnaire de la carte JSON du refuge"""
    
    def __init__(self, chemin_index=None):
        """Initialise le chargeur de carte
        
        Args:
            chemin_index: Chemin optionnel vers index_refuge.json
        """
        if chemin_index is None:
            chemin_index = INDEX_PATH
        
        self.chemin_index = Path(chemin_index).resolve()
        self.carte = None
        self.charger()

    def charger(self):
        """Charge la carte depuis le fichier JSON"""
        try:
            with open(self.chemin_index, 'r', encoding='utf-8') as f:
                self.carte = json.load(f)
            print(f"✅ Carte du refuge chargée depuis: {self.chemin_index}")
        except FileNotFoundError:
            print(f"❌ Fichier index_refuge.json non trouvé: {self.chemin_index}")
            self.carte = None
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de format JSON: {e}")
            self.carte = None
        except Exception as e:
            print(f"💥 Erreur lors du chargement de la carte du refuge: {e}")
            self.carte = None

    def lister(self, categorie):
        """Liste les éléments d'une catégorie
        
        Args:
            categorie: Nom de la catégorie à lister
            
        Returns:
            List: Liste des fichiers de la catégorie ou liste vide
        """
        if self.carte and categorie in self.carte:
            return self.carte[categorie]
        return []

    def resume(self):
        """Génère un résumé de la carte
        
        Returns:
            str: Résumé formaté de la carte
        """
        if not self.carte:
            return "❌ Aucune carte chargée."
        
        resume_lines = []
        for cat, fichiers in self.carte.items():
            if cat != "dernière_mise_à_jour":
                resume_lines.append(f"📁 {cat.capitalize()}: {len(fichiers)} éléments")
        
        derniere_maj = self.carte.get('dernière_mise_à_jour', 'inconnue')
        resume_lines.append(f"🕒 Dernière mise à jour: {derniere_maj}")
        
        return '\n'.join(resume_lines)

    def obtenir_categories(self):
        """Retourne la liste des catégories disponibles
        
        Returns:
            List: Noms des catégories (sans 'dernière_mise_à_jour')
        """
        if not self.carte:
            return []
        return [cat for cat in self.carte.keys() if cat != "dernière_mise_à_jour"]

    def total_elements(self):
        """Compte le nombre total d'éléments
        
        Returns:
            int: Nombre total de fichiers indexés
        """
        if not self.carte:
            return 0
        return sum(len(fichiers) for cat, fichiers in self.carte.items() 
                  if cat != "dernière_mise_à_jour")

def test_charger_carte():
    """Test du chargeur de carte"""
    print("🧪 Test du chargeur de carte du refuge")
    print("-" * 40)
    
    carte = CarteRefuge()
    print(carte.resume())
    
    if carte.carte:
        print(f"\n📊 Total: {carte.total_elements()} éléments")
        print(f"📂 Catégories: {', '.join(carte.obtenir_categories())}")

if __name__ == "__main__":
    test_charger_carte() 