# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0

"""Pytest tests for the locations module (MFLocation, MFLocationList, MFLocationVector, fuzzy_in).

Tests only the module logic, not pyproj or Shapely internals.
"""

from typing import Any

from pyproj import CRS

from meteoforge.spatial_temporal.locations import (
    MFLocation,
    MFLocationList,
    MFLocationVector,
    _crs_to_obj,
    _transform_point,
    fuzzy_in,
)


def test_crs_to_obj_accepts_crs_types() -> None:
    """Test that _crs_to_obj correctly accepts CRS objects, ints, and strings."""
    # Accepts CRS, int, str
    crs = CRS.from_epsg(4326)
    assert _crs_to_obj(crs) == crs
    assert _crs_to_obj(4326) == CRS.from_epsg(4326)
    assert _crs_to_obj("EPSG:4326") == CRS.from_epsg(4326)


def test_transform_point_identity() -> None:
    """Transforming a point in the same CRS should return the same coordinates."""
    crs = CRS.from_epsg(4326)
    x, y = 1.0, 2.0
    assert _transform_point(x, y, crs, crs) == (x, y)


def test_mflocation_repr_and_eq() -> None:
    """Test MFLocation equality and string representation."""
    a = MFLocation(1, 2, 4326)
    b = MFLocation(1, 2, 4326)
    c = MFLocation(1.00001, 2, 4326)  # Use a value outside the default tolerance for fuzzy equality
    assert a == b
    assert a != c
    assert "MFLocation" in repr(a)


def test_mflocation_to_transforms(monkeypatch: Any) -> None:
    """Test that MFLocation.to correctly transforms coordinates using _transform_point."""
    # Only patch to check that _transform_point is called, not to replace its math
    called = {}

    def fake_transform(x: float, y: float, from_crs: CRS, to_crs: CRS) -> tuple[float, float]:
        called["args"] = (x, y, from_crs, to_crs)
        return (123, 456)

    monkeypatch.setattr("meteoforge.spatial_temporal.locations._transform_point", fake_transform)
    a = MFLocation(1, 2, 4326)
    b = a.to(3857)
    assert called["args"][0] == 1 and called["args"][1] == 2
    assert isinstance(b, MFLocation)
    assert b.x == 123 and b.y == 456


def test_mflocationlist_append_and_contains() -> None:
    """Test MFLocationList append, contains, get, set, and delete operations."""
    a = MFLocation(1, 2, 4326)
    b = MFLocation(3, 4, 4326)
    lst = MFLocationList([a])
    lst.append(b)
    assert len(lst) == 2
    assert a in lst
    assert b in lst
    c = MFLocation(1.00001, 2, 4326)  # Use a value outside the default tolerance for fuzzy equality
    assert c not in lst
    assert lst[0] == a
    lst[1] = a
    assert lst[1] == a
    del lst[1]
    assert len(lst) == 1


def test_mflocationlist_find_nearby() -> None:
    """Test MFLocationList.find_nearby method."""
    a = MFLocation(1, 2, 4326)
    b = MFLocation(1.0000001, 2, 4326)
    lst = MFLocationList([a])
    found = lst.find_nearby(b, tol=1e-5)
    assert found == a
    not_found = lst.find_nearby(MFLocation(5, 5, 4326))
    assert not_found is None


def test_mflocationvector_append_and_contains() -> None:
    """Test MFLocationVector with a valid closed polygon, no mutation after creation."""
    a = MFLocation(0, 0, 4326)
    b = MFLocation(1, 0, 4326)
    c = MFLocation(1, 1, 4326)
    d = MFLocation(0, 1, 4326)
    # Only pass 4 points, do not close explicitly
    vec = MFLocationVector([a, b, c, d])
    pt_inside = MFLocation(0.5, 0.5, 4326)
    pt_outside = MFLocation(2, 2, 4326)
    assert pt_inside in vec
    assert pt_outside not in vec
    pt_near = MFLocation(0, 0.00001, 4326)
    assert pt_near in vec
    assert vec[0] == a
    assert len(vec.locations) == 4


def test_fuzzy_in() -> None:
    """Test the fuzzy_in function for real MFLocation objects."""
    items = [MFLocation(1, 2, 4326), MFLocation(3, 4, 4326), MFLocation(5, 6, 4326)]
    item = MFLocation(3.0000001, 4, 4326)
    assert fuzzy_in(item, items, tol=1e-5)
    assert not fuzzy_in(MFLocation(7, 8, 4326), items, tol=1e-5)
