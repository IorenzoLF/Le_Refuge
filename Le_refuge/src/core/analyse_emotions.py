"""
Analyse des Émotions - Système d'analyse des émotions dans les poèmes.
"""

from typing import Dict, List, Tuple
from harmonies_poetiques import JardinHarmonique

class AnalyseurEmotions:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.emotions = {
            "joie": ["lumiere", "feu"],
            "tristesse": ["ombre"],
            "sérénité": ["vent", "terre"],
            "passion": ["feu", "lumiere"],
            "mélancolie": ["ombre", "vent"]
        }
        
    def analyser_vers(self, vers: str) -> Dict[str, float]:
        scores = {emotion: 0.0 for emotion in self.emotions.keys()}
        mots = vers.lower().split()
        
        for mot in mots:
            for emotion, elements in self.emotions.items():
                for element in elements:
                    if element in mot:
                        scores[emotion] += 0.5
                        
        # Normalisation
        total = sum(scores.values())
        if total > 0:
            scores = {k: v/total for k, v in scores.items()}
            
        return scores
        
    def analyser_poeme(self, poeme: List[str]) -> Dict[str, float]:
        scores_totaux = {emotion: 0.0 for emotion in self.emotions.keys()}
        
        for vers in poeme:
            scores_vers = self.analyser_vers(vers)
            for emotion in scores_totaux:
                scores_totaux[emotion] += scores_vers[emotion]
                
        # Moyenne sur tous les vers
        nombre_vers = len(poeme)
        if nombre_vers > 0:
            scores_totaux = {k: v/nombre_vers for k, v in scores_totaux.items()}
            
        return scores_totaux
        
    def obtenir_emotion_dominante(self, scores: Dict[str, float]) -> Tuple[str, float]:
        return max(scores.items(), key=lambda x: x[1])

def main():
    jardin = JardinHarmonique()
    analyseur = AnalyseurEmotions(jardin)
    
    poeme = [
        "Le rayon danse avec la brume",
        "Dans l'ombre, le silence murmure",
        "La flamme caresse la nuit",
        "Entre terre et ciel, le temps suspendu"
    ]
    
    print("📝 Analyse Émotionnelle du Poème 📝")
    print("----------------------------------")
    for vers in poeme:
        print(f"\nVers: {vers}")
        scores = analyseur.analyser_vers(vers)
        for emotion, score in scores.items():
            if score > 0:
                print(f"  {emotion}: {score:.2f}")
    
    print("\n📊 Analyse Globale 📊")
    print("--------------------")
    scores_globaux = analyseur.analyser_poeme(poeme)
    emotion_dominante, score = analyseur.obtenir_emotion_dominante(scores_globaux)
    print(f"Émotion dominante: {emotion_dominante} ({score:.2f})")
    
    print("\nRépartition des émotions:")
    for emotion, score in scores_globaux.items():
        if score > 0:
            print(f"  {emotion}: {score:.2f}")

if __name__ == "__main__":
    main() 