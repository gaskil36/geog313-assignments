# Avoids conflicts with Client for dask
from pystac_client import Client as clt
import planetary_computer
import leafmap
import stackstac
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd

def main(bbox, start_date, end_date):
    """
        This function searches the STAC API with given dates, gathers specified assets (such as bands),
        clips to the bounding box, calculates mean Normalize Difference Water Index for each scene,
        and plots the results.
        
        Parameters
        ----------
        bbox : tuple
            A tuple containing the x y coordinates of the bounding box used to clip to the study area
        start_date: string
            A string containing the start date
        end_date: string
            A string containing the end date
        
        Returns 
        -------
        stack : xarray.DataArray
            An xarray object with the requested assets stacked and clipped to the bbox
        """
    def search_stac():
        """
        This function searches for sentinel-2-l2a scenes from the Microsoft Planetery Computer
        
        Parameters
        ----------
        
        Returns 
        -------
        items : pystac.ItemCollection
            The collection of items matching the search parameters (collections, start date, end date)
        """
        catalog = clt.open(
            "https://planetarycomputer.microsoft.com/api/stac/v1",
            modifier=planetary_computer.sign_inplace,
        )
        
        search = catalog.search(
            collections=['sentinel-2-l2a'],
            datetime=f"{start_date}/{end_date}",
            bbox=bbox,
        )
        
        items = search.get_all_items()
        return items

    def return_assets(items, asset_list, bbox):
        """
        This function returns stackstac assets in a clipped bounding box xarray object
        
        Parameters
        ----------
        items : pystac.ItemCollection
            The collection of items matching the search parameters (collections, start date, end date)
        asset_list : list
            The list of assets requested by the user (such as sentinel-2-l2a bands)
        bbox : tuple
            A tuple containing the x y coordinates of the bounding box used to clip to the study area
        
        Returns 
        -------
        stack : xarray.DataArray
            An xarray object with the requested assets stacked and clipped to the bbox
        """
        # Create xarray object
        stack = stackstac.stack(items, assets=asset_list, bounds_latlon=bbox)
        return stack

    def mean_ndwi(xarray_bands):
        """
        This function calculates the mean Normalized Difference Water Index for the given xarray object
        
        Parameters
        ----------
        xarray_bands : xarray.DataArray
             An xarray object with the requested assets stacked and clipped to the bbox
             
        Returns 
        -------
        mean_ndwi : xarray.DataArray
            An xarray object with the mean Normalized Difference Water Index calculated for each scene
        """
        green = xarray_bands.sel(band="B03")
        nir = xarray_bands.sel(band="B08")
    
        ndwi = (green - nir) / (green + nir)
    
        # Calculate mean NDWI per scene, maintaining the time dimension
        mean_ndwi = ndwi.mean(dim=["x", "y"])
        return mean_ndwi

    def mean_ndwi_plot(mean_ndwi, start_date, end_date):
        """
        This function plots the mean Normalized Difference Water Index, given the start and end dates
        
        Parameters
        ----------
        mean_ndwi : xarray.DataArray
            An xarray object with the mean Normalized Difference Water Index calculated for each scene
        start_date: string
            A string containing the start date
        end_date: string
            A string containing the end date
             
        Returns 
        -------
        """
        # Select time range directly with xarray's slicing
        ndwi_date_range = mean_ndwi.sel(time=slice(start_date, end_date))
        
        ndwi_values = ndwi_date_range.values
        ndwi_dates = ndwi_date_range['time'].values
        
        plt.figure(figsize=(15, 10))
        plt.plot(ndwi_dates, ndwi_values)
        plt.xlabel("Time")
        plt.ylabel("Mean NDWI")
        plt.title("Mean NDWI Over Time")
        plt.show()

    # Running the functions in sequence
    items = search_stac()
    xarray_object = return_assets(items, ["B03", "B08"], bbox)
    ndwi_mean = mean_ndwi(xarray_object)
    mean_ndwi_plot(ndwi_mean, start_date, end_date)