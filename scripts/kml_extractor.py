#!/usr/bin/env python3

import os, csv, sys
from fastkml import kml

if len(sys.argv) == 2:
    with open(sys.argv[1]) as kml_file:
        doc = kml_file.read().encode('utf-8')

    k = kml.KML()
    k.from_string(doc)

    stations_file = open(kml_filename.split('.')[0], 'w', newline='')
    csv_writer = csv.writer(stations_file, lineterminator=os.linesep)

    for feat in k.features():
        for folder in feat.features():
            for pm in folder.features():
                # Name, Latitude (N), Longitude (W)
                csv_writer.writerow([pm.name, pm.geometry.y, pm.geometry.x])

    stations_file.close()
