
import pandas as pd
# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')
# Convert 'Date' to datetime and forward fill
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce').ffill()
# Convert 'Time' and forward fill
climatechange['Time'] = pd.to_datetime(climatechange['Time'], format='%H:%M', errors='coerce').dt.time
climatechange['Time'] = climatechange['Time'].ffill()

# Impute numeric columns (only if sufficient data exists) using MEDIAN
cols_to_check = ['Temperature', 'Humidity', 'AirQualityIndex']
for col in cols_to_check:
    if climatechange[col].notnull().mean() > 0.3:
        climatechange[col] = climatechange[col].fillna(climatechange[col].median())
print("Rows & Columns:", climatechange.shape)
print("\nGeneral Info:")
print(climatechange.info())

# Summary statistics
print("\nSummary Statistics:")
print(climatechange[cols_to_check].describe())

# Individual stats for AirQualityIndex
col = 'AirQualityIndex'
print(f"\nIndividual Stats for {col}:")
print(f"Mean: {climatechange[col].mean():.2f}")
print(f"Median: {climatechange[col].median():.2f}")
print(f"Mode: {climatechange[col].mode()[0]:.2f}")
print(f"Std: {climatechange[col].std():.2f}")
print(f"Min: {climatechange[col].min():.2f}")
print(f"Max: {climatechange[col].max():.2f}")
print(f"25th Percentile: {climatechange[col].quantile(0.25):.2f}")
print(f"75th Percentile: {climatechange[col].quantile(0.75):.2f}")

# Check for missing values
print("\nMissing Values:")
print(climatechange.isnull().sum())

# Summary for categorical fields
print("\nSummary of Categorical Columns:")
print(climatechange[['Country', 'City', 'AQI Category']].describe(include='object'))
