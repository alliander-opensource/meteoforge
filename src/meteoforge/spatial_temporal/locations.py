# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

"""Hybrid location module: easy use, CRS-flexible, fuzzy equality, and robust containment."""

from collections.abc import Iterable
from typing import Any

from pyproj import CRS, Transformer
from shapely.geometry import Point, Polygon

from meteoforge.spatial_temporal.validators import validate_mf_location


def _crs_to_obj(crs_like: int | str | CRS) -> CRS:
    """Convert an int, str, or CRS to a CRS object."""
    if isinstance(crs_like, CRS):
        return crs_like
    return CRS.from_user_input(value=crs_like)


def _transform_point(x: float, y: float, from_crs: CRS, to_crs: CRS) -> tuple[float, float]:
    """Transform a point (x, y) from one CRS to another."""
    if from_crs == to_crs:
        return x, y
    transformer = Transformer.from_crs(from_crs, to_crs, always_xy=True)
    x2, y2 = transformer.transform(x, y)
    return float(x2), float(y2)


class MFLocation:
    """A geographic location with CRS, supporting transformation and fuzzy equality."""

    def __init__(self, x: float, y: float, crs: int | str | CRS = 4326):
        """Create a location with coordinates (x, y) and a CRS."""
        self.crs = _crs_to_obj(crs)
        self.x = float(x)
        self.y = float(y)
        self.point = Point(self.x, self.y)
        validate_mf_location(self.x, self.y, self.crs)

    def to(self, target_crs: int | str | CRS) -> "MFLocation":
        """Return a new MFLocation transformed to the target CRS."""
        target_crs_obj = _crs_to_obj(target_crs)
        x2, y2 = _transform_point(self.x, self.y, self.crs, target_crs_obj)
        return MFLocation(x2, y2, target_crs_obj)

    def equals(self, other: "MFLocation", tol: float = 1e-6, crs: int | str | CRS = 4326) -> bool:
        """Check if two locations are close enough in a common CRS."""
        # Compare in a common CRS (default: WGS84)
        crs_obj = _crs_to_obj(crs)
        a = self.to(crs_obj)
        b = other.to(crs_obj)
        return abs(a.x - b.x) < tol and abs(a.y - b.y) < tol

    def __eq__(self, other: Any) -> bool:
        """Check equality with another MFLocation, using fuzzy equality in a common CRS."""
        if not isinstance(other, MFLocation):
            return NotImplemented
        return self.equals(other)

    def __repr__(self) -> str:
        """Get a string representation of the location."""
        return f"MFLocation(x={self.x}, y={self.y}, crs={self.crs.to_string()})"


class MFLocationList:
    """A class representing a list of MFLocation objects, with fuzzy containment and CRS handling."""

    def __init__(self, locations: Iterable[MFLocation] | None = None, crs: int | str | CRS = 4326):
        """Create a list of locations, converting all to the given CRS."""
        self.crs = _crs_to_obj(crs)
        self.locations: list[MFLocation] = []
        if locations:
            for loc in locations:
                self.append(loc)

    def append(self, location: Any) -> None:
        """Add a location to the list, converting to the list's CRS if needed."""
        if not isinstance(location, MFLocation):
            raise TypeError("Only MFLocation instances can be added.")
        # Accept any CRS, but store as self.crs
        loc_in_crs = location.to(self.crs)
        self.locations.append(loc_in_crs)

    def __getitem__(self, idx: int) -> MFLocation:
        """Get a location by index."""
        return self.locations[idx]

    def __setitem__(self, idx: int, value: MFLocation) -> None:
        """Set a location by index, converting to the list's CRS if needed."""
        self.locations[idx] = value.to(self.crs)

    def __delitem__(self, idx: int) -> None:
        """Delete a location by index."""
        del self.locations[idx]

    def __len__(self) -> int:
        """Return the number of locations in the list."""
        return len(self.locations)

    def __contains__(self, item: MFLocation) -> bool:
        """Check if a location is 'fuzzily' in the list, CRS-aware."""
        # Fuzzy containment: is any location in the list 'close enough' to item?
        return any(loc.equals(item) for loc in self.locations)

    def find_nearby(self, item: MFLocation, tol: float = 1e-6) -> MFLocation | None:
        """Return the first location in the list close to the given item, or None."""
        for loc in self.locations:
            if loc.equals(item, tol=tol):
                return loc
        return None

    def __repr__(self) -> str:
        """Return a string representation of the MFLocationList instance."""
        return f"MFLocationList({self.locations}, crs={self.crs.to_string()})"


