# Dictonary

dicttionary = {}

new_dictionary = dict()

new_dict = {
    'name': "Test",
    'surname': "burlakov",
    'age': 32
}

print(new_dict)

list_of_keys = new_dict.keys()
print(list_of_keys)

list_of_values = new_dict.values()
print(list_of_values)

list_of_items = new_dict.items()
print(list_of_items)

if 'name' in list_of_keys:
    print(new_dict['name'])


new_dict['key'] = 'multilock'

print(new_dict['key'])
print(new_dict)

new_dict.update({'new_key': "double mult"})
print(new_dict)

new_dict.clear()


