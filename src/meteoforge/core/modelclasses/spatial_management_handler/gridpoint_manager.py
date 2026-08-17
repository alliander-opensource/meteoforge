# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.spatial_management_handler.base_model import SpatialManagementModel, SpatialType


class GridpointManager(SpatialManagementModel):
    """This class is responsible for managing gridpoint spatial data in the MeteoForge framework."""

    spatial_type = SpatialType.GRIDPOINT

    def __init__(self):
        """Initialize the gridpoint manager."""
        super().__init__()
