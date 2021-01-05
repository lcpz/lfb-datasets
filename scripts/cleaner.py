#!/usr/bin/env python3

# remove entries not containing the given station code or having empty columns

import csv, sys

if len(sys.argv) == 3 and '.csv' in sys.argv[1]:
    missing_stations = []
    with open(sys.argv[2]) as f:
        missing_stations = f.readlines()
    missing_stations = [x.strip() for x in missing_stations]

    with open(sys.argv[1]) as f:
        for line in csv.reader(f):
            if len(line) == 10 and (line[0] == 'IncidentNumber' or (line[9] not
                in missing_stations and '' not in line)):
                print(*line, sep=',')
