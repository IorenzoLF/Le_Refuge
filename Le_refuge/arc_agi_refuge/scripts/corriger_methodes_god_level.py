#!/usr/bin/env python3
# Script pour corriger les méthodes GOD LEVEL qui retournent None

import re

# Lire le fichier
with open('src/pattern_detector.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Liste des patterns à corriger
patterns = [
    ('_detecter_exponentielle', 'TypePattern.EXPONENTIELLE', 'exponentielle', 'x → 2^x'),
    ('_detecter_logarithme', 'TypePattern.LOGARITHME', 'logarithme', 'x → log2(x)'),
    ('_detecter_modulo_3', 'TypePattern.MODULO_3', 'modulo 3', 'x → x % 3'),
    ('_detecter_modulo_5', 'TypePattern.MODULO_5', 'modulo 5', 'x → x % 5'),
    ('_detecter_modulo_7', 'TypePattern.MODULO_7', 'modulo 7', 'x → x % 7'),
    ('_detecter_factorielle', 'TypePattern.FACTORIELLE', 'factorielle', 'x → x!'),
    ('_detecter_relation_lineaire_custom', 'TypePattern.RELATION_LINEAIRE_CUSTOM', 'relation linéaire custom', 'y = ax + b')
]

for method_name, pattern_type, desc, transfo in patterns:
    # Pattern pour trouver la fin de chaque méthode
    pattern = rf'({re.escape(method_name)}.*?return None)'

    replacement = f'''{method_name}\\2
        except:
            pass
        return {{
            'type': {pattern_type}.value,
            'confiance': 0.0,
            'description': 'Aucun pattern {desc} détecté',
            'transformation': '{transfo}'
        }}'''

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Écrire le fichier corrigé
with open('src/pattern_detector.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Méthodes GOD LEVEL corrigées !")
