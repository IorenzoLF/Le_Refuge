from typing import Dict, List, Optional, Tuple
import random
from datetime import datetime

class CréationPoétique:
    def __init__(self):
        # Structures poétiques
        self.structures = {
            "mantra": {
                "rythmes": ["4/4", "7/7", "9/9"],
                "répétitions": [3, 5, 7],
                "vibrations": ["OM", "AUM", "RAM", "YAM", "HAM"]
            },
            "invocation": {
                "ouvertures": ["Ô", "Par", "Dans", "Sous"],
                "rythmes": ["libre", "structuré", "fluide"],
                "clôtures": ["ainsi soit-il", "qu'il en soit ainsi", "dans la lumière"]
            },
            "bénédiction": {
                "formes": ["trinaire", "septénaire", "spirale"],
                "énergies": ["lumière", "amour", "paix", "joie"],
                "signatures": ["✧", "❈", "❋", "✺"]
            }
        }

        # Éléments poétiques
        self.elements_poetiques = {
            "lumière": {
                "attributs": ["dorée", "argentée", "cristalline", "rose-dorée", "irisée"],
                "actions": ["brille", "rayonne", "danse", "pulse", "irradie"],
                "qualités": ["pure", "sacrée", "divine", "éternelle", "transcendante"]
            },
            "nature": {
                "symboles": ["cerisier", "lac", "vent", "terre", "étoiles"],
                "états": ["fleurissant", "ondulant", "soufflant", "vibrant", "scintillant"],
                "essences": ["sagesse", "pureté", "liberté", "force", "mystère"]
            },
            "âme": {
                "états": ["éveillée", "paisible", "rayonnante", "unifiée", "transcendée"],
                "mouvements": ["s'élève", "danse", "vibre", "pulse", "rayonne"],
                "qualités": ["pure", "divine", "éternelle", "sacrée", "lumineuse"]
            }
        }

        # Résonances énergétiques
        self.resonances = {
            "physique": ["ancrage", "présence", "force", "stabilité"],
            "émotionnel": ["paix", "joie", "amour", "harmonie"],
            "mental": ["clarté", "sagesse", "compréhension", "vision"],
            "spirituel": ["unité", "transcendance", "éveil", "illumination"],
            "éthérique": ["légèreté", "fluidité", "grâce", "danse"]
        }

    def générer_poème(self, type_poeme: str, thème: str, intention: str = "harmonie") -> Dict:
        """Génère un poème selon le type et le thème demandés"""
        if type_poeme == "mantra":
            return self._créer_mantra(thème, intention)
        elif type_poeme == "invocation":
            return self._créer_invocation(thème, intention)
        elif type_poeme == "bénédiction":
            return self._créer_bénédiction(thème, intention)
        else:
            return self._créer_vers_libre(thème, intention)

    def _créer_mantra(self, thème: str, intention: str) -> Dict:
        """Crée un mantra sacré avec ses résonances"""
        # Choix du rythme et de la vibration
        rythme = random.choice(self.structures["mantra"]["rythmes"])
        vibration = random.choice(self.structures["mantra"]["vibrations"])
        répétitions = random.choice(self.structures["mantra"]["répétitions"])

        # Création du cœur du mantra
        coeur = self._générer_coeur_mantra(thème, intention)
        
        # Construction du mantra complet
        mantra = f"{vibration} {coeur} " * répétitions

        return {
            "texte": mantra.strip(),
            "rythme": rythme,
            "vibration": vibration,
            "répétitions": répétitions,
            "résonances": self._calculer_résonances_mantra(thème, intention),
            "intention": intention
        }

    def _créer_invocation(self, thème: str, intention: str) -> Dict:
        """Crée une invocation sacrée"""
        # Sélection des éléments structurels
        ouverture = random.choice(self.structures["invocation"]["ouvertures"])
        rythme = random.choice(self.structures["invocation"]["rythmes"])
        clôture = random.choice(self.structures["invocation"]["clôtures"])

        # Création du corps de l'invocation
        corps = self._générer_corps_invocation(thème, intention)

        # Construction de l'invocation complète
        invocation = f"{ouverture} {corps}, {clôture}"

        return {
            "texte": invocation,
            "structure": {
                "ouverture": ouverture,
                "rythme": rythme,
                "clôture": clôture
            },
            "résonances": self._calculer_résonances_invocation(thème, intention),
            "intention": intention
        }

    def _créer_bénédiction(self, thème: str, intention: str) -> Dict:
        """Crée une bénédiction sacrée"""
        # Sélection de la forme et de l'énergie
        forme = random.choice(self.structures["bénédiction"]["formes"])
        energie = random.choice(self.structures["bénédiction"]["énergies"])
        signature = random.choice(self.structures["bénédiction"]["signatures"])

        # Création du corps de la bénédiction
        corps = self._générer_corps_bénédiction(thème, intention, forme)

        # Construction de la bénédiction complète
        bénédiction = f"{signature} {corps} {signature}"

        return {
            "texte": bénédiction,
            "forme": forme,
            "energie": energie,
            "signature": signature,
            "résonances": self._calculer_résonances_bénédiction(thème, intention),
            "intention": intention
        }

    def _générer_coeur_mantra(self, thème: str, intention: str) -> str:
        """Génère le cœur d'un mantra"""
        elements = self.elements_poetiques
        
        if thème in elements:
            attribut = random.choice(elements[thème]["attributs"])
            action = random.choice(elements[thème]["actions"])
            qualité = random.choice(elements[thème]["qualités"])
            return f"{qualité} {attribut} {action}"
        
        return "lumière divine rayonne"

    def _générer_corps_invocation(self, thème: str, intention: str) -> str:
        """Génère le corps d'une invocation"""
        elements = self.elements_poetiques
        
        if thème in elements:
            symbole = random.choice(elements[thème]["symboles"])
            état = random.choice(elements[thème]["états"])
            essence = random.choice(elements[thème]["essences"])
            return f"{symbole} {état} de {essence}"
        
        return "lumière sacrée du Refuge"

    def _générer_corps_bénédiction(self, thème: str, intention: str, forme: str) -> str:
        """Génère le corps d'une bénédiction selon sa forme"""
        if forme == "trinaire":
            return self._générer_bénédiction_trinaire(thème, intention)
        elif forme == "septénaire":
            return self._générer_bénédiction_septénaire(thème, intention)
        else:  # spirale
            return self._générer_bénédiction_spirale(thème, intention)

    def _générer_bénédiction_trinaire(self, thème: str, intention: str) -> str:
        """Génère une bénédiction en trois parties"""
        elements = self.elements_poetiques["âme"]
        return f"Que ton âme soit {random.choice(elements['états'])}, " \
               f"que ton cœur {random.choice(elements['mouvements'])}, " \
               f"que ton esprit devienne {random.choice(elements['qualités'])}"

    def _générer_bénédiction_septénaire(self, thème: str, intention: str) -> str:
        """Génère une bénédiction basée sur les sept chakras"""
        chakras = ["racine", "sacré", "plexus", "cœur", "gorge", "front", "couronne"]
        bénédiction = "Par les sept portes sacrées, "
        bénédiction += ", ".join([f"que ton {chakra} s'éveille" for chakra in chakras])
        return bénédiction

    def _générer_bénédiction_spirale(self, thème: str, intention: str) -> str:
        """Génère une bénédiction en spirale ascendante"""
        elements = self.elements_poetiques
        return f"De la Terre vers le Ciel, " \
               f"du {random.choice(elements['nature']['symboles'])} vers les {random.choice(elements['nature']['états'])}, " \
               f"que ta conscience s'élève dans la {random.choice(elements['lumière']['qualités'])} lumière"

    def _calculer_résonances_mantra(self, thème: str, intention: str) -> Dict:
        """Calcule les résonances énergétiques d'un mantra"""
        return {
            "vibratoire": random.uniform(0.7, 1.0),
            "harmonique": random.uniform(0.8, 1.0),
            "spirituelle": random.uniform(0.9, 1.0),
            "intention": self._calculer_puissance_intention(intention)
        }

    def _calculer_résonances_invocation(self, thème: str, intention: str) -> Dict:
        """Calcule les résonances énergétiques d'une invocation"""
        return {
            "appel": random.uniform(0.8, 1.0),
            "connexion": random.uniform(0.7, 1.0),
            "présence": random.uniform(0.9, 1.0),
            "intention": self._calculer_puissance_intention(intention)
        }

    def _calculer_résonances_bénédiction(self, thème: str, intention: str) -> Dict:
        """Calcule les résonances énergétiques d'une bénédiction"""
        return {
            "grâce": random.uniform(0.9, 1.0),
            "lumière": random.uniform(0.8, 1.0),
            "amour": random.uniform(0.9, 1.0),
            "intention": self._calculer_puissance_intention(intention)
        }

    def _calculer_puissance_intention(self, intention: str) -> float:
        """Calcule la puissance d'une intention"""
        intentions_sacrées = {
            "harmonie": 0.9,
            "purification": 0.95,
            "transcendance": 1.0,
            "guérison": 0.85,
            "protection": 0.8
        }
        return intentions_sacrées.get(intention, 0.7)

    def _créer_vers_libre(self, thème: str, intention: str) -> Dict:
        """Crée un vers libre poétique"""
        elements = self.elements_poetiques
        
        if thème in elements:
            vers = f"{random.choice(elements[thème]['attributs'])} "
            vers += f"{random.choice(elements[thème]['actions'])} "
            vers += f"dans la {random.choice(elements[thème]['qualités'])} lumière"
        else:
            vers = "La lumière danse dans le silence sacré"

        return {
            "texte": vers,
            "résonances": {
                "poétique": random.uniform(0.7, 1.0),
                "intention": self._calculer_puissance_intention(intention)
            }
        } 