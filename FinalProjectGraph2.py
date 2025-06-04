# -*- coding: utf-8 -*-
"""
Created on Sat May 10 17:44:46 2025

@author: Sirisha
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')
climatechange['AirQualityIndex'] = climatechange['AirQualityIndex'].fillna(climatechange['AirQualityIndex'].median())

# Make sure 'Date' is in datetime format
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')

# Group by Date and compute average AQI
daily_aqi = climatechange.groupby('Date')['AirQualityIndex'].mean().reset_index()

# Line plot
plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_aqi, x='Date', y='AirQualityIndex')
plt.title("Daily Average Air Quality Index")
plt.xlabel("Date")
plt.ylabel("Air Quality Index")
plt.tight_layout()
plt.show()
