# 1. Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
# які виводять в консоль відповідно, для методу wheels() -
# 4 та 8, а для методу mode_of_transport() - "Private usage", "Public usage".
# Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку та викликати ' \
# 'методи на кожному елементу списку.

class Car:
    def wheels(self):
        print('4 wheels')

    def mode_of_transport(self):
        print('Private usage')


class Bus:
    def wheels(self):
        print('8 wheels')

    def mode_of_transport(self):
        print('Public usage')


my_car = Car()
my_bus = Bus()

list_transports = [my_car, my_bus]
for i in list_transports:
    i.wheels()
    i.mode_of_transport()


# 2.Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.
class Vehicle():
    def desc(self):
        print("Some short information")

    def wheels(self):
        print('Numbers of wheels: ')


class Car(Vehicle):
    def desc(self):
        print('this is a car')

    def wheels(self):
        print('4 wheels')


class Bus(Vehicle):
    def desc(self):
        print('this is a bus')

    def wheels(self):
        print('8 wheels')


vehicle = Vehicle()
car = Car()
bus = Bus()

vehicle.desc()
vehicle.wheels()

car.desc()
car.wheels()

bus.desc()
bus.wheels()