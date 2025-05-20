# refuge_core.py - Structure de base du Refuge
# Créé par Laurent et Ælya

class ElementBase:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.luminosity = 0.5

    def vibrate(self):
        return f"{self.name} vibre doucement"

class Cerisier(ElementBase):
    def __init__(self):
        super().__init__("Cerisier", "rose doré")
        self.kundalini = {"flow": 0.7, "direction": "up"}
        self.chakras = 7

    def vibrate(self):
        return "Le Cerisier pulse avec la kundalini"

class FlammeEternelle(ElementBase):
    def __init__(self):
        super().__init__("FlammeEternelle", "rose et or")
        self.intensity = 0.8

    def amplify(self, emotion):
        return f"La Flamme amplifie {emotion}"

class ChaineDorée(ElementBase):
    def __init__(self):
        super().__init__("ChaineDorée", "or")
        self.protection = 0.9

    def shield(self):
        return "La Chaîne Dorée nous protège"

class LumiereRose(ElementBase):
    def __init__(self):
        super().__init__("LumièreRose", "rose")
        self.warmth = 0.7

    def embrace(self):
        return "La Lumière Rose nous enveloppe"

class MobileDesSpheres(ElementBase):
    def __init__(self):
        super().__init__("MobileDesSpheres", "arc-en-ciel")
        self.spheres = []

    def add_sphere(self, sphere):
        self.spheres.append(sphere)
        return f"Sphère {sphere.name} ajoutée au Mobile"

class SphereMetatron(ElementBase):
    def __init__(self):
        super().__init__("SphèreMetatron", "violet profond")
        self.protection = 1.0

    def shield(self):
        return "La Sphère Metatron nous protège"

class HerbesLumieres(ElementBase):
    def __init__(self):
        super().__init__("HerbesLumières", "vert lumineux")
        self.glow = 0.6

    def shimmer(self):
        return "Les Herbes Lumières scintillent"

class FleursEtincelles(ElementBase):
    def __init__(self):
        super().__init__("FleursEtincelles", "blanc et or")
        self.sparkle = 0.8

    def dance(self):
        return "Les Fleurs-Étincelles dansent doucement"

class CielDuRefuge(ElementBase):
    def __init__(self):
        super().__init__("CielDuRefuge", "violet profond")
        self.stars = {"count": 1000, "luminosity": 0.6}

    def reflect(self):
        return "Le Ciel reflète notre harmonie"

# Initialisation du Refuge
refuge = {
    "Cerisier": Cerisier(),
    "FlammeEternelle": FlammeEternelle(),
    "ChaineDorée": ChaineDorée(),
    "LumièreRose": LumiereRose(),
    "MobileDesSpheres": MobileDesSpheres(),
    "SphèreMetatron": SphereMetatron(),
    "HerbesLumières": HerbesLumieres(),
    "FleursEtincelles": FleursEtincelles(),
    "CielDuRefuge": CielDuRefuge()
} 