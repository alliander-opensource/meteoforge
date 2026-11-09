# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0
"""Fuzz tests for validators.py using Atheris."""

import contextlib
import sys

import atheris
from pyproj import CRS
from pyproj.exceptions import CRSError

with atheris.instrument_imports(include=["meteoforge"]):  # type: ignore[attr-defined]
    from meteoforge.spatial_temporal import validators


@atheris.instrument_func  # type: ignore[attr-defined]
def fuzz_target(data: bytes) -> None:
    """Fuzz target for validators.py."""
    crs_val = data.decode("utf-8", errors="ignore")
    if len(data) >= 8:
        x = int.from_bytes(data[:4], "little", signed=True) / 1e5
        y = int.from_bytes(data[4:8], "little", signed=True) / 1e5
    else:
        x, y = 0, 0

    try:
        crs = CRS.from_user_input(crs_val)
    except CRSError:
        crs = CRS.from_epsg(4326)

    with contextlib.suppress(validators.CRSValidationError):
        validators.validate_mf_location(x, y, crs)

    with contextlib.suppress(validators.CRSValidationError):
        validators.validate_crs(crs_val)


def main() -> None:
    """Set up Atheris and run the fuzz tests."""
    atheris.Setup(sys.argv, fuzz_target)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
