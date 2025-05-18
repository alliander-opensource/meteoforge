#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0

from typing import Annotated

from meteoforge_libraries.formats.annotations import ValidIdentifier, ValidURL
from meteoforge_libraries.formats.factors import ForgeParameter
from pydantic import BaseModel, StringConstraints


class ForgeModelIdentity(BaseModel):
    """A data structure to hold the identity of a meteorological model.

    Attributes
    ----------
        id (str):
            A unique identifier for the model, consisting of lowercase letters only.
            The ID must be between 3 and 12 characters long.
        name (str):
            A human-readable name for the model, starting with an uppercase letter.
            The name can contain spaces and must be between 4 and 32 characters long.
            It can include letters, digits, and spaces, but cannot start with a digit.
        description (str):
            A brief description of the model, which can include letters, digits, and spaces.
            The description must be between 12 and 256 characters long.
        information_url (str):
            A URL providing more information about the model.
            The URL must start with 'http', 'https', 'ftp', or 'ftps' and must be between 12 and 256 characters long.
        license (str):
            The license under which the model's data is distributed.
            The license can refer to a specific license type, specify a URL to the license text and/or a description
            of how the license operates.
            The license must be between 4 and 256 characters long.

    """

    id: ValidIdentifier
    name: Annotated[
        str, StringConstraints(min_length=4, max_length=32, pattern=r"^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z0-9]*)*$")
    ]
    description: Annotated[str, StringConstraints(min_length=12, max_length=256)]
    information_url: ValidURL
    license: Annotated[str, StringConstraints(min_length=4, max_length=256)]

    @property
    def metadata(self) -> dict:
        """Return the model metadata."""
        return {
            "ID": self.id,
            "Name": self.name,
            "Description": self.description,
            "Information URL": self.information_url,
            "License": self.license,
        }


class ForgeBaseModel:
    """Base class for all meteorological models in the Meteoforge project."""

    def __init__(self, identity: ForgeModelIdentity, parameter_list: list[ForgeParameter]):
        """..."""
        self.identity = identity
        self.factors = parameter_list
        self._parameter_list = []

    @property
    def id(self):
        """Return the model ID."""
        return self.identity.id

    @property
    def metadata(self) -> dict:
        """Return the model metadata."""
        return ...

    def fetch_model_data(self, requested_parameters: list[str] | None = None, **kwargs):
        """Fetch model data for the specified parameters."""
        # Validate requested parameters
        self._validate_requested_parameters(requested_parameters)

        # Download the requested data:
        downloaded_data = self._download_data(requested_parameters, **kwargs)

        # Process the downloaded data:
        processed_data = self._process_data(downloaded_data, requested_parameters, **kwargs)

        # Return the processed data:
        return processed_data

    def _validate_requested_parameters(self, requested_parameters: list[str] | None) -> None:
        """Validate the requested parameters."""
        ...

    def _download_data(self, requested_parameters: list[str] | None, **kwargs):
        """Download the requested data."""
        raise NotImplementedError("ForgeModel classes must implement this method!")

    def _process_data(self, downloaded_data, requested_parameters: list[str] | None, **kwargs):
        """Process the downloaded data."""
        raise NotImplementedError("ForgeModel classes must implement this method!")

    def __repr__(self):
        return f"ForgeModel<{self.identity.id}>: <...>"  # TODO: Add inherited classes list
