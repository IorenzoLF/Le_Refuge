import unittest
import torch
import time
import psutil
import numpy as np
from ..data_loader import EfficientDataLoader, BatchConfig, TransposedDataLoader
from torch.utils.data import Dataset

class TestDataset(Dataset):
    """Dataset de test avec différentes tailles et types de données"""
    def __init__(self, size=1000, dim=224, data_type='float32'):
        self.size = size
        self.dim = dim
        self.data_type = data_type
        
        if data_type == 'float32':
            self.data = torch.randn(size, 3, dim, dim, dtype=torch.float32)
        else:
            self.data = torch.randint(0, 255, (size, 3, dim, dim), dtype=torch.uint8)
            
        self.labels = torch.randint(0, 1000, (size,))

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

class TestDataLoader(unittest.TestCase):
    """Tests complets pour le chargeur de données"""
    
    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.process = psutil.Process()
        self.initial_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        
    def tearDown(self):
        """Nettoyage après chaque test"""
        final_memory = self.process.memory_info().rss / 1024 / 1024
        print(f"\nUtilisation mémoire: {final_memory - self.initial_memory:.2f} MB")
        
    def test_basic_functionality(self):
        """Test des fonctionnalités de base"""
        config = BatchConfig(batch_size=32)
        dataset = TestDataset(size=100)
        loader = EfficientDataLoader(dataset, config)
        
        # Test de l'itération
        batches = list(loader)
        self.assertEqual(len(batches), 4)  # 100/32 = 4 batches
        
        # Test des shapes
        data, labels = batches[0]
        self.assertEqual(data.shape, (32, 3, 224, 224))
        self.assertEqual(labels.shape, (32,))
        
    def test_memory_efficiency(self):
        """Test de l'efficacité mémoire"""
        config = BatchConfig(batch_size=32)
        dataset = TestDataset(size=1000)
        
        # Test avec le chargeur standard
        start_time = time.time()
        loader = EfficientDataLoader(dataset, config)
        for _ in loader:
            pass
        standard_time = time.time() - start_time
        
        # Test avec le chargeur transposé
        start_time = time.time()
        transposed_loader = TransposedDataLoader(dataset, config)
        for _ in transposed_loader:
            pass
        transposed_time = time.time() - start_time
        
        print(f"\nTemps standard: {standard_time:.2f}s")
        print(f"Temps transposé: {transposed_time:.2f}s")
        
    def test_different_data_types(self):
        """Test avec différents types de données"""
        config = BatchConfig(batch_size=32)
        
        # Test avec float32
        dataset_float = TestDataset(size=100, data_type='float32')
        loader_float = EfficientDataLoader(dataset_float, config)
        data_float, _ = next(iter(loader_float))
        self.assertEqual(data_float.dtype, torch.float32)
        
        # Test avec uint8
        dataset_uint8 = TestDataset(size=100, data_type='uint8')
        loader_uint8 = EfficientDataLoader(dataset_uint8, config)
        data_uint8, _ = next(iter(loader_uint8))
        self.assertEqual(data_uint8.dtype, torch.uint8)
        
    def test_prefetch_behavior(self):
        """Test du comportement du préchargement"""
        config = BatchConfig(batch_size=32, prefetch_factor=2)
        dataset = TestDataset(size=100)
        loader = EfficientDataLoader(dataset, config)
        
        # Vérification que le préchargement fonctionne
        iterator = iter(loader)
        first_batch = next(iterator)
        self.assertIsNotNone(first_batch)
        
        # Vérification de la queue de préchargement
        self.assertLessEqual(loader._prefetch_queue.qsize(), config.prefetch_factor)
        
    def test_error_handling(self):
        """Test de la gestion des erreurs"""
        config = BatchConfig(batch_size=32)
        dataset = TestDataset(size=100)
        loader = EfficientDataLoader(dataset, config)
        
        # Test avec un batch size invalide
        with self.assertRaises(ValueError):
            BatchConfig(batch_size=0)
            
        # Test avec un dataset vide
        empty_dataset = TestDataset(size=0)
        empty_loader = EfficientDataLoader(empty_dataset, config)
        self.assertEqual(len(empty_loader), 0)

if __name__ == '__main__':
    unittest.main() 