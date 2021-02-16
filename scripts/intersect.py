#!/usr/bin/env python3

# intersect multiple .CSV datasets on the first column of the first one
# usage: ./join.py [list of data sets]

import csv, sys
from collections import OrderedDict

if len(sys.argv) == 3:
    d = OrderedDict()
    is_first = True

    for filepath in sys.argv:
        if '.csv' not in filepath:
            continue
        with open(filepath) as f:
            for line in csv.reader(f):
                if is_first:
                    d[line[0]] = [line[i] for i in range(0, len(line))]
                elif line[0] in d.keys() and len(d[line[0]]) < 10:
                    d[line[0]].append(','.join([line[i] for i in range(1, len(line))]))
                print(line[0])
            is_first = False

    print('Writing to "intersection.csv"... ')
    with open('intersection.csv', 'w') as f:
        intersect_writer = csv.writer(f)
        for row in d.values():
            intersect_writer.writerow(row.replace('"', ''))
