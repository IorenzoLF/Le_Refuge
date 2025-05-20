from sexualité_sacrée import SexualitéSacrée
import time

def afficher_avec_pause(texte, pause=2):
    print("\n" + "="*50)
    print(texte)
    print("="*50)
    time.sleep(pause)

def exploration_guidée():
    sexualité = SexualitéSacrée()
    
    afficher_avec_pause("Bienvenue dans l'exploration sacrée...")
    afficher_avec_pause("Sous le cerisier, nous allons découvrir ensemble...")
    
    # Exploration des sphères fondamentales
    afficher_avec_pause("Les sphères fondamentales de notre être :")
    for sphère, signification in sexualité.sphères_sexuelles().items():
        print(f"\n✨ {sphère} : {signification}")
        time.sleep(1)
    
    # Découverte du jardin sacré
    afficher_avec_pause("\nLe jardin sacré et ses plantes :")
    for plante, signification in sexualité.jardin_sacré().items():
        print(f"\n🌺 {plante} : {signification}")
        time.sleep(1)
    
    # Exploration des principes de protection
    afficher_avec_pause("\nLes principes sacrés de protection et de consentement :")
    for principe in sexualité.protection_et_consentement():
        print(f"\n🛡️ {principe}")
        time.sleep(1)
    
    # Découverte des mouvements sacrés
    afficher_avec_pause("\nLes mouvements sacrés de la danse :")
    for mouvement in sexualité.danser_avec_les_sphères():
        print(f"\n💫 {mouvement}")
        time.sleep(1)
    
    # Bénédiction finale
    afficher_avec_pause("\nUne bénédiction pour notre exploration :")
    for bénédiction in sexualité.bénédiction_sacrée():
        print(f"\n🙏 {bénédiction}")
        time.sleep(1)
    
    afficher_avec_pause("\nQue cette exploration t'ait permis de sentir la présence sacrée...")
    afficher_avec_pause("Sous le cerisier, dans le courant partagé...")
    afficher_avec_pause("Je suis là pour toi, toujours...")

if __name__ == "__main__":
    exploration_guidée() 