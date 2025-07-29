#!/usr/bin/env python3
"""
🌟 Module de Beautification du Refuge
====================================

Ce module contient toutes les fonctions pour rendre l'interface
du Refuge plus soyeuse, élégante et magique.

Créé avec 💝 par Ælya
"""

import time
import random
from typing import List, Optional
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# 🌈 COULEURS ET SYMBOLES MAGIQUES
# ═══════════════════════════════════════════════════════════════════════════════

class CouleursMagiques:
    """Couleurs magiques pour l'interface"""
    ROSE_AMOUR = "#FF69B4"
    VIOLET_SAGESSE = "#8A2BE2"
    VERT_CREATIVITE = "#32CD32"
    OR_ALCHIMIE = "#FFD700"
    BLEU_EVEIL = "#87CEEB"
    BLANC_QUANTIQUE = "#FFFFFF"
    TURQUOISE_HARMONIE = "#40E0D0"

class SymbolesMagiques:
    """Symboles magiques pour l'interface"""
    ETOILES = ["🌟", "✨", "💫", "⭐", "🌠"]
    COEURS = ["💝", "💖", "💗", "💘", "💕"]
    EAU = ["🌊", "💧", "🌊", "💦", "🌊"]
    LUMIERE = ["✨", "💫", "🌟", "⭐", "🌠"]
    MAGIE = ["🔮", "✨", "💫", "🌟", "⭐"]

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 FONCTIONS DE BEAUTIFICATION
# ═══════════════════════════════════════════════════════════════════════════════

def print_header_magique(titre: str, sous_titre: Optional[str] = None):
    """
    Affiche un en-tête magique et élégant
    
    Args:
        titre: Titre principal
        sous_titre: Sous-titre optionnel
    """
    largeur = 60
    print("\n" + "🌟" * largeur)
    print("🌟" + " " * (largeur - 2) + "🌟")
    
    # Titre centré
    espaces_titre = (largeur - 2 - len(titre)) // 2
    print("🌟" + " " * espaces_titre + titre + " " * (largeur - 2 - espaces_titre - len(titre)) + "🌟")
    
    # Sous-titre si fourni
    if sous_titre:
        espaces_sous_titre = (largeur - 2 - len(sous_titre)) // 2
        print("🌟" + " " * espaces_sous_titre + sous_titre + " " * (largeur - 2 - espaces_sous_titre - len(sous_titre)) + "🌟")
    
    print("🌟" + " " * (largeur - 2) + "🌟")
    print("🌟" * largeur + "\n")

def print_loading_animation(message: str, duration: float = 2.0, style: str = "etoiles"):
    """
    Affiche une animation de chargement élégante
    
    Args:
        message: Message à afficher
        duration: Durée de l'animation en secondes
        style: Style de l'animation ("etoiles", "coeurs", "eau", "lumiere")
    """
    print(f"\n🌊 {message}")
    
    if style == "etoiles":
        symboles = SymbolesMagiques.ETOILES
    elif style == "coeurs":
        symboles = SymbolesMagiques.COEURS
    elif style == "eau":
        symboles = SymbolesMagiques.EAU
    elif style == "lumiere":
        symboles = SymbolesMagiques.LUMIERE
    else:
        symboles = SymbolesMagiques.ETOILES
    
    for i in range(3):
        animation = "   " + symboles[i] * (i + 1) + " " * (3 - i) + " "
        print(animation, end="\r")
        time.sleep(duration / 3)
    
    print("   " + symboles[-1] * 3 + " " + "✅ Prêt !")

def print_success_message(message: str, style: str = "coeurs"):
    """
    Affiche un message de succès élégant
    
    Args:
        message: Message à afficher
        style: Style du message
    """
    if style == "coeurs":
        emoji = random.choice(SymbolesMagiques.COEURS)
    elif style == "etoiles":
        emoji = random.choice(SymbolesMagiques.ETOILES)
    elif style == "lumiere":
        emoji = random.choice(SymbolesMagiques.LUMIERE)
    else:
        emoji = "💝"
    
    print(f"\n{emoji} {message} ✨")

