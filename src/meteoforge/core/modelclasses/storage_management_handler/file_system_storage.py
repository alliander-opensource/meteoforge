# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.storage_management_handler.base_model import (
    StorageManagementModel,
    StorageMedium,
    StorageType,
)


class FileSystemStorageHandler(StorageManagementModel):
    """This class is responsible for handling file system storage operations in the MeteoForge framework.

    It provides methods to manage and interact with the file system for storing and retrieving data.
    """

    storage_type = StorageType.PERSISTENT
    storage_medium = StorageMedium.FILE_SYSTEM

    def __init__(self):
        """Initialize the file system storage handler."""
        super().__init__()
