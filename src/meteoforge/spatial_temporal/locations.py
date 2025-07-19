#  SPDX-FileCopyrightText: 2024-2025 Copyright Contributors to the MeteoForge project
#  SPDX-License-Identifier: MPL-2.0
from pyproj import CRS
from pyproj.exceptions import CRSError

from src.meteoforge.logging.logging import logger


class MFLocation:
    """The base class for representing geographic locations in MeteoForge.

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

    def __init__(self, *, x: int | float, y: int | float, epsg_code: int = 4326):
        """Initializes the MFLocation with x, y coordinates and an optional EPSG code."""
        # Validate the input parameters
        if self.valid_location(x, y, epsg_code):
            # Set the instance variables
            self.x = float(x)
            self.y = float(y)
            self.crs = epsg_code
        else:
            raise ValueError("Invalid location parameters")

    @staticmethod
    def valid_location(x: float, y: float, epsg_code: int = 4326) -> bool:
        """Validates the location parameters for type and existence."""
        logger.debug(f"Validating location: x={x}, y={y}, epgs_code={epsg_code}")

        # Validate the types of x, y, and epgs_code
        if not isinstance(x, (int, float)):
            raise ValueError("x must be a number")
        if not isinstance(y, (int, float)):
            raise ValueError("y must be a number")
        if not isinstance(epsg_code, int):
            raise ValueError("epgs_code must be an integer")

        logger.debug(f"Type validation passed: x={type(x)}, y={type(y)}, epgs_code={type(epsg_code)}")

        # Validate the CRS type suggested by the EPSG code
        MFLocation.valid_crs(epsg_code)

        logger.debug(f"CRS validation passed for EPSG code: {epsg_code}")

        # Check that x and y are within valid ranges for geographic coordinates on the given CRS
        ...

        logger.debug(f"Location validation passed and valid: x={x}, y={y}, epsg_code={epsg_code}")

    @staticmethod
    def valid_crs(epsg_code: int) -> bool:
        """Validates the EPSG code for known coordinate reference systems."""
        logger.debug(f"Validating CRS with EPSG code: {epsg_code}")

        try:
            crs = CRS.from_epsg(epsg_code)
        except CRSError as e:
            raise ValueError(f"invalid EPSG code '{crs}': --<<-- {e} -->>--") from e

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
