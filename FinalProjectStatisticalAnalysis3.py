# -*- coding: utf-8 -*-
"""
Created on Sat May 10 17:45:59 2025

@author: Sirisha
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')
climatechange['AirQualityIndex'] = climatechange['AirQualityIndex'].fillna(climatechange['AirQualityIndex'].median())
# Select numeric columns to check correlation
numeric_cols = ['Temperature', 'Humidity', 'Pressure', 'WindSpeed', 'AirQualityIndex']
corr = climatechange[numeric_cols].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Climate Variables")
plt.tight_layout()
plt.show()
