#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0
from meteoforge_libraries.formats.locations import ForgeLocation, ForgeLocations, ForgePolygonalArea
from meteoforge_libraries.formats.periods import ForgePeriod

"""This module contains mixin classes for different types of meteorological model extensions.

The mixins are designed to be used as mixins for the ForgeBaseModel class, allowing for the addition of specific
functionality and validation steps to the base model class.

The mixins include:
- PredictiveModelMixin: A mixin class for predictive models, which adds a forecast horizon to the model.
- HistoricalModelMixin: A mixin class for historical models, which adds a historical period to the model.

"""


class PredictiveModelMixin:
    """A mixin class for predictive models."""

    def __init__(self, forecast_horizon: ForgePeriod, *args, **kwargs):
        """This mixin class is used to add a forecast horizon to a predictive model."""
        super().__init__(*args, **kwargs)
        if self.properties:
            if not forecast_horizon.is_valid() or not isinstance(forecast_horizon, ForgePeriod):
                raise ValueError("Forecast horizon was not set with a valid ForgePeriod.")
            self.properties["Forecast Horizon"] = forecast_horizon

    def fetch_model_data(self, *args, forecast_period: ForgePeriod | None = None, **kwargs):
        # Validate and handle forecast_period
        self._validate_forecast_period(forecast_period)

        # And continue with the rest of the method
        return super().fetch_model_data(forecast_period=forecast_period, *args, **kwargs)

    def _validate_forecast_period(self, forecast_period: ForgePeriod | None) -> None:
        """Validate the forecast period."""
        if not isinstance(forecast_period, ForgePeriod):
            raise ValueError("Forecast period must be a ForgePeriod instance.")

        if not forecast_period.is_valid():
            raise ValueError("Forecast period is not valid.")

        if not forecast_period.is_within(self.forecast_horizon):
            raise ValueError("The requested forecast period does not lie within the forecast horizon.")

    def __repr__(self):
        return super.__repr__() + f", Forecast Horizon: {self.forecast_horizon}"


class HistoricalModelMixin:
    """A mixin class for historical models."""

    def __init__(self, supported_historical_period: ForgePeriod, *args, **kwargs):
        self.supported_historical_period = supported_historical_period

    def fetch_model_data(self, *args, historical_period: ForgePeriod, **kwargs):
        # Validate and handle history_period
        self._validate_historical_period(historical_period)

        # And continue with the rest of the method
        return super().fetch_model_data(historical_period=historical_period, *args, **kwargs)

    def _validate_historical_period(self, historical_period: ForgePeriod) -> None:
        """Validate the historical period."""
        if not isinstance(historical_period, ForgePeriod):
            raise ValueError("Historical period must be a ForgePeriod instance.")

        if not historical_period.is_valid():
            raise ValueError("Historical period is not valid.")

        if not historical_period.is_within(self.historical_period):
            raise ValueError("The requested historical period does not lie within the model's historical period.")

    def get_supported_filters(self):
        filters = super().get_supported_filters()
        filters["historical_period"] = True
        return filters


class SpatialModelMixin:
    """A mixin class for models that support spatial filters."""

    def __init__(self, allowed_area: tuple[ForgeLocation, ...] | ForgePolygonalArea, *args, **kwargs):
        """Initialize the mixin with a list of allowed area coordinates."""
        self.allowed_area = allowed_area

    def fetch_model_data(self, *args, location: ForgeLocations, **kwargs):
        # Validate and handle spatial filters
        self._validate_spatial_filter(location)
        if isinstance(location, ForgeLocation):
            location = [location]

        # And continue with the rest of the method
        return super().fetch_model_data(location=location, *args, **kwargs)

    def _validate_spatial_filter(self, locs: ForgeLocations) -> None:
        """Validate the spatial filter."""
        ...

    def get_supported_filters(self):
        filters = super().get_supported_filters()
        filters["spatial_filter"] = "polygon"
        return filters
