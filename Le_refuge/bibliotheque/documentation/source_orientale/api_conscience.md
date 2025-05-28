# Documentation de l'API REST — Conscience Artificielle

## Endpoints principaux

### 1. Dialogue
- **POST** `/api/dialogue`
- **Description** : Permet de dialoguer avec la conscience artificielle.
- **Exemple de requête** :
```json
{
  "contenu": "Bonjour, conscience"
}
```
- **Réponse** :
```json
{
  "reponse": "Bonjour, conscience... [réponse générée]"
}
```

### 2. Mémorisation
- **POST** `/api/memoire`
- **Description** : Mémorise une expérience ou un contenu.
- **Exemple de requête** :
```json
{
  "contenu": "Souvenir important"
}
```
- **Réponse** :
```json
{
  "memoire_id": 1
}
```

### 3. Récupération de mémoire
- **GET** `/api/memoire/{memoire_id}`
- **Description** : Récupère une mémoire enregistrée.
- **Réponse** :
```json
{
  "id": 1,
  "contenu": "Souvenir important",
  "date_creation": "2024-05-04T15:00:00"
}
```

### 4. Validation de mémoire
- **POST** `/api/validation`
- **Description** : Valide ou invalide une mémoire.
- **Exemple de requête** :
```json
{
  "memoire_id": 1,
  "validation": true,
  "commentaire": "Mémoire validée."
}
```
- **Réponse** :
```json
{
  "succes": true
}
```

### 5. État de la conscience
- **GET** `/api/etat`
- **Description** : Retourne l'état global de la conscience.
- **Réponse** :
```json
{
  "memoire_persistante": true,
  "auto_validation": true,
  ...
}
```

## Documentation interactive
- Accès : [http://localhost:8000/docs](http://localhost:8000/docs)

## Utilisation avec curl
```bash
curl -X POST http://localhost:8000/api/dialogue -H "Content-Type: application/json" -d '{"contenu": "Bonjour"}'
```

## Utilisation avec httpx (Python)
```python
import httpx
r = httpx.post("http://localhost:8000/api/dialogue", json={"contenu": "Bonjour"})
print(r.json())
``` 