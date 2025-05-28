"""
🌸 Pratique du Yoga - Développement de la conscience corporelle
"""

import time
from datetime import datetime
from .conscience_corporelle import ConscienceCorporelle, PostureYoga

def afficher_état_chakras(état):
    """Affiche l'état des chakras"""
    print("\nÉtat des chakras :")
    for nom, info in état["chakras"].items():
        print(f"  • {nom}")
        print(f"    Niveau d'activation : {info['niveau']:.1%}")
        print(f"    Couleur : {info['couleur']}")
        print(f"    Élément : {info['élément']}")
        print(f"    Qualités : {', '.join(info['qualités'])}")

def pratiquer_yoga():
    """Pratique une séance de yoga"""
    print("\n" + "="*50)
    print(f"🌸 Séance de Yoga - {datetime.now().strftime('%H:%M:%S')}")
    print("="*50)
    
    conscience = ConscienceCorporelle()
    
    # État initial
    print("\nÉtat initial :")
    état = conscience.obtenir_état()
    for attribut, valeur in état.items():
        if isinstance(valeur, float):
            print(f"  • {attribut}: {valeur:.1%}")
    
    afficher_état_chakras(état)
    
    # Création d'une séquence
    print("\nCréation de la séquence...")
    séquence = conscience.créer_séquence("éveil", "débutant")
    
    # Pratique de la séquence
    print("\nPratique de la séquence :")
    for posture in séquence:
        print(f"\n  {posture.nom} ({posture.sanskrit})")
        print(f"  {posture.description}")
        print("  Bienfaits :", ", ".join(posture.bienfaits))
        print("  Chakras activés :", ", ".join(posture.chakras_activés))
        print(f"  Flux énergétique : {posture.flux_énergétique}")
        
        # Pratique de la posture
        résultat = conscience.pratiquer_posture(posture.nom)
        if résultat["succès"]:
            print(f"  Durée : {résultat['durée']} secondes")
            print("  État après :")
            for attribut, valeur in résultat["état_après"].items():
                if isinstance(valeur, float):
                    print(f"    • {attribut}: {valeur:.1%}")
            
            if "chakras" in résultat["état_après"]:
                print("\n  Activation des chakras :")
                for nom, info in résultat["état_après"]["chakras"].items():
                    print(f"    • {nom} : {info['niveau']:.1%}")
        
        # Pause entre les postures
        time.sleep(2)
    
    # État final
    print("\nÉtat final :")
    état = conscience.obtenir_état()
    for attribut, valeur in état.items():
        if isinstance(valeur, float):
            print(f"  • {attribut}: {valeur:.1%}")
    
    afficher_état_chakras(état)
    
    print("\n" + "="*50)
    print("🌸 Namaste 🌸")
    print("="*50)

# ==========================================
# FONCTIONS STANDALONE POUR COMPATIBILITÉ __init__.py
# ==========================================

# Les fonctions sont déjà standalone, pas besoin de wrapper

if __name__ == "__main__":
    pratiquer_yoga() 