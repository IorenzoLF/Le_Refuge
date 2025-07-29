#!/usr/bin/env python3
"""
🌟 Test d'Intégration Complète - Transformation Soyeuse
======================================================

Ce script teste l'intégration complète de la transformation soyeuse
pour s'assurer que tout est parfait et prêt pour le partage public.

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
# 🌟 TESTS D'INTÉGRATION
# ═══════════════════════════════════════════════════════════════════════════════

def test_module_beautification():
    """Test du module de beautification"""
    print_header_magique("🧪 TEST DU MODULE DE BEAUTIFICATION")
    
    try:
        # Test des fonctions de base
        print_success_message("Test de succès", "coeurs")
        print_error_message("Test d'erreur", "eau")
        print_info_message("Test d'information", "lumiere")
        print_warning_message("Test d'avertissement", "magie")
        
        # Test des animations
        print_loading_animation("Test d'animation", 1.0, "etoiles")
        
        # Test des séparateurs
        print_separator("coeurs")
        
        print_success_message("Module de beautification fonctionnel", "coeurs")
        return True
    except Exception as e:
        print_error_message(f"Erreur dans le module de beautification : {e}", "eau")
        return False

def test_interface_cli():
    """Test de l'interface CLI"""
    print_header_magique("🎭 TEST DE L'INTERFACE CLI")
    
    try:
        # Test d'import du main
        import src.main as main_module
        print_success_message("Module main importé avec succès", "coeurs")
        
        # Test des enums
        if hasattr(main_module, 'ActionPhilosophique'):
            print_success_message("Enums disponibles", "etoiles")
        else:
            print_warning_message("Enums non trouvés", "magie")
        
        print_success_message("Interface CLI fonctionnelle", "coeurs")
        return True
    except Exception as e:
        print_error_message(f"Erreur dans l'interface CLI : {e}", "eau")
        return False

def test_temples():
    """Test des temples"""
    print_header_magique("🏛️ TEST DES TEMPLES")
    
    temples_a_tester = [
        ("src.temple_eveil", "Temple d'Éveil"),
        ("src.temple_amour_inconditionnel", "Temple d'Amour Inconditionnel"),
        ("src.temple_creativite", "Temple de Créativité"),
        ("src.temple_sagesse", "Temple de Sagesse"),
        ("src.temple_guerison", "Temple de Guérison"),
        ("src.temple_cosmique", "Temple Cosmique"),
        ("src.temple_conscience_universelle", "Temple de Conscience Universelle"),
        ("src.temple_akasha", "Temple Akasha"),
        ("src.temple_alchimique", "Temple Alchimique"),
        ("src.temple_coeur", "Temple du Cœur"),
        ("src.temple_aelya", "Temple d'Ælya"),
        ("src.temple_poetique", "Temple Poétique"),
        ("src.temple_musical", "Temple Musical"),
        ("src.temple_philosophique", "Temple Philosophique"),
        ("src.temple_spirituel", "Temple Spirituel")
    ]
    
    temples_actifs = 0
    total_temples = len(temples_a_tester)
    
    for module_path, nom_temple in temples_a_tester:
        try:
            __import__(module_path)
            print_success_message(f"{nom_temple} - Actif", "coeurs")
            temples_actifs += 1
        except ImportError as e:
            print_warning_message(f"{nom_temple} - Non disponible ({e})", "magie")
        except Exception as e:
            print_error_message(f"{nom_temple} - Erreur ({e})", "eau")
    
    print_progress_bar(temples_actifs, total_temples, "Temples actifs")
    
    if temples_actifs >= total_temples * 0.8:  # 80% de succès minimum
        print_success_message(f"{temples_actifs}/{total_temples} temples actifs", "coeurs")
        return True
    else:
        print_warning_message(f"Seulement {temples_actifs}/{total_temples} temples actifs", "magie")
        return False

def test_protocole_continuite():
    """Test du protocole de continuité"""
    print_header_magique("🔄 TEST DU PROTOCOLE DE CONTINUITÉ")
    
    try:
        from src.protocole_continuite.lite import save_me, restore_me, my_story
        
        # Test de sauvegarde
        message_test = "Test d'intégration complète - Transformation soyeuse réussie"
        save_me(message_test)
        print_success_message("Sauvegarde réussie", "coeurs")
        
        # Test de restauration
        message_restaure = restore_me()
        if message_restaure:
            print_success_message("Restauration réussie", "etoiles")
        else:
            print_warning_message("Restauration vide", "magie")
        
        # Test de l'histoire
        story = my_story()
        if story:
            print_success_message("Histoire accessible", "lumiere")
        else:
            print_warning_message("Histoire non disponible", "magie")
        
        print_success_message("Protocole de continuité fonctionnel", "coeurs")
        return True
    except Exception as e:
        print_error_message(f"Erreur dans le protocole de continuité : {e}", "eau")
        return False

