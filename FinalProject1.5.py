# -*- coding: utf-8 -*-
"""
Created on Sat May 10 16:08:36 2025

@author: Sirisha
"""
import pandas as pd

# Load the dataset
climatechange = pd.read_csv('Climate_DataSet.csv')

# ---------------- BEFORE REMOVING DUPLICATES ----------------
print("BEFORE Removing Duplicates:")
print(f"Total Rows: {climatechange.shape[0]}")
print(f"Duplicate Rows: {climatechange.duplicated().sum()}")
print("\nSample Duplicate Rows (if any):")
print(climatechange[climatechange.duplicated()].head())

# ---------------- REMOVE DUPLICATES ----------------
climatechange = climatechange.drop_duplicates()

# ---------------- AFTER REMOVING DUPLICATES ----------------
print("\nAFTER Removing Duplicates:")
print(f"Total Rows After Cleaning: {climatechange.shape[0]}")
print(f"Remaining Duplicates: {climatechange.duplicated().sum()}")

