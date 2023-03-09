import xarray as xr


def nc_update(file):
    """update netCDF file to be compatible with QGIS

    transposes data variable dimensions then adds 
    coordinates to Dataset object

    Args
    ----
        file : str
            path to netCDF file to be read in and updated

    Returns
    -------
        ds : xarray.Dataset
            updated Dataset object 
    """
    ds = xr.open_dataset(file)

    # reorder x and y coordinates to y,x
    ds = ds.transpose("r", "c")

    # create coordinates in xarray object
    ds.coords['r'] = ds['y'].values
    ds.coords['c'] = ds['x'].values
    return ds


path = "/"
file_name = "file.nc"
new_name = "newfile.nc"

ds = nc_update(path+file_name)

encoding = {'x': {'zlib': False, '_FillValue': None},
            'y': {'zlib': False, '_FillValue': None}
            }

ds.to_netcdf(path+new_name,
             encoding=encoding)
