from datetime import datetime


def my_decorator(func):
    def wrapper():
        print('start of decorator')
        func()
        print('end of the decorator')
    return wrapper()


# @my_decorator
# def say_yuppi():
#     print('yuppi!')
#
#
# # say_yuppi = my_decorator(say_yuppi)
#
# say_yuppi()

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
        else:
            pass

    return wrapper


def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper
@do_twice
# @not_during_the_night
def say_yuppi():
    print('Yuppi!')


say_yuppi()