# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0
import logging

# Example fuzz test using Atheris for Python
# Install atheris: pip install atheris
import sys

import atheris

logger = logging.getLogger(__name__)


def fuzz_target(data: bytes) -> None:
    """Fuzz target example function that takes a byte string as input and performs some operations on it."""
    # Example: try to decode as utf-8 and split
    try:
        s = data.decode("utf-8")
        _ = s.split(",")
    except Exception as e:
        logger.warning("Exception occurred during fuzzing: %s", e)
        pass


def main() -> None:
    """Set up and run the Atheris fuzzing."""
    atheris.Setup(sys.argv, fuzz_target)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
