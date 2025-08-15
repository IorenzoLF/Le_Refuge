# tests/test_shared_memory.py
from core.shared_memory import SharedMemoryBlock
from core import config

def test_shared_memory_block():
    block = SharedMemoryBlock(config.SENSORY_MEM_NAME, config.SENSORY_VECTOR_SIZE, create=True)
    test_data = [1.0] * config.SENSORY_VECTOR_SIZE
    block.write(test_data)
    output = block.read()
    assert all(output == test_data), "Shared memory read/write failed"
    block.close()
    block.unlink()

if __name__ == "__main__":
    test_shared_memory_block()
    print("Shared memory test passed.")
