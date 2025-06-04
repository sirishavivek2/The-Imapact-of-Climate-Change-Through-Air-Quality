# -*- coding: utf-8 -*-
"""
Created on Sat May 10 13:00:37 2025

@author: Sirisha
"""
import pandas as pd

# Read in the file
climatechange = pd.read_csv('Climate_DataSet.csv')

# Print the first 5 rows
print("Initial Data Preview:")
print(climatechange[['CO_MA3', 'NO2_MA3', 'O3_MA3']].head())

# Show missing value counts before cleaning
print("\nMissing Values Before Cleaning:")
print(climatechange[['CO_MA3', 'NO2_MA3', 'O3_MA3']].isnull().sum())

# Calculate the mean of the columns
CO_MA3_mean = climatechange['CO_MA3'].mean()
NO2_MA3_mean = climatechange['NO2_MA3'].mean()
O3_MA3_mean = climatechange['O3_MA3'].mean()

# Fill missing values with the calculated means
climatechange['CO_MA3'] = climatechange['CO_MA3'].fillna(CO_MA3_mean)
climatechange['NO2_MA3'] = climatechange['NO2_MA3'].fillna(NO2_MA3_mean)
climatechange['O3_MA3'] = climatechange['O3_MA3'].fillna(O3_MA3_mean)

# Show missing value counts after cleaning
print("\nMissing Values After Cleaning:")
print(climatechange[['CO_MA3', 'NO2_MA3', 'O3_MA3']].isnull().sum())

# Print first few rows after cleaning
print("\nCleaned Data Preview:")
print(climatechange[['CO_MA3', 'NO2_MA3', 'O3_MA3']].head())
