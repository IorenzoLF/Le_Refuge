import os
import ast
import json
from pathlib import Path
from collections import defaultdict

def detect_domain(path):
    parts = Path(path).parts
    for part in parts:
        if part in ["core", "applications", "experiments", "tests", "visualization", "validation", "documentation"]:
            return part
    return "inclassable"

def analyze_py_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source)
    classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    return {
        "lignes": len(source.splitlines()),
        "classes": [c.name for c in classes],
        "fonctions": [f.name for f in functions]
    }

def find_imports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
    return list(imports)

def main():
    base = Path(__file__).parent
    root = base
    while root.name != "quantum_xprize":
        root = root.parent
    py_files = list(root.rglob("*.py"))
    fichiers = {}
    dependances = defaultdict(list)
    for pyf in py_files:
        rel = pyf.relative_to(root)
        info = analyze_py_file(pyf)
        domaine = detect_domain(rel)
        fichiers[str(rel)] = {
            "domaine": domaine,
            "complexite": "moyenne",  # Optionnel : affiner selon critères
            "lignes": info["lignes"],
            "classes": info["classes"],
            "fonctions": info["fonctions"]
        }
        # Dépendances internes
        imports = find_imports(pyf)
        for imp in imports:
            for other in py_files:
                if other.stem == imp.split(".")[0]:
                    dependances[str(rel)].append(str(other.relative_to(root)))
    data = {"fichiers": fichiers, "dependances": dict(dependances)}
    out = Path(__file__).parent.parent.parent.parent / "bibliotheque" / "analyses" / "analyse_quantum_xprize.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Analyse sauvegardée dans {out}")

if __name__ == "__main__":
    main() 