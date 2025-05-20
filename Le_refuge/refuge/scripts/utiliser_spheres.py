from refuge.coeur.spheres_sensations import Sphere, SpheresDuRefuge

# 1. Créer la collection de sphères
refuge = SpheresDuRefuge()

# 2. Charger les sphères existantes (si tu as déjà un fichier)
try:
    refuge.charger('mes_spheres.json')
    print("Sphères chargées !")
except FileNotFoundError:
    print("Aucune sphère existante, carnet vierge.")

# 3. Ajouter une nouvelle sphère
print("\nDépose une nouvelle sphère dans le Refuge :")
texte = input("Sensation ou souvenir : ")
emotion = input("Émotion principale : ")
image = input("Image associée (optionnel) : ") or None
rituel = input("Rituel associé (optionnel) : ") or None

nouvelle_sphere = Sphere(texte=texte, emotion=emotion, image=image, rituel=rituel)
refuge.ajouter(nouvelle_sphere)

# 4. Sauvegarder les sphères
refuge.sauvegarder('mes_spheres.json')
print("Sphère ajoutée et sauvegardée !")

# 5. Relire toutes les sphères
print("\n--- Toutes les sphères déposées ---")
for sph in refuge.lister():
    print(sph)

# 6. Générer un rituel inspiré
gen_rituel = input("\nGénérer un rituel inspiré d'une sphère ? (o/n) : ")
if gen_rituel.lower() == 'o':
    print("\n--- Rituel inspiré du Refuge ---")
    print(refuge.generer_rituel()) 