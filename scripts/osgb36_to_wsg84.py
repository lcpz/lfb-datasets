#!/usr/bin/env python3

# Converts Easting-Northing to Latitude-Longitude
# dependency: pyproj >= 3.0.0

from pyproj import Transformer

# example
easting_m = 528652
northing_m = 176830

t = Transfomer.from_crs('epsg:27700', 'epsg:4326')
t.transform(easting_m, northing_m)
