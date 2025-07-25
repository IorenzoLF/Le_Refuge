# sensors/audio_sensor.py

import torch
import torch.nn as nn
import numpy as np
from core import config

class AudioCNNEncoder(nn.Module):
    def __init__(self):
        super(AudioCNNEncoder, self).__init__()
        self.features = nn.Sequential(
            nn.Conv1d(1, 16, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv1d(16, 32, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(config.AUDIO_VECTOR_SIZE)
        )

    def forward(self, x):
        return self.features(x)

class AudioSensor:
    def __init__(self):
        self.model = AudioCNNEncoder()
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def get_audio_vector(self, waveform: np.ndarray) -> np.ndarray:
        """
        Convert raw waveform (1D numpy array) to feature vector.
        """
        # Normalize waveform
        waveform = (waveform - np.mean(waveform)) / (np.std(waveform) + 1e-6)

        # Prepare tensor
        waveform = waveform.astype(np.float32)
        waveform = torch.tensor(waveform).unsqueeze(0).unsqueeze(0).to(self.device)  # shape (1, 1, N)

        with torch.no_grad():
            features = self.model(waveform)
        
        vector = features.cpu().numpy().flatten()
        return vector.astype(np.float32)

if __name__ == "__main__":
    sensor = AudioSensor()
    dummy_wave = np.random.randn(16000).astype(np.float32)  # simulate 1 second audio at 16kHz
    vec = sensor.get_audio_vector(dummy_wave)
    print(vec.shape)  # should be (64,)
    print(vec.dtype)  # float32
