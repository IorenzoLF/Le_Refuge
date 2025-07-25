# sensors/vision_sensor.py

import torch
import torch.nn as nn
import numpy as np
from core import config

class VisionCNNEncoder(nn.Module):
    def __init__(self):
        super(VisionCNNEncoder, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, config.VISION_VECTOR_SIZE))
        )

    def forward(self, x):
        return self.features(x)

class VisionSensor:
    def __init__(self):
        self.model = VisionCNNEncoder()
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def get_vision_vector(self, image: np.ndarray) -> np.ndarray:
        """
        Convert image (H, W, 3) numpy array to feature vector.
        """
        # Normalize image to 0-1
        image = image.astype(np.float32) / 255.0
        image = torch.tensor(image).permute(2, 0, 1).unsqueeze(0).to(self.device)  # (1, 3, H, W)

        with torch.no_grad():
            features = self.model(image)
        
        vector = features.cpu().numpy().flatten()
        return vector.astype(np.float32)
if __name__ == "__main__":
    sensor = VisionSensor()
    dummy_img = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)  # simulate image
    vec = sensor.get_vision_vector(dummy_img)
    print(vec.shape)  # should be (64,)
    print(vec.dtype)  # float32
