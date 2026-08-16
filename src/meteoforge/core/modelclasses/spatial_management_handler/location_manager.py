from meteoforge.core.modelclasses.spatial_management_handler.base_model import SpatialManagementModel, SpatialType


class LocationManager(SpatialManagementModel):
    """Class to manage locations in the MeteoForge system."""

    spatial_type = SpatialType.LOCATION

    def __init__(self):
        super().__init__()
