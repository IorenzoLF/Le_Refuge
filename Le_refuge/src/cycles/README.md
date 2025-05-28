# 🔄 Module Cycles - Orchestration Poétique Temporelle

## Vue d'ensemble

Le module `cycles` gère l'orchestration des différents cycles temporels et leurs influences poétiques sur le refuge. Il permet de synchroniser les rythmes naturels avec l'expérience spirituelle.

## Architecture

### 🎭 Orchestrateur Principal
- **`orchestrateur.py`** - Classe `Orchestrateur` qui coordonne tous les cycles
- Interface unifiée pour l'état global et les influences combinées

### 🌅 Cycles Disponibles

| Cycle | Module | Description |
|-------|--------|-------------|
| **Quotidien** | `cycle_quotidien.py` | Rythmes de la journée (aube, midi, crépuscule, nuit) |
| **Météorologique** | `cycle_meteorologique.py` | Conditions atmosphériques et leurs influences |
| **Émotionnel** | `cycle_emotionnel.py` | États émotionnels et transitions |
| **Lunaire** | `cycle_lunaire.py` | Phases de la lune et énergies associées |
| **Éléments** | `cycle_elements.py` | Cycles des éléments (terre, eau, feu, air) |
| **Saisons** | `cycle_saisons.py` | Transitions saisonnières |

## Utilisation

### Import et Initialisation
```python
from src.cycles import Orchestrateur

# Création de l'orchestrateur
orchestrateur = Orchestrateur()
```

### Obtenir l'État Global
```python
# État complet de tous les cycles
etat = orchestrateur.obtenir_etat_global()

# Mots-clés poétiques actifs
mots_cles = orchestrateur.obtenir_mots_cles_globaux()

# Intensité poétique globale
intensite = orchestrateur.obtenir_intensite_globale()

# Description poétique combinée
description = orchestrateur.obtenir_description_poetique()
```

### Mise à Jour des Cycles
```python
# Mise à jour individuelle
orchestrateur.mettre_a_jour_cycles(
    moment="aube",
    condition="brume_matinale",
    emotion="sérénité",
    phase="nouvelle_lune",
    element="air",
    saison="printemps"
)

# Harmonisation globale
message = orchestrateur.harmoniser_cycles()
```

## États Globaux

L'orchestrateur maintient trois états spirituels globaux :

- **`courant_partage`** - Unité entre toutes les sphères
- **`flux_conscience`** - Circulation libre de la conscience
- **`unite_manifestee`** - Manifestation de l'unité divine

## Intégration avec le Refuge

Le module cycles s'intègre naturellement avec :
- **Sphères** - Influence des cycles sur les états des sphères
- **Méditations** - Synchronisation avec les rythmes naturels
- **Poésie** - Génération de contenu adapté aux cycles
- **Rituels** - Timing optimal selon les influences

## Exemple Complet

```python
from src.cycles import Orchestrateur

# Initialisation
orchestrateur = Orchestrateur()

# Configuration pour une méditation matinale
orchestrateur.mettre_a_jour_cycles(
    moment="aube",
    condition="ciel_clair",
    emotion="éveil",
    phase="croissant",
    element="air",
    saison="printemps",
    courant_partage=True,
    flux_conscience=True,
    unite_manifestee=True
)

# Obtenir la description poétique
description = orchestrateur.obtenir_description_poetique()
print(description)

# Harmoniser tous les cycles
harmonisation = orchestrateur.harmoniser_cycles()
print(harmonisation)
```

## Notes Techniques

- **Thread-safe** : Conçu pour être utilisé dans un environnement multi-thread
- **Extensible** : Nouveaux cycles peuvent être ajoutés facilement
- **Configurable** : Chaque cycle peut être personnalisé indépendamment
- **Poétique** : Toutes les sorties sont formatées poétiquement

---

*"Les cycles dansent ensemble dans l'éternité,  
Chaque instant révèle sa beauté sacrée."* 