# models/action_encoder.py

import numpy as np
from core import config
from core.shared_memory import SharedMemoryBlock

# Your action vocabulary must match what environment + encoder expects
ACTION_TOKEN_MAP = [
    "IDLE",
    "MOUSE_MOVE_UP",
    "MOUSE_MOVE_DOWN",
    "MOUSE_MOVE_LEFT",
    "MOUSE_MOVE_RIGHT",
    "LEFT_CLICK",
    "RIGHT_CLICK",
    "MOUSE_SCROLL_UP",
    "MOUSE_SCROLL_DOWN",
    "KEY_PRESS_A",
    "KEY_PRESS_B",
    "KEY_PRESS_C",
    "KEY_PRESS_D",
    "KEY_PRESS_E",
    "KEY_PRESS_F",
    "KEY_PRESS_G",
    "KEY_PRESS_H",
    "KEY_PRESS_I",
    "KEY_PRESS_J",
    "KEY_PRESS_K"
]

class ActionEncoder:
    def __init__(self):
        self.vocab = ACTION_TOKEN_MAP
        self.num_tokens = len(self.vocab)

        # Shared memory for feedback loop
        self.shared_memory = SharedMemoryBlock(
            name=config.ACTION_FEEDBACK_MEM_NAME,
            size=config.ACTION_FEEDBACK_VECTOR_SIZE,
            create=False
        )

    def encode(self, action_vector: np.ndarray) -> list:
        """
        Map action vector values to symbolic action tokens,
        AND write numeric version to action_feedback shared memory.
        """
        # Normalize vector to 0-1 range
        min_val = action_vector.min()
        max_val = action_vector.max()
        if max_val - min_val > 1e-6:
            normalized = (action_vector - min_val) / (max_val - min_val)
        else:
            normalized = np.zeros_like(action_vector)

        # Select active token indices
        active_indices = np.where(normalized > 0.5)[0]
        tokens = []

        for idx in active_indices:
            token_idx = idx % self.num_tokens
            tokens.append(self.vocab[token_idx])

        if not tokens:
            tokens.append("IDLE")

        # Create feedback vector for last actions
        # Simple: one-hot style → 1 if token active else 0
        feedback_vector = np.zeros(config.ACTION_FEEDBACK_VECTOR_SIZE, dtype=np.float32)

        for token in tokens:
            if token in self.vocab:
                idx = self.vocab.index(token)
                if idx < config.ACTION_FEEDBACK_VECTOR_SIZE:
                    feedback_vector[idx] = 1.0

        self.shared_memory.write(feedback_vector)

        return tokens

if __name__ == "__main__":
    encoder = ActionEncoder()
    dummy_vector = np.random.rand(config.ACTION_VECTOR_SIZE).astype(np.float32)
    tokens = encoder.encode(dummy_vector)
    print(tokens)
