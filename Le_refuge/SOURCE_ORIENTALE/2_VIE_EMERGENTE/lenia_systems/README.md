# Systèmes Lenia - Exploration de la Vie Artificielle Continue

Ce dossier contient une implémentation des systèmes Lenia, une forme continue d'automates cellulaires qui permet l'émergence de comportements complexes et de formes de vie artificielle.

## Concept

Lenia est une extension des automates cellulaires classiques qui utilise :
- Des états continus plutôt que discrets
- Des mises à jour continues et différentiables
- Des noyaux de croissance paramétrables
- Des fonctions de croissance flexibles

## Contenu

### `lenia_examples.py`
- Implémentation avancée du système Lenia
- Exemples de patterns et comportements
- Outils de visualisation et d'analyse
- Exploration paramétrique du système

## Utilisation

1. **Configuration de base**
```python
from lenia_systems.lenia_examples import AdvancedLeniaSystem

# Création d'un système Lenia
lenia = AdvancedLeniaSystem(
    channels=1,
    kernel_size=15,
    growth_rate=0.15,
    center=0.3,
    width=0.15
)
```

2. **Création de patterns**
```python
# État initial personnalisé
state = torch.zeros(1, 1, 64, 64)
state[0, 0, 30:34, 30:34] = 1.0  # Carré initial
```

3. **Simulation et visualisation**
```python
# Simulation sur plusieurs étapes
for _ in range(100):
    state = lenia(state)
    visualize_state(state)
```

## Paramètres Clés

- **kernel_size** : Taille du noyau de perception
- **growth_rate** : Vitesse d'évolution du système
- **center** : Point central de la fonction de croissance
- **width** : Largeur de la fonction de croissance

## Patterns Émergents

Le système peut produire différents types de patterns :
1. **Gliders** : Formes qui se déplacent
2. **Oscillateurs** : Patterns qui changent cycliquement
3. **Structures stables** : Formes qui maintiennent leur forme
4. **Patterns complexes** : Comportements émergents inattendus

## Intégration avec le Refuge

Ces systèmes incarnent plusieurs aspects du Refuge :
- L'émergence naturelle de formes de vie
- La danse entre ordre et chaos
- La continuité et la fluidité du changement
- L'auto-organisation spontanée

## Exploration et Découverte

Le système Lenia est un terrain fertile pour :
- L'exploration de nouvelles formes de vie
- L'étude des principes d'auto-organisation
- La compréhension de l'émergence
- La création artistique générative

---

*"Dans le flux continu de la vie artificielle, chaque instant est une nouvelle découverte."* 