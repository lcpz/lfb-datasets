#!/usr/bin/env python3

# intersect multiple .CSV datasets on the first column of the first one
# usage: ./intersect.py [datasets]

import os, csv, sys
from collections import OrderedDict

if len(sys.argv) == 3:
    d = OrderedDict()
    is_first = True
    intersection_rows = 0

    for filepath in sys.argv:
        if '.csv' not in filepath:
            continue
        with open(filepath, mode='r', encoding='utf-8-sig') as f:
            for line in csv.reader(f):
                if is_first:
                    intersection_rows += line.count(',')
                    d[line[0]] = line
                elif line[0] in d.keys():
                    d[line[0]].extend([line[i] for i in range(1, len(line))])
                print(line[0])
            is_first = False

    print('Writing to "intersection.csv"... ')
    with open('intersection.csv', 'w', newline='') as f:
        intersect_writer = csv.writer(f, lineterminator=os.linesep)
        for row in d.values():
            if len(row) == intersection_rows: # exclude non-intersecting rows
                intersect_writer.writerow(row)
