import pandas as pd
import csv

data  = []

file = pd.read_csv('./used_data/20_data.csv')
# print(file.head())
file = file.to_dict(orient='records')
print(file)