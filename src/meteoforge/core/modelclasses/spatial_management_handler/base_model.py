import logging
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import ClassVar

from meteoforge.spatial_temporal.locations import MFLocation


class SpatialType(Enum):
    GRIDPOINT = auto()  # Represents a grid point in a spatial grid.
    LOCATION = auto()  # Represents a specific location described by the class itself.


class SpatialManagementModel(ABC):
    """Base class for spatial management handlers."""

    spatial_type = ClassVar[SpatialType]

    def __init__(self):
        """Initializes the spatial management handler."""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(f"Initializing {self.__class__.__name__} with spatial type: {self.spatial_type.name}")

    @property
    def meta(self) -> dict:
        """Returns metadata about the spatial management handler."""
        return {"class_name": self.__class__.__name__, "spatial_type": self.spatial_type.name}

    @abstractmethod
    def find_nearest(self, location: MFLocation) -> dict:
        """Finds the nearest spatial point to the given location.

        Args:
            location (MFLocation): The location to find the nearest neighbor for.

        Returns:
            dict: Information about the nearest spatial point.
        """
        raise NotImplementedError("Subclasses must implement the find_nearest method.")
