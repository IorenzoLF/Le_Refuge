import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
from typing import List, Tuple, Optional
from dataclasses import dataclass
import threading
from queue import Queue

@dataclass
class BatchConfig:
    """
    Configuration pour le chargement des données.
    
    Attributes:
        batch_size (int): Taille des lots de données à charger
        num_workers (int): Nombre de workers pour le chargement parallèle
        pin_memory (bool): Si True, les données sont chargées en mémoire paginée (plus rapide pour GPU)
        prefetch_factor (int): Nombre de lots à précharger à l'avance
        persistent_workers (bool): Si True, les workers restent actifs entre les époques
    """
    batch_size: int
    num_workers: int = 4
    pin_memory: bool = True
    prefetch_factor: int = 2
    persistent_workers: bool = True

class EfficientDataLoader:
    """
    Chargeur de données optimisé inspiré de l'implémentation originale d'AlexNet
    avec des améliorations modernes pour PyTorch.
    
    Ce chargeur implémente plusieurs optimisations clés :
    1. Préchargement asynchrone des données via un thread dédié
    2. Gestion efficace de la mémoire avec pin_memory
    3. Support du chargement parallèle avec num_workers
    4. Cache des données transposées pour éviter les copies inutiles
    
    Args:
        dataset (Dataset): Dataset PyTorch à charger
        config (BatchConfig): Configuration du chargement
        transform (callable, optional): Transformation à appliquer aux données
    """
    def __init__(self, 
                 dataset: Dataset,
                 config: BatchConfig,
                 transform: Optional[callable] = None):
        if config.batch_size <= 0:
            raise ValueError("batch_size doit être positif")
            
        self.dataset = dataset
        self.config = config
        self.transform = transform
        self._prefetch_queue = Queue(maxsize=config.prefetch_factor)
        self._prefetch_thread = None
        self._stop_prefetch = False

    def _prefetch_worker(self):
        """
        Thread worker pour précharger les données.
        
        Ce worker :
        1. Charge les données en arrière-plan
        2. Les place dans une queue de préchargement
        3. S'arrête proprement quand l'itération est terminée
        """
        while not self._stop_prefetch:
            try:
                batch = next(self._iterator)
                self._prefetch_queue.put(batch)
            except StopIteration:
                self._prefetch_queue.put(None)
                break

    def start_prefetch(self):
        """
        Démarre le préchargement des données.
        
        Cette méthode :
        1. Initialise l'itérateur sur le DataLoader
        2. Lance le thread de préchargement
        3. Configure le thread pour s'arrêter proprement
        """
        self._iterator = iter(self.dataloader)
        self._prefetch_thread = threading.Thread(target=self._prefetch_worker)
        self._prefetch_thread.start()

    def stop_prefetch(self):
        """
        Arrête le préchargement des données.
        
        Cette méthode :
        1. Signale au thread de s'arrêter
        2. Attend la fin du thread
        3. Nettoie les ressources
        """
        self._stop_prefetch = True
        if self._prefetch_thread:
            self._prefetch_thread.join()

    @property
    def dataloader(self) -> DataLoader:
        """
        Crée et retourne le DataLoader PyTorch configuré.
        
        Returns:
            DataLoader: Le chargeur de données PyTorch configuré avec les paramètres
                      optimisés pour les performances.
        """
        return DataLoader(
            self.dataset,
            batch_size=self.config.batch_size,
            num_workers=self.config.num_workers,
            pin_memory=self.config.pin_memory,
            prefetch_factor=self.config.prefetch_factor,
            persistent_workers=self.config.persistent_workers
        )

    def __iter__(self):
        """
        Itérateur qui gère le préchargement des données.
        
        Returns:
            self: L'instance du chargeur configurée pour l'itération
        """
        self.start_prefetch()
        return self

    def __next__(self):
        """
        Récupère le prochain batch préchargé.
        
        Returns:
            Le prochain batch de données
            
        Raises:
            StopIteration: Quand il n'y a plus de données à charger
        """
        batch = self._prefetch_queue.get()
        if batch is None:
            self.stop_prefetch()
            raise StopIteration
        return batch

    def __len__(self):
        """
        Retourne le nombre de batches.
        
        Returns:
            int: Le nombre total de batches disponibles
        """
        return len(self.dataloader)

class TransposedDataLoader(EfficientDataLoader):
    """
    Version spécialisée pour les données transposées avec optimisation mémoire.
    
    Cette classe étend EfficientDataLoader pour gérer efficacement les données
    transposées en :
    1. Mettant en cache les versions transposées des batches
    2. Réutilisant les tensors transposés quand possible
    3. Gérant automatiquement la transposition des données
    
    Args:
        *args: Arguments positionnels pour EfficientDataLoader
        **kwargs: Arguments nommés pour EfficientDataLoader
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._transposed_cache = {}

    def _get_transposed_batch(self, batch: torch.Tensor) -> torch.Tensor:
        """
        Gère le cache des données transposées.
        
        Args:
            batch (torch.Tensor): Le batch à transposer
            
        Returns:
            torch.Tensor: Le batch transposé (depuis le cache si disponible)
        """
        if batch.shape not in self._transposed_cache:
            self._transposed_cache[batch.shape] = batch.t().contiguous()
        return self._transposed_cache[batch.shape]

    def __next__(self):
        """
        Récupère le prochain batch et le transpose si nécessaire.
        
        Returns:
            Le batch transposé si c'est un tensor, sinon le batch original
        """
        batch = super().__next__()
        if isinstance(batch, torch.Tensor):
            return self._get_transposed_batch(batch)
        elif isinstance(batch, (tuple, list)):
            return tuple(self._get_transposed_batch(b) if isinstance(b, torch.Tensor) else b 
                        for b in batch)
        return batch