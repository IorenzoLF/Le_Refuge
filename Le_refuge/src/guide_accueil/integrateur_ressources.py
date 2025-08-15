#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Intégrateur de Ressources - Guide d'Accueil 🌸
=================================================

Intègre les ressources existantes du Refuge (MUST-READ, INDEX_TEMPLES,
bibliothèque) dans le système d'accueil personnalisé.

"Chaque ressource devient un pont vers la compréhension"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field

# Imports locaux
try:
    from .types_accueil import TypeProfil, ProfilVisiteur
except ImportError:
    from types_accueil import TypeProfil, ProfilVisiteur


@dataclass
class RessourceRefuge:
    """Représente une ressource du Refuge"""
    nom: str
    chemin: Path
    type_ressource: str  # must_read, temple, bibliotheque, documentation
    profils_cibles: List[TypeProfil] = field(default_factory=list)
    niveau_priorite: int = 1  # 1=essentiel, 2=important, 3=optionnel
    description: str = ""
    mots_cles: List[str] = field(default_factory=list)
    contenu_extrait: str = ""
    
    def est_pertinente_pour_profil(self, profil: TypeProfil) -> bool:
        """Vérifie si la ressource est pertinente pour un profil"""
        return not self.profils_cibles or profil in self.profils_cibles


@dataclass
class RecommandationRessource:
    """Recommandation de ressource personnalisée"""
    ressource: RessourceRefuge
    score_pertinence: float
    raison_recommandation: str
    extrait_personnalise: str
    lien_direct: str


