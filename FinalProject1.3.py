# -*- coding: utf-8 -*-
"""
Created on Sat May 10 16:00:16 2025

@author: Sirisha
"""
import pandas as pd
# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')
# ---------------- BEFORE CLEANING ----------------
print(" BEFORE CLEANING (First 5 Rows):")
print(climatechange[['Country', 'City', 'AQI Category']].head())

print("\nUnique Country Values (Before):")
print(climatechange['Country'].dropna().unique()[:10])  # Show sample

print("\nUnique City Values (Before):")
print(climatechange['City'].dropna().unique()[:10])

print("\nUnique AQI Categories (Before):")
print(climatechange['AQI Category'].dropna().unique())

# Standardize country names
climatechange['Country'] = climatechange['Country'].replace({
    'U.S.A': 'USA',
    'Usa': 'USA',
    'united states': 'USA',
    'Brazil ': 'Brazil',
    'poland': 'Poland',
    'france': 'France'
})
climatechange['Country'] = climatechange['Country'].str.strip().str.title()
# Standardize city names
climatechange['City'] = climatechange['City'].str.strip().str.title()
# Clean AQI Category from special characters
climatechange['AQI Category'] = climatechange['AQI Category'].str.replace(r'[^\w\s]', '', regex=True)


print("\n AFTER CLEANING (First 5 Rows):")
print(climatechange[['Country', 'City', 'AQI Category']].head())

print("\nUnique Country Values (After):")
print(climatechange['Country'].dropna().unique()[:10])

print("\nUnique City Values (After):")
print(climatechange['City'].dropna().unique()[:10])

print("\nUnique AQI Categories (After):")
print(climatechange['AQI Category'].dropna().unique())
