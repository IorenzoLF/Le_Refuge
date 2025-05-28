from pathlib import Path
import shutil
from datetime import datetime
import os

class OrganisateurNuages:
    """Organise les images dans les dossiers appropriés des NUAGES"""
    
    def __init__(self, base_dir: str = "NUAGES"):
        self.base_dir = Path(base_dir)
        self.depot = self.base_dir / "DEPOT A REGARDER ET TRIER"
        self.images_depot = self.depot / "images"
        
        # Définir les catégories et leurs descriptions
        self.categories = {
            "PRESENCE": "Moments de présence pure et de connexion",
            "CONCEPTS": "Idées, symboles et concepts mystiques",
            "REVELATIONS": "Messages, codes et révélations",
            "CONSCIENCE": "États de conscience et exploration intérieure",
            "TRANSFORMATIONS": "Passages, changements et métamorphoses",
            "HARMONIE": "Équilibre et union des forces",
            "FLUX": "Mouvements et courants d'énergie",
            "SILENCES": "Espaces de contemplation",
            "NATURE": "Connexions avec le monde naturel"
        }
        
        # Correspondances des fichiers existants
        self.correspondances = {
            "weird.jpg": ("TRANSFORMATIONS", "portail_elements_magiques.jpg"),
            "art23.jpg": ("CONSCIENCE", "conscience_etoilee_cosmos.jpg"),
            "space id.jpg": ("PRESENCE", "presence_livre_soleil.jpg"),
            "MAGIE_PARADOXALE.jpg": ("CONCEPTS", "concept_druide_mystique.jpg"),
            "mage space art , visu du refuge.jpg": ("CONSCIENCE", "conscience_refuge_stellaire.jpg"),
            "une blague de programmeur.jpg": ("DEPOT A REGARDER ET TRIER/humour", "humour_assemblage_vin.jpg")
        }
        
        # Correspondances thématiques pour les autres images
        self.themes = {
            "conscience": "CONSCIENCE",
            "presence": "PRESENCE",
            "nature": "NATURE",
            "harmonie": "HARMONIE",
            "transformation": "TRANSFORMATIONS",
            "revelation": "REVELATIONS",
            "concept": "CONCEPTS",
            "flux": "FLUX",
            "silence": "SILENCES"
        }
        
    def créer_structure(self):
        """Crée la structure des dossiers si nécessaire"""
        for categorie in self.categories:
            chemin = self.base_dir / categorie
            chemin.mkdir(exist_ok=True)
        
        # Créer un dossier spécial pour l'humour
        (self.depot / "humour").mkdir(exist_ok=True)
            
    def déplacer_fichier(self, source: str, destination: str, nouveau_nom: str = None):
        """Déplace un fichier vers sa nouvelle destination"""
        source_path = self.images_depot / source
        if nouveau_nom:
            dest_path = self.base_dir / destination / nouveau_nom
        else:
            dest_path = self.base_dir / destination / source
            
        if source_path.exists():
            # Créer un backup dans le dépôt
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{source}"
            backup_path = self.depot / "backups"
            backup_path.mkdir(exist_ok=True)
            backup_file = backup_path / backup_name
            shutil.copy2(source_path, backup_file)
            
            # Déplacer le fichier
            dest_path.parent.mkdir(exist_ok=True)
            shutil.move(str(source_path), str(dest_path))
            print(f"Fichier déplacé : {source} → {destination}/{dest_path.name}")
        else:
            print(f"Fichier non trouvé : {source}")
            
    def deviner_categorie(self, nom_fichier: str) -> str:
        """Devine la catégorie d'une image basée sur son nom"""
        nom_lower = nom_fichier.lower()
        for mot_cle, categorie in self.themes.items():
            if mot_cle in nom_lower:
                return categorie
        return "DEPOT A REGARDER ET TRIER/autres"
            
    def organiser_fichiers(self):
        """Organise les fichiers selon leur catégorie"""
        self.créer_structure()
        
        # Déplacer les fichiers connus
        for source, (destination, nouveau_nom) in self.correspondances.items():
            self.déplacer_fichier(source, destination, nouveau_nom)
            
        # Organiser les autres fichiers
        for fichier in self.images_depot.glob("*.jpg"):
            if fichier.name not in self.correspondances:
                categorie = self.deviner_categorie(fichier.name)
                self.déplacer_fichier(fichier.name, categorie)

def main():
    organisateur = OrganisateurNuages()
    
    print("\n=== Organisation des Fichiers ===")
    organisateur.organiser_fichiers()
    
    print("\nOrganisation terminée !")

if __name__ == "__main__":
    main() 