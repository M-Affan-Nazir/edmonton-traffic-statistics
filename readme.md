# Edmonton Urban Structure

This repository contains datasets and reproducible notebooks for exploring relationships between Edmonton traffic collisions, traffic volume, and weather. It also includes lightweight Python utilities for basic data cleaning. All sections below describe  files that are present in this repository.

> The datasets were sourced from the Edmonton Open Data Portal and subsequently processed and merged to create the final dataset used for the statistical analysis.

## Repository Structure

```text
Edmonton Urban Structure/
├─ data/
│  ├─ raw/
│  │  └─ Annual_Collision_Report.csv
│  │  └─ Average_Annual_Weekday_Traffic_Volumes.csv
│  │  └─ Weather_Data_Hourly.csv
│  └─ processed/
│     └─ edmonton_weather.csv
│     └─ merged_features.csv
│     └─ traffic_collisions.csv
│     └─ traffic_volume.csv
├─ notebooks/
│  └─ 00_data_overview.ipynb
│  └─ 01_data_cleaning.ipynb
│  └─ 02_feature_engineering.ipynb
│  └─ 03_statistical_inference.ipynb
│  └─ 04_model_prototyping.ipynb
├─ notes/
│  └─ data_dictionary.md
├─ reports/
│  └─ report.pdf
└─ src/
   ├─ __init__.py
   └─ data/
      ├─ __init__.py
      └─ clean_data.py
```
 
## Contents

### `data/`
Raw inputs and cleaned/derived datasets used by the notebooks.

#### `data/raw/` (source CSVs)
- `Annual_Collision_Report.csv`
- `Average_Annual_Weekday_Traffic_Volumes.csv`
- `Weather_Data_Hourly.csv`

#### `data/processed/` (prepared tables)
- `edmonton_weather.csv`
- `merged_features.csv`
- `traffic_collisions.csv`
- `traffic_volume.csv`

### `notebooks/`
Jupyter notebooks for exploration, cleaning, feature engineering, inference, and prototyping.
- `00_data_overview.ipynb` – data overview
- `01_data_cleaning.ipynb` – data cleaning
- `02_feature_engineering.ipynb` – feature engineering
- `03_statistical_inference.ipynb` – statistical inference
- `04_model_prototyping.ipynb` – model prototyping

### `notes/`
Supporting documentation.
- `data_dictionary.md` – field descriptions for collision, traffic volume, and weather datasets.

### `reports/`
- Contains a report summarizing findings from the statistical analysis.

### `src/`
Python package for simple data utilities.
- `__init__.py` – package version.
- `data/` – helpers for data cleaning:
  - `clean_data.py` – functions: `drop_columns`, `drop_all_null_rows`, `drop_null_rows`, `filter_dataframe`.