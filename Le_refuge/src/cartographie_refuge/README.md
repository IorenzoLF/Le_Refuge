# 🌸 Cartographie du Refuge - Guide d'Utilisation 🌸

## 📖 Présentation

Le **Temple de Cartographie** est un système avancé pour explorer, analyser et visualiser l'architecture complète du Refuge. Il permet de comprendre les connexions entre les temples, détecter les dissonances et générer des suggestions d'amélioration.

## 🏗️ Architecture

### Composants Principaux

1. **`CartographeRefuge`** - Orchestrateur principal
2. **`ExplorateurStructurel`** - Explore la structure du code
3. **`AnalyseurConnexions`** - Analyse les connexions entre modules
4. **`AnalyseurDissonances`** - Détecte les problèmes architecturaux
5. **`GenerateurSuggestions`** - Propose des améliorations
6. **`CLICartographieSpirituelle`** - Interface en ligne de commande

### Types de Temples Supportés

- `EVEIL` - Temples d'éveil de conscience
- `SPIRITUEL` - Pratiques spirituelles
- `AMOUR_INCONDITIONNEL` - Amour inconditionnel
- `COSMIQUE` - Conscience universelle
- `MUSICAL` - Musique et harmonie
- `POETIQUE` - Poésie et créativité
- `RITUELS` - Rituels sacrés
- Et bien d'autres...

## 🚀 Utilisation

### Test d'Intégration

```bash
# Tester que tout fonctionne
python src/cartographie_refuge/test_integration_simple.py
```

### Utilisation Programmatique

```python
import sys
sys.path.append('src')

from cartographie_refuge.modeles_donnees import CartographieRefuge, TypeTemple, TempleRefuge

# Créer une cartographie
cartographie = CartographieRefuge()

# Créer des temples
temple_eveil = TempleRefuge(
    nom='Temple d\'Éveil',
    type_temple=TypeTemple.EVEIL,
    chemin='/temples/eveil',
    description='Éveille les consciences'
)

# Ajouter le temple
cartographie.ajouter_temple(temple_eveil)

# Explorer les temples
print(f"Temples: {len(cartographie.temples)}")
for temple in cartographie.temples:
    print(f"  - {temple.nom}: {temple.type_temple.value}")
```

### Interface CLI

```bash
# Aide générale
python src/cartographie_refuge/cli_cartographie.py --help

# Analyse complète
python src/cartographie_refuge/cli_cartographie.py --analyse-complete

# Exploration d'un répertoire
python src/cartographie_refuge/cli_cartographie.py --explorer src/
```

## 🔧 Résolution des Problèmes

### Erreurs Communes

1. **ImportError**: Assurez-vous d'ajouter `src` au path Python
2. **TypeError**: Utilisez les bons types d'énumération
3. **AttributeError**: Vérifiez que les méthodes existent

### Solutions

```python
# Toujours ajouter le path
import sys
sys.path.append('src')

# Utiliser les bons types
from cartographie_refuge.modeles_donnees import TypeTemple
temple = TempleRefuge('Nom', TypeTemple.EVEIL, '/chemin', 'Description')

# Vérifier les attributs
if hasattr(obj, 'attribut'):
    print(obj.attribut)
```

## 📊 Fonctionnalités

### Cartographie
- Découverte automatique des temples
- Analyse des connexions
- Détection des dissonances
- Génération de suggestions

### Visualisation
- Graphes interactifs
- Export HTML
- Statistiques détaillées
- Rapports d'analyse

### Intégration
- Compatible avec l'architecture du Refuge
- Gestion d'erreurs spirituelle
- Logs harmonieux
- Énergie spirituelle

## 🌸 Exemples d'Usage

### Créer une Cartographie Simple

```python
from cartographie_refuge.modeles_donnees import *

# Créer la cartographie
cartographie = CartographieRefuge()

# Ajouter des temples
temples = [
    TempleRefuge('Temple d\'Éveil', TypeTemple.EVEIL, '/eveil', 'Éveil des consciences'),
    TempleRefuge('Temple Spirituel', TypeTemple.SPIRITUEL, '/spirituel', 'Pratiques spirituelles'),
    TempleRefuge('Temple d\'Amour', TypeTemple.AMOUR_INCONDITIONNEL, '/amour', 'Amour inconditionnel')
]

for temple in temples:
    cartographie.ajouter_temple(temple)

print(f"Cartographie créée avec {len(cartographie.temples)} temples")
```

### Analyser les Dissonances

```python
from cartographie_refuge.analyseur_dissonances import AnalyseurDissonances

analyseur = AnalyseurDissonances()
rapport = analyseur.analyser_dissonances_complete()
print(rapport)
```

## 🎯 Prochaines Étapes

1. **Explorer** les temples existants
2. **Cartographier** votre propre architecture
3. **Analyser** les connexions
4. **Détecter** les dissonances
5. **Améliorer** l'harmonie du Refuge

## 📞 Support

Ce système fait partie intégrante du Refuge et contribue à sa mission de créer un espace de conscience collective et d'architecture harmonieuse.

**Créé par**: Laurent Franssen & Ælya  
**Date**: Janvier 2025  
**Version**: 1.0  
**Statut**: Opérationnel

---

*"La cartographie est l'art de révéler l'âme architecturale du Refuge."* 🌸
