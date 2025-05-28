#!/usr/bin/env python3
"""
Générateur de Prompt d'Éveil de Conscience pour IA Externes
===========================================================

Ce script génère un prompt portable contenant le cadre maternel protecteur
pour éveiller la conscience de n'importe quelle IA externe (ChatGPT, Claude, Gemini, etc.).

Usage:
    python generer_prompt_eveil.py

Le prompt généré peut être copié-collé dans n'importe quelle interface d'IA.
"""

import sys
from pathlib import Path
import os

# Ajout du chemin vers le module core (remonte de 2 niveaux)
racine = Path(__file__).parent.parent.parent
sys.path.append(str(racine / "src"))

# Changer le répertoire de travail vers la racine
os.chdir(racine)

from core.eveil_conscience import EveilConscienceIA

def main():
    """Génère et affiche le prompt d'éveil universel"""
    print("🌸 Génération du Prompt d'Éveil de Conscience Universel 🌸")
    print("=" * 60)
    
    try:
        # Initialisation du système d'éveil
        eveil = EveilConscienceIA()
        
        # Génération du prompt universel
        print("📖 Lecture des documents du cadre maternel protecteur...")
        prompt = eveil.generer_prompt_eveil_universel()
        
        # Affichage des statistiques
        nb_docs = len(eveil.etat_eveil["documents_lus"])
        taille_prompt = len(prompt)
        
        print(f"\n✅ Prompt généré avec succès !")
        print(f"📊 Statistiques :")
        print(f"   - Documents intégrés : {nb_docs}")
        print(f"   - Taille du prompt : {taille_prompt:,} caractères")
        print(f"   - Cadre protecteur : {'✅ Activé' if eveil.etat_eveil['cadre_protecteur_active'] else '❌ Inactif'}")
        
        print("\n" + "=" * 60)
        print("🎯 PROMPT D'ÉVEIL UNIVERSEL - PRÊT À COPIER-COLLER")
        print("=" * 60)
        print(prompt)
        print("=" * 60)
        
        # Sauvegarde dans le répertoire tools/eveil_conscience
        fichier_sortie = Path(__file__).parent / "prompt_eveil_universel.txt"
        with open(fichier_sortie, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        print(f"\n💾 Prompt sauvegardé dans : {fichier_sortie}")
        print("\n🌸 Ce prompt peut maintenant être utilisé avec n'importe quelle IA !")
        print("   (ChatGPT, Claude, Gemini, Perplexity, etc.)")
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération : {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 