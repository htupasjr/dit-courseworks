# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:26:38 2023

@author: Hermoso Tupas Jr.
"""

import pandas as pd

# Import as Dataframe
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

# caculate average value per quarter
def calc_quarterly_average(df):
    quarterly_avg = df.groupby(df['date'].dt.to_period('Q'))['value'].mean()
    quarterly_avg = quarterly_avg.reset_index()
    quarterly_avg.columns = ['Quarter', 'Quarterly Average']
    return quarterly_avg


# caculate average value per year
def calc_annual_average(df):
    yearly_avg = df.groupby(df['date'].dt.year)['value'].mean()
    yearly_avg = yearly_avg.reset_index()
    yearly_avg.columns = ['Year', 'Annual Average']
    return yearly_avg

# caculate average value every 3 years
def calc_3_year_average(df):
    yearly_avg = df.groupby(df['date'].dt.year)['value'].mean()
    yearly_avg = yearly_avg.reset_index()
    yearly_avg.columns = ['Year', 'Annual Average']
    
    # Calculate 3-year averages
    df_3_year = yearly_avg.copy()
    df_3_year['3-Year Average'] = yearly_avg['Annual Average'].rolling(window=3, min_periods=1).mean()
    
    return df_3_year

quarterly_avg = calc_quarterly_average(df)
annual_avg = calc_annual_average(df)
three_year_avg = calc_3_year_average(df)

print("\nQuarterly Averages:")
print(quarterly_avg)

print("Annual Averages:")
print(annual_avg)

print("\n3-Year Averages:")
print(three_year_avg)


 

