from meteoforge.core.modelclasses.storage_management_handler.base_model import (
    StorageManagementModel,
    StorageType,
    StorageMedium,
)


class NoStorageHandler(StorageManagementModel):
    """Handler for no storage scenario."""

    storage_type = StorageType.NONE
    storage_medium = StorageMedium.NONE

    def __init__(self):
        """Initialize the no storage handler."""
        super().__init__()
