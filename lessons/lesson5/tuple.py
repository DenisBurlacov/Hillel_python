var_tuple = (1, 2, 3, 4, 5)
print(var_tuple)
new_tuple = (1, 7, 8, 9, [1, 2, 4],)
print(new_tuple)
print(new_tuple[0])
new_tuple[4][0] = 10
print(new_tuple)
new_tuple[4].append(1)
print(new_tuple)

nested_tuple = new_tuple[3]

if 1 in new_tuple:
    print('1 is in the tuple:{}'.format(new_tuple))

print(new_tuple[len(nested_tuple) -1])