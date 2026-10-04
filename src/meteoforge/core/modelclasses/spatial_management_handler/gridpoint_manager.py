# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.spatial_management_handler.base_model import (
    SpatialManagementModel,
    SpatialType,
)
from meteoforge.spatial_temporal.locations import MFLocation


class GridpointManager(SpatialManagementModel):
    """This class is responsible for managing gridpoint spatial data in the MeteoForge framework."""

    def find_nearest(self, location: MFLocation) -> dict:
        """Find the nearest gridpoint to the given location.

        Args:
            location (MFLocation): The location to find the nearest gridpoint for.

        Returns:
            dict: A dictionary containing information about the nearest gridpoint.
        """
        raise NotImplementedError("The find_nearest method must be implemented by the subclass.")

    spatial_type = SpatialType.GRIDPOINT

    def __init__(self):
        """Initialize the gridpoint manager."""
        super().__init__()
