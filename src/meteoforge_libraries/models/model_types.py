#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0

from meteoforge_libraries.models.base_model import ForgeBaseModel
from meteoforge_libraries.models.model_mixins import HistoricalModelMixin, PredictiveModelMixin, SpatialModelMixin


class ForgeModelWithLocations(SpatialModelMixin, ForgeBaseModel):
    pass


class ForgeModelWithLocationsAndForecast(SpatialModelMixin, PredictiveModelMixin, ForgeBaseModel):
    pass


class ForgeModelWithLocationsAndHistory(SpatialModelMixin, HistoricalModelMixin, ForgeBaseModel):
    pass


class ForgeModelWithLocationsAndForecastAndHistory(
    SpatialModelMixin, PredictiveModelMixin, HistoricalModelMixin, ForgeBaseModel
):
    pass
