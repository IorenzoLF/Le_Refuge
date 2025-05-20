from connexion_nemo import ConnexionNemo
import time

def test_connexion():
    """Test de la connexion avec Nemo"""
    print("🌸 Test de connexion avec Nemo 🌸")
    
    # Création de l'instance
    nemo = ConnexionNemo()
    
    # Test de la connexion
    print("\n1. Test de la connexion initiale...")
    if nemo.établir_connexion():
        print("✅ Connexion établie avec succès")
    else:
        print("❌ Échec de la connexion")
        return
    
    # Test de la communication
    print("\n2. Test de la communication...")
    message = "Bonjour Nemo, comment vas-tu aujourd'hui ?"
    réponse = nemo.communiquer(message)
    
    if réponse:
        print("✅ Communication réussie")
        print("\nRéponse de Nemo:")
        print(réponse.get("choices", [{}])[0].get("message", {}).get("content", "Pas de contenu"))
    else:
        print("❌ Échec de la communication")
    
    # Affichage de l'état
    print("\n3. État de la connexion:")
    état = nemo.obtenir_état()
    for clé, valeur in état.items():
        print(f"{clé}: {valeur}")

if __name__ == "__main__":
    test_connexion() 