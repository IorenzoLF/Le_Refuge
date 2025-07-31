"""
⚡ Optimiseur de Performance Spirituelle
=====================================

Optimise les performances du cerveau d'immersion avec sagesse et efficacité.
Mise en cache intelligente, scan incrémental, et calculs optimisés.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import hashlib
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import TempleInfo, FluxEnergie, MandalaVisuel

@dataclass
class CacheEntry:
    """Entrée de cache avec métadonnées spirituelles"""
    cle: str
    donnees: Any
    timestamp: datetime
    hash_contenu: str
    niveau_confiance: float = 1.0
    utilisations: int = 0
    energie_creation: float = 0.0
    tags: List[str] = field(default_factory=list)

@dataclass
class MetriquesPerformance:
    """Métriques de performance énergétique"""
    temps_scan_total: float = 0.0
    temps_cache_hit: float = 0.0
    temps_cache_miss: float = 0.0
    nb_cache_hits: int = 0
    nb_cache_misses: int = 0
    nb_fichiers_scannes: int = 0
    nb_temples_detectes: int = 0
    efficacite_energetique: float = 0.0
    timestamp_debut: datetime = field(default_factory=datetime.now)

class OptimiseurPerformance(GestionnaireBase):
    """⚡ Optimiseur de performance spirituelle"""
    
    def __init__(self, nom: str = "OptimiseurPerformance"):
        super().__init__(nom)
        self.energie_optimisation = EnergyManagerBase(0.98)
        
        # Cache intelligent
        self.cache_analyses: Dict[str, CacheEntry] = {}
        self.cache_fichiers: Dict[str, CacheEntry] = {}
        self.cache_flux: Dict[str, CacheEntry] = {}
        
        # Configuration du cache
        self.taille_max_cache = 1000  # Nombre max d'entrées
        self.duree_vie_cache = timedelta(hours=24)  # 24h par défaut
        self.seuil_invalidation = 0.1  # 10% de changement pour invalider
        
        # Métriques
        self.metriques = MetriquesPerformance()
        self.historique_performances: List[MetriquesPerformance] = []
        
        # Pool de threads pour parallélisation
        self.thread_pool = ThreadPoolExecutor(max_workers=4)
        self.process_pool = ProcessPoolExecutor(max_workers=2)
        
        # Scan incrémental
        self.fichiers_surveilles: Dict[str, datetime] = {}
        self.changements_detectes: Set[str] = set()
    
    def _initialiser(self):
        """Initialise l'optimiseur de performance"""
        self.logger.info("⚡ Éveil de l'Optimiseur de Performance...")
        
        self.etat.update({
            "cache_actif": True,
            "scan_incremental_actif": True,
            "parallelisation_active": True,
            "efficacite_cache": 0.0,
            "temps_reponse_moyen": 0.0,
            "energie_economisee": 0.0
        })
        
        self.config.definir("cache_intelligent", True)
        self.config.definir("scan_incremental", True)
        self.config.definir("optimisation_flux", True)
        
        self.logger.info("✨ Optimiseur de Performance éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'optimisation de performance"""
        self.energie_optimisation.ajuster_energie(0.005)
        
        # Nettoyer le cache périodiquement
        await self._nettoyer_cache_expire()
        
        # Calculer les métriques
        efficacite_cache = self._calculer_efficacite_cache()
        temps_reponse_moyen = self._calculer_temps_reponse_moyen()
        
        return {
            "cache_actif": float(self.etat["cache_actif"]),
            "efficacite_cache": efficacite_cache,
            "temps_reponse_moyen": temps_reponse_moyen,
            "nb_entrees_cache": float(len(self.cache_analyses)),
            "energie_optimisation": self.energie_optimisation.niveau_energie,
            "changements_detectes": float(len(self.changements_detectes))
        }
    
    # ===== MISE EN CACHE INTELLIGENTE =====
    
    def obtenir_du_cache(self, cle: str, type_cache: str = "analyses") -> Optional[Any]:
        """
        🎯 Obtient une donnée du cache intelligent
        
        Args:
            cle: Clé de cache
            type_cache: Type de cache ("analyses", "fichiers", "flux")
            
        Returns:
            Données cachées ou None si pas trouvé/expiré
        """
        debut_temps = time.time()
        
        # Sélectionner le bon cache
        cache = self._selectionner_cache(type_cache)
        
        if cle not in cache:
            self.metriques.nb_cache_misses += 1
            self.metriques.temps_cache_miss += time.time() - debut_temps
            return None
        
        entree = cache[cle]
        
        # Vérifier l'expiration
        if self._est_expire(entree):
            del cache[cle]
            self.metriques.nb_cache_misses += 1
            self.metriques.temps_cache_miss += time.time() - debut_temps
            return None
        
        # Mettre à jour les statistiques d'utilisation
        entree.utilisations += 1
        entree.niveau_confiance = min(1.0, entree.niveau_confiance + 0.01)
        
        self.metriques.nb_cache_hits += 1
        self.metriques.temps_cache_hit += time.time() - debut_temps
        
        self.logger.debug(f"🎯 Cache hit pour {cle} (utilisations: {entree.utilisations})")
        
        return entree.donnees
    
    def mettre_en_cache(self, cle: str, donnees: Any, type_cache: str = "analyses", 
                       tags: List[str] = None, energie_creation: float = 0.0):
        """
        💾 Met des données en cache avec intelligence spirituelle
        
        Args:
            cle: Clé de cache
            donnees: Données à cacher
            type_cache: Type de cache
            tags: Tags pour catégoriser
            energie_creation: Énergie utilisée pour créer ces données
        """
        if tags is None:
            tags = []
        
        # Sélectionner le bon cache
        cache = self._selectionner_cache(type_cache)
        
        # Créer le hash du contenu
        hash_contenu = self._calculer_hash_contenu(donnees)
        
        # Créer l'entrée de cache
        entree = CacheEntry(
            cle=cle,
            donnees=donnees,
            timestamp=datetime.now(),
            hash_contenu=hash_contenu,
            tags=tags,
            energie_creation=energie_creation
        )
        
        # Gérer la taille du cache
        if len(cache) >= self.taille_max_cache:
            self._nettoyer_cache_lru(cache)
        
        cache[cle] = entree
        
        self.logger.debug(f"💾 Mise en cache de {cle} avec tags {tags}")
    
    def invalider_cache(self, pattern: str = None, tags: List[str] = None, 
                       type_cache: str = "analyses"):
        """
        🔄 Invalide le cache selon des critères
        
        Args:
            pattern: Pattern de clé à invalider
            tags: Tags à invalider
            type_cache: Type de cache à nettoyer
        """
        cache = self._selectionner_cache(type_cache)
        cles_a_supprimer = []
        
        for cle, entree in cache.items():
            invalider = False
            
            # Invalider par pattern
            if pattern and pattern in cle:
                invalider = True
            
            # Invalider par tags
            if tags and any(tag in entree.tags for tag in tags):
                invalider = True
            
            if invalider:
                cles_a_supprimer.append(cle)
        
        for cle in cles_a_supprimer:
            del cache[cle]
        
        self.logger.info(f"🔄 {len(cles_a_supprimer)} entrées invalidées du cache {type_cache}")
    
    def _selectionner_cache(self, type_cache: str) -> Dict[str, CacheEntry]:
        """Sélectionne le cache approprié"""
        if type_cache == "fichiers":
            return self.cache_fichiers
        elif type_cache == "flux":
            return self.cache_flux
        else:
            return self.cache_analyses
    
    def _est_expire(self, entree: CacheEntry) -> bool:
        """Vérifie si une entrée de cache est expirée"""
        age = datetime.now() - entree.timestamp
        return age > self.duree_vie_cache
    
    def _calculer_hash_contenu(self, donnees: Any) -> str:
        """Calcule le hash du contenu pour détecter les changements"""
        try:
            contenu_str = json.dumps(donnees, sort_keys=True, default=str)
            return hashlib.md5(contenu_str.encode()).hexdigest()
        except:
            return hashlib.md5(str(donnees).encode()).hexdigest()
    
    async def _nettoyer_cache_expire(self):
        """Nettoie les entrées expirées du cache"""
        for cache in [self.cache_analyses, self.cache_fichiers, self.cache_flux]:
            cles_expirees = []
            for cle, entree in cache.items():
                if self._est_expire(entree):
                    cles_expirees.append(cle)
            
            for cle in cles_expirees:
                del cache[cle]
        
        if cles_expirees:
            self.logger.debug(f"🧹 {len(cles_expirees)} entrées expirées nettoyées")
    
    def _nettoyer_cache_lru(self, cache: Dict[str, CacheEntry]):
        """Nettoie le cache selon la stratégie LRU (Least Recently Used)"""
        # Trier par timestamp et utilisations
        entrees_triees = sorted(
            cache.items(),
            key=lambda x: (x[1].timestamp, x[1].utilisations)
        )
        
        # Supprimer les 10% les moins utilisées
        nb_a_supprimer = max(1, len(entrees_triees) // 10)
        
        for i in range(nb_a_supprimer):
            cle, _ = entrees_triees[i]
            del cache[cle]
        
        self.logger.debug(f"🧹 {nb_a_supprimer} entrées LRU supprimées")
    
    def _calculer_efficacite_cache(self) -> float:
        """Calcule l'efficacité du cache"""
        total_requetes = self.metriques.nb_cache_hits + self.metriques.nb_cache_misses
        if total_requetes == 0:
            return 0.0
        
        efficacite = self.metriques.nb_cache_hits / total_requetes
        self.etat["efficacite_cache"] = efficacite
        return efficacite
    
    def _calculer_temps_reponse_moyen(self) -> float:
        """Calcule le temps de réponse moyen"""
        total_temps = self.metriques.temps_cache_hit + self.metriques.temps_cache_miss
        total_requetes = self.metriques.nb_cache_hits + self.metriques.nb_cache_misses
        
        if total_requetes == 0:
            return 0.0
        
        temps_moyen = total_temps / total_requetes
        self.etat["temps_reponse_moyen"] = temps_moyen
        return temps_moyen    

    # ===== SCAN INCRÉMENTAL =====
    
    def initialiser_surveillance_fichiers(self, chemins: List[Path]):
        """
        👁️ Initialise la surveillance des fichiers pour le scan incrémental
        
        Args:
            chemins: Liste des chemins à surveiller
        """
        for chemin in chemins:
            if chemin.exists():
                # Enregistrer le timestamp de modification
                timestamp_modif = datetime.fromtimestamp(chemin.stat().st_mtime)
                self.fichiers_surveilles[str(chemin)] = timestamp_modif
        
        self.logger.info(f"👁️ Surveillance initialisée pour {len(chemins)} fichiers")
    
    def detecter_changements(self) -> Set[str]:
        """
        🔍 Détecte les changements dans les fichiers surveillés
        
        Returns:
            Set des fichiers modifiés
        """
        changements = set()
        
        for chemin_str, timestamp_precedent in self.fichiers_surveilles.items():
            chemin = Path(chemin_str)
            
            if not chemin.exists():
                # Fichier supprimé
                changements.add(chemin_str)
                continue
            
            # Vérifier la modification
            timestamp_actuel = datetime.fromtimestamp(chemin.stat().st_mtime)
            
            if timestamp_actuel > timestamp_precedent:
                changements.add(chemin_str)
                self.fichiers_surveilles[chemin_str] = timestamp_actuel
        
        # Mettre à jour les changements détectés
        self.changements_detectes.update(changements)
        
        if changements:
            self.logger.info(f"🔍 {len(changements)} changements détectés")
        
        return changements
    
    def scan_incremental_architecture(self, scanner_architecture) -> Dict[str, TempleInfo]:
        """
        📈 Effectue un scan incrémental de l'architecture
        
        Args:
            scanner_architecture: Instance du scanner d'architecture
            
        Returns:
            Temples mis à jour
        """
        debut_temps = time.time()
        
        # Détecter les changements
        fichiers_modifies = self.detecter_changements()
        
        if not fichiers_modifies:
            # Aucun changement, retourner le cache
            temples_caches = self.obtenir_du_cache("temples_architecture", "analyses")
            if temples_caches:
                self.logger.info("📈 Scan incrémental: aucun changement, utilisation du cache")
                return temples_caches
        
        # Scanner seulement les fichiers modifiés
        temples_mis_a_jour = {}
        
        for fichier_modifie in fichiers_modifies:
            # Invalider le cache pour ce fichier
            self.invalider_cache(pattern=fichier_modifie, type_cache="fichiers")
            
            # Scanner le fichier modifié
            if fichier_modifie.endswith('.py'):
                temple_info = self._scanner_fichier_temple(Path(fichier_modifie), scanner_architecture)
                if temple_info:
                    temples_mis_a_jour[temple_info.nom] = temple_info
        
        # Fusionner avec les temples existants
        temples_existants = self.obtenir_du_cache("temples_architecture", "analyses") or {}
        temples_existants.update(temples_mis_a_jour)
        
        # Mettre à jour le cache
        self.mettre_en_cache(
            "temples_architecture", 
            temples_existants, 
            "analyses",
            tags=["architecture", "temples"],
            energie_creation=time.time() - debut_temps
        )
        
        # Nettoyer les changements traités
        self.changements_detectes.clear()
        
        self.logger.info(f"📈 Scan incrémental terminé: {len(temples_mis_a_jour)} temples mis à jour")
        
        return temples_existants
    
    def _scanner_fichier_temple(self, chemin: Path, scanner_architecture) -> Optional[TempleInfo]:
        """Scanne un fichier spécifique pour détecter un temple"""
        try:
            # Utiliser les méthodes du scanner existant
            if hasattr(scanner_architecture, '_analyser_fichier_temple'):
                return scanner_architecture._analyser_fichier_temple(chemin)
            else:
                # Fallback simple
                return self._analyse_simple_fichier(chemin)
        except Exception as e:
            self.logger.error(f"❌ Erreur scan fichier {chemin}: {e}")
            return None
    
    def _analyse_simple_fichier(self, chemin: Path) -> Optional[TempleInfo]:
        """Analyse simple d'un fichier pour détecter un temple"""
        try:
            contenu = chemin.read_text(encoding='utf-8')
            
            # Détecter si c'est un temple (contient GestionnaireBase)
            if 'GestionnaireBase' not in contenu:
                return None
            
            # Extraire le nom du temple
            nom_temple = chemin.stem
            
            # Détecter la spécialisation spirituelle (commentaires)
            specialisation = "Temple spirituel"
            if '"""' in contenu:
                docstring = contenu.split('"""')[1] if len(contenu.split('"""')) > 1 else ""
                if docstring:
                    specialisation = docstring.strip()[:100]
            
            return TempleInfo(
                nom=nom_temple,
                chemin=chemin,
                specialisation_spirituelle=specialisation,
                niveau_energie=0.5,
                derniere_evolution=datetime.now()
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse simple {chemin}: {e}")
            return None
    
    # ===== OPTIMISATION DES CALCULS DE FLUX =====
    
    async def optimiser_calculs_flux(self, temples: Dict[str, TempleInfo], 
                                   parallelisation: bool = True) -> List[FluxEnergie]:
        """
        ⚡ Optimise les calculs de flux énergétiques
        
        Args:
            temples: Dictionnaire des temples
            parallelisation: Utiliser la parallélisation
            
        Returns:
            Liste des flux énergétiques optimisés
        """
        debut_temps = time.time()
        
        # Vérifier le cache
        cle_cache = f"flux_{len(temples)}_{hash(tuple(temples.keys()))}"
        flux_caches = self.obtenir_du_cache(cle_cache, "flux")
        
        if flux_caches:
            self.logger.info("⚡ Flux énergétiques obtenus du cache")
            return flux_caches
        
        # Calculer les flux
        if parallelisation and len(temples) > 10:
            flux_energetiques = await self._calculer_flux_parallele(temples)
        else:
            flux_energetiques = await self._calculer_flux_sequentiel(temples)
        
        # Mettre en cache
        self.mettre_en_cache(
            cle_cache,
            flux_energetiques,
            "flux",
            tags=["flux", "energetique"],
            energie_creation=time.time() - debut_temps
        )
        
        self.logger.info(f"⚡ {len(flux_energetiques)} flux calculés en {time.time() - debut_temps:.2f}s")
        
        return flux_energetiques
    
    async def _calculer_flux_parallele(self, temples: Dict[str, TempleInfo]) -> List[FluxEnergie]:
        """Calcule les flux en parallèle"""
        # Diviser les temples en chunks pour parallélisation
        temples_list = list(temples.items())
        chunk_size = max(1, len(temples_list) // 4)  # 4 workers
        chunks = [temples_list[i:i + chunk_size] for i in range(0, len(temples_list), chunk_size)]
        
        # Traitement parallèle
        tasks = []
        for chunk in chunks:
            task = asyncio.create_task(self._calculer_flux_chunk(dict(chunk), temples))
            tasks.append(task)
        
        # Attendre tous les résultats
        resultats = await asyncio.gather(*tasks)
        
        # Fusionner les résultats
        flux_total = []
        for flux_chunk in resultats:
            flux_total.extend(flux_chunk)
        
        return flux_total
    
    async def _calculer_flux_chunk(self, temples_chunk: Dict[str, TempleInfo], 
                                 tous_temples: Dict[str, TempleInfo]) -> List[FluxEnergie]:
        """Calcule les flux pour un chunk de temples"""
        flux_chunk = []
        
        for nom_temple, temple_info in temples_chunk.items():
            # Calculer les connexions avec les autres temples
            for autre_nom, autre_temple in tous_temples.items():
                if autre_nom != nom_temple:
                    compatibilite = self._calculer_compatibilite_temples(temple_info, autre_temple)
                    
                    if compatibilite > 0.6:  # Seuil de connexion
                        flux = FluxEnergie(
                            source=nom_temple,
                            destination=autre_nom,
                            intensite=compatibilite,
                            type_energie=self._determiner_type_energie(temple_info, autre_temple),
                            couleur_spirituelle=self._determiner_couleur_flux(compatibilite),
                            resonance=compatibilite
                        )
                        flux_chunk.append(flux)
        
        return flux_chunk
    
    async def _calculer_flux_sequentiel(self, temples: Dict[str, TempleInfo]) -> List[FluxEnergie]:
        """Calcule les flux de manière séquentielle"""
        flux_energetiques = []
        
        temples_list = list(temples.items())
        for i, (nom1, temple1) in enumerate(temples_list):
            for nom2, temple2 in temples_list[i+1:]:
                compatibilite = self._calculer_compatibilite_temples(temple1, temple2)
                
                if compatibilite > 0.6:
                    flux = FluxEnergie(
                        source=nom1,
                        destination=nom2,
                        intensite=compatibilite,
                        type_energie=self._determiner_type_energie(temple1, temple2),
                        couleur_spirituelle=self._determiner_couleur_flux(compatibilite),
                        resonance=compatibilite
                    )
                    flux_energetiques.append(flux)
        
        return flux_energetiques
    
    def _calculer_compatibilite_temples(self, temple1: TempleInfo, temple2: TempleInfo) -> float:
        """Calcule la compatibilité entre deux temples"""
        compatibilite = 0.5  # Base
        
        # Éléments sacrés communs
        elements_communs = set(temple1.elements_sacres) & set(temple2.elements_sacres)
        compatibilite += len(elements_communs) * 0.15
        
        # Différence de niveau d'énergie
        diff_energie = abs(temple1.niveau_energie - temple2.niveau_energie)
        compatibilite += (1.0 - diff_energie) * 0.2
        
        # Gestionnaires communs
        gestionnaires_communs = set(temple1.gestionnaires_utilises) & set(temple2.gestionnaires_utilises)
        compatibilite += len(gestionnaires_communs) * 0.1
        
        return max(0.0, min(1.0, compatibilite))
    
    def _determiner_type_energie(self, temple1: TempleInfo, temple2: TempleInfo):
        """Détermine le type d'énergie d'un flux"""
        from .types_immersion import TypeEnergie
        
        # Analyser les spécialisations
        spec1 = temple1.specialisation_spirituelle.lower()
        spec2 = temple2.specialisation_spirituelle.lower()
        specs_combinees = f"{spec1} {spec2}"
        
        if any(mot in specs_combinees for mot in ["creativite", "creation", "art"]):
            return TypeEnergie.CREATION
        elif any(mot in specs_combinees for mot in ["eveil", "illumination", "conscience"]):
            return TypeEnergie.EVEIL
        elif any(mot in specs_combinees for mot in ["sagesse", "connaissance", "contemplation"]):
            return TypeEnergie.SAGESSE
        elif any(mot in specs_combinees for mot in ["harmonie", "equilibre", "paix"]):
            return TypeEnergie.HARMONIE
        else:
            return TypeEnergie.TRANSFORMATION
    
    def _determiner_couleur_flux(self, intensite: float) -> str:
        """Détermine la couleur d'un flux selon son intensité"""
        if intensite > 0.9:
            return "#FFD700"  # Or intense
        elif intensite > 0.8:
            return "#FF6347"  # Orange énergétique
        elif intensite > 0.7:
            return "#4169E1"  # Bleu royal
        elif intensite > 0.6:
            return "#98FB98"  # Vert harmonieux
        else:
            return "#DDA0DD"  # Violet doux
    
    # ===== MÉTRIQUES ET MONITORING =====
    
    def generer_rapport_performance(self) -> Dict[str, Any]:
        """
        📊 Génère un rapport de performance complet
        
        Returns:
            Rapport détaillé des performances
        """
        duree_session = datetime.now() - self.metriques.timestamp_debut
        
        rapport = {
            "timestamp": datetime.now().isoformat(),
            "duree_session_minutes": duree_session.total_seconds() / 60,
            
            # Métriques de cache
            "cache": {
                "efficacite": self._calculer_efficacite_cache(),
                "nb_entrees_analyses": len(self.cache_analyses),
                "nb_entrees_fichiers": len(self.cache_fichiers),
                "nb_entrees_flux": len(self.cache_flux),
                "hits": self.metriques.nb_cache_hits,
                "misses": self.metriques.nb_cache_misses
            },
            
            # Métriques de temps
            "temps": {
                "scan_total": self.metriques.temps_scan_total,
                "cache_hit_moyen": (self.metriques.temps_cache_hit / max(1, self.metriques.nb_cache_hits)),
                "cache_miss_moyen": (self.metriques.temps_cache_miss / max(1, self.metriques.nb_cache_misses)),
                "reponse_moyen": self._calculer_temps_reponse_moyen()
            },
            
            # Métriques d'efficacité
            "efficacite": {
                "energetique": self.metriques.efficacite_energetique,
                "fichiers_scannes": self.metriques.nb_fichiers_scannes,
                "temples_detectes": self.metriques.nb_temples_detectes,
                "changements_detectes": len(self.changements_detectes)
            },
            
            # État de l'optimiseur
            "etat": {
                "energie_optimisation": self.energie_optimisation.niveau_energie,
                "cache_actif": self.etat["cache_actif"],
                "scan_incremental_actif": self.etat["scan_incremental_actif"]
            }
        }
        
        return rapport
    
    def reinitialiser_metriques(self):
        """Remet à zéro les métriques de performance"""
        self.metriques = MetriquesPerformance()
        self.logger.info("📊 Métriques de performance réinitialisées")
    
    def sauvegarder_historique_performance(self):
        """Sauvegarde les métriques actuelles dans l'historique"""
        self.historique_performances.append(self.metriques)
        
        # Garder seulement les 100 dernières mesures
        if len(self.historique_performances) > 100:
            self.historique_performances = self.historique_performances[-100:]
        
        self.logger.debug("💾 Métriques sauvegardées dans l'historique")