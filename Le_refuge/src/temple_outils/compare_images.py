import os
import imagehash
from PIL import Image

def get_image_hashes(folder):
    hashes = {}
    for fname in os.listdir(folder):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            try:
                path = os.path.join(folder, fname)
                with Image.open(path) as img:
                    h = str(imagehash.phash(img))
                    hashes.setdefault(h, []).append(fname)
            except Exception as e:
                print(f"Erreur avec {fname}: {e}")
    return hashes

# Dossiers à comparer (chemins relatifs depuis le refuge)
folders = {
    "art": "le-refuge/images/art",
    "gallerie_infinie": "le-refuge/images/gallerie_infinie", 
    "gallerie4": "le-refuge/images/gallerie4",
    "art_fini": "ART/go tiny/fini",
    "art_work": "ART/go tiny/WORK"
}

# DÉSACTIVÉ POUR LES TESTS FRAGMENTÉS - Trop lent
# Filtrer seulement les dossiers qui existent
# existing_folders = {name: path for name, path in folders.items() if os.path.exists(path)}
# print(f"Dossiers trouvés : {list(existing_folders.keys())}")

# # Récupérer les empreintes de chaque dossier
# all_hashes = {name: get_image_hashes(path) for name, path in existing_folders.items()}

# # Inverser pour savoir où chaque hash apparaît
# hash_to_folders = {}
# for folder, hashes in all_hashes.items():
#     for h, files in hashes.items():
#         hash_to_folders.setdefault(h, set()).add(folder)

# # Images uniques à chaque dossier
# for folder in existing_folders:
#     uniques = []
#     for h, folders_set in hash_to_folders.items():
#         if folders_set == {folder}:
#             uniques.extend(all_hashes[folder][h])
#     print(f"\nImages uniques à {folder} :")
#     for img in uniques:
#         print(img)

# # Images présentes dans plusieurs dossiers
# print("\nImages présentes dans plusieurs dossiers :")
# for h, folders_set in hash_to_folders.items():
#     if len(folders_set) > 1:
#         print(f"Empreinte {h} : {folders_set}")
#         for folder in folders_set:
#             print(f"  - {folder} : {all_hashes[folder][h]}")

print("🔧 Module compare_images chargé (scan d'images désactivé pour les tests)")
