from meteoforge.core.modelclasses.spatial_management_handler.base_model import SpatialManagementModel, SpatialType


class GridpointManager(SpatialManagementModel):
    """This class is responsible for managing gridpoint spatial data in the MeteoForge framework."""

    spatial_type = SpatialType.GRIDPOINT

    def __init__(self):
        super().__init__()
