# -*- coding: utf-8 -*-
"""
Created on Sat May 10 17:32:00 2025

@author: Sirisha
"""

import pandas as pd

# Load dataset
climatechange = pd.read_csv('Climate_DataSet.csv')

# Overview
print("Rows & Columns:", climatechange.shape)
print("\nGeneral Info:")
print(climatechange.info())

# Set display options
pd.set_option('display.max_columns', None)

# Summary stats for selected numeric columns
numeric_cols = ['Temperature', 'Humidity', 'AirQualityIndex']
print("\nSummary Statistics:")
print(climatechange[numeric_cols].describe())

# Individual stats for AirQualityIndex
print("\nIndividual Stats for AirQualityIndex:")
print(f"Mean: {climatechange['AirQualityIndex'].mean():.2f}")
print(f"Median: {climatechange['AirQualityIndex'].median():.2f}")
print(f"Mode: {climatechange['AirQualityIndex'].mode()[0]:.2f}")
print(f"Std: {climatechange['AirQualityIndex'].std():.2f}")
print(f"Min: {climatechange['AirQualityIndex'].min():.2f}")
print(f"Max: {climatechange['AirQualityIndex'].max():.2f}")
print(f"25th Percentile: {climatechange['AirQualityIndex'].quantile(0.25):.2f}")
print(f"75th Percentile: {climatechange['AirQualityIndex'].quantile(0.75):.2f}")

# Check for missing values
print("\nMissing Values:")
print(climatechange.isnull().sum())

# Descriptive stats for non-numeric columns
print("\nSummary of Categorical Columns:")
print(climatechange[['Country', 'City', 'AQI Category']].describe(include='object'))
