# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0
"""Spatial and temporal primitives for MeteoForge."""

from meteoforge.spatial_temporal.catalog import (
    CatalogEntry,
    LocationResolution,
    NamedLocationCatalog,
    ResolutionStatus,
)
from meteoforge.spatial_temporal.geography import (
    DEFAULT_TOLERANCE_METERS,
    DEFAULT_TOLERANCE_POLICY,
    Area,
    AreaGeometry,
    AreaResult,
    BoundingBox,
    GridPoint,
    Location,
    PointMatch,
    PointMatchResult,
    SpatialError,
    TolerancePolicy,
    match_points,
    normalize_crs,
)

__all__ = [
    "DEFAULT_TOLERANCE_METERS",
    "DEFAULT_TOLERANCE_POLICY",
    "Area",
    "AreaGeometry",
    "AreaResult",
    "BoundingBox",
    "CatalogEntry",
    "GridPoint",
    "Location",
    "LocationResolution",
    "NamedLocationCatalog",
    "PointMatch",
    "PointMatchResult",
    "ResolutionStatus",
    "SpatialError",
    "TolerancePolicy",
    "match_points",
    "normalize_crs",
]
