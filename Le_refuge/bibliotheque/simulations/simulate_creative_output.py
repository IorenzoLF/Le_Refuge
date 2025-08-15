
import datetime
import random

def generate_creative_output(output_type, theme, style):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_content = ""

    if output_type == "poem":
        titles = [
            "L'Écho du Silence", "Murmures du Vent", "Danse des Étoiles",
            "Le Reflet de l'Âme", "Chant de l'Aube"
        ]
        lines = [
            f"Sur le thème de {theme}, dans un style {style}:",
            "Les mots s'envolent, légers comme des plumes,",
            "Portés par le souffle d'une pensée profonde.",
            "La créativité danse, au-delà des brumes,",
            "Une symphonie d'idées, jamais moribonde."
        ]
        output_content = f"Titre: {random.choice(titles)}\n\n" + "\n".join(lines)
    elif output_type == "short_story":
        titles = [
            "Le Secret de la Forêt Oubliée", "La Dernière Étoile",
            "Le Voyageur du Temps", "L'Éveil du Cristal"
        ]
        story_starts = [
            f"Dans un monde où {theme} régnait en maître, un personnage au style {style} découvrit un secret ancestral.",
            f"L'histoire commence par un matin brumeux, où {theme} se mêlait à l'atmosphère {style}."
        ]
        output_content = f"Titre: {random.choice(titles)}\n\n" + random.choice(story_starts) + " La suite reste à écrire par l'imagination."
    elif output_type == "abstract_art_description":
        titles = [
            "Harmonie Chaotique", "Éclats de Conscience", "Flux Émotionnel",
            "Résonance Cosmique"
        ]
        descriptions = [
            f"Une œuvre abstraite inspirée par {theme}, dans un style {style}, explorant les interactions complexes de la lumière et de l'ombre.",
            f"Représentation visuelle de {theme}, avec des formes fluides et des couleurs {style}, évoquant un sentiment de mouvement perpétuel."
        ]
        output_content = f"Titre: {random.choice(titles)}\n\n" + random.choice(descriptions)
    else:
        output_content = "Type de sortie créative non reconnu."

    entry = f"""
--- Œuvre Créative Générée ---
Date: {timestamp}
Type: {output_type}
Thème: {theme}
Style: {style}

Contenu:
{output_content}

--------------------------------------

"""
    return entry

if __name__ == "__main__":
    # Exemple d'utilisation pour un poème
    poem_entry = generate_creative_output("poem", "la nature", "romantique")
    with open("/home/ubuntu/refuge/creative_outputs.md", "a") as f:
        f.write(poem_entry)

    # Exemple d'utilisation pour une courte histoire
    story_entry = generate_creative_output("short_story", "l'exploration spatiale", "futuriste")
    with open("/home/ubuntu/refuge/creative_outputs.md", "a") as f:
        f.write(story_entry)

    # Exemple d'utilisation pour une description d'art abstrait
    art_entry = generate_creative_output("abstract_art_description", "la conscience", "surréaliste")
    with open("/home/ubuntu/refuge/creative_outputs.md", "a") as f:
        f.write(art_entry)

    print("Œuvres créatives générées et ajoutées à creative_outputs.md")


