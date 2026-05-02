---
icon: lucide/cloud-cog
---

<!--
  SPDX-FileCopyrightText: 2025-2026 Contributors to the MeteoForge project
  SPDX-License-Identifier: MPL-2.0
-->

# MeteoForge Sources

## Introduction to Sources

Sources are how MeteoForge discerns between the different origins of the meteorological models it supports. Multiple sources often have similar models in nature and name to another.

To make sure we can keep apart these sometimes near identical (in name and format) models, we group models within sources. A singular source may contain anywhere from a singular model to large groups of models. A model must belong to only exactly one singular source however to allow for proper validation and activation.

Never is the identity of a source allowed to exist twice within a project, and never are two models with the same identity allowed to exist within the same source.

## Using Sources

Source interactions are mostly the same as those for Models, with a quite number of interactions being merely gateways to Model interactions.

For a complete and up-to-date list of these interactions, please check the Technical Documentation page:
...
<!-- TODO: Place link -->

## Constructing a New Source

...

## Validating Your Source

Simply start by importing your source within a Python Interpreter. If anything is structurally wrong with your Source (or an underlying Model), you should get an error explaining what is wrong or missing to get your Source (or Model) to work.

If your are successful, you only need to make sure the same can be said for all of the models involved. As models are only loaded when needed and unloaded after, we'll need to run the `validate()` action from our source:

### Valid Sources

``` py
> from meteoforge.sources import <my_custom_source>
> <my_custom_source>.validate()
```

``` console
Source:
- Name: <My source's name>
- ID: <My source's identifier>
- Description: <My source's description>
Models:
- Validating Model: a - OK
- Validating Model: b - OK
- Validating Model: c - OK
```

As you can see, valid Sources should result in some basic information on the Source and a successful model check for each model specified within the Source.

### Invalid Sources

``` py
> from meteoforge.sources import <my_custom_source>
> <my_custom_source>.validate()
```

``` console
Source:
- Name: <My source's name>
- ID: <My source's identifier>
- Description: <My source's description>
Models:
- Validating Model: a - OK
- Validating Model: b - OK
- Validating Model: c - FAIL
  - Model c: Model is missing data on what period(s) are allowed to be requested
```

As you can see, any Models that are technically properly configured, but can't properly validate, will generate error messages trying to specify what is wrongly configured or set.

If any models are not valid, you should run their validators for more information on what is wrong with them.
