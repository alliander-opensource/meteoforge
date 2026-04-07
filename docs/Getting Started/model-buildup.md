---
icon: lucide/cloud-download
---

# MeteoForge Models

## Introduction to Models

Models are how MeteoForge interacts with meteorological datasets. Models contain information on how to connect to these datasets, what data is stored there, how to download it and how to reformat it into other common formats.

Each model should be made accessible from a source. While the model class format itself does allow for independent use, and users are of course free to do exactly that, most MeteoForge components are written with the "Source containing Models" system in mind.

As such standalone models aren't supported by, for example the MeteoForge API system.

## Using Models

Model interactions are grouped in the following interaction types:

1. Informing the user on the properties of the dataset and the capabilities of the model to acquire that data.
2. Supplying the user with that data based on requests made using those capabilities.
3. Reformatting data acquired from the model into other unit- or filesystems
4. (Optionally) If configured, supplying capabilities to store and retrieve the data via a data storage/cache.



## Constructing a New Model
...

## Validating Your Model

Simply start by importing your Model within a Python Interpreter. If anything is structurally wrong with your Model, you should get an error explaining what is wrong or missing to get your Model to work.

To confirm that everything functions of your model, just run the `validate()` method.

#### Valid Models:

``` py
> from meteoforge.sources.<my_custom_source>.models import <my_custom_model>
> <my_custom_model>.validate()
```
``` console
Model:
- Name: <My model's name>
- ID: <My model's identifier>
- Description: <My model's description>
Properties:
- Request Range: from (2020-1-1 00:00) to (2026-4-6 12:22)
- Historical/Predictive: Historical
- Base location type: KNMI Weather Station
- Supports Spatial Conversion: Yes
Parameters:
- 2m Temperature: K > Convertable
- 2m Wind speed : Bft > Convertable
- 10m Vision range: Bunny Vision Range > Non-Convertable
```

Valid Model objects should return a listing of model properties without errors. Please note that a valid model can still contain meteorological parameters that aren't considered convertable into a standard unit format. When converting data, these parameters will remain unchanged and retain their specific unit types.

#### Invalid Models

If Models are constructed properly, but certain properties or settings have issues validating as properly functioning, you may get another response:

``` py
> from meteoforge.sources.<my_custom_source>.models import <my_custom_model>
> <my_custom_model>.validate()
```
``` console
Model:
- Name: <My model's name>
- ID: <My model's identifier>
- Description: <My model's description>
Properties:
- Request Range: FAIL
    - Request Range could not properly translate into a currently valid temporal range.
- Historical/Predictive: FAIL
    - Model type was set to Predictive, but no valid predictive range was configured.
- Base location type: WGS84 lat/lon coordinates
- Supports Spatial Conversion: Yes
Parameters:
- 2m Temperature: K > Convertable
- 2m Wind speed : Bft > Convertable
- 10m Vision range: FAIL
    - Unit was set to convertable type "Bunny Vision Range", but no conversion rules were found
```

As you can see, any properties or parameters that are technically properly configured, but can't properly validate, will generate error messages trying to specify what is wrongly configured or set.
