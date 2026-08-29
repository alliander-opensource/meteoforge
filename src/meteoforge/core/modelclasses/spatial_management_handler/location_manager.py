# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0
from abc import abstractmethod

from meteoforge.core.modelclasses.spatial_management_handler.base_model import SpatialManagementModel, SpatialType
from meteoforge.spatial_temporal.locations import MFLocation


class LocationManager(SpatialManagementModel):
    """Class to manage locations in the MeteoForge system."""

    @abstractmethod
    def find_nearest(self, location: MFLocation) -> dict:
        """Find the nearest location to the given MFLocation."""
        raise NotImplementedError("Subclasses must implement the find_nearest method.")

    spatial_type = SpatialType.LOCATION

    def __init__(self):
        """Initialize the LocationManager."""
        super().__init__()
