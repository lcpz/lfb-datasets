# London Fire Brigade Task Allocation Datasets

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7017496.svg)](https://doi.org/10.5281/zenodo.7017496)

This repository contains real-world datasets that can be used to generate task allocation
problems simulating the mobilisation of fire-fighting UAV swarms in the London
metropolitan area.

We used the following resources:

- [LFB Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
- [LFB Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)
- [LFB Fleet List](https://data.london.gov.uk/dataset/london-fire-brigade---fleet-list)

The data considered is dated from 1 January 2009 to 30 June 2022. The fleet list is
updated to January 2022.

Station locations have been retrieved in June 2021 from [Google
Maps](https://www.google.com/maps/d/viewer?mid=1rSai4zdG8uSujX8QxY1i0cwgNAU&msa=0&ll=51.576189821246516%2C-0.5874470076488247&spn=0.064273%2C0.169086&iwloc=lyrftr%3Almq%3A1004%3Afire%20station%2C9131785149235576475%2C51.606291%2C0.10437&z=10)
and elaborated with [`fastkml`](https://pypi.org/project/fastkml).

## How to generate data from LFB records

- If necessary, use [`xlsx2csv`](https://pypi.org/project/xls2csv) to convert to
  `.csv` format.
- Select the following columns from the Incident Records:
  ```shell
  IncidentNumber,DateOfCall,TimeOfCall,IncidentGroup,Easting_rounded,Northing_rounded
  ```
- Select the following columns from the Mobilisation Records:
  ```shell
  IncidentNumber,(DateAnd)TimeMobilised,(DateAnd)TimeArrived,AttendanceTimeSeconds,DeployedFromStation_Code
  ```
- Exclude rows containing `NULL`, `Null`, or `null`.
- Intersect the datasets thus obtained on with `scripts/intersect.py`.
  Intersection order: Mobilisation, Incident.
- Convert to latitude-longitude coordinates with
  `scripts/osgb36_to_wsg84.py`. Dependency: [`pyproj`](https://pypi.org/project/pyproj)
  Be sure that `Easting_rounded` and `Northing_rounded` are the last two columns in the
  intersection.
- If necessary, sort entries chronologically with `scripts/sort.py`.

## How to generate problems

- Incident records: task IDs, task locations, optionally task weight (notional cost).
- Mobilisation records: task time windows (alpha: date and time arrived; gamma: attendance
  time in seconds; beta: value in [alpha, gamma]).
- Fleet List: agent IDs and speeds.
- Initial agent locations (station locations).

Coalition values (e.g., the utility of multiple pumping appliances working on the same
fire) cannot be defined from the records.

However, we can generate them with distributions typically used in Coalition Structure
Generations. For example, we can use the distributions defined in Section 4 of [this
paper](https://ojs.aaai.org/index.php/AAAI/article/view/8265).

## Citation

If you use these datasets in your work, please use the following citation.

```
Luca Capezzuto (2021). "Large-scale, Dynamic and Distributed Multi-agent Coordination for
Real-time Systems". PhD Thesis. School of Electronics and Computer Science, University of
Southampton.
```

## Licenses

[OGLv2](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2)
for the records and [ODBL](https://opendefinition.org/licenses/odc-odbl) for the
fleet list.
