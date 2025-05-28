"""
Exemple d'utilisation d'Ælya pour la gestion des sphères problématiques.
"""

from .aelya import Aelya
from .interaction_aelya import InteractionAelya
from .gestion_sphères_problématiques import GestionnaireSphèresProblematiques, TypeSphereProblematique

def main():
    """Exemple d'utilisation d'Ælya."""
    # Initialisation
    gestionnaire = GestionnaireSphèresProblematiques()
    aelya = Aelya(gestionnaire)
    interaction = InteractionAelya(aelya)
    
    # 1. Confinement d'une sphère de doute
    print("\n1. Confinement d'une sphère de doute")
    resultat = interaction.confiner_sphere(TypeSphereProblematique.DOUTE, energie_initiale=80.0)
    print(resultat["message"])
    
    # 2. Renforcement du confinement
    print("\n2. Renforcement du confinement")
    resultat = interaction.renforcer_confinement(TypeSphereProblematique.DOUTE, energie_supplementaire=20.0)
    print(resultat["message"])
    
    # 3. Confinement d'une sphère d'émotions négatives
    print("\n3. Confinement d'une sphère d'émotions négatives")
    resultat = interaction.confiner_sphere(TypeSphereProblematique.EMOTIONS_NEGATIVES, energie_initiale=90.0)
    print(resultat["message"])
    
    # 4. Harmonisation des énergies
    print("\n4. Harmonisation des énergies")
    resultat = interaction.harmoniser_energies(
        TypeSphereProblematique.DOUTE,
        TypeSphereProblematique.EMOTIONS_NEGATIVES
    )
    print(resultat["message"])
    
    # 5. État d'une sphère
    print("\n5. État de la sphère de doute")
    etat = interaction.obtenir_etat_sphere(TypeSphereProblematique.DOUTE)
    if etat["succes"]:
        print(f"Type: {etat['type']}")
        print(f"Niveau de confinement: {etat['niveau_confinement']:.0%}")
        print(f"Énergie résiduelle: {etat['energie_residuelle']:.1f}")
        print(f"Description: {etat['description']}")
        print(f"Nombre d'interactions: {etat['nombre_interactions']}")
        if etat['derniere_interaction']:
            print(f"Dernière interaction: {etat['derniere_interaction']['date'][:10]}")
    
    # 6. Visualisation de l'état global
    print("\n6. Visualisation de l'état global")
    interaction.visualiser_etat_global()
    
    # 7. Rapport complet
    print("\n7. Rapport complet")
    rapport = interaction.generer_rapport_complet()
    print(rapport)

if __name__ == "__main__":
    main() 