class MFLocationVector:
    """A vector (polygon) of MFLocation objects, with fuzzy containment and CRS handling."""

    def __init__(self, locations: Iterable[MFLocation] | None = None, crs: int | str | CRS = 4326):
        """Create a vector (polygon) from locations, converting all to the given CRS."""
        self.crs = _crs_to_obj(crs)
        self.locations: list[MFLocation] = []
        self.polygon: Polygon | None = None
        if locations:
            for loc in locations:
                self.append(loc)
        self._update_polygon()

    def append(self, location: Any) -> None:
        """Add a location to the vector, converting to the vector's CRS if needed."""
        if not isinstance(location, MFLocation):
            raise TypeError("Only MFLocation instances can be added.")
        loc_in_crs = location.to(self.crs)
        self.locations.append(loc_in_crs)
        self._update_polygon()

    def _update_polygon(self) -> None:
        """Update the internal Shapely polygon from the current locations."""
        coords = [loc.to(self.crs).point for loc in self.locations]
        # Only create a polygon if there are at least 3 unique points (4 for closure)
        if len(coords) >= 3:
            xy = [(pt.x, pt.y) for pt in coords]
            # Ensure closure: first == last
            if xy[0] != xy[-1]:
                xy.append(xy[0])
            if len(xy) >= 4:
                self.polygon = Polygon(xy)
            else:
                self.polygon = None
        else:
            self.polygon = None

    def contains(self, location: MFLocation, tol: float = 1e-6) -> bool:
        """Check if the vector contains a location (fuzzy, CRS-aware, and near boundary)."""
        pt = location.to(self.crs).point
        # 1. True Shapely containment
        if self.polygon and self.polygon.contains(pt):
            return True
        # 2. Fuzzy: check if any vertex is close to the point
        if any(pt.distance(vertex.point) < tol for vertex in self.locations):
            return True
        # 3. Fuzzy: check if point is near the polygon boundary (within tol)
        return bool(self.polygon and self.polygon.boundary.distance(pt) < tol)

    def __contains__(self, item: MFLocation) -> bool:
        """Check if a location is in the vector, using fuzzy containment."""
        return self.contains(item)

    def __getitem__(self, idx: int) -> MFLocation:
        """Get a location by index."""
        return self.locations[idx]

    def __setitem__(self, idx: int, value: MFLocation) -> None:
        """Set a location by index, converting to the vector's CRS if needed."""
        self.locations[idx] = value.to(self.crs)
        self._update_polygon()

    def __delitem__(self, idx: int) -> None:
        """Delete a location by index."""
        del self.locations[idx]
        self._update_polygon()

    def __len__(self) -> int:
        """Return the number of locations in the vector."""
        return len(self.locations)

    def __repr__(self) -> str:
        """Return a string representation of the MFLocationVector instance."""
        return f"MFLocationVector({self.locations}, crs={self.crs.to_string()})"


# Utility: fuzzy membership for a location in a list/vector


def fuzzy_in(item: MFLocation, container: Iterable[MFLocation], tol: float = 1e-6, crs: int | str | CRS = 4326) -> bool:
    """Check if a location is 'fuzzily' in a container (list/vector), CRS-aware."""
    crs_obj = _crs_to_obj(crs)
    item_in_crs = item.to(crs_obj)
    return any(loc.to(crs_obj).equals(item_in_crs, tol=tol, crs=crs_obj) for loc in container)
