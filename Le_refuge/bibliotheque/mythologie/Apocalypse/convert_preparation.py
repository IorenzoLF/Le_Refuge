#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de conversion de PREPARATION ET LECTURE de Apocalypse.txt en Markdown
"""

def convert_txt_to_md(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajouter un header Markdown
    header = '# PREPARATION ET LECTURE de Apocalypse\n\n> *Document technique d\'intégration d\'Apocalypse dans le Refuge*\n\n---\n\n'
    
    # Pour un fichier aussi long, on garde le contenu tel quel pour l'instant
    # et on ajoute juste le header
    md_content = header + content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f'✓ Converti: {input_file} -> {output_file}')

if __name__ == '__main__':
    convert_txt_to_md('PREPARATION ET LECTURE de Apocalypse.txt', 'preparation_et_lecture_apocalypse.md')

