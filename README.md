[//]: # (SPDX-FileCopyrightText: 2024-2025 Copyright Contributors to the MeteoForge project)

[//]: # (SPDX-License-Identifier: MPL-2.0)

# MeteoForge - Core System

[![License: MPL2.0](https://img.shields.io/badge/License-MPL2.0-informational.svg)](https://github.com/alliander-opensource/weather-provider-libraries/LICENSE.md)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=bugs)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_meteoforge&metric=coverage)](https://sonarcloud.io/summary/new_code?id=alliander-opensource_meteoforge)

<div align="center">
  <img src="/docs/images/meteoforge_logo.png" alt="MeteoForge" width="25%" />
</div>

## Index

- [On the MeteoForge project](#on-the-meteoforge-project)
- [A bit more information on MeteoForge: Libraries](#a-bit-more-information-on-the-core-system)
- [How to install](#how-to-install)
- [View License](./LICENSE.md)

## On the "MeteoForge" project

The MeteoForge project evolved from the original Weather Provider API project. It aims to provide a unified interface
for accessing and processing meteorological data from various sources. It is modular and extensible, allowing users to
easily add new sources and models.

The project consists of three main components:

1. **The MeteoForge API**
   A RESTful API built with FastAPI. It provides a unified interface for accessing data from sources built with the
   MeteoForge Libraries. It is OpenAPI-compliant and easy to deploy via Docker or custom solutions.

2. **The MeteoForge Core System**
   Core functionality for accessing and processing meteorological data, including support for file formats, data
   transformation, and extensibility. Includes base classes for sources and models.

3. **The MeteoForge Sources**
   A collection of source packages based on Alliander models. Sources are installable independently and provide access
   to meteorological models usable standalone or with the API.

## A bit more information on the Core System

### The goal of the Core System component

The Core System provides base and interface classes as well as utilities for accessing and processing meteorological
data. They are designed for use with the API and source packages and not meant for standalone use.

They offer tools for easily integrating new datasets and standardizing data processing workflows.

### How it works

#### **Sources govern models**

Each model belongs to a source. This allows similar models from different sources to coexist and be validated
consistently.

#### **Models are generic but unique**

Models use a shared interface but must implement their own data retrieval and formatting logic. They’re standardized in
usage but uniquely implemented.

#### **Equalizing the models via ECCODES**

The Core System uses [ECCODES](https://confluence.ecmwf.int/display/ECC) to decode GRIB/BUFR data and standardize
parameters. Unit conversion is handled with [Pint](https://pint.readthedocs.io/).

> **An example**
>
> _A model defines a "200 meter wind speed" in Beaufort. The ECCODES parameter 228241 corresponds to "200 metre wind_
> _speed" in m/s._
> _The Core System can convert Beaufort to m/s using its registry of standard parameters and Pint-based conversions._

## How to install

You can install the MeteoForge Core System via pip or poetry.

With pip:

```sh
pip install meteoforge
```

With poetry:

```sh
poetry add meteoforge
```
