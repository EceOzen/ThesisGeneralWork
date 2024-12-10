# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:16:45 2024

@author: Ece
"""

import folium

# Coordinates of Bozkurt, Kastamonu
latitude = 41.9547
longitude = 34.0108

# Create a map centered on Bozkurt
bozkurt_map = folium.Map(location=[latitude, longitude], zoom_start=13)

# Add a marker
folium.Marker(
    [latitude, longitude],
    popup="Bozkurt, Kastamonu",
).add_to(bozkurt_map)

# Display the map
bozkurt_map.save("C:/Users/ece_z/Downloads/bozkurt_map.html")
