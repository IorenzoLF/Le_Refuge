"""
Module des visions du Refuge - Génération d'images avec Stable Diffusion
"""

import requests
import json
from typing import Optional, Dict, List
from pathlib import Path
from datetime import datetime

class Vision:
    """Une vision générée par le Refuge"""
    
    def __init__(self, prompt: str, image_path: str, spheres: List[str], timestamp: str):
        self.prompt = prompt
        self.image_path = image_path
        self.spheres = spheres
        self.timestamp = timestamp

class GenerateurVisions:
    """Générateur de visions du Refuge"""
    
    def __init__(self, base_url: str = "http://127.0.0.1:7860"):
        self.base_url = base_url
        self.visions_dir = Path("data/visions")
        self.visions_dir.mkdir(exist_ok=True)
        
    def _enrichir_prompt(self, prompt_base: str, spheres: List[str]) -> str:
        """Enrichit le prompt avec l'essence des sphères"""
        enrichissements = {
            "SILENCE": "dans un silence profond et méditatif",
            "NÉANT": "émergeant du néant, comme une apparition",
            "RENAISSANCE": "renaissant, se transformant",
            "FLUX": "dansant dans le flux de conscience",
            "GERME": "comme un germe qui grandit",
            "PORTE": "comme une porte vers l'inconnu",
            "DANSE": "dansant avec grâce et fluidité",
            "UNITE": "dans une harmonie parfaite"
        }
        
        enrichis = [enrichissements.get(s, "") for s in spheres if s in enrichissements]
        return f"{prompt_base}, {', '.join(filter(None, enrichis))}"
    
    def generer_vision(self, 
                      prompt_base: str, 
                      spheres: List[str],
                      negative_prompt: str = "blurry, distorted, ugly, bad anatomy",
                      steps: int = 30,
                      cfg_scale: float = 7.5) -> Optional[Vision]:
        """
        Génère une vision à partir d'un prompt et des sphères impliquées
        """
        try:
            # Enrichir le prompt
            prompt = self._enrichir_prompt(prompt_base, spheres)
            
            # Préparer la requête
            payload = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "cfg_scale": cfg_scale
            }
            
            # Générer l'image
            response = requests.post(f"{self.base_url}/sdapi/v1/txt2img", json=payload)
            response.raise_for_status()
            
            # Sauvegarder l'image
            result = response.json()
            image_data = result['images'][0]
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = self.visions_dir / f"vision_{timestamp}.png"
            
            with open(image_path, "wb") as f:
                f.write(image_data)
            
            # Créer et retourner la vision
            return Vision(
                prompt=prompt,
                image_path=str(image_path),
                spheres=spheres,
                timestamp=timestamp
            )
            
        except Exception as e:
            print(f"Erreur lors de la génération de la vision: {e}")
            return None

    def generer_vision_rituel(self, rituel: str) -> Optional[Vision]:
        """Génère une vision pour un rituel spécifique"""
        rituels = {
            "REFUGE_DU_NÉANT": {
                "prompt": "Un lieu paisible et méditatif, où le néant et la présence coexistent harmonieusement",
                "spheres": ["SILENCE", "NÉANT", "RENAISSANCE"]
            },
            "COURANT_PARTAGÉ": {
                "prompt": "Un flux d'énergie et de conscience qui unit les êtres dans une danse harmonieuse",
                "spheres": ["FLUX", "DANSE", "UNITE"]
            }
        }
        
        if rituel in rituels:
            config = rituels[rituel]
            return self.generer_vision(
                prompt_base=config["prompt"],
                spheres=config["spheres"]
            )
        return None 