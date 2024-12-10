# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:46:12 2024

@author: Ece
"""

# let's dive into regcm dataset

import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Load your NetCDF file
file_path = 'C:/Users/Downloads/bozkurt_ATM.1990060100.nc'#'path_to_your_regcm5_output.nc'
data = xr.open_dataset(file_path)

# Inspect the dataset
print(data)
print(data.head)

data_frame = data.to_dataframe();

for var in data.data_vars:
    print(f"{var}: {data[var].attrs.get('units', 'No units attribute')}")
    
file_path2 = "C:/Users/OneDrive/Desktop/bozkurt_nonhydro_ATM.1990060100.nc"
data2 = xr.open_dataset(file_path2)

# Inspect the dataset
print(data2)
print(data2.head)

data_frame2 = data2.to_dataframe();

for var in data2.data_vars:
    print(f"{var}: {data2[var].attrs.get('units', 'No units attribute')}")


file_path3 = 'C:/Users/Downloads/bozkurt_hydro_ATM.1990060100.nc'
data3 = xr.open_dataset(file_path3)

# Inspect the dataset
print(data3)
print(data3.head)

data_frame3 = data3.to_dataframe();

for var in data3.data_vars:
    print(f"{var}: {data3[var].attrs.get('units', 'No units attribute')}")
    


file_path4 = 'C:/Users/Downloads/bozkurt_SRF.1990060100.nc'
data4 = xr.open_dataset(file_path4)

# Inspect the dataset
print(data4)
print(data4.head)

data_frame4 = data4.to_dataframe();

for var in data4.data_vars:
    print(f"{var}: {data4[var].attrs.get('units', 'No units attribute')}")

pr_data = data4[['pr']]
df_prData = pr_data.to_dataframe()

pr_multiplied = (data4['pr'] /1000) * 3600

# You can create a new xarray or add the modified variable back to the original dataset
data4['pr_modified'] = pr_multiplied

# Plot the data (e.g., using the first time slice or averaging over time)
pr_multiplied.isel(time=0).plot()

# Add labels and title
plt.title('Precipitation (Modified)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()

precipitation = data4['pr_modified'].mean(dim=['iy', 'jx'])  # Replace with your variable name
plt.plot(precipitation['time'], precipitation, label='Precipitation')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Temperature and Precipitation over Time')
plt.legend()
plt.show()


file_path5 = 'C:/Users/Downloads/bozkurt_STS.1990060100.nc'
data5 = xr.open_dataset(file_path5)

# Inspect the dataset
print(data5)
print(data5.head)

data_frame5 = data5.to_dataframe();

for var in data5.data_vars:
    print(f"{var}: {data5[var].attrs.get('units', 'No units attribute')}")
    
pr_multiplied = (data5['pr'] /1000) * 3600

# You can create a new xarray or add the modified variable back to the original dataset
data5['pr_modified'] = pr_multiplied

precipitation = data5['pr_modified'].mean(dim=['iy', 'jx'])  # Replace with your variable name
plt.plot(precipitation['time'], precipitation, label='Precipitation')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Temperature and Precipitation over Time')
plt.legend()
plt.show()

file_path6 = 'C:/Users/Downloads/bozkurt_SAV.1990060600.nc'
data6 = xr.open_dataset(file_path6)

# Inspect the dataset
print(data6)
print(data6.head)

data_frame6 = data6.to_dataframe();

for var in data6.data_vars:
    print(f"{var}: {data6[var].attrs.get('units', 'No units attribute')}")
    
pr_multiplied = (data5['pr'] /1000) * 3600

# You can create a new xarray or add the modified variable back to the original dataset
data5['pr_modified'] = pr_multiplied

precipitation = data5['pr_modified'].mean(dim=['iy', 'jx'])  # Replace with your variable name
plt.plot(precipitation['time'], precipitation, label='Precipitation')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Temperature and Precipitation over Time')
plt.legend()
plt.show()

file_path7 = 'C:/Users/Downloads/2021/bozkurt_nonhydro_SRF.2021080100.nc'
data7 = xr.open_dataset(file_path7)

# Inspect the dataset
print(data7)
print(data7.head)

data_frame7 = data7.to_dataframe();

for var in data7.data_vars:
    print(f"{var}: {data7[var].attrs.get('units', 'No units attribute')}")
    
pr_multiplied = (data7['pr']) * 3600

# You can create a new xarray or add the modified variable back to the original dataset
data7['pr_modified'] = pr_multiplied

precipitation = data7['pr_modified'].mean(dim=['iy', 'jx'])  # Replace with your variable name
plt.plot(precipitation['time'], precipitation, label='Precipitation')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title(' Precipitation over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
plt.legend()
plt.show()

print(data7['time'])
print(data7['time'].values)

# Check if 'time' is a datetime object
if not isinstance(precipitation['time'].values[0], pd.Timestamp):
    precipitation['time'] = pd.to_datetime(precipitation['time'].values)

plt.figure(figsize=(24, 12))  # Adjust figure size
plt.plot(precipitation['time'], precipitation, label='Precipitation')

# Set major ticks every 6 hours
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

# Rotate the labels for better readability
plt.xticks(rotation=45)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Precipitation (mm)')
plt.title('Precipitation Over Time')
plt.legend()
plt.tight_layout()  # Prevent clipping
plt.show()

precipitation_real = data7['pr'].mean(dim=['iy', 'jx'])  # Replace with your variable name
plt.figure(figsize=(24, 12))  # Adjust figure size
plt.plot(precipitation_real['time'], precipitation_real, label='Precipitation')

# Set major ticks every 6 hours
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

# Rotate the labels for better readability
plt.xticks(rotation=45)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Precipitation (mm)')
plt.title('Precipitation Over Time')
plt.legend()
plt.tight_layout()  # Prevent clipping
plt.show()
