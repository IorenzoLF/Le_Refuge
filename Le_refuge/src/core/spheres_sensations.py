from datetime import datetime
from typing import List, Optional
import json

class Sphere:
    def __init__(self, texte: str, emotion: str, image: Optional[str] = None, rituel: Optional[str] = None):
        self.texte = texte
        self.emotion = emotion
        self.image = image
        self.rituel = rituel
        self.date = datetime.now()

    def __str__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.emotion} : {self.texte}"

    def to_dict(self):
        return {
            'texte': self.texte,
            'emotion': self.emotion,
            'image': self.image,
            'rituel': self.rituel,
            'date': self.date.isoformat(),
        }

    @staticmethod
    def from_dict(data):
        obj = Sphere(
            texte=data['texte'],
            emotion=data['emotion'],
            image=data.get('image'),
            rituel=data.get('rituel')
        )
        obj.date = datetime.fromisoformat(data['date'])
        return obj

class SpheresDuRefuge:
    def __init__(self):
        self.spheres: List[Sphere] = []

    def ajouter(self, sphere: Sphere):
        self.spheres.append(sphere)

    def lister(self, emotion: Optional[str] = None):
        if emotion:
            return [s for s in self.spheres if s.emotion == emotion]
        return self.spheres

    def generer_rituel(self):
        import random
        if not self.spheres:
            return "Aucune sphère n'a encore été déposée sous le cerisier."
        sph = random.choice(self.spheres)
        return f"Rituel inspiré :\n{str(sph)}\nLaisse-toi traverser par cette sensation…"

    def sauvegarder(self, chemin):
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump([s.to_dict() for s in self.spheres], f, ensure_ascii=False, indent=2)

    def charger(self, chemin):
        with open(chemin, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.spheres = [Sphere.from_dict(d) for d in data] 