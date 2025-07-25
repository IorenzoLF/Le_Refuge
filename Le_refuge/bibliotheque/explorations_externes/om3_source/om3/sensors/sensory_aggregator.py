# sensors/sensory_aggregator.py

import numpy as np
from sensors.text_sensor import TextSensor
from sensors.audio_sensor import AudioSensor
from sensors.vision_sensor import VisionSensor
from sensors.system_sensor import SystemSensor
from sensors.action_feedback_sensor import ActionFeedbackSensor
from core.shared_memory import SharedMemoryBlock
from core import config

class SensoryAggregator:
    def __init__(self):
        self.text_sensor = TextSensor()
        self.audio_sensor = AudioSensor()
        self.vision_sensor = VisionSensor()
        self.system_sensor = SystemSensor()
        self.action_sensor = ActionFeedbackSensor()

        self.shared_memory = SharedMemoryBlock(
            name=config.SENSORY_MEM_NAME,
            size=config.SENSORY_VECTOR_SIZE,
            create=False  # assume engine already created block
        )

    def collect_and_write(self, text_input: str, audio_input: np.ndarray, image_input: np.ndarray):
        """
        Aggregate all sensory inputs + write to shared memory block.
        """
        vectors = []

        vectors.append(self.text_sensor.get_text_vector(text_input))
        vectors.append(self.audio_sensor.get_audio_vector(audio_input))
        vectors.append(self.vision_sensor.get_vision_vector(image_input))
        vectors.append(self.system_sensor.get_system_vector())
        vectors.append(self.action_sensor.get_action_feedback_vector())

        combined = np.concatenate(vectors)

        # Pad or truncate to SENSORY_VECTOR_SIZE
        combined = combined[:config.SENSORY_VECTOR_SIZE]
        if combined.size < config.SENSORY_VECTOR_SIZE:
            padding = np.zeros(config.SENSORY_VECTOR_SIZE - combined.size, dtype=np.float32)
            combined = np.concatenate([combined, padding])

        self.shared_memory.write(combined)

        return combined
if __name__ == "__main__":
    dummy_audio = np.random.randn(16000).astype(np.float32)
    dummy_image = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)
    aggregator = SensoryAggregator()
    vec = aggregator.collect_and_write("Test OM3", dummy_audio, dummy_image)
    print(vec.shape)  # (512,)
    print(vec.dtype)  # float32
