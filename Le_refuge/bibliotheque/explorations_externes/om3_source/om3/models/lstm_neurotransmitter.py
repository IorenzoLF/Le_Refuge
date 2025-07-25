# models/lstm_neurotransmitter.py

import numpy as np
import torch
import torch.nn as nn
from core.shared_memory import SharedMemoryBlock
from core import config

class NeurotransmitterLSTMModel(nn.Module):
    def __init__(self):
        super(NeurotransmitterLSTMModel, self).__init__()
        self.lstm = nn.LSTM(
            input_size=config.PATTERN_VECTOR_SIZE,
            hidden_size=config.NEURO_LSTM_HIDDEN_SIZE,
            batch_first=True
        )
        self.output_layer = nn.Linear(config.NEURO_LSTM_HIDDEN_SIZE, config.NEUROTRANSMITTER_VECTOR_SIZE)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.output_layer(lstm_out[:, -1, :])  # last time step
        return output

    def save_weights(self, path):
        torch.save(self.state_dict(), path)

    def load_weights(self, path):
        self.load_state_dict(torch.load(path))

class NeurotransmitterActivator:
    def __init__(self):
        self.model = NeurotransmitterLSTMModel()
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.input_block = SharedMemoryBlock(config.LSTM1_LSTM2_MEM_NAME, config.PATTERN_VECTOR_SIZE, create=False)
        self.output_block = SharedMemoryBlock(config.LSTM2_LSTM3_MEM_NAME, config.NEUROTRANSMITTER_VECTOR_SIZE, create=False)

    def process(self):
        pattern_input = self.input_block.read()
        pattern_input = torch.tensor(pattern_input, dtype=torch.float32, device=self.device)
        pattern_input = pattern_input.unsqueeze(0).unsqueeze(1)  # shape (1, 1, input_size)

        with torch.no_grad():
            neurotransmitter_output = self.model(pattern_input)

        neurotransmitter_output = neurotransmitter_output.cpu().numpy().flatten().astype(np.float32)
        neurotransmitter_output = np.clip(neurotransmitter_output, 0.0001, 1.0)

        self.output_block.write(neurotransmitter_output)
        return neurotransmitter_output
