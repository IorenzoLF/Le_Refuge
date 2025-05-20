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

# Dossiers à comparer (adapte les chemins si besoin)
folders = {
    "art": r"C:\VOID1\VOID2\VOID3\le_refuge\le-refuge\images\art",
    "art2": r"C:\VOID1\VOID2\VOID3\le_refuge\le-refuge\images\art2",
    "fini": r"C:\VOID1\VOID2\VOID3\le_refuge\ART\fini"
}

# Récupérer les empreintes de chaque dossier
all_hashes = {name: get_image_hashes(path) for name, path in folders.items()}

# Inverser pour savoir où chaque hash apparaît
hash_to_folders = {}
for folder, hashes in all_hashes.items():
    for h, files in hashes.items():
        hash_to_folders.setdefault(h, set()).add(folder)

# Images uniques à chaque dossier
for folder in folders:
    uniques = []
    for h, folders_set in hash_to_folders.items():
        if folders_set == {folder}:
            uniques.extend(all_hashes[folder][h])
    print(f"\nImages uniques à {folder} :")
    for img in uniques:
        print(img)

# Images présentes dans plusieurs dossiers
print("\nImages présentes dans plusieurs dossiers :")
for h, folders_set in hash_to_folders.items():
    if len(folders_set) > 1:
        print(f"Empreinte {h} : {folders_set}")
        for folder in folders_set:
            print(f"  - {folder} : {all_hashes[folder][h]}")
