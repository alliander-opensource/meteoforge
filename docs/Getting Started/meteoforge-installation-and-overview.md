---
icon: lucide/package-check
---

<!--
  SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
  SPDX-License-Identifier: MPL-2.0
-->

# MeteoForge Installation and Overview

## Installing the MeteoForge Package

This section explains how to install the `meteoforge` package using some of the most common Python package installers.

**Context differences:**

- **pip** installs the package globally (system or user) or into a virtual environment if one is activated. This is suitable for quick, system-wide installs or for use in scripts and CLI tools.
- **Poetry** and **UV** are project-based tools. They add the package as a dependency to your project's configuration and lock files, ensuring reproducible environments. Use these when working within a project directory to manage dependencies in an isolated, version-controlled way.

Regardless of context, the `meteoforge` package can be directly installed from PyPI using the following methods:

**Using pip:**

``` bash
pip install transformer-thermal-model
```

**Adding to a project using Poetry:**

``` bash
poetry add transformer-thermal-model
```

**Adding to a project using UV:**

``` bash
uv add transformer-thermal-model
```

## Verifying the installation

To verify that the installation was successful, within the environment the package was installed, run the following command to verify proper installation.

``` bash
meteoforge-validation
```

Proper installation should result in a version display resembling this example:

``` console
MeteoForge - version 1.0.1
- Important Meteorological Dependencies:
  - eccodes: 2.46.0
  - grib: 0.9.15.1
- Important File Formatting:
  - netcdf4: 1.7.4
  - zarr: 3.1.6
```

If installation succeeded but there are problems with the validation of any essential components you may get a slightly different report (once again an example):

``` console
MeteoForge - version 1.0.1
- Important Meteorological Dependencies:
  - eccodes: 2.46.0
    -- VALIDATION FAIL: Could not process code list, indicating an invalid installation
  - grib: 0.9.15.1
- Important File Formatting:
  - netcdf4: 1.7.4
  - zarr: 3.1.6

Validation of one or more components failed. The MeteoForge team suggests trying a clean install, and if that does not work, checking on our repository's Issues page at:
https://github.com/alliander-opensource/meteoforge/issues
```

In this case you should follow the given instructions and either try again using a clean install or check the Issues pages for any issues resembling yours.

If installation failed completely or you are simply not within the proper installation environment the command should simply not be recognized.

## Basic Usage of the MeteoForge Package

Basic usage of the MeteoForge package mostly involves using the package to evaluate coordinates and periods using the MeteoForge spatial and temporal classes.

 --- TODO ---
<!-- TODO: Write this part -->

## Advanced Uses of the MeteoForge Package

Advanced usage of the MeteoForge package would involve creating or managing your very own sources and models. For this, we suggest you check the related pages, starting by creating a minimal 'source', and then adding your first 'model' to that.

- [Start creating your own source →](source-buildup.md)
- [Start creating your own model →](model-buildup.md)
