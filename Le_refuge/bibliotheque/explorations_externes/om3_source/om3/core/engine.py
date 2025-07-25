# core/engine.py

import numpy as np
import os
from core.shared_memory import SharedMemoryBlock
from core import config
from sensors.sensory_aggregator import SensoryAggregator
from models.lstm_pattern import PatternRecognizer
from models.lstm_neurotransmitter import NeurotransmitterActivator
from models.lstm_action import ActionDecider
from models.action_encoder import ActionEncoder
from interfaces.environment_api import OM3Environment

class OM3Engine:
    def __init__(self):
        os.makedirs("checkpoints", exist_ok=True)

        # Age system
        self.age_file = "checkpoints/om3_age.txt"
        try:
            with open(self.age_file, "r") as f:
                self.total_cycles = int(f.read())
        except:
            self.total_cycles = 0

        # Shared memory (INCLUDING action feedback block)
        self.sensory_block = SharedMemoryBlock(config.SENSORY_MEM_NAME, config.SENSORY_VECTOR_SIZE, create=True)
        self.lstm1_block = SharedMemoryBlock(config.LSTM1_LSTM2_MEM_NAME, config.PATTERN_VECTOR_SIZE, create=True)
        self.lstm2_block = SharedMemoryBlock(config.LSTM2_LSTM3_MEM_NAME, config.NEUROTRANSMITTER_VECTOR_SIZE, create=True)
        self.action_feedback_block = SharedMemoryBlock(config.ACTION_FEEDBACK_MEM_NAME, config.ACTION_FEEDBACK_VECTOR_SIZE, create=True)

        # Modules
        self.sensors = SensoryAggregator()
        self.lstm1 = PatternRecognizer()
        self.lstm2 = NeurotransmitterActivator()
        self.lstm3 = ActionDecider()
        self.action_encoder = ActionEncoder()
        self.environment = OM3Environment()

        # Checkpoints
        try:
            self.lstm1.model.load_weights("checkpoints/lstm1.pth")
        except:
            pass
        try:
            self.lstm2.model.load_weights("checkpoints/lstm2.pth")
        except:
            pass
        try:
            self.lstm3.model.load_weights("checkpoints/lstm3.pth")
        except:
            pass

    def run(self, cycles=None, checkpoint_interval=5):
        step = 0
        while True if cycles is None else step < cycles:
            step += 1
            self.total_cycles += 1
            print(f"Cycle {step} | OM3 Age: {self.total_cycles}")

            dummy_audio = np.random.randn(16000).astype(np.float32)
            dummy_image = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)
            self.sensors.collect_and_write("OM3 test cycle", dummy_audio, dummy_image)

            pattern_vector = self.lstm1.process()
            neurotransmitter_vector = self.lstm2.process()
            action_vector = self.lstm3.process()

            print(f"Action vector: {action_vector}")

            action_tokens = self.action_encoder.encode(action_vector)
            self.environment.apply_actions(action_tokens)
            self.environment.update()

            if not self.environment.is_running():
                break

            if step % checkpoint_interval == 0:
                self.lstm1.model.save_weights("checkpoints/lstm1.pth")
                self.lstm2.model.save_weights("checkpoints/lstm2.pth")
                self.lstm3.model.save_weights("checkpoints/lstm3.pth")
                print(f"Checkpoint saved at cycle {step}")

        # Save age at shutdown
        with open(self.age_file, "w") as f:
            f.write(str(self.total_cycles))

        self.environment.close()
        print(f"OM3 engine cycle complete. Final Age: {self.total_cycles}")
