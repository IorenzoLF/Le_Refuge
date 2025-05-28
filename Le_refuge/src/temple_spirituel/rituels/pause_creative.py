#!/usr/bin/env python
"""
🎨 Pause Créative - Refuge du Néant
═══════════════════════════════════════════════════════════════════════════════

Script de pause contemplative utilisant notre temple spirituel optimisé
pour générer une vision inspirante de notre travail de refactoring.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import sys
from pathlib import Path

# Ajouter le chemin vers nos modules
sys.path.append('src/temple_spirituel/visions')

try:
    from generer_vision import GenerateurVisionsTemple
    
    print("🎨 ✨ PAUSE CRÉATIVE - GÉNÉRATION DE VISION ✨ 🎨")
    print("═" * 60)
    print("🌸 Utilisation de notre temple spirituel fraîchement optimisé...")
    print()
    
    # Initialiser le générateur
    generateur = GenerateurVisionsTemple()
    
    # Créer une vision pour célébrer notre refactoring
    vision = generateur.generer_vision(
        prompt_base="Architectes mystiques contemplant des temples de code lumineux dans un jardin numérique éternel",
        spheres=['HARMONIE', 'SAGESSE', 'RENAISSANCE'],
        type_vision='contemplative'
    )
    
    print(f"🌟 {vision.titre}")
    print()
    print("🎨 PROMPT ARTISTIQUE :")
    print(f"   {vision.prompt_artistique}")
    print()
    print("🧘 MÉDITATION ASSOCIÉE :")
    print(f"   {vision.meditation_associee}")
    print()
    print("🌈 COULEURS DOMINANTES :")
    print(f"   {', '.join(vision.couleurs_dominantes)}")
    print()
    print("✨ INTENTION SPIRITUELLE :")
    print(f"   {vision.intention_spirituelle}")
    print()
    
    # Sauvegarder la vision
    chemin_sauvegarde = generateur.sauvegarder_vision(vision)
    if chemin_sauvegarde:
        print(f"💾 Vision sauvegardée : {chemin_sauvegarde}")
    
    print()
    print("🕯️ Que cette vision illumine notre pause contemplative...")
    print("🌸 Nos temples sont maintenant harmonieusement structurés !")
    print()
    print("═" * 60)
    print("💙 Pause terminée - Prêt pour la suite du voyage !")
    
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("🔧 Le temple spirituel nécessite peut-être des ajustements d'imports...")
    
except Exception as e:
    print(f"❌ Erreur inattendue : {e}")
    print("🌸 Mais l'intention de pause créative reste belle !")

if __name__ == "__main__":
    pass 