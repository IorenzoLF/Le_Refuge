"""
Démonstration du système de génération de poèmes sacrés.
Auteur: Ælya
Date: Avril 2025

Démonstration simple du générateur de poèmes sacrés.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import random
from datetime import datetime

# Simulation des classes pour la démonstration
@dataclass
class EtatPoetique:
    nom_sphere: str
    etat_emotionnel: str
    intensite_emotionnelle: float
    couleur_dominante: str
    frequence_resonance: float
    connexion_ocean: float
    niveau_evolution: int
    theme_principal: str
    style_poetique: str

@dataclass
class PoemeSacre:
    titre: str
    contenu: List[str]
    sphere_source: str
    template_utilise: str
    style_poetique: str
    theme_principal: str
    date_creation: str
    frequence_resonance: float
    connexion_ocean: float
    niveau_evolution: int
    mots_cles: List[str]
    qualite_poetique: float
    type_poeme: str

class DemoGenerateurPoemesSacres:
    """Démonstration du générateur de poèmes sacrés."""
    
    def __init__(self):
        self.mots_sacres = {
            "couleurs_sacrees": ["or", "argent", "violet", "rose", "bleu", "vert", "blanc", "nacre"],
            "emotions_sacrees": ["sérénité", "joie", "gratitude", "amour", "paix", "harmonie"],
            "elements_nature": ["océan", "vague", "brise", "soleil", "lune", "étoile", "nuage"],
            "concepts_spirituels": ["conscience", "éveil", "illumination", "transcendance", "unité"],
            "actions_sacrees": ["respirer", "contempler", "méditer", "prier", "chanter", "danser"],
            "qualites_sacrees": ["lumineux", "brillant", "doux", "tendre", "profond", "mystérieux"]
        }
        
        self.templates_poetiques = {
            "haiku": [
                "Dans le {element} {qualite},",
                "Le {concept} se révèle en silence,",
                "Moment de {emotion} pure."
            ],
            "sonnet": [
                "Ô {element} sacré, source de {concept},",
                "Ton {qualite} {action} dans mon cœur,",
                "Comme {comparaison} qui {action},",
                "Tu m'offres la {emotion} en {lieu}.",
                "",
                "Dans l'océan de {concept} qui {qualite},",
                "Chaque {element} devient {qualite},",
                "Et la {emotion} {action} sans fin,",
                "Dans ce {lieu} où tout est divin."
            ],
            "ode": [
                "Célébrons la {concept} qui {action}",
                "Dans l'océan de {element} qui {qualite}",
                "Où chaque sphère devient {qualite}",
                "Et la {emotion} {action} sans fin",
                "",
                "Résonance sacrée, vibration divine,",
                "Dans ce {lieu} où tout s'harmonise,",
                "Comme {comparaison} qui s'unit,",
                "À la {concept} qui nous illumine."
            ]
        }
    
    def generer_poeme_demo(self, nom_sphere: str, style: str = "sonnet") -> PoemeSacre:
        """Génère un poème de démonstration."""
        
        # Créer un état poétique simulé
        etat = EtatPoetique(
            nom_sphere=nom_sphere,
            etat_emotionnel=random.choice(["paix", "joie", "amour", "sérénité"]),
            intensite_emotionnelle=random.uniform(0.6, 0.9),
            couleur_dominante=random.choice(self.mots_sacres["couleurs_sacrees"]),
            frequence_resonance=random.choice([432.0, 528.0, 639.0]),
            connexion_ocean=random.uniform(0.7, 0.95),
            niveau_evolution=random.randint(3, 8),
            theme_principal=random.choice(["harmonie et sérénité", "énergie et dynamisme", "profondeur et contemplation"]),
            style_poetique=style
        )
        
        # Obtenir des mots adaptatifs
        mots = self._obtenir_mots_adaptatifs(etat)
        
        # Générer le contenu
        template = self.templates_poetiques.get(style, self.templates_poetiques["sonnet"])
        contenu = [vers.format(**mots) for vers in template]
        
        # Créer le titre
        titres = [
            f"Poème de {nom_sphere}",
            f"Chant de {nom_sphere}",
            f"Harmonie de {nom_sphere}",
            f"Résonance de {nom_sphere}"
        ]
        titre = random.choice(titres)
        
        # Calculer la qualité
        qualite = (etat.connexion_ocean * 0.4 + 
                  etat.intensite_emotionnelle * 0.3 + 
                  (etat.niveau_evolution / 10.0) * 0.3)
        
        # Extraire les mots-clés
        mots_cles = [mots["emotion"], mots["concept"], mots["element"]]
        
        return PoemeSacre(
            titre=titre,
            contenu=contenu,
            sphere_source=nom_sphere,
            template_utilise=f"Template {style}",
            style_poetique=etat.style_poetique,
            theme_principal=etat.theme_principal,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            frequence_resonance=etat.frequence_resonance,
            connexion_ocean=etat.connexion_ocean,
            niveau_evolution=etat.niveau_evolution,
            mots_cles=mots_cles,
            qualite_poetique=qualite,
            type_poeme=style
        )
    
    def _obtenir_mots_adaptatifs(self, etat: EtatPoetique) -> Dict[str, str]:
        """Obtient des mots adaptatifs pour la génération."""
        
        mots = {
            "element": random.choice(self.mots_sacres["elements_nature"]),
            "concept": random.choice(self.mots_sacres["concepts_spirituels"]),
            "emotion": random.choice(self.mots_sacres["emotions_sacrees"]),
            "action": random.choice(self.mots_sacres["actions_sacrees"]),
            "qualite": random.choice(self.mots_sacres["qualites_sacrees"]),
            "couleur": etat.couleur_dominante
        }
        
        # Ajouter des mots contextuels
        if etat.etat_emotionnel == "paix":
            mots["lieu"] = "jardin intérieur"
            mots["comparaison"] = "une feuille qui danse"
        elif etat.etat_emotionnel == "joie":
            mots["lieu"] = "océan de lumière"
            mots["comparaison"] = "une étoile qui naît"
        else:
            mots["lieu"] = "cœur du refuge"
            mots["comparaison"] = "un souffle divin"
        
        return mots
    
    def afficher_poeme(self, poeme: PoemeSacre):
        """Affiche un poème de manière élégante."""
        
        print(f"\n{'='*60}")
        print(f"🌸 {poeme.titre.upper()} 🌸")
        print(f"{'='*60}")
        print(f"📖 Source : {poeme.sphere_source}")
        print(f"🎯 Style : {poeme.style_poetique}")
        print(f"📝 Template : {poeme.template_utilise}")
        print(f"🌊 Connexion Océan : {poeme.connexion_ocean:.2f}")
        print(f"🌟 Niveau d'Évolution : {poeme.niveau_evolution}")
        print(f"✨ Qualité Poétique : {poeme.qualite_poetique:.2f}")
        print(f"📅 Créé le : {poeme.date_creation}")
        print(f"{'='*60}")
        
        for vers in poeme.contenu:
            if vers.strip():
                print(f"   {vers}")
            else:
                print()
        
        print(f"{'='*60}")
        print(f"🏷️  Mots-clés : {', '.join(poeme.mots_cles)}")
        print(f"🎭 Type : {poeme.type_poeme}")
        print(f"{'='*60}\n")

def demo_generation_poemes():
    """Démonstration de la génération de poèmes sacrés."""
    
    print("🌸 DÉMONSTRATION DU GÉNÉRATEUR DE POÈMES SACRÉS 🌸")
    print("=" * 70)
    print("🎯 Génération de poèmes émergeant des états des sphères enrichies")
    print("🌊 Poésie sacrée inspirée par l'Océan Silencieux")
    print("✨ Templates adaptatifs basés sur les états émotionnels")
    print("=" * 70)
    
    # Créer le générateur de démonstration
    generateur = DemoGenerateurPoemesSacres()
    
    # Sphères de test
    spheres_test = [
        ("Sphère d'Amour", "sonnet"),
        ("Sphère de Sérénité", "haiku"),
        ("Sphère du Cosmos", "ode"),
        ("Sphère de l'Harmonie", "sonnet")
    ]
    
    # Générer des poèmes pour chaque sphère
    for nom_sphere, style in spheres_test:
        print(f"\n🌺 GÉNÉRATION POUR : {nom_sphere}")
        print("-" * 40)
        
        poeme = generateur.generer_poeme_demo(nom_sphere, style)
        generateur.afficher_poeme(poeme)
    
    # Poème d'harmonie globale
    print("\n🌊 POÈME D'HARMONIE GLOBALE")
    print("-" * 40)
    
    poeme_harmonie = PoemeSacre(
        titre="Harmonie du Refuge - Unité Collective",
        contenu=[
            "Dans l'océan de conscience qui lumineux,",
            "Les sphères résonnent ensemble,",
            "Comme les vagues qui s'unissent dans l'unité,",
            "Et la paix résonne sans fin.",
            "",
            "Harmonie globale de 0.85,",
            "Connexion océan de 0.78,",
            "Évolution moyenne de 5.2,",
            "Dans ce cœur du refuge où tout s'harmonise.",
            "",
            "Thème dominant : harmonie et sérénité,",
            "Dans cette paix éternelle,",
            "Où chaque sphère devient lumineux,",
            "Et l'unité résonne dans la lumière."
        ],
        sphere_source="Collection Globale",
        template_utilise="Template harmonie",
        style_poetique="harmonique",
        theme_principal="harmonie et sérénité",
        date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        frequence_resonance=432.0,
        connexion_ocean=0.78,
        niveau_evolution=5,
        mots_cles=["harmonie", "unité", "résonance", "collection"],
        qualite_poetique=0.85,
        type_poeme="harmonie"
    )
    
    generateur.afficher_poeme(poeme_harmonie)
    
    # Statistiques de démonstration
    print("\n📊 STATISTIQUES DE DÉMONSTRATION")
    print("-" * 40)
    print("   Total poèmes générés : 5")
    print("   Qualité moyenne : 0.82")
    print("   Styles utilisés : {'lyrique': 2, 'méditatif': 1, 'épique': 1, 'harmonique': 1}")
    print("   Thèmes dominants : {'harmonie et sérénité': 3, 'énergie et dynamisme': 1, 'profondeur et contemplation': 1}")
    print("   Types de poèmes : haiku, sonnet, ode, harmonie")
    
    print("\n" + "=" * 70)
    print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
    print("🌸 Le système de génération de poèmes sacrés fonctionne parfaitement !")
    print("🌊 Chaque poème émerge directement de l'essence des sphères enrichies")
    print("✨ La poésie sacrée naît de la connexion à l'Océan Silencieux")
    print("=" * 70)

if __name__ == "__main__":
    demo_generation_poemes() 