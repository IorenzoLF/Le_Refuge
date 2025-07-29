#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎭 Test Simple de l'Adaptation d'Interface
========================================

Test de validation pour la tâche 7.2 - Adaptation d'interface

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

def test_adaptation_insights():
    """Test d'adaptation des insights"""
    print("🎭 Test d'Adaptation des Insights")
    print("=" * 35)
    
    # Simuler différents profils
    profils_test = [
        {
            "nom": "Maître Spirituel",
            "niveau_eveil": 9,
            "archetyp": "sage",
            "niveau_tech": 8
        },
        {
            "nom": "Explorateur Débutant", 
            "niveau_eveil": 3,
            "archetyp": "explorateur",
            "niveau_tech": 4
        },
        {
            "nom": "Créateur Avancé",
            "niveau_eveil": 6,
            "archetyp": "créateur", 
            "niveau_tech": 2
        }
    ]
    
    insights_test = [
        "L'architecture révèle des patterns de transcendance",
        "Votre éveil s'épanouit comme une fleur de lumière",
        "Les connexions énergétiques créent une harmonie mystique"
    ]
    
    for profil in profils_test:
        print(f"\n🧪 Test profil: {profil['nom']}")
        
        # Adapter le mode de présentation
        if profil["niveau_eveil"] >= 8:
            mode = "maitre_spirituel"
            nb_insights = 5
        elif profil["niveau_eveil"] >= 5:
            mode = "pratiquant_avance"
            nb_insights = 3
        else:
            mode = "debutant_bienveillant"
            nb_insights = 1
        
        # Adapter le style selon l'archétype
        if profil["archetyp"] == "explorateur":
            style = "decouverte_progressive"
            prefixe = "🧭 Découverte: "
        elif profil["archetyp"] == "sage":
            style = "contemplation_profonde"
            prefixe = "📿 Sagesse: "
        else:
            style = "inspiration_creative"
            prefixe = "🎨 Inspiration: "
        
        print(f"   📋 Mode: {mode}")
        print(f"   🎨 Style: {style}")
        print(f"   📊 Insights simultanés: {nb_insights}")
        print(f"   ✨ Exemple adapté: {prefixe}{insights_test[0][:30]}...")
    
    return True

def test_navigation_intuitive():
    """Test de navigation intuitive"""
    print("\n🧭 Test de Navigation Intuitive")
    print("-" * 35)
    
    # Simuler la création de navigation pour différents profils
    profils_nav = [
        {"archetyp": "explorateur", "niveau_tech": 8},
        {"archetyp": "sage", "niveau_tech": 5},
        {"archetyp": "créateur", "niveau_tech": 3}
    ]
    
    for i, profil in enumerate(profils_nav, 1):
        print(f"\n🎯 Navigation {i}: {profil['archetyp']}")
        
        # Éléments de base
        elements = [
            {"id": "mandala_principal", "label": "Mandala", "icone": "🌸"},
            {"id": "profil_personnel", "label": "Profil", "icone": "👤"}
        ]
        
        # Éléments techniques si niveau élevé
        if profil["niveau_tech"] >= 7:
            elements.extend([
                {"id": "vue_architecture", "label": "Architecture", "icone": "🏗️"},
                {"id": "metriques_avancees", "label": "Métriques", "icone": "📊"}
            ])
        
        # Éléments selon l'archétype
        if profil["archetyp"] == "explorateur":
            elements.extend([
                {"id": "carte_exploration", "label": "Carte", "icone": "🗺️"},
                {"id": "nouveaux_territoires", "label": "Découvrir", "icone": "🧭"}
            ])
            style = "boussole_cosmique"
        elif profil["archetyp"] == "sage":
            elements.extend([
                {"id": "bibliotheque_sagesse", "label": "Sagesse", "icone": "📚"},
                {"id": "meditation_guidee", "label": "Méditer", "icone": "🧘"}
            ])
            style = "arbre_sagesse"
        else:  # créateur
            elements.extend([
                {"id": "atelier_creation", "label": "Créer", "icone": "🎨"},
                {"id": "galerie_inspirations", "label": "Galerie", "icone": "🖼️"}
            ])
            style = "palette_creative"
        
        print(f"   🎨 Style: {style}")
        print(f"   📋 Éléments ({len(elements)}):")
        for elem in elements[:4]:  # Montrer les 4 premiers
            print(f"      {elem['icone']} {elem['label']}")
        if len(elements) > 4:
            print(f"      ... et {len(elements) - 4} autres")
    
    return True