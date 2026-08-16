from meteoforge.core.modelclasses.projection_handler.base_model import MeteoProjectionHandlerModel, ProjectionType


class MeteoNoCastingHandler(MeteoProjectionHandlerModel):
    """This class is responsible for handling scenarios where no casting (neither nowcasting nor forecasting) is required.
    It serves as a placeholder or default handler in the MeteoForge framework.
    """

    forecast_support = ProjectionType.NONE

    def __init__(self):
        super().__init__()
