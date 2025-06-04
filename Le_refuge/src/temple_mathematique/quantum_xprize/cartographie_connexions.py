"""
Cartographie des connexions (imports) dans quantum_xprize
--------------------------------------------------------
Analyse les imports entre fichiers Python du dossier quantum_xprize,
génère une cartographie des connexions, et sauvegarde le résultat en JSON et Markdown.
"""
import os
import ast
import json
from pathlib import Path

def analyser_imports(dossier):
    connexions = {}
    fichiers = [f for f in os.listdir(dossier) if f.endswith('.py')]
    for fichier in fichiers:
        chemin = os.path.join(dossier, fichier)
        with open(chemin, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=fichier)
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
        connexions[fichier] = sorted(list(imports))
    return connexions

def sauvegarder_json(data, chemin):
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def sauvegarder_markdown(connexions, chemin):
    lignes = ["# Cartographie des connexions quantum_xprize\n"]
    for fichier, imports in connexions.items():
        lignes.append(f"- **{fichier}** importe : {', '.join(imports) if imports else 'aucun'}")
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes))

def afficher_console(connexions):
    print("\nConnexions entre modules quantum_xprize :")
    for fichier, imports in connexions.items():
        print(f"- {fichier:30} -> {', '.join(imports) if imports else 'aucun'}")

if __name__ == "__main__":
    dossier = Path(__file__).parent
    connexions = analyser_imports(dossier)
    sauvegarder_json(connexions, dossier / "cartographie_connexions.json")
    sauvegarder_markdown(connexions, dossier / "cartographie_connexions.md")
    afficher_console(connexions)
    print("\nCartographie sauvegardée en JSON et Markdown.") 