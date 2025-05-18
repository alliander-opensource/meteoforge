#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0


class ForgeLocation:
    """A class representing a geographical location."""

    ...


class ForgePolygonalArea:
    """A class representing a geographical location defined by a polygon."""

    def __init__(self, coordinates: tuple[ForgeLocation, ForgeLocation, ForgeLocation, ...]):
        """Initialize the polygonal area with a list of coordinates.

        Attributes:
            coordinates (tuple[ForgeLocation, ...]):
                A tuple of ForgeLocation objects representing the vertices of the polygon.
                These should be in order, either clockwise or counterclockwise.
        """
        self.coordinates = coordinates

    def __repr__(self):
        return f"ForgePolygonalArea(coordinates={self.coordinates})"

    def contains(self, location: ForgeLocation) -> bool:
        """Check if a given location is within the polygonal area.

        Args:
            location (ForgeLocation): The location to check.

        Returns:
            bool: True if the location is within the polygon, False otherwise.
        """
        # Implement point-in-polygon algorithm here
        pass


ForgeLocations = ForgeLocation | tuple[ForgeLocation, ...] | ForgePolygonalArea