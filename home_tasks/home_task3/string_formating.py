# Створити файл де показати форматування рядків за допомогою '{}'.format() та f'{}'

first_name = input("Enter your first name: ")
last_mame = input("Enter your last name: ")
age = input("Enter your age: ")

print("Hello, my first name is " + first_name + ', ' + "last name " + last_mame + ", " + "and I'm " + age
      + " years old")
print(f"Hello, my first name is {first_name}, last name {last_mame}, and I'm {age} years old")
print("Hello, my first name is {}, last name {}, and I'm {} years old".format(first_name, last_mame, age))
print("Hello, my last name is {1}, firts name {0}, and I'm {2} years old".format(first_name, last_mame, age))


