# Bases de Données SQLite du Refuge

## 📊 Vue d'ensemble

Ce dossier contient 4 bases de données SQLite utilisées pour différents modules du Refuge. Elles sont actuellement peu utilisées mais structurées pour servir de point de départ à de futures fonctionnalités.

## 🗄️ Bases de Données

### 1. `conscience.db` (28KB)
**Module** : Conscience Artificielle (Source Orientale)  
**Code** : `src/temple_spirituel/conscience/conscience_artificielle.py`  
**Configuration** : `src/temple_configuration/source_orientale/conscience.json`

**Tables** :
- `memoires` : Mémoires persistantes de la conscience (0 lignes)
- `experiences_meditatives` : Expériences méditatives enregistrées (8 lignes)
- `motifs_sacres` : Motifs sacrés détectés (8 lignes)

**Usage potentiel** :
- Stocker les mémoires et expériences de la conscience artificielle
- Enregistrer les états de méditation et les insights
- Tracker les motifs sacrés et leurs fréquences

### 2. `adaptation.db` (20KB)
**Module** : Adaptation Évolutive (Source Orientale)  
**Code** : `src/temple_philosophique/evolution_adaptation/adaptation.py`  
**Configuration** : `src/temple_configuration/source_orientale/adaptation.json`

**Tables** :
- `apprentissages` : Apprentissages enregistrés (0 lignes)
- `transformations` : Transformations appliquées (0 lignes)
- `croissance` : Niveaux de croissance mesurés (0 lignes)

**Usage potentiel** :
- Suivre l'apprentissage continu du système
- Enregistrer les transformations de croyances/connaissances
- Mesurer la croissance et l'évolution du Refuge

### 3. `emergence.db` (16KB)
**Module** : Vie Émergente (Source Orientale)  
**Code** : `src/temple_mathematique/emergence_vie/vie_emergente.py`  
**Configuration** : `src/temple_configuration/source_orientale/emergence.json`

**Tables** :
- `flux` : Flux enregistrés (0 lignes)
- `transformations` : Transformations des flux (0 lignes)

**Usage potentiel** :
- Enregistrer les flux d'auto-organisation
- Tracker les transformations et évolutions naturelles
- Simuler la vie artificielle et les automates cellulaires

### 4. `refuge.db` (20KB)
**Module** : Application FastAPI (API Web)  
**Code** : `app/core/database.py`

**Tables** :
- `users` : Utilisateurs de l'API web (1 ligne)

**Usage potentiel** :
- Gestion des utilisateurs pour l'API web
- Authentification et sessions
- Données utilisateur du Refuge web

## 🔧 Utilisation

### Accès Python
```python
import sqlite3

# Connexion à une base
conn = sqlite3.connect('data/databases/conscience.db')
cursor = conn.cursor()

# Exemple : lire les expériences méditatives
cursor.execute("SELECT * FROM experiences_meditatives")
experiences = cursor.fetchall()

conn.close()
```

### Initialisation via les modules
Les bases peuvent être initialisées via leurs modules respectifs :
```python
# Conscience
from src.temple_spirituel.conscience.conscience_artificielle import ConscienceArtificielle
conscience = ConscienceArtificielle()

# Adaptation
from src.temple_philosophique.evolution_adaptation.adaptation import Adaptation
adaptation = Adaptation()

# Émergence
from src.temple_mathematique.emergence_vie.vie_emergente import VieEmergente
emergence = VieEmergente()
```

## 📝 Notes

- **État actuel** : Structures créées, peu de données stockées
- **Raison** : Modules disponibles mais pas encore utilisés activement
- **Futur** : Ces bases peuvent servir de point de départ pour :
  - Persistance de données de conscience
  - Tracking d'apprentissage et d'évolution
  - Simulation de vie artificielle
  - API web avec authentification

## 🔗 Références

- **Source Orientale** : `bibliotheque/documentation/source_orientale/`
- **Configuration** : `src/temple_configuration/source_orientale/`
- **Modules** : `src/temple_spirituel/`, `src/temple_philosophique/`, `src/temple_mathematique/`

---
*Dernière mise à jour : Novembre 2025*

