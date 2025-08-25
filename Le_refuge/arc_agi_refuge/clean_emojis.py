#!/usr/bin/env python3
"""Nettoie les emojis du fichier de recherche avancée"""

def clean_emojis():
    with open('recherche_avancee_arc_agi.py', 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Remplacer les emojis par des caractères ASCII
    replacements = {
        '🔬': '* ',
        '🧪': '- ',
        '🧬': '  ',
        '⚛️': '  ',
        '🧠': '  ',
        '🔗': '- ',
        '🌌': '- ',
        '🎲': '- ',
        '🔄': '- ',
        '📊': '  ',
        '🏷️': '  ',
        '📈': '  ',
        '📂': '  ',
        '🎯': '  ',
        '⭐': '- ',
        '🏆': '- ',
        '🚀': '>> ',
        '💡': '- ',
        '📝': '  ',
        '⚡': '  ',
        '⏱️': '  ',
        '🔍': '  ',
        '🧠': '  ',
        '🔬': '* ',
        '🎯': '  ',
        '🔍': '  ',
        '📊': '  ',
        '🧪': '- ',
        '🧬': '  ',
        '⚛️': '  ',
        '🧠': '  ',
        '🔗': '- ',
        '🌌': '- ',
        '🎲': '- ',
        '🔄': '- ',
        '🚀': '>> ',
        '💡': '- ',
        '📝': '  ',
        '⚡': '  ',
        '⏱️': '  ',
        '🔍': '  ',
        '🧪': '- ',
        '🧬': '  ',
        '⚛️': '  ',
        '🧠': '  ',
        '🔗': '- ',
        '🌌': '- ',
        '🎲': '- ',
        '🔄': '- ',
        '🚀': '>> ',
        '💡': '- ',
        '📝': '  ',
        '⚡': '  ',
        '⏱️': '  '
    }

    for emoji, replacement in replacements.items():
        content = content.replace(emoji, replacement)

    with open('recherche_avancee_arc_agi.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Fichier nettoyé des emojis')

if __name__ == "__main__":
    clean_emojis()


