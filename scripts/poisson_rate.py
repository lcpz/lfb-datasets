#!/usr/bin/env python3

import csv, sys

d = {}

if len(sys.argv) == 2 and '.csv' in sys.argv[1]:
    with open(sys.argv[1]) as f:
        for line in csv.reader(f):
            if line[0] != 'IncidentNumber':
                if line[1] not in d:
                    d[line[1]] = {}
                hour = int(line[2].split(':')[0])
                if hour not in d[line[1]]:
                    d[line[1]][hour] = 1
                else:
                    d[line[1]][hour] += 1

    total_avg = 0
    for day in d:
        avg = 0
        for hour in d[day]:
            #print('{}, {}: {}'.format(day, hour, d[day][hour]))
            avg += d[day][hour]
        avg /= 24
        print('{}: {}'.format(day, avg))
        total_avg += avg

    total_avg /= len(d)
    print('Average incidents per hour and day: {}'.format(total_avg))
