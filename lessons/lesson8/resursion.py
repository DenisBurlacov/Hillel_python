def factorital(n):
    if n == 1:
        return n
    else:
        return n * factorital(n - 1)


print(factorital(11))


def get_some_data_from_user():
    name = input('enter some data; ')
    surname = input('Type your surname please ')
    age = input('How old are you? ')


get_some_data_from_user()