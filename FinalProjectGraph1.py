# -*- coding: utf-8 -*-
"""
Created on Sat May 10 17:42:34 2025

@author: Sirisha
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')
climatechange['Date'] = pd.to_datetime(climatechange['Date'], errors='coerce')
climatechange['AirQualityIndex'] = climatechange['AirQualityIndex'].fillna(climatechange['AirQualityIndex'].median())


# Bar plot of AQI categories
plt.figure(figsize=(8, 5))
sns.countplot(data=climatechange, x='AQI Category', order=climatechange['AQI Category'].value_counts().index)
plt.title("Count of Each AQI Category")
plt.xlabel("AQI Category")
plt.ylabel("Number of Observations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
