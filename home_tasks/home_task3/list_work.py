# Створити файл де показати роботу зі списками
# створити список
my_list = [1, 2]

# копіювати через .copy()
my_list2 = my_list.copy()
print(my_list)

# додати елемент до списку.
my_list2.append(3)
my_list2.extend([5, 9])

# вставити елемент а певне місце. (Задача на використання методу .insert(), говорив, але
# не встиг показати) (Задача з зірочкою*)
my_list2.insert(3, 'string')

# додати один список до іншого 2 способами *
my_list3 = my_list + my_list2
for i in my_list3:
    my_list.append(i)

# команда .pop()
print(f'before method pop implemented {my_list}')
my_list.pop(0)
print(f'method pop {my_list}')

# видалити елемент за значенням і за індексом.
my_list.remove(3)
print(f'method remove {my_list}')
del my_list[0]
print(f'method del {my_list}')

# показати як дістати значення елемента за його індексом.
print(f'element in list with index 1 = {my_list[1]}')

print(my_list2)
print(my_list3)
