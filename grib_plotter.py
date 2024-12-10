# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:59:24 2024

@author: Ece
"""

import xarray as xr

# Open the GRIB file
file_path = "C:/Users/Downloads/2a7583d164316a45632fbc611263b999.grib"  # Replace with your file path
data = xr.open_dataset(file_path, engine="cfgrib")

# Inspect the dataset
print(data.attrs)

data_frame = data.to_dataframe()
