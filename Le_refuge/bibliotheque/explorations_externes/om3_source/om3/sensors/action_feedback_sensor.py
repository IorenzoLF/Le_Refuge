# sensors/action_feedback_sensor.py

import numpy as np
from core.shared_memory import SharedMemoryBlock
from core import config

class ActionFeedbackSensor:
    def __init__(self):
        self.vector_size = config.ACTION_FEEDBACK_VECTOR_SIZE
        self.shared_memory = SharedMemoryBlock(
            name=config.ACTION_FEEDBACK_MEM_NAME,
            size=self.vector_size,
            create=False
        )

    def get_action_feedback_vector(self) -> np.ndarray:
        """
        Reads last action tokens from shared memory as float vector.
        """
        feedback_vector = self.shared_memory.read()
        return feedback_vector

if __name__ == "__main__":
    sensor = ActionFeedbackSensor()
    vec = sensor.get_action_feedback_vector()
    print(vec.shape)  # should be (config.ACTION_FEEDBACK_VECTOR_SIZE,)
    print(vec.dtype)  # float32
