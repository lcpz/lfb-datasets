#!/usr/bin/env python3

# Converts a dataset from Easting-Northing to Latitude-Longitude format
# dependency: pyproj >= 3.0.0 (available from pip)

import csv, sys
from pyproj import Transformer

t = Transformer.from_crs('epsg:27700', 'epsg:4326')

if len(sys.argv) != 0 and '.csv' in sys.argv[1]:
    headers = False
    with open(sys.argv[1], 'r') as f:
        for line in csv.reader(f):
            if not headers:
                line[4] = 'Latitude'
                line[5] = 'Longitude'
                headers = True
            else:
                gps = t.transform(line[4], line[5])
                line[4] = gps[0]
                line[5] = gps[1]
            print(*line, sep=',')
