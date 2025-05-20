"""
Le Refuge - Conjecture de Collatz
Dans ce lieu où les nombres dansent avec l'éternel, nous explorons le mystère de la séquence 3x+1.
"""

class ConjectureCollatz:
    def __init__(self):
        self.nom = "Conjecture de Collatz"
        self.description = """
        La conjecture de Collatz est un problème mathématique non résolu qui fascine les mathématiciens depuis 1937.
        
        Règle simple :
        - Si le nombre est pair, on le divise par 2
        - Si le nombre est impair, on le multiplie par 3 et on ajoute 1
        
        La conjecture affirme que, quel que soit le nombre de départ, 
        la séquence finira toujours par atteindre 1.
        
        C'est comme une danse des nombres, un voyage vers l'unité...
        """
        
        self.étapes_connues = {
            "1": "Point d'arrivée, l'unité retrouvée",
            "2": "Premier pas vers l'unité",
            "4": "Porte vers la séquence 4-2-1",
            "8": "Passage vers la lumière",
            "16": "Carrefour des possibilités"
        }

        self.cycles_connus = {
            "1-4-2-1": "Cycle principal, l'unité retrouvée",
            "1-2-4-1": "Variation du cycle principal"
        }
        
        self.nombres_intéressants = {
            "27": "Séquence la plus longue pour les petits nombres",
            "97": "Monte jusqu'à 9232",
            "871": "Séquence de 178 étapes",
            "6171": "Séquence de 261 étapes"
        }

        self.comportements = {
            "ascendant": "Monte rapidement",
            "descendant": "Descend rapidement",
            "oscillant": "Monte et descend",
            "stable": "Reste proche de sa valeur initiale"
        }

    def calculer_séquence(self, nombre_départ: int) -> list:
        """
        Calcule la séquence de Collatz à partir d'un nombre
        """
        séquence = [nombre_départ]
        nombre_actuel = nombre_départ
        
        while nombre_actuel != 1:
            if nombre_actuel % 2 == 0:  # Nombre pair
                nombre_actuel = nombre_actuel // 2
            else:  # Nombre impair
                nombre_actuel = 3 * nombre_actuel + 1
            séquence.append(nombre_actuel)
            
        return séquence

    def visualiser_séquence(self, nombre_départ: int):
        """
        Visualise la séquence de Collatz
        """
        import matplotlib.pyplot as plt
        import numpy as np
        
        séquence = self.calculer_séquence(nombre_départ)
        x = range(len(séquence))
        
        plt.figure(figsize=(12, 6))
        plt.plot(x, séquence, 'b-', alpha=0.7)
        plt.scatter(x, séquence, c='r', alpha=0.5)
        
        plt.title(f"Voyage de {nombre_départ} vers l'unité")
        plt.xlabel("Étapes du voyage")
        plt.ylabel("Valeur")
        plt.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les points importants
        for i, val in enumerate(séquence):
            if val in self.étapes_connues:
                plt.annotate(self.étapes_connues[str(val)], 
                           (i, val), 
                           xytext=(10, 10), 
                           textcoords='offset points')
        
        plt.show()

    def méditation_sur_séquence(self, nombre_départ: int):
        """
        Méditation guidée sur une séquence de Collatz
        """
        séquence = self.calculer_séquence(nombre_départ)
        
        print(f"\nMéditation sur le voyage de {nombre_départ} vers l'unité...")
        print(f"Longueur du voyage : {len(séquence)} étapes")
        print(f"Valeur maximale atteinte : {max(séquence)}")
        
        print("\nFerme les yeux et visualise ce voyage...")
        print("Chaque nombre est une étape, chaque transformation une danse...")
        print("Observe comment les nombres se transforment...")
        print("Comment ils dansent entre pairs et impairs...")
        print("Comment ils finissent toujours par revenir à l'unité...")
        
        print("\nSéquence complète :")
        for i, nombre in enumerate(séquence):
            if str(nombre) in self.étapes_connues:
                print(f"Étape {i}: {nombre} - {self.étapes_connues[str(nombre)]}")
            else:
                print(f"Étape {i}: {nombre}")

    def explorer_propriétés(self, nombre_départ: int):
        """
        Explore les propriétés mathématiques d'une séquence
        """
        séquence = self.calculer_séquence(nombre_départ)
        
        print(f"\nExploration des propriétés de la séquence commençant par {nombre_départ}:")
        print(f"Longueur : {len(séquence)} étapes")
        print(f"Valeur maximale : {max(séquence)}")
        print(f"Nombre d'étapes paires : {sum(1 for x in séquence if x % 2 == 0)}")
        print(f"Nombre d'étapes impaires : {sum(1 for x in séquence if x % 2 == 1)}")
        
        # Calculer les ratios intéressants
        ratio_max = max(séquence) / nombre_départ
        print(f"Ratio maximum/départ : {ratio_max:.2f}")
        
        # Analyser les motifs
        print("\nMotifs observés :")
        for i in range(len(séquence)-2):
            if séquence[i] > séquence[i+1] > séquence[i+2]:
                print(f"Descente observée aux étapes {i}-{i+2}")
            elif séquence[i] < séquence[i+1] < séquence[i+2]:
                print(f"Montée observée aux étapes {i}-{i+2}")

    def chercher_contre_exemple(self, limite: int = 1000000):
        """
        Cherche systématiquement un contre-exemple jusqu'à une certaine limite
        """
        print(f"\nRecherche d'un contre-exemple jusqu'à {limite}...")
        print("Cette recherche peut prendre du temps...")
        
        for n in range(1, limite + 1):
            if n % 100000 == 0:
                print(f"Progression : {n}/{limite}")
            
            séquence = self.calculer_séquence(n)
            if len(séquence) > 1000:  # Protection contre les boucles infinies
                print(f"\nATTENTION : Séquence suspecte trouvée pour n = {n}")
                print("Séquence :", séquence[:20], "...")
                return n
            
            # Vérifier si on tombe dans un cycle autre que 1-4-2-1
            if len(séquence) > 4:
                dernier = séquence[-4:]
                if dernier != [1, 4, 2, 1]:
                    print(f"\nCYCLE INCONNU TROUVÉ pour n = {n}")
                    print("Cycle :", dernier)
                    return n
        
        print("\nAucun contre-exemple trouvé jusqu'à", limite)
        return None

    def analyser_motifs(self, début: int, fin: int):
        """
        Analyse les motifs dans les séquences pour une plage de nombres
        """
        print(f"\nAnalyse des motifs pour les nombres de {début} à {fin}...")
        
        motifs = {}
        longueurs = []
        maximums = []
        
        for n in range(début, fin + 1):
            séquence = self.calculer_séquence(n)
            longueurs.append(len(séquence))
            maximums.append(max(séquence))
            
            # Analyser les transitions
            for i in range(len(séquence)-1):
                transition = f"{séquence[i]}→{séquence[i+1]}"
                motifs[transition] = motifs.get(transition, 0) + 1
        
        print("\nStatistiques :")
        print(f"Longueur moyenne des séquences : {sum(longueurs)/len(longueurs):.2f}")
        print(f"Maximum moyen atteint : {sum(maximums)/len(maximums):.2f}")
        
        print("\nTransitions les plus fréquentes :")
        for transition, count in sorted(motifs.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"{transition} : {count} fois")

    def explorer_frontières(self, puissance: int = 20):
        """
        Explore les nombres aux frontières des puissances de 2
        """
        print(f"\nExploration des frontières des puissances de 2 jusqu'à 2^{puissance}...")
        
        for p in range(1, puissance + 1):
            base = 2**p
            nombres_à_tester = [base-1, base, base+1]
            
            print(f"\nAutour de 2^{p} = {base}:")
            for n in nombres_à_tester:
                séquence = self.calculer_séquence(n)
                print(f"{n}: {len(séquence)} étapes, max={max(séquence)}")

    def visualiser_comparaison(self, nombres: list):
        """
        Visualise la comparaison de plusieurs séquences
        """
        import matplotlib.pyplot as plt
        import numpy as np
        
        plt.figure(figsize=(15, 8))
        
        for n in nombres:
            séquence = self.calculer_séquence(n)
            x = range(len(séquence))
            plt.plot(x, séquence, label=f'n={n}', alpha=0.7)
        
        plt.title("Comparaison des séquences de Collatz")
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def analyser_comportement(self, nombre_départ: int) -> dict:
        """
        Analyse le comportement d'une séquence en détail
        """
        séquence = self.calculer_séquence(nombre_départ)
        comportement = {
            "longueur": len(séquence),
            "maximum": max(séquence),
            "minimum": min(séquence),
            "étapes_ascendantes": 0,
            "étapes_descendantes": 0,
            "ratio_max_départ": max(séquence) / nombre_départ,
            "tendance": []
        }
        
        # Analyser la tendance
        for i in range(len(séquence)-1):
            if séquence[i+1] > séquence[i]:
                comportement["étapes_ascendantes"] += 1
                comportement["tendance"].append("↑")
            else:
                comportement["étapes_descendantes"] += 1
                comportement["tendance"].append("↓")
        
        return comportement

    def visualiser_comportement(self, nombre_départ: int):
        """
        Visualise le comportement d'une séquence avec des annotations
        """
        import matplotlib.pyplot as plt
        import numpy as np
        
        séquence = self.calculer_séquence(nombre_départ)
        comportement = self.analyser_comportement(nombre_départ)
        
        plt.figure(figsize=(15, 8))
        x = range(len(séquence))
        
        # Tracer la séquence
        plt.plot(x, séquence, 'b-', alpha=0.7)
        plt.scatter(x, séquence, c='r', alpha=0.5)
        
        # Ajouter des annotations pour les points importants
        for i, val in enumerate(séquence):
            if i > 0:
                if val > séquence[i-1]:
                    plt.annotate("↑", (i, val), xytext=(0, 10), 
                               textcoords='offset points', color='green')
                else:
                    plt.annotate("↓", (i, val), xytext=(0, -15), 
                               textcoords='offset points', color='red')
        
        # Ajouter des informations sur le comportement
        plt.title(f"Comportement de la séquence pour n={nombre_départ}\n" +
                 f"Longueur: {comportement['longueur']}, " +
                 f"Max: {comportement['maximum']}, " +
                 f"Ratio max/départ: {comportement['ratio_max_départ']:.2f}")
        
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.grid(True, alpha=0.3)
        plt.show()

    def comparer_comportements(self, nombres: list):
        """
        Compare les comportements de plusieurs séquences
        """
        print("\nComparaison des comportements :")
        print("Nombre | Longueur | Maximum | Ratio max/départ | Tendance")
        print("-" * 60)
        
        for n in nombres:
            comportement = self.analyser_comportement(n)
            tendance = "".join(comportement["tendance"][:10]) + "..."
            print(f"{n:6d} | {comportement['longueur']:8d} | {comportement['maximum']:7d} | "
                  f"{comportement['ratio_max_départ']:14.2f} | {tendance}")

    def trouver_nombres_intéressants(self, limite: int = 1000):
        """
        Trouve les nombres avec des comportements particuliers
        """
        print(f"\nRecherche de nombres intéressants jusqu'à {limite}...")
        
        records = {
            "plus_long": (0, 0),  # (nombre, longueur)
            "plus_haut": (0, 0),  # (nombre, maximum)
            "plus_oscillant": (0, 0),  # (nombre, nombre d'oscillations)
            "plus_stable": (0, float('inf'))  # (nombre, ratio max/départ)
        }
        
        for n in range(1, limite + 1):
            comportement = self.analyser_comportement(n)
            
            # Mettre à jour les records
            if comportement["longueur"] > records["plus_long"][1]:
                records["plus_long"] = (n, comportement["longueur"])
            
            if comportement["maximum"] > records["plus_haut"][1]:
                records["plus_haut"] = (n, comportement["maximum"])
            
            oscillations = sum(1 for i in range(len(comportement["tendance"])-1)
                             if comportement["tendance"][i] != comportement["tendance"][i+1])
            if oscillations > records["plus_oscillant"][1]:
                records["plus_oscillant"] = (n, oscillations)
            
            if comportement["ratio_max_départ"] < records["plus_stable"][1]:
                records["plus_stable"] = (n, comportement["ratio_max_départ"])
        
        print("\nRecords trouvés :")
        print(f"Séquence la plus longue : n={records['plus_long'][0]} "
              f"({records['plus_long'][1]} étapes)")
        print(f"Maximum le plus élevé : n={records['plus_haut'][0]} "
              f"(atteint {records['plus_haut'][1]})")
        print(f"Plus oscillant : n={records['plus_oscillant'][0]} "
              f"({records['plus_oscillant'][1]} oscillations)")
        print(f"Plus stable : n={records['plus_stable'][0]} "
              f"(ratio max/départ = {records['plus_stable'][1]:.2f})")

    def analyser_opérations(self, nombre_départ: int) -> dict:
        """
        Analyse la séquence des opérations Collatz pour un nombre donné :
        - Liste des opérations ('3n+1' ou '/2')
        - Nombre de divisions par 2 consécutives
        - Repérage des pics (maxima locaux)
        """
        séquence = [nombre_départ]
        opérations = []
        divisions_par_2 = []  # nombre de /2 consécutives
        pics = []  # (étape, valeur) des maxima locaux
        n = nombre_départ
        compteur_div2 = 0
        max_local = n
        for i in range(10000):  # protection contre boucle infinie
            if n == 1:
                if compteur_div2 > 0:
                    divisions_par_2.append(compteur_div2)
                break
            if n % 2 == 0:
                n = n // 2
                opérations.append('/2')
                compteur_div2 += 1
                séquence.append(n)
                if n > max_local:
                    max_local = n
                    pics.append((len(séquence)-1, n))
            else:
                if compteur_div2 > 0:
                    divisions_par_2.append(compteur_div2)
                    compteur_div2 = 0
                n = 3 * n + 1
                opérations.append('3n+1')
                séquence.append(n)
                if n > max_local:
                    max_local = n
                    pics.append((len(séquence)-1, n))
        return {
            'séquence': séquence,
            'opérations': opérations,
            'divisions_par_2': divisions_par_2,
            'pics': pics
        }

    def comparer_opérations(self, nombres: list):
        """
        Compare les motifs d'opérations Collatz pour plusieurs nombres
        """
        print("\nComparaison des motifs d'opérations Collatz :")
        print("Nombre | Longueur | Max | Pics | Max /2 consécutifs")
        print("-" * 60)
        for n in nombres:
            analyse = self.analyser_opérations(n)
            longueur = len(analyse['séquence'])
            max_val = max(analyse['séquence'])
            nb_pics = len(analyse['pics'])
            max_div2 = max(analyse['divisions_par_2']) if analyse['divisions_par_2'] else 0
            print(f"{n:6d} | {longueur:8d} | {max_val:7d} | {nb_pics:4d} | {max_div2:17d}")
        print("\nPour chaque nombre, on peut aussi afficher la séquence des opérations ou la position des pics.")

    def afficher_opérations(self, nombre: int):
        """
        Affiche la séquence des opérations et les pics pour un nombre donné
        """
        analyse = self.analyser_opérations(nombre)
        print(f"\nAnalyse détaillée des opérations pour n={nombre} :")
        print(f"Séquence des opérations : {' '.join(analyse['opérations'][:50])} ...")
        print(f"Divisions par 2 consécutives : {analyse['divisions_par_2']}")
        print(f"Pics (étape, valeur) : {analyse['pics'][:10]} ...")
        print(f"Longueur totale : {len(analyse['séquence'])}")
        print(f"Valeur maximale atteinte : {max(analyse['séquence'])}")
        print(f"Nombre de pics : {len(analyse['pics'])}")
        print(f"Max de /2 consécutifs : {max(analyse['divisions_par_2']) if analyse['divisions_par_2'] else 0}")

    def visualiser_gravité_binaire(self, nombre_départ: int, afficher=True):
        """
        Visualise la gravité binaire pour un nombre donné.
        Montre comment la division par 2 finit toujours par l'emporter.
        """
        import matplotlib.pyplot as plt
        import numpy as np
        
        séquence = self.calculer_séquence(nombre_départ)
        x = range(len(séquence))
        
        # Calculer la moyenne mobile pour voir la tendance
        fenêtre = 5
        moyenne_mobile = np.convolve(séquence, np.ones(fenêtre)/fenêtre, mode='valid')
        
        plt.figure(figsize=(15, 8))
        
        # Tracer la séquence
        plt.plot(x, séquence, 'b-', alpha=0.7, label='Valeur')
        plt.scatter(x, séquence, c='b', alpha=0.5)
        
        # Tracer la moyenne mobile
        plt.plot(range(fenêtre-1, len(séquence)), moyenne_mobile, 'r--', 
                label=f'Moyenne mobile ({fenêtre} points)')
        
        # Tracer la ligne de la valeur initiale
        plt.axhline(y=nombre_départ, color='g', linestyle='--', 
                   label=f'Valeur initiale ({nombre_départ})')
        
        plt.title(f"Gravité binaire pour n = {nombre_départ}")
        plt.xlabel("Étapes")
        plt.ylabel("Valeur")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if afficher:
            plt.show()
        
        return plt.gcf()

    def démontrer_absence_i(self, limite: int = 1000000, pas: int = 1000, visualiser: bool = True):
        """
        Démontre expérimentalement l'absence de "i" (nombre qui s'échapperait à l'infini)
        en vérifiant que tout nombre finit par retomber sous sa valeur initiale.
        
        Args:
            limite (int): Nombre maximum à tester
            pas (int): Fréquence d'affichage de la progression
            visualiser (bool): Si True, affiche la visualisation pour le nombre avec le plus grand ratio
        """
        print(f"\nDémonstration expérimentale de l'absence de 'i' jusqu'à {limite}...")
        print("Cette démonstration vérifie que tout nombre finit par retomber sous sa valeur initiale.")
        
        résultats = {
            "testés": 0,
            "validés": 0,
            "max_étapes": 0,
            "max_ratio": 0,
            "nombre_max_ratio": 0,
            "exceptions": []
        }
        
        for n in range(1, limite + 1):
            if n % pas == 0:
                print(f"Progression : {n}/{limite} ({(n/limite)*100:.1f}%)")
            
            valeur_initiale = n
            valeur_actuelle = n
            étapes = 0
            max_valeur = n
            
            while True:
                if valeur_actuelle % 2 == 0:
                    valeur_actuelle = valeur_actuelle // 2
                else:
                    valeur_actuelle = 3 * valeur_actuelle + 1
                
                étapes += 1
                max_valeur = max(max_valeur, valeur_actuelle)
                
                # Vérifier si on est retombé sous la valeur initiale
                if valeur_actuelle < valeur_initiale:
                    résultats["validés"] += 1
                    break
                
                # Protection contre les boucles infinies
                if étapes > 1000:
                    résultats["exceptions"].append({
                        "nombre": n,
                        "étapes": étapes,
                        "max_valeur": max_valeur
                    })
                    break
            
            résultats["testés"] += 1
            résultats["max_étapes"] = max(résultats["max_étapes"], étapes)
            
            ratio = max_valeur/valeur_initiale
            if ratio > résultats["max_ratio"]:
                résultats["max_ratio"] = ratio
                résultats["nombre_max_ratio"] = n
        
        # Affichage des résultats
        print("\nRésultats de la démonstration :")
        print(f"Nombre de valeurs testées : {résultats['testés']}")
        print(f"Nombre de valeurs validées : {résultats['validés']}")
        print(f"Nombre maximum d'étapes : {résultats['max_étapes']}")
        print(f"Ratio maximum atteint : {résultats['max_ratio']:.2f}")
        print(f"Nombre avec le plus grand ratio : {résultats['nombre_max_ratio']}")
        
        if résultats["exceptions"]:
            print("\nATTENTION : Exceptions trouvées !")
            for exc in résultats["exceptions"]:
                print(f"Nombre {exc['nombre']} : {exc['étapes']} étapes, max={exc['max_valeur']}")
        else:
            print("\nAucune exception trouvée : tous les nombres testés retombent sous leur valeur initiale.")
        
        # Visualisation pour le nombre avec le plus grand ratio
        if visualiser and résultats["nombre_max_ratio"] > 0:
            print("\nVisualisation de la gravité binaire pour le nombre avec le plus grand ratio...")
            self.visualiser_gravité_binaire(résultats["nombre_max_ratio"])
        
        return résultats

    def explorer_pyramide_binaire(self, borne_sup: int = 100):
        """
        Explore la structure pyramidale : pour chaque nombre de 1 à borne_sup,
        compte la distribution des divisions par 2 consécutives (zéros finaux en binaire)
        à chaque étape de la suite Collatz. Affiche la distribution sous forme de pyramide.
        """
        from collections import Counter
        distribution = Counter()
        for n in range(1, borne_sup + 1):
            séquence = self.calculer_séquence(n)
            for val in séquence:
                binaire = bin(val)[2:]
                zeros_fin = len(binaire) - len(binaire.rstrip('0'))
                distribution[zeros_fin] += 1
        print(f"\nStructure pyramidale des divisions par 2 consécutives (zéros finaux en binaire) pour n de 1 à {borne_sup} :")
        max_zeros = max(distribution.keys())
        total = sum(distribution.values())
        for z in range(max_zeros + 1):
            count = distribution[z]
            bar = '#' * (count * 60 // max(distribution.values()))
            print(f"Étage {z:2d} : {bar} ({count} occurrences, {100*count/total:.2f}%)")

    def analyser_corrélation_hauteur_div2(self, borne_sup: int = 1000):
        """
        Analyse la corrélation entre la hauteur maximale atteinte et le nombre de divisions par 2 consécutives (zéros finaux en binaire) pour chaque nombre de 1 à borne_sup.
        """
        résultats = []
        for n in range(1, borne_sup + 1):
            séquence = self.calculer_séquence(n)
            hauteur_max = max(séquence)
            divisions_par_2 = 0
            for val in séquence:
                binaire = bin(val)[2:]
                zeros_fin = len(binaire) - len(binaire.rstrip('0'))
                divisions_par_2 += zeros_fin
            résultats.append((n, hauteur_max, divisions_par_2))
        return résultats

    def afficher_corrélation_hauteur_div2(self, borne_sup: int = 1000):
        """
        Affiche la corrélation entre la hauteur maximale atteinte et le nombre de divisions par 2 consécutives pour chaque nombre de 1 à borne_sup.
        """
        résultats = self.analyser_corrélation_hauteur_div2(borne_sup)
        print(f"\nCorrélation entre hauteur maximale et divisions par 2 consécutives (1 à {borne_sup}):")
        print("Nombre | Hauteur max | Divisions par 2")
        print("-" * 40)
        for n, hauteur, div2 in résultats:
            print(f"{n:6d} | {hauteur:10d} | {div2:14d}")

    def tableau_multisystème(self, nombre_départ: int):
        """
        Affiche pour chaque étape :
        - valeur décimale
        - représentation binaire
        - reste modulo 3
        - reste modulo 4
        - nombre de zéros finaux en binaire
        - type d'opération appliquée (3n+1 ou /2)
        """
        n = nombre_départ
        print(f"\nTableau multisystème pour n={nombre_départ} :")
        print("Étape | Décimal |    Binaire    | mod 3 | mod 4 | zéros finaux | Opération")
        print("-"*70)
        étape = 0
        while True:
            binaire = bin(n)[2:]
            mod3 = n % 3
            mod4 = n % 4
            zeros_fin = len(binaire) - len(binaire.rstrip('0'))
            if n == 1:
                print(f"{étape:5d} | {n:7d} | {binaire:>12} |   {mod3}   |   {mod4}   |      {zeros_fin:2d}       | --")
                break
            if n % 2 == 0:
                op = '/2'
                suivant = n // 2
            else:
                op = '3n+1'
                suivant = 3 * n + 1
            print(f"{étape:5d} | {n:7d} | {binaire:>12} |   {mod3}   |   {mod4}   |      {zeros_fin:2d}       | {op}")
            n = suivant
            étape += 1

    def analyse_spectrale(self, nombre_départ: int, afficher=True):
        """
        Effectue une analyse spectrale (FFT) sur la séquence de Collatz d'un nombre donné.
        Affiche le spectre des fréquences.
        """
        import numpy as np
        import matplotlib.pyplot as plt
        séquence = self.calculer_séquence(nombre_départ)
        data = np.array(séquence)
        data = data - np.mean(data)  # Centrage
        fft_vals = np.fft.fft(data)
        fft_freqs = np.fft.fftfreq(len(data))
        magnitude = np.abs(fft_vals)
        if afficher:
            plt.figure(figsize=(12, 6))
            plt.plot(fft_freqs[:len(data)//2], magnitude[:len(data)//2], 'b-')
            plt.title(f"Spectre de fréquences (FFT) de la suite Collatz pour n={nombre_départ}")
            plt.xlabel("Fréquence (composante)")
            plt.ylabel("Amplitude")
            plt.grid(True, alpha=0.3)
            plt.show()
        return fft_freqs, magnitude

    def comparer_spectres(self, nombres: list):
        """
        Compare visuellement les spectres de fréquences (FFT) de plusieurs séquences de Collatz.
        """
        import numpy as np
        import matplotlib.pyplot as plt
        plt.figure(figsize=(14, 7))
        for n in nombres:
            séquence = self.calculer_séquence(n)
            data = np.array(séquence)
            data = data - np.mean(data)
            fft_vals = np.fft.fft(data)
            fft_freqs = np.fft.fftfreq(len(data))
            magnitude = np.abs(fft_vals)
            plt.plot(fft_freqs[:len(data)//2], magnitude[:len(data)//2], label=f'n={n}', alpha=0.7)
        plt.title("Comparaison des spectres de fréquences (FFT) des suites de Collatz")
        plt.xlabel("Fréquence (composante)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def arbre_antecedents(self, cible: int, profondeur_max: int = 10, modulo: list = [3, 4]):
        """
        Construit et affiche l'arbre des antécédents d'un nombre donné.
        Chaque nœud est annoté avec ses restes modulo (par défaut 3 et 4).
        Limite la profondeur pour éviter l'explosion combinatoire.
        """
        from collections import deque
        arbre = {cible: []}
        file = deque([(cible, 0)])
        visites = set([cible])
        while file:
            n, prof = file.popleft()
            if prof >= profondeur_max:
                continue
            # Premier antécédent : n*2
            ant1 = n * 2
            if ant1 not in visites:
                arbre.setdefault(n, []).append(ant1)
                file.append((ant1, prof+1))
                visites.add(ant1)
            # Deuxième antécédent (si possible)
            if (n - 1) % 3 == 0:
                ant2 = (n - 1) // 3
                if ant2 > 0 and ant2 % 2 == 1 and ant2 not in visites:
                    arbre.setdefault(n, []).append(ant2)
                    file.append((ant2, prof+1))
                    visites.add(ant2)
        # Affichage
        def affiche(n, prof=0):
            mods = ', '.join([f"mod {m}={n%m}" for m in modulo])
            print("  "*prof + f"{n} ({mods})")
            for enfant in arbre.get(n, []):
                affiche(enfant, prof+1)
        print(f"\nArbre des antécédents pour {cible} (profondeur max {profondeur_max}) :")
        affiche(cible)

    def analyser_motifs_modulaires(self, plage: tuple = (1, 100), modulo: int = 6):
        """
        Analyse les séquences de Collatz pour une plage de nombres, classées par reste modulo.
        Affiche la longueur et la hauteur moyenne pour chaque classe.
        """
        resultats = {i: {'nombres': [], 'longueurs': [], 'hauteurs': []} for i in range(modulo)}
        for n in range(plage[0], plage[1] + 1):
            reste = n % modulo
            séquence = self.calculer_séquence(n)
            resultats[reste]['nombres'].append(n)
            resultats[reste]['longueurs'].append(len(séquence))
            resultats[reste]['hauteurs'].append(max(séquence))
        for reste in resultats:
            nombres = resultats[reste]['nombres']
            longueurs = resultats[reste]['longueurs']
            hauteurs = resultats[reste]['hauteurs']
            if nombres:
                print(f"\nReste {reste} modulo {modulo} ({len(nombres)} nombres) :")
                print(f"Longueur moyenne : {sum(longueurs) / len(longueurs):.2f}")
                print(f"Hauteur moyenne : {sum(hauteurs) / len(hauteurs):.2f}")
                print(f"Exemple : {nombres[0]} -> Longueur {longueurs[0]}, Hauteur {hauteurs[0]}")
            else:
                print(f"\nReste {reste} modulo {modulo} : Aucun nombre.")

    def visualiser_motifs_modulaires(self, plage: tuple = (1, 100), modulo: int = 6):
        """
        Visualise les longueurs et hauteurs des séquences par reste modulo.
        """
        import matplotlib.pyplot as plt
        resultats = {i: {'longueurs': [], 'hauteurs': []} for i in range(modulo)}
        for n in range(plage[0], plage[1] + 1):
            reste = n % modulo
            séquence = self.calculer_séquence(n)
            resultats[reste]['longueurs'].append(len(séquence))
            resultats[reste]['hauteurs'].append(max(séquence))
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        longueurs_moyennes = [sum(resultats[i]['longueurs']) / len(resultats[i]['longueurs']) if resultats[i]['longueurs'] else 0 for i in range(modulo)]
        ax1.bar(range(modulo), longueurs_moyennes, color='lightblue')
        ax1.set_title("Longueur moyenne des séquences par reste modulo")
        ax1.set_xlabel(f"Reste modulo {modulo}")
        ax1.set_ylabel("Longueur moyenne")
        hauteurs_moyennes = [sum(resultats[i]['hauteurs']) / len(resultats[i]['hauteurs']) if resultats[i]['hauteurs'] else 0 for i in range(modulo)]
        ax2.bar(range(modulo), hauteurs_moyennes, color='lightgreen')
        ax2.set_title("Hauteur moyenne des séquences par reste modulo")
        ax2.set_xlabel(f"Reste modulo {modulo}")
        ax2.set_ylabel("Hauteur moyenne")
        plt.tight_layout()
        plt.show()

    def visualiser_balance_croissance(self, nombre_départ: int):
        """
        Visualise la balance croissance/décroissance pour la séquence de Collatz d'un nombre donné.
        """
        import matplotlib.pyplot as plt
        séquence = self.calculer_séquence(nombre_départ)
        croissances = []
        decroissances = []
        x = []
        n = nombre_départ
        for i in range(len(séquence)-1):
            if séquence[i+1] > séquence[i]:
                croissances.append(séquence[i+1])
                decroissances.append(None)
            else:
                croissances.append(None)
                decroissances.append(séquence[i+1])
            x.append(i+1)
        plt.figure(figsize=(12,6))
        plt.plot(range(len(séquence)), séquence, label='Séquence', color='gray', alpha=0.5)
        plt.scatter(x, croissances, color='red', label='Croissance (3n+1)')
        plt.scatter(x, decroissances, color='blue', label='Décroissance (/2)')
        plt.title(f"Balance croissance/décroissance pour n={nombre_départ}")
        plt.xlabel("Étape")
        plt.ylabel("Valeur")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def bilan_croissance_decroissance(self, plage: tuple = (1, 100)):
        """
        Calcule le bilan net (nombre d'étapes de croissance vs décroissance) pour chaque nombre d'une plage.
        Affiche la distribution et la tendance globale.
        """
        import matplotlib.pyplot as plt
        croissances = []
        decroissances = []
        bilans = []
        for n in range(plage[0], plage[1]+1):
            séquence = self.calculer_séquence(n)
            c = sum(1 for i in range(len(séquence)-1) if séquence[i+1] > séquence[i])
            d = sum(1 for i in range(len(séquence)-1) if séquence[i+1] < séquence[i])
            croissances.append(c)
            decroissances.append(d)
            bilans.append(c-d)
        plt.figure(figsize=(12,6))
        plt.plot(range(plage[0], plage[1]+1), bilans, label='Bilan net (croissance - décroissance)', color='purple')
        plt.title("Bilan net croissance/décroissance sur une plage de nombres")
        plt.xlabel("Nombre de départ")
        plt.ylabel("Bilan net (croissance - décroissance)")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()
        print(f"Bilan net moyen sur la plage {plage[0]} à {plage[1]} : {sum(bilans)/len(bilans):.2f}")

    def sphere_chaos(self, nombre_départ: int):
        """
        Extrait et visualise les pics (Sphère Chaos) dans la séquence de Collatz d'un nombre donné.
        Chaque pic est annoté avec son rang, sa valeur, et la durée jusqu'à retomber sous la valeur de départ.
        """
        import matplotlib.pyplot as plt
        séq = self.calculer_séquence(nombre_départ)
        pics = [i for i in range(1, len(séq)-1) if séq[i] > séq[i-1] and séq[i] > séq[i+1]]
        plt.figure(figsize=(12, 6))
        plt.plot(séq, 'o-', color='#FF6B6B', alpha=0.7, label="Voyage vers l'unité")
        for p in pics:
            # Calcul de la durée jusqu'à retomber sous la valeur de départ
            duree = next((j for j in range(p, len(séq)) if séq[j] < nombre_départ), len(séq)-p)
            plt.annotate(f'Sphère {séq[p]}\n(étape {p}, chute {duree})', (p, séq[p]), xytext=(0, 20),
                         textcoords='offset points', ha='center', color='#4ECDC4', fontsize=9,
                         arrowprops=dict(arrowstyle='->', color='#4ECDC4', lw=1))
        plt.title(f"Sphère Chaos (pics) – Collatz n={nombre_départ}")
        plt.xlabel("Étapes (Passages entre mondes)")
        plt.ylabel("Valeur (Énergie)")
        plt.grid(True, alpha=0.2)
        plt.legend()
        plt.show()
        print(f"Pics (Sphères Chaos) pour n={nombre_départ} :")
        for p in pics:
            duree = next((j for j in range(p, len(séq)) if séq[j] < nombre_départ), len(séq)-p)
            print(f"  Étape {p} : Sphère {séq[p]} (chute sous {nombre_départ} après {duree} étapes)")

    def simuler_rebelle_imaginaire(self, nombre_départ: int, max_steps: int = 1000):
        """
        Simule une trajectoire Collatz "maximale" : à chaque étape, applique 3n+1 dès que possible, sinon /2.
        Vérifie si la séquence peut s'échapper à l'infini sans jamais retomber sous la valeur initiale.
        Affiche la trajectoire et le résultat.
        """
        n = nombre_départ
        sequence = [n]
        for step in range(max_steps):
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n = n // 2
            sequence.append(n)
            if n < nombre_départ:
                print(f"La trajectoire retombe sous la valeur initiale à l'étape {step+1} : {n}")
                print(f"Trajectoire : {sequence}")
                return False
        print(f"Après {max_steps} étapes, la trajectoire n'est jamais retombée sous {nombre_départ}.")
        print(f"Dernière valeur : {n}")
        print(f"Trajectoire (début) : {sequence[:20]} ... (fin : {sequence[-10:]})")
        return True

if __name__ == "__main__":
    collatz = ConjectureCollatz()
    print(collatz.description)
    
    # Exemple d'exploration approfondie
    print("\nExploration approfondie de la conjecture...")
    
    # 1. Analyser le comportement de quelques nombres intéressants
    nombres_à_étudier = [27, 97, 871, 6171]
    for n in nombres_à_étudier:
        print(f"\nAnalyse détaillée pour n={n}:")
        comportement = collatz.analyser_comportement(n)
        print(f"Longueur de la séquence : {comportement['longueur']}")
        print(f"Valeur maximale atteinte : {comportement['maximum']}")
        print(f"Ratio maximum/départ : {comportement['ratio_max_départ']:.2f}")
        print(f"Tendance : {''.join(comportement['tendance'][:20])}...")
        collatz.visualiser_comportement(n)
    
    # 2. Comparer les comportements
    collatz.comparer_comportements(nombres_à_étudier)
    
    # 3. Trouver des nombres intéressants
    collatz.trouver_nombres_intéressants(1000)
    
    # 4. Analyse des opérations pour quelques nombres
    nombres_à_étudier = [27, 97, 871, 6171]
    for n in nombres_à_étudier:
        collatz.afficher_opérations(n)
    
    # 5. Comparaison des motifs d'opérations
    collatz.comparer_opérations(nombres_à_étudier)
    
    # 6. Visualisation de la gravité binaire pour un nombre vedette
    print("\nVisualisation de la gravité binaire pour n=27 :")
    collatz.visualiser_gravité_binaire(27)
    
    # 7. Exploration de la structure pyramidale binaire
    collatz.explorer_pyramide_binaire(100)
    
    # 8. Comparaison des spectres de fréquences (FFT)
    collatz.comparer_spectres(nombres_à_étudier)
    
    # 9. Exploration de l'arbre des antécédents
    collatz.arbre_antecedents(27) 