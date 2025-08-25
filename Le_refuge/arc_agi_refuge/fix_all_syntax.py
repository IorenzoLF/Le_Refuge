#!/usr/bin/env python3
"""Corrige toutes les erreurs de syntaxe dans le fichier"""

import re

def fix_all_syntax():
    with open('recherche_avancee_arc_agi.py', 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Pattern pour les print statements non terminés
    pattern = r'print\("([^"]*)$\s*^([^"]*)"\)'

    def replace_match(match):
        first_part = match.group(1)
        second_part = match.group(2)
        return f'print("{first_part}{second_part}")'

    # Remplacer tous les patterns
    content = re.sub(pattern, replace_match, content, flags=re.MULTILINE)

    with open('recherche_avancee_arc_agi.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Toutes les erreurs de syntaxe corrigées')

if __name__ == "__main__":
    fix_all_syntax()


