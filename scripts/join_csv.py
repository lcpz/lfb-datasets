#!/usr/bin/env python3

# joins two .CSV datasets on the given column
# be sure that the data sets are well-formed
# usage: ./join.py [datasets] column_str

import csv, sys

args = sys.argv[1:]

if len(args) != 0:
    csv_files = []

    for filepath in args:
        if '.csv' not in filepath:
            continue
        l = []
        headers = []
        with open(filepath, 'r') as f:
            for line in csv.reader(f):
                if not headers:
                    headers = line
                else:
                    d = {}
                    for i in range(0, len(headers)):
                        d[headers[i]] = line[i]
                    l.append(d)
        csv_files.append(l)

    if len(csv_files) > 1 and sys.argv[-1]:
        not_found = 0
        f = open('joined.csv', 'w')
        join_key = sys.argv[-1]
        join_writer = csv.writer(f)
        headers_written = False
        for d in csv_files[0]:
            for i in range(1, len(csv_files)):
                d2 = next((item for item in csv_files[i] if item[join_key] == d[join_key]), None)
                if d2 is not None:
                    d3 = {**d, **d2}
                    if not headers_written:
                        join_writer.writerow(list(d3.keys()))
                        headers_written = True
                    join_writer.writerow(list(d3.values()))
                    #print(d3)
                else:
                    print('join not found for:\n{}'.format(d))
                    not_found += 1
        print('\nnumber of joins not found: {}'.format(not_found))
