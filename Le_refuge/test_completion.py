import requests
import json

url = "http://192.168.0.217:1234/v1/completions"
headers = {"Content-Type": "application/json"}
data = {
    "prompt": """[INSTRUCTIONS: Réponds en français et en vers poétiques. Ne fais pas d'analyse.]

Sous le cerisier, je viens chercher le refuge du néant""",
    "max_tokens": 150,
    "temperature": 0.7,
    "stop": ["[INSTRUCTIONS"]
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}") 