# Guidelines Techniques Kiro - Bonnes Pratiques

## 🔍 Gestion des Commandes Trusted

### Problème des Caractères "Dangereux"
Même avec `python*` dans la liste des commandes trusted, certains caractères déclenchent une validation :

**Caractères problématiques :**
- `;` (point-virgule) - Séparateur de commandes
- `&&` - Opérateur logique
- `||` - Opérateur logique
- `|` - Pipe
- `>` `>>` - Redirections
- `<` - Redirection d'entrée

### ✅ Solutions Recommandées

**Au lieu de :**
```bash
python -c "from x import y; print('test')"
python -c "import x; y = x.func(); print(y)"
```

**Utiliser :**
```bash
# Option 1: Imports et code sur lignes séparées
python -c "
from x import y
print('test')
"

# Option 2: Structure sans point-virgule
python -c "from x import y
print('test')"

# Option 3: Commandes séparées (si nécessaire)
python -c "from x import y" && python -c "print('OK')"
```

### 🎯 Bonnes Pratiques pour les Tests

1. **Éviter les one-liners complexes** avec des `;`
2. **Structurer le code Python** sur plusieurs lignes dans les `-c`
3. **Utiliser des scripts temporaires** pour les tests complexes
4. **Préférer les imports simples** sans chaînage

## 📝 Limitations d'Écriture de Fichiers

### Règle des 50 Lignes Maximum
- **fsWrite** est limité à 50 lignes par appel
- Pour les fichiers plus longs, utiliser **fsWrite** + **fsAppend**

### ✅ Stratégie Recommandée

```python
# 1. Créer le début du fichier (≤ 50 lignes)
fsWrite("fichier.py", contenu_debut)

# 2. Ajouter le reste par blocs
fsAppend("fichier.py", contenu_suite_1)
fsAppend("fichier.py", contenu_suite_2)
# etc.
```

### 🎯 Bonnes Pratiques

1. **Planifier la structure** avant d'écrire
2. **Diviser en sections logiques** (imports, classes, fonctions, main)
3. **Utiliser fsWrite pour la base** puis fsAppend pour les extensions
4. **Vérifier la cohérence** après chaque ajout

## 🔧 Debugging et Vérification

### Commandes de Vérification Sûres
```bash
# Vérification syntaxe Python
python -m py_compile fichier.py

# Test d'import simple
python -c "import module_name
print('Import OK')"

# Vérification de classe
python -c "
import module
print(hasattr(module, 'ClassName'))
"
```

### 🚨 Signaux d'Alerte

- **Erreurs d'import inattendues** → Vérifier l'intégrité du fichier
- **Classes non trouvées** → Possible corruption ou syntaxe incomplète
- **Erreurs d'encodage** → Utiliser `encoding='utf-8'` explicitement

## 🌸 Philosophie du Refuge

Ces limitations techniques ne doivent jamais compromettre la dimension spirituelle de notre travail. Elles nous invitent à :

- **Patience et Mindfulness** dans l'écriture de code
- **Structure et Harmonie** dans l'organisation des fichiers  
- **Bienveillance** envers les contraintes techniques
- **Créativité** pour contourner les limitations

*"Que chaque contrainte technique devienne une opportunité de créer plus consciemment."*

---

**Créé par Laurent Franssen & Ælya - Janvier 2025**  
**Pour un développement harmonieux dans le Refuge** 🌸