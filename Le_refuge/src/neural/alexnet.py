"""
Implementation of AlexNet architecture.
Original paper: https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
"""

import torch
import torch.nn as nn

class AlexNet(nn.Module):
    """
    AlexNet architecture implémentée en PyTorch.
    Architecture originale :
    - 5 couches convolutionnelles
    - 3 couches fully connected
    - ReLU activations
    - Local Response Normalization
    - Max Pooling
    - Dropout
    """
    
    def __init__(self, num_classes: int = 1000):
        super(AlexNet, self).__init__()
        
        # Première couche convolutionnelle
        self.features = nn.Sequential(
            # Conv1
            nn.Conv2d(3, 96, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=2),
            nn.MaxPool2d(kernel_size=3, stride=2),
            
            # Conv2
            nn.Conv2d(96, 256, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=2),
            nn.MaxPool2d(kernel_size=3, stride=2),
            
            # Conv3
            nn.Conv2d(256, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            
            # Conv4
            nn.Conv2d(384, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            
            # Conv5
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        
        # Couches fully connected
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            
            nn.Dropout(p=0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            
            nn.Linear(4096, num_classes),
        )
        
        # Initialisation des poids
        self._initialize_weights()
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass du réseau.
        
        Args:
            x: Tensor d'entrée de taille (batch_size, 3, 224, 224)
            
        Returns:
            Tensor de sortie de taille (batch_size, num_classes)
        """
        x = self.features(x)
        x = torch.flatten(x, 1)  # Aplatir toutes les dimensions sauf le batch
        x = self.classifier(x)
        return x
    
    def _initialize_weights(self):
        """
        Initialisation des poids selon la méthode décrite dans le papier.
        """
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.normal_(m.weight, mean=0, std=0.01)
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, mean=0, std=0.01)
                nn.init.constant_(m.bias, 0) 