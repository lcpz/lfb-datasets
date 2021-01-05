#!/usr/bin/env python3

# select data between recorded between hours X and Y

import csv, sys

if len(sys.argv) >= 3 and '.csv' in sys.argv[1]:
    headers = False
    with open(sys.argv[1]) as f:
        for line in csv.reader(f):
            if not headers:
                headers = True
                print(*line, sep=',')
            else:
                hour = int(line[2].split(':')[0])
                if hour >= int(sys.argv[2]) and hour <= int(sys.argv[3]):
                    print(*line, sep=',')
