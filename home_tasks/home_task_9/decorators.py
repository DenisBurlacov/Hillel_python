# 1. Напишіть програму на Python для створення ланцюжка декораторів функцій (bold, italic, underline etc.):
#    a. Декоратор make_bold(fn) приймає функцію та повертає рядок який починається з відповідного тегу конкатенується
#       із функцією та далі конкатенується з відповідним закриваючим тегом.
#    b. Декоратор make_italic(fn) приймає функцію та повертає рядок який починається з відповідного тегу конкатенується
#       із функцією та далі конкатенується з відповідним закриваючим тегом.
#    c. Декоратор make_underline(fn) приймає функцію та повертає рядок який починається з
#       відповідного тегу конкатенується із функцією та далі конкатенується з відповідним закриваючим тегом.
#    d. Результатом роботи, залежно від порядку декораторів, має бути подібний рядок - "<b><i><u>hello world</u></i></b>"

def make_bold(fn):
    def wrapper():
        return '<b>' + fn() + '</b>'

    return wrapper


def make_italic(fn):
    def wrapper():
        return '<i>' + fn() + '</i>'

    return wrapper


def make_underline(fn):
    def wrapper():
        return '<u>' + fn() + '</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def string_format():
    return 'hello world'


_some_sting = string_format()

result_comparison = "<b><i><u>hello world</u></i></b>"
assert _some_sting == result_comparison, f'Expected: {result_comparison}, got: {_some_sting}'

print(_some_sting)
