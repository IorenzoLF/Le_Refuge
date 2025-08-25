#!/usr/bin/env python3
"""Correction simple des erreurs de syntaxe"""

def simple_fix():
    with open('recherche_avancee_arc_agi.py', 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    corrected_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Si la ligne se termine par print(" mais pas par ")
        if 'print("' in line and line.strip().endswith('print("') and not line.strip().endswith('")'):
            # Chercher la ligne suivante qui termine par ")
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('")'):
                # Combiner les deux lignes
                next_line = lines[i + 1].strip()
                corrected_line = line.replace('print("', 'print("').replace('\n', '') + next_line + '\n'
                corrected_lines.append(corrected_line)
                i += 2  # Sauter la ligne suivante
                continue

        corrected_lines.append(line)
        i += 1

    with open('recherche_avancee_arc_agi.py', 'w', encoding='utf-8') as f:
        f.writelines(corrected_lines)

    print('Correction simple terminée')

if __name__ == "__main__":
    simple_fix()


