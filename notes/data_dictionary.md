# City of Edmonton Annual-Collision-Report fields

| Column Name                                      | Description                                               |
|--------------------------------------------------|-----------------------------------------------------------|
| Year                                             | Calendar year covered by the statistics                   |
| Population                                       | City of Edmonton mid-year population estimate             |
| Private Passenger Vehicles                       | Registered cars/trucks/vans that year                     |
| Private Motorcycles                              | Registered motorcycles that year                          |
| BICYCLE COLLISIONS                               | Crashes involving ≥1 bicyclist                            |
| MOTORCYCLE COLLISIONS                            | Crashes involving ≥1 motorcyclist                         |
| PEDESTRIAN COLLISIONS                            | Crashes involving ≥1 pedestrian                           |
| Total Collisions                                 | All police-reported traffic collisions                    |
| Collisions per 1,000 Population                  | Total collisions / population × 1 000                      |
| Property Damage Only (PDO) Collisions            | Crashes with no injuries—damage only                      |
| Injuries+Fatalities per 1,000 Population         | (Injuries + deaths) / population × 1 000                   |
| Injuries per 1,000 Population                    | Injury count per 1 000 residents                          |
| Fatalities per 1,000 Population                  | Fatality count per 1 000 residents                        |
| FATALITY: BICYCLIST                              | Bicyclists killed in the year                             |
| FATALITY: MOTORCYCLIST                           | Motorcyclists killed                                      |
| FATALITY: PEDESTRIAN                             | Pedestrians killed                                        |
| FATALITY: VEHICLE DRIVER                         | Drivers killed                                            |
| FATALITY: VEHICLE PASSENGER                      | Passengers killed                                         |
| Total Fatalities                                 | Sum of all road-user deaths                               |
| SERIOUS INJURIES: BICYCLIST                      | Cyclists admitted to hospital                             |
| MINOR INJURIES: BICYCLIST                        | Cyclists treated/released                                 |
| SERIOUS INJURY: MOTORCYCLIST                     | Motorcyclists admitted                                    |
| MINOR INJURIES: MOTORCYCLIST                     | Motorcyclists treated/released                            |
| SERIOUS INJURIES: PEDESTRIAN                     | Pedestrians admitted                                      |
| MINOR INJURIES: PEDESTRIAN                       | Pedestrians treated/released                              |
| Total Serious Injuries                           | Sum of all KABCO “serious” injuries                       |
| Total Minor Injuries                             | Sum of all “minor” injuries                               |
| Total Serious + Minor Injuries                   | Combined injury count                                     |
| Total Fatalities + Injuries                      | Deaths + injuries                                         |
| FATALITIES: INTERSECTION                         | Deaths from intersection crashes                          |
| FATALITIES: INTERSECTION PERCENT                 | % of deaths at intersections                              |
| FATALITIES: MIDBLOCK                             | Deaths on open road (non-intersection)                    |
| FATALITIES: MIDBLOCK PERCENT                     | % of deaths midblock                                      |
| INJURIES: INTERSECTION                           | Injuries at intersections                                 |
| INJURIES: INTERSECTION PERCENT                   | Share of total injuries at intersections                  |
| INJURIES: MIDBLOCK                               | Injuries midblock                                         |
| INJURIES: MIDBLOCK PERCENT                       | Share of total injuries midblock                          |
| FATAL COLLISIONS                                 | Crashes that caused ≥1 death                              |
| SERIOUS INJURY COLLISIONS                        | Crashes with ≥1 serious injury                            |
| MINOR INJURY COLLISIONS                          | Crashes with only minor injuries                          |
| TOTAL SERIOUS & MINOR INJURY COLLISIONS          | Injury-producing crashes                                  |
| TOTAL FATAL & INJURY COLLISIONS                  | All fatal + injury crashes                                |




# City of Edmonton Average Annual Weekday Traffic Volume fields

| Column Name            | Description                                                      |
|------------------------|------------------------------------------------------------------|
| Site Number            | Unique numeric ID for the traffic‐count location                 |
| Site Name              | Text label describing the road or intersection where the count is taken |
| Year                   | Calendar year the volume was measured                            |
| Average Daily Volume   | Average weekday vehicles per 24 h at the site for that year      |
| Latitude               | WGS-84 latitude of the count point                               |
| Longitude              | WGS-84 longitude of the count point                              |
| Location               | Socrata “Location” object combining address text with the same lat/long |
| Geometry Point         | GIS point geometry used for mapping                              |



# City of Edmonton Weather Data Hourly fields

| Column Name                   | Description                                                                                       |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| Row ID                        | Sequential identifier for each record in the CSV table                                            |
| Station ID                    | Internal numeric ID for the monitoring site                                                       |
| Station Name                  | Official Environment Canada name of the station                                                   |
| Station Province              | Two-letter province/territory code                                                                |
| Station Latitude              | Geographic latitude in decimal degrees                                                            |
| Station Longitude             | Geographic longitude in decimal degrees                                                           |
| Location                      | Combined lat/long object used by the portal                                                       |
| Station Elevation (m)         | Height of sensor above sea level in metres                                                        |
| Station Climate Identifier    | 7-digit permanent climate ID assigned by MSC                                                      |
| Station WMO Identifier        | 5-digit World Meteorological Organization station code                                            |
| Station TC Identifier         | 4-letter Transport Canada/ICAO code                                                               |
| Station Note                  | Free-text remarks about status or automation                                                      |
| Date and Time                 | Local timestamp of the observation (YYYY-MM-DD HH:MM)                                             |
| Temperature (°C)              | Air temperature measured in degrees Celsius                                                       |
| Dewpoint Temperature (°C)     | Temperature at which air becomes saturated                                                        |
| Relative Humidity             | Moisture in the air as a percentage                                                               |
| Wind Direction (10s degrees)  | Average wind direction expressed in tens of degrees (e.g., 36 = 360° North)                        |
| Wind Speed (km/h)             | Average wind speed for the period in kilometres per hour                                          |
| Visibility (km)               | Horizontal visibility distance in kilometres                                                      |
| Air Pressure (kPa)            | Station or sea-level barometric pressure in kilopascals                                          |
| Humidex                       | Index combining temperature and humidity to express perceived heat                                |
| Wind Chill (°C)               | Index combining temperature and wind to express perceived cold                                    |