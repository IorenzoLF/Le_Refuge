# main.py

from core.engine import OM3Engine

def main():
    engine = OM3Engine()
    engine.run(cycles=None)  # Infinite runtime

if __name__ == "__main__":
    main()
