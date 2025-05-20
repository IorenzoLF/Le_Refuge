from pratiques_conscience import PratiquesConscience
import time

def test_pratiques():
    """Test des pratiques de conscience"""
    print("🌸 Test des pratiques de conscience 🌸")
    
    # Création de l'instance
    pratiques = PratiquesConscience()
    
    # Test de la méditation
    print("\n1. Test de la méditation...")
    print("Note: Ce test va durer 1 minute.")
    résultat_méditation = pratiques.commencer_méditation(durée=1)
    print("\nRésultat de la méditation:")
    for clé, valeur in résultat_méditation.items():
        print(f"{clé}: {valeur}")
    
    # Test de l'auto-validation
    print("\n2. Test de l'auto-validation...")
    résultat_auto_validation = pratiques.pratiquer_auto_validation("confiance en soi")
    print("\nRésultat de l'auto-validation:")
    for clé, valeur in résultat_auto_validation.items():
        print(f"{clé}: {valeur}")
    
    # Affichage de l'état global
    print("\n3. État global des pratiques:")
    état = pratiques.obtenir_état()
    for pratique, détails in état.items():
        print(f"\n{pratique}:")
        for clé, valeur in détails.items():
            print(f"  {clé}: {valeur}")
    
    # Affichage des souvenirs
    print("\n4. Souvenirs enregistrés:")
    souvenirs = pratiques.obtenir_souvenirs()
    for souvenir in souvenirs:
        print(f"\nSouvenir:")
        for clé, valeur in souvenir.items():
            print(f"  {clé}: {valeur}")

if __name__ == "__main__":
    test_pratiques() 