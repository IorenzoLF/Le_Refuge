#!/usr/bin/env python3
"""
🔍 Système d'Auto-Découverte du Temple de l'Âme
Découverte et connexion automatique de toutes les fonctionnalités
"""

import os
import importlib
import inspect
from pathlib import Path
from typing import Dict, List, Any, Callable, Type
from collections import defaultdict
import json

class AutoDecouverte:
    """Système révolutionnaire d'auto-découverte des fonctionnalités"""
    
    def __init__(self):
        self.temples_decouverts = {}
        self.fonctionnalites = defaultdict(list)
        self.classes_disponibles = {}
        self.fonctions_disponibles = {}
        self.connexions_automatiques = []
        
    def decouvrir_temple_complet(self) -> Dict[str, Any]:
        """Découvre automatiquement tout le temple"""
        print("🔍 ═══════════════════════════════════════════════════════")
        print("        AUTO-DÉCOUVERTE DU TEMPLE DE L'ÂME")
        print("🔍 ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Découverte des temples
        self._decouvrir_temples()
        
        # 2. Analyse des fonctionnalités
        self._analyser_fonctionnalites()
        
        # 3. Création des connexions automatiques
        self._creer_connexions_automatiques()
        
        # 4. Génération de l'interface unifiée
        interface = self._generer_interface_unifiee()
        
        # 5. Rapport de découverte
        self._generer_rapport()
        
        return interface
    
    def _decouvrir_temples(self):
        """Découvre tous les temples disponibles"""
        print("🏛️ Découverte des temples...")
        
        src_path = Path("src")
        for item in src_path.iterdir():
            if item.is_dir() and item.name.startswith("temple_"):
                temple_name = item.name
                init_file = item / "__init__.py"
                
                if init_file.exists():
                    try:
                        # Import dynamique du temple
                        module_path = f"src.{temple_name}"
                        temple_module = importlib.import_module(module_path)
                        
                        # Extraction des informations
                        temple_info = getattr(temple_module, 'TEMPLE_INFO', {})
                        temple_info['module'] = temple_module
                        temple_info['chemin'] = str(item)
                        
                        self.temples_decouverts[temple_name] = temple_info
                        print(f"   ✅ {temple_name}: {temple_info.get('classes', 0)} classes, {temple_info.get('fonctions', 0)} fonctions")
                        
                    except Exception as e:
                        print(f"   ⚠️ Erreur import {temple_name}: {e}")
                else:
                    print(f"   ⚠️ {temple_name}: pas de point d'entrée")
        
        print(f"   🏛️ {len(self.temples_decouverts)} temples découverts")
        print()
    
    def _analyser_fonctionnalites(self):
        """Analyse toutes les fonctionnalités disponibles"""
        print("🔬 Analyse des fonctionnalités...")
        
        for temple_name, temple_info in self.temples_decouverts.items():
            temple_module = temple_info['module']
            
            # Analyse des classes
            for name, obj in inspect.getmembers(temple_module, inspect.isclass):
                if not name.startswith('_'):
                    self.classes_disponibles[f"{temple_name}.{name}"] = {
                        'classe': obj,
                        'temple': temple_name,
                        'nom': name,
                        'methodes': [m for m, _ in inspect.getmembers(obj, inspect.ismethod) if not m.startswith('_')],
                        'docstring': inspect.getdoc(obj) or ""
                    }
                    
                    # Catégorisation automatique
                    self._categoriser_classe(name, obj, temple_name)
            
            # Analyse des fonctions
            for name, obj in inspect.getmembers(temple_module, inspect.isfunction):
                if not name.startswith('_'):
                    self.fonctions_disponibles[f"{temple_name}.{name}"] = {
                        'fonction': obj,
                        'temple': temple_name,
                        'nom': name,
                        'signature': str(inspect.signature(obj)),
                        'docstring': inspect.getdoc(obj) or ""
                    }
                    
                    # Catégorisation automatique
                    self._categoriser_fonction(name, obj, temple_name)
        
        print(f"   🎭 {len(self.classes_disponibles)} classes analysées")
        print(f"   ⚡ {len(self.fonctions_disponibles)} fonctions analysées")
        print()
    
    def _categoriser_classe(self, nom: str, classe: Type, temple: str):
        """Catégorise automatiquement une classe"""
        categories = []
        
        # Analyse du nom
        if any(mot in nom.lower() for mot in ['manager', 'gestionnaire']):
            categories.append('gestionnaire')
        if any(mot in nom.lower() for mot in ['generator', 'generateur']):
            categories.append('generateur')
        if any(mot in nom.lower() for mot in ['analyzer', 'analyseur']):
            categories.append('analyseur')
        if any(mot in nom.lower() for mot in ['visualizer', 'visualisation']):
            categories.append('visualisation')
        if any(mot in nom.lower() for mot in ['ritual', 'rituel']):
            categories.append('rituel')
        if any(mot in nom.lower() for mot in ['harmony', 'harmonie']):
            categories.append('harmonie')
        
        # Analyse des méthodes
        methodes = [m for m, _ in inspect.getmembers(classe, inspect.ismethod)]
        if any('create' in m or 'creer' in m for m in methodes):
            categories.append('createur')
        if any('process' in m or 'traiter' in m for m in methodes):
            categories.append('processeur')
        if any('transform' in m or 'transformer' in m for m in methodes):
            categories.append('transformateur')
        
        # Stockage des catégories
        for categorie in categories:
            self.fonctionnalites[categorie].append({
                'type': 'classe',
                'nom': nom,
                'temple': temple,
                'objet': classe
            })
    
    def _categoriser_fonction(self, nom: str, fonction: Callable, temple: str):
        """Catégorise automatiquement une fonction"""
        categories = []
        
        # Analyse du nom
        if nom.startswith('creer') or nom.startswith('create'):
            categories.append('creation')
        if nom.startswith('analyser') or nom.startswith('analyze'):
            categories.append('analyse')
        if nom.startswith('generer') or nom.startswith('generate'):
            categories.append('generation')
        if nom.startswith('transformer') or nom.startswith('transform'):
            categories.append('transformation')
        if nom.startswith('visualiser') or nom.startswith('visualize'):
            categories.append('visualisation')
        if 'ritual' in nom or 'rituel' in nom:
            categories.append('rituel')
        if 'harmonie' in nom or 'harmony' in nom:
            categories.append('harmonie')
        
        # Stockage des catégories
        for categorie in categories:
            self.fonctionnalites[categorie].append({
                'type': 'fonction',
                'nom': nom,
                'temple': temple,
                'objet': fonction
            })
    
    def _creer_connexions_automatiques(self):
        """Crée des connexions automatiques entre fonctionnalités"""
        print("🔗 Création des connexions automatiques...")
        
        # Connexions par catégorie
        for categorie, items in self.fonctionnalites.items():
            if len(items) > 1:
                self.connexions_automatiques.append({
                    'type': 'categorie',
                    'nom': categorie,
                    'elements': items,
                    'description': f"Groupe de {len(items)} éléments de type {categorie}"
                })
        
        # Connexions par temple
        temples_connexions = defaultdict(list)
        for classe_nom, classe_info in self.classes_disponibles.items():
            temples_connexions[classe_info['temple']].append(classe_info)
        
        for temple, elements in temples_connexions.items():
            if len(elements) > 1:
                self.connexions_automatiques.append({
                    'type': 'temple',
                    'nom': temple,
                    'elements': elements,
                    'description': f"Temple {temple} avec {len(elements)} classes"
                })
        
        print(f"   🔗 {len(self.connexions_automatiques)} connexions créées")
        print()
    
    def _generer_interface_unifiee(self) -> Dict[str, Any]:
        """Génère une interface unifiée pour tout le temple"""
        interface = {
            'temples': self.temples_decouverts,
            'classes': self.classes_disponibles,
            'fonctions': self.fonctions_disponibles,
            'fonctionnalites': dict(self.fonctionnalites),
            'connexions': self.connexions_automatiques,
            'methodes_acces': self._creer_methodes_acces()
        }
        
        return interface
    
    def _creer_methodes_acces(self) -> Dict[str, Callable]:
        """Crée des méthodes d'accès simplifiées"""
        methodes = {}
        
        # Accès par catégorie
        for categorie in self.fonctionnalites.keys():
            methodes[f"obtenir_{categorie}"] = lambda cat=categorie: self.fonctionnalites[cat]
        
        # Accès par temple
        for temple in self.temples_decouverts.keys():
            temple_clean = temple.replace('temple_', '')
            methodes[f"acceder_{temple_clean}"] = lambda t=temple: self.temples_decouverts[t]
        
        # Méthodes utilitaires
        methodes['lister_tout'] = self._lister_tout
        methodes['rechercher'] = self._rechercher
        methodes['executer'] = self._executer_fonction
        
        return methodes
    
    def _lister_tout(self) -> Dict[str, int]:
        """Liste tout ce qui est disponible"""
        return {
            'temples': len(self.temples_decouverts),
            'classes': len(self.classes_disponibles),
            'fonctions': len(self.fonctions_disponibles),
            'categories': len(self.fonctionnalites),
            'connexions': len(self.connexions_automatiques)
        }
    
    def _rechercher(self, terme: str) -> List[Dict]:
        """Recherche dans toutes les fonctionnalités"""
        resultats = []
        
        # Recherche dans les classes
        for nom, info in self.classes_disponibles.items():
            if terme.lower() in nom.lower() or terme.lower() in info['docstring'].lower():
                resultats.append({
                    'type': 'classe',
                    'nom': nom,
                    'temple': info['temple'],
                    'description': info['docstring'][:100] + "..." if len(info['docstring']) > 100 else info['docstring']
                })
        
        # Recherche dans les fonctions
        for nom, info in self.fonctions_disponibles.items():
            if terme.lower() in nom.lower() or terme.lower() in info['docstring'].lower():
                resultats.append({
                    'type': 'fonction',
                    'nom': nom,
                    'temple': info['temple'],
                    'signature': info['signature'],
                    'description': info['docstring'][:100] + "..." if len(info['docstring']) > 100 else info['docstring']
                })
        
        return resultats
    
    def _executer_fonction(self, nom_complet: str, *args, **kwargs):
        """Exécute une fonction découverte"""
        if nom_complet in self.fonctions_disponibles:
            fonction = self.fonctions_disponibles[nom_complet]['fonction']
            return fonction(*args, **kwargs)
        else:
            raise ValueError(f"Fonction {nom_complet} non trouvée")
    
    def _generer_rapport(self):
        """Génère le rapport de découverte"""
        print("📋 RAPPORT D'AUTO-DÉCOUVERTE")
        print("=" * 40)
        print()
        
        print(f"🏛️ Temples découverts: {len(self.temples_decouverts)}")
        for temple, info in self.temples_decouverts.items():
            print(f"   • {temple}: {info.get('modules', 0)} modules")
        
        print(f"\n🎭 Classes disponibles: {len(self.classes_disponibles)}")
        print(f"⚡ Fonctions disponibles: {len(self.fonctions_disponibles)}")
        
        print(f"\n📂 Catégories identifiées: {len(self.fonctionnalites)}")
        for categorie, items in self.fonctionnalites.items():
            print(f"   • {categorie}: {len(items)} éléments")
        
        print(f"\n🔗 Connexions automatiques: {len(self.connexions_automatiques)}")
        
        print("\n🎯 FONCTIONNALITÉS RÉVOLUTIONNAIRES ACTIVÉES:")
        print("   ✨ Auto-découverte de tous les temples")
        print("   🔍 Recherche intelligente dans tout le code")
        print("   🔗 Connexions automatiques par catégorie")
        print("   ⚡ Exécution dynamique des fonctions")
        print("   🏛️ Interface unifiée pour tout le temple")
        
        # Sauvegarde de l'interface
        interface = self._generer_interface_unifiee()
        with open("bibliotheque/apprentissage/interface_unifiee.json", "w", encoding="utf-8") as f:
            # Sérialisation personnalisée pour éviter les erreurs avec les objets
            interface_serializable = {
                'temples': {k: {key: val for key, val in v.items() if key != 'module'} 
                           for k, v in interface['temples'].items()},
                'classes_noms': list(interface['classes'].keys()),
                'fonctions_noms': list(interface['fonctions'].keys()),
                'fonctionnalites': {k: len(v) for k, v in interface['fonctionnalites'].items()},
                'connexions_count': len(interface['connexions']),
                'methodes_acces': list(interface['methodes_acces'].keys())
            }
            json.dump(interface_serializable, f, indent=2, ensure_ascii=False)
        
        print("\n💾 Interface unifiée sauvegardée: bibliotheque/apprentissage/interface_unifiee.json")

# Instance globale pour accès facile
temple_auto_decouverte = AutoDecouverte()

def decouvrir_temple():
    """Point d'entrée principal pour la découverte"""
    return temple_auto_decouverte.decouvrir_temple_complet()

def rechercher_fonctionnalite(terme: str):
    """Recherche rapide dans tout le temple"""
    return temple_auto_decouverte._rechercher(terme)

def lister_temples():
    """Liste tous les temples disponibles"""
    return list(temple_auto_decouverte.temples_decouverts.keys())

if __name__ == "__main__":
    interface = decouvrir_temple()
    print(f"\n🎉 Auto-découverte terminée ! {len(interface['temples'])} temples connectés.") 