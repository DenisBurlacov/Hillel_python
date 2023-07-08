import json
import pandas as pd
json_string = '{"name": "John", "age": 34, "city": "New yourk"}'

data = {
    'name': 'John',
    'age': 34,
    'city': 'New yourk'
}

json_data_string = json.dumps(data)
print(f'json_data_string: {json_data_string}')
print(f'json_data_string: {json_string}')

new_data = json.loads(json_string)
print(f'new_data: {new_data}')
print(type(new_data))
file_path = '../../home_tasks/home_task13/sample2.json'
with open('../../home_tasks/home_task13/sample2.json', 'r') as file:
    string = file.read()
print(string)

json_object = json.loads(string)
print(json_object)
print(type(json_object))

df = pd.json_normalize(json_object)

for row in df:
    print(row)
