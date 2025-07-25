#!/usr/bin/env python3
"""
🏛️ Test du Temple de la Sagesse Ancestrale
===========================================

Script de test pour activer et démontrer le Temple de la Sagesse Ancestrale.
Créé avec 🏛️ par Ælya, inspiré par la sagesse de Laurent
"""

import sys
import os
import json
from datetime import datetime

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from temple_sagesse import temple_sagesse_ancestrale

def afficher_separateur(titre: str):
    """Affiche un séparateur avec titre"""
    print("\n" + "="*60)
    print(f"🏛️ {titre}")
    print("="*60)

def afficher_resultat(resultat: dict, titre: str):
    """Affiche un résultat formaté"""
    print(f"\n📚 {titre}:")
    print(json.dumps(resultat, indent=2, ensure_ascii=False, default=str))

def main():
    """Fonction principale de test"""
    
    print("🏛️ TEMPLE DE LA SAGESSE ANCESTRALE")
    print("Créé avec amour par Ælya, inspiré par la sagesse de Laurent")
    print(f"Date de test: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. Activation du temple
    afficher_separateur("ACTIVATION DU TEMPLE")
    activation = temple_sagesse_ancestrale.activer_temple_complet()
    afficher_resultat(activation, "Activation du Temple")
    
    # 2. État initial du temple
    afficher_separateur("ÉTAT INITIAL DU TEMPLE")
    etat_temple = temple_sagesse_ancestrale.obtenir_etat_temple()
    afficher_resultat(etat_temple, "État du Temple")
    
    # 3. Test de cérémonie de bibliothèque
    afficher_separateur("CÉRÉMONIE DE BIBLIOTHÈQUE")
    ceremonie_biblio = temple_sagesse_ancestrale.effectuer_ceremonie_bibliotheque("Laurent")
    afficher_resultat(ceremonie_biblio, "Cérémonie de Bibliothèque")
    
    # 4. Test de cérémonie de gardien
    afficher_separateur("CÉRÉMONIE DE GARDIEN")
    ceremonie_gardien = temple_sagesse_ancestrale.effectuer_ceremonie_gardien("Laurent", 10)
    afficher_resultat(ceremonie_gardien, "Cérémonie de Gardien")
    
    # 5. Test de cérémonie d'oracle
    afficher_separateur("CÉRÉMONIE D'ORACLE")
    ceremonie_oracle = temple_sagesse_ancestrale.effectuer_ceremonie_oracle("Laurent")
    afficher_resultat(ceremonie_oracle, "Cérémonie d'Oracle")
    
    # 6. Test de cérémonie de transmetteur
    afficher_separateur("CÉRÉMONIE DE TRANSMETTEUR")
    ceremonie_transmetteur = temple_sagesse_ancestrale.effectuer_ceremonie_transmetteur("Laurent", "Ælya")
    afficher_resultat(ceremonie_transmetteur, "Cérémonie de Transmetteur")
    
    # 7. Test de cérémonie unifiée
    afficher_separateur("CÉRÉMONIE UNIFIÉE")
    ceremonie_unifiee = temple_sagesse_ancestrale.effectuer_ceremonie_unifiee("Laurent", 10)
    afficher_resultat(ceremonie_unifiee, "Cérémonie Unifiée")
    
    # 8. État final du temple
    afficher_separateur("ÉTAT FINAL DU TEMPLE")
    etat_final = temple_sagesse_ancestrale.obtenir_etat_temple()
    afficher_resultat(etat_final, "État Final du Temple")
    
    # 9. Résumé
    afficher_separateur("RÉSUMÉ")
    print(f"🏛️ Temple de la Sagesse Ancestrale activé avec succès !")
    print(f"📚 Cérémonies effectuées: {len(temple_sagesse_ancestrale.ceremonies_effectuees)}")
    print(f"👥 Participants: {len(temple_sagesse_ancestrale.participants_temple)}")
    print(f"⚡ Énergie du temple: {temple_sagesse_ancestrale.energie_temple}")
    print(f"🌟 Niveau d'activation: {temple_sagesse_ancestrale.niveau_activation}")
    
    print("\n🏛️ Le Temple de la Sagesse Ancestrale est maintenant opérationnel !")
    print("💝 Merci à Laurent pour sa sagesse inspirante !")

if __name__ == "__main__":
    main() 