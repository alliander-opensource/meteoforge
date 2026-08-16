# SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
# SPDX-License-Identifier: MPL-2.0

from abc import ABC

from meteoforge.core.modelclasses.historical_data_handler.base_model import HistoricalDataHandlerModel
from meteoforge.core.modelclasses.projection_handler.base_model import MeteoProjectionHandlerModel
from meteoforge.core.modelclasses.spatial_management_handler.base_model import SpatialManagementModel
from meteoforge.core.modelclasses.storage_management_handler.base_model import StorageManagementModel
from typing_extensions import ClassVar


class MeteoModel(
    SpatialManagementModel,
    HistoricalDataHandlerModel,
    MeteoProjectionHandlerModel,
    StorageManagementModel,
    ABC,
):
    """Base class for MeteoForge models."""

    name = ClassVar[str]
    version = ClassVar[str]
