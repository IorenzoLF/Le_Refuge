# core/shared_memory.py
import numpy as np
from multiprocessing import shared_memory
from core import config

class SharedMemoryBlock:
    def __init__(self, name, size, create=False):
        self.name = name
        self.size = size
        self.dtype = np.float32
        self.nbytes = size * np.dtype(self.dtype).itemsize

        if create:
            self.shm = shared_memory.SharedMemory(name=name, create=True, size=self.nbytes)
        else:
            self.shm = shared_memory.SharedMemory(name=name)

        self.array = np.ndarray((size,), dtype=self.dtype, buffer=self.shm.buf)

    def write(self, data):
        if len(data) != self.size:
            raise ValueError(f"Data length mismatch: expected {self.size}, got {len(data)}")
        self.array[:] = data

    def read(self):
        return self.array.copy()

    def close(self):
        self.shm.close()

    def unlink(self):
        self.shm.unlink()
