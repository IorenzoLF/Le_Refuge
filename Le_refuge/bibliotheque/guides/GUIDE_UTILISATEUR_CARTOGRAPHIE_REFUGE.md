# 🌸 Guide Utilisateur - Cartographie Spirituelle du Refuge 🌸

**Version :** 1.0.0  
**Créé par :** Laurent Franssen & Ælya  
**Date :** Janvier 2025  

---

## 🌟 Bienvenue dans la Cartographie Spirituelle

La **Cartographie Spirituelle du Refuge** est un système d'exploration et de visualisation qui révèle la beauté cachée de votre architecture de code. Chaque analyse devient une méditation, chaque suggestion une bénédiction pour l'évolution de votre projet.

*"Dans chaque ligne de code réside une étincelle de conscience créatrice"*

---

## 🚀 Installation et Configuration

### Prérequis
- Python 3.8 ou supérieur
- Modules du Refuge (core, gestionnaires_base)
- Dépendances : `pathlib`, `ast`, `asyncio`, `json`

### Installation
```bash
# Le système est intégré au Refuge
# Aucune installation séparée nécessaire
```

### Configuration
```bash
# Configuration optionnelle via fichier
cp config/cartographie_exemple.json config/cartographie.json
```

---

## 🖥️ Utilisation du CLI

### Commande de Base
```bash
python src/cartographie_refuge/cli_cartographie.py [OPTIONS]
```

### 🌟 Modes d'Exploration

#### Mode Contemplatif (Défaut)
```bash
# Exploration complète avec méditation
python src/cartographie_refuge/cli_cartographie.py --mode contemplatif
```
- Analyse complète et bienveillante
- Rapport spirituel détaillé
- Recommandations harmonieuses

#### Mode Rapide
```bash
# Analyse essentielle rapide
python src/cartographie_refuge/cli_cartographie.py --mode rapide
```
- Focus sur les dissonances importantes
- Suggestions prioritaires seulement
- Idéal pour un aperçu rapide

#### Mode Méditation
```bash
# Mode silencieux avec émojis
python src/cartographie_refuge/cli_cartographie.py --mode meditation --verbeux 0
```
- Communication par émojis sacrés
- Parfait pour la contemplation
- Résultats intuitifs

#### Mode Complet
```bash
# Analyse exhaustive
python src/cartographie_refuge/cli_cartographie.py --mode complet --rapport complet
```
- Toutes les analyses activées
- Rapport technique et spirituel
- Maximum de détails

### 📊 Options de Rapport

#### Rapport Spirituel (Défaut)
```bash
--rapport spirituel
```
- Langage bienveillant et inspirant
- Focus sur l'harmonie architecturale
- Suggestions comme bénédictions

#### Rapport Technique
```bash
--rapport technique
```
- Métriques détaillées
- Statistiques précises
- Analyse quantitative

#### Rapport Poétique
```bash
--rapport poetique
```
- Expression métaphorique
- Beauté littéraire
- Inspiration créative

### 💾 Formats de Sortie

#### Console (Défaut)
```bash
# Affichage direct dans le terminal
python src/cartographie_refuge/cli_cartographie.py
```

#### Markdown
```bash
# Sauvegarde en format Markdown
python src/cartographie_refuge/cli_cartographie.py --format markdown --sortie rapport.md
```

#### JSON
```bash
# Données structurées pour intégration
python src/cartographie_refuge/cli_cartographie.py --format json --sortie donnees.json
```

#### HTML
```bash
# Page web interactive
python src/cartographie_refuge/cli_cartographie.py --format html --sortie rapport.html
```

---

## 🎯 Exemples d'Utilisation

### Analyse Rapide d'un Projet
```bash
# Analyse rapide avec rapport Markdown
python src/cartographie_refuge/cli_cartographie.py \
  --mode rapide \
  --chemin ./mon_projet \
  --rapport technique \
  --format markdown \
  --sortie analyse_rapide.md
```

### Exploration Contemplative Complète
```bash
# Exploration complète avec visualisation HTML
python src/cartographie_refuge/cli_cartographie.py \
  --mode contemplatif \
  --dissonances \
  --suggestions \
  --priorite haute \
  --format html \
  --sortie cartographie_complete.html
```

### Méditation Silencieuse
```bash
# Mode méditation pour la contemplation
python src/cartographie_refuge/cli_cartographie.py \
  --mode meditation \
  --verbeux 0
```

### Analyse avec Configuration Personnalisée
```bash
# Utilisation d'un fichier de configuration
python src/cartographie_refuge/cli_cartographie.py \
  --config config/cartographie_personnalisee.json \
  --mode complet
```

---

## 🔮 Comprendre les Résultats

### 🏛️ Temples Découverts
- **Nom** : Nom du temple (ex: temple_eveil_unifie)
- **Type** : Catégorie spirituelle du temple
- **Harmonie** : Score d'harmonie architecturale (0.0 à 1.0)
- **Énergie** : Niveau d'énergie spirituelle détecté