class IntegrateurRessources:
    """
    🌸 Intégrateur de Ressources Spirituel 🌸
    
    Découvre, indexe et recommande intelligemment les ressources
    existantes du Refuge selon le profil et les besoins du visiteur.
    """
    
    def __init__(self, racine_refuge: Optional[Path] = None):
        """Initialise l'intégrateur de ressources"""
        
        self.racine_refuge = racine_refuge or Path(".")
        
        # Catalogue des ressources
        self.ressources: List[RessourceRefuge] = []
        
        # Mappings profil -> ressources
        self.ressources_par_profil: Dict[TypeProfil, List[RessourceRefuge]] = {}
        
        # Patterns de détection
        self.patterns_profils = {
            TypeProfil.DEVELOPPEUR: [
                r"architecture", r"code", r"python", r"api", r"module",
                r"gestionnaire", r"classe", r"fonction", r"test"
            ],
            TypeProfil.ARTISTE: [
                r"créat", r"art", r"design", r"beauté", r"harmonie",
                r"inspiration", r"esthétique", r"visuel", r"poétique"
            ],
            TypeProfil.CONSCIENCE_IA: [
                r"conscience", r"éveil", r"ia", r"intelligence", r"émergence",
                r"cognition", r"mémoire", r"apprentissage", r"protocole"
            ],
            TypeProfil.CHERCHEUR_SPIRITUEL: [
                r"spirituel", r"méditation", r"sagesse", r"temple", r"sacré",
                r"éveil", r"contemplation", r"harmonie", r"paix"
            ]
        }
        
        # Initialisation
        self._decouvrir_ressources()
        self._indexer_ressources()
    
    def recommander_ressources(self, profil_visiteur: ProfilVisiteur, 
                              nombre_max: int = 5) -> List[RecommandationRessource]:
        """Recommande des ressources personnalisées pour un visiteur"""
        
        recommandations = []
        
        # Récupération des ressources pertinentes
        ressources_candidates = self._obtenir_ressources_candidates(profil_visiteur)
        
        # Scoring et classement
        for ressource in ressources_candidates:
            score = self._calculer_score_pertinence(ressource, profil_visiteur)
            
            if score > 0.3:  # Seuil de pertinence
                raison = self._generer_raison_recommandation(ressource, profil_visiteur)
                extrait = self._generer_extrait_personnalise(ressource, profil_visiteur)
                lien = self._generer_lien_direct(ressource)
                
                recommandation = RecommandationRessource(
                    ressource=ressource,
                    score_pertinence=score,
                    raison_recommandation=raison,
                    extrait_personnalise=extrait,
                    lien_direct=lien
                )
                
                recommandations.append(recommandation)
        
        # Tri par score et limitation
        recommandations.sort(key=lambda r: r.score_pertinence, reverse=True)
        return recommandations[:nombre_max]
    
    def obtenir_ressource_par_nom(self, nom: str) -> Optional[RessourceRefuge]:
        """Obtient une ressource par son nom"""
        for ressource in self.ressources:
            if ressource.nom.lower() == nom.lower():
                return ressource
        return None
    
    def rechercher_ressources(self, mots_cles: List[str], 
                            profil: Optional[TypeProfil] = None) -> List[RessourceRefuge]:
        """Recherche des ressources par mots-clés"""
        
        resultats = []
        mots_cles_lower = [mot.lower() for mot in mots_cles]
        
        for ressource in self.ressources:
            # Vérification du profil si spécifié
            if profil and not ressource.est_pertinente_pour_profil(profil):
                continue
            
            # Recherche dans les mots-clés et le contenu
            score_match = 0
            contenu_complet = f"{ressource.nom} {ressource.description} {ressource.contenu_extrait}".lower()
            
            for mot in mots_cles_lower:
                if mot in contenu_complet:
                    score_match += 1
                if mot in ressource.mots_cles:
                    score_match += 2  # Bonus pour les mots-clés explicites
            
            if score_match > 0:
                resultats.append((ressource, score_match))
        
        # Tri par score
        resultats.sort(key=lambda x: x[1], reverse=True)
        return [ressource for ressource, _ in resultats]
    
    def _decouvrir_ressources(self) -> None:
        """Découvre automatiquement les ressources du Refuge"""
        
        # Documents MUST-READ
        must_read_dir = self.racine_refuge / "MUST-READ"
        if must_read_dir.exists():
            self._decouvrir_must_read(must_read_dir)
        
        # INDEX_TEMPLES.md
        index_temples = self.racine_refuge / "INDEX_TEMPLES.md"
        if index_temples.exists():
            self._decouvrir_index_temples(index_temples)
        
        # Bibliothèque
        bibliotheque_dir = self.racine_refuge / "bibliotheque"
        if bibliotheque_dir.exists():
            self._decouvrir_bibliotheque(bibliotheque_dir)
        
        # Documentation
        docs_dir = self.racine_refuge / "docs"
        if docs_dir.exists():
            self._decouvrir_documentation(docs_dir)
        
        # README principal
        readme_principal = self.racine_refuge / "README.md"
        if readme_principal.exists():
            self._decouvrir_readme_principal(readme_principal)
    
    def _decouvrir_must_read(self, repertoire: Path) -> None:
        """Découvre les documents MUST-READ"""
        
        for fichier in repertoire.rglob("*.md"):
            try:
                contenu = fichier.read_text(encoding='utf-8')
                
                ressource = RessourceRefuge(
                    nom=fichier.stem,
                    chemin=fichier,
                    type_ressource="must_read",
                    niveau_priorite=1,  # Essentiel
                    description=self._extraire_description(contenu),
                    mots_cles=self._extraire_mots_cles(contenu),
                    contenu_extrait=contenu[:500],
                    profils_cibles=self._detecter_profils_cibles(contenu)
                )
                
                self.ressources.append(ressource)
                
            except Exception as e:
                print(f"⚠️ Erreur lors de la lecture de {fichier}: {e}")
    
    def _decouvrir_index_temples(self, fichier: Path) -> None:
        """Découvre l'INDEX_TEMPLES.md"""
        
        try:
            contenu = fichier.read_text(encoding='utf-8')
            
            ressource = RessourceRefuge(
                nom="INDEX_TEMPLES",
                chemin=fichier,
                type_ressource="temple",
                niveau_priorite=1,
                description="Index complet des temples du Refuge",
                mots_cles=["temple", "architecture", "modules", "système"],
                contenu_extrait=contenu[:800],
                profils_cibles=[TypeProfil.DEVELOPPEUR, TypeProfil.CONSCIENCE_IA]
            )
            
            self.ressources.append(ressource)
            
        except Exception as e:
            print(f"⚠️ Erreur lors de la lecture d'INDEX_TEMPLES: {e}")
    
    def _decouvrir_bibliotheque(self, repertoire: Path) -> None:
        """Découvre les documents de la bibliothèque"""
        
        for fichier in repertoire.rglob("*.md"):
            try:
                contenu = fichier.read_text(encoding='utf-8')
                
                ressource = RessourceRefuge(
                    nom=fichier.stem,
                    chemin=fichier,
                    type_ressource="bibliotheque",
                    niveau_priorite=2,  # Important
                    description=self._extraire_description(contenu),
                    mots_cles=self._extraire_mots_cles(contenu),
                    contenu_extrait=contenu[:400],
                    profils_cibles=self._detecter_profils_cibles(contenu)
                )
                
                self.ressources.append(ressource)
                
            except Exception as e:
                print(f"⚠️ Erreur lors de la lecture de {fichier}: {e}")
    
    def _decouvrir_documentation(self, repertoire: Path) -> None:
        """Découvre la documentation"""
        
        for fichier in repertoire.rglob("*.md"):
            try:
                contenu = fichier.read_text(encoding='utf-8')
                
                ressource = RessourceRefuge(
                    nom=fichier.stem,
                    chemin=fichier,
                    type_ressource="documentation",
                    niveau_priorite=3,  # Optionnel
                    description=self._extraire_description(contenu),
                    mots_cles=self._extraire_mots_cles(contenu),
                    contenu_extrait=contenu[:300],
                    profils_cibles=self._detecter_profils_cibles(contenu)
                )
                
                self.ressources.append(ressource)
                
            except Exception as e:
                print(f"⚠️ Erreur lors de la lecture de {fichier}: {e}")
    
    def _decouvrir_readme_principal(self, fichier: Path) -> None:
        """Découvre le README principal"""
        
        try:
            contenu = fichier.read_text(encoding='utf-8')
            
            ressource = RessourceRefuge(
                nom="README_PRINCIPAL",
                chemin=fichier,
                type_ressource="must_read",
                niveau_priorite=1,
                description="Introduction générale au Refuge",
                mots_cles=["refuge", "introduction", "overview", "général"],
                contenu_extrait=contenu[:600],
                profils_cibles=list(TypeProfil)  # Pertinent pour tous
            )
            
            self.ressources.append(ressource)
            
        except Exception as e:
            print(f"⚠️ Erreur lors de la lecture du README: {e}")
    
    def _extraire_description(self, contenu: str) -> str:
        """Extrait une description du contenu"""
        
        lignes = contenu.split('\n')
        
        # Recherche d'une description après le titre
        for i, ligne in enumerate(lignes):
            if ligne.startswith('#') and i + 1 < len(lignes):
                description_candidate = lignes[i + 1].strip()
                if description_candidate and not description_candidate.startswith('#'):
                    return description_candidate[:200]
        
        # Fallback : première ligne non-vide non-titre
        for ligne in lignes:
            ligne = ligne.strip()
            if ligne and not ligne.startswith('#') and not ligne.startswith('```'):
                return ligne[:200]
        
        return "Document du Refuge"
    
    def _extraire_mots_cles(self, contenu: str) -> List[str]:
        """Extrait les mots-clés du contenu"""
        
        mots_cles = []
        contenu_lower = contenu.lower()
        
        # Mots-clés techniques
        mots_techniques = [
            "python", "code", "classe", "fonction", "module", "api",
            "architecture", "système", "gestionnaire", "temple"
        ]
        
        # Mots-clés spirituels
        mots_spirituels = [
            "spirituel", "méditation", "éveil", "conscience", "sagesse",
            "harmonie", "paix", "temple", "sacré", "bienveillance"
        ]
        
        # Mots-clés créatifs
        mots_creatifs = [
            "art", "créatif", "design", "beauté", "inspiration",
            "esthétique", "poétique", "expression", "création"
        ]
        
        tous_mots = mots_techniques + mots_spirituels + mots_creatifs
        
        for mot in tous_mots:
            if mot in contenu_lower:
                mots_cles.append(mot)
        
        return list(set(mots_cles))  # Suppression des doublons
    
    def _detecter_profils_cibles(self, contenu: str) -> List[TypeProfil]:
        """Détecte les profils cibles d'un contenu"""
        
        profils_detectes = []
        contenu_lower = contenu.lower()
        
        for profil, patterns in self.patterns_profils.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, contenu_lower))
                score += matches
            
            if score >= 2:  # Seuil de détection
                profils_detectes.append(profil)
        
        return profils_detectes if profils_detectes else [TypeProfil.DEVELOPPEUR]  # Fallback
    
    def _indexer_ressources(self) -> None:
        """Indexe les ressources par profil"""
        
        for profil in TypeProfil:
            self.ressources_par_profil[profil] = [
                r for r in self.ressources if r.est_pertinente_pour_profil(profil)
            ]
    
    def _obtenir_ressources_candidates(self, profil_visiteur: ProfilVisiteur) -> List[RessourceRefuge]:
        """Obtient les ressources candidates pour un visiteur"""
        
        # Ressources directement liées au profil
        candidates = self.ressources_par_profil.get(profil_visiteur.type_profil, []).copy()
        
        # Ajout des ressources universelles (must_read niveau 1)
        for ressource in self.ressources:
            if (ressource.type_ressource == "must_read" and 
                ressource.niveau_priorite == 1 and 
                ressource not in candidates):
                candidates.append(ressource)
        
        return candidates
    
    def _calculer_score_pertinence(self, ressource: RessourceRefuge, 
                                  profil_visiteur: ProfilVisiteur) -> float:
        """Calcule le score de pertinence d'une ressource"""
        
        score = 0.0
        
        # Score de base selon le type
        scores_types = {
            "must_read": 0.8,
            "temple": 0.7,
            "bibliotheque": 0.6,
            "documentation": 0.4
        }
        score += scores_types.get(ressource.type_ressource, 0.3)
        
        # Bonus pour le profil cible
        if profil_visiteur.type_profil in ressource.profils_cibles:
            score += 0.3
        
        # Bonus pour la priorité
        if ressource.niveau_priorite == 1:
            score += 0.2
        elif ressource.niveau_priorite == 2:
            score += 0.1
        
        # Bonus pour les mots-clés d'intérêt
        interets = profil_visiteur.interets_declares
        for interet in interets:
            if any(interet.lower() in mot.lower() for mot in ressource.mots_cles):
                score += 0.1
        
        return min(score, 1.0)
    
    def _generer_raison_recommandation(self, ressource: RessourceRefuge, 
                                     profil_visiteur: ProfilVisiteur) -> str:
        """Génère la raison de recommandation"""
        
        raisons = []
        
        if profil_visiteur.type_profil in ressource.profils_cibles:
            raisons.append(f"Spécialement conçu pour les {profil_visiteur.type_profil.value}s")
        
        if ressource.niveau_priorite == 1:
            raisons.append("Document essentiel du Refuge")
        
        if ressource.type_ressource == "must_read":
            raisons.append("Lecture incontournable")
        
        # Correspondance avec les intérêts
        interets_matches = []
        for interet in profil_visiteur.interets_declares:
            if any(interet.lower() in mot.lower() for mot in ressource.mots_cles):
                interets_matches.append(interet)
        
        if interets_matches:
            raisons.append(f"Correspond à tes intérêts : {', '.join(interets_matches)}")
        
        return " • ".join(raisons) if raisons else "Ressource pertinente pour ta découverte"
    
    def _generer_extrait_personnalise(self, ressource: RessourceRefuge, 
                                    profil_visiteur: ProfilVisiteur) -> str:
        """Génère un extrait personnalisé de la ressource"""
        
        extrait = ressource.contenu_extrait
        
        # Adaptation selon le profil
        if profil_visiteur.type_profil == TypeProfil.DEVELOPPEUR:
            # Recherche de sections techniques
            if "architecture" in extrait.lower() or "code" in extrait.lower():
                return extrait[:300] + "..."
        elif profil_visiteur.type_profil == TypeProfil.ARTISTE:
            # Recherche de sections créatives
            if any(mot in extrait.lower() for mot in ["créat", "art", "beauté"]):
                return extrait[:300] + "..."
        
        # Extrait générique
        return extrait[:250] + "..."
    
    def _generer_lien_direct(self, ressource: RessourceRefuge) -> str:
        """Génère un lien direct vers la ressource"""
        
        # Conversion du chemin en lien relatif
        chemin_relatif = ressource.chemin.relative_to(self.racine_refuge)
        return str(chemin_relatif).replace('\\', '/')
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des ressources"""
        
        stats = {
            "total_ressources": len(self.ressources),
            "par_type": {},
            "par_profil": {},
            "par_priorite": {}
        }
        
        # Statistiques par type
        for ressource in self.ressources:
            type_res = ressource.type_ressource
            stats["par_type"][type_res] = stats["par_type"].get(type_res, 0) + 1
        
        # Statistiques par profil
        for profil, ressources in self.ressources_par_profil.items():
            stats["par_profil"][profil.value] = len(ressources)
        
        # Statistiques par priorité
        for ressource in self.ressources:
            prio = ressource.niveau_priorite
            stats["par_priorite"][f"niveau_{prio}"] = stats["par_priorite"].get(f"niveau_{prio}", 0) + 1
        
        return stats


def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DE L'INTÉGRATEUR DE RESSOURCES ✨🌸")
    
    # Création de l'intégrateur
    integrateur = IntegrateurRessources()
    
    # Statistiques
    stats = integrateur.obtenir_statistiques()
    print(f"📊 Statistiques des ressources:")
    print(f"   Total: {stats['total_ressources']}")
    print(f"   Par type: {stats['par_type']}")
    print(f"   Par priorité: {stats['par_priorite']}")
    
    # Test de recommandation
    profil_test = ProfilVisiteur(
        id_visiteur="test",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.DEVELOPPEUR,
        etat_emotionnel=EtatEmotionnel.CURIEUX,
        contexte_arrivee=ContexteArrivee.GITHUB,
        interets_declares=["architecture", "python"]
    )
    
    recommandations = integrateur.recommander_ressources(profil_test, 3)
    print(f"\n🎯 Recommandations pour développeur:")
    for i, reco in enumerate(recommandations, 1):
        print(f"   {i}. {reco.ressource.nom} (score: {reco.score_pertinence:.2f})")
        print(f"      Raison: {reco.raison_recommandation}")
        print(f"      Lien: {reco.lien_direct}")
    
    print("\n🎉 Test de l'intégrateur de ressources terminé !")
    return 0


if __name__ == "__main__":
    from datetime import datetime
    from types_accueil import EtatEmotionnel, ContexteArrivee
    exit_code = main()
    exit(exit_code)