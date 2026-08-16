from meteoforge.core.modelclasses.storage_management_handler.base_model import (
    StorageManagementModel,
    StorageType,
    StorageMedium,
)


class FileSystemStorageHandler(StorageManagementModel):
    """
    This class is responsible for handling file system storage operations in the MeteoForge framework.
    It provides methods to manage and interact with the file system for storing and retrieving data.
    """

    storage_type = StorageType.PERSISTENT
    storage_medium = StorageMedium.FILE_SYSTEM

    def __init__(self):
        super().__init__()
