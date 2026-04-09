# Example fuzz test using Atheris for Python
# Install atheris: pip install atheris

import sys

import atheris


def fuzz_target(data: bytes):
    """Fuzz target example function that takes a byte string as input and performs some operations on it."""
    # Example: try to decode as utf-8 and split
    try:
        s = data.decode('utf-8')
        _ = s.split(',')
    except Exception:
        pass

def main():
    """Set up and run the Atheris fuzzing."""
    atheris.Setup(sys.argv, fuzz_target)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
