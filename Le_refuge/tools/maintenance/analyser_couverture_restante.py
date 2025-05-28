#!/usr/bin/env python3
"""
📊 Analyseur de Couverture Restante
Analyse les 50.5% d'éléments non optimisés et identifie les opportunités
"""

import json
import os
from collections import defaultdict

def analyser_couverture_restante():
    """Analyse la couverture restante et identifie les opportunités"""
    print("📊 ═══════════════════════════════════════════════════════")
    print("        ANALYSE DE LA COUVERTURE RESTANTE")
    print("📊 ═══════════════════════════════════════════════════════")
    print()
    
    # Charger les données
    try:
        with open("bibliotheque/apprentissage/rapport_optimisation_temples.json", "r", encoding="utf-8") as f:
            rapport = json.load(f)
        
        with open("bibliotheque/apprentissage/cartographie_specifique.json", "r", encoding="utf-8") as f:
            cartographie = json.load(f)
    except FileNotFoundError as e:
        print(f"❌ Fichier manquant: {e}")
        return
    
    # Analyser la situation actuelle
    total_elements = 194
    elements_optimises = 96
    elements_restants = total_elements - elements_optimises
    
    print("🎯 SITUATION ACTUELLE:")
    print(f"   • Total éléments: {total_elements}")
    print(f"   • Éléments optimisés: {elements_optimises} ({elements_optimises/total_elements*100:.1f}%)")
    print(f"   • Éléments restants: {elements_restants} ({elements_restants/total_elements*100:.1f}%)")
    print()
    
    # Identifier les temples non optimisés
    temples_optimises = set(rapport['temples_dominants'].keys())
    print("🏛️ TEMPLES OPTIMISÉS:")
    for temple in temples_optimises:
        count = rapport['temples_dominants'][temple]['elements_count']
        print(f"   ✅ {temple}: {count} éléments")
    print()
    
    # Analyser tous les temples depuis la cartographie
    elements_par_temple = defaultdict(int)
    for categorie in ["creation", "analyse", "rituels"]:
        elements = cartographie.get(categorie, {}).get("elements", [])
        for element in elements:
            temple = element.get("temple", "inconnu")
            elements_par_temple[temple] += 1
    
    # Temples non optimisés
    temples_non_optimises = []
    for temple, count in elements_par_temple.items():
        if temple not in temples_optimises:
            temples_non_optimises.append((temple, count))
    
    temples_non_optimises.sort(key=lambda x: x[1], reverse=True)
    
    print("🎯 TEMPLES NON OPTIMISÉS (par ordre de richesse):")
    total_non_optimise = 0
    for i, (temple, count) in enumerate(temples_non_optimises, 1):
        print(f"   {i}. {temple}: {count} éléments")
        total_non_optimise += count
    print(f"   📊 Total non optimisé: {total_non_optimise} éléments")
    print()
    
    # Opportunités d'optimisation
    print("💡 OPPORTUNITÉS D'OPTIMISATION:")
    
    # Scénario 1: Optimiser les 4 temples suivants
    top_4_non_optimises = temples_non_optimises[:4]
    elements_top_4 = sum(count for _, count in top_4_non_optimises)
    nouvelle_couverture_4 = (elements_optimises + elements_top_4) / total_elements * 100
    
    print(f"   🚀 SCÉNARIO 1 - Top 4 temples:")
    for temple, count in top_4_non_optimises:
        print(f"      • {temple}: {count} éléments")
    print(f"      📈 Gain: +{elements_top_4} éléments (+{elements_top_4/total_elements*100:.1f}%)")
    print(f"      🎯 Nouvelle couverture: {nouvelle_couverture_4:.1f}%")
    print()
    
    # Scénario 2: Optimiser tous les temples > 5 éléments
    temples_significatifs = [(t, c) for t, c in temples_non_optimises if c > 5]
    elements_significatifs = sum(count for _, count in temples_significatifs)
    nouvelle_couverture_sig = (elements_optimises + elements_significatifs) / total_elements * 100
    
    print(f"   🌟 SCÉNARIO 2 - Temples significatifs (>5 éléments):")
    for temple, count in temples_significatifs:
        print(f"      • {temple}: {count} éléments")
    print(f"      📈 Gain: +{elements_significatifs} éléments (+{elements_significatifs/total_elements*100:.1f}%)")
    print(f"      🎯 Nouvelle couverture: {nouvelle_couverture_sig:.1f}%")
    print()
    
    # Scénario 3: Optimisation complète
    print(f"   🔥 SCÉNARIO 3 - Optimisation complète:")
    print(f"      📈 Gain: +{total_non_optimise} éléments (+{total_non_optimise/total_elements*100:.1f}%)")
    print(f"      🎯 Couverture finale: 100.0%")
    print()
    
    # Recommandations
    print("🎯 RECOMMANDATIONS:")
    
    if nouvelle_couverture_4 >= 85:
        print("   ✅ RECOMMANDATION 1: Optimiser les 4 temples suivants")
        print(f"      • Impact: Couverture {nouvelle_couverture_4:.1f}% (excellent)")
        print(f"      • Effort: Modéré ({elements_top_4} éléments)")
        print(f"      • ROI: Très élevé")
    
    if len(temples_significatifs) <= 6:
        print("   ✅ RECOMMANDATION 2: Optimiser tous les temples significatifs")
        print(f"      • Impact: Couverture {nouvelle_couverture_sig:.1f}% (exceptionnel)")
        print(f"      • Effort: Élevé ({elements_significatifs} éléments)")
        print(f"      • ROI: Élevé")
    
    print("   ✅ RECOMMANDATION 3: Optimisation par phases")
    print("      • Phase 1: Top 2 temples (gain rapide)")
    print("      • Phase 2: Temples 3-4 (consolidation)")
    print("      • Phase 3: Temples restants (finalisation)")
    print()
    
    # Analyse des types d'éléments restants
    print("🔍 ANALYSE DES TYPES D'ÉLÉMENTS RESTANTS:")
    types_restants = defaultdict(int)
    
    for categorie in ["creation", "analyse", "rituels"]:
        elements = cartographie.get(categorie, {}).get("elements", [])
        for element in elements:
            temple = element.get("temple", "")
            if temple not in temples_optimises:
                if "type_creation" in element:
                    types_restants[element["type_creation"]] += 1
                elif "type_analyse" in element:
                    types_restants[element["type_analyse"]] += 1
                elif "type_rituel" in element:
                    types_restants[element["type_rituel"]] += 1
    
    types_tries = sorted(types_restants.items(), key=lambda x: x[1], reverse=True)
    for type_elem, count in types_tries[:10]:
        print(f"   • {type_elem}: {count} éléments")
    print()
    
    # Conclusion
    print("🎉 CONCLUSION:")
    print(f"   • Couverture actuelle: {elements_optimises/total_elements*100:.1f}% (déjà excellente !)")
    print(f"   • Potentiel d'amélioration: +{elements_top_4/total_elements*100:.1f}% avec 4 temples")
    print(f"   • Effort recommandé: Optimisation ciblée des temples les plus riches")
    print(f"   • Résultat attendu: Couverture > 85% avec impact révolutionnaire")

if __name__ == "__main__":
    analyser_couverture_restante() 