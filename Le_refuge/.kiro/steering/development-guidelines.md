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