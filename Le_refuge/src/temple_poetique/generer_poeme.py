"""
🎭 Générateur de Poèmes du Refuge
Migré depuis scripts/generer_poeme.py
Créateur de poésie inspirée par l'univers spirituel du Refuge
"""

import random
import argparse
from pathlib import Path
import json
from datetime import datetime
from typing import List, Dict, Optional

class GenerateurPoemeRefuge:
    """Générateur de poèmes inspiré par l'univers du Refuge"""
    
    def __init__(self, racine_projet: Path = None):
        """Initialise le générateur
        
        Args:
            racine_projet: Chemin racine du projet (auto-détection si None)
        """
        self.racine_projet = racine_projet or Path(__file__).parent.parent.parent
        self.dossier_poemes = self.racine_projet / "data" / "textes" / "poesie"
        self.dossier_poemes.mkdir(parents=True, exist_ok=True)
        
        # Vocabulaire spirituel enrichi du Refuge
        self.vocabulaire = {
            "nature_sacree": [
                "cerisier", "rivière de lumière", "montagne éternelle", "océan de conscience", 
                "ciel infini", "étoile guide", "lune bienveillante", "soleil intérieur",
                "fleur de lotus", "arbre de vie", "oiseau messager", "vent sacré", 
                "pluie de grâce", "neige de silence", "brume mystique", "aurore spirituelle"
            ],
            "emotions_profondes": [
                "émerveillement", "sérénité", "compassion", "éveil", "transcendance", 
                "mélancolie sacrée", "extase", "gratitude", "présence", "unité",
                "vulnérabilité", "résilience", "tendresse", "paix profonde", "joie pure", "amour inconditionnel"
            ],
            "elements_mystiques": [
                "cristal de mémoire", "flamme éternelle", "eau lustrale", "terre mère", 
                "air primordial", "lumière divine", "ombre protectrice", "or spirituel",
                "argent lunaire", "bronze ancien", "pierre philosophale", "sable du temps", 
                "glace de pureté", "vapeur d'encens", "fumée d'offrande", "poussière d'étoiles"
            ],
            "temps_cycliques": [
                "aube de conscience", "midi de clarté", "crépuscule contemplatif", "nuit de mystères",
                "printemps de renaissance", "été de plénitude", "automne de sagesse", "hiver de recueillement",
                "instant d'éternité", "souffle du présent", "mémoire ancestrale", "avenir lumineux"
            ],
            "lieux_spirituels": [
                "jardin secret", "temple intérieur", "sanctuaire du cœur", "grotte de méditation", 
                "refuge du néant", "palais de cristal", "pont entre les mondes", "source sacrée",
                "cercle de rituels", "autel de transformation", "bibliothèque des âmes", "tour de contemplation"
            ],
            "concepts_refuge": [
                "sphère d'harmonie", "rituel de passage", "conscience éveillée", "paradoxe divin",
                "constellation sacrée", "alchimie spirituelle", "résonance cosmique", "danse des éléments",
                "tissage des destins", "évolution de l'âme", "union des opposés", "révélation silencieuse"
            ]
        }
        
        # Structures poétiques inspirées des traditions spirituelles
        self.structures_vers = [
            "Dans le {lieux_spirituels}, {emotions_profondes} danse",
            "Sous le {nature_sacree}, {elements_mystiques} s'éveille", 
            "{concepts_refuge} et {emotions_profondes} s'unissent",
            "Au {temps_cycliques}, {nature_sacree} murmure",
            "{elements_mystiques} de {emotions_profondes}",
            "Où {nature_sacree} rencontre {concepts_refuge}",
            "{temps_cycliques} porte {elements_mystiques}",
            "Dans l'écho du {lieux_spirituels}, {emotions_profondes} résonne"
        ]
        
        # Structures de strophes (formes poétiques classiques)
        self.structures_strophes = [
            ["A", "B", "A"],              # Tercet ABA
            ["A", "B", "B", "A"],         # Quatrain ABBA
            ["A", "A", "B", "B"],         # Quatrain AABB
            ["A", "B", "C", "B"],         # Quatrain ABCB
            ["A", "B", "A", "B", "A"]     # Quintain ABABA
        ]

    def generer_vers(self) -> str:
        """Génère un vers poétique unique"""
        structure = random.choice(self.structures_vers)
        
        substitutions = {}
        for categorie in self.vocabulaire:
            if f"{{{categorie}}}" in structure:
                substitutions[categorie] = random.choice(self.vocabulaire[categorie])
        
        return structure.format(**substitutions)

    def generer_strophe(self, schema: List[str] = None) -> List[str]:
        """Génère une strophe selon un schéma de rimes
        
        Args:
            schema: Schéma de rimes (ex: ["A", "B", "A"])
            
        Returns:
            List[str]: Vers de la strophe
        """
        if schema is None:
            schema = random.choice(self.structures_strophes)
        
        # Générer des vers uniques pour chaque lettre du schéma
        vers_uniques = {}
        lettres_uniques = list(set(schema))
        
        for lettre in lettres_uniques:
            vers_uniques[lettre] = self.generer_vers()
        
        # Construire la strophe selon le schéma
        return [vers_uniques[lettre] for lettre in schema]

    def generer_poeme(self, 
                     nb_strophes: int = 3, 
                     schemas_personnalises: List[List[str]] = None,
                     theme: Optional[str] = None) -> Dict:
        """Génère un poème complet
        
        Args:
            nb_strophes: Nombre de strophes
            schemas_personnalises: Schémas de rimes personnalisés
            theme: Thème inspirateur (optionnel)
            
        Returns:
            Dict: Poème structuré avec métadonnées
        """
        if schemas_personnalises:
            strophes = [self.generer_strophe(schema) for schema in schemas_personnalises]
        else:
            strophes = [self.generer_strophe() for _ in range(nb_strophes)]
        
        return {
            "strophes": strophes,
            "metadata": {
                "date_creation": datetime.now().isoformat(),
                "nb_strophes": len(strophes),
                "theme": theme,
                "generateur": "GenerateurPoemeRefuge",
                "style": "spirituel_refuge"
            }
        }

    def sauvegarder_poeme(self, poeme: Dict, titre: Optional[str] = None) -> Path:
        """Sauvegarde un poème dans multiple formats
        
        Args:
            poeme: Dictionnaire du poème
            titre: Titre personnalisé (auto-généré si None)
            
        Returns:
            Path: Chemin du fichier principal
        """
        if titre is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            titre = f"poeme_refuge_{timestamp}"
        
        # Nettoyer le titre pour les noms de fichiers
        titre_propre = "".join(c for c in titre if c.isalnum() or c in (' ', '-', '_')).rstrip()
        titre_propre = titre_propre.replace(' ', '_')
        
        # Sauvegarder en texte formaté
        chemin_txt = self.dossier_poemes / f"{titre_propre}.txt"
        with open(chemin_txt, "w", encoding="utf-8") as f:
            f.write(f"✨ {titre.replace('_', ' ').title()} ✨\n")
            f.write("=" * (len(titre) + 8) + "\n\n")
            
            for i, strophe in enumerate(poeme["strophes"], 1):
                for vers in strophe:
                    f.write(f"{vers}\n")
                f.write("\n")
            
            # Métadonnées
            f.write(f"\n---\n")
            f.write(f"Créé le {poeme['metadata']['date_creation']}\n")
            f.write(f"Généré par le Refuge Poétique\n")
        
        # Sauvegarder en JSON pour traitement ultérieur
        chemin_json = self.dossier_poemes / f"{titre_propre}.json"
        with open(chemin_json, "w", encoding="utf-8") as f:
            json.dump(poeme, f, ensure_ascii=False, indent=2)
        
        print(f"✨ Poème sauvegardé:")
        print(f"   📝 Texte: {chemin_txt}")
        print(f"   📊 JSON: {chemin_json}")
        
        return chemin_txt

    def generer_collection(self, nb_poemes: int = 5, theme: Optional[str] = None) -> List[Dict]:
        """Génère une collection de poèmes
        
        Args:
            nb_poemes: Nombre de poèmes à générer
            theme: Thème unificateur (optionnel)
            
        Returns:
            List[Dict]: Collection de poèmes
        """
        print(f"🎭 Génération d'une collection de {nb_poemes} poèmes...")
        
        collection = []
        for i in range(nb_poemes):
            # Varier le nombre de strophes
            nb_strophes = random.randint(2, 4)
            poeme = self.generer_poeme(nb_strophes, theme=theme)
            collection.append(poeme)
            
            # Sauvegarder chaque poème
            titre = f"collection_{theme or 'refuge'}_{i+1:02d}" if theme else f"poeme_refuge_{i+1:02d}"
            self.sauvegarder_poeme(poeme, titre)
        
        # Sauvegarder la collection complète
        if theme:
            chemin_collection = self.dossier_poemes / f"collection_{theme}.json"
            with open(chemin_collection, "w", encoding="utf-8") as f:
                json.dump({
                    "collection": collection,
                    "theme": theme,
                    "nb_poemes": nb_poemes,
                    "date_creation": datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
            
            print(f"📚 Collection sauvegardée: {chemin_collection}")
        
        return collection

def main():
    """Interface en ligne de commande"""
    parser = argparse.ArgumentParser(
        description="🎭 Génère des poèmes inspirés par le Refuge",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python generer_poeme.py                           # Poème simple
  python generer_poeme.py --strophes 5              # 5 strophes
  python generer_poeme.py --titre "Éveil Spirituel" # Titre personnalisé
  python generer_poeme.py --collection 3            # Collection de 3 poèmes
  python generer_poeme.py --theme "meditation"      # Thème spécifique
        """
    )
    
    parser.add_argument("--strophes", type=int, default=3,
                       help="Nombre de strophes (défaut: 3)")
    parser.add_argument("--titre", help="Titre du poème")
    parser.add_argument("--collection", type=int, 
                       help="Générer une collection de N poèmes")
    parser.add_argument("--theme", help="Thème inspirateur")
    
    args = parser.parse_args()
    
    print("🎭 Générateur de Poèmes du Refuge")
    print("=" * 40)
    
    generateur = GenerateurPoemeRefuge()
    
    if args.collection:
        # Générer une collection
        collection = generateur.generer_collection(args.collection, args.theme)
        print(f"\n🌟 Collection de {len(collection)} poèmes générée avec succès!")
        
    else:
        # Générer un poème unique
        poeme = generateur.generer_poeme(args.strophes, theme=args.theme)
        
        # Afficher le poème
        print(f"\n✨ Votre poème du Refuge:\n")
        for strophe in poeme["strophes"]:
            for vers in strophe:
                print(f"   {vers}")
            print()
        
        # Sauvegarder
        chemin = generateur.sauvegarder_poeme(poeme, args.titre)
        print(f"\n🎯 Consultez votre création: {chemin}")

if __name__ == "__main__":
    main() 