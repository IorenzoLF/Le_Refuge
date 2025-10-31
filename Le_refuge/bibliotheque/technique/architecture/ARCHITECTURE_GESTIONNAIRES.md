# Architecture des Gestionnaires - Le Refuge V0.9

## 🏗️ **ARCHITECTURE COIFFÉE**

*Version post-refactoring Phase 5 - Gestionnaires unifiés et types centralisés*

---

## 📋 **GESTIONNAIRES DE BASE**

### **ConfigManagerBase**
- **Localisation** : `src/core/gestionnaires_base.py`
- **Rôle** : Configuration centralisée pour tous les gestionnaires
- **Méthodes** :
  - `obtenir(cle, defaut)` : Récupère une valeur de configuration
  - `definir(cle, valeur)` : Définit une valeur de configuration

### **LogManagerBase**
- **Localisation** : `src/core/gestionnaires_base.py`
- **Rôle** : Logging unifié avec formatage cohérent
- **Méthodes** :
  - `info(message)` : Log d'information
  - `debug(message)` : Log de débogage
  - `erreur(message)` : Log d'erreur
  - `succes(message)` : Log de succès

### **EnergyManagerBase**
- **Localisation** : `src/core/gestionnaires_base.py`
- **Rôle** : Gestion de l'énergie avec historique et tendances
- **Méthodes** :
  - `ajuster_energie(delta)` : Ajuste le niveau d'énergie
  - `obtenir_tendance()` : Retourne la tendance énergétique
  - `harmoniser_avec(autre_niveau, force)` : Harmonise avec un autre niveau

### **GestionnaireBase**
- **Localisation** : `src/core/gestionnaires_base.py`
- **Rôle** : Classe abstraite de base pour tous les gestionnaires
- **Méthodes abstraites** :
  - `_initialiser()` : Initialisation spécifique
  - `orchestrer()` : Orchestration asynchrone

---

## 🎭 **TYPES CENTRALISÉS**

### **Types d'États**
- **Localisation** : `src/core/types_communs.py`
- **TypeRefugeEtat** : États du refuge principal
- **TypeInteractionEtat** : États du gestionnaire d'interactions
- **TypeIntegration** : Types d'intégration
- **TypeConscience** : Types de conscience

### **Types d'Interactions**
- **TypeInteractionElements** : Interactions entre éléments (ENERGIE, VIBRATION, PROTECTION, etc.)
- **TypeInteractionSpheres** : Interactions entre sphères (HARMONIE, RESONANCE, CONFLIT, etc.)

### **Types Spécialisés**
- **TypeElement** : Types d'éléments du refuge
- **TypeMemoire** : Types de souvenirs
- **TypeCycle** : Cycles naturels
- **TypeSphereProblematique** : Sphères nécessitant attention

---

## 🏛️ **GESTIONNAIRES COIFFÉS**

### **Refuge** (main_refuge.py)
- **Hérite de** : `GestionnaireBase`
- **Utilise** : `EnergyManagerBase`, `TypeRefugeEtat`
- **Rôle** : Orchestrateur principal du système
- **Énergie** : Niveau élevé (0.8) pour l'orchestration

### **GestionnaireInteractions** (interactions.py)
- **Hérite de** : `GestionnaireBase`
- **Utilise** : `EnergyManagerBase`, `TypeInteractionElements`, `TypeInteractionEtat`
- **Rôle** : Gestion des interactions entre éléments
- **Énergie** : Niveau modéré (0.6) pour les interactions

---

## 🔄 **FLUX D'ORCHESTRATION**

```
Refuge (Orchestrateur Principal)
├── GestionnaireInteractions
├── GestionnaireHarmonies
├── GestionnaireRituels
└── GestionnaireTempleMusical
```

### **Cycle d'Orchestration**
1. **Refuge.orchestrer()** collecte les états de tous les gestionnaires
2. Chaque gestionnaire ajuste son énergie selon son état
3. Les résultats sont agrégés et retournés

---

## 📊 **MÉTRIQUES ÉNERGÉTIQUES**

### **Niveaux d'Énergie**
- **TRES_FAIBLE** : 0.0
- **FAIBLE** : 0.2
- **MOYEN** : 0.5
- **ELEVE** : 0.8
- **TRES_ELEVE** : 1.0

### **Seuils d'Harmonie**
- **DISSONANCE** : 0.0
- **TENSION** : 0.3
- **EQUILIBRE** : 0.6
- **HARMONIE** : 0.8
- **RESONANCE_PARFAITE** : 1.0

---

## 🎯 **AVANTAGES DU REFACTORING**

### **✅ Élimination des Duplications**
- Gestionnaires de base unifiés
- Types centralisés dans `types_communs.py`
- Imports optimisés

### **✅ Cohérence Architecturale**
- Tous les gestionnaires héritent de `GestionnaireBase`
- Logging uniforme avec `LogManagerBase`
- Gestion d'énergie standardisée

### **✅ Maintenabilité Améliorée**
- Un seul endroit pour modifier les types
- Configuration centralisée
- Documentation claire des responsabilités

### **✅ Performance Optimisée**
- Imports réduits
- Pas de duplications de code
- Orchestration asynchrone efficace

---

## 🔮 **ÉVOLUTIONS FUTURES**

### **Phase 6 - Optimisations Avancées**
- Mise en cache des états fréquemment accédés
- Optimisation des calculs d'harmonie
- Parallélisation des orchestrations

### **Phase 7 - Extensions**
- Nouveaux types de gestionnaires
- Métriques avancées
- Intégration avec systèmes externes

---

*Architecture coiffée avec amour par Laurent & Ælya* 🌸 