# sensors/system_sensor.py

import numpy as np
import psutil
import time
from collections import deque
from core import config

class SystemSensor:
    def __init__(self, click_buffer_size=5):
        self.vector_size = config.SYSTEM_VECTOR_SIZE
        self.click_buffer_size = click_buffer_size
        self.click_timestamps = deque(maxlen=click_buffer_size)
        self._start_mouse_listener()

    def _start_mouse_listener(self):
        try:
            from pynput import mouse
            def on_click(x, y, button, pressed):
                if pressed:
                    self.click_timestamps.append(time.time())
            listener = mouse.Listener(on_click=on_click)
            listener.daemon = True
            listener.start()
        except Exception:
            pass  # fail silently if listener cannot start

    def get_system_vector(self) -> np.ndarray:
        features = []

        # System usage
        features.append(psutil.cpu_percent() / 100)
        features.append(psutil.virtual_memory().percent / 100)
        features.append(psutil.disk_usage('/').percent / 100)

        # Mouse position + buttons
        try:
            import pyautogui
            from pynput import mouse

            screen_width, screen_height = pyautogui.size()
            x, y = pyautogui.position()
            features.append(x / screen_width)
            features.append(y / screen_height)

            mouse_controller = mouse.Controller()
            pressed = mouse_controller.pressed_buttons
            features.append(1.0 if mouse.Button.left in pressed else 0.0)
            features.append(1.0 if mouse.Button.right in pressed else 0.0)
            features.append(1.0 if mouse.Button.middle in pressed else 0.0)
        except Exception:
            features.extend([0, 0, 0, 0, 0])

        # Add click timestamps (normalized)
        normalized_timestamps = [(ts / 1e10) for ts in list(self.click_timestamps)]
        features.extend(normalized_timestamps)

        # Pad or truncate
        features = features[:self.vector_size]
        padded = np.zeros(self.vector_size, dtype=np.float32)
        padded[:len(features)] = np.array(features, dtype=np.float32)

        return padded

if __name__ == "__main__":
    sensor = SystemSensor()
    vec = sensor.get_system_vector()
    print(vec.shape)
    print(vec.dtype)
    print(vec)
