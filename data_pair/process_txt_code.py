import pandas as pd
import csv

data  = []

file = pd.read_csv('./used_data/11_data_downtrend.csv')
# print(file.head())
file = file.to_dict(orient='records')
print(file)