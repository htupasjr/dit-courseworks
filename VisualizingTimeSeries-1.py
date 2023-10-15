# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:27:47 2023

@author: Hermoso Tupas Jr.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from the URL and parse the 'date' column as dates
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

# Calculate and plot the average value per quarter
quarterly_avg = df.resample('Q', on='date')['value'].mean()
quarterly_avg = quarterly_avg.reset_index()

plt.figure(figsize=(10, 6))
plt.plot(quarterly_avg['date'], quarterly_avg['value'], marker='o', linestyle='-')
plt.title('Quarterly average of drug sales in Australia from 1992 to 2008')
plt.xlabel('Quarter')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()


#Workshop
# Plot average value per quarter
# Plot average value per year
# Plot average value every 3 years