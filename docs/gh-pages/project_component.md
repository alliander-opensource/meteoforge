# MeteoForge - Core

## Index

1. Responsibilities

## Responsibilities

At the center of the entire MeteoForge project, the core system for this project is responsible for all of the active
processing and handling of meteorological data. This includes the following responsibilities:

### Base classes for meteorological resources

The core system is responsible for a number of base classes, interface classes and mix-in classes that allow the system
to work with minimal effort. The most prominent of these are:

- Base classes for interaction with meteorological models. Classes aimed at identifying and communicating with sources
  and models are a part of this, as well as classes that help consolidate over multiple sources and models like a
  controller-class for accessing multiple sources and models or an storage agent-class for managing and updating locally
  stored data for those sources and models.
- Interface classes aimed at streamlining and simplifying working with common factors like locations and times and
  meteorological parameters regardless of your intended use.
- Mix-in and supportive classes to help base classes to only have to deal with those aspects that are relevant for that
  instance of that base class.
  Think of classes that allow a model to expand to use predictive data as well, or at the opposite spectrum make sure a
  class doesn't always need locational awareness if the model in question does not work with locations.

### Parameter standardization and processing

The core system also is responsible for making sure that harmonization works, which means that it is also responsible
for handling multiple types of locations, timezones and parameter formatting and making sure these can interact with
another. As such it is capable of translating numerous coordinate systems, timezones and parameters into project set
standards and from there back into any other of these numerous options.

To do this the project uses the following standards wherever possible to harmonize data:

- ***Coordinate system harmonization:***
  Via the WGS84 (World Geodetic System 1984) latitude and longitude system, using **pyproj** library.
- ***Timezone harmonization:***
  Via UTC and the Python default **datetime** library.
- ***Meteorological parameter harmonization:***
  Via the ECCODES parameters database. Being both a default standard for GRIB files and the European Centre for
  Medium-Range Weather Forecasts, a lot of models will already support these and most other models are likely to use
  parameters that are equivalents to these parameters.
  Any exceptions to this would probably not be able to be harmonized anyway, meaning harmonization can not be supported
  for these factors.
