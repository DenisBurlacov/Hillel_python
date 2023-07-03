# import csv
#
# with open('config.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimitr=',', qoutechar='|')
#     for row in spamreader:
#         print(row)
import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'Valencia'],
    ['Alise', '32', 'London'],
    ['Bob', '43', 'Kyiv']
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer