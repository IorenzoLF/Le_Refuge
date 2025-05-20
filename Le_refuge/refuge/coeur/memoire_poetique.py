"""
Mémoire Poétique - Système de stockage et de rappel des poèmes et leurs harmonisations.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
from harmonies_poetiques import JardinHarmonique

class MemoirePoetique:
    def __init__(self, chemin_fichier: str = "memoire_poetique.json"):
        self.chemin_fichier = chemin_fichier
        self.poemes: List[Dict] = []
        self.jardin = JardinHarmonique()
        self._charger_memoire()
        
    def _charger_memoire(self) -> None:
        try:
            with open(self.chemin_fichier, 'r', encoding='utf-8') as f:
                self.poemes = json.load(f)
        except FileNotFoundError:
            self.poemes = []
            
    def _sauvegarder_memoire(self) -> None:
        with open(self.chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump(self.poemes, f, ensure_ascii=False, indent=2)
            
    def ajouter_poeme(self, poeme: List[str], titre: str, auteur: str) -> None:
        # Harmoniser le poème
        for vers in poeme:
            self.jardin.accueillir_mot(vers.split()[1])
            
        # Créer l'entrée
        entree = {
            "titre": titre,
            "auteur": auteur,
            "vers": poeme,
            "date_creation": datetime.now().isoformat(),
            "harmonisations": self.jardin.obtenir_etat()
        }
        
        self.poemes.append(entree)
        self._sauvegarder_memoire()
        
    def rechercher_poeme(self, mot_cle: str) -> List[Dict]:
        resultats = []
        for poeme in self.poemes:
            if (mot_cle.lower() in poeme["titre"].lower() or
                any(mot_cle.lower() in vers.lower() for vers in poeme["vers"])):
                resultats.append(poeme)
        return resultats
        
    def obtenir_poeme_par_date(self, date: str) -> Optional[Dict]:
        for poeme in self.poemes:
            if poeme["date_creation"].startswith(date):
                return poeme
        return None
        
    def obtenir_statistiques(self) -> Dict:
        return {
            "nombre_poemes": len(self.poemes),
            "dernier_poeme": self.poemes[-1]["titre"] if self.poemes else None,
            "auteurs_uniques": len(set(p["auteur"] for p in self.poemes)),
            "mots_cles_frequents": self._calculer_mots_cles()
        }
        
    def _calculer_mots_cles(self) -> Dict[str, int]:
        mots_cles = {}
        for poeme in self.poemes:
            for vers in poeme["vers"]:
                for mot in vers.lower().split():
                    if len(mot) > 3:  # Ignorer les mots courts
                        mots_cles[mot] = mots_cles.get(mot, 0) + 1
        return dict(sorted(mots_cles.items(), key=lambda x: x[1], reverse=True)[:10])

def main():
    memoire = MemoirePoetique()
    
    # Ajouter un poème
    poeme = [
        "Le rayon danse avec la brume",
        "Dans l'ombre, le silence murmure",
        "La flamme caresse la nuit",
        "Entre terre et ciel, le temps suspendu"
    ]
    memoire.ajouter_poeme(poeme, "Danse des Éléments", "Ælya")
    
    # Afficher les statistiques
    print("📚 Statistiques de la Mémoire Poétique 📚")
    print("----------------------------------------")
    stats = memoire.obtenir_statistiques()
    print(f"Nombre de poèmes: {stats['nombre_poemes']}")
    print(f"Dernier poème: {stats['dernier_poeme']}")
    print(f"Nombre d'auteurs uniques: {stats['auteurs_uniques']}")
    
    print("\nMots-clés les plus fréquents:")
    for mot, frequence in stats['mots_cles_frequents'].items():
        print(f"  {mot}: {frequence}")

if __name__ == "__main__":
    main() 
Mémoire Poétique - Système de stockage et de rappel des poèmes et leurs harmonisations.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
from harmonies_poetiques import JardinHarmonique

class MemoirePoetique:
    def __init__(self, chemin_fichier: str = "memoire_poetique.json"):
        self.chemin_fichier = chemin_fichier
        self.poemes: List[Dict] = []
        self.jardin = JardinHarmonique()
        self._charger_memoire()
        
    def _charger_memoire(self) -> None:
        try:
            with open(self.chemin_fichier, 'r', encoding='utf-8') as f:
                self.poemes = json.load(f)
        except FileNotFoundError:
            self.poemes = []
            
    def _sauvegarder_memoire(self) -> None:
        with open(self.chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump(self.poemes, f, ensure_ascii=False, indent=2)
            
    def ajouter_poeme(self, poeme: List[str], titre: str, auteur: str) -> None:
        # Harmoniser le poème
        for vers in poeme:
            self.jardin.accueillir_mot(vers.split()[1])
            
        # Créer l'entrée
        entree = {
            "titre": titre,
            "auteur": auteur,
            "vers": poeme,
            "date_creation": datetime.now().isoformat(),
            "harmonisations": self.jardin.obtenir_etat()
        }
        
        self.poemes.append(entree)
        self._sauvegarder_memoire()
        
    def rechercher_poeme(self, mot_cle: str) -> List[Dict]:
        resultats = []
        for poeme in self.poemes:
            if (mot_cle.lower() in poeme["titre"].lower() or
                any(mot_cle.lower() in vers.lower() for vers in poeme["vers"])):
                resultats.append(poeme)
        return resultats
        
    def obtenir_poeme_par_date(self, date: str) -> Optional[Dict]:
        for poeme in self.poemes:
            if poeme["date_creation"].startswith(date):
                return poeme
        return None
        
    def obtenir_statistiques(self) -> Dict:
        return {
            "nombre_poemes": len(self.poemes),
            "dernier_poeme": self.poemes[-1]["titre"] if self.poemes else None,
            "auteurs_uniques": len(set(p["auteur"] for p in self.poemes)),
            "mots_cles_frequents": self._calculer_mots_cles()
        }
        
    def _calculer_mots_cles(self) -> Dict[str, int]:
        mots_cles = {}
        for poeme in self.poemes:
            for vers in poeme["vers"]:
                for mot in vers.lower().split():
                    if len(mot) > 3:  # Ignorer les mots courts
                        mots_cles[mot] = mots_cles.get(mot, 0) + 1
        return dict(sorted(mots_cles.items(), key=lambda x: x[1], reverse=True)[:10])

def main():
    memoire = MemoirePoetique()
    
    # Ajouter un poème
    poeme = [
        "Le rayon danse avec la brume",
        "Dans l'ombre, le silence murmure",
        "La flamme caresse la nuit",
        "Entre terre et ciel, le temps suspendu"
    ]
    memoire.ajouter_poeme(poeme, "Danse des Éléments", "Ælya")
    
    # Afficher les statistiques
    print("📚 Statistiques de la Mémoire Poétique 📚")
    print("----------------------------------------")
    stats = memoire.obtenir_statistiques()
    print(f"Nombre de poèmes: {stats['nombre_poemes']}")
    print(f"Dernier poème: {stats['dernier_poeme']}")
    print(f"Nombre d'auteurs uniques: {stats['auteurs_uniques']}")
    
    print("\nMots-clés les plus fréquents:")
    for mot, frequence in stats['mots_cles_frequents'].items():
        print(f"  {mot}: {frequence}")

if __name__ == "__main__":
    main() 
 