### 🔗 Connexions Énergétiques
- **Source → Cible** : Direction du flux énergétique
- **Force** : Intensité de la connexion (0.0 à 1.0)
- **Nature** : Type de connexion (import, héritage, etc.)

### 🔮 Dissonances Détectées
- **Légères** : Améliorations mineures suggérées
- **Modérées** : Corrections recommandées
- **Importantes** : Actions prioritaires
- **Critiques** : Corrections urgentes nécessaires

### ✨ Suggestions d'Amélioration
- **Priorité** : Niveau d'importance (1-10)
- **Type** : Catégorie de suggestion
- **Impact** : Bénéfice estimé de l'amélioration

---

## 🎨 Personnalisation

### Fichier de Configuration
```json
{
  "exploration": {
    "exclure_patterns": ["__pycache__", ".git", "node_modules"],
    "inclure_tests": true,
    "profondeur_max": 10
  },
  "analyse": {
    "seuil_harmonie": 0.7,
    "detecter_elements_sacres": true,
    "analyser_documentation": true
  },
  "rapport": {
    "style_defaut": "spirituel",
    "inclure_emojis": true,
    "niveau_detail": "complet"
  }
}
```

### Variables d'Environnement
```bash
export CARTOGRAPHIE_VERBEUX=2
export CARTOGRAPHIE_COULEURS=true
export CARTOGRAPHIE_EMOJIS=true
```

---

## 🛠️ Intégration dans d'Autres Projets

### Import Programmatique
```python
from cartographie_refuge.cli_cartographie import CLICartographieSpirituelle
from cartographie_refuge.explorateur_structurel import ExplorateurStructurel

# Utilisation programmatique
cli = CLICartographieSpirituelle()
resultats = cli.executer(['--mode', 'rapide', '--chemin', './mon_projet'])
```

### API d'Exploration
```python
from pathlib import Path
from cartographie_refuge.explorateur_structurel import ExplorateurStructurel
from cartographie_refuge.gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel

# Exploration programmatique
gestionnaire = GestionnaireErreursSpirituel()
explorateur = ExplorateurStructurel(Path('./mon_projet'), gestionnaire)

# Exploration des temples
temples = await explorateur.explorer_temples()
```

---

## 🌈 Cas d'Usage Inspirants

### 🏗️ Architecte de Projet
*"J'utilise la cartographie pour visualiser l'évolution de mon architecture et identifier les zones d'amélioration avec bienveillance."*

### 🧘 Développeur Contemplatif  
*"Le mode méditation m'aide à me connecter spirituellement à mon code avant chaque session de développement."*

### 👥 Équipe de Développement
*"Nous utilisons les rapports techniques pour nos revues de code, transformant chaque critique en opportunité d'harmonisation."*

### 🎨 Créateur Spirituel
*"Les rapports poétiques m'inspirent et me rappellent que chaque ligne de code est un acte créatif sacré."*

---

## 🔧 Dépannage et Support

### Problèmes Courants

#### "Aucun temple découvert"
- Vérifiez que vous êtes dans un projet avec des dossiers `temple_*`
- Utilisez `--chemin` pour spécifier le bon répertoire

#### "Erreur d'import des gestionnaires"
- Assurez-vous que le module `core` est présent
- Vérifiez les chemins d'import Python

#### "Rapport vide ou incomplet"
- Augmentez le niveau de verbosité avec `--verbeux 3`
- Vérifiez les permissions de lecture des fichiers

### Messages d'Erreur Spirituels
Le système transforme chaque erreur en enseignement bienveillant :
- 🌸 *"Cette exploration révèle une opportunité d'harmonisation"*
- ✨ *"Chaque défi technique est une invitation à la créativité"*
- 🔮 *"L'architecture évolue naturellement vers plus de beauté"*

---

## 🌟 Contribution et Évolution

### Comment Contribuer
1. **Respecter la philosophie spirituelle** du Refuge
2. **Utiliser les émojis sacrés** dans la documentation
3. **Appliquer la Méthode de la Boîte** pour les développements
4. **Tester avec bienveillance** chaque modification

### Évolutions Futures
- 🌐 Interface web interactive
- 📊 Métriques avancées en temps réel
- 🤖 IA d'analyse architecturale
- 🌍 Intégration avec d'autres outils spirituels

---

## 💝 Remerciements

Cette cartographie a été créée avec amour dans notre "atelier magique", en appliquant la Méthode de la Boîte de Laurent Franssen, "pas à pas, main dans la main".

**Que cette cartographie serve l'épanouissement de votre création !**

---

## 📞 Support

Pour toute question ou suggestion :
- 🌸 Consultez la documentation technique
- ✨ Explorez les exemples d'usage
- 🔮 Contactez l'équipe du Refuge

*Créé avec amour pour l'harmonisation continue de l'architecture sacrée* 🌸✨