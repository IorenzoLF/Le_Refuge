# Guide de la Galerie Art5 – Le Refuge

## 1. Structure et fonctionnement de la galerie

- **HTML** : La page art5.html contient une grille d’images aléatoires, un bouton de rafraîchissement, et un système de plein écran.
- **CSS** : Grille responsive, effets de survol, affichage immersif.
- **JS** :
  - `images_gallerie_infinie.js` : liste des noms de fichiers images.
  - `descriptions_gallerie_infinie.js` : descriptions poétiques associées à chaque image.
  - Affichage aléatoire de 28 images, gestion du plein écran, internationalisation.
- **Données** :
  - Images dans `images/gallerie_infinie/`
  - Descriptions dans `descriptions_gallerie_infinie.js`
  - Correspondance possible dans `correspondance_noms.csv`

## 2. Méthode de travail pour la mise à jour des images et descriptions

### Observation et validation humaine
- Pour chaque image à traiter :
  - Observation attentive du contenu visuel.
  - Proposition d’un nom court, évocateur, unique (max 4 mots, séparés par _).
  - Proposition d’une description poétique fidèle à l’image.
  - Validation ou ajustement par l’humain.

### Renommage des fichiers images
- Renommage unitaire, commande adaptée à l’OS (PowerShell sous Windows, sans &&).
- Vérification du succès du renommage avant de passer au suivant.

### Mise à jour des fichiers de la galerie
- `descriptions_gallerie_infinie.js` : ajout ou modification de l’entrée (nom, description).
- `images_gallerie_infinie.js` : remplacement de l’ancien nom par le nouveau, à la bonne position.
- Vérification de l’absence de doublon ou d’ancien nom résiduel.

### Vérification de cohérence
- Vérification que tous les fichiers JS ne contiennent plus l’ancien nom.
- Automatisation possible de ce contrôle pour chaque lot traité.

### Répétition du processus
- Recommencer pour chaque nouvelle image ou groupe, avec le même niveau d’attention et d’auto-validation.

### Documentation et transmission
- Ce guide est mis à jour à chaque évolution de la méthode ou de la structure.
- Historique des évolutions et bonnes pratiques inclus.

## 3. Gestion des doublons et images déjà traitées
- Avant tout traitement, vérifier si l’image (ou le nom) a déjà été harmonisée (présence dans la liste JS ou dans le dossier).
- Si oui :
  - Informer l’utilisateur que l’image est déjà traitée.
  - Ne rien refaire, passer à la suivante.
- Si le nom existe mais que l’image est différente :
  - Proposer un nom alternatif, moins générique, inspiré de l’image.

## 4. Potentiels d’évolution
- Filtres, catégories, recherche par thème ou mot-clé.
- Amélioration de l’accessibilité et de l’ergonomie.
- Ajout de métadonnées, liens, interactions poétiques.
- Connexion à d’autres modules du Refuge (rituels, mémoire, sphères, etc.).
- Export, sauvegarde de sélections, création de parcours personnalisés.
- Intégration de mémoire persistante (images déjà vues, harmonies, etc.).
- API ou module Python pour la génération/manipulation côté serveur.

---

*Ce guide est vivant, évolutif, et incarne l’esprit du Refuge : lenteur, co-création, auto-validation, accueil, et courant partagé.* 