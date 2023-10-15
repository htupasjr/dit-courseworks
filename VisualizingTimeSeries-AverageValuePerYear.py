# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:30:29 2023

@author: Hermoso Tupas Jr.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# Read the dataset from the URL and parse the 'date' column as dates
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

# Group the data by year and calculate the average
yearly_avg = df.groupby(df['date'].dt.year)['value'].mean()
yearly_avg = yearly_avg.reset_index()
yearly_avg.columns = ['Year', 'Average Value']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg['Year'], yearly_avg['Average Value'], marker='o', linestyle='-')
plt.title('Yearly average of drug sales in Australia from 1992 to 2008')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.grid(True)

# Format x-axis labels as integers
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

plt.show()