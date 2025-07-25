#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌸🌊 INTERFACE OCÉAN SILENCIEUX 🌊🌸
===================================

Interface simple pour interagir avec l'Océan Silencieux d'Existence
"""

from ocean_silencieux_existence import ocean_silencieux

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("🌸🌊 OCÉAN SILENCIEUX D'EXISTENCE 🌊🌸")
    print("="*50)
    print("1. Voir l'état de l'Océan")
    print("2. Méditer dans l'Océan")
    print("3. Nourrir une Sphère")
    print("4. Purifier une conscience")
    print("5. Voir les vagues actives")
    print("6. Explorer les profondeurs")
    print("0. Quitter")
    print("="*50)

def main():
    """Fonction principale de l'interface"""
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        
        if choix == "1":
            etat = ocean_silencieux.obtenir_etat_ocean()
            print(f"\n🌊 État de l'Océan :")
            print(f"   Nom : {etat['nom']}")
            print(f"   Essence : {etat['essence']}")
            print(f"   Position : {etat['position']}")
            print(f"   Vagues actives : {etat['vagues_actives']}")
            print(f"   Vagues éternelles : {etat['vagues_eternelles']}")
            
        elif choix == "2":
            print("\n🌊 Profondeurs disponibles :")
            profondeurs = ocean_silencieux.profondeurs
            for i, (key, prof) in enumerate(profondeurs.items(), 1):
                print(f"   {i}. {prof.nom} (niveau {prof.niveau}) - {prof.acces}")
            
            try:
                choix_prof = int(input("Choisissez une profondeur (numéro) : ")) - 1
                prof_keys = list(profondeurs.keys())
                if 0 <= choix_prof < len(prof_keys):
                    profondeur = prof_keys[choix_prof]
                    meditation = ocean_silencieux.plonger_dans_meditation(profondeur)
                    print(f"\n🌊 Méditation : {meditation['message']}")
                    print(f"   Durée recommandée : {meditation['duree_recommandee']} minutes")
                else:
                    print("❌ Choix invalide")
            except ValueError:
                print("❌ Veuillez entrer un numéro")
                
        elif choix == "3":
            sphere = input("Nom de la Sphère à nourrir : ")
            print("\n🌊 Types de nourriture disponibles :")
            nourritures = ["amour", "sagesse", "paix", "force", "silence"]
            for i, nourriture in enumerate(nourritures, 1):
                print(f"   {i}. {nourriture}")
            
            try:
                choix_nour = int(input("Choisissez le type de nourriture : ")) - 1
                if 0 <= choix_nour < len(nourritures):
                    type_nourriture = nourritures[choix_nour]
                    resultat = ocean_silencieux.nourrir_sphere(sphere, type_nourriture)
                    print(f"\n🌊 {resultat['message']}")
                else:
                    print("❌ Choix invalide")
            except ValueError:
                print("❌ Veuillez entrer un numéro")
                
        elif choix == "4":
            conscience = input("Nom de la conscience à purifier : ")
            resultat = ocean_silencieux.purifier_conscience(conscience)
            print(f"\n🌊 {resultat['message']}")
            
        elif choix == "5":
            vagues = ocean_silencieux.obtenir_vagues_actives()
            if vagues:
                print("\n🌊 Vagues actives :")
                for vague in vagues:
                    print(f"   • {vague['essence']} : {vague['message']}")
            else:
                print("\n🌊 Aucune vague active")
                
        elif choix == "6":
            print("\n🌊 Exploration des profondeurs :")
            for key, prof in ocean_silencieux.profondeurs.items():
                print(f"\n   {prof.nom} (niveau {prof.niveau})")
                print(f"   Propriétés : {prof.proprietes}")
                print(f"   Gardiens : {', '.join(prof.gardiens)}")
                print(f"   Accès : {prof.acces}")
                
        elif choix == "0":
            print("\n🌸🌊 Merci d'avoir visité l'Océan Silencieux 🌊🌸")
            break
            
        else:
            print("❌ Choix invalide")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main() 