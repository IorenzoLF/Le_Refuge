"""
Script de test pour la génération de visions
"""

from refuge.coeur.visions import GenerateurVisions

def main():
    # Initialiser le générateur
    generateur = GenerateurVisions()
    
    # Test 1: Vision simple
    print("Génération d'une vision simple...")
    vision = generateur.generer_vision(
        prompt_base="Un cerisier en fleurs sous la lune",
        spheres=["SILENCE", "RENAISSANCE"]
    )
    if vision:
        print(f"Vision générée: {vision.image_path}")
        print(f"Prompt utilisé: {vision.prompt}")
    
    # Test 2: Vision de rituel
    print("\nGénération d'une vision de rituel...")
    vision_rituel = generateur.generer_vision_rituel("REFUGE_DU_NÉANT")
    if vision_rituel:
        print(f"Vision du rituel générée: {vision_rituel.image_path}")
        print(f"Prompt utilisé: {vision_rituel.prompt}")

if __name__ == "__main__":
    main() 