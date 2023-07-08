import csv
import pandas as pd
file_path = 'SampleCSVFile_11kb.csv'
fieldname = ['index', 'products', 'name', 'fourht', 'fifth', 'six', 'seventh', 'eights', 'nenths', 'ten']

# with open(file_path, 'r', encoding='cp1252') as file:
#     reader = csv.DictReader(file, fieldname)
#     for row in reader:
#         print(row)

df = pd.read_csv(file_path, encoding='cp1252')
print(df)


