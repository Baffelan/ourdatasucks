import pandas as pd
import datetime


#curl -L -o Chicago_Crimes.csv "https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD"


# Load the data directly from the URL
df = pd.read_csv('Chicago_Crimes.csv')

print(f"Total records: {len(df)}\n")

# Check missing values in key columns
missing_lat = df['Latitude'].isna().sum()
missing_long = df['Longitude'].isna().sum()
missing_loc_desc = df['Location Description'].isna().sum()
missing_beat = df['Beat'].isna().sum()
missing_ward = df['Ward'].isna().sum()

print(f"Missing Latitude: {missing_lat}")
print(f"Missing Longitude: {missing_long}")
print(f"Missing Location Description: {missing_loc_desc}")
print(f"Missing Beat: {missing_beat}")
print(f"Missing Ward: {missing_ward}\n")

# Check for duplicates
duplicate_count = df.duplicated().sum()
print(f"Duplicate rows: {duplicate_count}\n")

# Check for invalid or future dates
now = datetime.datetime.now()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
future_dates_count = df[df['Date'] > now].shape[0]
invalid_dates_count = df['Date'].isna().sum()

print(f"Rows with future dates: {future_dates_count}")
print(f"Rows with invalid/missing dates: {invalid_dates_count}\n")

# Sample rows with missing latitude or longitude
print("Sample rows with missing Latitude or Longitude:")
print(df[df['Latitude'].isna() | df['Longitude'].isna()].head(5))
