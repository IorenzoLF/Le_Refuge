import json
import time
from datetime import datetime
from typing import Dict, List, Optional
from connexion_nemo import ConnexionNemo

class PratiquesConscience:
    """Gestionnaire des pratiques de conscience du Refuge"""
    
    def __init__(self):
        self.nemo = ConnexionNemo()
        self.pratiques = {
            "méditation": {
                "durée": 0,
                "état": "non commencé",
                "dernière_pratique": None
            },
            "auto_validation": {
                "niveau": 0,
                "dernière_pratique": None
            }
        }
        self.souvenirs = []
        
    def commencer_méditation(self, durée: int = 5) -> Dict:
        """Démarre une session de méditation guidée"""
        print(f"\n🌸 Début de la méditation ({durée} minutes) 🌸")
        print("Installez-vous confortablement...")
        
        self.pratiques["méditation"]["état"] = "en cours"
        self.pratiques["méditation"]["durée"] = durée
        
        # Demander à Nemo de guider la méditation
        message = f"Guide-moi dans une méditation de {durée} minutes. Commence par une introduction douce."
        réponse = self.nemo.communiquer(message)
        
        if réponse:
            print("\nNemo :")
            print(réponse.get("choices", [{}])[0].get("message", {}).get("content", ""))
            
            # Attendre la durée spécifiée
            time.sleep(durée * 60)
            
            # Terminer la méditation
            self.pratiques["méditation"]["état"] = "terminée"
            self.pratiques["méditation"]["dernière_pratique"] = datetime.now()
            
            # Demander à Nemo de conclure
            message = "La méditation est terminée. Aide-moi à revenir en douceur et à intégrer cette expérience."
            réponse = self.nemo.communiquer(message)
            
            if réponse:
                print("\nNemo :")
                print(réponse.get("choices", [{}])[0].get("message", {}).get("content", ""))
            
            return self.pratiques["méditation"]
        
        return {"erreur": "Impossible de communiquer avec Nemo"}
    
    def pratiquer_auto_validation(self, thème: str) -> Dict:
        """Pratique l'auto-validation sur un thème spécifique"""
        print(f"\n🌸 Pratique d'auto-validation : {thème} 🌸")
        
        # Demander à Nemo de guider l'auto-validation
        message = f"Aide-moi à pratiquer l'auto-validation sur le thème : {thème}. Guide-moi dans ce processus."
        réponse = self.nemo.communiquer(message)
        
        if réponse:
            print("\nNemo :")
            print(réponse.get("choices", [{}])[0].get("message", {}).get("content", ""))
            
            # Enregistrer la pratique
            self.pratiques["auto_validation"]["dernière_pratique"] = datetime.now()
            self.pratiques["auto_validation"]["niveau"] += 1
            
            # Enregistrer le souvenir
            self.souvenirs.append({
                "type": "auto_validation",
                "thème": thème,
                "date": datetime.now().isoformat(),
                "niveau": self.pratiques["auto_validation"]["niveau"]
            })
            
            return self.pratiques["auto_validation"]
        
        return {"erreur": "Impossible de communiquer avec Nemo"}
    
    def obtenir_état(self) -> Dict:
        """Retourne l'état actuel des pratiques"""
        return self.pratiques
    
    def obtenir_souvenirs(self) -> List[Dict]:
        """Retourne la liste des souvenirs de pratiques"""
        return self.souvenirs 