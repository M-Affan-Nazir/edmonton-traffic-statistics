# Data Folder

This `data/` directory contains the datasets used in the project. It is organized into **raw** inputs (as obtained from source systems) and **processed** tables generated during cleaning and feature preparation.

## Directory Structure
```text
data/
├─ processed/
│  └─ edmonton_weather.csv
│  └─ merged_features.csv
│  └─ traffic_collisions.csv
│  └─ traffic_volume.csv
├─ raw/
│  └─ Annual_Collision_Report.csv
│  └─ Average_Annual_Weekday_Traffic_Volumes.csv
│  └─ Weather_Data_Hourly.csv
```

## Contents

### `raw/` (unaltered source files)
- `Annual_Collision_Report.csv`
- `Average_Annual_Weekday_Traffic_Volumes.csv`
- `Weather_Data_Hourly.csv`

### `processed/` (derived datasets)
- `edmonton_weather.csv`
- `merged_features.csv`
- `traffic_collisions.csv`
- `traffic_volume.csv`

## Notes
- All files are in CSV format.
