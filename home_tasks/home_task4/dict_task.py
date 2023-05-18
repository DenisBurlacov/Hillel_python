import copy
# Створити пустий словник одним з наведених в лекції способів

my_dict = dict()

# Створити новий словник з 2-3 парами ключ:значення

my_personal_dict = {
    'first_name': 'Denis',
    'second_name': 'Burlakov',
    'id_card': 112323445
}

# Додати одну пару ключ:значення до першого словника
my_dict['new_key'] = 'new_value_in_empty_list'

# Додати до першого словника другий словник використовуючи .update()
my_personal_dict.update(my_dict)

# видалити один елемент словника за допомогою .pop()
my_personal_dict.pop('first_name')
print(my_personal_dict)

# Видалити один елемент за допомогою .popitem() метод работает по приципу последним пришел первым ушел
my_personal_dict.popitem()
print(my_personal_dict)

# Зробити глибоку копію першого словника в нову змінну
deep_copy_firt_list = copy.deepcopy(my_dict)
print(deep_copy_firt_list)

# Додати до нового словника новий ключ, а як значення передати перший словник
deep_copy_firt_list['key_my_dict'] = my_dict
print(deep_copy_firt_list)

# Вивести список ключів
print(deep_copy_firt_list.keys())

# Вивести список значень
print(deep_copy_firt_list.values())