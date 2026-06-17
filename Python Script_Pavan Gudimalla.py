# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 18:31:28 2025

@author: pavan
"""
import pandas as pd
from sqlalchemy import create_engine

# 1. Load traffic data for each month from CSV files
traffic_sep = pd.read_csv("Moving_Violations_Issued_in_September_2024.csv")
traffic_oct = pd.read_csv("Moving_Violations_Issued_in_October_2024.csv")
traffic_nov = pd.read_csv("Moving_Violations_Issued_in_November_2024.csv")
traffic_dec = pd.read_csv("Moving_Violations_Issued_in_December_2024.csv")
traffic_jan = pd.read_csv("Moving_Violations_Issued_in_January_2025.csv")
traffic_feb = pd.read_csv("Moving_Violations_Issued_in_February_2025.csv")

# 2. Convert ISSUE_DATE from text to proper datetime for each month
date_fmt = '%Y/%m/%d %H:%M:%S%z'
traffic_sep['ISSUE_DATE'] = pd.to_datetime(traffic_sep['ISSUE_DATE'], format=date_fmt)
traffic_oct['ISSUE_DATE'] = pd.to_datetime(traffic_oct['ISSUE_DATE'], format=date_fmt)
traffic_nov['ISSUE_DATE'] = pd.to_datetime(traffic_nov['ISSUE_DATE'], format=date_fmt)
traffic_dec['ISSUE_DATE'] = pd.to_datetime(traffic_dec['ISSUE_DATE'], format=date_fmt)
traffic_jan['ISSUE_DATE'] = pd.to_datetime(traffic_jan['ISSUE_DATE'], format=date_fmt)
traffic_feb['ISSUE_DATE'] = pd.to_datetime(traffic_feb['ISSUE_DATE'], format=date_fmt)
# (Any new monthly traffic file would be loaded above and converted here)

# 3. Load daily weather data from CSV
weather = pd.read_csv("Sep2024 to Oct1st 2025_ Weather data.csv")

# 4. Basic weather cleaning: handle missing values
weather['temp'] = weather['temp'].fillna(weather['temp'].mean())
weather['precip'] = weather['precip'].fillna(0)
weather['preciptype'] = weather['preciptype'].fillna('None')
weather['conditions'] = weather['conditions'].fillna('Unknown')

# 5. Exploration of raw data (before loading to SQL)
print("Traffic September sample rows")
print(traffic_sep.head())          # first few rows of traffic

print("Traffic September column info")
print(traffic_sep.info())          # column types and missing values

print("Weather sample rows")
print(weather.head())              # first few rows of weather

print("Weather summary statistics")
print(weather.describe())          # basic stats for numeric weather field

print("Most common weather conditions")
print(weather['conditions'].value_counts().head())  # top conditions

# 6. Keep only the weather columns needed in SQL
weather_clean = weather[['datetime', 'temp', 'precip', 'preciptype', 'conditions']]
print("Rows to load into SQL (weather):", len(weather_clean))
print("Weather Data Sent to SQL")

# 7. Create connection to MySQL schema final_project2
engine = create_engine(
    'mysql+pymysql://root:Pavanpk%40900@127.0.0.1:3306/final_project2',
    echo=False
)

# 8. Load weather data into SQL (append to existing table)
weather_clean.to_sql(name='weather', con=engine, if_exists='append', index=False)

# 9. Function to clean a single month of traffic data in a consistent way
def clean_month(df):
    # Fill missing fine amounts with the mean fine for that file
    df['FINE_AMOUNT'] = df['FINE_AMOUNT'].fillna(df['FINE_AMOUNT'].mean())
    # Replace missing times with a default value
    df['ISSUE_TIME'] = df['ISSUE_TIME'].fillna('0000')
    # Standardize missing text fields
    df['ISSUING_AGENCY_NAME'] = df['ISSUING_AGENCY_NAME'].fillna('Unknown')
    df['VIOLATION_PROCESS_DESC'] = df['VIOLATION_PROCESS_DESC'].fillna('Unknown')
    # Treat missing accident flags as 'N' (no accident)
    df['ACCIDENT_INDICATOR'] = df['ACCIDENT_INDICATOR'].fillna('N')
    # Return only the columns that will be stored in SQL
    return df[['OBJECTID',
               'ISSUE_DATE',
               'ISSUE_TIME',
               'ISSUING_AGENCY_NAME',
               'VIOLATION_PROCESS_DESC',
               'FINE_AMOUNT',
               'ACCIDENT_INDICATOR']]

# 10. Clean and load each month of traffic into SQL (append to existing table)

# September: append September rows
traffic_sep_clean = clean_month(traffic_sep)
print("Rows September:", len(traffic_sep_clean))
traffic_sep_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# October: append October rows
traffic_oct_clean = clean_month(traffic_oct)
print("Rows October:", len(traffic_oct_clean))
traffic_oct_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# November: append November rows
traffic_nov_clean = clean_month(traffic_nov)
print("Rows November:", len(traffic_nov_clean))
traffic_nov_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# December: append December rows
traffic_dec_clean = clean_month(traffic_dec)
print("Rows December:", len(traffic_dec_clean))
traffic_dec_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# January: append January rows
traffic_jan_clean = clean_month(traffic_jan)
print("Rows January:", len(traffic_jan_clean))
traffic_jan_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# February: append February rows
traffic_feb_clean = clean_month(traffic_feb)
print("Rows February:", len(traffic_feb_clean))
traffic_feb_clean.to_sql(name='traffic', con=engine,
                         if_exists='append', index=False)

# (Any new monthly traffic file would be cleaned and appended here)

print("All Traffic Data Sent to SQL")
print("All the datasets are sent to SQL")




