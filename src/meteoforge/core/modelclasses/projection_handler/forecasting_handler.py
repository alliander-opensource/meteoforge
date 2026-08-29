# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.projection_handler.base_model import MeteoProjectionHandlerModel, ProjectionType


class MeteoForeCastingHandler(MeteoProjectionHandlerModel):
    """This class is responsible for handling forecasting operations in the MeteoForge framework.

    It provides methods to process and analyze weather data for short-term and long-term forecasting.
    """

    forecast_support = ProjectionType.FORECAST

    def __init__(self):
        """Initialize the forecasting handler."""
        super().__init__()
