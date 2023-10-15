# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:54:17 2023

@author: Hermoso Tupas Jr.
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the dataset from the URL and parse the 'date' column as dates
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

# Set the 'date' column as the index
df.set_index('date', inplace=True)

# Decompose the time series into trend, seasonal, and residual components
decomposition = sm.tsa.seasonal_decompose(df['value'], model='additive')

# Plot the components
plt.figure(figsize=(12, 8))

plt.subplot(411)
plt.plot(df['value'], label='Original')
plt.legend(loc='best')
plt.title('Original Time Series')

plt.subplot(412)
plt.plot(decomposition.trend, label='Trend')
plt.legend(loc='best')
plt.title('Trend Component')

plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonal')
plt.legend(loc='best')
plt.title('Seasonal Component')

plt.subplot(414)
plt.plot(decomposition.resid, label='Residual')
plt.legend(loc='best')
plt.title('Residual Component')

plt.tight_layout()
plt.show()

