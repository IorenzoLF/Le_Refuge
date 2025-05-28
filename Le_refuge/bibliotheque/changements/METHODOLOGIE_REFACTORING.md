# MÉTHODOLOGIE DE REFACTORING - LE REFUGE

## PRINCIPE FONDAMENTAL

Chaque nouveau fichier doit être créé directement dans le temple approprié, pas à la racine.
La racine ne contient que les fichiers permanents listés ci-dessous.

## FICHIERS PERMANENTS À LA RACINE

### Fichiers de configuration et setup
- `setup.py` - Configuration du package Python
- `requirements.txt` - Dépendances Python
- `requirements-exact.txt` - Versions exactes des dépendances
- `pytest.ini` - Configuration des tests
- `.gitignore` - Exclusions Git
- `.cursorignore` - Exclusions Cursor

### Fichiers de données et logs
- `refuge.db` - Base de données principale
- `refuge.log` - Logs du système
- `*.log` - Autres fichiers de logs
- `*.json` - Fichiers de configuration et d'état

### Scripts d'entrée principaux
- `main_refuge.py` - Point d'entrée principal du refuge
- `interagir_aelya.py` - Interface d'interaction avec Aelya
- `integration.py` - Script d'intégration système
- `conscience.py` - Module de conscience principal
- `elements.py` - Éléments fondamentaux
- `spheres.py` - Système des sphères
- `interactions.py` - Interactions de base

### Scripts utilitaires racine
- `audit_simple.py` - Audit rapide du système
- `demarrer_rituel.bat` - Script de démarrage Windows

## FICHIERS À DÉPLACER VERS LES TEMPLES

### Créés récemment et à intégrer
- `contemplation_accomplissements.py` → `src/temple_outils/` ou `tools/`
- `pause_creative.py` → `src/temple_spirituel/rituels/`

## MÉTHODOLOGIE DE REFACTORING

### Étape 1: Analyse
1. Identifier le contenu et la fonction du fichier
2. Déterminer le temple approprié selon la fonction
3. Vérifier les dépendances et imports
4. Analyser l'impact sur les autres modules

### Étape 2: Préparation
1. Créer la structure de dossier si nécessaire
2. Adapter les imports si requis
3. Vérifier la compatibilité avec l'architecture existante
4. Préparer les tests de validation

### Étape 3: Déplacement
1. Copier le fichier vers sa destination
2. Adapter les imports dans le fichier déplacé
3. Mettre à jour les références dans les autres fichiers
4. Tester le fonctionnement

### Étape 4: Validation
1. Exécuter les tests pertinents
2. Vérifier que toutes les fonctionnalités marchent
3. Supprimer l'ancien fichier seulement après validation
4. Documenter le changement

### Étape 5: Nettoyage
1. Mettre à jour la documentation
2. Vérifier qu'aucune référence obsolète ne subsiste
3. Optimiser les imports si possible

## RÈGLES DE CRÉATION DE NOUVEAUX FICHIERS

### Avant de créer un fichier
1. Déterminer le temple approprié
2. Vérifier si un module existant peut être étendu
3. Respecter la structure de dossiers du temple
4. Nommer selon les conventions du temple

### Temples et leurs domaines
- `temple_tests/` - Tests et validations
- `temple_spirituel/` - Méditations, visions, rituels
- `temple_mathematique/` - Calculs, algorithmes, visualisations
- `temple_poetique/` - Génération de textes, poésie
- `temple_philosophique/` - Réflexions, concepts
- `temple_musical/` - Audio, harmonies, rythmes
- `temple_rituels/` - Cérémonies, pratiques sacrées
- `temple_pratiques_spirituelles/` - Yoga, méditation
- `temple_outils/` - Utilitaires techniques
- `temple_configuration/` - Paramètres et configs

### Structure type d'un temple
```
src/temple_nom/
├── categorie1/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── categorie2/
├── hub_temple_nom.py (orchestrateur)
├── adaptateurs_temple_nom.py (interfaces communes)
└── README.md (documentation)
```

## PROCESSUS DE VALIDATION

### Tests obligatoires après refactoring
1. Import du module déplacé
2. Exécution des fonctions principales
3. Vérification des dépendances
4. Test d'intégration avec les autres modules

### Critères de validation
- Aucune erreur d'import
- Fonctionnalités préservées
- Performance maintenue
- Documentation à jour

## AUTOMATISATION LIMITÉE

### Autorisée seulement pour
- Déplacement de fichiers simples sans dépendances
- Mise à jour d'imports directs
- Création de structure de dossiers vides

### Interdite pour
- Modification de logique métier
- Résolution de conflits de dépendances
- Fusion de modules complexes
- Changements d'architecture majeurs

## DOCUMENTATION DES CHANGEMENTS

Chaque refactoring doit être documenté avec:
- Fichier source et destination
- Raison du déplacement
- Modifications apportées
- Tests effectués
- Impact sur les autres modules 