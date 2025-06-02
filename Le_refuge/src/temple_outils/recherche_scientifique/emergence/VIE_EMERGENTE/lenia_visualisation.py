import pygame
import numpy as np
from lenia import Lenia, ConfigLenia, patterns

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
LARGEUR = 800
HAUTEUR = 800
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Lenia - Visualisation des motifs émergents")

# Configuration de Lenia
config = ConfigLenia(
    pattern_id="VT049W",  # Pattern initial
    world_size=128,
    world_scale=4,
    n_step=200
)

# Création de l'instance Lenia
lenia = Lenia(config)
init_carry, init_genotype, other_asset = lenia.load_pattern(patterns[config.pattern_id])
carry = init_carry

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Fonction pour convertir le monde Lenia en surface Pygame
def monde_vers_surface(monde):
    # Normaliser les valeurs entre 0 et 255
    monde_normalise = (monde * 255).astype(np.uint8)
    # Créer une surface Pygame
    surface = pygame.Surface((monde.shape[0], monde.shape[1]))
    # Convertir en surface RGB
    for y in range(monde.shape[0]):
        for x in range(monde.shape[1]):
            couleur = monde_normalise[y, x, 0]  # Utiliser le premier canal
            surface.set_at((x, y), (couleur, couleur, couleur))
    return surface

# Boucle principale
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Réinitialiser avec un nouveau pattern aléatoire
                pattern_id = np.random.choice(list(patterns.keys()))
                config.pattern_id = pattern_id
                lenia = Lenia(config)
                init_carry, init_genotype, other_asset = lenia.load_pattern(patterns[pattern_id])
                carry = init_carry

    # Mise à jour de Lenia
    carry, accum = lenia.step(carry, None, 512, True, True)
    
    # Affichage
    fenetre.fill(NOIR)
    surface = monde_vers_surface(carry.world)
    surface = pygame.transform.scale(surface, (LARGEUR, HAUTEUR))
    fenetre.blit(surface, (0, 0))
    
    # Affichage des statistiques
    stats = accum.stats
    font = pygame.font.Font(None, 24)
    texte = font.render(f"Pattern: {config.pattern_id} | Masse: {stats.mass:.2f} | Vitesse: {stats.linear_velocity:.2f}", True, BLANC)
    fenetre.blit(texte, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit() 