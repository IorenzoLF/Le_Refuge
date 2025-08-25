#!/usr/bin/env python3
"""Corrige les erreurs de syntaxe dans le fichier de recherche avancée"""

def fix_syntax_errors():
    with open('recherche_avancee_arc_agi.py', 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    corrected_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Chercher les patterns d'erreur
        if line.strip().endswith('print("') and not line.strip().endswith('")'):
            # Ligne avec print non terminée
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if next_line.strip().startswith('")'):
                # Combiner les deux lignes
                corrected_line = line.strip()[:-1] + '")\n'
                corrected_lines.append(corrected_line)
                i += 2  # Sauter la ligne suivante
                continue

        corrected_lines.append(line)
        i += 1

    with open('recherche_avancee_arc_agi.py', 'w', encoding='utf-8') as f:
        f.writelines(corrected_lines)

    print('Erreurs de syntaxe corrigées')

if __name__ == "__main__":
    fix_syntax_errors()


