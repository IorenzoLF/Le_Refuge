# tests/test_model_pipeline.py

import numpy as np
from core.shared_memory import SharedMemoryBlock
from core import config
from models.lstm_pattern import PatternRecognizer
from models.lstm_neurotransmitter import NeurotransmitterActivator
from models.lstm_action import ActionDecider
from models.action_encoder import ActionEncoder

def test_model_pipeline():
    # Create all shared memory blocks
    sensory_block = SharedMemoryBlock(config.SENSORY_MEM_NAME, config.SENSORY_VECTOR_SIZE, create=True)
    sensory_block.write(np.random.rand(config.SENSORY_VECTOR_SIZE).astype(np.float32))

    lstm1_block = SharedMemoryBlock(config.LSTM1_LSTM2_MEM_NAME, config.PATTERN_VECTOR_SIZE, create=True)
    lstm2_block = SharedMemoryBlock(config.LSTM2_LSTM3_MEM_NAME, config.NEUROTRANSMITTER_VECTOR_SIZE, create=True)

    # Initialize models
    pattern_recognizer = PatternRecognizer()
    neurotransmitter_activator = NeurotransmitterActivator()
    action_decider = ActionDecider()
    action_encoder = ActionEncoder()

    # Run model chain
    pattern_output = pattern_recognizer.process()
    print(f"LSTM-1 output shape: {pattern_output.shape}")

    neurotransmitter_output = neurotransmitter_activator.process()
    print(f"LSTM-2 output shape: {neurotransmitter_output.shape}")

    action_vector = action_decider.process()
    print(f"LSTM-3 output shape: {action_vector.shape}")

    tokens = action_encoder.encode(action_vector)
    print(f"Action tokens: {tokens}")

    # Clean up
    sensory_block.close(); sensory_block.unlink()
    lstm1_block.close(); lstm1_block.unlink()
    lstm2_block.close(); lstm2_block.unlink()

if __name__ == "__main__":
    test_model_pipeline()
