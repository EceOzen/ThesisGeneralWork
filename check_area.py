# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:15:16 2024

@author: Ece
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig, ax = plt.subplots(subplot_kw={"projection": ccrs.PlateCarree()})
ax.set_extent([33.8072, 0, 41.9381, 0], crs=ccrs.PlateCarree())
ax.coastlines()
plt.title("Requested Area")
plt.show()
