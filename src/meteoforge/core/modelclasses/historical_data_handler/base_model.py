# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from abc import ABC
from enum import Enum, auto
from typing import ClassVar


class HistoricalDataType(Enum):
    """Enum representing the type of historical data available."""

    NO_DATA = auto()
    DATA = auto()


class HistoricalDataHandlerModel(ABC):
    """Base model for historical storage handlers."""

    historical_data: ClassVar[HistoricalDataType]

    def __init__(self):
        """Initialize the historical data handler model."""
        raise NotImplementedError("This method should be implemented by subclasses.")
