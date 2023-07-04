# 1. Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.

import csv
with open('SampleCSVFile_11kb.csv', 'r', encoding='utf-8', errors='ignore') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)


# with open('SampleCSVFile_11kb.csv', newline='', encoding='utf-8', errors='ignore') as file:
#     reader = csv.reader(file, delimiter=' ', quotechar='|')
#     for row in reader:
#         print(', '.join(row))

# Оба рабочие варианты, второй из премера на занятии, добавил encoding='utf-8', errors='ignore' так как без этих
# параметров возмникает ошибка "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xae in position 265: invalid start byte"