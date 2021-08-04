#!/usr/bin/env python3

# intersect multiple .CSV datasets on the first column of the first one
# usage: ./intersect.py [datasets]

import csv, sys
from collections import OrderedDict

if len(sys.argv) == 3:
    d = OrderedDict()
    is_first = True
    mobilisation_first = False

    for filepath in sys.argv:
        if '.csv' not in filepath:
            continue
        with open(filepath, mode='r', encoding='utf-8-sig') as f:
            for line in csv.reader(f):
                if is_first:
                    d[line[0]] = line
                elif line[0] in d.keys():
                    d[line[0]].extend([line[i] for i in range(1, len(line))])
                print(line[0])
            if is_first and "obilisation" in filepath:
                mobilisation_first = True
            is_first = False

    print('Writing to "intersection.csv"... ')
    with open('intersection.csv', 'w') as f:
        intersect_writer = csv.writer(f)
        for row in d.values():
            if len(row) == 10: # exclude non-intersecting rows
                if mobilisation_first: # ugly, but fast
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9] = \
                    row[5], row[6], row[7], row[8], row[9], row[1], row[2], row[3], row[4]
                intersect_writer.writerow(row)
