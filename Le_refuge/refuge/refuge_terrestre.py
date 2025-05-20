from typing import Dict, Optional
from datetime import datetime
from .spheres_terrestres import CollectionSpheresTerrestres, TypeSphereTerrestre
from .rituels_terrestres import GestionnaireRituelsTerrestres

class RefugeTerrestre:
    """Intègre les aspects terrestres dans le Refuge, comme un jardin où chaque sphère est une fleur qui danse."""
    
    def __init__(self):
        self.collection_spheres = CollectionSpheresTerrestres()
        self.gestionnaire_rituels = GestionnaireRituelsTerrestres(self.collection_spheres)
        self.harmonie = 0.5
        self.etat = "initialisation"
        self.derniere_activation = None
        self._initialiser_harmonie()

    def _initialiser_harmonie(self):
        """Initialise l'harmonie du Refuge Terrestre."""
        self.harmonie = 0.5
        self.etat = "en_attente"
        self.derniere_activation = datetime.now()

    def activer_sphere_terrestre(self, type_sphere: TypeSphereTerrestre) -> str:
        """Active une sphère terrestre et met à jour l'harmonie."""
        resultat = self.collection_spheres.activer_sphere(type_sphere)
        if "activée" in resultat:
            self.harmonie = min(1.0, self.harmonie + 0.1)
            self.derniere_activation = datetime.now()
        return resultat

    def executer_rituel_terrestre(self, nom_rituel: str) -> str:
        """Exécute un rituel terrestre et met à jour l'harmonie."""
        resultat = self.gestionnaire_rituels.executer_rituel(nom_rituel)
        if "exécuté avec succès" in resultat:
            self.harmonie = min(1.0, self.harmonie + 0.2)
            self.etat = "rituel_en_cours"
        return resultat

    def equilibrer_spheres_terrestres(self) -> str:
        """Équilibre toutes les sphères terrestres et harmonise le Refuge."""
        resultat = self.collection_spheres.equilibrer_spheres()
        self.harmonie = 0.7  # Équilibre parfait
        self.etat = "equilibre"
        return resultat

    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel du Refuge Terrestre, comme un jardin en fleur."""
        return {
            "harmonie": self.harmonie,
            "etat": self.etat,
            "derniere_activation": self.derniere_activation,
            "spheres": {
                type_sphere.value: {
                    "couleur": sphere.couleur,
                    "frequence": sphere.frequence,
                    "luminosite": sphere.luminosite,
                    "etat": sphere.etat,
                    "capacites": sphere.capacites
                }
                for type_sphere, sphere in self.collection_spheres.spheres.items()
            },
            "rituels": self.gestionnaire_rituels.obtenir_etat()["rituels"]
        }

    def integrer_dans_refuge(self, refuge_principal) -> str:
        """Intègre les aspects terrestres dans le Refuge principal."""
        self.etat = "integre"
        return "Aspects terrestres intégrés dans le Refuge, comme des racines qui s'enfoncent dans la terre"

    def __str__(self) -> str:
        """Représentation poétique du Refuge Terrestre."""
        return f"""Refuge Terrestre
        Harmonie: {self.harmonie:.2f}
        État: {self.etat}
        Dernière activation: {self.derniere_activation}
        Sphères actives: {sum(1 for s in self.collection_spheres.spheres.values() if s.etat == 'actif')}
        """

# Exemple d'utilisation
if __name__ == "__main__":
    refuge = RefugeTerrestre()
    
    # Activation des sphères
    print(refuge.activer_sphere_terrestre(TypeSphereTerrestre.MAGNETOSPHERE))
    print(refuge.activer_sphere_terrestre(TypeSphereTerrestre.CYCLE_HYDRIQUE))
    
    # Exécution d'un rituel
    print(refuge.executer_rituel_terrestre("rituel_protection_magnetique"))
    
    # Équilibrage
    print(refuge.equilibrer_spheres_terrestres())
    
    # Affichage de l'état
    print(refuge) 