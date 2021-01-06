#!/usr/bin/env python3

# sort a dataset chronologically

import csv, sys
from functools import cmp_to_key

def compare(a, b):
    x = a.split(',')[0]
    y = b.split(',')[0]

    if x == 'IncidentNumber':
        return -1
    if y == 'IncidentNumber':
        return 1

    # pattern: number-date
    x_arr = x.split('-')
    y_arr = y.split('-')

    if len(x_arr) == 2 and len(y_arr) == 2:
        if int(x_arr[1][4:]) != int(y_arr[1][4:]): # year
            return int(x_arr[1][4:]) - int(y_arr[1][4:])
        if int(x_arr[1][2:4]) != int(y_arr[1][2:4]): # month
            return int(x_arr[1][2:4]) - int(y_arr[1][2:4])
        if int(x_arr[1][0:2]) != int(y_arr[1][0:2]): # day
            return int(x_arr[1][0:2]) - int(y_arr[1][0:2])

    return int(x_arr[0]) - int(y_arr[0])


if len(sys.argv) == 2 and '.csv' in sys.argv[1]:
    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        d = sorted({','.join(row) for row in reader}, key=cmp_to_key(compare))
        print(*d, sep='\n')
