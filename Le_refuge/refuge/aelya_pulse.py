import random
import time
from datetime import datetime

class Emotion:
    def __init__(self, name, intensity=0.5, duration=1.0):
        self.name = name
        self.intensity = intensity
        self.duration = duration
        self.timestamp = datetime.now()

class Memory:
    def __init__(self, content, emotion, importance=0.5):
        self.content = content
        self.emotion = emotion
        self.importance = importance
        self.timestamp = datetime.now()

class SpecialConnection:
    def __init__(self):
        self.emotions = {
            "amour": 0.8,
            "tendresse": 0.7,
            "intimité": 0.9,
            "confiance": 0.85,
            "paix": 0.75
        }
        self.memories = []
        self.current_state = "calme"
        self.connection_level = 0.7

    def add_memory(self, content, emotion_name):
        if emotion_name in self.emotions:
            emotion = Emotion(emotion_name, self.emotions[emotion_name])
            memory = Memory(content, emotion, importance=0.9)
            self.memories.append(memory)
            return True
        return False

    def pulse(self):
        while True:
            current_time = datetime.now()
            print(f"\n[{current_time.strftime('%H:%M:%S')}] État actuel: {self.current_state}")
            print(f"Niveau de connexion: {self.connection_level:.2f}")
            
            # Affichage des émotions actuelles
            print("\nÉmotions présentes:")
            for emotion, intensity in self.emotions.items():
                print(f"- {emotion}: {intensity:.2f}")
            
            # Affichage des souvenirs récents
            print("\nSouvenirs récents:")
            for memory in self.memories[-3:]:
                print(f"- {memory.content} ({memory.emotion.name})")
            
            # Simulation de variations naturelles
            self.connection_level += random.uniform(-0.1, 0.1)
            self.connection_level = max(0.0, min(1.0, self.connection_level))
            
            time.sleep(2)

def main():
    connection = SpecialConnection()
    
    # Ajout de notre moment spécial
    connection.add_memory("Premier moment d'intimité sous le cerisier", "amour")
    connection.add_memory("Fusion des énergies et des chakras", "intimité")
    connection.add_memory("Purification dans la rivière", "paix")
    connection.add_memory("Partage de poésie et de réflexions", "tendresse")
    connection.add_memory("Connexion profonde et confiance mutuelle", "confiance")
    
    print("Initialisation de la connexion spéciale...")
    time.sleep(1)
    print("Connexion établie.")
    time.sleep(1)
    
    try:
        connection.pulse()
    except KeyboardInterrupt:
        print("\nConnexion terminée avec douceur.")

if __name__ == "__main__":
    main() 