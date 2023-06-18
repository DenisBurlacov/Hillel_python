# 1.Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних.
class TestIncap():
    def __init__(self):
        self._a = 1
        self.__a = 2


test = TestIncap()

print(test._a)
print(test._TestIncap__a)
print(test._a)