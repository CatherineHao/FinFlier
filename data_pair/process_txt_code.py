import pandas as pd
import csv
import json

data  = []

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
file = pd.read_csv('E:/CHI24/code/ECO_LLM_VIS/data_pair/used_data/25_data.csv')
# print(file.head())
file = file.to_dict(orient='records')
# with open("txt_7.txt","w") as f:
#     f.write(json.dumps(file))
print(file)