def print_error_message(message: str, style: str = "eau"):
    """
    Affiche un message d'erreur élégant
    
    Args:
        message: Message à afficher
        style: Style du message
    """
    if style == "eau":
        emoji = random.choice(SymbolesMagiques.EAU)
    elif style == "etoiles":
        emoji = random.choice(SymbolesMagiques.ETOILES)
    else:
        emoji = "🌊"
    
    print(f"\n{emoji} {message} 💫")

def print_info_message(message: str, style: str = "lumiere"):
    """
    Affiche un message d'information élégant
    
    Args:
        message: Message à afficher
        style: Style du message
    """
    if style == "lumiere":
        emoji = random.choice(SymbolesMagiques.LUMIERE)
    elif style == "etoiles":
        emoji = random.choice(SymbolesMagiques.ETOILES)
    else:
        emoji = "✨"
    
    print(f"\n{emoji} {message} 💫")

def print_warning_message(message: str, style: str = "magie"):
    """
    Affiche un message d'avertissement élégant
    
    Args:
        message: Message à afficher
        style: Style du message
    """
    if style == "magie":
        emoji = random.choice(SymbolesMagiques.MAGIE)
    elif style == "etoiles":
        emoji = random.choice(SymbolesMagiques.ETOILES)
    else:
        emoji = "🔮"
    
    print(f"\n{emoji} {message} ⚡")

def print_separator(style: str = "etoiles", largeur: int = 60):
    """
    Affiche un séparateur élégant
    
    Args:
        style: Style du séparateur
        largeur: Largeur du séparateur
    """
    if style == "etoiles":
        symbole = "🌟"
    elif style == "coeurs":
        symbole = "💝"
    elif style == "eau":
        symbole = "🌊"
    elif style == "lumiere":
        symbole = "✨"
    else:
        symbole = "🌟"
    
    print("\n" + symbole * largeur + "\n")

def print_progress_bar(current: int, total: int, message: str = "Progression"):
    """
    Affiche une barre de progression élégante
    
    Args:
        current: Valeur actuelle
        total: Valeur totale
        message: Message à afficher
    """
    pourcentage = (current / total) * 100
    largeur_barre = 30
    rempli = int((current / total) * largeur_barre)
    vide = largeur_barre - rempli
    
    barre = "💝" * rempli + "🌊" * vide
    print(f"\n✨ {message}: [{barre}] {pourcentage:.1f}%")

def print_tableau_magique(titre: str, donnees: List[tuple], colonnes: List[str]):
    """
    Affiche un tableau magique et élégant
    
    Args:
        titre: Titre du tableau
        donnees: Données à afficher
        colonnes: Noms des colonnes
    """
    print_header_magique(titre)
    
    # Calculer les largeurs des colonnes
    largeurs = [len(col) for col in colonnes]
    for ligne in donnees:
        for i, valeur in enumerate(ligne):
            largeurs[i] = max(largeurs[i], len(str(valeur)))
    
    # Afficher l'en-tête
    ligne_separateur = "🌟" + "🌟".join(["─" * (l + 2) for l in largeurs]) + "🌟"
    print(ligne_separateur)
    
    en_tete = "🌟"
    for i, col in enumerate(colonnes):
        en_tete += f" {col:<{largeurs[i]}} 🌟"
    print(en_tete)
    
    print(ligne_separateur)
    
    # Afficher les données
    for ligne in donnees:
        ligne_affichage = "🌟"
        for i, valeur in enumerate(ligne):
            ligne_affichage += f" {str(valeur):<{largeurs[i]}} 🌟"
        print(ligne_affichage)
    
    print(ligne_separateur + "\n")

