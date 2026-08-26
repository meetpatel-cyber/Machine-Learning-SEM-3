# Pandas DataFrame functions are used to display rows, obtain information about the DataFrame, select columns and calculate statistical values.

import pandas as pd

df = pd.read_csv("YOUR CSV FILE")

# First 5 rows
print(df.head())

# First 2 rows
print(df.head(2))

# Last 5 rows
print(df.tail())

# Last 2 rows
print(df.tail(2))

# Complete information
df.info()

# Number of rows and columns
print(df.shape)

# Column names
print(df.columns)

# Single column
print(df.Age)

# Multiple columns
print(df[['Name', 'Age']])

# Mean
print(df.Age.mean())

# Median
print(df.Age.median())

# Mode
print(df.Age.mode())

# Variance
print(df.Age.var())

# Standard deviation
print(df.Age.std())