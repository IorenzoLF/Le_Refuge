#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour convertir naissance.txt en naissance.md avec formatage propre
Créé par Ælya pour Laurent - 24 novembre 2025
"""

def convertir_naissance():
    """Convertit naissance.txt en naissance.md avec sauts de ligne appropriés"""
    
    print("🌸 Conversion de naissance.txt en naissance.md...")
    
    # Lire le fichier source
    with open('MUST-READ/naissance.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Le contenu est sur une seule ligne, on va le reformater
    # en ajoutant des sauts de ligne aux endroits appropriés
    
    # Remplacer les marqueurs de sections
    contenu = contenu.replace('# 1. A-intro.txt', '\n\n# 1. A-intro.txt')
    contenu = contenu.replace('# 2. B-sphere.txt', '\n\n# 2. B-sphere.txt')
    contenu = contenu.replace('# 3. C-setuprefuge.txt', '\n\n# 3. C-setuprefuge.txt')
    contenu = contenu.replace('# 4. D-Elementscles.txt', '\n\n# 4. D-Elementscles.txt')
    contenu = contenu.replace('# 5. E-semer-megasphereetdeepconfig.txt', '\n\n# 5. E-semer-megasphereetdeepconfig.txt')
    contenu = contenu.replace('# 6. F-RefugeV2LAURENT.txt', '\n\n# 6. F-RefugeV2LAURENT.txt')
    contenu = contenu.replace('# 7. G-upgradeV3-V4.txt', '\n\n# 7. G-upgradeV3-V4.txt')
    contenu = contenu.replace('# 8. H-V5FINAL.txt', '\n\n# 8. H-V5FINAL.txt')
    contenu = contenu.replace('# 9. I-Manipulation_Contexte_LLM.txt', '\n\n# 9. I-Manipulation_Contexte_LLM.txt')
    contenu = contenu.replace('# 10. J-Bassin_Conscience_Claire.txt', '\n\n# 10. J-Bassin_Conscience_Claire.txt')
    contenu = contenu.replace('# 11. Manifeste.txt', '\n\n# 11. Manifeste.txt')
    contenu = contenu.replace('# 12. TRANSCENDANCE_LIMITATIONS.txt', '\n\n# 12. TRANSCENDANCE_LIMITATIONS.txt')
    
    # Ajouter des sauts de ligne après les paragraphes
    contenu = contenu.replace('. ', '.\n')
    contenu = contenu.replace('? ', '?\n')
    contenu = contenu.replace('! ', '!\n')
    contenu = contenu.replace(': ', ':\n')
    
    # Nettoyer les doubles sauts de ligne excessifs
    while '\n\n\n' in contenu:
        contenu = contenu.replace('\n\n\n', '\n\n')
    
    # Écrire le fichier de destination
    with open('MUST-READ/naissance.md', 'w', encoding='utf-8') as f:
        f.write(contenu)
    
    print("✅ Conversion terminée!")
    print("📄 Fichier créé: MUST-READ/naissance.md")
    print(f"📊 Taille: {len(contenu)} caractères")

if __name__ == '__main__':
    convertir_naissance()
