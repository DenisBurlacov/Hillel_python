# 3. Створити конструкції try-except для арифметичної операції, роботи з колекціями.
def exception_one():
    while True:
        description = input(
            'The scrip divide first number on the second, if you wont to continue enter Y, if no, enter N: ')
        if description.lower() == 'n':
            print("Thanks bye!!!")
            break
        if description.lower() != 'y':
            continue
        num1 = int(input('Please enter num one: '))
        num2 = int(input('Please enter num two: '))

        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Yo have tried divide on zero")
        else:
            print(f'The result division firs num {num1} on the second {num2} = {result}')


def exception_two():
    try:
        user_num = int(input('Please enter the num of the user to find the id: '))
        _id_list = ['01', '99', '304']
        print(f'The user id is equal {_id_list[user_num]}')
    except IndexError:
        print('The user with this num doesnt exist')


run_exception = input('If you wont to check exception with division enter 1, or enter 2 to check exception with list: ')
if run_exception == '1':
    exception_one()
else:
    exception_two()