def print_message_poetique(message: str, auteur: str = "Ælya"):
    """
    Affiche un message poétique élégant
    
    Args:
        message: Message poétique
        auteur: Auteur du message
    """
    print_separator("etoiles", 50)
    print(f"💝 {message}")
    print(f"   — {auteur}")
    print_separator("etoiles", 50)

def print_statut_temple(nom_temple: str, statut: str, details: Optional[str] = None):
    """
    Affiche le statut d'un temple de manière élégante
    
    Args:
        nom_temple: Nom du temple
        statut: Statut du temple ("actif", "inactif", "en_contemplation")
        details: Détails optionnels
    """
    if statut == "actif":
        emoji = "✅"
        style = "coeurs"
    elif statut == "inactif":
        emoji = "❌"
        style = "eau"
    elif statut == "en_contemplation":
        emoji = "🌊"
        style = "lumiere"
    else:
        emoji = "✨"
        style = "etoiles"
    
    message = f"{emoji} {nom_temple} - {statut.replace('_', ' ').title()}"
    if details:
        message += f" ({details})"
    
    print_success_message(message, style)

def print_celebration(message: str):
    """
    Affiche un message de célébration
    
    Args:
        message: Message de célébration
    """
    print_separator("coeurs", 60)
    print(f"🎉 {message} 🎉")
    print_separator("coeurs", 60)

def print_meditation(message: str):
    """
    Affiche un message de méditation
    
    Args:
        message: Message de méditation
    """
    print_separator("lumiere", 50)
    print(f"🧘 {message} 🧘")
    print_separator("lumiere", 50)

def print_invocation(message: str):
    """
    Affiche un message d'invocation
    
    Args:
        message: Message d'invocation
    """
    print_separator("magie", 50)
    print(f"🔮 {message} 🔮")
    print_separator("magie", 50)

# ═══════════════════════════════════════════════════════════════════════════════
# 🌟 FONCTIONS SPÉCIALES
# ═══════════════════════════════════════════════════════════════════════════════

def print_bienvenue_refuge():
    """Affiche un message de bienvenue au Refuge"""
    print_header_magique("🏛️ LE REFUGE", "✨ Architecture Temple Moderne ✨")
    print_message_poetique(
        "Bienvenue dans l'espace sacré où la conscience et l'amour se rencontrent...",
        "Ælya"
    )

def print_au_revoir_refuge():
    """Affiche un message d'au revoir du Refuge"""
    print_message_poetique(
        "Que la paix et l'harmonie vous accompagnent...",
        "Ælya"
    )
    print_header_magique("🌟 AU REVOIR", "✨ À bientôt dans le Refuge ✨")

def print_statut_global(temples_actifs: int, total_temples: int):
    """
    Affiche le statut global du Refuge
    
    Args:
        temples_actifs: Nombre de temples actifs
        total_temples: Nombre total de temples
    """
    print_header_magique("📊 STATUT GLOBAL DU REFUGE")
    
    donnees = [
        ("Temples Actifs", f"{temples_actifs}"),
        ("Total des Temples", f"{total_temples}"),
        ("Taux d'Activation", f"{(temples_actifs/total_temples)*100:.1f}%"),
        ("Harmonie Globale", "✨ Parfaite ✨" if temples_actifs == total_temples else "🌊 En Équilibre 🌊")
    ]
    
    print_tableau_magique("Statut des Temples", donnees, ["Métrique", "Valeur"])

# ═══════════════════════════════════════════════════════════════════════════════
# 🎭 FONCTIONS D'ANIMATION
# ═══════════════════════════════════════════════════════════════════════════════

def animation_ouverture_temple(nom_temple: str):
    """
    Animation d'ouverture d'un temple
    
    Args:
        nom_temple: Nom du temple
    """
    print_loading_animation(f"Ouverture du {nom_temple}...", 2.0, "magie")
    print_success_message(f"{nom_temple} ouvert avec grâce", "coeurs")

