#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0

from enum import StrEnum
from typing import Annotated, Any

import xarray as xr
from pydantic import BaseModel, StringConstraints, conint


class ForgeUnitSystem(StrEnum):
    """An enumeration of the different supported unit systems.

    Attributes
    ----------
        ORIGINAL (str):
            The original unit system of the parameter, which is used for unit conversion.
            This is the default unit system for the parameter.
        SI (str):
            The SI unit system of the parameter, which is used for unit conversion.
            This is the standard unit system for scientific measurements.
        IMPERIAL (str):
            The imperial unit system of the parameter, which is used for unit conversion.
            This is the unit system used in the United States and some other countries.
        US (str):
            The US unit system of the parameter, which is used for unit conversion.
            This is the unit system used in the United States and some other countries.

    """

    ORIGINAL = "original"
    SI = "si"
    IMPERIAL = "imperial"
    US = "us"


class ForgeParameter(BaseModel):
    """"""

    id: Annotated[str, StringConstraints(min_length=2, max_length=12, pattern=r"^[a-z]+$")]

    def convert_data_array_to_original_values(
        self, value: xr.DataArray, current_unit_system: ForgeUnitSystem
    ) -> xr.DataArray:
        """The base unit of the parameter, which is used for unit conversion.

        Any data downloaded for a model is assumed to be set to this base unit.

        Returns
        -------
            Any: The base unit of the parameter.

        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get_si_value(self, value: Any, current_unit_system: ForgeUnitSystem = ForgeUnitSystem.ORIGINAL) -> Any:
        """The SI unit of the parameter, which is used for unit conversion.

        Returns
        -------
            Any: The SI unit of the parameter.

        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get_imperial_value(self, value: Any, current_unit_system: ForgeUnitSystem = ForgeUnitSystem.ORIGINAL) -> Any:
        """The imperial unit of the parameter, which is used for unit conversion.

        Returns
        -------
            Any: The imperial unit of the parameter.

        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get_us_value(self, value: Any, current_unit_system: ForgeUnitSystem = ForgeUnitSystem.ORIGINAL) -> Any:
        """The US unit of the parameter, which is used for unit conversion.

        Returns
        -------
            Any: The US unit of the parameter.

        """
        raise NotImplementedError("Subclasses must implement this method.")


class ECCODESFactor(BaseModel):
    """A data class to hold the data needed to define a ECCODES parameter.

    For consistent harmonization, ECCODES are used as the basis for this harmonization of parameters, as they are
    widely used in meteorological data formats. The ECCODES parameters are defined by the ECMWF (European Centre for
    Medium-Range Weather Forecasts) and are used in various meteorological data formats.

    Attributes
    ----------
        eccodes_id (int):
            The ECCODES ID of the parameter, which is a unique identifier for the parameter in the ECCODES system.
            The ID must be between 1 and 254.
        name (str):
            The name of the parameter, which must be between 8 and 120 characters long.
        short_name (str):
            A short name for the parameter, which must be between 1 and 8 characters long.
        description (str):
            A description of the parameter, which must be between 12 and 512 characters long.
        unit (str):
            The unit of measurement for the parameter, which must be between 1 and 20 characters long.
            Should be expressed as a Pint unit.
        si_unit (str):
            The SI unit of measurement for the parameter, which must be between 1 and 20 characters long.
            Should be expressed as a Pint unit.
        imperial_unit (str):
            The imperial unit of measurement for the parameter, which must be between 1 and 20 characters long.
            Should be expressed as a Pint unit.
        us_unit (str):
            The US unit of measurement for the parameter, which must be between 1 and 20 characters long.
            Should be expressed as a Pint unit.

    """

    eccodes_id: conint(ge=1, le=254)
    name: Annotated[str, StringConstraints(min_length=8, max_length=120)]
    short_name: Annotated[str, StringConstraints(min_length=1, max_length=8)]
    description: Annotated[str, StringConstraints(min_length=12, max_length=512)]
    si_unit: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    imperial_unit: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    us_unit: Annotated[str, StringConstraints(min_length=1, max_length=20)]


class ForgeECCODESParameter(ForgeParameter):
    """A variant ForgeParameter class that establishes a link to the ECCODES parameter via the Pint unit system.

    Attributes
    ----------
        eccodes_id (int):
            The equivalent ECCODES ID for the parameter, which is a unique identifier for the parameter in the ECCODES system.
            The ID must be between 1 and 254.
            This is used to establish a link between the Forge parameter and the ECCODES parameter, which can then be
            used to convert units via Pint.

    """

    eccodes_factor: ECCODESFactor
    base_unit: Annotated[str, StringConstraints(min_length=1, max_length=20)]

    def get_base_value(self, value: Any, current_unit_system: ForgeUnitSystem) -> Any:
        """Implementation of the get_base_value method."""
        if current_unit_system == ForgeUnitSystem.ORIGINAL:
            # If the current unit system is the original, return the value as is
            return value

        target_pint_unit_str = self.base_unit
        current_pint_unit_str = (
            self.eccodes_factor.si_unit
            if current_unit_system == ForgeUnitSystem.SI
            else self.eccodes_factor.imperial_unit
            if current_unit_system == ForgeUnitSystem.IMPERIAL
            else self.eccodes_factor.us_unit
        )

        # Use Pint to convert the value to the target unit

        return self.base


class ForgePintParameter(ForgeParameter):
    """A variant ForgeParameter class that can't harmonize but still allows for unit conversion via Pint.

    Attributes
    ----------


    """

    ...


class ForgeCustomParameter(ForgeParameter):
    """A variant ForgeParameter class that can't harmonize and doesn't allow for unit conversion via Pint.

    This class allows for custom unit conversion to be defined by the user, but does not provide any

    Attributes
    ----------

    """

    ...
