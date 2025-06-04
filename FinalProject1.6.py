# -*- coding: utf-8 -*-
"""
Created on Sat May 10 16:09:53 2025

@author: Sirisha
"""

import pandas as pd

# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')

# ---------------- BEFORE HANDLING MISSING DATA ----------------
print(" BEFORE Handling Missing Data:")
print("Missing values per column:\n")
print(climatechange.isnull().sum())
print("\nSample rows with missing values:")
print(climatechange[climatechange.isnull().any(axis=1)].head())

# ---------------- HANDLING MISSING DATA ----------------

# 1. Fill numeric columns with mean
numeric_cols = ['CO_MA3', 'NO2_MA3', 'O3_MA3', 'Temperature', 'Humidity', 'Pressure']
for col in numeric_cols:
    climatechange[col] = climatechange[col].fillna(climatechange[col].mean())

# 2. Fill categorical columns with mode
categorical_cols = ['Country', 'City', 'AQI Category']
for col in categorical_cols:
    climatechange[col] = climatechange[col].fillna(climatechange[col].mode()[0])

# Clean up Date and Time
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')
climatechange['Date'] = climatechange['Date'].ffill()

climatechange['Time'] = pd.to_datetime(climatechange['Time'], errors='coerce').dt.time
climatechange['Time'] = climatechange['Time'].ffill()


# ---------------- AFTER HANDLING MISSING DATA ----------------
print("\n AFTER Handling Missing Data:")
print("Remaining missing values per column:\n")
print(climatechange.isnull().sum())
