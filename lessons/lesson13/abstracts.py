import abc
from abc import ABC, abstractmethod


class HTTP(ABC):
    @abstractmethod
    def put(self):
        return

    @staticmethod
    @abstractmethod
    def my_abstract_static_method():
        pass

    @classmethod
    @abstractmethod
    def my_abstract_class_method(cls):
        return

    @property
    @abstractmethod
    def my_property(self):
        return

    @my_property.setter
    @abstractmethod
    def my_property(self, value):
        return

    @my_property.getter
    @abstractmethod
    def my_property(self):
        return

    @abstractmethod
    def _get_x(self):
        return

    @abstractmethod
    def _set_x(self, value):
        return

    x = property(_set_x, _get_x)


class NewHTTP(HTTP):

    def __init__(self):
        self.property = "my property"

    def put(self):
        return 'I\'m a put method'

    @property
    def my_property(self):
        return self.property

    @my_property.setter
    def my_property(self, value):
        if not isinstance(value, str):
            return "the value is not a string"
        self.property = value

    def _get_x(self):
        return self.x

    def _set_x(self, value):
        self.x = value

    def my_abstract_class_method(self):
        return

    def my_abstract_static_method(self):
        return

    def x(self):
        return self.x

        # print(http.put())


new_http = NewHTTP()
print(new_http.put())
print(new_http.my_property)
new_http.my_property = "new property value"
new_http.my_property = 10
print(new_http.my_property)

print(new_http.x(4))
print(new_http.x())