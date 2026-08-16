from abc import ABC
from enum import Enum, auto

from typing_extensions import ClassVar


class HistoricalDataType(Enum):
    NO_DATA = auto()
    DATA = auto()


class HistoricalDataHandlerModel(ABC):
    """
    Base model for historical storage handlers.
    """

    historical_data: ClassVar[HistoricalDataType]

    def __init__(self):
        pass
