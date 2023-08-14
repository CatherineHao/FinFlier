import pandas as pd
import csv

data  = []

file = pd.read_csv('./yuzhe_data/23_data_uptrend.csv')
# print(file.head())
file = file.to_dict(orient='records')
print(file)