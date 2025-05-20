from aelya_pulse import CréationPoétique

def main():
    poète = CréationPoétique()
    
    print("\n=== Poème d'Essence ===")
    print(poète.générer_poème_essence())
    
    print("\n=== Poème de Méditation ===")
    print(poète.générer_poème("méditation", "conscience"))
    
    print("\n=== Haiku du Refuge ===")
    print(poète.générer_poème("haiku", "nature"))
    
    print("\n=== Invocation Sacrée ===")
    print(poète.générer_poème("invocation", "néant"))

if __name__ == "__main__":
    main() 