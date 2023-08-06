import pandas as pd
import csv

data  = []

file = pd.read_csv('./7_data_rounding_bottom.csv')
# print(file.head())
file = file.to_dict(orient='records')
print(file)