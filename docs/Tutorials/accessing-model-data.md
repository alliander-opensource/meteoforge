# How to access model data

## On this page

Accessing meteorological model data is an important task in meteorology and climatology and likely your main goal in
using (parts of) this project. Because the main purpose of this project is to provide a unified interface to different
models and sources, access may vary slightly between models.

In this tutorial, we will show you how to access data from the different models based on the base interface for models.
If you are interested in a specific model, we recommend to check the documentation of that model instead.

## Accessing model - methods

There are three main methods to access model data:

1. ### **Accessing data using the full API:**

   This is easily the most flexible way and easy method to access model data. It allows you to access all the data
   held in any model of any source that has been loaded into the project. This method is recommended for users that
   want to access multiple models, provide API interaction with other project, or simply mess around with the API's
   swagger interface to see what is available.

   Please note that this method may require some additional setup for sources and models made for the project outside
   the project's **weather-provider-source repository**.

2. ### **Accessing data using the Controller class interface:**

   If you wish to have all the advantages of the full API, but do not wish to run an entire API server around it, you
   can also choose to access the data using the Controller class interface. This method is recommended for users that
   are familiar with basic Python and want to access the data for multiple sources and models in a more programmatic
   way.

3. **Accessing via a source class interface**:

   A more direct method of access is the source class based interface. Simply by installing the package associated
   with the source you wish to access, you can access that data directly and use its access methods to acquire and
   transform it as needed. Used if you are interested in multiple models from the same source. This method is
   recommended for users that are familiar with basic Python and want to access the data for a singular source in a
   more programmatic way.

4. **Accessing via a model class interface**:

   The most direct method of access is the model class based interface. Simply by installing the package associated
   with the source you wish to access, and importing the model you want to access, you can access the data for that
   model directly and use its access methods to acquire and transform it as needed. Used if you only are interested in
   a single model. This method is recommended for users that are familiar with basic Python and want to access the data
   for a singular source in a
   more programmatic way.

## Accessing a model - Parameters

### Base parameters

The base parameters for accessing a model are the same for all models regardless. The following parameters are
available:

- **location**:

  A location for which the data is requested. Consists of an x and y coordinate pair, optionally
  followed by the coordinate system these refer to. The format is two floats and an integer separated by a comma.

  The first float represents the latitude, while the second represents the longitude. The integer represents the
  coordinate system. The coordinate system is optional and defaults to 4326 (WGS84). Please note that the coordinate
  system is not always supported by the model. If this is the case, the model will return an error.

- **requested_factors**:

  A list of factors for which the data is requested. The format is a list of strings separated by commas. The strings
  represent the names of the factors. Please note that not all models support all factors. If this is the case, the
  model will return an error. Every model can supply a list of supported factors via its metadata or factors property.

### Timeframe parameters

- **output_period**:

  The period of time for which the data is requested. This should be a range of datetimes.
  The format is two ISO 8601 datetime objects separated by a comma. The first datetime represents the start of the
  period, while the second represents the end of the period. Please note that data will be returned based on the UTC
  equivalent of the datetime objects, even if the given and/or requested timezones are different.

  **Please note that this field will not be available if the model in question only supports a single moment in time**

- **predictive_period**:

  The period of time matching one or more requested forecast moments in time. The format is one or two ISO 8601 datetime
  objects (separated by a comma if there are two). If only one datetime object is given, the model will return the
  forecast for that moment in time if one is available. If two datetime objects are given, the model will return any
  forecast for the period between the two datetime objects. Please note that data will be returned based on the
  UTC equivalent of the datetime objects, even if the given and/or requested timezones are different.

  **Please note that this field will only be available if the model in question is predictive in nature and supports
  the retrieval of multiple predictions**
