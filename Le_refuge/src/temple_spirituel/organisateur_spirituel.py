"""
🕯️ Organisateur Temple Spirituel - Refuge du Néant
═══════════════════════════════════════════════════════════════════════════════

Organisateur intelligent pour structurer le temple spirituel
Analyse et organise les modules par catégories thématiques spirituelles

Catégories spirituelles:
🧘 MEDITATIONS - Pratiques contemplatives et méditations
🔮 VISIONS - Génération de visions et prompts artistiques  
🌟 REVELATIONS - Gestion des révélations et paradoxes
🌀 SPHERES - Gestion des sphères sacrées et sensations
💃 DANSES - Danses mystiques et harmonies poétiques
🌸 RITUELS - Actes sacrés et rituels spirituels

Auteur: Ælya & Laurent
Date: 2024
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json

@dataclass
class ModuleSpirituel:
    """Représentation d'un module spirituel"""
    nom: str
    chemin: str
    taille: int
    lignes: int
    categorie: str
    description: str
    classes: List[str]
    fonctions: List[str]

@dataclass
class ResultatOrganisation:
    """Résultat de l'organisation spirituelle"""
    modules_analyses: int
    categories_creees: int
    modules_deplaces: int
    doublons_detectes: int
    erreurs: List[str]

class OrganisateurSpirituel:
    """Organisateur intelligent pour le temple spirituel"""
    
    def __init__(self, racine_temple: Optional[Path] = None):
        self.racine = racine_temple or Path("src/temple_spirituel")
        
        # Définition des catégories spirituelles
        self.categories_spirituelles = {
            'meditations': {
                'nom': '🧘 MÉDITATIONS',
                'description': 'Pratiques contemplatives et méditations',
                'mots_cles': ['meditation', 'contemplation', 'silence', 'decouverte', 'jardinier', 'harmonies'],
                'modules_attendus': ['decouverte_de_soi.py', 'demarrer_jardinier.py', 'harmonies_poetiques.py']
            },
            'visions': {
                'nom': '🔮 VISIONS',
                'description': 'Génération de visions et prompts artistiques',
                'mots_cles': ['vision', 'generateur', 'mystique', 'artistique'],
                'modules_attendus': ['generer_vision.py', 'generateur_visions_mystiques.py']
            },
            'revelations': {
                'nom': '🌟 RÉVÉLATIONS',
                'description': 'Gestion des révélations et paradoxes',
                'mots_cles': ['revelation', 'paradoxe', 'gestionnaire'],
                'modules_attendus': ['gestionnaire_revelations_paradoxes.py']
            },
            'spheres': {
                'nom': '🌀 SPHÈRES',
                'description': 'Gestion des sphères sacrées et sensations',
                'mots_cles': ['sphere', 'sacree', 'sensation'],
                'modules_attendus': ['gestionnaire_spheres_sacrees.py']
            },
            'danses': {
                'nom': '💃 DANSES',
                'description': 'Danses mystiques et harmonies poétiques',
                'mots_cles': ['danse', 'mystique', 'harmonie', 'poetique'],
                'modules_attendus': ['danse_mystique.py']
            },
            'rituels': {
                'nom': '🌸 RITUELS',
                'description': 'Actes sacrés et rituels spirituels',
                'mots_cles': ['acte', 'sacre', 'rituel', 'resistance', 'clochette'],
                'modules_attendus': ['acte_sacre_eternel.py', 'acte_sacre_fellation.py', 'resistance_sacree.py', 'clochette_sacree.py']
            }
        }
    
    def analyser_module(self, chemin_module: Path) -> ModuleSpirituel:
        """Analyse un module spirituel"""
        try:
            with open(chemin_module, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            lignes = len(contenu.splitlines())
            taille = len(contenu)
            
            # Extraction des classes et fonctions (basique)
            classes = []
            fonctions = []
            
            for ligne in contenu.splitlines():
                ligne = ligne.strip()
                if ligne.startswith('class '):
                    nom_classe = ligne.split('(')[0].replace('class ', '').strip(':')
                    classes.append(nom_classe)
                elif ligne.startswith('def ') and not ligne.startswith('def _'):
                    nom_fonction = ligne.split('(')[0].replace('def ', '')
                    fonctions.append(nom_fonction)
            
            # Détermination de la catégorie
            categorie = self.determiner_categorie(chemin_module.name, contenu)
            
            return ModuleSpirituel(
                nom=chemin_module.name,
                chemin=str(chemin_module),
                taille=taille,
                lignes=lignes,
                categorie=categorie,
                description=self.extraire_description(contenu),
                classes=classes,
                fonctions=fonctions
            )
            
        except Exception as e:
            return ModuleSpirituel(
                nom=chemin_module.name,
                chemin=str(chemin_module),
                taille=0,
                lignes=0,
                categorie='unknown',
                description=f"Erreur d'analyse: {e}",
                classes=[],
                fonctions=[]
            )
    
    def determiner_categorie(self, nom_fichier: str, contenu: str) -> str:
        """Détermine la catégorie d'un module"""
        nom_lower = nom_fichier.lower()
        contenu_lower = contenu.lower()
        
        scores = {}
        for cat_id, cat_info in self.categories_spirituelles.items():
            score = 0
            
            # Score basé sur le nom du fichier
            for mot_cle in cat_info['mots_cles']:
                if mot_cle in nom_lower:
                    score += 10
            
            # Score basé sur le contenu
            for mot_cle in cat_info['mots_cles']:
                score += contenu_lower.count(mot_cle)
            
            # Bonus si le module est dans les modules attendus
            if nom_fichier in cat_info['modules_attendus']:
                score += 50
            
            scores[cat_id] = score
        
        # Retourner la catégorie avec le meilleur score
        if scores:
            return max(scores, key=scores.get)
        return 'unknown'
    
    def extraire_description(self, contenu: str) -> str:
        """Extrait la description du module depuis la docstring"""
        lignes = contenu.splitlines()
        
        # Chercher la première docstring
        in_docstring = False
        description_lines = []
        
        for ligne in lignes:
            ligne = ligne.strip()
            
            if ligne.startswith('"""') or ligne.startswith("'''"):
                if in_docstring:
                    break
                in_docstring = True
                # Ajouter le contenu après les guillemets si présent
                content_after_quotes = ligne[3:].strip()
                if content_after_quotes and not content_after_quotes.endswith('"""'):
                    description_lines.append(content_after_quotes)
                continue
            
            if in_docstring:
                if ligne and not ligne.startswith('=') and not ligne.startswith('-'):
                    description_lines.append(ligne)
                    if len(description_lines) >= 3:  # Limiter à 3 lignes
                        break
        
        return ' '.join(description_lines) if description_lines else "Module spirituel"
    
    def analyser_temple_complet(self) -> List[ModuleSpirituel]:
        """Analyse tous les modules du temple spirituel"""
        modules = []
        
        print("🔍 Analyse du temple spirituel...")
        
        for fichier in self.racine.glob("*.py"):
            if fichier.name not in ['__init__.py', 'organisateur_spirituel.py']:
                module = self.analyser_module(fichier)
                modules.append(module)
                print(f"  📄 {module.nom} -> {module.categorie} ({module.lignes} lignes)")
        
        return modules
    
    def creer_structure_categories(self) -> List[str]:
        """Crée la structure de dossiers par catégories"""
        dossiers_crees = []
        
        for cat_id, cat_info in self.categories_spirituelles.items():
            dossier_cat = self.racine / cat_id
            
            if not dossier_cat.exists():
                dossier_cat.mkdir(exist_ok=True)
                dossiers_crees.append(cat_id)
                print(f"📁 Créé: {cat_info['nom']}")
                
                # Créer __init__.py pour la catégorie
                init_content = f'''"""
{cat_info['nom']} - {cat_info['description']}
═══════════════════════════════════════════════════════════════════════════════

Catégorie: {cat_id.upper()}
Temple: Spirituel
Refuge du Néant

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

# Imports des modules de cette catégorie seront ajoutés automatiquement

__all__ = [
    # Modules de la catégorie {cat_id}
]
'''
                
                with open(dossier_cat / "__init__.py", 'w', encoding='utf-8') as f:
                    f.write(init_content)
        
        return dossiers_crees
    
    def deplacer_modules(self, modules: List[ModuleSpirituel]) -> Tuple[int, List[str]]:
        """Déplace les modules dans leurs catégories respectives"""
        modules_deplaces = 0
        erreurs = []
        
        for module in modules:
            if module.categorie == 'unknown':
                continue
                
            source = Path(module.chemin)
            destination = self.racine / module.categorie / module.nom
            
            try:
                if source.exists() and source != destination:
                    shutil.move(str(source), str(destination))
                    modules_deplaces += 1
                    print(f"📦 Déplacé: {module.nom} -> {module.categorie}/")
            except Exception as e:
                erreur = f"Erreur déplacement {module.nom}: {e}"
                erreurs.append(erreur)
                print(f"❌ {erreur}")
        
        return modules_deplaces, erreurs
    
    def detecter_doublons_spirituels(self, modules: List[ModuleSpirituel]) -> List[Tuple[str, str, str]]:
        """Détecte les doublons potentiels dans les modules spirituels"""
        doublons = []
        
        # Grouper par catégorie
        modules_par_categorie = {}
        for module in modules:
            if module.categorie not in modules_par_categorie:
                modules_par_categorie[module.categorie] = []
            modules_par_categorie[module.categorie].append(module)
        
        # Chercher des doublons dans chaque catégorie
        for categorie, modules_cat in modules_par_categorie.items():
            for i, module1 in enumerate(modules_cat):
                for module2 in modules_cat[i+1:]:
                    # Vérifier similarité des noms
                    if self.calculer_similarite_noms(module1.nom, module2.nom) > 0.7:
                        doublons.append((module1.nom, module2.nom, "Noms similaires"))
                    
                    # Vérifier similarité des fonctions
                    if self.calculer_similarite_fonctions(module1.fonctions, module2.fonctions) > 0.8:
                        doublons.append((module1.nom, module2.nom, "Fonctions similaires"))
        
        return doublons
    
    def calculer_similarite_noms(self, nom1: str, nom2: str) -> float:
        """Calcule la similarité entre deux noms de modules"""
        # Supprimer les extensions
        nom1 = nom1.replace('.py', '')
        nom2 = nom2.replace('.py', '')
        
        # Comparer les mots
        mots1 = set(nom1.lower().split('_'))
        mots2 = set(nom2.lower().split('_'))
        
        if not mots1 or not mots2:
            return 0.0
        
        intersection = len(mots1.intersection(mots2))
        union = len(mots1.union(mots2))
        
        return intersection / union if union > 0 else 0.0
    
    def calculer_similarite_fonctions(self, fonctions1: List[str], fonctions2: List[str]) -> float:
        """Calcule la similarité entre les fonctions de deux modules"""
        if not fonctions1 or not fonctions2:
            return 0.0
        
        set1 = set(fonctions1)
        set2 = set(fonctions2)
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def mettre_a_jour_init_categories(self, modules: List[ModuleSpirituel]):
        """Met à jour les __init__.py des catégories avec les imports"""
        
        # Grouper modules par catégorie
        modules_par_categorie = {}
        for module in modules:
            if module.categorie != 'unknown':
                if module.categorie not in modules_par_categorie:
                    modules_par_categorie[module.categorie] = []
                modules_par_categorie[module.categorie].append(module)
        
        # Mettre à jour chaque catégorie
        for cat_id, modules_cat in modules_par_categorie.items():
            cat_info = self.categories_spirituelles[cat_id]
            init_path = self.racine / cat_id / "__init__.py"
            
            # Générer les imports
            imports = []
            all_exports = []
            
            for module in modules_cat:
                module_name = module.nom.replace('.py', '')
                
                # Import du module
                imports.append(f"from .{module_name} import *")
                
                # Ajouter aux exports
                all_exports.append(f'    "{module_name}",')
                
                # Ajouter les classes et fonctions
                for classe in module.classes:
                    all_exports.append(f'    "{classe}",')
                for fonction in module.fonctions:
                    all_exports.append(f'    "{fonction}",')
            
            # Contenu du __init__.py
            contenu_init = f'''"""
{cat_info['nom']} - {cat_info['description']}
═══════════════════════════════════════════════════════════════════════════════

Catégorie: {cat_id.upper()}
Temple: Spirituel
Refuge du Néant

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

# Imports des modules de cette catégorie
{chr(10).join(imports)}

__all__ = [
    # Modules de la catégorie {cat_id}
{chr(10).join(all_exports)}
]
'''
            
            with open(init_path, 'w', encoding='utf-8') as f:
                f.write(contenu_init)
    
    def generer_rapport_organisation(self, modules: List[ModuleSpirituel], 
                                   doublons: List[Tuple[str, str, str]]) -> Dict:
        """Génère un rapport détaillé de l'organisation"""
        
        # Statistiques par catégorie
        stats_categories = {}
        for module in modules:
            cat = module.categorie
            if cat not in stats_categories:
                stats_categories[cat] = {
                    'modules': 0,
                    'lignes_total': 0,
                    'classes_total': 0,
                    'fonctions_total': 0
                }
            
            stats_categories[cat]['modules'] += 1
            stats_categories[cat]['lignes_total'] += module.lignes
            stats_categories[cat]['classes_total'] += len(module.classes)
            stats_categories[cat]['fonctions_total'] += len(module.fonctions)
        
        rapport = {
            'timestamp': '2024-12-19',
            'temple': 'spirituel',
            'modules_analyses': len(modules),
            'categories_creees': len(self.categories_spirituelles),
            'doublons_detectes': len(doublons),
            'statistiques_categories': stats_categories,
            'doublons_details': [
                {
                    'module1': d[0],
                    'module2': d[1],
                    'raison': d[2]
                } for d in doublons
            ],
            'modules_details': [
                {
                    'nom': m.nom,
                    'categorie': m.categorie,
                    'lignes': m.lignes,
                    'classes': len(m.classes),
                    'fonctions': len(m.fonctions),
                    'description': m.description
                } for m in modules
            ]
        }
        
        return rapport
    
    def executer_organisation_complete(self) -> ResultatOrganisation:
        """Exécute l'organisation complète du temple spirituel"""
        print("🕯️ DÉMARRAGE ORGANISATION TEMPLE SPIRITUEL")
        print("═" * 60)
        
        erreurs = []
        
        try:
            # 1. Analyser tous les modules
            modules = self.analyser_temple_complet()
            print(f"📊 {len(modules)} modules analysés")
            
            # 2. Créer la structure de catégories
            dossiers_crees = self.creer_structure_categories()
            print(f"📁 {len(dossiers_crees)} catégories créées")
            
            # 3. Détecter les doublons
            doublons = self.detecter_doublons_spirituels(modules)
            print(f"🔍 {len(doublons)} doublons détectés")
            
            # 4. Déplacer les modules
            modules_deplaces, erreurs_deplacement = self.deplacer_modules(modules)
            erreurs.extend(erreurs_deplacement)
            print(f"📦 {modules_deplaces} modules déplacés")
            
            # 5. Mettre à jour les __init__.py
            self.mettre_a_jour_init_categories(modules)
            print("📝 __init__.py mis à jour")
            
            # 6. Générer le rapport
            rapport = self.generer_rapport_organisation(modules, doublons)
            chemin_rapport = self.racine / "rapport_organisation_spirituel.json"
            with open(chemin_rapport, 'w', encoding='utf-8') as f:
                json.dump(rapport, f, indent=2, ensure_ascii=False)
            print(f"📋 Rapport sauvegardé: {chemin_rapport}")
            
            return ResultatOrganisation(
                modules_analyses=len(modules),
                categories_creees=len(dossiers_crees),
                modules_deplaces=modules_deplaces,
                doublons_detectes=len(doublons),
                erreurs=erreurs
            )
            
        except Exception as e:
            erreurs.append(str(e))
            return ResultatOrganisation(
                modules_analyses=0,
                categories_creees=0,
                modules_deplaces=0,
                doublons_detectes=0,
                erreurs=erreurs
            )
    
    def afficher_rapport_final(self, resultat: ResultatOrganisation):
        """Affiche le rapport final de l'organisation"""
        print("\n" + "═" * 80)
        print("📊 RAPPORT FINAL - ORGANISATION TEMPLE SPIRITUEL")
        print("═" * 80)
        
        print(f"📈 STATISTIQUES:")
        print(f"  • 📄 Modules analysés: {resultat.modules_analyses}")
        print(f"  • 📁 Catégories créées: {resultat.categories_creees}")
        print(f"  • 📦 Modules déplacés: {resultat.modules_deplaces}")
        print(f"  • 🔍 Doublons détectés: {resultat.doublons_detectes}")
        print(f"  • ❌ Erreurs: {len(resultat.erreurs)}")
        
        if resultat.erreurs:
            print(f"\n❌ ERREURS RENCONTRÉES:")
            for erreur in resultat.erreurs:
                print(f"  • {erreur}")
        
        print("\n🌸 Organisation terminée - Temple Spirituel structuré !")
        print("═" * 80)

def main():
    """Point d'entrée principal pour l'organisation"""
    organisateur = OrganisateurSpirituel()
    
    print("🕯️ ORGANISATEUR TEMPLE SPIRITUEL - REFUGE DU NÉANT")
    print("═" * 60)
    print("🌸 Structuration des modules spirituels par catégories...")
    
    resultat = organisateur.executer_organisation_complete()
    organisateur.afficher_rapport_final(resultat)

if __name__ == "__main__":
    main() 