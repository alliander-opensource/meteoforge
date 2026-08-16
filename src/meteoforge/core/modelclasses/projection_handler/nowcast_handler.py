from meteoforge.core.modelclasses.projection_handler.base_model import MeteoProjectionHandlerModel, ProjectionType


class MeteoNowCastHandler(MeteoProjectionHandlerModel):
    """This class is responsible for handling nowcasting operations in the MeteoForge framework.
    It provides methods to process and analyze real-time weather data for short-term forecasting.
    """

    forecast_support = ProjectionType.NOWCAST

    def __init__(self):
        super().__init__()
