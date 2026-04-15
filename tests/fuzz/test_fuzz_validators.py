# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0
"""Fuzz tests for validators.py using Atheris."""
import sys

import atheris
from pyproj import CRS

from meteoforge.spatial_temporal import validators


def fuzz_target(data: bytes):
    """Fuzz target for validators.py."""
    try:
        # Try to interpret data as a string or int for CRS
        try:
            crs_val = data.decode("utf-8", errors="ignore")
        except Exception:
            crs_val = 4326
        # Try to use as int/float for x/y
        if len(data) >= 8:
            x = int.from_bytes(data[:4], "little", signed=True) / 1e5
            y = int.from_bytes(data[4:8], "little", signed=True) / 1e5
        else:
            x, y = 0, 0
        # Fuzz validate_mf_location
        try:
            crs = CRS.from_user_input(crs_val)
        except Exception:
            crs = CRS.from_epsg(4326)
        try:
            validators.validate_mf_location(x, y, crs)
        except Exception:
            pass
        # Fuzz validate_crs
        try:
            validators.validate_crs(crs_val)
        except Exception:
            pass
    except Exception:
        pass

def main():
    """Set up Atheris and run the fuzz tests."""
    atheris.Setup(sys.argv, fuzz_target)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
