# SPDX-FileCopyrightText: 2026 2025-2026 Contributors to the MeteoForge project
#
# SPDX-License-Identifier: MPL-2.0

from meteoforge.core.modelclasses.projection_handler.base_model import MeteoProjectionHandlerModel, ProjectionType


class MeteoNoCastingHandler(MeteoProjectionHandlerModel):
    """This class is for handling scenarios where no casting (neither nowcasting nor forecasting) is required.

    It serves as a placeholder or default handler in the MeteoForge framework.
    """

    forecast_support = ProjectionType.NONE

    def __init__(self):
        """Initialize the no casting handler."""
        super().__init__()
