# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.storage_management_handler.base_model import (
    StorageManagementModel,
    StorageMedium,
    StorageType,
)


class NoStorageHandler(StorageManagementModel):
    """Handler for no storage scenario."""

    storage_type = StorageType.NONE
    storage_medium = StorageMedium.NONE

    def __init__(self):
        """Initialize the no storage handler."""
        super().__init__()
