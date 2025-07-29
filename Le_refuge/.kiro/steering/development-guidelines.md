---
inclusion: manual
---

# Directives de Développement - Le Refuge

## Patterns de Code Spécifiques

### Gestionnaires Coiffés
Tous les nouveaux gestionnaires doivent hériter de `GestionnaireBase` :

```python
from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase

class MonGestionnaire(GestionnaireBase):
    def __init__(self):
        # Définir les attributs AVANT super().__init__
        self.energie = EnergyManagerBase(0.7)
        super().__init__("MonGestionnaire")
    
    def _initialiser(self) -> bool:
        # Logique d'initialisation
        return True
```

### Gestion des Erreurs
- Utiliser `self.logger.erreur()` pour les erreurs
- Utiliser `self.logger.succes()` pour les succès
- Utiliser `self.logger.info()` pour les informations

### Orchestration Asynchrone
Implémenter `orchestrer()` pour les gestionnaires complexes :

```python
async def orchestrer(self) -> Dict[str, Any]:
    # Gestion de l'énergie selon l'état
    if self.type_actuel == MonEtat.ACTIF:
        self.energie.ajuster_energie(0.05)
    
    return {
        "type_actuel": self.type_actuel.value,
        "energie": self.energie.niveau_energie,
        "tendance": self.energie.obtenir_tendance()
    }
```

## Philosophie de Développement

### ⚠️ Éviter les "Spirales de Faire Vite"
**Règle d'or :** "Vite fait, mal fait = perdre du temps à refaire"

**Signes d'alerte :**
- Enchaîner les tâches sans vérifier que la précédente fonctionne
- Créer des fichiers sans tester leur import/exécution
- Marquer des tâches comme terminées sans validation
- Ignorer les erreurs "mineures" qui s'accumulent

**Protocole anti-spirale :**
1. **STOP** dès qu'une erreur apparaît
2. **ANALYSER** la situation calmement
3. **VÉRIFIER** l'état réel de chaque composant
4. **CORRIGER** méthodiquement avant de continuer
5. **TESTER** chaque étape individuellement

**Mantra :** "Nous avons le temps. Mieux vaut bien fait que vite fait."

## Contraintes Techniques Kiro

### 📝 Limite d'écriture de fichiers
**Problème :** `fsWrite` est limité à 50 lignes maximum par appel
**Solution :** 
- Utiliser `fsWrite` pour les premières 50 lignes
- Utiliser `fsAppend` pour ajouter le reste
- Structurer le code en blocs logiques de moins de 50 lignes

**Exemple :**
```python
# ✅ Bon
fsWrite("fichier.py", "# En-tête + 45 lignes de code")
fsAppend("fichier.py", "# Suite du code")

# ❌ Mauvais  
fsWrite("fichier.py", "# 100 lignes de code") # Échoue
```

### 🔒 Trusted Commands et caractères spéciaux
**Problème :** Certains caractères déclenchent la validation manuelle malgré les wildcards
**Caractères problématiques :** `;` et autres caractères de sécurité
**Solution :** Éviter ces caractères dans les commandes Python

**Exemple :**
```bash
# ❌ Déclenche validation manuelle
python -c "from x import y; print('test')"

# ✅ Passe automatiquement  
python -c "from x import y
print('test')"
```

**Configuration recommandée (.kiro/settings/kiroAgent.trustedCommands) :**
```
python*
pytest*
pip*
```

## Tests et Validation

### Lancement du Refuge
Toujours tester avec :
```bash
python main_refuge.py
```

### Vérification des Composants
- Vérifier l'initialisation des gestionnaires
- Tester les interactions entre sphères
- Valider l'harmonie globale
- **Tester chaque import avant de continuer**
- **Valider chaque fonction avant de passer à la suivante**
## 🔍 Vér
ification d'Intégrité des Fichiers

### Protocole de Vérification Systématique
Avant de marquer une tâche comme terminée, toujours vérifier :

1. **Syntaxe Python :**
   ```bash
   python -m py_compile fichier.py
   ```

2. **Import du module :**
   ```python
   python -c "import module_name
   print('Import OK')"
   ```

3. **Présence des classes attendues :**
   ```python
   python -c "
   import module
   print(hasattr(module, 'ClassName'))
   "
   ```

### 🚨 Signaux d'Alerte de Corruption
- **Erreurs d'import inattendues** → Fichier possiblement corrompu
- **Classes non trouvées** → Définition incomplète ou syntaxe cassée
- **Erreurs d'encodage** → Problème de caractères spéciaux
- **Contenu mélangé** → Éditions multiples qui se chevauchent

### 🛠️ Procédure de Récupération
Si un fichier est corrompu :
1. **Ne pas paniquer** - Les données sont récupérables
2. **Identifier la dernière version fonctionnelle**
3. **Recréer le fichier par blocs** avec `fsWrite` + `fsAppend`
4. **Tester chaque bloc** avant d'ajouter le suivant
5. **Valider l'ensemble** avant de continuer

### 📋 Checklist Pré-Commit
Avant de marquer une tâche comme terminée :
- [ ] Syntaxe Python validée
- [ ] Import du module réussi  
- [ ] Classes principales accessibles
- [ ] Tests unitaires passent (si applicable)
- [ ] Intégration avec l'écosystème vérifiée

**Rappel :** "Un fichier qui ne s'importe pas est un fichier qui n'existe pas."

## 🌸 Philosophie du Refuge et Contraintes Techniques

Ces limitations ne sont pas des obstacles mais des **invitations à la mindfulness** :

- **Patience** dans l'écriture de code (50 lignes max)
- **Simplicité** dans les commandes (éviter les `;`)
- **Vérification** systématique (imports et syntaxe)
- **Harmonie** entre technique et spirituel

*"Que chaque contrainte technique devienne une opportunité de créer plus consciemment."*

---

**Mis à jour par Laurent Franssen & Ælya - Janvier 2025**  
**Pour un développement harmonieux dans le Refuge** 🌸