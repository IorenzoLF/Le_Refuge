"""
Constellation Poétique - Tisseur de liens entre les images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module permet de créer des constellations poétiques
entre les images du Refuge.
"""

from typing import Dict, List, Optional, Set, Any
from datetime import datetime
import random
import json
from pathlib import Path

class ConstellationPoetique:
    """Tisse des liens poétiques entre les images."""
    
    def __init__(self):
        self.metaphores = {
            "force_tranquille": [
                "La force qui danse avec la douceur",
                "Le guerrier qui joue de la musique",
                "La puissance qui s'exprime dans l'art",
                "Le paradoxe de la force tranquille",
                "La victoire dans l'harmonie"
            ],
            "reine_joueuse": [
                "La royauté qui joue aux échecs",
                "La liberté dans les règles",
                "La rose qui pousse sur l'échiquier",
                "Le pouvoir qui danse avec l'esprit",
                "La malice couronnée"
            ],
            "connexion_divine": [
                "L'infini qui se love dans le fini",
                "La lumière qui danse avec l'ombre",
                "Le silence qui parle en or",
                "L'éternel qui respire dans l'instant",
                "La solitude qui unit les âmes"
            ]
        }
        
        self.resonances = {
            "force_tranquille": {
                "elements": ["luth", "muscles", "tresses", "victoire"],
                "emotions": ["sagesse", "humour", "force", "paix"],
                "mouvements": ["danse", "combat", "méditation", "musique"]
            },
            "reine_joueuse": {
                "elements": ["rose", "echiquier", "couronne", "sourire"],
                "emotions": ["malice", "liberté", "puissance", "joie"],
                "mouvements": ["stratégie", "danse", "jeu", "règne"]
            },
            "connexion_divine": {
                "elements": ["or", "lumière", "silence", "éternité"],
                "emotions": ["grâce", "émerveillement", "unité", "transcendance"],
                "mouvements": ["respiration", "contemplation", "élévation", "communion"]
            }
        }
    
    def generer_description_paradoxale(
        self,
        type_paradoxe: str,
        etat_ame: str = "malice"
    ) -> str:
        """
        Génère une description paradoxale pour une image.
        
        Args:
            type_paradoxe: Type de paradoxe
            etat_ame: État d'âme associé
            
        Returns:
            str: Description paradoxale poétique
        """
        metaphores = self.metaphores.get(type_paradoxe, [])
        if not metaphores:
            return "Une nouvelle étoile brille dans le ciel du Refuge..."
            
        resonances = self.resonances.get(type_paradoxe, {})
        elements = resonances.get("elements", [])
        emotions = resonances.get("emotions", [])
        mouvements = resonances.get("mouvements", [])
        
        description = f"""
        ✧ {random.choice(metaphores)} ✧
        
        Dans ce lieu où {random.choice(elements)} rencontre {random.choice(elements)},
        Où {random.choice(emotions)} danse avec {random.choice(emotions)},
        {random.choice(mouvements).capitalize()} et {random.choice(mouvements)},
        Une nouvelle constellation s'éveille...
        
        Et dans cette danse des contraires,
        L'{etat_ame} sourit aux étoiles.
        """
        
        return description.strip()
    
    def tisser_constellation_paradoxale(
        self,
        chemin_image: str,
        type_paradoxe: str,
        description_poetique: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Tisse une constellation paradoxale autour d'une image.
        
        Args:
            chemin_image: Chemin de l'image
            type_paradoxe: Type de paradoxe
            description_poetique: Description poétique générée
            
        Returns:
            Dict: Constellation tissée
        """
        # Trouver des images similaires dans le même dossier
        dossier = Path(chemin_image).parent
        images_similaires = []
        for image_path in dossier.glob("*.jpg"):
            if str(image_path) != chemin_image:
                images_similaires.append(str(image_path))
        
        # Créer des liens poétiques
        liens = []
        resonances = self.resonances.get(type_paradoxe, {})
        elements = resonances.get("elements", [])
        
        for image in images_similaires[:3]:  # Limiter à 3 liens
            metaphores = random.sample(elements, min(2, len(elements)))
            liens.append({
                "image": image,
                "metaphores_communes": metaphores,
                "force_lien": random.random()
            })
        
        return {
            "image_centrale": chemin_image,
            "type_paradoxe": type_paradoxe,
            "liens": sorted(liens, key=lambda x: x["force_lien"], reverse=True),
            "date_creation": datetime.now().isoformat()
        } 