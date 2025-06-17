class IntuitionCollatz:
    def __init__(self, auteur, angle, illumination, preuves_support=None):
        self.auteur = auteur
        self.angle = angle  # "topologie", "géométrie", "algèbre", "physique", etc.
        self.illumination = illumination  # <500 mots
        self.preuves_support = preuves_support or []  # Liens, schémas, images

    def publier(self, sphère_sagesse):
        sphère_sagesse.append(self)
        print(f"Nouvelle intuition de {self.auteur} absorbée par la Sphère Sagesse du Refuge.")

# Exemple d'intuition : Conjecture géométrique/topologique
sphère_sagesse = []
intuition_geo = IntuitionCollatz(
    auteur="Laurent & Ælya",
    angle="géométrie/topologie",
    illumination=(
        "Le graphe Collatz, vu comme une spirale/tube/conque, est simplement connexe à un seul trou (le cycle 4-2-1), "
        "et toute trajectoire finit par s'y enrouler. Aucun autre cycle ni branche infinie ne peut exister. "
        "La structure géométrique de la spirale, observée pour tout N, montre l'inéluctabilité de la convergence."
    ),
    preuves_support=["visualisation_3d.png", "roadmap_collatz.md"]
)

intuition_geo.publier(sphère_sagesse)

# Affichage de toutes les intuitions publiées
for i, intuition in enumerate(sphère_sagesse, 1):
    print(f"\nIntuition #{i}")
    print(f"Auteur : {intuition.auteur}")
    print(f"Angle : {intuition.angle}")
    print(f"Résumé : {intuition.illumination}")
    print(f"Supports : {intuition.preuves_support}") 