.. coding=utf-8
.. SPDX-FileCopyrightText: 2019-2023 Alliander N.V.
.. SPDX-License-Identifier: MPL-2.0

.. image:: https://img.shields.io/badge/License-MPL2.0-informational.svg
   :target: https://github.com/alliander-opensource/weather-provider-libraries/LICENSE.md
   :alt: License: MIT
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=alert_status
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Quality Gate Status
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=sqale_rating
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Maintainability Rating
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=security_rating
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Security Rating
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=vulnerabilities
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Vulnerabilities
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=bugs
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Bugs
.. image:: https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-libraries&metric=coverage
   :target: https://sonarcloud.io/summary/new_code?id=alliander-opensource_weather-provider-libraries
   :alt: Coverage

.. image:: ./docs/logo/meteoforge_logo.png
    :alt: MeteoForge
    :align: center
    :width: 25%

Index:
======
- `On the MeteoForge project <#on_the_meteoforge_project>`_
- `A bit more information on MeteoForge: Libraries <#a_bit_more_information_on_meteoforge>`_
- `How to install <#how_to_install>`_
- `More information? <#more_information>`_
- `View License <./LICENSE.md>`_


.. _on_the_meteoforge_project:

On the MeteoForge project:
==========================

The MeteoForge project is the project that evolved from the original Weather Provider API project. It is a project that
aims to provide a unified interface for accessing and processing meteorological data from various sources. The project
is designed to be modular and extensible, allowing users to easily add new sources and models as needed. The project
consists of three main components:

1. **The MeteoForge API**

   This component provides a RESTful API for accessing meteorological data from various sources based on FastAPI. It is
   built on top of the MeteoForge Libraries and provides a unified interface for accessing data from different sources
   provided by the MeteoForge Sources or other compatible sources made from the base classes of the MeteoForge
   Libraries. The API is designed to be easy to use and provides a wide range of features for accessing and processing
   data with minimal configuration. The API is fully compliant with the OpenAPI standard and can be easily deployed
   using Docker images or custom deployment methods. The API is designed to be scalable and can be easily extended to
   support new sources and models as needed.

2. **The MeteoForge Libraries**

   This component provides the core functionality for accessing and processing meteorological data. It includes a wide
   range of tools and libraries for working with meteorological data, including support for various file formats,
   data transformation, and data processing. The Libraries are designed to be modular and extensible, allowing users to
   easily add new features and functionality as needed. The Libraries also provide a set of base classes for creating
   new sources and models, making it easy to integrate new datasets into the system.

3. **The MeteoForge Sources**

   This component provides a a basic collection of sources for accessing meteorological data from various providers
   based on the original models constructed for Alliander. Each source is designed to be modular and extensible,
   allowing collaborators to easily add new models as needed. The sources are designed to be easy to use separately
   and provide a wide range of features for accessing and processing data and generate their own packages for
   distribution and installation. Merely installing a source package is enough to use the source and its models both
   separately and in combination with the API, though further configuration may be needed to use a source in a
   specific context.



.. _a_bit_more_information_on_meteoforge:

A bit more information on MeteoForge: Libraries
===============================================

The goal of the Libraries component:
------------------------------------
The goal of the Libraries component is to provide a set of base classes and utilities for accessing and processing
meteorological data from various sources. The Libraries component is designed to be modular and extensible, allowing
collaborators to easily add functionality for new sources and models as needed, as well as to provide a set of base
classes for easily creating new sources and models. The Libraries component is designed to be used in conjunction with
the API, the Sources component and other compatible sources, and cannot be used separately outside of creating new
sources and models.

The Libraries component is designed to be easy to use and will provide plenty of support for accessing and processing
data from various sources as well as help you through the process of creating new sources and models.

How it works:
-------------

Sources govern models:
**********************

As stated, the MeteoForge project is meant to be modular and extensible, allowing users to easily add new sources and
models as needed. This means that any number of models should be able to be used in combination with each other.

However, similar models with similar functionality may exist for different sources. To allow for this, each model needs
to be governed by a source. This means that each model is part of a source and cannot be used outside of that source.
This allows for models under the same name and functionality to be used in combination with each other, while still
being distinct from each other.

Sources are also able to validate each of their models in one go, allowing for a more efficient way of validating
models.

Models are generic but unique:
******************************

While this sounds like a contradiction, it is not.
The models are generic in the sense that they are designed to be used with the (nearly) same interface for each base
type of meteorological model, but unique in the sense that every model will need a separate implementation for
retrieving and formatting the data. So while the interface for each model is the same, and the base implementation
behind that interface will also be, at the import and configuration level, the models are very unique.

Equalizing the models via ECCODES:
**********************************

To be able to equalize the models, the Libraries component uses ECCODES. This is a library for decoding and encoding
GRIB and BUFR files. It is a library that is widely used in the meteorological community and is designed to be fast
and efficient. ECCODES also has an extensive parameter database that can be used to look up standard parameters and
their units.

By using this database as a reference and using Pint for unit conversion with such parameters as a base, the Libraries
component is able to equalize the models and provide a unified interface for accessing and processing meteorological
factors into standardized unit(s) (systems) and file formats.

An example:
~~~~~~~~~~~

  A model contains a factor "200 meter wind speed" indicating the wind speed at 200 meters above ground level.
  This factor is supplied in Beaufort. Looking up the parameter in the ECCODES database, we find that the
  "200 metre wind speed" is standard parameter 228241 with default unit "m * s^-1" (meters per second).

  The Libraries component only needs to know that the factor is equivalent to the standard parameter 228241 and that the
  supplied unit is Beaufort. The Libraries component has a register of each standard parameter and its default unit as
  well as a list of supported unit systems and their target units. The Libraries component can then use to convert the
  supplied unit to the target unit using Pint.


.. _how_to_install:

How to install:
===============
Installation can be done via pip or poetry. The Libraries component is available on PyPI and can be installed
using the following command for pip:

.. code-block:: shell

   pip install meteoforge-libraries

or for poetry:

.. code-block:: shell

   poetry add meteoforge-libraries

.. note:: Installing only the Libraries component is not enough to access models and/or sources in any way.
          You need to install the API or a source package to access models and/or sources. Both will also install
          the Libraries component as a dependency.

.. _more_information:

Need a bit more information?
----------------------------

For a far more extensive source of information, please visit the GitHub Pages at:
 https://alliander-opensource.github.io/weather-provider-libraries/
