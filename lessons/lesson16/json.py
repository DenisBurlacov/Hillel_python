import json

data = {
    'name': 'John',
    'age': 34,
    'city': 'New yourk'
}

json_sting = json.dumps(data)
print(json_sting)

json_object = json.loads(json_sting)

print(json_object)

name = json_object['name']
age = json_object['age']
print(name)
print(age)
