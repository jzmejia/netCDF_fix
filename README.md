# netCDF_fix
python script for fixing netCDF files with incorrect or absent geo referencing when reading into QGIS


When trying to import a few netCDF of data from Greenland into QGIS that I retrieved from a data repository I was left with a very small country in the middle of the Arctic Ocean. 
The coordinate reference system was correct but the georeferening was not working. 

There were a few issues in the referencing and this is the script I used to fix the files. Not sure if this was a one off thing or if it will be useful to others so I will share. 


## Requirements
xarray
