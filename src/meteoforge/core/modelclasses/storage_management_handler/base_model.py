from abc import ABC
from enum import Enum, auto
from typing import ClassVar


class StorageType(Enum):
    NONE = auto()  # No storage at all
    CACHE = auto()  # Only cache storage
    PERSISTENT = auto()  # Persistent storage (e.g., file system)
    PERSISTENT_WITH_CACHE = auto()  # Persistent storage with cache support


class StorageMedium(Enum):
    NONE = auto()  # No storage medium
    FILE_SYSTEM = auto()  # File system storage
    CLOUD_STORAGE = auto()  # Cloud storage (e.g., AWS S3, Google Cloud Storage)


class StorageManagementModel(ABC):
    """Base model for storage management handler."""

    storage_type = ClassVar[StorageType]
    storage_medium = ClassVar[StorageMedium]

    def __init__(self):
        """Initialize the storage management handler with default values."""
        pass
