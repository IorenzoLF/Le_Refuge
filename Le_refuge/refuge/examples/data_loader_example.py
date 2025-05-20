import torch
from torch.utils.data import Dataset
from data_loader import EfficientDataLoader, BatchConfig, TransposedDataLoader
import numpy as np

class SimpleDataset(Dataset):
    """Dataset simple pour démonstration"""
    def __init__(self, size=1000, dim=224):
        self.data = torch.randn(size, 3, dim, dim)
        self.labels = torch.randint(0, 1000, (size,))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

def main():
    # Configuration du chargeur
    config = BatchConfig(
        batch_size=32,
        num_workers=4,
        pin_memory=True,
        prefetch_factor=2
    )

    # Création du dataset
    dataset = SimpleDataset()

    # Utilisation du chargeur standard
    print("Test du chargeur standard:")
    loader = EfficientDataLoader(dataset, config)
    for i, (data, labels) in enumerate(loader):
        print(f"Batch {i}: données shape={data.shape}, labels shape={labels.shape}")
        if i >= 2:  # Test avec 3 batches
            break

    # Utilisation du chargeur transposé
    print("\nTest du chargeur transposé:")
    transposed_loader = TransposedDataLoader(dataset, config)
    for i, (data, labels) in enumerate(transposed_loader):
        print(f"Batch {i}: données shape={data.shape}, labels shape={labels.shape}")
        if i >= 2:  # Test avec 3 batches
            break

if __name__ == "__main__":
    main() 