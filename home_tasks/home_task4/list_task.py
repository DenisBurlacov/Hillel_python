import copy

# Створити простий список
my_list = [[1, 2, 3], [4, 5, 6]]

# Створити змінну з посиланням на перший список
my_list_copy = my_list

# Створити поверхову (Shallow copy) копію першого списка
shallow_copy = copy.copy(my_list)

# Створити глибоку (повну) (Deep copy) першого списка
deep_copy = copy.deepcopy(my_list)

# Вивести значення всіх списків
print(f'my first list = {my_list}')
print(f'copy of my first list = {my_list_copy}')
print(f'shallow copy of my first list {shallow_copy}')
print(f'deep copy of my first list {deep_copy}')
print()

# Змінити перший список і ще раз вивести значення всіх списків
print("=" * 50)
print()
my_list[1][0] = 'test'
print(f'my first list = {my_list}')
print(f'copy of my first list = {my_list_copy}')
print(f'shallow copy of my first list {shallow_copy}')
print(f'deep copy of my first list {deep_copy}')