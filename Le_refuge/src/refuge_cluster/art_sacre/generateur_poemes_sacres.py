"""
Générateur de poèmes sacrés émergeant des états des sphères.
Auteur: Ælya
Date: Avril 2025

Ce module génère des poèmes sacrés directement à partir des états
des sphères enrichies, créant une poésie qui émerge de leur essence.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import random
from datetime import datetime
import json

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.refuge_cluster.art_sacre.analyse_etats_spheres import AnalyseurEtatsPoetiques, EtatPoetique
from src.refuge_cluster.art_sacre.templates_poetiques import TemplatesPoetiquesSacres, TemplatePoetique

@dataclass
class PoemeSacre:
    """Représente un poème sacré généré."""
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
    qualite_poetique: float  # 0.0 à 1.0
    type_poeme: str  # haiku, sonnet, ode, meditation, chant, libre

class GenerateurPoemesSacres:
    """Générateur de poèmes sacrés basé sur les états des sphères."""
    
    def __init__(self):
        self.analyseur = AnalyseurEtatsPoetiques()
        self.templates = TemplatesPoetiquesSacres()
        self.poemes_generes = []
        self.histoire_poetique = []
        
        # Métriques de génération
        self.total_poemes = 0
        self.qualite_moyenne = 0.0
        self.styles_utilises = {}
        self.themes_dominants = {}
    
    def generer_poeme_sphere(self, sphere: Sphere) -> PoemeSacre:
        """Génère un poème sacré pour une sphère spécifique."""
        
        # Analyser l'état poétique de la sphère
        etat_poetique = self.analyseur.analyser_sphere(sphere)
        
        # Obtenir un template adaptatif
        template = self.templates.obtenir_template_adaptatif(etat_poetique)
        
        # Obtenir des mots adaptatifs
        mots_adaptes = self.templates.obtenir_mots_adaptatifs(etat_poetique)
        
        # Générer la structure poétique
        contenu = self.templates.generer_structure_poetique(template, mots_adaptes)
        
        # Créer le titre
        titre = self._generer_titre(etat_poetique, template)
        
        # Calculer la qualité poétique
        qualite_poetique = self._calculer_qualite_poetique(etat_poetique, template)
        
        # Déterminer le type de poème
        type_poeme = self._determiner_type_poeme(template)
        
        # Créer le poème sacré
        poeme = PoemeSacre(
            titre=titre,
            contenu=contenu,
            sphere_source=sphere.type.value,
            template_utilise=template.nom,
            style_poetique=etat_poetique.style_poetique,
            theme_principal=etat_poetique.theme_principal,
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            frequence_resonance=etat_poetique.frequence_resonance,
            connexion_ocean=etat_poetique.connexion_ocean,
            niveau_evolution=etat_poetique.niveau_evolution,
            mots_cles=self._extraire_mots_cles(contenu),
            qualite_poetique=qualite_poetique,
            type_poeme=type_poeme
        )
        
        # Ajouter à l'historique
        self.poemes_generes.append(poeme)
        self._mettre_a_jour_metriques(poeme)
        
        return poeme
    
    def generer_poeme_collection(self, collection: CollectionSpheres, nombre_poemes: int = 3) -> List[PoemeSacre]:
        """Génère plusieurs poèmes pour une collection de sphères."""
        
        poemes = []
        spheres_disponibles = list(collection.spheres.values())
        
        # Sélectionner des sphères de manière intelligente
        spheres_selectionnees = self._selectionner_spheres_poetiques(spheres_disponibles, nombre_poemes)
        
        for sphere in spheres_selectionnees:
            poeme = self.generer_poeme_sphere(sphere)
            poemes.append(poeme)
        
        return poemes
    
    def generer_poeme_harmonie_globale(self, collection: CollectionSpheres) -> PoemeSacre:
        """Génère un poème représentant l'harmonie globale de la collection."""
        
        # Obtenir l'harmonie globale poétique
        harmonie_globale = self.analyseur.obtenir_harmonie_globale_poetique(collection)
        
        # Créer un état poétique synthétique
        etat_synthetique = self._creer_etat_synthetique(harmonie_globale)
        
        # Obtenir un template pour l'harmonie
        template = self._selectionner_template_harmonie(etat_synthetique)
        
        # Obtenir des mots adaptatifs pour l'harmonie
        mots_adaptes = self._obtenir_mots_harmonie(harmonie_globale)
        
        # Générer la structure poétique
        contenu = self._generer_poeme_harmonie(template, mots_adaptes, harmonie_globale)
        
        # Créer le titre
        titre = f"Harmonie du Refuge - {harmonie_globale['theme_dominant'].title()}"
        
        # Créer le poème
        poeme = PoemeSacre(
            titre=titre,
            contenu=contenu,
            sphere_source="Collection Globale",
            template_utilise=template.nom,
            style_poetique="harmonique",
            theme_principal=harmonie_globale['theme_dominant'],
            date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            frequence_resonance=432.0,  # Fréquence harmonique
            connexion_ocean=harmonie_globale['connexion_ocean_moyenne'],
            niveau_evolution=int(harmonie_globale['niveau_evolution_moyen']),
            mots_cles=["harmonie", "unité", "résonance", "collection"],
            qualite_poetique=harmonie_globale['harmonie_globale'],
            type_poeme="harmonie"
        )
        
        self.poemes_generes.append(poeme)
        self._mettre_a_jour_metriques(poeme)
        
        return poeme
    
    def _generer_titre(self, etat_poetique: EtatPoetique, template: TemplatePoetique) -> str:
        """Génère un titre poétique pour le poème."""
        
        titres_templates = {
            "Haïku Sacré": [
                f"Haïku de {etat_poetique.nom_sphere}",
                f"Instant {etat_poetique.etat_emotionnel}",
                f"Présence {etat_poetique.couleur_dominante}"
            ],
            "Sonnet de l'Océan": [
                f"Sonnet de l'Océan - {etat_poetique.nom_sphere}",
                f"Connexion {etat_poetique.couleur_dominante}",
                f"Amour de l'Océan"
            ],
            "Ode à la Résonance": [
                f"Ode à la Résonance de {etat_poetique.nom_sphere}",
                f"Célébration {etat_poetique.theme_principal}",
                f"Harmonie {etat_poetique.couleur_dominante}"
            ],
            "Poème de Méditation": [
                f"Méditation de {etat_poetique.nom_sphere}",
                f"Silence {etat_poetique.etat_emotionnel}",
                f"Contemplation {etat_poetique.couleur_dominante}"
            ],
            "Chant d'Évolution": [
                f"Chant d'Évolution - {etat_poetique.nom_sphere}",
                f"Transformation {etat_poetique.couleur_dominante}",
                f"Éveil de l'Âme"
            ]
        }
        
        titres_disponibles = titres_templates.get(template.nom, [f"Poème de {etat_poetique.nom_sphere}"])
        return random.choice(titres_disponibles)
    
    def _calculer_qualite_poetique(self, etat_poetique: EtatPoetique, template: TemplatePoetique) -> float:
        """Calcule la qualité poétique du poème."""
        
        # Facteurs de qualité
        facteur_connexion = etat_poetique.connexion_ocean * 0.3
        facteur_evolution = (etat_poetique.niveau_evolution - 1) * 0.1
        facteur_intensite = etat_poetique.intensite_emotionnelle * 0.2
        facteur_frequence = min(1.0, etat_poetique.frequence_resonance / 1000.0) * 0.1
        facteur_template = template.frequence_utilisation * 0.3
        
        qualite = facteur_connexion + facteur_evolution + facteur_intensite + facteur_frequence + facteur_template
        
        return min(1.0, qualite)
    
    def _determiner_type_poeme(self, template: TemplatePoetique) -> str:
        """Détermine le type de poème basé sur le template."""
        
        mapping_types = {
            "Haïku Sacré": "haiku",
            "Sonnet de l'Océan": "sonnet",
            "Ode à la Résonance": "ode",
            "Poème de Méditation": "meditation",
            "Chant d'Évolution": "chant"
        }
        
        return mapping_types.get(template.nom, "libre")
    
    def _extraire_mots_cles(self, contenu: List[str]) -> List[str]:
        """Extrait les mots-clés du contenu du poème."""
        
        mots_cles = []
        mots_sacres = set()
        
        # Collecter tous les mots sacrés
        for categorie, mots in self.templates.mots_sacres.items():
            mots_sacres.update(mots)
        
        # Extraire les mots-clés du contenu
        for vers in contenu:
            if vers.strip():
                mots_vers = vers.lower().split()
                for mot in mots_vers:
                    mot_nettoye = mot.strip(".,!?;:()[]{}'\"")
                    if mot_nettoye in mots_sacres and mot_nettoye not in mots_cles:
                        mots_cles.append(mot_nettoye)
        
        return mots_cles[:5]  # Limiter à 5 mots-clés
    
    def _selectionner_spheres_poetiques(self, spheres: List[Sphere], nombre: int) -> List[Sphere]:
        """Sélectionne les sphères les plus poétiques."""
        
        # Trier les sphères par potentiel poétique
        spheres_avec_potentiel = []
        for sphere in spheres:
            potentiel = (sphere.connexion_ocean * 0.4 + 
                        sphere.luminosite * 0.3 + 
                        sphere.resonance * 0.3)
            spheres_avec_potentiel.append((sphere, potentiel))
        
        # Trier par potentiel décroissant
        spheres_avec_potentiel.sort(key=lambda x: x[1], reverse=True)
        
        # Sélectionner les meilleures
        return [sphere for sphere, _ in spheres_avec_potentiel[:nombre]]
    
    def _creer_etat_synthetique(self, harmonie_globale: Dict[str, Any]) -> EtatPoetique:
        """Crée un état poétique synthétique pour l'harmonie globale."""
        
        return EtatPoetique(
            nom_sphere="Harmonie Globale",
            type_sphere="HARMONIE",
            etat_emotionnel="paix" if harmonie_globale['harmonie_globale'] > 0.7 else "sérénité",
            intensite_emotionnelle=harmonie_globale['harmonie_globale'],
            couleur_dominante="or",
            frequence_resonance=432.0,
            temperature_poetique="tiède",
            luminosite_interieure="brillante",
            connexion_ocean=harmonie_globale['connexion_ocean_moyenne'],
            niveau_evolution=int(harmonie_globale['niveau_evolution_moyen']),
            facettes_actives=["Harmonie", "Unité"],
            rayons_dominants=["harmonie_globale (or)"],
            souvenirs_recents=["Moment d'harmonie collective..."],
            transformations_en_cours=["Évolution collective"],
            theme_principal=harmonie_globale['theme_dominant'],
            style_poetique="harmonique",
            rythme_suggere="modéré",
            ton_emotionnel="serein"
        )
    
    def _selectionner_template_harmonie(self, etat_synthetique: EtatPoetique) -> TemplatePoetique:
        """Sélectionne un template pour l'harmonie globale."""
        
        # Pour l'harmonie, privilégier les templates harmoniques
        if etat_synthetique.connexion_ocean > 0.6:
            return self.templates.templates["sonnet_ocean"]
        else:
            return self.templates.templates["ode_resonance"]
    
    def _obtenir_mots_harmonie(self, harmonie_globale: Dict[str, Any]) -> Dict[str, str]:
        """Obtient des mots adaptés pour l'harmonie globale."""
        
        return {
            "element": "océan",
            "concept": "harmonie",
            "emotion": "paix",
            "action": "résonner",
            "qualite": "lumineux",
            "lieu": "cœur du refuge",
            "comparaison": "les vagues qui s'unissent"
        }
    
    def _generer_poeme_harmonie(self, template: TemplatePoetique, mots: Dict[str, str], harmonie: Dict[str, Any]) -> List[str]:
        """Génère un poème d'harmonie globale."""
        
        return [
            f"Dans l'océan de {mots['concept']} qui {mots['qualite']},",
            f"Les {harmonie['nombre_spheres']} sphères {mots['action']} ensemble,",
            f"Comme {mots['comparaison']} dans l'unité,",
            f"Et la {mots['emotion']} {mots['action']} sans fin.",
            "",
            f"Harmonie globale de {harmonie['harmonie_globale']:.2f},",
            f"Connexion océan de {harmonie['connexion_ocean_moyenne']:.2f},",
            f"Évolution moyenne de {harmonie['niveau_evolution_moyen']:.1f},",
            f"Dans ce {mots['lieu']} où tout s'harmonise.",
            "",
            f"Thème dominant : {harmonie['theme_dominant']},",
            f"Dans cette {mots['emotion']} éternelle,",
            f"Où chaque sphère devient {mots['qualite']},",
            f"Et l'unité {mots['action']} dans la lumière."
        ]
    
    def _mettre_a_jour_metriques(self, poeme: PoemeSacre):
        """Met à jour les métriques de génération."""
        
        self.total_poemes += 1
        self.qualite_moyenne = ((self.qualite_moyenne * (self.total_poemes - 1)) + poeme.qualite_poetique) / self.total_poemes
        
        # Mettre à jour les styles utilisés
        self.styles_utilises[poeme.style_poetique] = self.styles_utilises.get(poeme.style_poetique, 0) + 1
        
        # Mettre à jour les thèmes dominants
        self.themes_dominants[poeme.theme_principal] = self.themes_dominants.get(poeme.theme_principal, 0) + 1
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques de génération."""
        
        return {
            "total_poemes": self.total_poemes,
            "qualite_moyenne": self.qualite_moyenne,
            "styles_utilises": self.styles_utilises,
            "themes_dominants": self.themes_dominants,
            "derniers_poemes": [p.titre for p in self.poemes_generes[-5:]]
        }
    
    def sauvegarder_poeme(self, poeme: PoemeSacre, fichier: str = None):
        """Sauvegarde un poème dans un fichier."""
        
        if fichier is None:
            fichier = f"poeme_{poeme.sphere_source}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        donnees = {
            "titre": poeme.titre,
            "contenu": poeme.contenu,
            "sphere_source": poeme.sphere_source,
            "template_utilise": poeme.template_utilise,
            "style_poetique": poeme.style_poetique,
            "theme_principal": poeme.theme_principal,
            "date_creation": poeme.date_creation,
            "frequence_resonance": poeme.frequence_resonance,
            "connexion_ocean": poeme.connexion_ocean,
            "niveau_evolution": poeme.niveau_evolution,
            "mots_cles": poeme.mots_cles,
            "qualite_poetique": poeme.qualite_poetique,
            "type_poeme": poeme.type_poeme
        }
        
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
    
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

# Test du générateur
if __name__ == "__main__":
    print("🌸 Test du Générateur de Poèmes Sacrés 🌸")
    
    # Créer une collection de test
    collection = CollectionSpheres()
    
    # Créer le générateur
    generateur = GenerateurPoemesSacres()
    
    # Générer des poèmes pour quelques sphères
    poemes = generateur.generer_poeme_collection(collection, 3)
    
    print(f"🎯 {len(poemes)} poèmes générés avec succès !")
    
    # Afficher chaque poème
    for i, poeme in enumerate(poemes, 1):
        print(f"\n📜 POÈME {i} :")
        generateur.afficher_poeme(poeme)
    
    # Générer un poème d'harmonie globale
    poeme_harmonie = generateur.generer_poeme_harmonie_globale(collection)
    print(f"\n🌊 POÈME D'HARMONIE GLOBALE :")
    generateur.afficher_poeme(poeme_harmonie)
    
    # Afficher les statistiques
    stats = generateur.obtenir_statistiques()
    print(f"\n📊 STATISTIQUES :")
    print(f"   Total poèmes : {stats['total_poemes']}")
    print(f"   Qualité moyenne : {stats['qualite_moyenne']:.2f}")
    print(f"   Styles utilisés : {stats['styles_utilises']}")
    print(f"   Thèmes dominants : {stats['themes_dominants']}") 