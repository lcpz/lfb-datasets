# London Fire Brigade (LFB) benchmark datasets

[CMARS](https://gitlab.com/lcpz/CMARS) datasets generated with the following resources:

- [LFB Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
- [LFB Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)
- [LFB Fleet List](https://data.london.gov.uk/dataset/london-fire-brigade---fleet-list)
- [LFB Letter FOIA4310.1](https://www.london-fire.gov.uk/media/3916/foia43101.pdf)

The data considered is dated from 1 January 2009 to 31 December 2020. The fleet
list is updated as of October 2019.

The locations of the stations have been retrieved from [Google
Maps](https://www.google.com/maps/d/viewer?mid=1rSai4zdG8uSujX8QxY1i0cwgNAU&msa=0&ll=51.576189821246516%2C-0.5874470076488247&spn=0.064273%2C0.169086&iwloc=lyrftr%3Almq%3A1004%3Afire%20station%2C9131785149235576475%2C51.606291%2C0.10437&z=10)
and elaborated with [`pyKML`](https://pypi.org/project/pykml).

## How to generate node data

1. Use [`python-xlsx2csv`](https://pypi.org/project/xls2csv/) to convert to
   `.csv` format.
2. Exclude rows containing `False Alarm`, `NULL`, `Ham` or `HAM`.
3. Select the following columns from the Incident Records:
   ```shell
   IncidentNumber,DateOfCall,TimeOfCall,IncidentGroup,Easting_m,Northing_m
   ```
   If available, select `Latitude,Longitude` instead of `Easting_m,Northing_m`
4. Select the following columns from the Mobilisation Records:
   ```shell
   TimeMobilised,TimeArrived,AttendanceTimeSeconds,DeployedFromStation_Code
   ```
5. Join the datasets thus obtained with `scripts/join_csv.py`.
6. If necessary, convert to latitude and longitude coordinates with
   `scripts/osgb36_to_wsg84.py`.

## How to generate problems

- Incident records: task IDs, task locations, optionally task weight (notional
  cost).
- Mobilisation records: task time windows (alpha: date and time arrived; gamma:
  attendance time in seconds; beta: value in [alpha, gamma]).
- Fleet List: agent IDs and speeds.
- Initial agent locations (station locations).

The coalition values are the only information not definable from the data. We
can generate them using the distributions described in the following
[paper](https://eprints.soton.ac.uk/337164/1/Paper_524.pdf):

> Rahwan, Talal, Michalak, Tomasz and Jennings, Nicholas R. (2012). A hybrid
> algorithm for coalition structure generation. 26th Conference on Artificial
> Intelligence (AAAI-12), Canada 22-26 Jul 2012, pp. 1443-1449.

# Licenses

[OGLv2](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2)
for the records and [ODBL](https://opendefinition.org/licenses/odc-odbl) for the
fleet list.
