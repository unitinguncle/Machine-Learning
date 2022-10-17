"""Problem 01 - Data Cleaning in Store Sales data
A popular Departmental store in Kentucky wants to clean their unstructured daily sales data. They are ready to freelance the data cleaning work. To select the right person for this task they are providing a sample data for cleaning. So this is your turn to prove yourself by cleaning the data to their expectations.

Create a noteook with detailed cleaning of the sales_data.csv """

# Your Code Here
import pandas as pd
import numpy as np
df = pd.read_csv('/content/sales_data - sales_data.csv.csv')


df['city'] = df['city'].fillna(method='ffill')
df['sale_number'] = df['sale_number'].fillna(df['sale_number'].median())
df['associate'] = df['associate'].fillna(df['associate'].mode()[0])
df
