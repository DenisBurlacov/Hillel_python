class Page:
    """
    Some test

    """
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        print("Id of object {}".format(id(self)))

    def get_name(self):
        """
        Function tha return

        :return:
        """
        print(f'My name is {self.name}')

    def __str__(self):
        return f'this is calss Page thich contains variabe {self.name}'

    def __del__(self):
        del self
        Page.counter = -1



print("Page class objects counter {}".format())
a = Page("Den")
b = Page("Burlakov")

print(a)
print(a.print_name())
print('ID of object a {}'.format(id(a)))
print(b)
print(b.print_name())
print('ID of object a {}'.format(id(b)))
print(a.__doc__)


