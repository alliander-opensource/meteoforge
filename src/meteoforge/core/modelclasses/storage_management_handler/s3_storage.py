# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.storage_management_handler.base_model import (
    StorageManagementModel,
    StorageMedium,
    StorageType,
)


class S3StorageHandler(StorageManagementModel):
    """This class is responsible for handling AWS S3 storage operations in the MeteoForge framework.

    It provides methods to manage and interact with AWS S3 for storing and retrieving data.
    """

    storage_type = StorageType.PERSISTENT_WITH_CACHE
    storage_medium = StorageMedium.CLOUD_STORAGE

    def __init__(self):
        """Initialize the S3 storage handler."""
        super().__init__()
