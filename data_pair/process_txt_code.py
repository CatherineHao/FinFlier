import pandas as pd
import csv

data  = []

file = pd.read_csv('./used_data/13_data_triple_top.csv')
# print(file.head())
file = file.to_dict(orient='records')
print(file)