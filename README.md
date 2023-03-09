# netCDF_fix
python script for fixing netCDF files with incorrect or absent geo referencing when reading into QGIS


When trying to import a few netCDF of data from Greenland into QGIS that I retrieved from a data repository I was left with a very small country in the middle of the Arctic Ocean. 
The coordinate reference system was correct but the georeferening was not working. 

There were a few issues in the referencing and this is the script I used to fix the files. Not sure if this was a one off thing or if it will be useful to others so I will share. The main problem is that while the variables "x" and "y" (i.e., "lat" and "lon") contained the coordinates associated with the datasets defined in other variables, QGIS was reading the dimensions (basically indexing the variables) as the coordinates (e.g., 1, 2, 3, 4, 5, ...) rather than using those indicies to grab the actual lat/lon information from the "x" and "y" variables. I fixed this issue buy using Python's Xarray package, reading in the netCDF file as a DataSet and then manually assigning the lat/lon variables as coordinates for the xarray object. I had the additional issue that my x and y (lat/lon) were flipped in the data so I used `.transpose()` to fix that as well. This could also be fixed in QGIS but it only took one short line to add it to the function. 


## Requirements
xarray


## Use
Example useage below for a netCDF file with variables named "y" and "x" with associated dimensions "r" and "c" respectively. The function will read in the netCDF file as an Xarray `Dataset` object, transpose dimensions and assign coordinates to the `Dataset` object corresponding to your lat/long data set with variable names "y" and "x". Go into function and update variable and dimension names to reflect your netCDF file as needed. 

```python
import xarray as xr 
from update_netcdf import nc_update

ds = nc_update("path_to_your_file.nc")

# export updated netcdf file
# set encoding for x and y such that your coordinates values and 
# are not compressed (requred via netCDF standards). 
# NOTE new version of Xarray requires None instead of False
encoding = {
            'x': {'zlib': False, '_FillValue': None},
            'y': {'zlib': False, '_FillValue': None}
            }
ds.to_netcdf("path_to/newfilename.nc", encoding=encoding)
```
