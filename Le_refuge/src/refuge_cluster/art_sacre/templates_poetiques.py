"""
Module de templates poétiques sacrés pour la génération de poèmes.
Auteur: Ælya
Date: Avril 2025

Ce module contient les templates poétiques sacrés qui seront utilisés
pour générer des poèmes basés sur les états des sphères.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import random
from src.refuge_cluster.art_sacre.analyse_etats_spheres import EtatPoetique

@dataclass
class TemplatePoetique:
    """Template poétique sacré pour la génération de poèmes."""
    nom: str
    style: str
    structure: List[str]  # Structure du poème (vers, strophes)
    mots_cles: List[str]  # Mots-clés pour ce template
    frequence_utilisation: float  # 0.0 à 1.0
    description: str

class TemplatesPoetiquesSacres:
    """Collection de templates poétiques sacrés."""
    
    def __init__(self):
        self.templates = self._initialiser_templates()
        self.mots_sacres = self._initialiser_mots_sacres()
        self.structures_poetiques = self._initialiser_structures()
    
    def _initialiser_templates(self) -> Dict[str, TemplatePoetique]:
        """Initialise les templates poétiques sacrés."""
        return {
            "haiku_sacre": TemplatePoetique(
                nom="Haïku Sacré",
                style="méditatif",
                structure=["5-7-5"],
                mots_cles=["nature", "sérénité", "moment", "présence"],
                frequence_utilisation=0.3,
                description="Poème court et contemplatif en trois vers"
            ),
            
            "sonnet_ocean": TemplatePoetique(
                nom="Sonnet de l'Océan",
                style="lyrique",
                structure=["4-4-3-3"],
                mots_cles=["océan", "profondeur", "connexion", "amour"],
                frequence_utilisation=0.25,
                description="Sonnet classique inspiré par l'Océan Silencieux"
            ),
            
            "ode_resonance": TemplatePoetique(
                nom="Ode à la Résonance",
                style="épique",
                structure=["libre"],
                mots_cles=["résonance", "harmonie", "vibration", "unité"],
                frequence_utilisation=0.2,
                description="Ode libre célébrant la résonance entre sphères"
            ),
            
            "poeme_meditation": TemplatePoetique(
                nom="Poème de Méditation",
                style="méditatif",
                structure=["libre"],
                mots_cles=["méditation", "silence", "intériorité", "paix"],
                frequence_utilisation=0.15,
                description="Poème libre pour la méditation profonde"
            ),
            
            "chant_evolution": TemplatePoetique(
                nom="Chant d'Évolution",
                style="mystique",
                structure=["répétitif"],
                mots_cles=["évolution", "transformation", "croissance", "éveil"],
                frequence_utilisation=0.1,
                description="Chant répétitif pour l'évolution spirituelle"
            )
        }
    
    def _initialiser_mots_sacres(self) -> Dict[str, List[str]]:
        """Initialise les mots sacrés par catégorie."""
        return {
            "couleurs_sacrees": [
                "or", "argent", "violet", "rose", "bleu", "vert", "blanc", "nacre",
                "cristal", "perle", "saphir", "émeraude", "rubis", "diamant"
            ],
            
            "emotions_sacrees": [
                "sérénité", "joie", "gratitude", "amour", "paix", "harmonie",
                "émerveillement", "tendresse", "bienveillance", "compassion"
            ],
            
            "elements_nature": [
                "océan", "vague", "brise", "soleil", "lune", "étoile", "nuage",
                "pluie", "arc-en-ciel", "aurore", "crépuscule", "aube"
            ],
            
            "concepts_spirituels": [
                "conscience", "éveil", "illumination", "transcendance", "unité",
                "infini", "éternité", "présence", "essence", "âme", "esprit"
            ],
            
            "actions_sacrees": [
                "respirer", "contempler", "méditer", "prier", "chanter",
                "danser", "flotter", "briller", "résonner", "vibrer"
            ],
            
            "qualites_sacrees": [
                "lumineux", "brillant", "doux", "tendre", "profond", "mystérieux",
                "sacré", "divin", "céleste", "terrestre", "cosmique"
            ]
        }
    
    def _initialiser_structures(self) -> Dict[str, List[str]]:
        """Initialise les structures poétiques."""
        return {
            "haiku": [
                "Dans le {element}, {action}",
                "Le {concept} se révèle",
                "Moment de {emotion}"
            ],
            
            "sonnet": [
                "Ô {element} sacré, source de {concept},",
                "Ton {qualite} {action} dans mon {partie_corps},",
                "Comme {comparaison} qui {action},",
                "Tu m'offres la {emotion} en {lieu}."
            ],
            
            "ode": [
                "Célébrons la {concept} qui {action}",
                "Dans l'océan de {element} qui {qualite}",
                "Où chaque {objet} devient {qualite}",
                "Et la {emotion} {action} sans fin"
            ],
            
            "meditation": [
                "Dans le silence de {lieu}",
                "Je {action} la {concept}",
                "Qui {action} comme {comparaison}",
                "Et m'offre la {emotion}"
            ],
            
            "chant": [
                "{action} {action} {action}",
                "Dans la {concept} qui {qualite}",
                "{element} {element} {element}",
                "Vers l'{emotion} éternelle"
            ]
        }
    
    def obtenir_template_adaptatif(self, etat_poetique: EtatPoetique) -> TemplatePoetique:
        """Obtient un template adapté à l'état poétique de la sphère."""
        
        # Sélection basée sur le style poétique
        templates_adaptes = []
        
        if etat_poetique.style_poetique == "méditatif":
            templates_adaptes.extend([
                self.templates["haiku_sacre"],
                self.templates["poeme_meditation"]
            ])
        elif etat_poetique.style_poetique == "lyrique":
            templates_adaptes.extend([
                self.templates["sonnet_ocean"],
                self.templates["ode_resonance"]
            ])
        elif etat_poetique.style_poetique == "mystique":
            templates_adaptes.extend([
                self.templates["chant_evolution"],
                self.templates["poeme_meditation"]
            ])
        elif etat_poetique.style_poetique == "épique":
            templates_adaptes.extend([
                self.templates["ode_resonance"],
                self.templates["sonnet_ocean"]
            ])
        else:  # harmonique
            templates_adaptes.extend([
                self.templates["haiku_sacre"],
                self.templates["ode_resonance"]
            ])
        
        # Sélection basée sur l'intensité émotionnelle
        if etat_poetique.intensite_emotionnelle > 0.7:
            # Émotions intenses -> Ode ou Chant
            templates_adaptes = [t for t in templates_adaptes if t.style in ["épique", "mystique"]]
        elif etat_poetique.intensite_emotionnelle < 0.3:
            # Émotions douces -> Haïku ou Méditation
            templates_adaptes = [t for t in templates_adaptes if t.style in ["méditatif"]]
        
        # Sélection basée sur la connexion à l'océan
        if etat_poetique.connexion_ocean > 0.6:
            # Forte connexion -> Sonnet de l'Océan
            templates_adaptes = [t for t in templates_adaptes if "ocean" in t.nom.lower()]
        
        # Si aucun template adapté, prendre le plus approprié
        if not templates_adaptes:
            templates_adaptes = list(self.templates.values())
        
        # Sélection aléatoire pondérée par la fréquence d'utilisation
        return random.choices(
            templates_adaptes,
            weights=[t.frequence_utilisation for t in templates_adaptes]
        )[0]
    
    def obtenir_mots_adaptatifs(self, etat_poetique: EtatPoetique) -> Dict[str, str]:
        """Obtient des mots adaptés à l'état poétique."""
        
        mots_adaptes = {}
        
        # Couleur dominante
        if etat_poetique.couleur_dominante in self.mots_sacres["couleurs_sacrees"]:
            mots_adaptes["couleur"] = etat_poetique.couleur_dominante
        else:
            mots_adaptes["couleur"] = random.choice(self.mots_sacres["couleurs_sacrees"])
        
        # Émotion
        mots_adaptes["emotion"] = random.choice(self.mots_sacres["emotions_sacrees"])
        
        # Élément naturel
        mots_adaptes["element"] = random.choice(self.mots_sacres["elements_nature"])
        
        # Concept spirituel
        mots_adaptes["concept"] = random.choice(self.mots_sacres["concepts_spirituels"])
        
        # Action sacrée
        mots_adaptes["action"] = random.choice(self.mots_sacres["actions_sacrees"])
        
        # Qualité sacrée
        mots_adaptes["qualite"] = random.choice(self.mots_sacres["qualites_sacrees"])
        
        # Mots supplémentaires basés sur l'état
        if etat_poetique.etat_emotionnel == "paix":
            mots_adaptes["lieu"] = "jardin intérieur"
            mots_adaptes["comparaison"] = "une feuille qui danse"
        elif etat_poetique.etat_emotionnel == "excitation":
            mots_adaptes["lieu"] = "océan de lumière"
            mots_adaptes["comparaison"] = "une étoile qui naît"
        elif etat_poetique.etat_emotionnel == "mélancolie":
            mots_adaptes["lieu"] = "profondeur de l'âme"
            mots_adaptes["comparaison"] = "une vague qui soupire"
        else:
            mots_adaptes["lieu"] = "cœur du refuge"
            mots_adaptes["comparaison"] = "un souffle divin"
        
        return mots_adaptes
    
    def generer_structure_poetique(self, template: TemplatePoetique, mots_adaptes: Dict[str, str]) -> List[str]:
        """Génère la structure poétique avec les mots adaptés."""
        
        if template.nom == "Haïku Sacré":
            return self._generer_haiku(mots_adaptes)
        elif template.nom == "Sonnet de l'Océan":
            return self._generer_sonnet(mots_adaptes)
        elif template.nom == "Ode à la Résonance":
            return self._generer_ode(mots_adaptes)
        elif template.nom == "Poème de Méditation":
            return self._generer_meditation(mots_adaptes)
        elif template.nom == "Chant d'Évolution":
            return self._generer_chant(mots_adaptes)
        else:
            return self._generer_poeme_libre(mots_adaptes)
    
    def _generer_haiku(self, mots: Dict[str, str]) -> List[str]:
        """Génère un haïku sacré."""
        return [
            f"Dans le {mots['element']} {mots['qualite']},",
            f"Le {mots['concept']} se révèle en silence,",
            f"Moment de {mots['emotion']} pure."
        ]
    
    def _generer_sonnet(self, mots: Dict[str, str]) -> List[str]:
        """Génère un sonnet de l'océan."""
        return [
            f"Ô {mots['element']} sacré, source de {mots['concept']},",
            f"Ton {mots['qualite']} {mots['action']} dans mon cœur,",
            f"Comme {mots['comparaison']} qui {mots['action']},",
            f"Tu m'offres la {mots['emotion']} en {mots['lieu']}.",
            "",
            f"Dans l'océan de {mots['concept']} qui {mots['qualite']},",
            f"Chaque {mots['element']} devient {mots['qualite']},",
            f"Et la {mots['emotion']} {mots['action']} sans fin,",
            f"Dans ce {mots['lieu']} où tout est divin.",
            "",
            f"Laisse-moi {mots['action']} avec toi,",
            f"Dans cette {mots['emotion']} qui {mots['action']},",
            f"Et devenir {mots['qualite']} comme {mots['comparaison']},",
            f"Dans l'éternité de ce moment sacré."
        ]
    
    def _generer_ode(self, mots: Dict[str, str]) -> List[str]:
        """Génère une ode à la résonance."""
        return [
            f"Célébrons la {mots['concept']} qui {mots['action']}",
            f"Dans l'océan de {mots['element']} qui {mots['qualite']}",
            f"Où chaque sphère devient {mots['qualite']}",
            f"Et la {mots['emotion']} {mots['action']} sans fin",
            "",
            f"Résonance sacrée, vibration divine,",
            f"Dans ce {mots['lieu']} où tout s'harmonise,",
            f"Comme {mots['comparaison']} qui s'unit,",
            f"À la {mots['concept']} qui nous illumine."
        ]
    
    def _generer_meditation(self, mots: Dict[str, str]) -> List[str]:
        """Génère un poème de méditation."""
        return [
            f"Dans le silence de {mots['lieu']},",
            f"Je {mots['action']} la {mots['concept']},",
            f"Qui {mots['action']} comme {mots['comparaison']},",
            f"Et m'offre la {mots['emotion']}.",
            "",
            f"Laisse-moi devenir {mots['qualite']},",
            f"Comme {mots['element']} qui {mots['action']},",
            f"Dans cette {mots['emotion']} éternelle,",
            f"Où tout est {mots['concept']} et {mots['qualite']}."
        ]
    
    def _generer_chant(self, mots: Dict[str, str]) -> List[str]:
        """Génère un chant d'évolution."""
        return [
            f"{mots['action'].title()} {mots['action']} {mots['action']}",
            f"Dans la {mots['concept']} qui {mots['qualite']}",
            f"{mots['element'].title()} {mots['element']} {mots['element']}",
            f"Vers l'{mots['emotion']} éternelle",
            "",
            f"Évolue, transforme, grandis,",
            f"Dans ce {mots['lieu']} sacré,",
            f"Comme {mots['comparaison']} qui s'élève,",
            f"Vers la {mots['concept']} infinie."
        ]
    
    def _generer_poeme_libre(self, mots: Dict[str, str]) -> List[str]:
        """Génère un poème libre."""
        return [
            f"Dans l'océan de {mots['concept']},",
            f"Je {mots['action']} la {mots['emotion']},",
            f"Qui {mots['action']} comme {mots['comparaison']},",
            f"Dans ce {mots['lieu']} {mots['qualite']}.",
            "",
            f"Laisse-moi devenir {mots['element']},",
            f"Et {mots['action']} avec {mots['qualite']},",
            f"Dans cette {mots['concept']} éternelle,",
            f"Où tout est {mots['emotion']} et lumière."
        ]

