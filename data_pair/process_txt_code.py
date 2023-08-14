import pandas as pd
import csv

data  = []

<<<<<<< HEAD
file = pd.read_csv('./used_data/13_data_triple_top.csv')
=======
file = pd.read_csv('./yuzhe_data/23_data_uptrend.csv')
>>>>>>> acf7e15a2a3d74bffeead05004446ce3e6bb4ed5
# print(file.head())
file = file.to_dict(orient='records')
print(file)