# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0

"""Module for validating spatial and temporal data in MeteoForge."""

from typing import Any

from pyproj import CRS, Transformer
from pyproj.exceptions import CRSError

from meteoforge.logging.logging import logger


class CRSValidationError(ValueError):
    """Raised when a CRS validation fails in MFLocation."""


def validate_mf_location(x: int | float, y: int | float, crs: CRS) -> bool:
    """Validate a given x,y location with an EPSG code as a valid coordinate for MeteoForge."""
    # Perform type checks on the input parameters
    _perform_mf_location_type_checks(x, y, crs)
    logger.debug("Type checks passed for x=%s, y=%s, crs=%s", x, y, crs)

    # Evaluate the EPSG code as a valid CRS for MeteoForge
    validate_crs(crs)
    logger.debug("CRS validation passed for CRS: %s", crs)

    # Evaluate the x and y coordinates as valid for the given CRS
    validate_location(x, y, crs)
    logger.debug("Location validation passed for x=%s, y=%s, CRS=%s", x, y, crs)
    return True


def validate_mf_period(start_time: object, end_time: object) -> bool:
    """Validate a given start and end time as a valid period for MeteoForge."""
    # Perform type checks on the input parameters
    _perform_mf_period_type_checks(start_time, end_time)

    # Evaluate the start and end times as valid for MeteoForge
    ...

    return True


def _perform_mf_location_type_checks(x: Any, y: Any, crs: Any) -> None:
    """Check the types of x, y, and CRS."""
    if not isinstance(x, int | float):
        raise TypeError("x must be a number")
    if not isinstance(y, int | float):
        raise TypeError("y must be a number")
    if not isinstance(crs, CRS):
        raise TypeError("crs must be a CRS instance")


def validate_crs(crs: Any) -> bool:
    """Validate the given CRS as a valid CRS for MeteoForge."""
    logger.debug("Validating CRS: %s", crs)

    if not isinstance(crs, CRS | int | str):
        raise TypeError("crs must be a CRS instance, int, or str")

    try:
        # Attempt to create a CRS object from the EPSG code to check if it is valid
        if isinstance(crs, CRS):
            crs_object = crs
        elif isinstance(crs, int):
            crs_object = CRS.from_epsg(crs)
        else:  # Assume it's a CRS string like "EPSG:4326"
            crs_object = CRS.from_string(crs)

    except CRSError as e:
        raise CRSValidationError(f"Invalid CRS type or value: {crs}") from e

    # Check that the created CRS is not deprecated
    if crs_object.is_deprecated:
        raise CRSValidationError(
            f"The CRS built from {crs} is deprecated. Please use a different (non-deprecated) CRS."
        )

    # Check that the CRS is either geographic, geocentric, or projected, as these are the types supported by MFLocation
    if not crs_object.is_geographic and not crs_object.is_geocentric and not crs_object.is_projected:
        raise CRSValidationError(
            "The MFLocation class type only supports Geographic (CRS.is_geographic=True), Geocentric Coordinate "
            "Systems (CRS.is_geocentric=True) and Projected Coordinate Systems (CRS.is_projected=True)."
        )
    return True


def validate_location(x: int | float, y: int | float, crs: CRS) -> bool:
    """Validate the given x and y coordinates as valid for the specified CRS.

    Evaluate the x and y coordinates as valid for the given CRS, e.g., check if they fall within the valid range for
    the CRS. This may involve checking if the coordinates are within the bounds of the CRS's valid area.

    Attributes
    ----------
    x (int | float):
            The x-coordinate of the location. Typically, this represents longitude, but this can vary based on the
            Coordinate Reference System (CRS) used.
    y (int | float):
            The y-coordinate of the location. Typically, this represents latitude, but this can vary based on the
            Coordinate Reference System (CRS) used.
    crs (CRS):
            The coordinate reference system of the location. This is used to properly interpret the x and y coordinates
            in a geographic context.

    Returns
    -------
    bool
        True if the location is valid for the given CRS, False otherwise.

    """
    area_of_use = crs.area_of_use

    if area_of_use is None:
        logger.warning("No area of use defined for CRS %s, skipping bounds check", crs)
        return True

    # Transform area_of_use bounds (WGS84) to the native CRS units
    transformer = Transformer.from_crs(CRS.from_epsg(4326), crs, always_xy=True)
    min_x, min_y = transformer.transform(area_of_use.west, area_of_use.south)
    max_x, max_y = transformer.transform(area_of_use.east, area_of_use.north)

    if not (min_x <= x <= max_x):
        raise CRSValidationError(f"x coordinate {x} is outside valid bounds [{min_x}, {max_x}] for CRS {crs}")

    if not (min_y <= y <= max_y):
        raise CRSValidationError(f"y coordinate {y} is outside valid bounds [{min_y}, {max_y}] for CRS {crs}")

    logger.debug("Location validation passed and valid: x=%s, y=%s, CRS=%s", x, y, crs)
    return True


def _perform_mf_period_type_checks(start_time: Any, end_time: Any) -> None:
    """Check the types of start_time and end_time."""
    # Implement type checks for start_time and end_time, e.g., check if they are datetime objects
    _, _ = start_time, end_time
    ...
