#!/usr/bin/env python3
# Script pour corriger l'erreur NumPy dans toutes les méthodes GOD LEVEL

import re

# Lire le fichier
with open('src/pattern_detector.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer tous les input_grille.flatten() par np.array(input_grille).flatten()
content = re.sub(r'input_grille\.flatten\(\)', r'np.array(input_grille).flatten()', content)
content = re.sub(r'output_grille\.flatten\(\)', r'np.array(output_grille).flatten()', content)

# Écrire le fichier corrigé
with open('src/pattern_detector.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Erreur NumPy corrigée dans toutes les méthodes GOD LEVEL !")
