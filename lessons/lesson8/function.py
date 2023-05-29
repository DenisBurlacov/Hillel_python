def print_hi(name):
    print(f"Hi, {name}")


# if __name__ == '__main__':
#     print_hi("PyCharm")

_name = 'test'
_surname = 'surname'
_age = None


def print_hi():
    print(f'{_name}, {_surname}, {_age}')


def print_hi(_name, _surname, _age):
    print(_name)
    print(_surname)
    print(_age)
    print(f'{_name}{_surname} is {_age} years old')
    message = None
    if _age >= 60:
        message = 'You are a senior person'
    elif _age >= 18:
        message = 'You are an adult'
    else:
        message = 'Yor are kid'
    print(message)


print_hi('test', 'test3', 40)
print('-' * 30)
print_hi(_name='test', _surname='test', _age=10)
print('-' * 30)
print_hi(_age=34, _surname='test3', _name='test50')


def print_multiple_argument(*args, name, group):
    print(args)
    for i in args:
        print(i)
    print(name)
    print(group)


print_multiple_argument(1, 2, 3, 4, 5, 6, name='Test1', group='gdreout')


def print_multiple_args(name, *args, group):
    print(args)

    for i in args:
        print(i)


def kwords_print(**kwargs):
    print(kwargs)
    _keys = kwargs.keys()
    if 'name' in _keys:
        print(kwargs['name'])


kwords_print(name=_name, surname=_surname, ager=_age)


def args_and_kwards(*args, **kwargs):
    pass


args_and_kwards(1, 2, 3, 4, 54)

