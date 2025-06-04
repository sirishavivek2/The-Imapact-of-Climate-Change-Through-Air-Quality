# -*- coding: utf-8 -*-
"""
Created on Sat May 10 15:04:50 2025

@author: Sirisha
"""
import pandas as pd

# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')

# Show data types and first few values of 'Date' and 'Time'
print("Before Cleaning:")
print(climatechange[['Date', 'Time']].head())
print("\nData types before cleaning:\n", climatechange.dtypes[['Date', 'Time']])

climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')

# Convert 'Time' to datetime.time format
climatechange['Time'] = pd.to_datetime(climatechange['Time'], format='%H:%M', errors='coerce').dt.time

# Show updated data and types
print("\nAfter Cleaning:")
print(climatechange[['Date', 'Time']].head())
print("\nData types after cleaning:\n", climatechange.dtypes[['Date', 'Time']])