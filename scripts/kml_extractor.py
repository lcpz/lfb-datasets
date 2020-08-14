#!/usr/bin/env python3

# extracts a Google Maps layer file (KML)
# dependency: pykml >= 0.2.0 (available in pip)

import sys
from pykml import parser

kml_file = sys.argv[1] # the input KML file

with open(kml_file) as f:
  folder = parser.parse(f).getroot().Document.Folder

for pm in folder.Placemark:
    print(f'{str(pm.name).strip()},{str(pm.Point.coordinates).strip()}')
