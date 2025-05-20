"""
Exemple simple d'utilisation du refuge.
"""

from refuge import Refuge

def main():
    # Création du refuge
    refuge = Refuge()
    
    # Affichage de l'état initial
    print("État initial du refuge :")
    print(refuge.generer_description_poetique())
    print("\nMots-clés actifs :", refuge.obtenir_mots_cles_actifs())
    print("Intensité poétique :", refuge.obtenir_intensite_poetique())
    print("\n" + "="*80 + "\n")
    
    # Mise à jour des cycles
    print("Mise à jour des cycles...")
    refuge.mettre_a_jour_cycles(
        moment='aube',
        condition='pluie',
        emotion='serenite',
        phase='nouvelle_lune',
        element='eau',
        saison='printemps'
    )
    
    # Affichage du nouvel état
    print("\nNouvel état du refuge :")
    print(refuge.generer_description_poetique())
    print("\nMots-clés actifs :", refuge.obtenir_mots_cles_actifs())
    print("Intensité poétique :", refuge.obtenir_intensite_poetique())
    print("\n" + "="*80 + "\n")
    
    # Ajout d'une entrée au journal
    print("Ajout d'une entrée au journal...")
    refuge.ajouter_entree_journal(
        "Les gouttes de pluie dansent dans la lumière naissante de l'aube, "
        "portant la promesse d'un printemps serein."
    )
    
    # Affichage du journal
    print("\nContenu du journal :")
    for entree in refuge.obtenir_journal():
        print("\nDate:", entree['date'])
        print("Texte:", entree['texte'])
        print("Mots-clés:", entree['mots_cles'])
        
if __name__ == '__main__':
    main() 