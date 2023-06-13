# 1. Написати лямбда функцію яка приймає один або 2 аргументи (другому задати значення за замовчуванням рівне 100,
# як у звичайних функціях) та друкує символ переданий як перший аргумент ту кількість раз яка вказана в другому
# аргументі, зробити можливим роботу фнкції не тільки з рядком а й з цифрами.

print_value = lambda first_arg, second_arg=100: print(str(first_arg) * second_arg)
print_value(5, 3)
print_value('some_text', 10)
print_value(3)
print_value('some_text')



# 2. Написати лямбда функцію яка приймає 2 числа як аргументи та повертає більше з них (використовуйте тернарний if)

max_num = lambda first_value, second_value: first_value if first_value > second_value else second_value

x = int(input('Please enter first num: '))
y = int(input('Please enter second num: '))
print(f'The max num from entered = {max_num(x, y)}')

# The variant with max function
# max_num = lamda first_value, second_value: max(first_value, second_value)



# 3. Написати лямбда функція яка нічого не приймає та завжди повертає 10.

return_ten = lambda: 10
print(return_ten())
