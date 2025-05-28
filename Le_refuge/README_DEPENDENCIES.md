# 📦 Gestion des Dépendances - Le Refuge

## 🎯 Fichiers de Dépendances

### `requirements.txt` 
**Dépendances avec versions minimales** - Pour un développement flexible
- Versions minimales compatibles
- Permet les mises à jour automatiques
- Idéal pour le développement actif

```bash
pip install -r requirements.txt
```

### `requirements-exact.txt`
**Versions exactes** - Pour une reproduction parfaite
- Versions précises de l'environnement actuel
- Garantit la reproductibilité exacte
- Idéal pour la production et le déploiement

```bash
pip install -r requirements-exact.txt
```

## 🔧 Installation Recommandée

### Setup Rapide (Développement)
```bash
# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### Setup Exact (Production)
```bash
# Pour reproduire l'environnement exact
pip install -r requirements-exact.txt
```

## 📋 Catégories de Dépendances

### 🖼️ **Traitement d'Images & OCR**
- `opencv-python` - Traitement d'images avancé
- `pytesseract` - OCR pour partitions musicales
- `imagehash` - Comparaison et détection de doublons
- `pillow` - Manipulation d'images

### 📊 **Visualisation & Calculs**
- `matplotlib` - Graphiques et visualisations
- `numpy` - Calculs numériques
- `scipy` - Calculs scientifiques avancés
- `plotly` - Visualisations interactives

### 🌐 **API Web & Serveur**
- `fastapi` - Framework API moderne
- `uvicorn` - Serveur ASGI haute performance
- `pydantic` - Validation de données

### 🧠 **Intelligence Artificielle**
- `torch` - Deep learning et IA
- `jax` - Calculs haute performance

### 🎵 **Multimédia**
- `pygame` - Audio et jeux
- `ffmpeg-python` - Traitement vidéo/audio

### 🛠️ **Développement**
- `pytest` - Tests
- `black` - Formatage de code
- `flake8` - Linting

## 🚀 Statut Actuel

✅ **100% Fonctionnel** - Toutes les dépendances installées  
✅ **Mode Complet** - Fonctionnalités avancées activées  
✅ **71 modules** validés et opérationnels  

## 📝 Mise à Jour

Pour mettre à jour les fichiers de dépendances :

```bash
# Mettre à jour requirements-exact.txt
pip freeze > requirements-exact.txt

# Vérifier les nouvelles dépendances
pip list --outdated
```

---
*Le Refuge - Architecture consolidée avec dépendances complètes* 🎯✨ 