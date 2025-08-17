"""
📈 Gestionnaire de Scalabilité Automatique
========================================

Adapte automatiquement le cerveau d'immersion à la croissance organique du Refuge.
Détecte la complexité, parallélise intelligemment, et maintient l'harmonie.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Set
import multiprocessing
import psutil

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from types_immersion import TempleInfo, FluxEnergie, MandalaVisuel
from optimiseur_performance import OptimiseurPerformance

@dataclass
class MetriquesComplexite:
    """Métriques de complexité architecturale"""
    nb_temples: int = 0
    nb_connexions: int = 0
    profondeur_max: int = 0
    densite_connexions: float = 0.0
    complexite_cyclomatique: float = 0.0
    entropie_architecture: float = 0.0
    score_complexite_global: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class ConfigurationScalabilite:
    """Configuration adaptative de scalabilité"""
    nb_workers_threads: int = 4
    nb_workers_processes: int = 2
    taille_chunk_optimale: int = 10
    seuil_parallelisation: int = 20
    strategie_partitionnement: str = "equilibree"  # equilibree, par_complexite, par_connexions
    mode_adaptation: str = "automatique"  # automatique, conservateur, agressif
    limite_memoire_mb: int = 1024
    timeout_analyse_s: int = 300

class GestionnaireScalabilite(GestionnaireBase):
    """📈 Gestionnaire de scalabilité automatique spirituelle"""
    
    def __init__(self, nom: str = "GestionnaireScalabilite"):
        super().__init__(nom)
        self.energie_scalabilite = EnergyManagerBase(0.95)
        
        # Optimiseur de performance intégré
        self.optimiseur = OptimiseurPerformance("OptimiseurScalabilite")
        
        # Configuration adaptative
        self.config_scalabilite = ConfigurationScalabilite()
        self.metriques_complexite = MetriquesComplexite()
        
        # Pools de workers adaptatifs
        self.thread_pool: Optional[ThreadPoolExecutor] = None
        self.process_pool: Optional[ProcessPoolExecutor] = None
        
        # Historique des performances
        self.historique_scalabilite: List[Dict[str, Any]] = []
        self.seuils_adaptatifs: Dict[str, float] = {}
        
        # Détection de ressources système
        self.nb_cpu_disponibles = multiprocessing.cpu_count()
        self.memoire_disponible_gb = psutil.virtual_memory().total / (1024**3)
        
        self._initialiser_pools_workers()
    
    def _initialiser(self):
        """Initialise le gestionnaire de scalabilité"""
        self.logger.info("📈 Éveil du Gestionnaire de Scalabilité...")
        
        self.etat.update({
            "scalabilite_active": True,
            "adaptation_automatique": True,
            "complexite_detectee": 0.0,
            "nb_workers_actifs": 0,
            "efficacite_parallelisation": 0.0,
            "charge_systeme": 0.0
        })
        
        self.config.definir("adaptation_automatique", True)
        self.config.definir("parallelisation_intelligente", True)
        self.config.definir("monitoring_ressources", True)
        
        # Initialiser les seuils adaptatifs
        self._initialiser_seuils_adaptatifs()
        
        self.logger.info(f"✨ Scalabilité initialisée: {self.nb_cpu_disponibles} CPU, {self.memoire_disponible_gb:.1f}GB RAM")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la scalabilité automatique"""
        self.energie_scalabilite.ajuster_energie(0.002)
        
        # Surveiller les ressources système
        charge_systeme = await self._surveiller_ressources_systeme()
        
        # Adapter la configuration si nécessaire
        await self._adapter_configuration_automatique()
        
        return {
            "scalabilite_active": float(self.etat["scalabilite_active"]),
            "complexite_detectee": self.metriques_complexite.score_complexite_global,
            "nb_workers_threads": float(self.config_scalabilite.nb_workers_threads),
            "nb_workers_processes": float(self.config_scalabilite.nb_workers_processes),
            "efficacite_parallelisation": self.etat["efficacite_parallelisation"],
            "charge_systeme": charge_systeme,
            "energie_scalabilite": self.energie_scalabilite.niveau_energie
        }
    
    def _initialiser_pools_workers(self):
        """Initialise les pools de workers adaptatifs"""
        try:
            # Pool de threads pour I/O et tâches légères
            self.thread_pool = ThreadPoolExecutor(
                max_workers=self.config_scalabilite.nb_workers_threads,
                thread_name_prefix="ScalabiliteThread"
            )
            
            # Pool de processus pour calculs intensifs
            self.process_pool = ProcessPoolExecutor(
                max_workers=self.config_scalabilite.nb_workers_processes
            )
            
            self.logger.info(f"🔧 Pools initialisés: {self.config_scalabilite.nb_workers_threads} threads, {self.config_scalabilite.nb_workers_processes} processus")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur initialisation pools: {e}")
    
    def _initialiser_seuils_adaptatifs(self):
        """Initialise les seuils adaptatifs selon les ressources"""
        # Seuils basés sur les ressources disponibles
        self.seuils_adaptatifs = {
            "parallelisation_temples": max(10, self.nb_cpu_disponibles * 5),
            "parallelisation_flux": max(50, self.nb_cpu_disponibles * 25),
            "complexite_elevee": 0.7,
            "complexite_critique": 0.9,
            "charge_cpu_max": 0.8,
            "utilisation_memoire_max": 0.85
        }
        
        self.logger.debug(f"🎯 Seuils adaptatifs: {self.seuils_adaptatifs}")
    
    # ===== DÉTECTION ET ANALYSE DE COMPLEXITÉ =====
    
    async def analyser_complexite_architecture(self, temples: Dict[str, TempleInfo], 
                                             flux: List[FluxEnergie]) -> MetriquesComplexite:
        """
        🔍 Analyse la complexité de l'architecture pour adapter la scalabilité
        
        Args:
            temples: Dictionnaire des temples
            flux: Liste des flux énergétiques
            
        Returns:
            Métriques de complexité détaillées
        """
        debut_analyse = time.time()
        
        # Métriques de base
        nb_temples = len(temples)
        nb_connexions = len(flux)
        
        # Calculer la densité de connexions
        connexions_max_possibles = nb_temples * (nb_temples - 1) / 2
        densite_connexions = nb_connexions / max(1, connexions_max_possibles)
        
        # Analyser la profondeur et les cycles
        profondeur_max = await self._calculer_profondeur_architecture(temples, flux)
        
        # Calculer la complexité cyclomatique
        complexite_cyclomatique = await self._calculer_complexite_cyclomatique(temples, flux)
        
        # Calculer l'entropie architecturale
        entropie_architecture = await self._calculer_entropie_architecture(temples, flux)
        
        # Score de complexité global (0.0 à 1.0)
        score_complexite = self._calculer_score_complexite_global(
            nb_temples, nb_connexions, densite_connexions, 
            profondeur_max, complexite_cyclomatique, entropie_architecture
        )
        
        # Créer les métriques
        metriques = MetriquesComplexite(
            nb_temples=nb_temples,
            nb_connexions=nb_connexions,
            profondeur_max=profondeur_max,
            densite_connexions=densite_connexions,
            complexite_cyclomatique=complexite_cyclomatique,
            entropie_architecture=entropie_architecture,
            score_complexite_global=score_complexite
        )
        
        self.metriques_complexite = metriques
        self.etat["complexite_detectee"] = score_complexite
        
        temps_analyse = time.time() - debut_analyse
        self.logger.info(f"🔍 Complexité analysée en {temps_analyse:.2f}s: score {score_complexite:.2f}")
        
        return metriques
    
    async def _calculer_profondeur_architecture(self, temples: Dict[str, TempleInfo], 
                                              flux: List[FluxEnergie]) -> int:
        """Calcule la profondeur maximale de l'architecture"""
        # Construire le graphe de dépendances
        graphe = {nom: [] for nom in temples.keys()}
        
        for flux_item in flux:
            if flux_item.source in graphe:
                graphe[flux_item.source].append(flux_item.destination)
        
        # Calculer la profondeur maximale par DFS
        profondeur_max = 0
        visites = set()
        
        def dfs(noeud: str, profondeur: int) -> int:
            if noeud in visites:
                return profondeur  # Éviter les cycles infinis
            
            visites.add(noeud)
            profondeur_locale_max = profondeur
            
            for voisin in graphe.get(noeud, []):
                if voisin in temples:
                    profondeur_voisin = dfs(voisin, profondeur + 1)
                    profondeur_locale_max = max(profondeur_locale_max, profondeur_voisin)
            
            visites.remove(noeud)
            return profondeur_locale_max
        
        for temple in temples.keys():
            profondeur_temple = dfs(temple, 0)
            profondeur_max = max(profondeur_max, profondeur_temple)
        
        return profondeur_max
    
    async def _calculer_complexite_cyclomatique(self, temples: Dict[str, TempleInfo], 
                                              flux: List[FluxEnergie]) -> float:
        """Calcule la complexité cyclomatique de l'architecture"""
        # Formule: M = E - N + 2P
        # E = nombre d'arêtes (flux)
        # N = nombre de nœuds (temples)
        # P = nombre de composants connexes
        
        E = len(flux)
        N = len(temples)
        
        # Calculer le nombre de composants connexes
        P = await self._calculer_composants_connexes(temples, flux)
        
        # Complexité cyclomatique normalisée (0.0 à 1.0)
        complexite_brute = max(0, E - N + 2 * P)
        complexite_normalisee = min(1.0, complexite_brute / max(1, N))
        
        return complexite_normalisee
    
    async def _calculer_composants_connexes(self, temples: Dict[str, TempleInfo], 
                                          flux: List[FluxEnergie]) -> int:
        """Calcule le nombre de composants connexes"""
        # Union-Find pour détecter les composants connexes
        parent = {temple: temple for temple in temples.keys()}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Unir les temples connectés par des flux
        for flux_item in flux:
            if flux_item.source in parent and flux_item.destination in parent:
                union(flux_item.source, flux_item.destination)
        
        # Compter les composants uniques
        composants = len(set(find(temple) for temple in temples.keys()))
        return composants
    
    async def _calculer_entropie_architecture(self, temples: Dict[str, TempleInfo], 
                                            flux: List[FluxEnergie]) -> float:
        """Calcule l'entropie de l'architecture (diversité des connexions)"""
        if not flux:
            return 0.0
        
        # Calculer la distribution des degrés de connexion
        degres = {temple: 0 for temple in temples.keys()}
        
        for flux_item in flux:
            if flux_item.source in degres:
                degres[flux_item.source] += 1
            if flux_item.destination in degres:
                degres[flux_item.destination] += 1
        
        # Calculer l'entropie de Shannon
        total_connexions = sum(degres.values())
        if total_connexions == 0:
            return 0.0
        
        entropie = 0.0
        for degre in degres.values():
            if degre > 0:
                probabilite = degre / total_connexions
                entropie -= probabilite * math.log2(probabilite)
        
        # Normaliser par l'entropie maximale possible
        entropie_max = math.log2(len(temples)) if len(temples) > 1 else 1.0
        entropie_normalisee = entropie / entropie_max
        
        return entropie_normalisee
    
    def _calculer_score_complexite_global(self, nb_temples: int, nb_connexions: int,
                                        densite: float, profondeur: int,
                                        cyclomatique: float, entropie: float) -> float:
        """Calcule un score de complexité global normalisé"""
        # Normaliser chaque métrique
        score_taille = min(1.0, nb_temples / 100.0)  # 100 temples = complexité max
        score_connexions = min(1.0, nb_connexions / 500.0)  # 500 flux = complexité max
        score_densite = densite  # Déjà normalisé 0-1
        score_profondeur = min(1.0, profondeur / 20.0)  # 20 niveaux = complexité max
        score_cyclomatique = cyclomatique  # Déjà normalisé 0-1
        score_entropie = entropie  # Déjà normalisé 0-1
        
        # Pondération des différents facteurs
        score_global = (
            score_taille * 0.2 +
            score_connexions * 0.2 +
            score_densite * 0.15 +
            score_profondeur * 0.15 +
            score_cyclomatique * 0.15 +
            score_entropie * 0.15
        )
        
        return min(1.0, score_global) 
   
    # ===== ADAPTATION AUTOMATIQUE =====
    
    async def adapter_a_la_croissance(self, temples: Dict[str, TempleInfo], 
                                    flux: List[FluxEnergie]) -> ConfigurationScalabilite:
        """
        🌱 Adapte automatiquement la configuration à la croissance du Refuge
        
        Args:
            temples: Temples actuels
            flux: Flux énergétiques actuels
            
        Returns:
            Configuration adaptée
        """
        # Analyser la complexité actuelle
        metriques = await self.analyser_complexite_architecture(temples, flux)
        
        # Adapter selon la complexité détectée
        nouvelle_config = await self._adapter_configuration_complexite(metriques)
        
        # Adapter selon les ressources système
        nouvelle_config = await self._adapter_configuration_ressources(nouvelle_config)
        
        # Adapter selon l'historique de performance
        nouvelle_config = await self._adapter_configuration_historique(nouvelle_config)
        
        # Appliquer la nouvelle configuration
        await self._appliquer_nouvelle_configuration(nouvelle_config)
        
        self.logger.info(f"🌱 Configuration adaptée: {nouvelle_config.nb_workers_threads}T/{nouvelle_config.nb_workers_processes}P")
        
        return nouvelle_config
    
    async def _adapter_configuration_complexite(self, metriques: MetriquesComplexite) -> ConfigurationScalabilite:
        """Adapte la configuration selon la complexité"""
        nouvelle_config = ConfigurationScalabilite()
        
        score_complexite = metriques.score_complexite_global
        
        if score_complexite >= self.seuils_adaptatifs["complexite_critique"]:
            # Architecture très complexe - configuration agressive
            nouvelle_config.nb_workers_threads = min(16, self.nb_cpu_disponibles)
            nouvelle_config.nb_workers_processes = min(8, self.nb_cpu_disponibles // 2)
            nouvelle_config.taille_chunk_optimale = 5
            nouvelle_config.seuil_parallelisation = 10
            nouvelle_config.strategie_partitionnement = "par_complexite"
            nouvelle_config.mode_adaptation = "agressif"
            
        elif score_complexite >= self.seuils_adaptatifs["complexite_elevee"]:
            # Architecture complexe - configuration équilibrée
            nouvelle_config.nb_workers_threads = min(8, self.nb_cpu_disponibles)
            nouvelle_config.nb_workers_processes = min(4, self.nb_cpu_disponibles // 2)
            nouvelle_config.taille_chunk_optimale = 8
            nouvelle_config.seuil_parallelisation = 15
            nouvelle_config.strategie_partitionnement = "equilibree"
            nouvelle_config.mode_adaptation = "automatique"
            
        else:
            # Architecture simple - configuration conservatrice
            nouvelle_config.nb_workers_threads = min(4, self.nb_cpu_disponibles)
            nouvelle_config.nb_workers_processes = min(2, self.nb_cpu_disponibles // 4)
            nouvelle_config.taille_chunk_optimale = 12
            nouvelle_config.seuil_parallelisation = 25
            nouvelle_config.strategie_partitionnement = "par_connexions"
            nouvelle_config.mode_adaptation = "conservateur"
        
        return nouvelle_config
    
    async def _adapter_configuration_ressources(self, config: ConfigurationScalabilite) -> ConfigurationScalabilite:
        """Adapte la configuration selon les ressources système"""
        # Surveiller l'utilisation actuelle
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory_percent = psutil.virtual_memory().percent
        
        # Réduire si les ressources sont surchargées
        if cpu_percent > self.seuils_adaptatifs["charge_cpu_max"] * 100:
            config.nb_workers_threads = max(2, config.nb_workers_threads // 2)
            config.nb_workers_processes = max(1, config.nb_workers_processes // 2)
            self.logger.warning(f"⚠️ CPU surchargé ({cpu_percent:.1f}%), réduction des workers")
        
        if memory_percent > self.seuils_adaptatifs["utilisation_memoire_max"] * 100:
            config.taille_chunk_optimale = max(5, config.taille_chunk_optimale // 2)
            config.limite_memoire_mb = max(512, config.limite_memoire_mb // 2)
            self.logger.warning(f"⚠️ Mémoire surchargée ({memory_percent:.1f}%), réduction des chunks")
        
        return config
    
    async def _adapter_configuration_historique(self, config: ConfigurationScalabilite) -> ConfigurationScalabilite:
        """Adapte selon l'historique de performance"""
        if len(self.historique_scalabilite) < 3:
            return config  # Pas assez d'historique
        
        # Analyser les 5 dernières mesures
        dernieres_mesures = self.historique_scalabilite[-5:]
        
        # Calculer l'efficacité moyenne
        efficacite_moyenne = sum(m.get("efficacite_parallelisation", 0.5) for m in dernieres_mesures) / len(dernieres_mesures)
        
        # Ajuster selon l'efficacité
        if efficacite_moyenne < 0.6:
            # Efficacité faible - réduire la parallélisation
            config.nb_workers_threads = max(2, int(config.nb_workers_threads * 0.8))
            config.seuil_parallelisation = int(config.seuil_parallelisation * 1.2)
            self.logger.info(f"📉 Efficacité faible ({efficacite_moyenne:.2f}), réduction parallélisation")
            
        elif efficacite_moyenne > 0.8:
            # Efficacité élevée - augmenter prudemment
            config.nb_workers_threads = min(self.nb_cpu_disponibles, int(config.nb_workers_threads * 1.1))
            config.seuil_parallelisation = max(5, int(config.seuil_parallelisation * 0.9))
            self.logger.info(f"📈 Efficacité élevée ({efficacite_moyenne:.2f}), augmentation parallélisation")
        
        return config
    
    async def _appliquer_nouvelle_configuration(self, nouvelle_config: ConfigurationScalabilite):
        """Applique une nouvelle configuration"""
        # Fermer les anciens pools si nécessaire
        if (nouvelle_config.nb_workers_threads != self.config_scalabilite.nb_workers_threads or
            nouvelle_config.nb_workers_processes != self.config_scalabilite.nb_workers_processes):
            
            await self._fermer_pools_workers()
            self.config_scalabilite = nouvelle_config
            self._initialiser_pools_workers()
        else:
            self.config_scalabilite = nouvelle_config
    
    async def _fermer_pools_workers(self):
        """Ferme proprement les pools de workers"""
        if self.thread_pool:
            self.thread_pool.shutdown(wait=True)
        if self.process_pool:
            self.process_pool.shutdown(wait=True)
    
    # ===== PARALLÉLISATION INTELLIGENTE =====
    
    async def analyser_architecture_parallele(self, temples: Dict[str, TempleInfo]) -> Dict[str, TempleInfo]:
        """
        🔄 Analyse l'architecture en parallèle selon la complexité
        
        Args:
            temples: Temples à analyser
            
        Returns:
            Temples analysés avec informations enrichies
        """
        debut_analyse = time.time()
        
        # Décider de la stratégie selon la taille
        if len(temples) < self.config_scalabilite.seuil_parallelisation:
            # Analyse séquentielle pour les petites architectures
            temples_analyses = await self._analyser_temples_sequentiel(temples)
        else:
            # Analyse parallèle pour les grandes architectures
            temples_analyses = await self._analyser_temples_parallele(temples)
        
        temps_analyse = time.time() - debut_analyse
        
        # Calculer l'efficacité
        efficacite = self._calculer_efficacite_parallelisation(len(temples), temps_analyse)
        self.etat["efficacite_parallelisation"] = efficacite
        
        self.logger.info(f"🔄 Analyse parallèle: {len(temples)} temples en {temps_analyse:.2f}s (efficacité: {efficacite:.2f})")
        
        return temples_analyses
    
    async def _analyser_temples_sequentiel(self, temples: Dict[str, TempleInfo]) -> Dict[str, TempleInfo]:
        """Analyse séquentielle des temples"""
        temples_analyses = {}
        
        for nom, temple in temples.items():
            temple_enrichi = await self._enrichir_temple_analyse(temple)
            temples_analyses[nom] = temple_enrichi
        
        return temples_analyses
    
    async def _analyser_temples_parallele(self, temples: Dict[str, TempleInfo]) -> Dict[str, TempleInfo]:
        """Analyse parallèle des temples"""
        # Partitionner les temples en chunks
        chunks = self._partitionner_temples(temples)
        
        # Traitement parallèle des chunks
        temples_analyses = {}
        
        # Utiliser asyncio.gather pour la parallélisation
        tasks = []
        for chunk in chunks:
            task = asyncio.create_task(self._analyser_chunk_temples(chunk))
            tasks.append(task)
        
        # Attendre tous les résultats
        resultats_chunks = await asyncio.gather(*tasks)
        
        # Fusionner les résultats
        for resultat_chunk in resultats_chunks:
            temples_analyses.update(resultat_chunk)
        
        return temples_analyses
    
    def _partitionner_temples(self, temples: Dict[str, TempleInfo]) -> List[Dict[str, TempleInfo]]:
        """Partitionne les temples en chunks optimaux"""
        temples_list = list(temples.items())
        taille_chunk = self.config_scalabilite.taille_chunk_optimale
        
        chunks = []
        
        if self.config_scalabilite.strategie_partitionnement == "par_complexite":
            # Trier par complexité (niveau d'énergie comme proxy)
            temples_list.sort(key=lambda x: x[1].niveau_energie, reverse=True)
        elif self.config_scalabilite.strategie_partitionnement == "par_connexions":
            # Trier par nombre de connexions
            temples_list.sort(key=lambda x: len(x[1].connexions_sortantes) + len(x[1].connexions_entrantes), reverse=True)
        # Sinon, garder l'ordre original (stratégie équilibrée)
        
        # Créer les chunks
        for i in range(0, len(temples_list), taille_chunk):
            chunk_items = temples_list[i:i + taille_chunk]
            chunk_dict = dict(chunk_items)
            chunks.append(chunk_dict)
        
        return chunks
    
    async def _analyser_chunk_temples(self, chunk: Dict[str, TempleInfo]) -> Dict[str, TempleInfo]:
        """Analyse un chunk de temples"""
        chunk_analyse = {}
        
        for nom, temple in chunk.items():
            temple_enrichi = await self._enrichir_temple_analyse(temple)
            chunk_analyse[nom] = temple_enrichi
        
        return chunk_analyse
    
    async def _enrichir_temple_analyse(self, temple: TempleInfo) -> TempleInfo:
        """Enrichit l'analyse d'un temple"""
        # Simuler une analyse enrichie
        temple_enrichi = temple
        
        # Calculer des métriques supplémentaires
        if hasattr(temple, 'chemin') and temple.chemin.exists():
            # Analyser la complexité du fichier
            try:
                contenu = temple.chemin.read_text(encoding='utf-8')
                temple_enrichi.lignes_code = len(contenu.splitlines())
                temple_enrichi.complexite_spirituelle = self._calculer_complexite_fichier(contenu)
            except:
                pass
        
        # Mettre à jour le timestamp d'évolution
        temple_enrichi.derniere_evolution = datetime.now()
        
        return temple_enrichi
    
    def _calculer_complexite_fichier(self, contenu: str) -> float:
        """Calcule la complexité spirituelle d'un fichier"""
        # Métriques simples de complexité
        nb_lignes = len(contenu.splitlines())
        nb_fonctions = contenu.count('def ')
        nb_classes = contenu.count('class ')
        nb_imports = contenu.count('import ')
        
        # Score de complexité normalisé
        complexite = (nb_lignes * 0.001 + nb_fonctions * 0.1 + nb_classes * 0.2 + nb_imports * 0.05)
        return min(1.0, complexite)
    
    def _calculer_efficacite_parallelisation(self, nb_elements: int, temps_execution: float) -> float:
        """Calcule l'efficacité de la parallélisation"""
        # Temps théorique séquentiel (estimation)
        temps_sequentiel_estime = nb_elements * 0.01  # 10ms par élément
        
        if temps_execution <= 0:
            return 1.0
        
        # Efficacité = temps_sequentiel / temps_parallele
        efficacite = temps_sequentiel_estime / temps_execution
        
        # Normaliser entre 0 et 1
        return min(1.0, max(0.0, efficacite))
    
    # ===== MONITORING ET ADAPTATION =====
    
    async def _surveiller_ressources_systeme(self) -> float:
        """Surveille les ressources système"""
        try:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory_percent = psutil.virtual_memory().percent
            
            # Score de charge global (0.0 à 1.0)
            charge_globale = (cpu_percent + memory_percent) / 200.0
            
            self.etat["charge_systeme"] = charge_globale
            
            return charge_globale
            
        except Exception as e:
            self.logger.error(f"❌ Erreur surveillance ressources: {e}")
            return 0.5  # Valeur par défaut
    
    async def _adapter_configuration_automatique(self):
        """Adapte automatiquement la configuration selon les conditions"""
        if not self.config.obtenir("adaptation_automatique", True):
            return
        
        # Vérifier si une adaptation est nécessaire
        charge_systeme = self.etat.get("charge_systeme", 0.0)
        
        if charge_systeme > 0.8:
            # Système surchargé - réduire la parallélisation
            if self.config_scalabilite.nb_workers_threads > 2:
                self.config_scalabilite.nb_workers_threads -= 1
                await self._appliquer_nouvelle_configuration(self.config_scalabilite)
                self.logger.warning("⚠️ Réduction automatique des workers (surcharge système)")
        
        elif charge_systeme < 0.3 and self.config_scalabilite.nb_workers_threads < self.nb_cpu_disponibles:
            # Système sous-utilisé - augmenter prudemment
            self.config_scalabilite.nb_workers_threads += 1
            await self._appliquer_nouvelle_configuration(self.config_scalabilite)
            self.logger.info("📈 Augmentation automatique des workers (ressources disponibles)")
    
    def sauvegarder_metriques_scalabilite(self):
        """Sauvegarde les métriques de scalabilité dans l'historique"""
        metriques_actuelles = {
            "timestamp": datetime.now().isoformat(),
            "complexite_globale": self.metriques_complexite.score_complexite_global,
            "nb_temples": self.metriques_complexite.nb_temples,
            "nb_connexions": self.metriques_complexite.nb_connexions,
            "nb_workers_threads": self.config_scalabilite.nb_workers_threads,
            "nb_workers_processes": self.config_scalabilite.nb_workers_processes,
            "efficacite_parallelisation": self.etat.get("efficacite_parallelisation", 0.0),
            "charge_systeme": self.etat.get("charge_systeme", 0.0)
        }
        
        self.historique_scalabilite.append(metriques_actuelles)
        
        # Garder seulement les 50 dernières mesures
        if len(self.historique_scalabilite) > 50:
            self.historique_scalabilite = self.historique_scalabilite[-50:]
    
    def generer_rapport_scalabilite(self) -> Dict[str, Any]:
        """
        📊 Génère un rapport complet de scalabilité
        
        Returns:
            Rapport détaillé de scalabilité
        """
        return {
            "timestamp": datetime.now().isoformat(),
            
            # Configuration actuelle
            "configuration": {
                "nb_workers_threads": self.config_scalabilite.nb_workers_threads,
                "nb_workers_processes": self.config_scalabilite.nb_workers_processes,
                "taille_chunk_optimale": self.config_scalabilite.taille_chunk_optimale,
                "seuil_parallelisation": self.config_scalabilite.seuil_parallelisation,
                "strategie_partitionnement": self.config_scalabilite.strategie_partitionnement,
                "mode_adaptation": self.config_scalabilite.mode_adaptation
            },
            
            # Métriques de complexité
            "complexite": {
                "score_global": self.metriques_complexite.score_complexite_global,
                "nb_temples": self.metriques_complexite.nb_temples,
                "nb_connexions": self.metriques_complexite.nb_connexions,
                "densite_connexions": self.metriques_complexite.densite_connexions,
                "profondeur_max": self.metriques_complexite.profondeur_max,
                "entropie_architecture": self.metriques_complexite.entropie_architecture
            },
            
            # Performance
            "performance": {
                "efficacite_parallelisation": self.etat.get("efficacite_parallelisation", 0.0),
                "charge_systeme": self.etat.get("charge_systeme", 0.0),
                "energie_scalabilite": self.energie_scalabilite.niveau_energie
            },
            
            # Ressources système
            "ressources": {
                "nb_cpu_disponibles": self.nb_cpu_disponibles,
                "memoire_disponible_gb": self.memoire_disponible_gb,
                "cpu_utilise_percent": psutil.cpu_percent(),
                "memoire_utilisee_percent": psutil.virtual_memory().percent
            },
            
            # Historique (résumé)
            "historique_resume": {
                "nb_mesures": len(self.historique_scalabilite),
                "efficacite_moyenne": sum(m.get("efficacite_parallelisation", 0) for m in self.historique_scalabilite[-10:]) / min(10, len(self.historique_scalabilite)) if self.historique_scalabilite else 0.0
            }
        }
    
    def __del__(self):
        """Nettoyage lors de la destruction"""
        try:
            if hasattr(self, 'thread_pool') and self.thread_pool:
                self.thread_pool.shutdown(wait=False)
            if hasattr(self, 'process_pool') and self.process_pool:
                self.process_pool.shutdown(wait=False)
        except:
            pass