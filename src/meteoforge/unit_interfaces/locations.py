#  SPDX-FileCopyrightText: 2024-2025 Copyright Contributors to the MeteoForge project
#  SPDX-License-Identifier: MPL-2.0

"""The Meteoforge locations interface.

The locations interface provides a way to uniformly work with different types of geographic locations regardless of
their original format. It allows for the conversion of various location formats into a standardized format, enabling
the use of a common set of operations on these locations.

It also provides methods to work with multiple locations to generate bounding boxes and polygons, which can be useful
for geospatial analysis and visualization. The interface is designed to be flexible and extensible, allowing for
the addition of new location formats and operations as needed.
"""

from pyproj import CRS
from pyproj.exceptions import CRSError

logger = logging.getLogger("MeteoForgeLogger")


class MFLocation:
    """A class representing a Geographical location.

    This class serves as a base for various location based  formats, such as coordinates, bounding boxes, and polygons.
    It provides a common interface for working with these different formats, allowing for the easy conversion and
    manipulation of geographic data.

    Attributes
    ----------
        x (float):
            The x-coordinate of the location. Typically, this represents longitude, but this can vary based on the
            Coordinate Reference System (CRS) used.
        y (float):
            The y-coordinate of the location. Typically, this represents latitude, but this can vary based on the
            Coordinate Reference System (CRS) used.
        crs (int):
            The coordinate reference system of the location, if applicable via EPSG numerical code. This is used to
            properly interpret the x and y coordinates in a geographic context. The default setting is EPSG code 4326,
            which represents the WGS 84 geographic coordinate system.

    """

    def __init__(self, *, x: float, y: float, epsg_code: int = 4326):
        """Initialize the MFLocation with coordinates and CRS."""
        self.__validate(x, y, epsg_code)

        if not isinstance(x, (int, float)):
            raise TypeError(f"Parameter x must be a number, got {type(self.x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"Parameter y must be a number, got {type(self.y).__name__}")
        if not isinstance(epsg_code, int):
            raise TypeError(f"Parameter crs must be an integer, got {type(self.crs).__name__}")

        self.crs = self.validate_crs(epsg_code)
        self.x, self.y = self._is_validate_coordinate(x, y, self.crs)

    def __repr__(self) -> str:
        """Return a string representation of the MFLocation."""
        return f"MFLocation(x={self.x}, y={self.y}, crs={self.crs})"

    def __str__(self) -> str:
        """Return a string representation of the MFLocation."""
        return f"MFLocation: ({self.x}, {self.y}) in CRS {self.crs}"

    def __eq__(self, other: "MFLocation") -> bool:
        """Check if two MFLocation instances are equal."""
        """
        if not isinstance(other, MFLocation):
            raise TypeError(f"Cannot compare MFLocation with {type(other).__name__}")

        if not self.is_validate_coordinate() or not other.is_validate_coordinate():
            raise ValueError(
                "Cannot compare MFLocation instances with invalid coordinates."
            )
        """

        return self.as_wgs84_coordinate() == other.as_wgs84_coordinate()

    @staticmethod
    def validate_epsg_code_as_crs(*, epsg_code: int) -> bool:
        """Check if the given epsg code represents a valid CRS."""
        # Verify that the CRS exists and is valid
        try:
            crs = CRS.from_epsg(epsg_code)
        except CRSError as e:
            raise ValueError(f"invalid CRS code '{crs}': --<<-- {e} -->>--") from e

        # Check that the CRS is not deprecated
        if crs.is_deprecated:
            raise ValueError(
                f"The CRS with EPSG code {epsg_code} is deprecated. Please use a different (non-deprecated) CRS."
            )

        # Check that the CRS is for an x,y based geographic coordinate system
        if not crs.is_geographic and not crs.is_geocentric:
            raise ValueError(
                "The MFLocation class type only supports Geographic (CRS.is_geographic=True) and Geocentric Coordinate "
                "Systems (CRS.is_geocentric=True)."
            )
        return True

    @staticmethod
    def is_validate_coordinate(x: float, y: float, crs: CRS | int) -> bool:
        """Check if the coordinates are valid."""
        ...
        return ...

    def lies_within_bounds_of_crs(self, crs: CRS | int) -> bool:
        """Check if the location lies within the bounds of the given CRS."""
        if isinstance(crs, int):
            try:
                crs = CRS.from_epsg(crs)
            except CRSError as e:
                raise ValueError(f"invalid CRS code '{crs}': --<<-- {e} -->>--") from e

        return False

    def is_first_coordinate_northing(self, crs) -> bool:
        """Check if the first coordinate is a northing (y-coordinate) or an easting (x-coordinate).

        Example:
        -------
            - For the WGS 84 CRS (EPSG:4326), this returns True,
              indicating that the first coordinate is a northing (latitude).
            - For the UTM CRS (e.g., EPSG:32633), this returns False,
                indicating that the first coordinate is an easting (longitude).

        """
        return self.crs.axis_info[0].direction == "north" and self.crs.axis_info[1].direction == "east"


class MFLocationList(list[MFLocation]): ...


class MFLocationPolygon: ...
