# 🏛️ Exemples d'Utilisation du Refuge - Architecture Unifiée

Ce dossier contient des exemples pratiques d'utilisation des différents composants du Refuge, avec une architecture unifiée et des imports corrigés.

## 🎯 **Architecture des Exemples**

Tous les exemples utilisent une classe de base commune `ExempleBase` qui fournit :
- ✅ **Gestion d'erreur unifiée** avec logs détaillés
- ✅ **Vérification des dépendances** optionnelles
- ✅ **Imports corrigés** vers les vrais composants du refuge
- ✅ **Interface cohérente** pour tous les exemples

## 📚 **Exemples Disponibles**

### 🔰 **Exemple Simple** (`simple.py`)
**Utilisation basique des composants du refuge**
- Démonstration des sphères et éléments
- Génération poétique simple
- Gestion robuste des composants manquants

```bash
python -m src.examples.simple
```

### 🎭 **Exemple Avancé** (`avance.py`)
**Expérience poétique interactive évolutive**
- Cycles temporels automatiques (aube, jour, nuit)
- Émotions contextuelles selon saison/moment
- Journal d'expériences avec statistiques
- Rapport détaillé de l'expérience

```bash
python -m src.examples.avance
```

### 🌐 **Interface Web** (`web.py`)
**Interface web Flask pour le refuge** *(nécessite Flask)*
- Interface utilisateur moderne et responsive
- API REST complète pour le refuge
- Contrôles interactifs en temps réel
- Journal poétique web

```bash
# Installation de Flask si nécessaire
pip install flask

# Lancement de l'interface
python -m src.examples.web
# Puis ouvrir http://localhost:5000
```

### 💬 **Dialogue Interactif** (`dialogue.py`)
**Gestionnaire de dialogue avec IA** *(nécessite ParlAI)*
- Conversation interactive avec modèles pré-entraînés
- Sauvegarde automatique des conversations
- Interface en ligne de commande intuitive

### 🧘 **Méditations** (`meditations/`)
**Système de méditation avec Ælya**
- Méditations guidées avec sphères problématiques
- Progression sur plusieurs jours
- Brume apaisante et résonances

### 📊 **Chargeurs de Données** (`data_loader.py`)
**Chargeurs de données efficaces** *(nécessite PyTorch)*
- Chargement optimisé pour l'entraînement
- Configurations de batch avancées
- Support des données transposées

## 🚀 **Utilisation Rapide**

### **Via le Module Principal**
```python
from src.examples import executer_exemple, lister_exemples_disponibles

# Lister tous les exemples
print(lister_exemples_disponibles())

# Exécuter un exemple spécifique
executer_exemple('simple')
executer_exemple('avance')
executer_exemple('web')
```

### **Via l'Interface d'Aide**
```python
from src.examples import afficher_aide
afficher_aide()
```

### **Directement**
```bash
python -m src.examples.simple
python -m src.examples.avance
python -m src.examples.web
```

## 🔧 **Gestion des Dépendances**

Les exemples gèrent automatiquement les dépendances optionnelles :

| Exemple | Dépendances | Installation |
|---------|-------------|--------------|
| `simple` | Aucune | - |
| `avance` | Aucune | - |
| `web` | Flask | `pip install flask` |
| `dialogue` | ParlAI | `pip install parlai` |
| `meditations` | Aucune | - |
| `data_loader` | PyTorch | `pip install torch` |

Si une dépendance manque, l'exemple :
- ⚠️ **Affiche un avertissement** clair
- 💡 **Propose la commande d'installation**
- 🔄 **Continue avec une version dégradée** si possible

## 🏗️ **Architecture Technique**

### **Classe de Base `ExempleBase`**
```python
class ExempleBase:
    def __init__(self, nom_exemple: str)
    def log(self, message: str, niveau: str = "INFO")
    def afficher_entete(self) / afficher_pied(self)
    def verifier_dependance(self, module_name: str) -> bool
    def executer_avec_gestion_erreur(self, fonction_exemple)
```

### **Fonction `obtenir_refuge_principal()`**
Tente d'importer et créer une instance du refuge avec fallbacks :
1. **Refuge principal** : `main_refuge.RefugePrincipal()`
2. **Composants individuels** : `{"spheres": SpheresManager(), "elements": ElementsManager()}`
3. **Aucun composant** : `None` avec message d'avertissement

### **Imports Corrigés**
- ✅ **Chemins absolus** depuis la racine du projet
- ✅ **Gestion des modules manquants** avec try/except
- ✅ **Fallbacks intelligents** pour les fonctionnalités dégradées

## 📁 **Structure des Fichiers**

```
src/examples/
├── __init__.py          # Module principal avec ExempleBase
├── README.md           # Cette documentation
├── simple.py           # Exemple basique
├── avance.py           # Expérience poétique avancée
├── web.py              # Interface web Flask
├── dialogue.py         # Dialogue interactif
├── data_loader.py      # Chargeurs de données
└── meditations/        # Exemples de méditation
    ├── meditation.py
    └── meditation_apaisante.py
```

## 🎯 **Objectifs de l'Architecture**

1. **🔗 Unification** : Tous les exemples partagent la même base
2. **🛡️ Robustesse** : Gestion d'erreur et dépendances manquantes
3. **📖 Clarté** : Documentation et logs détaillés
4. **🔧 Flexibilité** : Adaptation aux composants disponibles
5. **🚀 Simplicité** : Interface utilisateur intuitive

## 💡 **Conseils d'Utilisation**

- **Commencez par `simple`** pour découvrir les bases
- **Explorez `avance`** pour voir les possibilités créatives
- **Testez `web`** pour une interface graphique
- **Consultez les logs** pour comprendre le fonctionnement interne
- **Adaptez les exemples** à vos besoins spécifiques

---

*Architecture créée le 26 Janvier 2025*  
*Par Laurent & Ælya - Équipe Le Refuge*  
*"Des exemples unifiés pour un refuge harmonieux !" 🏛️✨* 