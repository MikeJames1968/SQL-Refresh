# Mini project set by CoPilot after finishing PANDAS tutorial at openpython.org
# 
# UK Pub Sales Anlysis

# Task 1 - create dataset (done)

# Task 2 - cleaning

## Task 2A - load the csv file
import numpy as np
import pandas as pd
df = pd.read_csv("UK_Pub_Sales.csv")

# Task 2B - convert types
df['date'] = pd.to_datetime(df['date'])
df['sales'] = df['sales'].astype(float)
df['customers'] = pd.to_numeric(df['customers'], errors='coerce')
df['customers'] = df['customers'].astype('Int64')
df['food_served'] = df['food_served'] == 'yes'

# Task 2C - clean text

df['pub_name'] = df['pub_name'].str.strip()
df['town'] = df['town'].str.strip()
df['manager'] = df['manager'].str.strip()
df['notes'] = df['notes'].str.capitalize()
is_bool_type = df['food_served'].dtype in ['bool', 'boolean']
print('food served column is all True/False:', is_bool_type, '\n')

#Task 2E - handle missing / inconsistent data

df.loc[2, 'sales'] = None
df.loc[5, 'notes'] = ''

df.loc[df['sales'].isna(), 'sales'] = 0
df.loc[df['notes'] == '', 'notes'] = 'None'

# Task 2D - add calculated columns

df['sales_per_customer'] = df['sales'] / df['customers']
df['day_of_week'] = df['date'].dt.day_name()

# Task 3 - analysis

print('Total sales per pub')
print(df.groupby('pub_name')['sales'].sum())

print('\nAverage sale per day per town')
print(df.groupby('town')['sales'].mean().sort_values(ascending=False))

print('\nBest performing manager')
sales_by_mgr = df.groupby('manager')['sales'].sum().sort_values(ascending=False)
print('Manager:', sales_by_mgr.index[0])
print('Total sales: £', sales_by_mgr.iloc[0])

print('\nAverage sales when food served:', df[df['food_served']]['sales'].mean())
print('Average sales when food not served:', df[~df['food_served']]['sales'].mean())

print('\nOutliers')
print(df[df["sales"] > df["sales"].mean() + 2*df["sales"].std()])

# Task 4 - export results

# Task 4a  - export cleaned data to csv

cvfile = df.to_csv("UK_Pub_Sales_Cleaned.csv", index=False)

# Task 4b - export summary stats in JSON

summary = df.describe()
print(summary)
summary.to_json("UK_Pub_Sales_Summary.json", indent=4)

# Analysts summary after completing all tasks

# The Fox and Hound pub was the top performing pub in the dataset, with total sales of £3,800.75.
# Birmingham had the greatest average sales per day in the dataset, being £1,470.10
# The best performing manager was Mark Jones at the Fox and Hound pub (to be expected - no manager worked at 2 or more pubs)
# Serving food made only a small difference to average sales per day, £1,214.25 vs £1,423.40
# Sales data appears valid with no sales exceeding twice standard deviation
# The dataset is very small, comprising 3 pubs, in separate towns, over 3 days. There is no data for the Kings Arms on 3rd June