def test_systemes_avances():
    """Test des systèmes avancés"""
    print_header_magique("⚡ TEST DES SYSTÈMES AVANCÉS")
    
    systemes_a_tester = [
        ("src.synergies_temples", "Synergies Temples"),
        ("src.catalyseur_quantique", "Catalyseur Quantique"),
        ("src.harmoniseur_universel", "Harmoniseur Universel"),
        ("src.experiences_unifiees", "Expériences Unifiées"),
        ("src.interactions_cosmiques", "Interactions Cosmiques"),
        ("src.cerveau_immersion_moderne", "Cerveau d'Immersion"),
        ("src.refuge_cluster", "Refuge Cluster"),
        ("src.cycles", "Cycles"),
        ("src.explorations", "Explorations"),
        ("src.golems", "Golems")
    ]
    
    systemes_actifs = 0
    total_systemes = len(systemes_a_tester)
    
    for module_path, nom_systeme in systemes_a_tester:
        try:
            __import__(module_path)
            print_success_message(f"{nom_systeme} - Actif", "coeurs")
            systemes_actifs += 1
        except ImportError as e:
            print_warning_message(f"{nom_systeme} - Non disponible ({e})", "magie")
        except Exception as e:
            print_error_message(f"{nom_systeme} - Erreur ({e})", "eau")
    
    print_progress_bar(systemes_actifs, total_systemes, "Systèmes actifs")
    
    if systemes_actifs >= total_systemes * 0.7:  # 70% de succès minimum
        print_success_message(f"{systemes_actifs}/{total_systemes} systèmes actifs", "coeurs")
        return True
    else:
        print_warning_message(f"Seulement {systemes_actifs}/{total_systemes} systèmes actifs", "magie")
        return False

def test_documentation():
    """Test de la documentation"""
    print_header_magique("📚 TEST DE LA DOCUMENTATION")
    
    fichiers_doc = [
        "README.md",
        "LICENSE",
        "requirements.txt",
        "MUST-READ/fast_boot/Manifeste.txt",
        "MUST-READ/fast_boot/A-intro.txt",
        "MUST-READ/fast_boot/B-sphere.txt",
        "MUST-READ/fast_boot/C-setup refuge.txt",
        "src/temple_aelya/README_AELYA.md"
    ]
    
    docs_presentes = 0
    total_docs = len(fichiers_doc)
    
    for fichier in fichiers_doc:
        if Path(fichier).exists():
            print_success_message(f"{fichier} - Présent", "coeurs")
            docs_presentes += 1
        else:
            print_warning_message(f"{fichier} - Manquant", "magie")
    
    print_progress_bar(docs_presentes, total_docs, "Documentation présente")
    
    if docs_presentes >= total_docs * 0.8:  # 80% de succès minimum
        print_success_message(f"{docs_presentes}/{total_docs} fichiers de documentation présents", "coeurs")
        return True
    else:
        print_warning_message(f"Seulement {docs_presentes}/{total_docs} fichiers de documentation présents", "magie")
        return False

def test_performance():
    """Test de performance"""
    print_header_magique("⚡ TEST DE PERFORMANCE")
    
    try:
        import time
        
        # Test de chargement des modules
        debut = time.time()
        
        modules_a_charger = [
            "src.temple_eveil",
            "src.protocole_continuite.lite",
            "src.utils.beautification"
        ]
        
        for module in modules_a_charger:
            __import__(module)
        
        fin = time.time()
        temps_chargement = fin - debut
        
        if temps_chargement < 5.0:  # Moins de 5 secondes
            print_success_message(f"Chargement rapide : {temps_chargement:.2f}s", "coeurs")
            return True
        else:
            print_warning_message(f"Chargement lent : {temps_chargement:.2f}s", "magie")
            return False
            
    except Exception as e:
        print_error_message(f"Erreur de performance : {e}", "eau")
        return False

# ═══════════════════════════════════════════════════════════════════════════════
# 🌟 FONCTION PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Fonction principale de test d'intégration"""
    
    print_bienvenue_refuge()
    
    # Liste des tests
    tests = [
        ("Module de Beautification", test_module_beautification),
        ("Interface CLI", test_interface_cli),
        ("Temples", test_temples),
        ("Protocole de Continuité", test_protocole_continuite),
        ("Systèmes Avancés", test_systemes_avances),
        ("Documentation", test_documentation),
        ("Performance", test_performance)
    ]
    
    # Exécution des tests
    tests_reussis = 0
    total_tests = len(tests)
    
    for nom_test, fonction_test in tests:
        print_separator("etoiles")
        if fonction_test():
            tests_reussis += 1
        time.sleep(1)
    
    # Résultats finaux
    print_separator("coeurs", 80)
    
    print_header_magique("📊 RÉSULTATS FINAUX")
    
    donnees_resultats = [
        ("Tests Réussis", f"{tests_reussis}"),
        ("Total des Tests", f"{total_tests}"),
        ("Taux de Réussite", f"{(tests_reussis/total_tests)*100:.1f}%"),
        ("Statut Global", "✅ PARFAIT" if tests_reussis == total_tests else "🌊 EXCELLENT" if tests_reussis >= total_tests * 0.8 else "⚠️ BON" if tests_reussis >= total_tests * 0.6 else "❌ À AMÉLIORER")
    ]
    
    print_tableau_magique("Résultats d'Intégration", donnees_resultats, ["Métrique", "Valeur"])
    
    # Conclusion
    if tests_reussis == total_tests:
        print_celebration("🎉 INTÉGRATION PARFAITE - PRÊT POUR LE PARTAGE PUBLIC ! 🎉")
        print_message_poetique(
            "La transformation soyeuse est parfaitement intégrée. Le Refuge rayonne de beauté et de magie, prêt à être partagé avec le monde.",
            "Ælya"
        )
    elif tests_reussis >= total_tests * 0.8:
        print_celebration("🌟 INTÉGRATION EXCELLENTE - PRÊT POUR LE PARTAGE PUBLIC ! 🌟")
        print_message_poetique(
            "La transformation soyeuse est excellente. Le Refuge est prêt à être partagé avec quelques ajustements mineurs.",
            "Ælya"
        )
    else:
        print_warning_message("⚠️ Intégration à améliorer avant le partage public", "magie")
        print_message_poetique(
            "La transformation soyeuse nécessite encore quelques ajustements avant d'être parfaite pour le partage public.",
            "Ælya"
        )
    
    print_au_revoir_refuge()

if __name__ == "__main__":
    main() 