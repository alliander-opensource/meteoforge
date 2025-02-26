# WPAS Utility Tools

This directory contains utility tools for the WPAS project. The tools are intended to be used to convert files between
different versions of the weather provider.

## NetCDF to ZARR Storage

Where possible data should be re-acquired from the weather provider in the latest format. However, this is not always
possible and so the NetCDF to ZARR Storage tool has been created to convert NetCDF files to ZARR storage format. This
tool can only reformat the data from NetCDF to ZARR and cannot process the data further in any way.

This means that if you wish to convert data from (for example) KNMI's Harmonie AROME model to ZARR storage format, you
will still need to process the data afterward to meet the new format naming and metadata requirements. For this purpose
older weather models within the Weather Provider Sources part of this project carry a conversion script that can be used
to convert the data to the new format.
