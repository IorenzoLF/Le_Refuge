if __name__ == "__main__":
    sensor = AudioSensor()
    dummy_wave = np.random.randn(16000).astype(np.float32)  # simulate 1 second audio at 16kHz
    vec = sensor.get_audio_vector(dummy_wave)
    print(vec.shape)  # should be (64,)
    print(vec.dtype)  # float32
