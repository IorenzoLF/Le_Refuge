# core/config.py

SENSORY_VECTOR_SIZE = 512
AUDIO_VECTOR_SIZE = 64  # recommend size for audio feature vector
VISION_VECTOR_SIZE = 64  # recommend size for vision feature vector
SYSTEM_VECTOR_SIZE = 64  # recommend size for system state feature vector
ACTION_FEEDBACK_VECTOR_SIZE = 64  # recommend size for action feedback vector
PATTERN_VECTOR_SIZE = 128   
PATTERN_LSTM_HIDDEN_SIZE = 256
PATTERN_LSTM_OUTPUT_SIZE = PATTERN_VECTOR_SIZE  # use local variable, not config.PATTERN_VECTOR_SIZE

ACTION_FEEDBACK_MEM_NAME = "om3_action_feedback"

ACTION_VECTOR_SIZE = 32  # recommended starting size (adjust later if needed)

ACTION_LSTM_HIDDEN_SIZE = 256
ACTION_LSTM_OUTPUT_SIZE = ACTION_VECTOR_SIZE


PATTERN_VECTOR_SIZE = 128
NEURO_LSTM_HIDDEN_SIZE = 256
NEUROTRANSMITTER_VECTOR_SIZE = 100
NEURO_LSTM_OUTPUT_SIZE = NEUROTRANSMITTER_VECTOR_SIZE

TEXT_VECTOR_SIZE = 128  # for sensors/text_sensor.py

# Shared memory keys
SENSORY_MEM_NAME = 'om3_sensory'
LSTM1_LSTM2_MEM_NAME = 'om3_lstm1_lstm2'
LSTM2_LSTM3_MEM_NAME = 'om3_lstm2_lstm3'
