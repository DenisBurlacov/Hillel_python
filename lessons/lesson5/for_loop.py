_list = ['yra', 'variable', 'trancate']

for name in _list:
    print(name)
    if type(name) == str:
        for char in name:
            print(char)
    else:
        print("Variable name isn't string")

index = None
for key, name in enumerate(_list):
    print(key, name)
    if name == 'trancate':
        index = key
        break
print('index {}'.format(index))
print(_list[index])

for key, name in enumerate(_list):
    print(key, name)

for name in _list:
    print(name)

for i in range(1, len(_list)):
    print(i)
    print(_list[i])
