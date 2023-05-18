# Навести приклад простого рядка
string_single_quotes = 'Some string wit single quotes'
string_twice_quotes = "Some string with twice and one's quotes"

# Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)
haiky = """ 
    Luna de agosto.
En el portón irrumpe
    la marejada.
"""
haiky_editing = "\tLuna de agosto. \nEn el portón irrumpe\n\tla marejada."


# Навести приклад рядка з ігноруванням екрануючих символів (Raw)
raw_string = r'https://some/fake/url'


# Навести приклад форматування довгих рядків
long_sring = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum.'''

print(string_single_quotes)
print(string_twice_quotes)
print(haiky)
print(haiky_editing)
print()
print(raw_string)
print()
print(long_sring)