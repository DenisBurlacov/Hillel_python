import json

with open('sample2.json', 'r') as file:
    json_file = json.load(file)

    print(json_file) #вариант без Python Pretty Print
    print('\n')

    PrettyJson = json.dumps(json_file, indent=4, separators=(',', ': '), sort_keys=True)
    print(PrettyJson)