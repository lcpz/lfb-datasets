# London Fire Brigade (LFB) benchmark datasets

[DC-MATS](https://gitlab.com/lcpz/dcmats) instances generated from the following resources:

- [LFB Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
- [LFB Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)
- [LFB Fleet List](https://data.london.gov.uk/dataset/london-fire-brigade---fleet-list)
- [LFB Letter FOIA4310.1](https://www.london-fire.gov.uk/media/3916/foia43101.pdf)

The data considered in the incident and mobilisation records goes from 1 January
2009 to 31 December 2020, while the fleet list is updated as of October 2019.

# Building your custom LFB benchmark

## How to generate data points

- (Optional) Use `python-xlsx2csv` to convert to `.csv` format.
- Exclude rows where `IncidentGroup="False Alarm"`.
- Select the following columns from the Incident Records:
  `1,2,4,6,12,26-29,30-33,36,38`.
- Select the following columns from the Mobilisation Records:
  `1,3,6,8,10,11,15,16`.
- Station locations have been fetched from [Google Maps](https://www.google.com/maps/d/viewer?mid=1rSai4zdG8uSujX8QxY1i0cwgNAU&msa=0&ll=51.576189821246516%2C-0.5874470076488247&spn=0.064273%2C0.169086&iwloc=lyrftr%3Almq%3A1004%3Afire%20station%2C9131785149235576475%2C51.606291%2C0.10437&z=10)
   and elaborated with [`pyKML`](https://pypi.org/project/pykml).

Final headers:

```shell
IncidentNumber,IncidentGroup,Latitude,Longitude,DateOfCall,TimeOfCall,DateAndTimeArrived,AttendanceTimeSeconds,DateAndTimeLeft,DeployedFromStation_Code
```

## How to generate problem parameters

- Incident Records: task IDs, task locations, task weight (notional cost).
- Mobilisation Records: task time windows (alpha: date and time arrived; gamma:
  attendance time in seconds; beta: random value in [alpha, gamma]).
- Fleet List: agent IDs and speeds.
- Initial agent locations (station locations or random).

The coalition values are the only information not definable from the data. We
can generate them using the distributions described in Section 4 of the
following [paper](https://eprints.soton.ac.uk/337164/1/Paper_524.pdf):

> Rahwan, Talal, Michalak, Tomasz and Jennings, Nicholas R. (2012). A hybrid
> algorithm for coalition structure generation. 26th Conference on Artificial
> Intelligence (AAAI-12), Canada 22-26 Jul 2012, pp. 1443-1449.

# Licenses

[OGLv2](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2)
for the records and [ODBL](https://opendefinition.org/licenses/odc-odbl) for the
fleet list.
