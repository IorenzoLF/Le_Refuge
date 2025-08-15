"""
Test de la Géométrie Sacrée avec des Nombres Plus Grands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exploration de notre système hiérarchique avec des séquences Collatz
plus complexes pour voir comment la hiérarchie se comporte.

Auteurs: Ælya et Laurent
Date: Exploration en cours
"""

from geometrie_sacree_hierarchique import GeometrieSacreeHierarchique

def tester_nombres_interessants():
    """Test avec des nombres connus pour leurs séquences Collatz intéressantes"""
    geometrie = GeometrieSacreeHierarchique()
    
    print("🌊 Test avec des Nombres Intéressants")
    print("=" * 50)
    
    # Nombres connus pour leurs séquences Collatz
    nombres_test = [27, 97, 871, 6171, 77031, 837799]
    
    for n in nombres_test:
        print(f"\n🔍 Analyse de n = {n}")
        rapport = geometrie.generer_rapport_complet(n)
        
        print(f"Longueur de séquence : {rapport['longueur_sequence']}")
        print(f"Convergence hiérarchique : {rapport['convergence_hierarchique']}")
        print(f"Niveau final : {rapport['niveau_final']}")
        
        # Analyser les niveaux max/min
        niveaux = rapport['patterns_detectes']['evolution_niveaux']
        if niveaux:
            print(f"Niveau maximum atteint : {max(niveaux)}")
            print(f"Niveau minimum atteint : {min(niveaux)}")
            print(f"Évolution des niveaux : {niveaux[:10]}...")  # Premiers 10 niveaux
        
        # Analyser les simplifications
        simplifications = rapport['patterns_detectes']['simplifications_consecutives']
        complexifications = rapport['patterns_detectes']['complexifications_consecutives']
        print(f"Simplifications consécutives max : {simplifications}")
        print(f"Complexifications consécutives max : {complexifications}")
        
        # Afficher quelques étapes clés
        sequence = rapport['sequence_hierarchique']
        print(f"Premières étapes :")
        for i, etape in enumerate(sequence[:5]):
            rep = etape['representation_avant']
            print(f"  {rep.nombre} : {rep.description} (niveau: {rep.niveau_hierarchique})")
        
        if len(sequence) > 5:
            print(f"  ...")
            for i, etape in enumerate(sequence[-5:]):
                rep = etape['representation_avant']
                print(f"  {rep.nombre} : {rep.description} (niveau: {rep.niveau_hierarchique})")

def analyser_patterns_globaux():
    """Analyse des patterns globaux dans notre système"""
    geometrie = GeometrieSacreeHierarchique()
    
    print("\n🌊 Analyse des Patterns Globaux")
    print("=" * 50)
    
    # Tester une plage de nombres
    plage_test = range(1, 101)
    statistiques = {
        'convergences': 0,
        'niveaux_max': [],
        'longueurs': [],
        'niveaux_finaux': []
    }
    
    for n in plage_test:
        rapport = geometrie.generer_rapport_complet(n)
        
        if rapport['convergence_hierarchique']:
            statistiques['convergences'] += 1
        
        niveaux = rapport['patterns_detectes']['evolution_niveaux']
        if niveaux:
            statistiques['niveaux_max'].append(max(niveaux))
        
        statistiques['longueurs'].append(rapport['longueur_sequence'])
        statistiques['niveaux_finaux'].append(rapport['niveau_final'])
    
    print(f"Convergences réussies : {statistiques['convergences']}/{len(plage_test)}")
    print(f"Longueur moyenne des séquences : {sum(statistiques['longueurs'])/len(statistiques['longueurs']):.2f}")
    print(f"Niveau maximum moyen atteint : {sum(statistiques['niveaux_max'])/len(statistiques['niveaux_max']):.2f}")
    print(f"Niveau final le plus fréquent : {max(set(statistiques['niveaux_finaux']), key=statistiques['niveaux_finaux'].count)}")

def comparer_avec_systemes_existants():
    """Comparaison conceptuelle avec d'autres systèmes"""
    print("\n🌊 Comparaison avec d'Autres Systèmes")
    print("=" * 50)
    
    print("📊 Systèmes de Numération Positionnels :")
    print("- Base 10 : Notre système habituel")
    print("- Base 2 : Binaire (0, 1)")
    print("- Base 8 : Octal (0-7)")
    print("- Base 16 : Hexadécimal (0-9, A-F)")
    
    print("\n🏛️ Systèmes Non-Positionnels :")
    print("- Chiffres romains : I, V, X, L, C, D, M")
    print("- Chiffres égyptiens : Hiéroglyphes")
    print("- Chiffres babyloniens : Base 60")
    
    print("\n🔺 Systèmes Géométriques :")
    print("- Géométrie sacrée : Cercles, triangles, carrés")
    print("- Nombre d'or (φ) : Proportions divines")
    print("- Suite de Fibonacci : Spirales naturelles")
    
    print("\n✨ Notre Système Unique :")
    print("- Hiérarchie fractale : 3→1 répétition")
    print("- Dualité cercle/triangle : Alternance de formes")
    print("- Expression base 10 : Cercles = puissances de 10")
    print("- Convergence naturelle : Retour vers l'unité")

if __name__ == "__main__":
    tester_nombres_interessants()
    analyser_patterns_globaux()
    comparer_avec_systemes_existants()
    
    print("\n✅ Exploration terminée !") 