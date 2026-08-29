# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0
"""Unit tests for validators.py."""

import pytest
from pyproj import CRS

from meteoforge.spatial_temporal.validators import (
    CRSValidationError,
    validate_crs,
    validate_location,
    validate_mf_location,
    validate_mf_period,
)


def test_validate_mf_location_valid() -> None:
    """Test valid inputs for validate_mf_location."""
    crs = CRS.from_epsg(4326)
    assert validate_mf_location(0, 0, crs)
    assert validate_mf_location(10.0, 20.0, crs)


def test_validate_mf_location_invalid_type() -> None:
    """Test invalid types for validate_mf_location."""
    crs = CRS.from_epsg(4326)
    with pytest.raises(TypeError):
        validate_mf_location("x", 0, crs)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        validate_mf_location(0, "y", crs)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        validate_mf_location(0, 0, "not_a_crs")  # type: ignore[arg-type]


def test_validate_crs_valid() -> None:
    """Test valid inputs for validate_crs."""
    assert validate_crs(CRS.from_epsg(4326))
    assert validate_crs(4326)
    assert validate_crs("EPSG:4326")


def test_validate_crs_invalid() -> None:
    """Test invalid inputs for validate_crs."""
    with pytest.raises(CRSValidationError):
        validate_crs(999999)  # Invalid EPSG
    with pytest.raises(TypeError):
        validate_crs([1, 2, 3])


def test_validate_location_valid() -> None:
    """Test valid inputs for validate_location."""
    crs = CRS.from_epsg(4326)
    assert validate_location(0, 0, crs)
    assert validate_location(10, 20, crs)


def test_validate_location_out_of_bounds() -> None:
    """Test out-of-bounds inputs for validate_location."""
    crs = CRS.from_epsg(4326)
    with pytest.raises(CRSValidationError):
        validate_location(-200, 0, crs)
    with pytest.raises(CRSValidationError):
        validate_location(0, -100, crs)


def test_validate_mf_period_stub() -> None:
    """Test stub for validate_mf_period."""
    # This is a stub, as the function is not implemented
    assert validate_mf_period("a", "b")
