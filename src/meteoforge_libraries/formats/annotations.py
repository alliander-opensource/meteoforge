#!/usr/bin/env python

#  SPDX-FileCopyrightText: 2019-2025 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0

from typing import Annotated

from pydantic import AnyUrl, StringConstraints

ValidIdentifier = Annotated[str, StringConstraints(min_length=3, max_length=12, pattern=r"^[a-z]+$")]


class ValidURL(AnyUrl):
    allowed_schemes = {"http", "https", "ftp", "ftps"}
    max_length = 256
