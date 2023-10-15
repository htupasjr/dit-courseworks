# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:08:02 2023

@author: Hermoso Tupas Jr.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from the URL and parse the 'date' column as dates
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

# Calculate the 3-year rolling average
rolling_avg = df.resample('3AS', on='date')['value'].mean()
rolling_avg = rolling_avg.reset_index()

plt.figure(figsize=(10, 6))
plt.plot(rolling_avg['date'], rolling_avg['value'], marker='o', linestyle='-')
plt.title('Average of sales every 3 years in Australia from 1992 to 2008')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
