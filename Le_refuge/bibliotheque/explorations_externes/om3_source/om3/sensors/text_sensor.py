# sensors/text_sensor.py

from transformers import AutoTokenizer
import numpy as np
from core import config

class TextSensor:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.vector_size = config.TEXT_VECTOR_SIZE

    def get_text_vector(self, text: str) -> np.ndarray:
        """
        Convert text input to fixed-size float vector.
        """
        # Tokenize
        tokens = self.tokenizer.encode(text, add_special_tokens=True)

        # Convert to numpy and pad/truncate
        tokens = tokens[:self.vector_size]
        padded = np.zeros(self.vector_size, dtype=np.float32)
        padded[:len(tokens)] = np.array(tokens, dtype=np.float32)

        return padded
