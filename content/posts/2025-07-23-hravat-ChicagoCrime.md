---
title: "Dirty Crime Data: A Case Study of the Chicago Crime Dataset"
tags: blog, missing data, data quality, chicago crime, data cleaning
date: 2025-01-02
---


# Even Crime Data Can’t Stay Clean

We pulled the Chicago Crime dataset straight from the city’s open data portal using a simple `curl` command. It’s public, it’s official, and  like most real-world data it’s messier than it looks.

```bash
curl -L -o Chicago_Crimes.csv "https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD"

```

This dataset contains detailed records of reported crimes in the City of Chicago from 2001 to the present. Each row represents a single incident, with columns including the type of crime (`Primary Type`), a more detailed description (`Description`), whether an arrest was made, the location of the crime, and administrative details like district, ward, beat, and census tract. Time-related fields include both the exact date and time of the incident as well as the report date.

While it's published by an official city department and updated regularly, the dataset is not immune to typical data



## Chicago Crime Dataset: Field Dictionary

| Column Name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `ID`                  | Unique identifier for the crime record                                      |
| `Case Number`         | Official case reference used by the police                                  |
| `Date`                | Date and time when the crime occurred (local time)                          |
| `Block`               | Approximate address of the crime                                            |
| `IUCR`                | Illinois Uniform Crime Reporting code for the type of crime                 |
| `Primary Type`        | High-level category of the crime (e.g., THEFT, BATTERY)                     |
| `Description`         | More detailed description of the crime                                      |
| `Location Description`| Type of location where the crime occurred (e.g., STREET, RESIDENCE)         |
| `Arrest`              | Indicates whether an arrest was made (`true` or `false`)                    |
| `Domestic`            | Indicates if the crime was domestic-related                                 |
| `Beat`                | Police beat where the crime occurred                                        |
| `District`            | Police district number                                                      |
| `Ward`                | City ward where the crime occurred                                          |
| `Community Area`      | Numeric code for the broader community area                                 |
| `FBI Code`            | Crime classification used by the FBI                                        |
| `X Coordinate`        | X coordinate (in UTM zone 16N) for mapping                                  |
| `Y Coordinate`        | Y coordinate (in UTM zone 16N) for mapping                                  |
| `Year`                | Year when the crime occurred                                                 |
| `Updated On`          | Date when the record was last updated                                        |
| `Latitude`            | Latitude of the crime location                                               |
| `Longitude`           | Longitude of the crime location                                              |
| `Location`            | Combined field of latitude and longitude in `(lat, long)` format             |



# Data Quality Issues

### Chicago Crime Data Quality Check Results

**Total records:** 8,355,979

| Issue                          | Count    |
|-------------------------------|----------|
| Missing Latitude              | 93,228   |
| Missing Longitude             | 93,228   |
| Missing Location Description  | 14,542   |
| Missing Beat                  | 0        |
| Missing Ward                  | 614,823  |
| Duplicate rows               | 0        |
| Rows with future dates        | 0        |
| Rows with invalid/missing dates | 0     |

---

### Sample rows with missing Latitude or Longitude:

| ID       | Case Number | Date                | Latitude | Longitude | Location |
|----------|-------------|---------------------|----------|-----------|----------|
| 13311263 | JG503434    | 2022-07-29 03:39:00 |          |           |          |
| 13053066 | JG103252    | 2023-01-03 16:44:00 |          |           |          |
| 11227634 | JB147599    | 2017-08-26 10:00:00 |          |           |          |
| 12416972 | JE293535    | 2020-10-01 00:01:00 |          |           |          |
| 12536164 | JE439378    | 2015-09-24 00:00:00 |          |           |          |



## Impact of Missing Values and Suggestions for Cleaning

The Chicago Crime dataset shows significant missing data in key fields such as latitude, longitude, location description, and ward. These gaps can seriously affect analysis quality and the insights drawn:

- **Missing Latitude and Longitude**: Without geographic coordinates, mapping crime hotspots or analyzing spatial patterns becomes impossible for those records. This reduces the accuracy of location-based insights and visualizations.

- **Missing Location Description**: When the nature of the crime location is unknown, it’s harder to categorize or group incidents meaningfully, which can skew trend analysis.

- **Missing Ward Information**: Ward-level analysis relies on accurate administrative boundaries. Missing wards limit the ability to perform political or jurisdictional crime studies.

- **No Missing Beat Values and No Duplicate Records**: This is a positive sign, suggesting some consistency in police beat data and record uniqueness.

---

### Suggestions to Handle Missing Data

- **Imputation**: For missing geographic data, infer location from related fields like `Block` or neighboring records using spatial interpolation or address geocoding services.

- **Flag and Filter**: Mark records with missing critical fields and consider excluding them from analyses where their absence would bias results.

- **Cross-Reference External Data**: Use other city datasets (e.g., address registries or census data) to enrich and fill gaps.

- **Regular Data Auditing**: Encourage data providers to validate entries at ingestion to reduce missing fields.

By applying these strategies, we can improve the reliability of findings and better communicate the limits of the data.
