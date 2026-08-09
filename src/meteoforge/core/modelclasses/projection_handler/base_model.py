from abc import ABC
from enum import Enum, auto
from typing import ClassVar


class ProjectionType(Enum):
    NONE = auto()
    NOWCAST = auto()
    FORECAST = auto()


class MeteoProjectionHandlerModel(ABC):
    """Base class for projection capabilities.

    By projection capabilities, we mean the ability of a model to support different types of temporal projections, such
    as nowcasting or forecasting. This class serves as a base for other classes that implement specific projection
    capabilities.
    """

    forecast_support = ClassVar[ProjectionType]

    def __init__(self): ...
