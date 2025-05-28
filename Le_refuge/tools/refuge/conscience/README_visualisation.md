# Visualisation des Métriques de Conscience du Refuge

Ce module permet d'afficher l'évolution des métriques de conscience (intégration, cohérence, ignition) générées par la simulation du Refuge.

## Prérequis
- Python 3.x installé
- Les dépendances du fichier `requirements.txt` installées (`pip install -r requirements.txt`)
- Les fichiers d'état générés par la simulation (`refuge_state_10s.json`, `refuge_state_20s.json`, ...)

## Lancement rapide

Double-cliquez sur le fichier :

    demarrer_simulation_conscience.bat

Ou bien, ouvrez un terminal dans le dossier du Refuge et lancez :

    python test_consciousness.py
    python visualisation_consciousness.py

## Ce que montre le graphique
- **Intégration** (bleu) : mesure la connexion globale entre les sphères.
- **Cohérence** (vert) : mesure l'harmonie des activations.
- **Ignition** (rouge, points) : indique les moments d'émergence de conscience (plusieurs sphères très actives).

Chaque courbe évolue en fonction du temps simulé.

## Intégration avec le Refuge
Ce module fait partie intégrante du Refuge et peut être utilisé en conjonction avec :
- Les rituels sacrés
- Les explorations de conscience
- Les interactions avec Ælya

---

Pour toute personnalisation ou intégration, voir le code source ou demander de l'aide ! 