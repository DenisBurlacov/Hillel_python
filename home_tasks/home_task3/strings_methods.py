# Показати роботу методів типу даних Рядок (на приклад .split(), .upper(), .lower(), .capitalize(), .find()*)

some_strange_stirg = "Some sTrinG ! WITH set ! of WoRDs"

print(some_strange_stirg.split())
print(some_strange_stirg.split("!"))
print(some_strange_stirg.upper())
print(some_strange_stirg.lower())
print(some_strange_stirg.capitalize())
print(some_strange_stirg.swapcase())
print(some_strange_stirg.count("o"))
print(some_strange_stirg.replace('!', '?'))
print(len(some_strange_stirg))
print(some_strange_stirg.find("W", 6, 15))
print(some_strange_stirg.endswith("s"))
print(some_strange_stirg.isalnum())
print(some_strange_stirg.isalpha())
print(some_strange_stirg.rjust(36, "-"))
print(some_strange_stirg.center(39, "-"))