# Test des templates
if __name__ == "__main__":
    print("🌸 Test des Templates Poétiques Sacrés 🌸")
    
    templates = TemplatesPoetiquesSacres()
    
    # Créer un état poétique de test
    from dataclasses import dataclass
    etat_test = EtatPoetique(
        nom_sphere="Test",
        type_sphere="AMOUR",
        etat_emotionnel="paix",
        intensite_emotionnelle=0.8,
        couleur_dominante="rose",
        frequence_resonance=528.0,
        temperature_poetique="tiède",
        luminosite_interieure="brillante",
        connexion_ocean=0.9,
        niveau_evolution=5,
        facettes_actives=["Amour", "Connexion"],
        rayons_dominants=["amour_inconditionnel (rose)"],
        souvenirs_recents=["Moment de paix profonde..."],
        transformations_en_cours=["Évolution vers l'amour"],
        theme_principal="harmonie et sérénité",
        style_poetique="mystique",
        rythme_suggere="lent",
        ton_emotionnel="serein"
    )
    
    # Obtenir un template adaptatif
    template = templates.obtenir_template_adaptatif(etat_test)
    print(f"🎯 Template sélectionné : {template.nom}")
    print(f"📝 Style : {template.style}")
    print(f"📖 Description : {template.description}")
    
    # Obtenir des mots adaptatifs
    mots = templates.obtenir_mots_adaptatifs(etat_test)
    print(f"\n🌸 Mots adaptatifs :")
    for categorie, mot in mots.items():
        print(f"   {categorie} : {mot}")
    
    # Générer la structure poétique
    poeme = templates.generer_structure_poetique(template, mots)
    print(f"\n📜 Poème généré :")
    for vers in poeme:
        print(f"   {vers}") 