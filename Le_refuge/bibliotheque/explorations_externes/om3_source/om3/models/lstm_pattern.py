# models/lstm_pattern.py

import numpy as np
import torch
import torch.nn as nn
from core.shared_memory import SharedMemoryBlock
from core import config

class PatternLSTMModel(nn.Module):
    def __init__(self):
        super(PatternLSTMModel, self).__init__()
        self.lstm = nn.LSTM(
            input_size=config.SENSORY_VECTOR_SIZE,
            hidden_size=config.PATTERN_LSTM_HIDDEN_SIZE,
            batch_first=True
        )
        self.output_layer = nn.Linear(config.PATTERN_LSTM_HIDDEN_SIZE, config.PATTERN_LSTM_OUTPUT_SIZE)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.output_layer(lstm_out[:, -1, :])  # last time step
        return output

    def save_weights(self, path):
        torch.save(self.state_dict(), path)

    def load_weights(self, path):
        self.load_state_dict(torch.load(path))

class PatternRecognizer:
    def __init__(self):
        self.model = PatternLSTMModel()
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.sensory_block = SharedMemoryBlock(config.SENSORY_MEM_NAME, config.SENSORY_VECTOR_SIZE, create=False)
        self.output_block = SharedMemoryBlock(config.LSTM1_LSTM2_MEM_NAME, config.PATTERN_VECTOR_SIZE, create=False)

    def process(self):
        sensory_input = self.sensory_block.read()
        sensory_input = torch.tensor(sensory_input, dtype=torch.float32, device=self.device)
        sensory_input = sensory_input.unsqueeze(0).unsqueeze(1)  # shape (1, 1, sensory_size)

        with torch.no_grad():
            pattern_output = self.model(sensory_input)

        pattern_output = pattern_output.cpu().numpy().flatten().astype(np.float32)
        self.output_block.write(pattern_output)
        return pattern_output
