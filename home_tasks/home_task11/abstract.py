# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.
from abc import ABC, abstractmethod


class Some_class():

    @abstractmethod
    def some_funct(self):
        return 'value'


value = Some_class()
print(value.some_funct())


# 2.Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.

class My_abstract(ABC):
    @abstractmethod
    def return_value(self):
        return 'some sting'


_method = My_abstract()
print(_method.return_value())  # в данном случае получаем ошибку так как нельзя создать обьек от абстрактного класса.


# Для реализации необходими создать класс который наследуется от абстрактного класса и реализовать абстрактные методы

# class My_abstract1(My_abstract):
#     def return_value(self):
#         return 'some other sting'
#
#
# _method = My_abstract1()
# print(_method.return_value())

# 3. Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від
# абстрактного класу і створіть об'єкт нового класу.

class Abstract_class(ABC):
    @classmethod
    @abstractmethod
    def print_some_text(cls):
        pass


class Abstract_class1(Abstract_class):
    def print_some_text(self):
        print('The other some text')


class_obj = Abstract_class1()
class_obj.print_some_text()