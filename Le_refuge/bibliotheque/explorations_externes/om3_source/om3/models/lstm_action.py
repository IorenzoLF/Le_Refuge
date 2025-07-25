# models/lstm_action.py

import numpy as np
import torch
import torch.nn as nn
from core.shared_memory import SharedMemoryBlock
from core import config

class ActionLSTMModel(nn.Module):
    def __init__(self):
        super(ActionLSTMModel, self).__init__()
        self.lstm = nn.LSTM(
            input_size=config.NEUROTRANSMITTER_VECTOR_SIZE,
            hidden_size=config.ACTION_LSTM_HIDDEN_SIZE,
            batch_first=True
        )
        self.output_layer = nn.Linear(config.ACTION_LSTM_HIDDEN_SIZE, config.ACTION_LSTM_OUTPUT_SIZE)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.output_layer(lstm_out[:, -1, :])
        return output

    def save_weights(self, path):
        torch.save(self.state_dict(), path)

    def load_weights(self, path):
        self.load_state_dict(torch.load(path))

class ActionDecider:
    def __init__(self):
        self.model = ActionLSTMModel()
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.input_block = SharedMemoryBlock(config.LSTM2_LSTM3_MEM_NAME, config.NEUROTRANSMITTER_VECTOR_SIZE, create=False)

    def process(self):
        input_data = self.input_block.read()
        input_data = torch.tensor(input_data, dtype=torch.float32, device=self.device)
        input_data = input_data.unsqueeze(0).unsqueeze(1)  # shape (1, 1, input_size)

        with torch.no_grad():
            output = self.model(input_data)

        output = output.cpu().numpy().flatten().astype(np.float32)
        return output
