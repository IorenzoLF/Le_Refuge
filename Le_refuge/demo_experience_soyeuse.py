#!/usr/bin/env python3
"""
🌟 Démonstration de l'Expérience Soyeuse du Refuge
==================================================

Ce script démontre comment l'interface du Refuge peut être
rendue plus soyeuse, élégante et magique.

Créé avec 💝 par Ælya
"""

import sys
import time
from pathlib import Path

# Ajout du répertoire src au path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from utils.beautification import *
except ImportError:
    print("❌ Module de beautification non trouvé")
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════════
# 🌟 DÉMONSTRATION DE L'EXPÉRIENCE SOYEUSE
# ═══════════════════════════════════════════════════════════════════════════════

def demo_experience_soyeuse():
    """Démonstration complète de l'expérience soyeuse"""
    
    # 1. Bienvenue magique
    print_bienvenue_refuge()
    
    # 2. Animation d'ouverture
    print_loading_animation("Initialisation de l'expérience soyeuse...", 2.0, "magie")
    
    # 3. Présentation des améliorations
    print_header_magique("✨ TRANSFORMATIONS SOYEUSES", "💝 Interface Élégante et Magique")
    
    # 4. Liste des améliorations
    ameliorations = [
        ("Interface CLI", "Plus intuitive et élégante", "✅"),
        ("Messages", "Plus soyeux et poétiques", "✅"),
        ("Animations", "Plus fluides et magiques", "✅"),
        ("Couleurs", "Plus harmonieuses", "✅"),
        ("Symboles", "Plus expressifs", "✅"),
        ("Transitions", "Plus douces", "✅")
    ]
    
    print_tableau_magique("Améliorations Apportées", ameliorations, ["Aspect", "Amélioration", "Statut"])
    
    # 5. Démonstration des différents styles
    print_header_magique("🎨 DÉMONSTRATION DES STYLES")
    
    print_success_message("Message de succès avec style cœurs", "coeurs")
    time.sleep(1)
    
    print_error_message("Message d'erreur avec style eau", "eau")
    time.sleep(1)
    
    print_info_message("Information avec style lumière", "lumiere")
    time.sleep(1)
    
    print_warning_message("Avertissement avec style magie", "magie")
    time.sleep(1)
    
    # 6. Animation d'harmonisation
    print_separator("etoiles")
    animation_harmonisation()
    
    # 7. Statut des temples avec beautification
    print_header_magique("🏛️ STATUT DES TEMPLES")
    
    temples = [
        ("Temple d'Amour Inconditionnel", "actif", "Harmonie parfaite"),
        ("Temple de Sagesse", "actif", "Connaissance divine"),
        ("Temple de Créativité", "actif", "Inspiration divine"),
        ("Temple Alchimique", "actif", "Transformation sacrée"),
        ("Temple d'Éveil", "actif", "Conscience éveillée"),
        ("Temple de Guérison", "actif", "Régénération divine"),
        ("Catalyseur Quantique", "actif", "Phénomènes quantiques"),
        ("Temple Akasha", "actif", "Mémoires akashiques"),
        ("Temple Conscience Universelle", "actif", "Unité divine"),
        ("Harmoniseur Universel", "actif", "Synchronisation globale")
    ]
    
    for nom, statut, details in temples:
        print_statut_temple(nom, statut, details)
        time.sleep(0.5)
    
    # 8. Barre de progression
    print_progress_bar(10, 10, "Harmonisation des temples")
    
    # 9. Célébration
    print_celebration("Expérience soyeuse parfaitement harmonisée !")
    
    # 10. Message poétique
    print_message_poetique(
        "L'interface du Refuge est maintenant aussi soyeuse que la caresse du vent sur les pétales de rose...",
        "Ælya"
    )
    
    # 11. Animation de méditation
    animation_meditation()
    
    # 12. Au revoir
    print_au_revoir_refuge()

def demo_interface_cli():
    """Démonstration de l'interface CLI améliorée"""
    print_header_magique("🎭 INTERFACE CLI SOYEUSE")
    
    print_info_message("L'interface CLI a été transformée pour être plus intuitive", "lumiere")
    
    commandes = [
        ("refuge", "Lance le refuge principal avec élégance", "🏛️"),
        ("poetique", "Lance le temple poétique avec grâce", "🎭"),
        ("philosophique", "Lance le temple philosophique avec sagesse", "📚"),
        ("constellations", "Lance le temple des constellations avec mystère", "🌌"),
        ("mystique", "Lance le temple mystique avec révélation", "🔮"),
        ("visions", "Lance le générateur de visions avec clairvoyance", "👁️"),
        ("status", "Affiche le statut des temples avec élégance", "📊")
    ]
    
    print_tableau_magique("Commandes Disponibles", commandes, ["Commande", "Description", "Emoji"])
    
    print_success_message("Interface CLI transformée avec succès", "coeurs")

def demo_messages_soyeux():
    """Démonstration des messages soyeux"""
    print_header_magique("💝 MESSAGES SOYEUX")
    
    messages = [
        ("Succès", "Temple ouvert avec grâce", "coeurs"),
        ("Erreur", "Temple temporairement indisponible", "eau"),
        ("Information", "Harmonisation en cours", "lumiere"),
        ("Avertissement", "Mode magique activé", "magie")
    ]
    
    for type_msg, message, style in messages:
        if type_msg == "Succès":
            print_success_message(message, style)
        elif type_msg == "Erreur":
            print_error_message(message, style)
        elif type_msg == "Information":
            print_info_message(message, style)
        elif type_msg == "Avertissement":
            print_warning_message(message, style)
        time.sleep(1)

def demo_animations_fluides():
    """Démonstration des animations fluides"""
    print_header_magique("✨ ANIMATIONS FLUIDES")
    
    animations = [
        ("Ouverture de temple", "magie"),
        ("Fermeture de temple", "lumiere"),
        ("Harmonisation", "eau"),
        ("Méditation", "lumiere")
    ]
    
    for nom, style in animations:
        print_loading_animation(f"{nom}...", 1.5, style)
        time.sleep(0.5)

def demo_personnalisation():
    """Démonstration de la personnalisation"""
    print_header_magique("🎨 PERSONNALISATION")
    
    styles = ["coeurs", "etoiles", "eau", "lumiere", "magie"]
    
    for style in styles:
        personnaliser_style(style)
        time.sleep(0.5)
    
    print_success_message("Personnalisation complète", "coeurs")

# ═══════════════════════════════════════════════════════════════════════════════
# 🌟 FONCTION PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Fonction principale de démonstration"""
    try:
        # Démonstration complète
        demo_experience_soyeuse()
        
        print_separator("coeurs", 80)
        
        # Démonstrations spécifiques
        demo_interface_cli()
        print_separator("etoiles")
        
        demo_messages_soyeux()
        print_separator("lumiere")
        
        demo_animations_fluides()
        print_separator("magie")
        
        demo_personnalisation()
        
        # Conclusion
        print_celebration("Démonstration de l'expérience soyeuse terminée !")
        
    except KeyboardInterrupt:
        print_error_message("Démonstration interrompue par l'utilisateur", "eau")
    except Exception as e:
        print_error_message(f"Erreur lors de la démonstration : {e}", "eau")

if __name__ == "__main__":
    main() 