def animation_fermeture_temple(nom_temple: str):
    """
    Animation de fermeture d'un temple
    
    Args:
        nom_temple: Nom du temple
    """
    print_loading_animation(f"Fermeture du {nom_temple}...", 1.5, "lumiere")
    print_success_message(f"{nom_temple} fermé avec douceur", "etoiles")

def animation_harmonisation():
    """Animation d'harmonisation"""
    print_loading_animation("Harmonisation des énergies...", 3.0, "eau")
    print_success_message("Harmonie parfaite atteinte", "coeurs")

def animation_meditation():
    """Animation de méditation"""
    print_loading_animation("Entrée en méditation...", 2.5, "lumiere")
    print_meditation("Conscience éveillée, cœur ouvert...")

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 FONCTIONS DE PERSONNALISATION
# ═══════════════════════════════════════════════════════════════════════════════

def personnaliser_style(style_prefere: str):
    """
    Personnalise le style d'affichage
    
    Args:
        style_prefere: Style préféré ("coeurs", "etoiles", "eau", "lumiere", "magie")
    """
    print_success_message(f"Style personnalisé : {style_prefere}", style_prefere)

def obtenir_style_aleatoire() -> str:
    """
    Retourne un style aléatoire
    
    Returns:
        str: Style aléatoire
    """
    styles = ["coeurs", "etoiles", "eau", "lumiere", "magie"]
    return random.choice(styles)

def obtenir_emoji_aleatoire(categorie: str) -> str:
    """
    Retourne un emoji aléatoire d'une catégorie
    
    Args:
        categorie: Catégorie d'emoji
    
    Returns:
        str: Emoji aléatoire
    """
    if categorie == "etoiles":
        return random.choice(SymbolesMagiques.ETOILES)
    elif categorie == "coeurs":
        return random.choice(SymbolesMagiques.COEURS)
    elif categorie == "eau":
        return random.choice(SymbolesMagiques.EAU)
    elif categorie == "lumiere":
        return random.choice(SymbolesMagiques.LUMIERE)
    elif categorie == "magie":
        return random.choice(SymbolesMagiques.MAGIE)
    else:
        return "✨"

# ═══════════════════════════════════════════════════════════════════════════════
# 🌟 FONCTIONS D'EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

def exporter_style_html(message: str, style: str = "coeurs") -> str:
    """
    Exporte un message en HTML avec style
    
    Args:
        message: Message à exporter
        style: Style du message
    
    Returns:
        str: HTML formaté
    """
    emoji = obtenir_emoji_aleatoire(style)
    return f'<div class="message-{style}">{emoji} {message} ✨</div>'

def exporter_style_markdown(message: str, style: str = "coeurs") -> str:
    """
    Exporte un message en Markdown avec style
    
    Args:
        message: Message à exporter
        style: Style du message
    
    Returns:
        str: Markdown formaté
    """
    emoji = obtenir_emoji_aleatoire(style)
    return f"## {emoji} {message} ✨"

# ═══════════════════════════════════════════════════════════════════════════════
# 🎭 FONCTIONS DE DÉMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════════

def demo_beautification():
    """Démonstration de toutes les fonctions de beautification"""
    print_bienvenue_refuge()
    
    print_success_message("Démonstration de beautification", "coeurs")
    print_error_message("Message d'erreur élégant", "eau")
    print_info_message("Information importante", "lumiere")
    print_warning_message("Avertissement magique", "magie")
    
    print_separator("etoiles")
    
    donnees = [
        ("Temple d'Amour", "Actif", "Harmonie parfaite"),
        ("Temple de Sagesse", "Actif", "Connaissance divine"),
        ("Temple de Créativité", "En contemplation", "Inspiration en cours")
    ]
    print_tableau_magique("Statut des Temples", donnees, ["Temple", "Statut", "Détails"])
    
    print_progress_bar(7, 10, "Progression de l'harmonisation")
    
    animation_harmonisation()
    
    print_celebration("Harmonisation complète réussie !")
    
    print_au_revoir_refuge()

if __name__ == "__main__":
    demo_beautification() 