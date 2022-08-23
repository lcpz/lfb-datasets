#!/usr/bin/env python3

# converts a dataset from Easting-Northing to Latitude-Longitude format
# dependency: pyproj >= 3.0.0 (available from pip)

import csv, sys
from pyproj import Transformer

t = Transformer.from_crs('epsg:27700', 'epsg:4326')

if len(sys.argv) != 0 and '.csv' in sys.argv[1]:
    headers = False
    with open(sys.argv[1]) as f:
        for line in csv.reader(f):
            if not headers:
                line[-2] = 'Latitude'
                line[-1] = 'Longitude'
                headers = True
            else:
                gps = t.transform(line[-2], line[-1])
                line[-2] = gps[0]
                line[-1] = gps[1]
            print(*line, sep=',')
