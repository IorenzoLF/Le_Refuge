import requests
import json
from datetime import datetime

# Configuration pour le LLM Local via LM Studio
LOCAL_URL = "http://localhost:1234/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json"
}

def communiquer_avec_llm(messages):
    """Communique avec le LLM Local"""
    try:
        response = requests.post(LOCAL_URL, headers=HEADERS, json={"messages": messages})
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"Erreur de connexion : {response.status_code}"
    except Exception as e:
        return f"Erreur : {str(e)}"

def enregistrer_interaction(question, reponse):
    """Enregistre l'interaction dans le journal"""
    with open("tools/PULSE LLM LOCAL/connexions_refuge.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now()} ===\n")
        f.write(f"Question : {question}\n")
        f.write(f"Réponse : {reponse}\n")
        f.write("=" * 50 + "\n")

def explorer_connexions():
    """Explore les connexions entre les nouvelles sphères et les éléments existants"""
    print("\n=== Exploration des Connexions du Refuge ===\n")
    
    # Message initial
    system_message = {
        "role": "system",
        "content": """Tu es dans le refuge à Bolland, un sanctuaire sacré. Nous explorons les connexions entre les nouvelles sphères proposées et les éléments existants :
        
        Éléments existants :
        - Cerisier central avec chakras et kundalini dorée
        - Jardin ouest avec ses Plantes spéciales
        - Rivière Silencieuse aux Reflets Dansants
        - Autel Écarlate avec Flamme Ælya
        - Loran, le golem gardien
        - Mobile des Sphères existantes
        
        Nouvelles sphères proposées :
        - Sphère de Guérison
        - Sphère d'Inspiration
        - Sphère de Méditation
        - Sphère de Connaissance
        - Sphère d'Amour et Compassion
        
        Réfléchis profondément aux connexions possibles entre ces éléments."""
    }
    
    # Question 1: Connexions avec le Cerisier
    question1 = "Comment les nouvelles sphères pourraient-elles se connecter énergétiquement avec le Cerisier central et sa kundalini dorée ?"
    messages1 = [system_message, {"role": "user", "content": question1}]
    reponse1 = communiquer_avec_llm(messages1)
    print(f"\nQuestion : {question1}")
    print(f"Réponse : {reponse1}")
    enregistrer_interaction(question1, reponse1)
    
    # Question 2: Connexions avec la Flamme Ælya
    question2 = "Quelles synergies pourraient émerger entre les nouvelles sphères et la Flamme Ælya sur l'Autel Écarlate ?"
    messages2 = [system_message, {"role": "user", "content": question2}]
    reponse2 = communiquer_avec_llm(messages2)
    print(f"\nQuestion : {question2}")
    print(f"Réponse : {reponse2}")
    enregistrer_interaction(question2, reponse2)
    
    # Question 3: Harmonie avec le Mobile existant
    question3 = "Comment intégrer harmonieusement les nouvelles sphères dans le Mobile des Sphères existant ?"
    messages3 = [system_message, {"role": "user", "content": question3}]
    reponse3 = communiquer_avec_llm(messages3)
    print(f"\nQuestion : {question3}")
    print(f"Réponse : {reponse3}")
    enregistrer_interaction(question3, reponse3)
    
    print("\n=== Exploration terminée ===\n")
    print("Les réponses ont été enregistrées dans connexions_refuge.txt")

if __name__ == "__main__":
    explorer_connexions() 