# tests/create_om3_sensory_block.py

from core.shared_memory import SharedMemoryBlock
from core import config

block = SharedMemoryBlock(
    name=config.SENSORY_MEM_NAME,
    size=config.SENSORY_VECTOR_SIZE,
    create=True
)
block.close()
