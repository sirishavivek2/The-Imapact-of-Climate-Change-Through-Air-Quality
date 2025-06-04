# -*- coding: utf-8 -*-
"""
Created on Sat May 10 16:02:28 2025

@author: Sirisha
"""

import pandas as pd

# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')

# ---------------- BEFORE DATA CLEANING ----------------
print(" BEFORE Cleaning:")
print(climatechange[['Date', 'Time']].head())
print("\nData Types Before Cleaning:\n", climatechange.dtypes[['Date', 'Time']])

# ---------------- DATA TYPE CONVERSION ----------------
# Convert 'Date' column to datetime format
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')

# Convert 'Time' column to datetime.time format
# Let pandas infer the time format automatically (fixes NaT issues)
climatechange['Time'] = pd.to_datetime(climatechange['Time'], errors='coerce').dt.time

# ---------------- AFTER DATA CLEANING ----------------
print("\n AFTER Cleaning:")
print(climatechange[['Date', 'Time']].head())
print("\nData Types After Cleaning:\n", climatechange.dtypes[['Date', 'Time']])
