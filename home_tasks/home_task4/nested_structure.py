# Створити 3 вимірний список (список 3х списків)
# Змінити, будь який, елемент, будь якого, спику.
# Вивести значення до та після

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(matrix)
matrix[0][0] = 10
print(matrix)

# Створити список зі вкладеним словником
list_with_dict = [1, 2, 3, 4, {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'}
                  ]

# Створити словник зі вкладеним списком
dict_with_nested_list = {
    'dict1': [1, 2, 3],
    'dict2': [4, 5, 6]
}

# Зберегти вкладений список зі словника у нову змінну
list_one_from_dict = dict_with_nested_list['dict1']
print(list_one_from_dict)