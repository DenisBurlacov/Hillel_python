import csv
with open('SampleCSVFile_11kb.csv', 'r', encoding='utf-8', errors='ignore') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)